"""三家 Provider 的真實呼叫（阿里閘道 / MiniMax / 火山 Ark）。

全部同步 requests；錯誤統一轉成 ProviderError（訊息含 provider 原始摘要）。
"""

from __future__ import annotations

import base64
import functools
import json
import time
from typing import Any

import requests

from . import comfyui
from .config import PROVIDERS, key_for, mark_model

TIMEOUT = 120


def _quota_like(msg: str) -> bool:
    low = str(msg).lower()
    return any(t in low for t in ("429", "quota", "額度", "balance", "餘額", "insufficient"))


def _mark_gen(fn):
    """生成函式（簽名 (provider, model, ...)）成功回寫 ok；額度類錯誤回寫 quota。"""
    @functools.wraps(fn)
    def wrapper(provider, model, *a, **kw):
        try:
            out = fn(provider, model, *a, **kw)
        except ProviderError as exc:
            if _quota_like(str(exc)):
                mark_model(provider, model, "quota", note=f"實測額度上限：{str(exc)[:100]}")
            raise
        mark_model(provider, model, "ok", note="實際生成成功")
        return out
    return wrapper


# ---------- LibTV（MCP streamable HTTP；架構中：工具名稱／參數以 live schema 為準） ----------

def _libtv_rpc(session: "requests.Session", payload: dict, timeout: int) -> dict:
    url = _base("libtv")
    try:
        r = session.post(url, json=payload, timeout=timeout)
    except requests.RequestException as exc:
        raise ProviderError("libtv", f"連線失敗：{exc.__class__.__name__}") from exc
    if r.status_code >= 400:
        raise ProviderError("libtv", _err_text(r), r.status_code)
    if "text/event-stream" in r.headers.get("Content-Type", ""):
        for line in r.text.splitlines():
            if line.startswith("data:"):
                try:
                    body = json.loads(line[5:].strip())
                except ValueError:
                    continue
                if body.get("id") == payload.get("id"):
                    return body
        raise ProviderError("libtv", "SSE 回應中沒有對應 id 的結果")
    try:
        return r.json()
    except ValueError as exc:
        raise ProviderError("libtv", f"非 JSON 回應：{r.text[:120]}") from exc


def _libtv_call(tool: str, arguments: dict, timeout: int = 600) -> dict:
    """呼叫 LibTV MCP 工具；回傳 content[0].text 的 JSON（非 JSON 時包成 {text, raw}）。"""
    token = key_for("libtv")
    if not token:
        raise ProviderError("libtv", "缺少 LIBTV_ACCESS_TOKEN（由 LibTV OAuth 取得；後端串接：架構中）")
    session = requests.Session()
    session.headers.update({**_headers("libtv"), "Accept": "application/json, text/event-stream"})
    init = _libtv_rpc(session, {
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2025-03-26", "capabilities": {},
                   "clientInfo": {"name": "reach-video", "version": "1.0"}},
    }, timeout=60)
    if "error" in init:
        raise ProviderError("libtv", f"initialize 失敗：{str(init['error'])[:160]}")
    call = _libtv_rpc(session, {
        "jsonrpc": "2.0", "id": 2, "method": "tools/call",
        "params": {"name": tool, "arguments": arguments},
    }, timeout=timeout)
    if "error" in call:
        raise ProviderError("libtv", f"{tool} 失敗：{str(call['error'])[:200]}")
    content = ((call.get("result") or {}).get("content") or [{}])[0]
    text = content.get("text") or ""
    try:
        return json.loads(text)
    except ValueError:
        return {"text": text, "raw": call.get("result")}


class ProviderError(RuntimeError):
    def __init__(self, provider: str, message: str, code: Any = None):
        super().__init__(f"[{provider}] {message}")
        self.provider = provider
        self.code = code


def _comfy(fn, *args, **kw):
    try:
        return fn(*args, **kw)
    except comfyui.ComfyError as exc:
        raise ProviderError("local-comfy", str(exc)) from exc


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
@_mark_gen
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
@_mark_gen
def image(provider: str, model: str, prompt: str, size: str = "1024x1024",
          references: list[str] | None = None) -> dict:
    """回傳 {url|b64, raw}。MiniMax 回 url；阿里/火山走 OpenAI images 路由。"""
    if provider == "local-comfy":
        return _comfy(comfyui.run_image, model, prompt, size, references)
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

    if provider == "libtv":
        res = _libtv_call("generate_image", {"prompt": prompt, "size": size, "model": model})
        if res.get("url"):
            return {"url": res["url"], "raw": res}
        if res.get("b64") or res.get("image_base64"):
            return {"b64": res.get("b64") or res.get("image_base64"), "raw": res}
        raise ProviderError("libtv", f"圖片回應格式未知：{str(res)[:160]}")

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
@_mark_gen
def tts(provider: str, model: str, text: str, voice: str = "male-qn-qingse", speed: float = 1.0,
        pitch: int = 0, vol: float = 1.0, emotion: str = "") -> bytes:
    if provider != "minimax":
        raise ProviderError(provider, "目前僅 MiniMax TTS 已打通")
    body = _post(
        provider,
        "/t2a_v2",
        {
            "model": model,
            "text": text,
            "stream": False,
            "voice_setting": {"voice_id": voice, "speed": float(speed), "vol": float(vol), "pitch": int(pitch)}
            | ({"emotion": emotion} if emotion else {}),
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


RES_ALIAS = {"2K": "1440P", "4K": "2160P"}


def video_create(provider: str, model: str, prompt: str, duration: int = 6,
                 resolution: str = "768P", ratio: str = "16:9",
                 first_frame_data_uri: str | None = None, generate_audio: bool = True) -> dict:
    resolution = RES_ALIAS.get(str(resolution).upper(), resolution)
    if provider == "minimax" and resolution.upper() in ("1440P", "2160P"):
        resolution = "1080P"  # MiniMax 最高 1080P
    if provider == "local-comfy":
        return _comfy(comfyui.video_create, model, prompt, duration, resolution, ratio, first_frame_data_uri)
    if provider == "libtv":
        res = _libtv_call("generate_video", {"prompt": prompt, "duration": int(duration),
                                             "ratio": ratio, "resolution": resolution, "count": 1}, timeout=900)
        task = res.get("task_id") or res.get("taskId") or res.get("nodeId") or res.get("node_id") or res.get("id")
        if not task:
            raise ProviderError("libtv", f"無 task_id／node id：{str(res)[:200]}")
        return {"task_id": str(task), "raw": res, "api": "mcp"}

    if provider == "minimax" and str(model).startswith("MiniMax-H3"):
        content = [{"type": "text", "text": prompt}]
        if first_frame_data_uri:
            content.append({"type": "image_url", "image_url": {"url": first_frame_data_uri}, "role": "first_frame"})
        body = _post_url(
            _minimax_v2_root() + "/v2/video_generation",
            {"model": model, "content": content, "resolution": resolution,
             "duration": int(duration), "ratio": ratio, "generate_audio": bool(generate_audio)},
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
    if provider == "libtv":
        res = _libtv_call("read_node", {"nodeId": task_id}, timeout=120)
        status = str(res.get("status") or res.get("state") or "").lower()
        if status in ("succeeded", "success", "done"):
            url = res.get("url") or res.get("video_url") or ((res.get("content") or {}).get("url"))
            if not url:
                return {"state": "failed", "message": "成功但沒有 URL"}
            if model:
                mark_model(provider, model, "ok", note="實際生成成功")
            return {"state": "succeeded", "url": url, "raw": res}
        if status in ("failed", "cancelled", "canceled"):
            msg = str(res.get("error") or res)[:200]
            if model and _quota_like(msg):
                mark_model(provider, model, "quota", note=f"實測額度上限：{msg[:100]}")
            return {"state": "failed", "message": msg}
        return {"state": "running" if status else "queued", "raw": res}

    if provider == "local-comfy":
        return _comfy(comfyui.poll, task_id, "video")
    if provider == "minimax" and str(model or "").startswith("MiniMax-H3"):
        # 注意：v2 查詢是「路徑參數」，用 query string 會忽略 task_id 回傳清單
        body = _get_url(_minimax_v2_root() + f"/v2/query/video_generation/{task_id}", {})
        task = body.get("task") or body
        status = (task.get("status") or "").lower()
        if status == "succeeded":
            url = (task.get("content") or {}).get("url") or task.get("url")
            if not url:
                return {"state": "failed", "message": "成功但沒有 URL"}
            if model:
                mark_model(provider, model, "ok", note="實際生成成功")
            return {"state": "succeeded", "url": url, "raw": task}
        if status in ("failed", "cancelled"):
            msg = str((task.get("error") or task))[:200]
            if model and _quota_like(msg):
                mark_model(provider, model, "quota", note=f"實測額度上限：{msg[:100]}")
            return {"state": "failed", "message": msg}
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
            if model:
                mark_model(provider, model, "ok", note="實際生成成功")
            return {"state": "succeeded", "url": url, "raw": body}
        if status in ("Fail", "Failed"):
            return {"state": "failed", "message": str(body)[:200]}
        return {"state": "running" if status in ("Processing", "Queueing", "Preparing") else "queued", "raw": body}

    if provider == "volcano":
        body = _get(provider, f"/contents/generations/tasks/{task_id}")
        status = body.get("status")
        if status == "succeeded":
            url = (body.get("content") or {}).get("video_url")
            if model:
                mark_model(provider, model, "ok", note="實際生成成功")
            return {"state": "succeeded", "url": url, "raw": body}
        if status in ("failed", "cancelled"):
            msg = str(body.get("error") or status)
            if model and _quota_like(msg):
                mark_model(provider, model, "quota", note=f"實測額度上限：{msg[:100]}")
            return {"state": "failed", "message": msg}
        return {"state": "running", "raw": body}

    body = _get(provider, f"/videos/generations/{task_id}")
    output = body.get("output") or {}
    status = (output.get("task_status") or body.get("status") or "").upper()
    if status in ("SUCCEEDED", "SUCCESS"):
        url = output.get("video_url") or (output.get("results") or [{}])[0].get("url")
        if model:
            mark_model(provider, model, "ok", note="實際生成成功")
        return {"state": "succeeded", "url": url, "raw": body}
    if status in ("FAILED", "CANCELED"):
        return {"state": "failed", "message": str(output.get("message") or body)[:200]}
    return {"state": "running", "raw": body}


def probe(provider: str) -> dict:
    """輕量連線測試：文字模型實打一次；Agent Plan 用圖片生成實測。"""
    started = time.time()
    if provider == "local-comfy":
        try:
            h = comfyui.health()
            return {"ok": True, "model": ", ".join(h["workflows"]) or "（尚無 workflow）",
                    "reply": f"{h['gpu']} free {h['vram_free_gb']}/{h['vram_total_gb']}GB queue {h['queue']}",
                    "seconds": round(time.time() - started, 2)}
        except comfyui.ComfyError as exc:
            return {"ok": False, "model": "comfyui", "error": str(exc)[:200]}
    if provider in ("local-wan", "local-ltx"):
        health = local_wan_health(provider)
        return {"ok": health["ok"], "model": "ltxv-2b" if provider == "local-ltx" else "wan2.2-ti2v-5b",
                "reply": json.dumps(health.get("state") or {}, ensure_ascii=False)[:120],
                "error": health.get("error"), "seconds": round(time.time() - started, 2)}
    p = PROVIDERS.get(provider) or {}
    if p.get("custom"):
        base = p["base_url"].rstrip("/")
        try:
            r = requests.get(base + "/models", headers={"Authorization": f"Bearer {key_for(provider)}"}, timeout=15)
            if r.ok:
                ids = [m.get("id", "?") for m in (r.json().get("data") or [])][:10]
                return {"ok": True, "model": "/models", "reply": ", ".join(ids) or "（空清單）",
                        "seconds": round(time.time() - started, 2)}
            model = next((m["id"] for m in p["models"] if m["kind"] == "text"), None)
            if model:
                text = chat(provider, model, [{"role": "user", "content": "回覆兩個字：READY"}], max_tokens=8)
                return {"ok": True, "model": model, "reply": text[:40], "seconds": round(time.time() - started, 2)}
            return {"ok": False, "model": "/models", "error": f"HTTP {r.status_code}"}
        except (ProviderError, requests.RequestException, ValueError) as exc:
            return {"ok": False, "model": "/models", "error": str(exc)[:200]}
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
    if provider == "libtv":
        session = requests.Session()
        try:
            session.headers.update({**_headers("libtv"), "Accept": "application/json, text/event-stream"})
            init = _libtv_rpc(session, {
                "jsonrpc": "2.0", "id": 1, "method": "initialize",
                "params": {"protocolVersion": "2025-03-26", "capabilities": {},
                           "clientInfo": {"name": "reach-video", "version": "1.0"}},
            }, timeout=30)
            if "error" in init:
                raise ProviderError("libtv", f"initialize 失敗：{str(init['error'])[:160]}")
            tools = _libtv_rpc(session, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, timeout=30)
            names = [t.get("name", "?") for t in (tools.get("result", {}).get("tools") or [])]
            return {"ok": True, "model": "MCP", "reply": f"MCP ok；tools: {', '.join(names) or '(無)'}",
                    "seconds": round(time.time() - started, 2)}
        except ProviderError as exc:
            return {"ok": False, "model": "MCP", "error": str(exc)[:200]}
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


# ---------------------------------------------------------------- 自訂 Provider
def custom_add(name: str, base_url: str, api_key: str, scope: str = "cloud", note: str = "") -> dict:
    """新增自訂 Provider：驗證連通（GET /models，失敗 fallback chat READY）→ 存 json＋.env。"""
    from reach_video.config import add_custom_entry, set_provider_config

    base = base_url.strip().rstrip("/")
    if not base.startswith("http"):
        raise ProviderError("custom", "網址格式錯誤，例：https://api.deepseek.com/v1")
    name = name.strip() or f"自訂 {base.split('//')[-1].split('/')[0]}"
    models: list[dict] = []
    probe_err = ""
    headers = {"Authorization": f"Bearer {api_key.strip()}"} if api_key.strip() else {}
    try:
        r = requests.get(base + "/models", headers=headers, timeout=15)
        if r.ok:
            models = [{"id": m.get("id", "?"), "kind": "text", "status": "untested"}
                      for m in (r.json().get("data") or [])][:30]
        else:
            probe_err = f"GET /models → HTTP {r.status_code}"
    except requests.RequestException as exc:
        probe_err = f"連線失敗：{exc.__class__.__name__}"
    pid = add_custom_entry(name, base, scope, models, note=note)
    if api_key.strip():
        set_provider_config(pid, "", api_key)
    test = probe(pid)
    return {"pid": pid, "models": models, "probe_err": probe_err, "probe": test}
