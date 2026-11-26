#!/bin/bash
# REACH AI Video Studio — Server 版安裝（macOS／Linux）
# 公司行號集中部署：App 跑在公司內網一台伺服器，員工瀏覽器連 http://<server-ip>:<port>
#   個人使用請用 install.command（單機版）
# 用法（在解壓後的包根目錄執行）：
#   bash install_server.sh [--port 35350] [--service] [--uninstall]
#   --port N     監聽埠（寫入 .env 的 REACH_PORT；預設 35350）
#   --service    註冊開機自啟服務（Linux: systemd；macOS: launchd）
#   --uninstall  移除已註冊的服務
set -euo pipefail
cd "$(dirname "$0")"
[[ -f app.py ]] || [[ -f ../app.py ]] && cd ..   # 從 scripts/ 子目錄執行時回包根

PORT=35350
WITH_SERVICE=0
UNINSTALL=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --port) PORT="$2"; shift 2 ;;
    --service) WITH_SERVICE=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    *) echo "未知參數：$1"; exit 1 ;;
  esac
done

banner() {
  cat <<'EOF'
╔═══════════════════════════════════════════════════════╗
║  REACH AI Video Studio — Server 版安裝                ║
║  公司行號集中部署：跑在公司內網伺服器，員工共用        ║
║  個人單機使用請改用 install.command（單機版）          ║
╚═══════════════════════════════════════════════════════╝
EOF
}
banner

die() { echo "❌ $*" >&2; exit 1; }
OS="$(uname -s)"
SVC_NAME="reach-ai-video"
SUDO=""; [[ "$(id -u)" == 0 ]] || SUDO="sudo"
PY="${PYTHON:-python3}"
MIN_PY="3.10"

# ---------- uninstall ----------
if [[ "$UNINSTALL" == 1 ]]; then
  if [[ "$OS" == Linux ]]; then
     $SUDO systemctl stop "$SVC_NAME" 2>/dev/null || true
     $SUDO systemctl disable "$SVC_NAME" 2>/dev/null || true
     $SUDO rm -f "/etc/systemd/system/$SVC_NAME.service"
     $SUDO systemctl daemon-reload
    echo "✓ 已移除 systemd 服務 $SVC_NAME"
  else
    launchctl bootout "gui/$(id -u)" "$HOME/Library/LaunchAgents/com.sky.$SVC_NAME.plist" 2>/dev/null || true
    rm -f "$HOME/Library/LaunchAgents/com.sky.$SVC_NAME.plist"
    echo "✓ 已移除 launchd 服務 com.sky.$SVC_NAME"
  fi
  exit 0
fi

# ---------- 前置檢查 ----------
[[ -f app.py ]] || die "請在解壓後的包根目錄執行（找不到 app.py）"
if ! command -v "$PY" >/dev/null 2>&1; then
  [[ "$OS" == Darwin ]] && HINT="brew install python" || HINT="sudo apt install python3 python3-venv"
  die "找不到 python3（${MIN_PY}+）：$HINT"
fi
"$PY" -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" \
  || die "需要 Python ${MIN_PY}+，目前 $("$PY" -V 2>&1)；可用 PYTHON=/path/to/python3 指定"
for bin in ffmpeg ffprobe; do
  command -v "$bin" >/dev/null 2>&1 || echo "⚠ 缺 ${bin}：影片合成功能不可用（其他不受影響）"
done
echo "✓ $("$PY" -V 2>&1)  系統：$OS"

# ---------- venv＋依賴 ----------
if [ ! -x .venv/bin/python ] || ! .venv/bin/python -m pip --version >/dev/null 2>&1; then
  rm -rf .venv
  echo "→ 建立虛擬環境 .venv"
  "$PY" -m venv .venv || die "建立 .venv 失敗（Linux 請先：sudo apt install python3-venv）"
fi
echo "→ 安裝相依套件"
.venv/bin/python -m pip install -q -r requirements.txt

# ---------- .env（含 REACH_PORT）----------
if [ ! -f .env ]; then
  sed 's/=REPLACE_ME$/=/' .env.example > .env
  chmod 600 .env
  echo "✓ 已建立 .env（權限 600）——金鑰請填公司採購的 API Key"
else
  echo "✓ 保留既有 .env"
fi
if grep -q "^REACH_PORT=" .env; then
  sed -i.bak "s/^REACH_PORT=.*/REACH_PORT=$PORT/" .env && rm -f .env.bak
else
  printf "\nREACH_PORT=%s\n" "$PORT" >> .env
fi
mkdir -p data
echo "✓ 監聽埠：$PORT（.env REACH_PORT，可隨時改）"

# ---------- 內網位址 ----------
LAN_IP=""
if command -v hostname >/dev/null 2>&1; then
  if [[ "$OS" == Darwin ]]; then
    LAN_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || true)
  else
    LAN_IP=$(hostname -I 2>/dev/null | awk '{print $1}')
  fi
fi

# ---------- 服務註冊 ----------
APP_DIR=$(pwd)
if [[ "$WITH_SERVICE" == 1 ]]; then
  if [[ "$OS" == Linux ]]; then
     $SUDO tee "/etc/systemd/system/$SVC_NAME.service" >/dev/null <<UNIT
[Unit]
Description=REACH AI Video Studio (server)
After=network-online.target

[Service]
Type=simple
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/.venv/bin/python $APP_DIR/app.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
UNIT
     $SUDO systemctl daemon-reload
     $SUDO systemctl enable --now "$SVC_NAME"
    echo "✓ systemd 服務已啟用：sudo systemctl status $SVC_NAME"
  else
    PLIST="$HOME/Library/LaunchAgents/com.sky.$SVC_NAME.plist"
    cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.sky.$SVC_NAME</string>
  <key>WorkingDirectory</key><string>$APP_DIR</string>
  <key>ProgramArguments</key><array>
    <string>$APP_DIR/.venv/bin/python</string><string>$APP_DIR/app.py</string>
  </array>
  <key>KeepAlive</key><true/>
  <key>RunAtLoad</key><true/>
</dict></plist>
PLIST
    launchctl bootstrap "gui/$(id -u)" "$PLIST" 2>/dev/null || launchctl kickstart -k "gui/$(id -u)/com.sky.$SVC_NAME"
    echo "✓ launchd 服務已啟用：com.sky.$SVC_NAME"
  fi
fi

cat <<MSG

──────────────────────────────────────────────────────
✅ Server 版安裝完成
  員工連線網址：
    $( [[ -n "$LAN_IP" ]] && echo "▸ http://$LAN_IP:$PORT/   （內網）" )
    ▸ http://127.0.0.1:$PORT/   （伺服器本機）
  金鑰設定：編輯 .env（公司採購的 API Key，不用留空）
  啟動方式：
$( [[ "$WITH_SERVICE" == 1 ]] && echo "    已註冊服務，開機自啟；手動控制：systemctl restart $SVC_NAME（mac: launchctl）" || echo "    .venv/bin/python app.py   或加上 --service 註冊開機自啟" )
  防火牆：若員工連不上，開放 TCP $PORT（Ubuntu: sudo ufw allow $PORT/tcp）
  版本：Server 版（公司行號）——個人單機請用 install.command
──────────────────────────────────────────────────────
MSG
