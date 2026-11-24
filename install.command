#!/bin/bash
# REACH AI Vidio Studio — 安裝（macOS／Ubuntu 共用）
#   macOS：Finder 雙擊，或終端機 ./install.command
#   Ubuntu／Debian：終端機 ./install.command（或 bash install.command）
# 只建立 .venv 與 .env 範本；不含任何 API Key，金鑰請自行填入 .env。
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
MIN_PY="3.10"

OS="$(uname -s)"
case "$OS" in
  Darwin) HINT_PY="brew install python（或 https://www.python.org/downloads/）"
          HINT_FFMPEG="brew install ffmpeg" ;;
  Linux)  HINT_PY="sudo apt install python3 python3-venv"
          HINT_FFMPEG="sudo apt install ffmpeg" ;;
  *)      HINT_PY="https://www.python.org/downloads/"
          HINT_FFMPEG="https://ffmpeg.org/download.html" ;;
esac
echo "✓ 系統：$OS"

if ! command -v "$PY" >/dev/null 2>&1; then
  echo "✗ 找不到 python3。請先安裝 Python ${MIN_PY}+：${HINT_PY}"
  exit 1
fi
if ! "$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
  echo "✗ 需要 Python ${MIN_PY} 以上，目前是 $("$PY" -V 2>&1)"
  echo "  可用 PYTHON=/path/to/python3.12 ./install.command 指定其他版本"
  exit 1
fi
echo "✓ $("$PY" -V 2>&1)"

for bin in ffmpeg ffprobe; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    echo "⚠ 找不到 ${bin}：影片合成／剪輯功能需要它（${HINT_FFMPEG}），其他功能不受影響"
  fi
done

# 既有 .venv 不完整（例如 Ubuntu 缺 python3-venv 時留下沒有 pip 的殘骸）就重建
if [ ! -x .venv/bin/python ] || ! .venv/bin/python -m pip --version >/dev/null 2>&1; then
  rm -rf .venv
  echo "→ 建立虛擬環境 .venv"
  if ! "$PY" -m venv .venv; then
    rm -rf .venv
    echo "✗ 建立 .venv 失敗"
    if [ "$OS" = Linux ]; then
      echo "  Ubuntu／Debian 請先：sudo apt install python3-venv（或對應版本的 python3.X-venv）"
    fi
    exit 1
  fi
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
     （Ubuntu 無桌面／SSH 連線：NO_BROWSER=1 ./start.command，常駐請見 INSTALL.md 的 systemd 段落）
MSG
