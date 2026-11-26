# REACH — LibTV Blender 插件自動安裝（Windows）
# 用法（PowerShell）：.\blender_plugin_install.ps1 [-Zip blender-macos.zip 對應的 windows zip 路徑]
#   無參數時依序找：$HOME\Downloads 最新的 blender-*.zip → 專案 static\downloads\blender-windows-x64.zip
# 安裝：解包 → 複製到 Blender 使用者 addons → headless 啟用 → 存偏好 → 驗證
param([string]$Zip = "")

$ErrorActionPreference = "Stop"

function Die($msg) { Write-Host "❌ $msg" -ForegroundColor Red; exit 1 }

# 1) 找 blender.exe（Program Files 慣例路徑，或 PATH）
$bin = @(
  (Get-Command blender.exe -ErrorAction SilentlyContinue)?.Source,
  (Get-ChildItem "C:\Program Files\Blender Foundation\Blender *\blender.exe" -ErrorAction SilentlyContinue |
    Sort-Object FullName -Descending | Select-Object -First 1).FullName
) | Where-Object { $_ } | Select-Object -First 1
if (-not $bin) { Die "找不到 blender.exe；請安裝 Blender 或自行指定路徑" }
Write-Host "▸ Blender：$bin"

# 2) 版本 → 使用者 addons 目錄（Windows 一律 %APPDATA%\Blender Foundation\Blender\<ver>）
$verLine = (& $bin --version | Select-Object -First 1)
if ($verLine -notmatch "^Blender (\d+\.\d+)") { Die "無法取得 Blender 版本" }
$ver = $Matches[1]
$addons = $env:APPDATA | Join-Path -ChildPath "Blender Foundation" | Join-Path -ChildPath "Blender" | Join-Path -ChildPath $ver | Join-Path -ChildPath "scripts" | Join-Path -ChildPath "addons"
Write-Host "▸ Blender $ver → $addons"

# 3) 找 zip
if (-not $Zip) {
  $cand = @(Get-ChildItem "$HOME\Downloads\blender-*.zip" -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1)
  $local = Join-Path $PSScriptRoot "..\static\downloads\blender-windows-x64.zip"
  if ($cand) { $Zip = $cand[0].FullName } elseif (Test-Path $local) { $Zip = $local }
}
if (-not $Zip -or -not (Test-Path $Zip)) { Die "找不到 blender-*.zip；請以 -Zip 傳入路徑" }

# 4) 解包並找頂層資料夾
$tmp = Join-Path ($env:TEMP ?? "/tmp") ("reach-blender-" + [guid]::NewGuid().ToString("N").Substring(0, 8))
Expand-Archive -Path $Zip -DestinationPath $tmp -Force
$top = Get-ChildItem $tmp -Directory | Select-Object -First 1
if (-not $top -or -not (Test-Path (Join-Path $top.FullName "__init__.py"))) {
  Die "zip 內沒有 addon 資料夾（含 __init__.py）"
}
$module = $top.Name

# 5) 複製（覆蓋舊版）
New-Item -ItemType Directory -Force -Path $addons | Out-Null
$dest = Join-Path $addons $module
if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
Copy-Item -Recurse -Force $top.FullName $dest
Write-Host "▸ 已安裝模組：$module"

# 6) headless 啟用＋存偏好
$expr = "import bpy; bpy.ops.preferences.addon_enable(module='$module'); bpy.ops.wm.save_userpref()"
& $bin --background --python-expr $expr 2>$null | Out-Null

# 7) 驗證
$checkExpr = "import bpy; print('REACH_CHECK:', '$module' in bpy.context.preferences.addons)"
$check = (& $bin --background --python-expr $checkExpr 2>$null | Select-String "REACH_CHECK:").Line
Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
if ($check -notmatch "REACH_CHECK: True") { Die "驗證失敗：$module 未在偏好中生效" }

Write-Host "✅ 安裝完成：$module 已啟用（Blender $ver）"
Write-Host "   開 Blender → 3D View 右側欄（N）→ LibTV 分頁"
