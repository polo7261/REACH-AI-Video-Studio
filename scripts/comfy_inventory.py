#!/usr/bin/env python3
"""列出地端 ComfyUI 已安裝的模型與 REACH 已註冊的 workflow。用法：python3 scripts/comfy_inventory.py"""
import json, os, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = os.environ.get("COMFYUI_BASE_URL", "")
env = ROOT / ".env"
if not base and env.is_file():
    for line in env.read_text(encoding="utf-8").splitlines():
        if line.startswith("COMFYUI_BASE_URL="):
            base = line.split("=", 1)[1].strip()
base = (base or "http://192.168.0.240:8188").rstrip("/")

def get(p):
    with urllib.request.urlopen(base + p, timeout=15) as r:
        return json.load(r)

try:
    s = get("/system_stats")
except Exception as e:
    sys.exit(f"✗ 連不到 {base}：{e}")
d = (s.get("devices") or [{}])[0]
print(f"ComfyUI {s['system'].get('comfyui_version')} @ {base}")
print(f"GPU {d.get('name')}  VRAM free {d.get('vram_free',0)/2**30:.1f}/{d.get('vram_total',0)/2**30:.1f} GB\n")
for folder in ("checkpoints", "diffusion_models", "unet", "text_encoders", "clip", "vae", "loras", "controlnet", "upscale_models", "clip_vision"):
    try:
        items = get(f"/models/{folder}")
    except Exception:
        continue
    if items:
        print(f"[{folder}] {len(items)}")
        for m in items:
            print("   ", m)
wf = sorted((ROOT / "workflows" / "comfyui").glob("*.json"))
print(f"\nREACH workflows：{', '.join(p.stem for p in wf) or '（尚無，用 scripts/comfy_import.py 匯入）'}")
