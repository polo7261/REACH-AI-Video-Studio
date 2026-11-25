# REACH AI Video Studio

一句話 → 分鏡 → 關鍵影格 → 影片 → 配音。本機影片工作室，獨立於 `REACH-AI-Image`。

- 工作室：<http://127.0.0.1:35350/>
- Skill 庫：<http://127.0.0.1:35350/skills/>（112 個 skill，`skill/<分類>/`，掛載用 API：`/api/skills`）
- API 與網址頁：<http://127.0.0.1:35350/api-page>
- 技術文件：<http://127.0.0.1:35350/docs/>（原始檔在 `docs/`）

## 啟動

```bash
cd ~/REACH-AI-Video-Studio
.venv/bin/python app.py
```

首次安裝（若 `.venv` 不存在）：

```bash
python3 -m venv .venv
.venv/bin/pip install flask waitress requests
cp .env.example .env   # 填入三家 API key
```

## 能力探測

```bash
.venv/bin/python scripts/probe.py            # 三家全部
.venv/bin/python scripts/probe.py minimax    # 單一
```

## 模型與金鑰

金鑰只存在 `.env`（`chmod 600`，已 gitignore）。端點與實測狀態見 `docs/02-model-matrix.md`
與 `/api-page`。

## 目錄

```text
app.py              Flask 入口（127.0.0.1:35350）
reach_video/        config / providers / pipeline / store
templates/ static/  工作室、API 頁、文件頁
docs/               技術文件（00–05）
scripts/probe.py    三家能力探測
data/               專案、任務、媒體（不入版控）
```
