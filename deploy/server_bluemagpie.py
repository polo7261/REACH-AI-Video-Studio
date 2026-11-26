"""REACH BlueMagpie TTS server（台灣華語；GPU 機）。

部署（在有 NVIDIA GPU 的機器）：
  git clone https://github.com/OpenFormosa/BlueMagpie-TTS && cd BlueMagpie-TTS
  python3.12 -m venv .venv && .venv/bin/pip install -e . soundfile flask
  REACH_BM_KEY=<與 REACH 端 .env 相同值> .venv/bin/python <REACH repo>/deploy/server_bluemagpie.py

API 形狀比照 server_wan.py／server_ltx.py：
  GET  /health      → {ok, model, speakers}
  POST /v1/tts      {text, speaker?, speed?} → audio/wav bytes

首次啟動會 snapshot_download("OpenFormosa/BlueMagpie-TTS")（約 8 GB，公開模型免 token）。
"""
from __future__ import annotations

import gc
import io
import os
import threading
import time

import soundfile as sf
from flask import Flask, jsonify, request, send_file

API_KEY = os.environ["REACH_BM_KEY"]  # 未設定即拒絕啟動
PORT = int(os.environ.get("REACH_BM_PORT") or 35333)
DEFAULT_SPEAKER = os.environ.get("REACH_BM_SPEAKER") or "hung_yi_lee"

app = Flask(__name__)
STATE = {"status": "loading", "error": "", "speakers": [], "model": "BlueMagpie-TTS (48kHz)"}
MODEL = {"obj": None, "tokenizer": None, "centroids": None, "sample_rate": 48000}
GPU_LOCK = threading.Lock()


def _load() -> None:
    import torch
    from huggingface_hub import snapshot_download
    from transformers import PreTrainedTokenizerFast
    from bluemagpie import BlueMagpieModel

    t0 = time.time()
    model_dir = snapshot_download("OpenFormosa/BlueMagpie-TTS")
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=os.path.join(model_dir, "tokenizer.json"))
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = BlueMagpieModel.from_local(model_dir, tokenizer=tokenizer, training=False, device=device)
    table = torch.load(os.path.join(model_dir, "checkpoints", "speaker_centroids.pt"),
                       map_location="cpu", weights_only=True)
    MODEL.update(obj=model, tokenizer=tokenizer, centroids=table,
                 sample_rate=model.sample_rate)
    STATE.update(status="ready", speakers=list(table["speaker_ids"]),
                 error="", loaded_at=time.strftime("%H:%M:%S"))
    print(f"[bluemagpie] ready on {device}（{time.time() - t0:.0f}s）；speakers: {table['speaker_ids']}", flush=True)


def _auth(req) -> str | None:
    auth = req.headers.get("Authorization", "")
    return auth.removeprefix("Bearer ").strip() or None


def _centroid(speaker: str):
    table = MODEL["centroids"]
    if speaker in table["speaker_ids"]:
        return table["centroids"][table["speaker_ids"].index(speaker)]
    return table["centroids"][0]


@app.get("/health")
def health():
    ok = STATE["status"] == "ready"
    body = {"ok": ok, **STATE}
    return (jsonify(body), 200) if ok else (jsonify(body), 503)


@app.post("/v1/tts")
def tts():
    if _auth(request) != API_KEY:
        return jsonify(error="unauthorized"), 401
    body = request.get_json(force=True, silent=True) or {}
    text = (body.get("text") or "").strip()
    if not text:
        return jsonify(error="text 必填"), 400
    speaker = (body.get("speaker") or DEFAULT_SPEAKER).strip()
    speed = float(body.get("speed") or 1.0)
    if STATE["status"] != "ready":
        return jsonify(error=f"模型 {STATE['status']}：{STATE['error'][:120]}"), 503
    with GPU_LOCK:
        try:
            audio = MODEL["obj"].generate(
                target_text=text, speaker_centroid=_centroid(speaker), cfg_value=2.0
            )
        except Exception as exc:  # 推論錯誤：回 500 帶訊息
            gc.collect()
            STATE["error"] = str(exc)[:200]
            return jsonify(error=str(exc)[:200]), 500
    wav = io.BytesIO()
    sf.write(wav, audio.squeeze().cpu().numpy(), MODEL["sample_rate"], format="WAV")
    wav.seek(0)
    print(f"[bluemagpie] tts ok：{len(text)} 字 → {audio.shape[-1] / MODEL['sample_rate']:.1f}s（speaker={speaker}）", flush=True)
    return send_file(wav, mimetype="audio/wav")


if __name__ == "__main__":
    try:
        _load()
    except Exception as exc:  # 載入失敗也保持可 /health 觀察
        STATE.update(status="error", error=str(exc)[:300])
        print(f"[bluemagpie] 載入失敗：{exc}", flush=True)
    app.run(host="0.0.0.0", port=PORT, threaded=False)
