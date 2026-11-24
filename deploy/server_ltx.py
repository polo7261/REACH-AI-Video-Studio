"""REACH LTXV 2B video server（192.168.0.219:35332）。

API 形狀刻意與 server_wan.py 相同：
  GET  /health
  POST /v1/videos/generations   {prompt, negative_prompt, duration, ratio, resolution, seed, steps}
  GET  /files/videos/<name>

lazy load、每個任務後卸載；bbox 由 ratio 決定，預設 704x480（快）。
"""
from __future__ import annotations

import gc
import os
import threading
import time
import uuid
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

BASE = Path.home() / "reach-image-gguf"
MODEL_DIR = BASE / "models" / "ltxv-2b-diffusers"
OUT_DIR = BASE / "outputs" / "videos-ltx"
API_KEY = os.environ["REACH_LTX_KEY"]  # 金鑰由環境變數提供，未設定即拒絕啟動
PORT = 35332
FPS = 24

# 2B 在 16GB 卡上以 704x480 最穩；1080P 需縮小幀數
# 寬高必須被 32 整除（LTXPipeline 驗證）
RESOLUTIONS = {
    "16:9": (768, 448),
    "9:16": (448, 768),
    "1:1": (512, 512),
    "4:3": (512, 384),
}
DEFAULT_STEPS = 24
GUIDANCE = 5.0  # 實測：3.0 偏糊，5.0 才穩定（dev 模型）

app = Flask(__name__)
STATE = {"status": "loading", "error": "", "loaded_at": None, "model": "LTXV-2B"}
PIPE = {"obj": None}
GPU_LOCK = threading.Lock()
PROGRESS: dict[str, dict] = {}
PROGRESS_LOCK = threading.Lock()


def _dtype():
    import torch

    return torch.bfloat16


def load_pipeline() -> None:
    try:
        import torch
        from diffusers import LTXPipeline

        t0 = time.time()
        print(f"[ltx] loading {MODEL_DIR}", flush=True)
        pipe = LTXPipeline.from_pretrained(str(MODEL_DIR), torch_dtype=_dtype(), local_files_only=True)
        # 16 GB 卡：權重 15 GB，必須把 T5/模組按需搬到 GPU，並切 VAE/attention
        try:
            pipe.enable_model_cpu_offload()
            print("[ltx] model cpu offload enabled", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"[ltx] cpu offload unavailable ({exc}); falling back to cuda", flush=True)
            pipe.to("cuda")
        try:
            pipe.vae.enable_tiling()
        except Exception:  # noqa: BLE001
            pass
        try:
            pipe.enable_attention_slicing("max")
            print("[ltx] attention slicing = max", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"[ltx] attention slicing unavailable ({exc})", flush=True)
        pipe.set_progress_bar_config(disable=True)
        PIPE["obj"] = pipe
        STATE.update(status="ready", error="", loaded_at=time.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"[ltx] ready in {time.time() - t0:.1f}s", flush=True)
    except Exception as exc:  # noqa: BLE001
        STATE.update(status="error", error=f"{type(exc).__name__}: {exc}"[:400])
        print(f"[ltx] load failed: {exc}", flush=True)


def _unload() -> None:
    import torch

    PIPE["obj"] = None
    gc.collect()
    torch.cuda.empty_cache()


def _step_cb(rid: str, total: int):
    """diffusers 要求 callback 回傳 dict（可修改 latents）；回空 dict 即可。"""
    def cb(_pipe, step_index, _timestep, _kwargs):
        _report(rid, step_index, total)
        return {}
    return cb


def _report(rid: str, step: int, total: int) -> None:
    with PROGRESS_LOCK:
        PROGRESS[rid] = {"step": int(step) + 1, "total": int(total)}


@app.get("/health")
def health():
    return jsonify(STATE)


@app.post("/v1/videos/generations")
def generate():
    if request.headers.get("Authorization", "") != f"Bearer {API_KEY}":
        return jsonify(error={"code": 401, "message": "unauthorized"}), 401
    body = request.get_json(force=True, silent=True) or {}
    prompt = (body.get("prompt") or "").strip()
    if not prompt:
        return jsonify(error={"code": 400, "message": "prompt required"}), 400

    rid = body.get("request_id") or f"ltx{int(time.time() * 1000)}"
    duration = float(body.get("duration", 3))
    ratio = body.get("ratio", "16:9")
    width, height = RESOLUTIONS.get(ratio, RESOLUTIONS["16:9"])
    # 允許覆寫（需被 32 整除；上限 960x544 避免 OOM）
    try:
        bw, bh = int(body.get("width") or 0), int(body.get("height") or 0)
        if bw >= 256 and bh >= 256 and bw % 32 == 0 and bh % 32 == 0 and bw <= 960 and bh <= 576:
            width, height = bw, bh
    except (TypeError, ValueError):
        pass
    steps = int(body.get("steps") or DEFAULT_STEPS)
    steps = max(4, min(40, steps))
    # LTX 以 8 幀為單位 + 1；時長上限 6 秒避免 OOM
    num_frames = max(9, min(145, int(round(min(duration, 6) * FPS / 8)) * 8 + 1))
    seed = int(body.get("seed") or time.time()) % (2**31 - 1)

    if PIPE["obj"] is None:
        load_pipeline()
    if PIPE["obj"] is None:
        return jsonify(error={"code": 503, "message": f"model not ready: {STATE['error']}"}), 503

    import torch

    t0 = time.time()
    with GPU_LOCK:
        try:
            pipe = PIPE["obj"]
            gen = torch.Generator(device="cuda").manual_seed(seed) if torch.cuda.is_available() else None
            out = pipe(
                prompt=prompt,
                negative_prompt=(body.get("negative_prompt") or "").strip(),
                width=width,
                height=height,
                num_frames=num_frames,
                num_inference_steps=steps,
                guidance_scale=float(body.get("guidance") or GUIDANCE),
                generator=gen,
                output_type="np",
                callback_on_step_end=_step_cb(rid, steps),
            )
        except RuntimeError as exc:
            gc.collect()
            torch.cuda.empty_cache()
            _unload()
            if "out of memory" in str(exc).lower():
                return jsonify(error={"code": 507, "message": "CUDA OOM；請降低時長/解析度"}), 507
            return jsonify(error={"code": 500, "message": str(exc)[:300]}), 500
        finally:
            with PROGRESS_LOCK:
                PROGRESS.pop(rid, None)

    frames = out.frames[0]
    try:
        from diffusers.utils import export_to_video

        OUT_DIR.mkdir(parents=True, exist_ok=True)
        fpath = OUT_DIR / f"{rid}.mp4"
        export_to_video(frames, str(fpath), fps=FPS)
    finally:
        del out
        gc.collect()
        torch.cuda.empty_cache()
        _unload()

    return jsonify(data=[{
        "url": f"/files/videos/{fpath.name}",
        "path": str(fpath),
        "frames": int(num_frames), "fps": FPS,
        "seconds": round(num_frames / FPS, 2),
        "width": width, "height": height,
        "seed": seed, "steps": steps,
        "elapsed_s": round(time.time() - t0, 1),
    }])


@app.get("/files/videos/<path:name>")
def files(name: str):
    return send_from_directory(OUT_DIR, name)


@app.get("/v1/videos/progress/<rid>")
def progress(rid: str):
    with PROGRESS_LOCK:
        return jsonify(progress=PROGRESS.get(rid))


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=PORT, threads=8)
