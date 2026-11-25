"""三家 Provider 的真實呼叫（阿里閘道 / MiniMax / 火山 Ark）。

全部同步 requests；錯誤統一轉成 ProviderError（訊息含 provider 原始摘要）。
"""

from __future__ import annotations

import base64
import json
import time
from typing import Any

import requests

from .config import PROVIDERS, key_for

TIMEOUT = 120


class ProviderError(RuntimeError):
    def __init__(self, provider: str, message: str, code: Any = None):
        super().__init__(f"[{provider}] {message}")
        self.provider = provider
        self.code = code


def _headers(provider: str) -> dict[str, str]:
    key = key_for(provider)
    if not key:
        raise ProviderError(provider, "API key 未設定")
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def _base(provider: str) -> str:
    return PROVIDERS[provider]["base_url"].rstrip("/")


def _post(provider: str, path: str, payload: dict, timeout: int = TIMEOUT) -> dict:
    try:
        r = requests.post(_base(provider) + path, headers=_headers(provider), json=payload, timeout=timeout)
    except requests.RequestException as exc:
        raise ProviderError(provider, f"連線失敗：{exc.__class__.__name__}") from exc
    if r.status_code >= 400:
        raise ProviderError(provider, _err_text(r), r.status_code)
    try:
        return r.json()
    except ValueError as exc:
        raise ProviderError(provider, f"非 JSON 回應：{r.text[:120]}") from exc


def _post_url(url: str, payload: dict, provider: str = "minimax", timeout: int = 120) -> dict:
    try:
        r = requests.post(url, headers=_headers(provider), json=payload, timeout=timeout)
    except requests.RequestException as exc:
        raise ProviderError(provider, f"連線失敗：{exc.__class__.__name__}") from exc
    if r.status_code >= 400:
        raise ProviderError(provider, _err_text(r), r.status_code)
    try:
        return r.json()
    except ValueError as exc:
        raise ProviderError(provider, f"非 JSON 回應：{r.text[:120]}") from exc


def _get_url(url: str, params: dict, provider: str = "minimax", timeout: int = 60) -> dict:
    try:
        r = requests.get(url, headers=_headers(provider), params=params, timeout=timeout)
    except requests.RequestException as exc:
        raise ProviderError(provider, f"連線失敗：{exc.__class__.__name__}") from exc
    if r.status_code >= 400:
        raise ProviderError(provider, _err_text(r), r.status_code)
    return r.json()


def _minimax_v2_root() -> str:
    base = _base("minimax").rstrip("/")
    return base[:-3] if base.endswith("/v1") else base


def _get(provider: str, path: str, params: dict | None = None, timeout: int = 60) -> dict:
    try:
        r = requests.get(_base(provider) + path, headers=_headers(provider), params=params or {}, timeout=timeout)
    except requests.RequestException as exc:
        raise ProviderError(provider, f"連線失敗：{exc.__class__.__name__}") from exc
    if r.status_code >= 400:
        raise ProviderError(provider, _err_text(r), r.status_code)
    return r.json()


def _err_text(r: requests.Response) -> str:
    try:
        body = r.json()
    except ValueError:
        return r.text[:200]
    if isinstance(body, dict):
        err = body.get("error")
        if isinstance(err, dict):
            return str(err.get("message") or err.get("code") or err)[:240]
        if isinstance(err, str):
            return err[:240]
        base = body.get("base_resp") or {}
        if base.get("status_msg"):
            return f"{base.get('status_msg')} (code {base.get('status_code')})"
    return str(body)[:240]


def _minimax_ok(provider: str, body: dict) -> dict:
    base = body.get("base_resp") or {}
    code = base.get("status_code")
    if code not in (0, None):
        raise ProviderError(provider, base.get("status_msg") or f"status_code {code}", code)
    return body


# ---------------------------------------------------------------- text
def chat(provider: str, model: str, messages: list[dict], max_tokens: int = 800, timeout: int = TIMEOUT) -> str:
    if provider == "minimax":
        body = _post(provider, "/text/chatcompletion_v2", {"model": model, "messages": messages, "max_tokens": max_tokens}, timeout=timeout)
        body = _minimax_ok(provider, body)
        choices = body.get("choices") or []
        if not choices:
            raise ProviderError(provider, f"無 choices：{str(body)[:160]}")
        msg = choices[0].get("message") or {}
        return (msg.get("content") or "").strip()
    body = _post(provider, "/chat/completions", {"model": model, "messages": messages, "max_tokens": max_tokens}, timeout=timeout)
    choices = body.get("choices") or []
    if not choices:
        raise ProviderError(provider, f"無 choices：{str(body)[:160]}")
    return (choices[0].get("message") or {}).get("content", "").strip()


# ---------------------------------------------------------------- image
def image(provider: str, model: str, prompt: str, size: str = "1024x1024",
          references: list[str] | None = None) -> dict:
    """回傳 {url|b64, raw}。MiniMax 回 url；阿里/火山走 OpenAI images 路由。"""
    if provider == "minimax":
        ratio = {"1280x720": "16:9", "720x1280": "9:16", "1024x1024": "1:1", "1024x768": "4:3"}.get(size, "1:1")
        body = _post(
            provider,
            "/image_generation",
            {"model": model, "prompt": prompt, "response_format": "url", "n": 1,
             "aspect_ratio": ratio, "prompt_optimizer": True},
            timeout=180,
        )
        body = _minimax_ok(provider, body)
        data = body.get("data") or {}
        urls = data.get("image_urls") or data.get("urls") or []
        if urls:
            return {"url": urls[0], "raw": body}
        if data.get("image_base64"):
            return {"b64": data["image_base64"], "raw": body}
        raise ProviderError(provider, f"圖片回應格式未知：{str(body)[:160]}")

    payload = {"model": model, "prompt": prompt, "n": 1, "size": size, "response_format": "url"}
    if provider in ("volcano", "volcano-plan"):
        payload["watermark"] = False
        if references:
            payload["image"] = references if len(references) > 1 else references[0]
    body = _post(provider, "/images/generations", payload, timeout=180)
    items = body.get("data") or []
    if items:
        item = items[0]
        return {"url": item.get("url"), "b64": item.get("b64_json"), "raw": body}
    raise ProviderError(provider, f"圖片回應格式未知：{str(body)[:160]}")


def download(url: str, timeout: int = 120) -> bytes:
    r = requests.get(url, timeout=timeout)
    if r.status_code >= 400:
        raise ProviderError("download", f"HTTP {r.status_code}")
    return r.content


# ---------------------------------------------------------------- tts
def tts(provider: str, model: str, text: str, voice: str = "male-qn-qingse") -> bytes:
    if provider != "minimax":
        raise ProviderError(provider, "目前僅 MiniMax TTS 已打通")
    body = _post(
        provider,
        "/t2a_v2",
        {
            "model": model,
            "text": text,
            "stream": False,
            "voice_setting": {"voice_id": voice, "speed": 1.0, "vol": 1.0, "pitch": 0},
            "audio_setting": {"sample_rate": 32000, "bitrate": 128000, "format": "mp3", "channel": 1},
        },
        timeout=180,
    )
    body = _minimax_ok(provider, body)
    audio = (body.get("data") or {}).get("audio")
    if not audio:
        raise ProviderError(provider, "TTS 無音訊資料")
    # MiniMax t2a_v2 回的是 hex 字串；舊版相容 base64
    if isinstance(audio, str) and len(audio) % 2 == 0 and all(c in "0123456789abcdefABCDEF" for c in audio[:64]):
        return bytes.fromhex(audio)
    return base64.b64decode(audio)


# ---------------------------------------------------------------- video
def ark_resolution(value: str) -> str:
    """MiniMax 用 768P/1080P；Ark 用小寫 720p/1080p。"""
    v = (value or "720p").lower().replace("p", "")
    if v in ("480", "720", "1080", "1440", "2160"):
        return f"{v}p"
    return "720p"


def video_create(provider: str, model: str, prompt: str, duration: int = 6,
                 resolution: str = "768P", ratio: str = "16:9",
                 first_frame_data_uri: str | None = None) -> dict:
    if provider == "minimax" and str(model).startswith("MiniMax-H3"):
        content = [{"type": "text", "text": prompt}]
        if first_frame_data_uri:
            content.append({"type": "image_url", "image_url": {"url": first_frame_data_uri}, "role": "first_frame"})
        body = _post_url(
            _minimax_v2_root() + "/v2/video_generation",
            {"model": model, "content": content, "resolution": resolution,
             "duration": int(duration), "ratio": ratio, "generate_audio": True},
            timeout=120,
        )
        task = body.get("task_id") or (body.get("task") or {}).get("id")
        if not task:
            raise ProviderError(provider, f"無 task_id：{str(body)[:160]}")
        return {"task_id": task, "raw": body, "api": "v2"}

    if provider == "minimax":
        body = _post(
            provider,
            "/video_generation",
            {"model": model, "prompt": prompt, "duration": duration, "resolution": resolution},
            timeout=90,
        )
        task = body.get("task_id")
        base = body.get("base_resp") or {}
        if base.get("status_code") not in (0, None):
            raise ProviderError(provider, base.get("status_msg") or "建立任務失敗", base.get("status_code"))
        if not task:
            raise ProviderError(provider, f"無 task_id：{str(body)[:160]}")
        return {"task_id": task, "raw": body}

    if provider == "volcano":
        body = _post(
            provider,
            "/contents/generations/tasks",
            {
                "model": model,
                "content": [{"type": "text", "text": prompt}],
                "ratio": ratio,
                "duration": duration,
                "resolution": ark_resolution(resolution),
                "watermark": False,
            },
            timeout=90,
        )
        if not body.get("id"):
            raise ProviderError(provider, f"無任務 id：{str(body)[:160]}")
        return {"task_id": body["id"], "raw": body}

    # aliyun 閘道：路由尚未確認，嘗試兩種常見路徑
    last: Exception | None = None
    for path in ("/videos/generations", "/video/generations"):
        try:
            body = _post(provider, path, {"model": model, "prompt": prompt, "duration": duration}, timeout=90)
            task = body.get("task_id") or body.get("id") or (body.get("output") or {}).get("task_id")
            if task:
                return {"task_id": task, "raw": body, "path": path}
        except ProviderError as exc:
            last = exc
    raise last or ProviderError(provider, "無法建立影片任務")


def video_poll(provider: str, task_id: str, model: str | None = None) -> dict:
    """回傳 {state: queued|running|succeeded|failed, url?, message?}。"""
    if provider == "minimax" and str(model or "").startswith("MiniMax-H3"):
        # 注意：v2 查詢是「路徑參數」，用 query string 會忽略 task_id 回傳清單
        body = _get_url(_minimax_v2_root() + f"/v2/query/video_generation/{task_id}", {})
        task = body.get("task") or body
        status = (task.get("status") or "").lower()
        if status == "succeeded":
            url = (task.get("content") or {}).get("url") or task.get("url")
            if not url:
                return {"state": "failed", "message": "成功但沒有 URL"}
            return {"state": "succeeded", "url": url, "raw": task}
        if status in ("failed", "cancelled"):
            return {"state": "failed",
                    "message": str((task.get("error") or task))[:200]}
        return {"state": "running", "raw": task}
    if provider == "minimax":
        body = _get(provider, "/query/video_generation", {"task_id": task_id})
        body = _minimax_ok(provider, body)
        status = (body.get("status") or "").strip()
        if status == "Success":
            file_id = body.get("file_id")
            if not file_id:
                return {"state": "failed", "message": "Success 但無 file_id"}
            info = _get(provider, "/files/retrieve", {"file_id": file_id})
            url = (info.get("file") or {}).get("download_url")
            if not url:
                return {"state": "failed", "message": f"取檔失敗：{str(info)[:160]}"}
            return {"state": "succeeded", "url": url, "raw": body}
        if status in ("Fail", "Failed"):
            return {"state": "failed", "message": str(body)[:200]}
        return {"state": "running" if status in ("Processing", "Queueing", "Preparing") else "queued", "raw": body}

    if provider == "volcano":
        body = _get(provider, f"/contents/generations/tasks/{task_id}")
        status = body.get("status")
        if status == "succeeded":
            url = (body.get("content") or {}).get("video_url")
            return {"state": "succeeded", "url": url, "raw": body}
        if status in ("failed", "cancelled"):
            return {"state": "failed", "message": str(body.get("error") or status)}
        return {"state": "running", "raw": body}

    body = _get(provider, f"/videos/generations/{task_id}")
    output = body.get("output") or {}
    status = (output.get("task_status") or body.get("status") or "").upper()
    if status in ("SUCCEEDED", "SUCCESS"):
        url = output.get("video_url") or (output.get("results") or [{}])[0].get("url")
        return {"state": "succeeded", "url": url, "raw": body}
    if status in ("FAILED", "CANCELED"):
        return {"state": "failed", "message": str(output.get("message") or body)[:200]}
    return {"state": "running", "raw": body}


def probe(provider: str) -> dict:
    """輕量連線測試：文字模型實打一次；Agent Plan 用圖片生成實測。"""
    started = time.time()
    if provider in ("local-wan", "local-ltx"):
        health = local_wan_health(provider)
        return {"ok": health["ok"], "model": "ltxv-2b" if provider == "local-ltx" else "wan2.2-ti2v-5b",
                "reply": json.dumps(health.get("state") or {}, ensure_ascii=False)[:120],
                "error": health.get("error"), "seconds": round(time.time() - started, 2)}
    if provider == "volcano-plan":
        try:
            res = image(provider, "doubao-seedream-5.5", "a small red dot on white background")
            return {
                "ok": True,
                "model": "doubao-seedream-5.5",
                "reply": "image url ok" if res.get("url") else "image bytes ok",
                "seconds": round(time.time() - started, 2),
            }
        except ProviderError as exc:
            return {"ok": False, "model": "doubao-seedream-5.5", "error": str(exc)[:220]}
    model = next((m["id"] for m in PROVIDERS[provider]["models"] if m["kind"] == "text"), None)
    if not model:
        return {"ok": False, "error": "沒有可測的文字模型"}
    try:
        text = chat(provider, model, [{"role": "user", "content": "回覆兩個字：READY"}], max_tokens=8)
        return {"ok": True, "model": model, "reply": text[:40], "seconds": round(time.time() - started, 2)}
    except ProviderError as exc:
        return {"ok": False, "model": model, "error": str(exc)[:200]}


# ---------------------------------------------------------------- local Wan 2.2
def local_wan_generate(
    prompt: str, *, provider: str = "local-wan", duration: float = 5, ratio: str = "16:9",
    resolution: str = "720P", negative: str = "", steps: int | None = None,
    timeout: int = 1800,
) -> dict:
    """呼叫地端同步端點（Wan 35331 / LTX 35332）；回 {url, meta}。"""
    base = _base(provider)
    payload = {
        "prompt": prompt,
        "negative_prompt": negative,
        "duration": float(duration),
        "ratio": ratio,
        "resolution": resolution,
    }
    if steps:
        payload["steps"] = int(steps)
    body = _post(provider, "/v1/videos/generations", payload, timeout=timeout)
    items = body.get("data") or []
    if not items:
        raise ProviderError(provider, f"回應沒有資料：{str(body)[:160]}")
    item = items[0]
    url = item.get("url") or ""
    return {"url": (base + url) if url.startswith("/") else url, "meta": item}


def local_wan_health(provider: str = "local-wan") -> dict:
    try:
        body = _get(provider, "/health", timeout=8)
        return {"ok": True, "state": body}
    except ProviderError as exc:
        return {"ok": False, "error": str(exc)[:200]}
