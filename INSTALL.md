# REACH AI Vidio Studio — 安裝說明（macOS／Ubuntu）

本安裝包**不含任何 API Key**，也不含 `.env`、`.venv`、`data/`、`exports/`。
同一份程式碼支援 macOS 與 Ubuntu／Debian；安裝包提供兩種格式，內容相同：

| 平台 | 安裝包 | 解壓縮 |
|---|---|---|
| macOS | `REACH-AI-Vidio-Studio-<版本>-<日期>.zip` | Finder 雙擊 |
| Ubuntu／Debian | `REACH-AI-Vidio-Studio-<版本>-<日期>.tar.gz` | `tar xzf <檔名>.tar.gz`（Ubuntu Server 預設沒有 `unzip`） |

## 需求

- Python 3.10 以上（Ubuntu 22.04＝3.10、24.04＝3.12、Debian 12＝3.11 皆可）
- ffmpeg / ffprobe（影片合成與剪輯用；沒裝其他功能照常）

## macOS

```bash
brew install python ffmpeg          # 若尚未安裝
```

1. 解壓縮到任意資料夾，例如 `~/REACH-AI-Vidio-Studio`
2. 雙擊 `install.command`（或終端機執行 `./install.command`）
3. 編輯 `.env` 填入金鑰（見下方「金鑰」）
4. 雙擊 `start.command`（或 `./start.command`），瀏覽器自動開啟 <http://127.0.0.1:35350/>

> 若 macOS 提示「無法打開，因為來自未識別的開發者」：在 Finder 對檔案按右鍵 → 打開，
> 或在終端機執行 `xattr -dr com.apple.quarantine .`。

## Ubuntu／Debian

```bash
sudo apt update
sudo apt install -y python3 python3-venv ffmpeg
tar xzf REACH-AI-Vidio-Studio-<版本>-<日期>.tar.gz
cd REACH-AI-Vidio-Studio
./install.command                   # 或 bash install.command
nano .env                           # 填入金鑰
NO_BROWSER=1 ./start.command        # 無桌面／SSH 連線；有桌面可省略 NO_BROWSER=1
```

- 缺 `python3-venv` 時 `install.command` 會提示並中止；補裝後重跑即可（會自動清掉不完整的 `.venv`）。
- 從其他機器連：`http://<主機 IP>:35350/`（啟動時會印出區網網址）。
  有開 ufw 防火牆請放行：`sudo ufw allow 35350/tcp`。
- 前景執行在 SSH 斷線時會一起結束；要常駐請用下方 systemd，或在 `tmux` 裡執行。

### 常駐服務（systemd，選用）

把 `<使用者>`、`<安裝路徑>` 換成實際值，存成 `/etc/systemd/system/reach-vidio.service`：

```ini
[Unit]
Description=REACH AI Vidio Studio
After=network-online.target
Wants=network-online.target

[Service]
User=<使用者>
WorkingDirectory=<安裝路徑>
ExecStart=<安裝路徑>/.venv/bin/python app.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now reach-vidio
journalctl -u reach-vidio -f        # 看 log
```

## 金鑰

`install.command` 會由 `.env.example` 產生 `.env`（權限 600，金鑰欄位為空白）。
在要用的供應商欄位填入你自己的金鑰：阿里雲 `ALIYUN_API_KEY`、火山方舟 `VOLC_API_KEY`、
MiniMax `MINIMAX_API_KEY`；其餘選填，留空白即可。

服務綁 `0.0.0.0:35350`，同網段其他裝置也能連；不想開放請在防火牆擋掉。

## 地端影片伺服器（選填）

`deploy/server_ltx.py` 讀環境變數 `REACH_LTX_KEY`（未設定會拒絕啟動），
部署到 GPU 主機時請在該主機設定此變數，並在本機 `.env` 填相同值。
