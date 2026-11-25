#!/bin/bash
# REACH AI Video Studio — 啟動（macOS／Ubuntu 共用）
#   macOS：Finder 雙擊，或終端機 ./start.command
#   Ubuntu：./start.command；無桌面或 SSH 連線用 NO_BROWSER=1 ./start.command
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

# 開瀏覽器：macOS 用 open；Linux 只在有圖形桌面時用 xdg-open（Ubuntu 的 open 可能是 openvt）
OS="$(uname -s)"
OPENER=""
case "$OS" in
  Darwin) command -v open >/dev/null 2>&1 && OPENER="open" ;;
  Linux)  if [ -n "${DISPLAY:-}${WAYLAND_DISPLAY:-}" ] && command -v xdg-open >/dev/null 2>&1; then
            OPENER="xdg-open"
          fi ;;
esac
if [ "${NO_BROWSER:-0}" != "1" ] && [ -n "$OPENER" ]; then
  ( sleep 2; "$OPENER" "$URL" >/dev/null 2>&1 || true ) &
fi

# 區網網址（服務綁 0.0.0.0，同網段其他裝置可連）；取不到就不顯示
LAN_IP=""
case "$OS" in
  Darwin) LAN_IP="$(ipconfig getifaddr en0 2>/dev/null || true)" ;;
  Linux)  LAN_IP="$(hostname -I 2>/dev/null | awk '{print $1}' || true)" ;;
esac

echo "→ 啟動中：$URL （關閉此視窗或按 Ctrl+C 停止）"
if [ -n "$LAN_IP" ]; then
  echo "  區網：http://${LAN_IP}:35350/"
fi
exec .venv/bin/python app.py
