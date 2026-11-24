#!/bin/bash
# REACH AI Vidio Studio — 啟動（macOS 可在 Finder 雙擊；終端機：./start.command）
set -euo pipefail
cd "$(dirname "$0")"

URL="http://127.0.0.1:35350/"

if [ ! -x .venv/bin/python ]; then
  echo "✗ 尚未安裝，請先執行 ./install.command"
  exit 1
fi
if [ ! -f .env ]; then
  echo "⚠ 找不到 .env：尚未設定任何 API Key，只能瀏覽介面（cp .env.example .env 後填入）"
fi

if [ "${NO_BROWSER:-0}" != "1" ] && command -v open >/dev/null 2>&1; then
  ( sleep 2; open "$URL" ) &
fi
echo "→ 啟動中：$URL （關閉此視窗或按 Ctrl+C 停止）"
exec .venv/bin/python app.py
