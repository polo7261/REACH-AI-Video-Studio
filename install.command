#!/bin/bash
# REACH AI Vidio Studio — 安裝（macOS 可在 Finder 雙擊；終端機：./install.command）
# 只建立 .venv 與 .env 範本；不含任何 API Key，金鑰請自行填入 .env。
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
MIN_PY="3.10"

if ! command -v "$PY" >/dev/null 2>&1; then
  echo "✗ 找不到 python3。請先安裝 Python ${MIN_PY}+（brew install python 或 https://www.python.org/downloads/）"
  exit 1
fi
if ! "$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
  echo "✗ 需要 Python ${MIN_PY} 以上，目前是 $("$PY" -V 2>&1)"
  exit 1
fi
echo "✓ $("$PY" -V 2>&1)"

for bin in ffmpeg ffprobe; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    echo "⚠ 找不到 ${bin}：影片合成／剪輯功能需要它（brew install ffmpeg），其他功能不受影響"
  fi
done

if [ ! -x .venv/bin/python ]; then
  echo "→ 建立虛擬環境 .venv"
  "$PY" -m venv .venv
fi
echo "→ 安裝相依套件（requirements.txt）"
.venv/bin/python -m pip install -q -r requirements.txt

if [ ! -f .env ]; then
  # 佔位值清成空白：程式以「非空」判定已設定，留 REPLACE_ME 會誤顯示為已設定
  sed 's/=REPLACE_ME$/=/' .env.example > .env
  chmod 600 .env
  echo "✓ 已建立 .env（權限 600）——金鑰欄位為空白，請填入你自己的 API Key"
else
  echo "✓ 保留既有 .env"
fi
mkdir -p data

cat <<'MSG'

安裝完成。
  1. 編輯 .env，填入要用的 API Key（不用的供應商留空白即可）
  2. 執行 ./start.command 啟動 → http://127.0.0.1:35350/
MSG
