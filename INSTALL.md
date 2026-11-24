# REACH AI Vidio Studio — 安裝說明

本安裝包**不含任何 API Key**，也不含 `.env`、`.venv`、`data/`、`exports/`。

## 需求

- macOS（或 Linux）＋ Python 3.10 以上
- ffmpeg / ffprobe（影片合成與剪輯用；`brew install ffmpeg`）

## 安裝

1. 解壓縮到任意資料夾，例如 `~/REACH-AI-Vidio-Studio`
2. 雙擊 `install.command`（或終端機執行 `./install.command`）
   - 建立 `.venv`、安裝 `requirements.txt`
   - 由 `.env.example` 產生 `.env`（權限 600，金鑰欄位為空白）
3. 編輯 `.env`，在要用的供應商欄位填入你自己的金鑰
   （阿里雲 `ALIYUN_API_KEY`、火山方舟 `VOLC_API_KEY`、MiniMax `MINIMAX_API_KEY`；其餘選填，留空白即可）

## 啟動

雙擊 `start.command`（或 `./start.command`），瀏覽器開啟 <http://127.0.0.1:35350/>。
服務綁 `0.0.0.0:35350`，同網段其他裝置也能連；不想開放請在防火牆擋掉。

> 若 macOS 提示「無法打開，因為來自未識別的開發者」：在 Finder 對檔案按右鍵 → 打開，
> 或在終端機執行 `xattr -dr com.apple.quarantine .`。

## 地端影片伺服器（選填）

`deploy/server_ltx.py` 讀環境變數 `REACH_LTX_KEY`（未設定會拒絕啟動），
部署到 GPU 主機時請在該主機設定此變數，並在本機 `.env` 填相同值。
