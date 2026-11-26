#!/usr/bin/env python3
"""reach-wan: self-hosted text-to-video / image-to-video (originally .219 AMD, now vendor-neutral).

Serves :35331, OpenAI-flavored /v1/videos/generations. Default target is
NVIDIA CUDA (flash/efficient SDPA native); AMD gfx1030 workarounds
(chunked math SDPA + OOM-retry) auto-activate only when an AMD card is
detected, or via REACH_GPU_ARCH / REACH_SDPA_CHUNKED overrides.

Cross-service coordination with a resident image server (server_gguf.py
:35330) is opt-in: set REACH_IMAGE_SERVER=1 on shared-card hosts (like
the old .219). Standalone DGX / single-tenant cards skip it.

Model set (~/reach-image-gguf/models/):
  wan22/Wan2.2-TI2V-5B-Q4_0.gguf   transformer (GGUF Q8, ComfyUI keys)
  wan22-diffusers/text_encoder/    umT5-xxl (bf16; placement auto, see _place)
  wan22-diffusers/vae/             Wan2.2 VAE (GPU)
  wan22-diffusers/{scheduler,tokenizer,*.json}
"""
import gc
import os
import threading
import time
from pathlib import Path

from flask import Flask, jsonify, request

from reach_gpu import card as _card

BASE = Path.home() / "reach-image-gguf"
GGUF_PATH = BASE / "models" / "wan22" / "Wan2.2-TI2V-5B-Q4_0.gguf"
DIFF_REPO_DIR = BASE / "models" / "wan22-diffusers"
DIFF_REPO_ID = "Wan-AI/Wan2.2-TI2V-5B-Diffusers"
API_KEY = "87dc257f7edb15c77fcb1610"
PORT = 35331
DTYPE_NAME = "bfloat16"
FPS = 24  # Wan2.2 VAE decodes at 24fps (4x16x16 compression)
STEPS = 20
GUIDANCE = 5.0  # official TI2V-5B recipe (cfg>1; enables negative prompt)

RESOLUTIONS = {
    "16:9": (1280, 704),
    "9:16": (704, 1280),
    "1:1": (960, 960),
    "4:3": (1024, 768),
}

QUEUE_TIMEOUT_S = 3600
app = Flask(__name__)
STATE = {"status": "loading", "error": "", "loaded_at": None, "devices": {}}
PIPE = {"obj": None}
GPU_LOCK = threading.Lock()
PROGRESS: dict[str, dict] = {}
PROGRESS_LOCK = threading.Lock()


def _dtype():
    import torch
    return {"bfloat16": torch.bfloat16, "float16": torch.float16}[DTYPE_NAME]


def _gpu_arch() -> str:
    """'nvidia' 或 'amd'。環境變數 REACH_GPU_ARCH 可強制覆寫。"""
    forced = os.environ.get("REACH_GPU_ARCH", "").strip().lower()
    if forced in ("nvidia", "amd"):
        return forced
    try:
        import torch
        name = torch.cuda.get_device_name(0) or ""
    except Exception:
        return "nvidia"
    return "amd" if ("amd" in name.lower() or "radeon" in name.lower() or "gfx" in name.lower()) else "nvidia"


def _patch_sdpa():
    """AMD gfx1030: no flash/efficient SDPA kernels; math backend materializes
    the full attention matrix. Chunk long queries; identical math.
    NVIDIA 有原生 flash/efficient kernel——預設跳過，REACH_SDPA_CHUNKED=1 可強制。"""
    import os
    import torch
    if getattr(torch.nn.functional, "_reach_sdpa_chunked", False):
        return
    if os.environ.get("REACH_SDPA_CHUNKED", "") != "1" and _gpu_arch() != "amd":
        return
    orig = torch.nn.functional.scaled_dot_product_attention
    CHUNK = 512  # 1024-chunk transients (~2-4GB) blow the budget left over
                 # beside the resident image server; 512 keeps them ~1GB.

    def chunked(query, key, value, attn_mask=None, *a, **kw):
        qlen = query.shape[-2]
        if qlen > CHUNK and not kw.get("is_causal", False):
            outs = []
            for s in range(0, qlen, CHUNK):
                m = attn_mask[..., s:s + CHUNK, :] if attn_mask is not None else None
                outs.append(orig(query[..., s:s + CHUNK, :], key, value, m, *a, **kw))
            return torch.cat(outs, dim=-2)
        return orig(query, key, value, attn_mask, *a, **kw)

    torch.nn.functional.scaled_dot_product_attention = chunked
    torch.nn.functional._reach_sdpa_chunked = True


def _place(pipe):
    import torch
    # umT5-xxl (~11GB bf16)：16GB 級共用卡放不下 → CPU；≥32GB 專用卡（DGX）留 GPU 提速。
    # REACH_TEXT_ENCODER=cpu|cuda 可強制；auto = 依 VRAM 決定。
    mode = os.environ.get("REACH_TEXT_ENCODER", "auto").strip().lower()
    if mode not in ("cpu", "cuda"):
        try:
            vram_gb = torch.cuda.get_device_properties(0).total_memory / 2**30
        except Exception:
            vram_gb = 0.0
        mode = "cuda" if vram_gb >= 32.0 else "cpu"
    pipe.text_encoder.to(mode)
    pipe.transformer.to("cuda")
    pipe.vae.to("cuda")
    # Wan2.2 VAE decode at 121×1280×704 materializes GBs of tiles otherwise.
    try:
        pipe.vae.enable_tiling()
    except Exception:
        pass
    gc.collect()
    torch.cuda.empty_cache()
    STATE["text_encoder_device"] = mode


def _video_to_file(video, path: Path) -> dict:
    """Export one decoded video to an MP4 via imageio/ffmpeg.

    Accepts a torch.Tensor (T, C, H, W) in [-1, 1] or a numpy array —
    this diffusers dev build returns (T, H, W, C) uint8 ndarray.
    """
    import numpy as np
    if hasattr(video, "cpu"):  # torch.Tensor path
        frames = video.cpu().float().numpy()  # (T, C, H, W) in [-1, 1]
        frames = ((frames + 1) * 127.5).clip(0, 255).astype("uint8")
        frames = frames.transpose(0, 2, 3, 1)  # (T, H, W, C)
    else:  # numpy path
        frames = np.asarray(video)
        if frames.dtype != np.uint8:
            if frames.max() <= 1.0:
                frames = frames * 255.0
            frames = frames.clip(0, 255).astype("uint8")
        if frames.shape[-1] not in (3, 4):  # (T, C, H, W) layout
            frames = frames.transpose(0, 2, 3, 1)
    try:
        import imageio.v2 as imageio
        w = imageio.get_writer(str(path), fps=FPS, codec="libx264", quality=8,
                               macro_block_size=16, ffmpeg_params=["-pix_fmt", "yuv420p"])
        for f in frames:
            w.append_data(f)
        w.close()
    except ImportError:
        import imageio
        imageio.mimwrite(str(path), frames, fps=FPS, codec="libx264",
                         quality=8, macro_block_size=16)
    return {"path": str(path), "frames": int(len(frames)), "fps": FPS}


def _ask_image_server_to_unload() -> None:
    """One 16GB card hosts both services. The image server may be mid-load
    when asked to unload, so poll until it reports fully unloaded."""
    import json as _json
    import time as _time
    import urllib.request

    def _call(path: str, method: str = "GET", timeout: int = 20):
        req = urllib.request.Request(
            f"http://127.0.0.1:35330{path}", method=method,
            headers={"Authorization": f"Bearer {API_KEY}",
                     "Content-Type": "application/json"},
            data=b"{}" if method == "POST" else None)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return _json.loads(resp.read())

    deadline = _time.time() + 900  # image load takes ~5 min; wait it out
    while _time.time() < deadline:
        try:
            health = _call("/health")
        except Exception as exc:  # noqa: BLE001 - image server may be down
            print(f"[wan] image health unreachable: {exc}", flush=True)
            return
        status = health.get("status")
        if status in ("loading", "generating"):
            print(f"[wan] image busy ({status}); waiting", flush=True)
            _time.sleep(10)
            continue
        if status == "unloaded":
            return
        try:
            result = _call("/api/admin/unload", method="POST")
            print(f"[wan] image unload -> {result}", flush=True)
            if result.get("unloaded") or result.get("status") == "unloaded":
                return
        except Exception as exc:  # noqa: BLE001
            print(f"[wan] image unload call failed: {exc}", flush=True)
            return
        _time.sleep(5)
    print("[wan] image never unloaded; proceeding anyway", flush=True)


def load_pipeline() -> None:
    try:
        import torch
        from diffusers import GGUFQuantizationConfig, WanPipeline, WanTransformer3DModel

        if not GGUF_PATH.is_file():
            raise FileNotFoundError(f"GGUF 檔不存在: {GGUF_PATH}")
        STATE["status"] = "loading"
        if os.environ.get("REACH_IMAGE_SERVER", "") == "1":
            _ask_image_server_to_unload()  # 共用卡的舊 .219 拓撲才需要；獨立卡（DGX）跳過
        _patch_sdpa()
        transformer = WanTransformer3DModel.from_single_file(
            str(GGUF_PATH),
            quantization_config=GGUFQuantizationConfig(compute_dtype=_dtype()),
            config=str(DIFF_REPO_DIR),
            subfolder="transformer",
            dtype=_dtype(),
        )
        pipe = WanPipeline.from_pretrained(
            str(DIFF_REPO_DIR), transformer=transformer, torch_dtype=_dtype())
        _place(pipe)
        PIPE["obj"] = pipe
        STATE.update(status="ready", loaded_at=time.time(),
                     devices={"text_encoder": "cpu", "transformer": "cuda", "vae": "cuda"})
        print("[wan] ready", flush=True)
    except Exception as exc:  # noqa: BLE001
        STATE.update(status="error", error=f"{type(exc).__name__}: {exc}"[:800])
        print(f"[wan] load FAILED: {exc}", flush=True)


def _unload():
    """Both servers share one 16GB card and the image server stays resident;
    the video model must fully release VRAM after every job."""
    import torch
    pipe = PIPE["obj"]
    if pipe is not None:
        try:
            del pipe.transformer
            del pipe.vae
        except Exception:
            pass
        PIPE["obj"] = None
        pipe = None
    gc.collect()
    torch.cuda.empty_cache()
    STATE.update(status="unloaded", loaded_at=None)
    print("[wan] unloaded", flush=True)


def _gen_one(pipe, prompt, negative, height, width, num_frames, seed, request_id, guidance=None):
    import torch
    gen = torch.Generator(device="cuda")
    if seed is not None and seed >= 0:
        gen.manual_seed(int(seed))
    else:
        seed = torch.seed() % (2**31)
        gen.manual_seed(seed)
    with torch.inference_mode():
        out = pipe(
            prompt=prompt,
            negative_prompt=negative or None,
            height=height, width=width,
            num_frames=num_frames,
            num_inference_steps=STEPS,
            guidance_scale=GUIDANCE if guidance is None else guidance,
            generator=gen,
            callback_on_step_end=lambda _p, _i, _t, kw: (
                (PROGRESS_LOCK, PROGRESS, request_id,
                 kw) and _report(request_id, _i, STEPS) or kw),
        )
    return out.frames[0], seed  # this diffusers build: WanPipelineOutput.frames


def _report(request_id, step, total):
    with PROGRESS_LOCK:
        PROGRESS[request_id] = {"step": int(step) + 1, "total": int(total)}
    return None


@app.get("/health")
def health():
    return jsonify(STATE)


@app.post("/v1/videos/generations")
def videos_generations():
    auth = request.headers.get("Authorization", "")
    if auth != f"Bearer {API_KEY}":
        return jsonify(error={"code": 401, "message": "unauthorized"}), 401
    body = request.get_json(force=True, silent=True) or {}
    prompt = (body.get("prompt") or "").strip()
    if not prompt:
        return jsonify(error={"code": 400, "message": "prompt required"}), 400
    request_id = body.get("request_id") or f"v{int(time.time()*1000)}"
    duration_s = float(body.get("duration", 5))
    num_frames = max(9, min(241, int(round(duration_s * FPS / 4)) * 4 + 1))
    ratio = body.get("ratio", "16:9")
    width, height = RESOLUTIONS.get(ratio, RESOLUTIONS["16:9"])
    if body.get("resolution") == "1080P":
        scale = 1.5
        width, height = int(width * scale) // 16 * 16, int(height * scale) // 16 * 16
    seed = body.get("seed")
    try:
        guidance = min(7.0, max(1.0, float(body.get("guidance", GUIDANCE))))
    except (TypeError, ValueError):
        guidance = GUIDANCE
    pipe = PIPE["obj"]
    if pipe is None:
        load_pipeline()
        pipe = PIPE["obj"]
    if pipe is None:
        return jsonify(error={"code": 503, "message": f"model not ready: {STATE['error']}"}), 503

    t0 = time.time()
    with _card(), GPU_LOCK:
        try:
            pipe = PIPE["obj"]
            if pipe is None:
                load_pipeline()
                pipe = PIPE["obj"]
            if pipe is None:
                return jsonify(error={"code": 503, "message": f"model not ready: {STATE['error']}"}), 503
            for attempt in (1, 2):
                try:
                    video, used_seed = _gen_one(
                        pipe, prompt, (body.get("negative_prompt") or "").strip(),
                        height, width, num_frames, seed, request_id)
                    break
                except RuntimeError as exc:
                    import traceback
                    traceback.print_exc()
                    import torch
                    print(f"[wan] OOM state: alloc={torch.cuda.memory_allocated()/2**30:.2f}GB "
                          f"reserved={torch.cuda.memory_reserved()/2**30:.2f}GB", flush=True)
                    gc.collect()
                    torch.cuda.empty_cache()
                    if "out of memory" not in str(exc).lower() or attempt == 2:
                        _unload()
                        return jsonify(error={"code": 507, "message": "CUDA OOM；請降低時長或尺寸"}), 507
                    time.sleep(2)
        finally:
            _unload()
    import torch
    torch.cuda.synchronize()
    outdir = BASE / "outputs" / "videos"
    outdir.mkdir(parents=True, exist_ok=True)
    fpath = outdir / f"{request_id}.mp4"
    meta = _video_to_file(video, fpath)
    del video
    gc.collect()
    torch.cuda.empty_cache()
    with PROGRESS_LOCK:
        PROGRESS.pop(request_id, None)
    return jsonify(data=[{
        "url": f"/files/videos/{fpath.name}",
        "path": meta["path"],
        "frames": meta["frames"], "fps": meta["fps"],
        "seconds": round(meta["frames"] / meta["fps"], 2),
        "width": width, "height": height,
        "seed": used_seed, "steps": STEPS, "guidance": guidance,
        "elapsed_s": round(time.time() - t0, 1),
    }])


@app.get("/files/videos/<path:name>")
def files_videos(name):
    from flask import send_from_directory
    return send_from_directory(BASE / "outputs" / "videos", name)


@app.get("/v1/videos/progress/<request_id>")
def videos_progress(request_id):
    with PROGRESS_LOCK:
        p = PROGRESS.get(request_id)
    return jsonify(progress=p)


if __name__ == "__main__":
    # No eager load: the card is shared with the resident image server.
    # The model loads lazily per request and unloads after each job.
    from waitress import serve
    serve(app, host="0.0.0.0", port=PORT, threads=8)
