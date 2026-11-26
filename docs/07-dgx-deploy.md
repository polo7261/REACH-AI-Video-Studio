# 07 · DGX 單機部署清單

> **獨立架構**：一台 DGX 包辦全部——REACH 主服務＋ComfyUI＋Wan/LTX 生成服務，全部綁 `127.0.0.1`。
> **不包含** Mac 調度機、不指向 192.168.0.240（ComfyUI）、不指向 192.168.0.219（Wan/LTX）。
> **API 設定全新製作**：在 DGX 上另建 `.env`，金鑰另行申請／填入，不從 Mac 複製。

## 0. 架構

```
DGX（Ubuntu, aarch64/x86_64 均可）
├─ reach-video.service      :35350  REACH 主服務（網頁＋調度＋ffmpeg 合成）
├─ comfyui.service          :8188   ComfyUI（local-comfy provider → 127.0.0.1）
├─ reach-ltx.service        :35332  LTXV 2B（deploy/server_ltx.py）
└─ reach-wan.service        :35331  Wan2.2 TI2V-5B（server_wan.py，見步驟 4）

瀏覽器／其他裝置 ──HTTP──> http://<DGX IP>:35350
生成：雲端 API（需外連）＋ 本機 GPU（四服務同機互呼 localhost）
```

所有 provider 的 `base_url` 都用環境變數覆寫成 `127.0.0.1`——
`reach_video/config.py` 的預設值是 Mac 時期的 192.168.0.x，**部署時必須覆寫**。

## 1. 系統需求

| 項目 | 要求 |
|---|---|
| OS | Ubuntu 22.04 / 24.04（DGX OS 即可） |
| Python | 3.10 以上 |
| ffmpeg / ffprobe | `sudo apt install ffmpeg` |
| CUDA / 驅動 | `nvidia-smi` 正常（跑 ComfyUI 與 Wan/LTX 用） |
| 磁碟 | 模型資產 ≥ 100 GB（Wan 5B＋LTXV＋SDXL/Flux 權重） |
| 對外 | 開放 35350（網頁）；8188/35331/35332 僅本機，不用對外 |

## 2. 安裝 REACH

```bash
sudo apt update && sudo apt install -y git python3 python3-venv ffmpeg
git clone https://github.com/polo7261/REACH-AI-Video-Studio.git ~/reach
cd ~/reach && ./install.command        # 建 .venv 與 .env 範本
```

## 3. `.env`（全新製作，勿複製 Mac 的）

```ini
# ── 雲端 API（另外申請／填入自己的金鑰）──────────────
ALIYUN_API_KEY=
MINIMAX_API_KEY=
VOLC_PLAN_API_KEY=
VOLC_API_KEY=

# ── 地端服務全部指向本機（關鍵：覆寫預設的 192.168.0.x）──
REACH_WAN_BASE=http://127.0.0.1:35331
REACH_LTX_BASE=http://127.0.0.1:35332
COMFYUI_BASE_URL=http://127.0.0.1:8188

# ── 地端服務共用金鑰（REACH 與生成服務兩邊要一致）──────
REACH_WAN_KEY=<自訂>
REACH_LTX_KEY=<自訂>
COMFYUI_API_KEY=            # 選填

# ── 選填：LibTV（OAuth token，架構中）────────────────
LIBTV_ACCESS_TOKEN=
```

## 4. GPU 生成服務

**ComfyUI**
```bash
git clone https://github.com/comfyanonymous/ComfyUI.git ~/ComfyUI
cd ~/ComfyUI && pip install -r requirements.txt   # 建議獨立 venv
```
- 權重放入 `~/ComfyUI/models/…`；REACH 的模型清單＝`workflows/comfyui/*.json`
  （用 `~/reach/scripts/comfy_import.py` 匯入後出現在 `/api/comfy/models`）。

**LTXV 2B**
```bash
# 模型目錄：server_ltx.py 讀 ~/reach-image-gguf/models/ltxv-2b-diffusers
mkdir -p ~/reach-image-gguf/models/ltxv-2b-diffusers   # 放入 diffusers 權重
```

**Wan2.2 5B**
- `deploy/server_wan.py`（已從 219 取回並改成 vendor-neutral）＋ 相依模組 `deploy/reach_gpu.py`
  （跨行程 GPU 卡鎖：`fcntl`，POSIX，Linux 直接可用）。
- GPU 自動適配：NVIDIA CUDA（DGX）→ 原生 flash SDPA；AMD（gfx1030/gfx1100）→ 自動啟用
  chunked math SDPA。覆寫用環境變數：
  - `REACH_GPU_ARCH=nvidia|amd`（強制指定，預設自動偵測）
  - `REACH_SDPA_CHUNKED=1`（強制分塊）
  - `REACH_TEXT_ENCODER=auto|cpu|cuda`（umT5-xxl 放置：auto＝VRAM ≥32GB 上 cuda，否則 cpu）
  - `REACH_IMAGE_SERVER=1`（僅「影像服務同卡常駐」的舊 .219 拓撲需要；DGX 獨立卡不要設）
- 模型資產（放 DGX 的 `~/reach-image-gguf/models/`）：
  - `wan22/Wan2.2-TI2V-5B-Q4_0.gguf`（transformer，GGUF）
  - `wan22-diffusers/{text_encoder,vae,scheduler,tokenizer}`（umT5-xxl、Wan VAE 等）
  - 可從 219：`rsync -a X99:~/reach-image-gguf/models/wan22* ~/reach-image-gguf/models/`
- PyTorch 依 GPU 裝對版本：NVIDIA → CUDA wheel；AMD RX 7900 系（gfx1100）→ ROCm wheel
  （`--index-url https://download.pytorch.org/whl/rocm6.x`，7900 以上原生支援）。
- 未部署前不影響其他功能；`.env` 的 `REACH_WAN_BASE` 留著，服務啟動時才會用到。

## 5. systemd（四份）

`/etc/systemd/system/reach-video.service`：

```ini
[Unit]
Description=REACH AI Video Studio (DGX)
After=network-online.target
Wants=network-online.target

[Service]
User=<使用者>
WorkingDirectory=/home/<使用者>/reach
ExecStart=/home/<使用者>/reach/.venv/bin/python app.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

`/etc/systemd/system/comfyui.service`：

```ini
[Unit]
Description=ComfyUI (DGX)
After=network-online.target

[Service]
User=<使用者>
WorkingDirectory=/home/<使用者>/ComfyUI
ExecStart=/home/<使用者>/ComfyUI/.venv/bin/python main.py --listen 127.0.0.1 --port 8188
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

`/etc/systemd/system/reach-ltx.service`：

```ini
[Unit]
Description=REACH LTXV server (DGX)
After=network-online.target

[Service]
User=<使用者>
WorkingDirectory=/home/<使用者>/reach
EnvironmentFile=/home/<使用者>/reach/.env
ExecStart=/home/<使用者>/reach/.venv/bin/python deploy/server_ltx.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

`/etc/systemd/system/reach-wan.service`：同上，`ExecStart` 換成 server_wan.py（步驟 4 取回後）。

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now reach-video comfyui reach-ltx
```

## 6. 驗收清單

```bash
nvidia-smi                                      # GPU 正常
curl -s http://127.0.0.1:35350/ | head -3       # REACH 首頁
curl -s http://127.0.0.1:8188/system_stats      # ComfyUI
curl -s http://127.0.0.1:35332/health           # LTXV
curl -s http://127.0.0.1:35350/api/comfy/models # 模型清單非空（匯入 workflow 後）
```

- [ ] `/api/config` 內所有地端 provider 的 `base_url` 都是 `127.0.0.1`，**沒有** 192.168.0.x
- [ ] 從另一台裝置開 `http://<DGX IP>:35350`，建一個測試專案走完「角色 → 劇本 → 影格 → 影片」
- [ ] 本機 GPU 生成一筆（local-comfy 或 local-ltx）成功回片
- [ ] ffmpeg 合成（專案工作室 → 影片合成）成功輸出

## 7. 安全（上線前必做）

- [ ] REACH 網頁**目前無任何鑑別**——放到對外網段前，前面加 reverse proxy（nginx + basic auth / token）
- [ ] 防火牆只開 35350（與 22）；8188/35331/35332 綁 127.0.0.1 已天然不對外
- [ ] `.env` 權限 600（install.command 已處理）；不要把金鑰 commit 進 repo

## 8. 資料遷移（可選，預設全新）

舊專案要帶過去才做：`~/reach/data/`（專案＋媒體）與 `skill/`（技能庫）整包 rsync；
全新開始則跳過——首次啟動自動建目錄。
