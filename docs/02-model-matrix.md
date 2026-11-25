# 02 · 模型與能力矩陣

實測日期：2026-11-21。狀態定義：**已實測**＝真實呼叫成功；**額度上限**＝認證/路由正常但方案受限；
**未打通**＝路由或 endpoint 待確認。

## 阿里雲 MaaS（token-plan 閘道，OpenAI 相容）

Base：`https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`
Anthropic 相容：`https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic`

| 模型 | 類型 | 狀態 | 備註 |
| --- | --- | --- | --- |
| `qwen3.7-plus` | text | ✅ 已實測 | 寫稿／分鏡 |
| `glm-5.2` | text | ✅ 已實測 | 回覆 READY |
| `qwen3.6-flash` | text | ✅ 已實測 | 速度優先 |
| `qwen3.8-max` / `qwen4-max` | text | 未實測 | 更高階 |
| `deepseek-v4-pro` | text | 未實測 | — |
| `wan2.7-image` / `wan2.7-image-pro` | image | ⚠️ 未打通 | `POST /images/generations` 回 `url error` |
| `qwen-image-3.0-pro` | image | ⚠️ 未打通 | 同上 |
| `wan3.0-video` | video | ⚠️ 未打通 | `/videos/generations` 回 `url error` |
| `qwen-audio-3.0-tts-plus` | tts | 未實測 | 路由待確認 |
| `qwen-audio-3.0-asr-flash` | asr | 未實測 | 語音轉文字 |

閘道 `/models` 回傳 23 個模型（含 `auto`、`decision-model-preview`）。
⚠️ 這把 key **只在閘道有效**：直打 `dashscope.aliyuncs.com` 會 401 `InvalidApiKey`。

## MiniMax（中國站）

Base：`https://api.minimaxi.com/v1`

| 模型 | 類型 | 狀態 | 備註 |
| --- | --- | --- | --- |
| `MiniMax-M2.5` | text | ✅ 已實測 | `base_resp.status_code=0`；`M2`/`M2.1`/`Text-01` 已下架（2069） |

> **Key 類型**：`sk-cp-…` = Coding Plan（只給文字/圖片/TTS；影片回 2056）；
> `sk-api-…` = 一般 API 金鑰（影片可用）。中國站 `api.minimaxi.com` 與國際站 `api.minimax.io` 帳戶不互通。
| `image-01` | image | ✅ 已實測 | 回 `data.image_urls[]` |
| `image-01-live` | image | ✅ 已實測 | — |
| `speech-2.5-hd-preview` | tts | ✅ 已實測 | 回 base64 mp3（實測 27 KB） |
| **`MiniMax-H3`** | video | ✅ **已實測**（v2 介面） | 5 秒 768P ≈ **91 秒**；1344×768、**自帶 AAC 音軌**；支援首幀／尾幀／參考圖 |
| `MiniMax-H3-Highspeed` / `-Lite` / `-Max` | video | 未實測 | 480P/768P（Max 5–15 秒） |
| `MiniMax-Hailuo-02` / `T2V-01` / `I2V-01` | video | ✅ 已實測 | 6 秒 768P ≈ 284 秒；無音軌；`I2V-01` 不穩（Preparing 10 分鐘後 Fail） |

> **H3 走 v2 介面**：建立 `POST /v2/video_generation`（`content[]` 多模態、`generate_audio` 預設 true）；
> 查詢是**路徑參數** `GET /v2/query/video_generation/{task_id}` — 用 query string 會忽略 task_id 回傳清單（曾誤下載別支影片）。
> H3 為後付費，餘額不足回 `1008 insufficient balance`（與 Coding Plan 的 2056 不同）。
| `music-1.5` | music | 未實測 | — |

## 地端 Wan2.2（192.168.0.219:35331）

服務：`reach-wan.service`（`~/reach-image-gguf/server_wan.py`，Flask + waitress）
模型：Wan2.2 **TI2V-5B**（GGUF，diffusers）｜24 fps｜20 steps｜guidance 5.0｜可負向提示詞
行為：**lazy load、每支跑完卸載**（不常駐 VRAM）；生成為**同步**呼叫

| 端點 | 說明 |
| --- | --- |
| `GET /health` | `{status: loading/ready/unloaded, error, loaded_at}` |
| `POST /v1/videos/generations` | Bearer key；body：`prompt`(必填)、`negative_prompt`、`duration`、`ratio`(16:9/9:16/1:1/4:3)、`resolution`(720P/1080P)、`seed`、`guidance`；回 `data[{url, frames, fps, seconds, width, height, seed, elapsed_s}]` |
| `GET /files/videos/<name>` | 下載 mp4 |
| `GET /v1/videos/progress/<request_id>` | 生成進度 |

實測數據：模型載入 ~10 秒、佔 **5.1 GB VRAM**（TI2V-5B）；6 秒 720P 生成數分鐘。
本站在鏡頭的「生成影片」下拉選 **地端 Wan（219）**；背景執行緒處理，完成自動下載 mp4。

**GPU 共享限制**：卡片 15.98 GiB。此服務會請生圖伺服器（35330）先卸載，
但**不會**協調 Strata（Qwen3.8，佔 16.3 GB）— 出片前必須先停 Strata。

## 地端 LTXV 2B（192.168.0.219:35332）

服務：`server_ltx.py`（`~/reach-image-gguf/`，Flask + waitress；由 `REACH-AI-Video-Studio/deploy/server_ltx.py` 部署）；啟動前須設定環境變數 `REACH_LTX_KEY`（與本機 `.env` 同值）
模型：**LTXV 2B**（`Lightricks/LTX-Video` diffusers 格式，transformer 28 層 / hidden 2048）
設定：24 fps｜步數預設 20（可由 `steps` 覆寫 4–40）｜guidance 3.0｜解析度 704×400（16:9）
行為：lazy load、每支後卸載；API 形狀**與 Wan 服務相同**（`/v1/videos/generations`、`/health`、`/files/videos/…`）

| 對比 | Wan2.2 TI2V-5B（35331） | LTXV 2B（35332） |
| --- | --- | --- |
| 參數量 | 5B | 2B |
| 實測速度 | ❌ 第 1 步 8 分鐘（gfx1030 無 CK 卷積） | ✅ **3s / 12 步 / 704×384 = 289 秒**（含載入；約 20 秒/步） |
| 畫質 | 未完成測試 | 12 步偏糊、彩色溢出；**建議 20–25 步**（3s ≈ 7–9 分鐘） |
| VRAM | 5.1 GB | 權重 15 GB → 需 `enable_model_cpu_offload` + VAE tiling + attention slicing |
| 用途 | I2V/T2V、畫面細膩 | 草稿、運鏡驗證（不適合最終交付） |

**參數配方（實測有效）**：`768×448`、`24 steps`、`guidance 5.0`、**英文短 prompt**。
- 3 秒（73 幀）＝ **438 秒**（約 7.3 分鐘，含載入）
- 4 秒（97 幀）＝ **630 秒**（約 10.5 分鐘）→ 線性約 **6.5 秒/幀**，6 秒片 ≈ 16 分鐘
- 12 步 / 384p / 中文混合長 prompt → 糊成抽象色塊（不要用）

實測限制：`height/width` 必須被 32 整除；`callback_on_step_end` 必須回傳 dict；
3 秒 = 73 幀（`round(sec*24/8)*8+1`）；輸出 h264、288 KB（768×448）。

> 同一個 16 GB 卡只能同時跑一個影片服務；生成前確認 Strata（8080）已停用。

## 火山方舟 **Agent Plan**（`ark-…` 專屬 key）

專屬 Base URL：`https://ark.cn-beijing.volces.com/api/plan/v3`（影片／圖片）
Anthropic 相容：`https://ark.cn-beijing.volces.com/api/plan`（`/v1/messages`）

| 模型 | 類型 | 狀態 | 備註 |
| --- | --- | --- | --- |
| `doubao-seedream-5.5` | image | ✅ **已實測** | 200，回圖片 URL；本站**預設出圖** |
| `doubao-seedream-5-0-pro` | image | 未實測 | Small 以上可用 |
| `doubao-seedream-5.0-flash` | image | 未實測 | Small 以上可用 |
| `doubao-seedance-2.5` | video | ⚠️ 套餐限制 | `UnsupportedModel`：影片僅 **Large / Max** 套餐 |
| `doubao-seedance-2.5-flash` | video | ⚠️ 套餐限制 | 同上 |
| `doubao-seedance-2.0` / `-fast` / `-mini` | video | ⚠️ 套餐限制 | 同上 |
| `doubao-seed-2.1-pro` | text | 條款限制 | Agent 工具專用；**不可**用於一般 API |

套餐額度（AFP）：Small 40 元/月（20k）、Medium 200（100k）、**Large 500（250k）**、Max 1000（500k）。
影片模型只在 **Large / Max**；圖片模型 Small 起就有。

> 條款提醒：Agent Plan 的文字／向量模型「不可用於 API 呼叫」（非 Agent 工具使用可能被判濫用）。
> 本站的劇本／分鏡文字仍走阿里雲或 MiniMax。

## 火山方舟 Ark（標準 API Key，後付費）

Base：`https://ark.cn-beijing.volces.com/api/v3`
Key：`GET /api/v3/models` 回 **55 個**可存取模型（含 domain 與 `api_supported`）。
**重點：可存取 ≠ 已開通** — 未開通者呼叫會回 `ModelNotOpen`，需先在方舟控制台「開通管理」開通。

| 模型 | 類型 | 狀態 | 備註 |
| --- | --- | --- | --- |
| `doubao-seedream-5-5-261028` | image | ✅ **已實測** | 200，回 1024×1024 PNG（1.6 MB）；本站出圖預設 |
| `doubao-seedream-5-0-flash-260915` | image | 未實測 | 已可存取 |
| `doubao-seedream-5-0-pro-260628` | image | 未實測 | 已可存取 |
| `doubao-seedream-4-5-251128` | image | 未實測 | 已可存取 |
| `doubao-seedance-2-5-flash-261115` | video | ⚠️ 未開通 | `ModelNotOpen`：控制台開通後即可用（本站預設影片模型） |
| `doubao-seedance-2-5-260628` | video | ⚠️ 未開通 | 同上 |
| `doubao-seedance-2-0-mini-260615` | video | ⚠️ 未開通 | 同上 |
| `doubao-seedance-2-0-fast-260128` | video | ⚠️ 未開通 | 同上 |
| `doubao-seed-2-1-pro-260915` | text | ⚠️ 未開通 | 同上 |
| `deepseek-v4-pro-ga-260813` | text | ⚠️ 未開通 | 同上 |
| `glm-5-3-flash-260828` | text | ⚠️ 未開通 | 同上 |
| `kimi-k3-1-pro-261024` | text | 未實測 | 已可存取 |

### 開通步驟（僅能在控制台操作，API 無法代開）

1. 開 <https://console.volcengine.com/ark>
2. 左側「開通管理」→ 找到 `Doubao-Seedance-2.5-flash`（或 2.5 / 2.0 mini）→ 開通
3. 回到本站按「生成影片」即可（程式與預設模型已就緒）

其他可用模型（同一把 key 可見）：`doubao-seed3d-2-0-260328`（3D）、
`doubao-embedding-vision-*`（向量）、`qwen3-32b`、`glm-4-5-air` 等。

## 建議分工（目前可跑）

| 層 | 主力 | 備援 |
| --- | --- | --- |
| 文字 | Aliyun `qwen3.7-plus` | MiniMax `MiniMax-M2.5` / Aliyun `glm-5.2` |
| 出圖 | MiniMax `image-01` | 阿里 `wan2.7-image`（待打通）／地端 Qwen-Image |
| 配音 | MiniMax `speech-2.5-hd-preview` | 阿里 `qwen-audio-3.0-tts-plus`（待打通） |
| 影片 | 待打通（MiniMax 額度／Ark endpoint／阿里路由） | 地端 Wan2.2（192.168.0.219:35331，需先啟動） |
| 音樂 | MiniMax `music-1.5`（未實測） | — |

## 已知限制

- MiniMax 影片需升級 Token Plan 或購買積分（錯誤碼 2056）。
- 阿里閘道的多模態路由與原生 DashScope 不同；若要用 Wan/Seedream，建議在阿里雲開通
  **原生 DashScope key**（`dashscope.aliyuncs.com` 走 `/api/v1/services/aigc/...` 非同步任務）。
- 火山方舟需 endpoint id，不是模型名稱。
