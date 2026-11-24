#!/bin/bash
# 打包安裝檔（不含任何 API Key）：.venv / .env / data / exports 一律不入包。
# 用法：scripts/build_installer.sh [版本]
#   → dist/REACH-AI-Vidio-Studio-<版本>-<日期>.zip     （macOS）
#   → dist/REACH-AI-Vidio-Studio-<版本>-<日期>.tar.gz  （Ubuntu／Debian，內容相同）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

VERSION="${1:-v0.3}"
NAME="REACH-AI-Vidio-Studio"
OUT_DIR="$ROOT/dist"
STAMP="${NAME}-${VERSION}-$(date +%Y%m%d)"
ZIP="$OUT_DIR/${STAMP}.zip"
TGZ="$OUT_DIR/${STAMP}.tar.gz"

# 白名單：只收原始碼與文件
FILES=(app.py requirements.txt README.md INSTALL.md .env.example .gitignore
       install.command start.command)
DIRS=(reach_video deploy scripts docs static templates)

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
STAGE="$TMP/$NAME"
mkdir -p "$STAGE"

cp "${FILES[@]}" "$STAGE/"
for d in "${DIRS[@]}"; do
  rsync -a --exclude '__pycache__' --exclude '*.py[cod]' --exclude '.DS_Store' "$d" "$STAGE/"
done
rm -f "$STAGE/scripts/build_installer.sh"
chmod +x "$STAGE/install.command" "$STAGE/start.command"

# deploy/server_ltx.py 必須讀環境變數 REACH_LTX_KEY，不得寫死金鑰
LTX="$STAGE/deploy/server_ltx.py"
grep -q '^API_KEY = os.environ\["REACH_LTX_KEY"\]' "$LTX" || { echo "✗ server_ltx.py 未改讀 REACH_LTX_KEY"; exit 1; }

# 防呆 1：不得出現的檔案
for bad in .env .venv data exports; do
  [ -e "$STAGE/$bad" ] && { echo "✗ 包內出現 $bad"; exit 1; }
done

# 防呆 2：.env 內任何金鑰「值」都不得出現在包內（只印變數名，不印值）
LEAK=0
if [ -f .env ]; then
  while IFS='=' read -r k v; do
    [[ "$k" =~ (KEY|TOKEN|SECRET|PASSWORD) ]] || continue
    v="${v%\"}"; v="${v#\"}"
    [ "${#v}" -ge 8 ] || continue
    [[ "$v" == REPLACE* ]] && continue
    if grep -rqF -- "$v" "$STAGE"; then
      echo "✗ 包內含 .env 的 $k 值"; LEAK=1
    fi
  done < <(grep -E '^[A-Z0-9_]+=' .env)
fi

# 防呆 3：常見金鑰樣式
if grep -rnE 'sk-[A-Za-z0-9_-]{16,}|Bearer [A-Za-z0-9]{16,}|(API_?KEY|TOKEN|SECRET)[A-Z_]* *= *"[A-Za-z0-9_-]{12,}"' "$STAGE" >/dev/null; then
  echo "✗ 包內有疑似寫死的金鑰樣式："
  grep -rlE 'sk-[A-Za-z0-9_-]{16,}|Bearer [A-Za-z0-9]{16,}|(API_?KEY|TOKEN|SECRET)[A-Z_]* *= *"[A-Za-z0-9_-]{12,}"' "$STAGE"
  LEAK=1
fi
[ "$LEAK" -eq 0 ] || { echo "✗ 中止打包"; exit 1; }

mkdir -p "$OUT_DIR"
rm -f "$ZIP" "$TGZ"
(cd "$TMP" && zip -qrX "$ZIP" "$NAME")
# tar.gz 給 Linux：不帶 macOS 擴充屬性／._ 檔，擁有者設 root（一般使用者解壓會歸自己）
(cd "$TMP" && COPYFILE_DISABLE=1 tar --no-xattrs --no-mac-metadata \
   --uid 0 --gid 0 --uname root --gname root -czf "$TGZ" "$NAME")
(cd "$OUT_DIR" && shasum -a 256 "$(basename "$ZIP")" > "$(basename "$ZIP").sha256" \
                && shasum -a 256 "$(basename "$TGZ")" > "$(basename "$TGZ").sha256")
echo "✓ 金鑰檢查通過"
echo "✓ $ZIP（$(du -h "$ZIP" | cut -f1)，$(unzip -Z1 "$ZIP" | grep -vc '/$') 個檔案）— macOS"
echo "✓ $TGZ（$(du -h "$TGZ" | cut -f1)，$(tar -tzf "$TGZ" | grep -vc '/$') 個檔案）— Ubuntu／Debian"
