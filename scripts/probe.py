#!/usr/bin/env python3
"""Provider smoke probe: 三家的 /models、chat、image、video 能力實測。

只印狀態與錯誤摘要（不印金鑰）。用法：python scripts/probe.py [provider]
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]


def load_env() -> None:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k, v)


def short(text: str, n: int = 160) -> str:
    text = " ".join(str(text).split())
    return text[:n]


def show(label: str, resp: requests.Response, want_json: bool = True) -> object | None:
    body = None
    try:
        body = resp.json()
    except ValueError:
        body = resp.text
    summary = json.dumps(body, ensure_ascii=False)[:220] if want_json and not isinstance(body, str) else short(body)
    print(f"  {label}: HTTP {resp.status_code} | {summary}")
    return body


def aliyun() -> None:
    print("== Aliyun token-plan (OpenAI compatible) ==")
    base = os.environ["ALIYUN_BASE_URL"].rstrip("/")
    key = os.environ["ALIYUN_API_KEY"]
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    r = requests.get(f"{base}/models", headers=h, timeout=20)
    models = show("GET /models", r)
    ids = []
    if isinstance(models, dict):
        ids = [m.get("id") for m in models.get("data", []) if isinstance(m, dict)]
        print(f"  model count: {len(ids)} e.g. {ids[:6]}")

    model = os.environ.get("ALIYUN_TEXT_MODEL") or (ids[0] if ids else "qwen-plus")
    r = requests.post(
        f"{base}/chat/completions",
        headers=h,
        json={"model": model, "messages": [{"role": "user", "content": "回覆兩個字：READY"}], "max_tokens": 8},
        timeout=60,
    )
    show(f"POST /chat/completions ({model})", r)

    img = os.environ.get("ALIYUN_IMAGE_MODEL")
    r = requests.post(
        f"{base}/images/generations",
        headers=h,
        json={"model": img, "prompt": "a red square on white", "n": 1, "size": "1024x1024"},
        timeout=120,
    )
    show(f"POST /images/generations ({img})", r)
    print(f"  anthropic endpoint (record only): {os.environ.get('ALIYUN_ANTHROPIC_URL')}")


def volcano() -> None:
    print("== Volcano Ark ==")
    base = os.environ["VOLC_BASE_URL"].rstrip("/")
    key = os.environ["VOLC_API_KEY"]
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    any_ok = False
    for model in [os.environ.get("VOLC_TEXT_MODEL") or "", "doubao-seed-1-6-250615", "doubao-1-5-pro-32k-250115"]:
        if not model:
            continue
        r = requests.post(
            f"{base}/chat/completions",
            headers=h,
            json={"model": model, "messages": [{"role": "user", "content": "hi"}], "max_tokens": 5},
            timeout=45,
        )
        body = show(f"POST /chat/completions ({model})", r)
        if r.status_code == 200:
            any_ok = True
            break
    if not any_ok:
        print("  note: Ark 需要 endpoint id（ep-...）或已開通模型；目前以上皆失敗")


def minimax() -> None:
    print("== MiniMax (cn) ==")
    base = os.environ["MINIMAX_BASE_URL"].rstrip("/")
    key = os.environ["MINIMAX_API_KEY"]
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    model = os.environ.get("MINIMAX_TEXT_MODEL", "MiniMax-M2")
    r = requests.post(
        f"{base}/text/chatcompletion_v2",
        headers=h,
        json={"model": model, "messages": [{"role": "user", "content": "hi"}], "max_tokens": 8},
        timeout=60,
    )
    show(f"POST /text/chatcompletion_v2 ({model})", r)
    r = requests.get(f"{base}/query/video_generation", headers=h, timeout=20)
    show("GET /query/video_generation (auth probe)", r)


def main() -> int:
    load_env()
    which = (sys.argv[1] if len(sys.argv) > 1 else "all").lower()
    if which in ("all", "aliyun"):
        aliyun()
    if which in ("all", "volcano"):
        volcano()
    if which in ("all", "minimax"):
        minimax()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
