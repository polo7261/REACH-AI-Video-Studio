#!/bin/bash
# REACH — LibTV Blender 插件一鍵安裝（macOS / Linux 單機版）
# 用法：blender_plugin_install.sh [blender-*.zip]
#   無參數時依序找：~/Downloads 最新的 blender-*.zip → 專案 static/downloads/blender-*.zip
#   Blender 路徑可用環境變數 BLENDER_BIN 覆寫
# 安裝：解包 → 複製到 Blender 使用者 addons → headless 啟用 → 存偏好 → 驗證
set -euo pipefail

ZIP="${1:-}"

banner() {
  cat <<'EOF'
╔═══════════════════════════════════════════════════════╗
║   REACH AI Video Studio — Blender 插件安裝（單機版）   ║
║   個人使用：App 跑在本機 http://127.0.0.1:35350        ║
║   Server 版（公司行號集中部署）請使用 Server 安裝程式  ║
╚═══════════════════════════════════════════════════════╝
EOF
}
banner
echo "   一鍵安裝：curl -fsSL https://raw.githubusercontent.com/polo7261/REACH-AI-Video-Studio/main/scripts/blender_plugin_install.sh | bash"

die() { echo "❌ $*" >&2; exit 1; }

# 0) 找 blender 執行檔（BLENDER_BIN 覆寫 → PATH → 平台慣例路徑）
find_blender() {
  if [[ -n "${BLENDER_BIN:-}" && -x "$BLENDER_BIN" ]]; then echo "$BLENDER_BIN"; return; fi
  if command -v blender >/dev/null 2>&1; then command -v blender; return; fi
  for c in \
    "/Applications/Blender.app/Contents/MacOS/Blender" \
    "/usr/bin/blender" "/usr/local/bin/blender" "/snap/bin/blender" \
    "$HOME/.local/bin/blender"; do
    [[ -x "$c" ]] && { echo "$c"; return; }
  done
  # flatpak（Linux）
  if command -v flatpak >/dev/null 2>&1 && flatpak info org.blender.Blender >/dev/null 2>&1; then
    echo "flatpak run org.blender.Blender"; return
  fi
}

BLENDER_BIN=$(find_blender) || true
[[ -n "$BLENDER_BIN" ]] || die "找不到 Blender。請安裝 Blender 或設 BLENDER_BIN 指向執行檔。"
echo "▸ Blender：$BLENDER_BIN"

# 1) 找 zip（插件是純 Python，macOS/linux 的 zip 通用）
if [[ -z "$ZIP" ]]; then
  ZIP=$(ls -t "$HOME/Downloads/"blender-*.zip 2>/dev/null | head -1 || true)
  if [[ -z "$ZIP" ]]; then
    local_zip="$(cd "$(dirname "$0")/.." 2>/dev/null && pwd)/static/downloads/"
    ZIP=$(ls -t "$local_zip"blender-macos.zip "$local_zip"blender-linux*.zip 2>/dev/null | head -1 || true)
  fi
  if [[ -z "$ZIP" ]]; then
    # 一鍵安裝（curl | bash）：本機沒有 zip 就直接抓 GitHub Release 最新版
    echo "▸ 本機沒有插件包，從 GitHub Release 下載最新版…"
    ZIP=$(mktemp -d)/blender-macos.zip
    curl -fsSL -o "$ZIP" \
      "https://github.com/polo7261/REACH-AI-Video-Studio/releases/latest/download/blender-macos.zip" \
      || die "下載失敗；請檢查網路，或手動下載 blender-macos.zip 後重試"
  fi
fi
[[ -f "$ZIP" ]] || die "檔案不存在：$ZIP"
echo "▸ 插件包：$ZIP"

# 2) Blender 版本 → 使用者 addons 目錄
bl() { if [[ "$BLENDER_BIN" == flatpak* ]]; then $BLENDER_BIN "$@"; else "$BLENDER_BIN" "$@"; fi; }
VER=$(bl --version 2>/dev/null | head -1 | sed -E 's/^Blender ([0-9]+\.[0-9]+).*/\1/')
[[ -n "$VER" ]] || die "無法取得 Blender 版本"
if [[ "$(uname)" == "Darwin" ]]; then
  ADDONS="$HOME/Library/Application Support/Blender/$VER/scripts/addons"
  [[ "$VER" < "4.2" ]] && ADDONS="$HOME/Library/Application Support/Blender Foundation/Blender/$VER/scripts/addons"
else
  ADDONS="$HOME/.config/blender/$VER/scripts/addons"
fi
echo "▸ Blender $VER → $ADDONS"

# 3) 解包並找頂層資料夾（unzip 不在時退回 python3）
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
if command -v unzip >/dev/null 2>&1; then
  unzip -q "$ZIP" -d "$TMP"
elif command -v python3 >/dev/null 2>&1; then
  python3 -m zipfile -e "$ZIP" "$TMP"
else
  die "系統缺少 unzip（也沒有 python3）；請先安裝 unzip"
fi
TOP=$(find "$TMP" -mindepth 1 -maxdepth 1 -type d | head -1)
[[ -n "$TOP" && -f "$TOP/__init__.py" ]] || die "zip 內沒有 addon 資料夾（含 __init__.py）"
MODULE=$(basename "$TOP")

# 4) 複製（覆蓋舊版）
mkdir -p "$ADDONS"
rm -rf "$ADDONS/$MODULE"
cp -R "$TOP" "$ADDONS/"
echo "▸ 已安裝模組：$MODULE"

# 5) headless 啟用＋存偏好
bl --background --python-expr "
import bpy
bpy.ops.preferences.addon_enable(module='$MODULE')
bpy.ops.wm.save_userpref()
" >/dev/null 2>&1 || die "addon_enable 失敗（詳情可手動啟動 Blender 看錯誤）"

# 6) 驗證（重新啟動讀回偏好）
CHECK=$(bl --background --python-expr "
import bpy
print('REACH_CHECK:', '$MODULE' in bpy.context.preferences.addons)
" 2>/dev/null | grep -o "REACH_CHECK: True\|REACH_CHECK: False" | head -1)
[[ "$CHECK" == "REACH_CHECK: True" ]] || die "驗證失敗：$MODULE 未在偏好中生效"

echo "✅ 安裝完成：${MODULE} 已啟用（Blender ${VER}，單機版）"
echo "   開 Blender → 3D View 右側欄（N）→ LibTV 分頁"
