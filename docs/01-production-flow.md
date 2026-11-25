# 01 · 製作流程（對照參考平台）

> 參考：<https://www.oiioii.ai/oii-tv>、<https://www.oiioii.ai/zh-Hant/how-it-works>、
> <https://www.oiioii.ai/zh-Hant/features/canvas>

## 參考平台的七 Agent 流水線

| Agent | 職責 | 本專案的對應 |
| --- | --- | --- |
| 藝術總監 | 風格、色板、燈光、比例；按鏡頭挑模型 | `style` + `ratio` 全域設定；Provider/模型可逐鏡指定 |
| 編劇 | 劇本 → 場景、節拍、台詞 | `/api/projects`（一句話 → 四鏡模板）／`AI 重寫分鏡`（LLM 產六鏡 JSON） |
| 角色設計師 | 鎖臉型、服裝、比例 | `character_lock`（併入每鏡 Prompt） |
| 場景師 | 可重用場景、光線一致性 | `location_lock`（併入每鏡 Prompt） |
| 動畫師 | 分鏡 → 影片、鏡頭間連續性 | 逐鏡 `video` 任務（`/api/projects/<pid>/shots/<sid>/video`） |
| 剪輯師 | 時間軸、轉場 | 時間軸條（`/api/projects/<pid>` 的 `timeline`）；後製接 FFmpeg（見 05） |
| 音效師 | 配樂、音效、配音 | `/api/projects/<pid>/tts`（MiniMax TTS） |

## 本專案的流程

```text
一句話 + 風格 + 片長 + 比例 + 角色/場景鎖
        │  POST /api/projects
        ▼
四鏡模板（建立／衝突／轉折／收束）
  每鏡：景別、運鏡、動作、光線、正向 Prompt、負向 Prompt
        │  （可選）POST /api/projects/<pid>/script → LLM 重寫成六鏡
        ▼
逐鏡：生成關鍵影格（image）→ 生成影片（video task → 輪詢 → 下載 mp4）
        │
        ▼
配音（TTS）＋ 旁白文字
        │
        ▼
（後製）FFmpeg 接片 / 轉檔 / 抽封面 —— 與 REACH-AI-Motion-Studio 的 media 模組同規格
```

## 運鏡目錄（15 種，對應參考平台運鏡庫）

| key | 中文 | 參考平台 |
| --- | --- | --- |
| locked | 固定鏡頭 | 固定镜头 |
| pan / tilt | 左右搖／上下搖 | 左右摇、上摇/下摇 |
| dolly_in / dolly_out | 推軌前進／後退 | 前推、后移 |
| tracking | 跟拍 | 跟随拍摄 |
| crane | 升降 | 抬升/下降 |
| orbit_180 / orbit_360 | 環繞 | 环绕拍摄 |
| bullet_time | 子彈時間 | 环绕＋定格 |
| dolly_zoom | 柯克變焦 | 柯克变焦 |
| whip_pan | 甩鏡 | 快速摇镜 |
| pov / handheld | 第一視角／手持 | 第一视角、手持拍摄 |
| drone | 無人機 | 无人机／高空航拍 |

## 單鏡重生契約

- 每鏡獨立 `shot_id`（S01…），Prompt/運鏡可單獨改（`PATCH /api/projects/<pid>/shots/<sid>`）。
- 出圖、出片各自記錄在 `shot.image` / `shot.video`，不影響其他鏡。
- 影片任務失敗只影響該鏡（`job.state = error` + 原因）。

## 與參考平台的差異（刻意）

| 項目 | 參考平台 | 本專案 |
| --- | --- | --- |
| 執行位置 | 雲端平台、盒飯計費 | 本機控制台，直接打各家 API |
| 模型 | 平台代挑 25+ | 你指定 Provider/模型，能力與價格看 profile |
| 一致性 | 角色設計師 agent | `character_lock` + 同一模型 + 首幀參考（規劃中） |
| 審核 | 平台 UI | 每鏡人工檢查後才進下一鏡 |
