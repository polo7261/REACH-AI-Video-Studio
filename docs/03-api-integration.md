# 03 · API 與網址

> 金鑰只放 `.env`（`chmod 600`），介面與日誌一律遮罩。以下只列端點與用法。

## 端點總表

| Provider | Base URL | 相容性 |
| --- | --- | --- |
| 阿里 MaaS 閘道 | `https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | OpenAI chat/completions |
| 阿里 Anthropic 閘道 | `https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic` | Anthropic messages |
| MiniMax（中國） | `https://api.minimaxi.com/v1` | 自家 REST |
| 火山方舟（標準，後付費） | `https://ark.cn-beijing.volces.com/api/v3` | OpenAI 相容（模型須開通） |
| **火山 Agent Plan（`ark-…` key）** | `https://ark.cn-beijing.volces.com/api/plan/v3` | 影片／圖片（`/contents/generations/tasks`、`/images/generations`） |
| 火山 Agent Plan（Anthropic） | `https://ark.cn-beijing.volces.com/api/plan` | `/v1/messages`（僅 Agent 工具） |

> ⚠️ Agent Plan 的 key **只在此專屬 base 有效**：拿去打 `/api/v3` 會 `InvalidEndpointOrModel.NotFound`；
> 標準 Ark key 打 `/api/plan/v3` 則回 `UnsupportedModel`／未授權。

## 本專案呼叫的端點

| 動作 | 方法與路徑 |
| --- | --- |
| 阿里／火山 文字 | `POST /chat/completions` |
| 阿里／火山 出圖 | `POST /images/generations` |
| 阿里／火山 影片建立 | `POST /videos/generations`（阿里）、`POST /contents/generations/tasks`（火山） |
| 火山 影片查詢 | `GET /contents/generations/tasks/{id}` |
| MiniMax 文字 | `POST /text/chatcompletion_v2` |
| MiniMax 出圖 | `POST /image_generation` |
| MiniMax 配音 | `POST /t2a_v2` |
| MiniMax 影片建立 | `POST /video_generation` |
| MiniMax 影片查詢 | `GET /query/video_generation?task_id=` |
| MiniMax 取檔 | `GET /files/retrieve?file_id=` |

## 環境變數（`.env`）

```ini
ALIYUN_BASE_URL=https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
ALIYUN_API_KEY=…（sk-sp-…）
ALIYUN_ANTHROPIC_URL=https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic
ALIYUN_IMAGE_MODEL=wan2.7-image
ALIYUN_TEXT_MODEL=qwen3.7-plus

MINIMAX_BASE_URL=https://api.minimaxi.com/v1
MINIMAX_API_KEY=…（sk-cp-…）
MINIMAX_TEXT_MODEL=MiniMax-M2.5
MINIMAX_TTS_MODEL=speech-2.5-hd-preview

VOLC_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
VOLC_API_KEY=…（UUID）
VOLC_IMAGE_MODEL=      # 填 ep-… endpoint id
VOLC_VIDEO_MODEL=      # 填 ep-… endpoint id
```

## 最小驗證指令

```bash
# 三家能力探測（不印金鑰）
.venv/bin/python scripts/probe.py

# 阿里文字
curl -s https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer $ALIYUN_KEY" -H "Content-Type: application/json" \
  -d '{"model":"qwen3.7-plus","messages":[{"role":"user","content":"hi"}]}'

# MiniMax 文字
curl -s https://api.minimaxi.com/v1/text/chatcompletion_v2 \
  -H "Authorization: Bearer $MINIMAX_KEY" -H "Content-Type: application/json" \
  -d '{"model":"MiniMax-M2.5","messages":[{"role":"user","content":"hi"}]}'
```

## 錯誤碼對照（實測遇到）

| 錯誤 | 意義 | 處理 |
| --- | --- | --- |
| `model_not_found`（阿里閘道） | 用了不在閘道清單的模型名 | `GET /models` 取清單 |
| `url error, please check url！`（阿里閘道） | 多模態路由未開或路徑不同 | 改用原生 DashScope key 或等閘道開通 |
| `InvalidApiKey`（dashscope 直打） | key 只綁閘道 | 不要直打 dashscope |
| `status_code 2069`（MiniMax） | 模型已下架 | 換 `MiniMax-M2.5` |
| `status_code 2056`（MiniMax） | Token Plan 用量上限 | 升級方案或買積分 |
| `InvalidEndpoint.ClosedEndpoint`（Ark） | endpoint 未開通/關閉 | 控制台建立 endpoint id |
| `InvalidEndpointOrModel.NotFound`（Ark） | 模型名不存在或無權限 | 用 `ep-…` |
