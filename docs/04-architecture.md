# 04 · 架構

## 分層

```text
瀏覽器（工作室 / API 頁 / 文件頁）
        │ fetch JSON
        ▼
Flask app.py ────────────── 靜態：templates/、static/
        │
        ├── reach_video.pipeline   一句話 → 四鏡模板、運鏡目錄、Prompt 編譯（純函式）
        ├── reach_video.providers  三家真實呼叫（chat / image / tts / video task / poll）
        ├── reach_video.store      JSON 專案與任務（原子寫入、ID 白名單）
        └── reach_video.config     .env 載入、Provider/模型註冊表、金鑰遮罩
        │
        ▼
data/projects/<pid>.json   data/jobs/<jid>.json   data/media/<pid>/{S01-….jpg|mp4, narration-….mp3}
```

## 資料模型（專案 JSON）

```json
{
  "schema": "reach-vidio/plan@1",
  "id": "a1b2c3d4e5",
  "title": "雨夜霓虹追蹤",
  "idea": "一名少女在雨夜的霓虹街道上追逐一枚飄走的紙鶴",
  "style": "電影感寫實",
  "ratio": "16:9",
  "duration_seconds": 24,
  "character_lock": "短髮少女、米色風衣",
  "location_lock": "雨夜霓虹街道、積水反光",
  "shots": [
    {
      "id": "S01", "beat": "建立",
      "start_seconds": 0, "duration_seconds": 6,
      "framing": "wide establishing shot",
      "camera": "drone", "camera_zh": "無人機航拍",
      "action": "…", "lighting": "…",
      "positive_prompt": "…",
      "negative_prompt": "blurry, distorted hands, …",
      "image": "S01-abc123.jpg",
      "video": "S01-def456.mp4",
      "video_job": "0f1e2d3c4b5a",
      "status": "video_ready"
    }
  ],
  "narration": "…",
  "narration_audio": "narration-xyz.mp3"
}
```

## HTTP API

| 方法 | 路徑 | 說明 |
| --- | --- | --- |
| GET | `/api/config` | Provider、端點、模型狀態、金鑰遮罩 |
| POST | `/api/config/test` | `{"provider":"aliyun"}` → 真實文字測試 |
| GET | `/api/projects` | 專案列表＋最近任務 |
| POST | `/api/projects` | `{title, idea, style, duration, ratio, character, location}` |
| GET | `/api/projects/<pid>` | 專案＋時間軸 |
| PATCH | `/api/projects/<pid>/shots/<sid>` | 改 Prompt／運鏡／長度 |
| POST | `/api/projects/<pid>/script` | LLM 重寫成六鏡 |
| POST | `/api/projects/<pid>/shots/<sid>/image` | 出關鍵影格（存到 media） |
| POST | `/api/projects/<pid>/shots/<sid>/video` | 建影片任務 |
| GET | `/api/jobs/<jid>` | 輪詢任務；成功即下載 mp4 |
| POST | `/api/projects/<pid>/narration` | 存旁白文字 |
| POST | `/api/projects/<pid>/tts` | 生成配音 mp3 |
| GET | `/media/<pid>/<file>` | 靜態媒體 |
| GET | `/api/docs/<slug>` | 讀 docs/*.md |

## 安全邊界

- 只綁 `127.0.0.1`，不對外開放。
- 寫入請求要求 `X-Requested-With: fetch`（CSRF 防護，與 Image Studio 同慣例）。
- 專案/任務 ID 走白名單正則；媒體檔名擋 `..` 與路徑分隔。
- 金鑰只在 `.env`；`/api/config` 僅回遮蔽值。
- `data/`、`.env`、`.venv/` 已 gitignore。

## 與其他專案的關係

| 專案 | 關係 |
| --- | --- |
| `REACH-AI-Image`（35320） | **無關**：不共用 DB／埠／檔案；只在概念上共用「模型管理＋驗證」思路 |
| `REACH-AI-Motion-Studio` | 方法論來源：運鏡目錄、Prompt 編譯、FFmpeg 後製規格；本專案自帶簡化版 |
| `oiioii-研究/` | OiiOii 參考頁與實測截圖，本專案的流程藍本 |
