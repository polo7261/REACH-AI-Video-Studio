# 05 · 路線圖

## 現在（v0.2，已完成）

- [x] 一句話 → 四鏡分鏡（離線模板，可 LLM 重寫）
- [x] 逐鏡出圖（**火山 Seedream 5.5 已實測**；備援 MiniMax `image-01`）
- [x] 逐鏡影片任務（建立／輪詢／下載框架；**火山 Seedance 程式已就緒，模型待開通**）
- [x] 配音（MiniMax TTS，實測可跑）
- [x] API 與網址頁（端點、模型狀態、金鑰遮罩、連線測試）
- [x] 三家能力探測腳本 `scripts/probe.py` ＋ 方舟 55 模型清單探查

## 下一步

### A. 打通影片（只剩方案選擇）

| 路線 | 需要 | 現況 |
| --- | --- | --- |
| **標準 Ark 開通 Seedance** | 方舟「開通管理」開通 `Doubao-Seedance-2.5-flash`（後付費） | 程式已就緒，開通即通；測試單價最低 |
| **Agent Plan 升級 Large** | ¥500/月（250k AFP），含 Seedance 2.5 / 2.5-flash / 2.0 | 現有 Small/Medium 套餐**不支援影片** |
| MiniMax Hailuo | 升級 Token Plan 或買積分 | 錯誤碼 2056 |
| 阿里 Wan3.0 | 原生 DashScope key | 閘道路由不通 |
| 地端 Wan2.2 | 停 .219 的 Strata 釋放 VRAM | 免費但吃 17 GB 卡 |

### A2. 已完成

- [x] 火山 **Agent Plan**（`ark-…` key）接上：圖片 `doubao-seedream-5.5` 可用並設為預設，
      端點 `…/api/plan/v3/images/generations`；`/api-page` 可一鍵測試。
- [x] **地端 LTXV 2B** 打通：`server_ltx.py`（35332）＋網站 provider `local-ltx`；
      3s/12 步/704×384 實測 289 秒，成品自動下載回專案。可調 `steps`、`duration`。
      草稿可用；最終交付仍建議雲端。

### B. 一致性（角色不漂移）— 下一步優先

- [x] 角色階段：四視圖設定圖（Seedream 5.5）＋人工確認閘門；未確認不能產生劇本
- [x] 角色描述寫進每鏡英文 prompt（文字鎖）
- [x] **I2V 首幀一致性**：每鏡關鍵影格自動作為 `MiniMax-H3` 的 first_frame（實測 135–150 秒/鏡）
- [x] **圖像參考條件**：Seedream 5.5 接受 **data URI** 參考圖；關鍵影格已自動帶角色設定圖
- [ ] 驗收：三鏡臉部相似度評分（視覺模型打分或人工比對）

### B2. 已完成（2026-11-22）

- [x] 劇本／分鏡 LLM 階段（`qwen3.7-plus`），4 鏡約 60 秒
- [x] 台灣夜市專案：3 角色確認 → 4 鏡出圖 → 4 鏡 MiniMax 影片（75 秒完成）→ 24 秒成片

### C. 後製

- 接 FFmpeg：`concat`（正規化＋接片）、`transcode`（h264/h265、loudnorm）、
  `still`（封面）、`mix`（BGM 墊旁白）。規格沿用 `REACH-AI-Motion-Studio/motion_studio/media.py`。
- 目前工作：以 v0.1 產出逐鏡 mp4 後，用該模組的命令行接片。

### D. 音樂

- MiniMax `music-1.5` 未實測；需要時先跑一次 smoke test 再寫入註冊表。

## 刻意不做

- 不做多使用者／登入（本機單人工具）。
- 不內建任何金鑰；不把金鑰寫進前端。
- 不假裝「已生成」：模型失敗一律回報原始錯誤碼。
