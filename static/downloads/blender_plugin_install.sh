#!/bin/bash
# REACH — LibTV Blender 插件自動安裝（macOS）
# 用法：blender_plugin_install.sh [blender-*.zip]
#   無參數時依序找：~/Downloads 最新的 blender-*.zip → 專案 static/downloads/blender-macos.zip
# 安裝：解包 → 複製到 Blender 使用者 addons → headless 啟用 → 存偏好 → 驗證
set -euo pipefail

ZIP="${1:-}"
BLENDER_BIN="${BLENDER_BIN:-/Applications/Blender.app/Contents/MacOS/Blender}"

die() { echo "❌ $*" >&2; exit 1; }

[[ -x "$BLENDER_BIN" ]] || die "找不到 Blender（$BLENDER_BIN）。請安裝或設 BLENDER_BIN 指向 blender 執行檔。"

# 1) 找 zip
if [[ -z "$ZIP" ]]; then
  ZIP=$(ls -t ~/Downloads/blender-*.zip 2>/dev/null | head -1 || true)
  if [[ -z "$ZIP" ]]; then
    local_zip="$(cd "$(dirname "$0")/.." && pwd)/static/downloads/blender-macos.zip"
    [[ -f "$local_zip" ]] && ZIP="$local_zip"
  fi
  [[ -n "$ZIP" ]] || die "找不到 blender-*.zip；請把 zip 拖到 ~/Downloads 或以參數傳入路徑"
fi
[[ -f "$ZIP" ]] || die "檔案不存在：$ZIP"

# 2) Blender 版本 → 使用者 addons 目錄（4.2+：~/Library/Application Support/Blender/<ver>）
VER=$("$BLENDER_BIN" --version 2>/dev/null | head -1 | sed -E 's/^Blender ([0-9]+\.[0-9]+).*/\1/') \
  || die "無法取得 Blender 版本"
ADDONS="$HOME/Library/Application Support/Blender/$VER/scripts/addons"
[[ "$VER" < "4.2" ]] && ADDONS="$HOME/Library/Application Support/Blender Foundation/Blender/$VER/scripts/addons"
echo "▸ Blender $VER → $ADDONS"

# 3) 解包並找頂層資料夾
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
unzip -q "$ZIP" -d "$TMP"
TOP=$(find "$TMP" -mindepth 1 -maxdepth 1 -type d | head -1)
[[ -n "$TOP" && -f "$TOP/__init__.py" ]] || die "zip 內沒有 addon 資料夾（含 __init__.py）"
MODULE=$(basename "$TOP")

# 4) 複製（覆蓋舊版）
mkdir -p "$ADDONS"
rm -rf "$ADDONS/$MODULE"
cp -R "$TOP" "$ADDONS/"
echo "▸ 已安裝模組：$MODULE"

# 5) headless 啟用＋存偏好
"$BLENDER_BIN" --background --python-expr "
import bpy
bpy.ops.preferences.addon_enable(module='$MODULE')
bpy.ops.wm.save_userpref()
" >/dev/null 2>&1 || die "addon_enable 失敗（詳情可手動執行 Blender 看錯誤）"

# 6) 驗證（重新啟動讀回偏好）
CHECK=$("$BLENDER_BIN" --background --python-expr "
import bpy
print('REACH_CHECK:', '$MODULE' in bpy.context.preferences.addons)
" 2>/dev/null | grep -o "REACH_CHECK: True\|REACH_CHECK: False" | head -1)
[[ "$CHECK" == "REACH_CHECK: True" ]] || die "驗證失敗：$MODULE 未在偏好中生效"

echo "✅ 安裝完成：$MODULE 已啟用（Blender $VER）"
echo "   開 Blender → 3D View 右側欄（N）→ LibTV 分頁"
