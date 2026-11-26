"""地端 ComfyUI Provider（192.168.0.240:8188）。

流程：workflows/comfyui/<id>.json（API 格式 + 佔位符）→ POST /prompt → 輪詢 /history → /view 取檔。
佔位符：整個字串為 "{{name}}" 時替換成對應型別的值；常用 prompt / negative / seed /
width / height / frames / fps / image。用 scripts/comfy_import.py 由 ComfyUI「Export (API)」自動產生。
"""

from __future__ import annotations

import base64
import json
import random
import re
import time
import uuid
from pathlib import Path
from urllib.parse import urlencode

import requests

from .config import ROOT, env

WORKFLOW_DIR = ROOT / "workflows" / "comfyui"
CLIENT_ID = f"reach-{uuid.uuid4().hex[:8]}"
_FULL = re.compile(r"^\{\{(\w+)\}\}$")
_ANY = re.compile(r"\{\{(\w+)\}\}")
SHORT_SIDE = {"480": 480, "540": 544, "720": 720, "768": 768, "1080": 1088, "1440": 1440, "2160": 2160}
RATIOS = {"16:9": (16, 9), "9:16": (9, 16), "1:1": (1, 1), "4:3": (4, 3), "3:4": (3, 4), "21:9": (21, 9)}


class ComfyError(RuntimeError):
    pass


def base() -> str:
    return env("COMFYUI_BASE_URL", "http://192.168.0.240:8188").rstrip("/")


def _headers() -> dict:
    key = env("COMFYUI_API_KEY")
    return {"Authorization": f"Bearer {key}"} if key else {}


def _req(method: str, path: str, **kw) -> requests.Response:
    kw.setdefault("timeout", 30)
    try:
        r = requests.request(method, base() + path, headers=_headers(), **kw)
    except requests.RequestException as exc:
        raise ComfyError(f"連線 {base()} 失敗：{exc.__class__.__name__}") from exc
    if r.status_code >= 400:
        raise ComfyError(f"HTTP {r.status_code}：{r.text[:300]}")
    return r


# ---------------------------------------------------------------- workflows
_INSTALLED: dict = {"at": 0.0, "data": {}}


def installed_cached(ttl: int = 60) -> dict:
    """已安裝模型快取；連不到 ComfyUI 時回空（內建預設就不顯示）。"""
    if time.time() - _INSTALLED["at"] > ttl:
        try:
            _INSTALLED["data"] = installed()
        except ComfyError:
            _INSTALLED["data"] = {}
        _INSTALLED["at"] = time.time()
    return _INSTALLED["data"]


def list_workflows() -> list[dict]:
    from . import comfy_presets

    out = []
    custom = set()
    for f in sorted(WORKFLOW_DIR.glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and isinstance(d.get("workflow"), dict):
            out.append({"id": d.get("id") or f.stem, "kind": d.get("kind", "image"),
                        "status": d.get("status", "untested"), "note": d.get("note", ""), "_file": f})
            custom.add(out[-1]["id"])
    for pid in comfy_presets.available(installed_cached()):
        if pid not in custom:  # 同名自訂 workflow 優先
            p = comfy_presets.PRESETS[pid]
            out.append({"id": pid, "kind": p["kind"], "status": "builtin", "note": p["note"], "_preset": pid})
    return out


def models_for_config() -> list[dict]:
    return [{k: v for k, v in w.items() if not k.startswith("_")} for w in list_workflows()]


def first(kind: str) -> str | None:
    return next((w["id"] for w in list_workflows() if w["kind"] == kind), None)


def default(kind: str) -> str | None:
    """預設 workflow：先看 comfy_presets.DEFAULT_BY_KIND 釘選，缺件才退回第一個。"""
    from . import comfy_presets

    ids = [w["id"] for w in list_workflows() if w["kind"] == kind]
    pin = comfy_presets.DEFAULT_BY_KIND.get(kind)
    if pin and pin in ids:
        return pin
    return ids[0] if ids else None


def load(wid: str) -> dict:
    from . import comfy_presets

    for w in list_workflows():
        if w["id"] == wid:
            if w.get("_preset"):
                return comfy_presets.spec(w["_preset"])
            return json.loads(w["_file"].read_text(encoding="utf-8"))
    raise ComfyError(f"找不到 workflow「{wid}」（放到 workflows/comfyui/）")


def fill(obj, values: dict):
    if isinstance(obj, dict):
        return {k: fill(v, values) for k, v in obj.items()}
    if isinstance(obj, list):
        return [fill(v, values) for v in obj]
    if isinstance(obj, str):
        m = _FULL.match(obj)
        if m and m.group(1) in values:
            return values[m.group(1)]
        return _ANY.sub(lambda mm: str(values.get(mm.group(1), mm.group(0))), obj)
    return obj


def _unresolved(obj) -> set[str]:
    s = json.dumps(obj, ensure_ascii=False)
    return set(_ANY.findall(s))


# ---------------------------------------------------------------- io
def upload_image(data_uri: str) -> str:
    head, _, b64 = data_uri.partition(",")
    raw = base64.b64decode(b64 or head)
    ext = "jpg" if "jpeg" in head else "png"
    files = {"image": (f"reach-{uuid.uuid4().hex[:8]}.{ext}", raw, f"image/{'jpeg' if ext == 'jpg' else 'png'}")}
    body = _req("POST", "/upload/image", files=files, data={"overwrite": "true"}, timeout=60).json()
    sub = body.get("subfolder") or ""
    return f"{sub}/{body['name']}" if sub else body["name"]


def submit(wid: str, values: dict) -> str:
    spec = load(wid)
    vals = dict(spec.get("defaults") or {})
    vals.update({k: v for k, v in values.items() if v not in (None, "")})
    if vals.get("seed") in (None, "", -1, "-1", "random"):
        vals["seed"] = random.randint(1, 2**48)
    graph = fill(spec["workflow"], vals)
    missing = _unresolved(graph)
    if missing:
        raise ComfyError(f"workflow「{wid}」缺少參數：{', '.join(sorted(missing))}")
    body = _req("POST", "/prompt", json={"prompt": graph, "client_id": CLIENT_ID}, timeout=60).json()
    if body.get("node_errors"):
        raise ComfyError(f"workflow 驗證失敗：{json.dumps(body['node_errors'], ensure_ascii=False)[:300]}")
    pid = body.get("prompt_id")
    if not pid:
        raise ComfyError(f"無 prompt_id：{str(body)[:200]}")
    return pid


def _files(outputs: dict) -> list[dict]:
    files = []
    for node in outputs.values():
        for key in ("videos", "gifs", "video", "images", "audio"):
            for f in node.get(key) or []:
                if isinstance(f, dict) and f.get("filename") and f.get("type", "output") == "output":
                    files.append(f)
    return files


def view_url(f: dict) -> str:
    q = urlencode({"filename": f["filename"], "subfolder": f.get("subfolder", ""), "type": f.get("type", "output")})
    return f"{base()}/view?{q}"


def poll(prompt_id: str, prefer: str = "") -> dict:
    """回傳 {state: queued|running|succeeded|failed, url?, files?, message?}。"""
    hist = _req("GET", f"/history/{prompt_id}").json().get(prompt_id)
    if not hist:
        q = _req("GET", "/queue").json()
        running = any(item[1] == prompt_id for item in q.get("queue_running") or [])
        return {"state": "running" if running else "queued"}
    status = hist.get("status") or {}
    if status.get("status_str") == "error":
        msgs = [m[1] for m in status.get("messages") or [] if m and m[0] == "execution_error"]
        err = (msgs[0].get("exception_message") if msgs else "") or "執行錯誤"
        return {"state": "failed", "message": str(err)[:300]}
    if not status.get("completed", True):
        return {"state": "running"}
    files = _files(hist.get("outputs") or {})
    if not files:
        return {"state": "failed", "message": "執行完成但沒有輸出檔（確認有 Save 節點）"}
    exts = {"video": (".mp4", ".webm", ".mov", ".gif", ".webp"), "image": (".png", ".jpg", ".jpeg", ".webp")}.get(prefer, ())
    pick = next((f for f in files if f["filename"].lower().endswith(exts)), files[-1]) if exts else files[-1]
    return {"state": "succeeded", "url": view_url(pick), "files": [view_url(f) for f in files]}


def wait(prompt_id: str, prefer: str = "", timeout: int = 900) -> dict:
    end = time.time() + timeout
    while time.time() < end:
        st = poll(prompt_id, prefer)
        if st["state"] in ("succeeded", "failed"):
            return st
        time.sleep(1.5)
    raise ComfyError(f"等待逾時（{timeout}s），prompt_id={prompt_id}")


# ---------------------------------------------------------------- high level
def _dims(spec: dict, width: int, height: int) -> tuple[int, int]:
    m = int((spec.get("defaults") or {}).get("size_multiple") or spec.get("size_multiple") or 16)
    return max(m, round(width / m) * m), max(m, round(height / m) * m)


def video_dims(resolution: str, ratio: str) -> tuple[int, int]:
    res = {"2K": "1440", "4K": "2160"}.get(str(resolution).upper(), resolution)
    short = SHORT_SIDE.get(re.sub(r"\D", "", res or "720") or "720", 720)
    a, b = RATIOS.get(ratio, (16, 9))
    return (round(short * a / b), short) if a >= b else (short, round(short * b / a))


def run_image(wid: str, prompt: str, size: str = "1024x1024", references: list[str] | None = None,
              negative: str = "") -> dict:
    spec = load(wid)
    try:
        w, h = (int(x) for x in size.lower().split("x"))
    except ValueError:
        w, h = 1024, 1024
    w, h = _dims(spec, w, h)
    vals = {"prompt": prompt, "negative": negative, "width": w, "height": h}
    if references and "image" in _unresolved(spec["workflow"]):
        vals["image"] = upload_image(references[0])
    st = wait(submit(wid, vals), "image", timeout=int(spec.get("timeout") or 600))
    if st["state"] != "succeeded":
        raise ComfyError(st.get("message") or "生成失敗")
    data = _req("GET", st["url"].replace(base(), ""), timeout=120).content
    return {"b64": base64.b64encode(data).decode(), "url": st["url"], "raw": st}


def video_create(wid: str, prompt: str, duration: float = 5, resolution: str = "720P", ratio: str = "16:9",
                 first_frame_data_uri: str | None = None, negative: str = "") -> dict:
    spec = load(wid)
    d = spec.get("defaults") or {}
    fps = d.get("fps") or 24
    frames = max(1, int(round(float(duration) * float(fps))))
    mult = int(spec.get("frame_multiple") or 0)
    if mult:
        frames = (frames // mult) * mult + 1
    w, h = _dims(spec, *video_dims(resolution, ratio))
    vals = {"prompt": prompt, "negative": negative, "width": w, "height": h, "frames": frames, "fps": fps}
    needs_image = "image" in _unresolved(spec["workflow"])
    if needs_image:
        if not first_frame_data_uri:
            raise ComfyError(f"workflow「{wid}」需要一張圖片（首幀或參考圖）")
        vals["image"] = upload_image(first_frame_data_uri)
    return {"task_id": submit(wid, vals), "frames": frames, "size": f"{w}x{h}"}


def health() -> dict:
    s = _req("GET", "/system_stats", timeout=8).json()
    dev = (s.get("devices") or [{}])[0]
    q = _req("GET", "/queue", timeout=8).json()
    return {"version": (s.get("system") or {}).get("comfyui_version"), "gpu": dev.get("name"),
            "vram_free_gb": round((dev.get("vram_free") or 0) / 2**30, 1),
            "vram_total_gb": round((dev.get("vram_total") or 0) / 2**30, 1),
            "queue": len(q.get("queue_running") or []) + len(q.get("queue_pending") or []),
            "workflows": [w["id"] for w in list_workflows()]}


FOLDERS = ("checkpoints", "diffusion_models", "unet", "text_encoders", "vae", "loras", "upscale_models", "clip_vision")


def installed() -> dict:
    """ComfyUI 已安裝的模型檔（/models/<folder>）。"""
    out = {}
    for folder in FOLDERS:
        try:
            items = _req("GET", f"/models/{folder}", timeout=10).json()
        except ComfyError:
            continue
        if items:
            out[folder] = items
    return out
