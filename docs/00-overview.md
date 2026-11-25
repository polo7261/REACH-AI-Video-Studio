# 00 · 總覽

REACH AI Video Studio — 本機影片工作室。把「一句話」變成可追蹤的影片專案：
**分鏡 → 關鍵影格 → 影片片段 → 配音 → 後製**。

- 網址：<http://127.0.0.1:35350/>
- 獨立於既有 `REACH-AI-Image`（35320），互不影響；不共用資料庫、不共用埠。
- 模型走雲端 API：阿里雲 MaaS（token-plan 閘道）、MiniMax、火山方舟。金鑰只存在本機 `.env`。
- 參考對象：參考平台的產品展示頁與其七 Agent 流水線設計。
- **分段流程**：① 角色設定圖（人工確認）→ ② 劇本＋分鏡 → ③ 關鍵影格 → ④ 影片 → ⑤ 後製。
  詳見 [`06-workflow-stages.md`](06-workflow-stages.md)。

## 頁面

| 路徑 | 用途 |
| --- | --- |
| `/` | 影片工作室：建專案、分鏡、逐鏡出圖／出片、配音 |
| `/api-page` | API 與網址：三家端點、模型狀態、金鑰遮罩、連線測試 |
| `/docs/` | 本文件（00–06） |

## 目前可用的能力（2026-11-21 實測）

| 能力 | Provider / 模型 | 狀態 |
| --- | --- | --- |
| 文字（劇本／分鏡） | Aliyun `qwen3.7-plus`、`glm-5.2`；MiniMax `MiniMax-M2.5` | ✅ 可用 |
| 出圖 | **火山 Agent Plan `doubao-seedream-5.5`**（預設）；標準 Ark `doubao-seedream-5-5-261028`；MiniMax `image-01` | ✅ 可用（已實測） |
| 配音 TTS | MiniMax `speech-2.5-hd-preview` | ✅ 可用 |
| 影片 | 火山 `doubao-seedance-2-5-flash-261115`（標準 Ark，待開通）；Agent Plan `doubao-seedance-2.5`（需 Large ¥500/月） | ⚠️ 未開通／套餐限制 |
| 影片（地端草稿） | **地端 LTXV 2B**（35332，`local-ltx`）：3s/20 步約 7–9 分鐘 | ✅ 可用（畫質限草稿） |
| 影片（備援） | MiniMax `MiniMax-Hailuo-02` | ⚠️ Token Plan 用量上限（2056） |
| 出圖／影片（阿里閘道） | `wan2.7-image`、`wan3.0-video` | ⚠️ 閘道路由回 `url error`，待確認正確路徑 |

## 檔案結構

```text
REACH-AI-Video-Studio/
├─ app.py                  # Flask（127.0.0.1:35350）
├─ reach_video/
│  ├─ config.py            # .env 載入、Provider/模型註冊表（含實測狀態）
│  ├─ providers.py         # 三家真實呼叫（chat/image/tts/video task）
│  ├─ pipeline.py          # 一句話 → 四鏡模板、運鏡目錄、Prompt 編譯
│  └─ store.py             # JSON 專案/任務儲存（原子寫入）
├─ templates/  static/     # 工作室 / API 頁 / 文件頁
├─ docs/                   # 本目錄
├─ data/                   # 專案、任務、媒體（不入版控）
└─ scripts/probe.py        # 三家能力探測（不印金鑰）
```

## 啟動

```bash
cd ~/REACH-AI-Video-Studio
.venv/bin/python app.py          # http://127.0.0.1:35350/
.venv/bin/python scripts/probe.py  # 重新探測三家能力
```
