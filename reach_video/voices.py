"""聲音：MiniMax 內建音色目錄、聲音克隆、專案角色聲音表。"""

from __future__ import annotations

import re
import time

import requests

from .config import PROVIDERS, key_for

# 取不到 /get_voice 時的備用清單（MiniMax 常用系統音色）
FALLBACK = [
    ("male-qn-qingse", "青澀青年"), ("male-qn-jingying", "精英青年"), ("male-qn-badao", "霸道青年"),
    ("male-qn-daxuesheng", "青年大學生"), ("female-shaonv", "少女"), ("female-yujie", "御姐"),
    ("female-chengshu", "成熟女性"), ("female-tianmei", "甜美女性"), ("presenter_male", "男性主持人"),
    ("presenter_female", "女性主持人"), ("audiobook_male_1", "男性有聲書 1"), ("audiobook_male_2", "男性有聲書 2"),
    ("audiobook_female_1", "女性有聲書 1"), ("audiobook_female_2", "女性有聲書 2"),
    ("clever_boy", "聰明男童"), ("cute_boy", "可愛男童"), ("lovely_girl", "萌萌女童"), ("cartoon_pig", "卡通豬小琪"),
]
EMOTIONS = ["", "neutral", "happy", "sad", "angry", "fearful", "disgusted", "surprised"]
_CACHE: dict = {"at": 0.0, "data": None}
VOICE_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{7,255}$")


class VoiceError(RuntimeError):
    pass


def _base() -> str:
    return PROVIDERS["minimax"]["base_url"].rstrip("/")


def _auth() -> dict:
    key = key_for("minimax")
    if not key:
        raise VoiceError("MiniMax API key 未設定")
    return {"Authorization": f"Bearer {key}"}


def _ok(body: dict) -> dict:
    base = body.get("base_resp") or {}
    if base.get("status_code") not in (0, None):
        raise VoiceError(f"{base.get('status_msg') or '失敗'}（{base.get('status_code')}）")
    return body


def catalog(refresh: bool = False) -> dict:
    """{builtin:[{id,name,desc}], cloned:[{id,name,desc}], source:'api'|'fallback'}"""
    if not refresh and _CACHE["data"] and time.time() - _CACHE["at"] < 3600:
        return _CACHE["data"]
    data = {"builtin": [{"id": i, "name": n, "desc": ""} for i, n in FALLBACK], "cloned": [], "source": "fallback"}
    try:
        r = requests.post(_base() + "/get_voice", headers=_auth() | {"Content-Type": "application/json"},
                          json={"voice_type": "all"}, timeout=20)
        body = _ok(r.json())
        sys_v = body.get("system_voice") or []
        if sys_v:
            data["builtin"] = [{"id": v.get("voice_id"), "name": v.get("voice_name") or v.get("voice_id"),
                                "desc": "、".join(v.get("description") or []) if isinstance(v.get("description"), list)
                                else str(v.get("description") or "")} for v in sys_v if v.get("voice_id")]
        data["cloned"] = [{"id": v.get("voice_id"), "name": v.get("voice_id"),
                           "desc": "、".join(v.get("description") or []) if isinstance(v.get("description"), list)
                           else str(v.get("description") or "")}
                          for v in (body.get("voice_cloning") or []) + (body.get("voice_generation") or []) if v.get("voice_id")]
        data["source"] = "api"
    except (requests.RequestException, ValueError, VoiceError) as exc:
        data["error"] = str(exc)[:200]
    _CACHE.update(at=time.time(), data=data)
    return data


def clone(data: bytes, filename: str, voice_id: str, preview_text: str = "", model: str = "speech-2.5-hd-preview") -> dict:
    """上傳音檔 → 建立克隆音色。MiniMax：音檔 10 秒～5 分鐘、mp3/m4a/wav；首次使用該音色時計費。"""
    if not VOICE_ID.fullmatch(voice_id or ""):
        raise VoiceError("音色 ID 需英文字母開頭、至少 8 碼，只能含英數、- 或 _")
    try:
        up = requests.post(_base() + "/files/upload", headers=_auth(), data={"purpose": "voice_clone"},
                           files={"file": (filename, data)}, timeout=120)
        body = _ok(up.json())
        fid = (body.get("file") or {}).get("file_id")
        if not fid:
            raise VoiceError(f"上傳失敗：{str(body)[:160]}")
        payload = {"file_id": fid, "voice_id": voice_id, "need_noise_reduction": True, "need_volume_normalization": True}
        if preview_text:
            payload |= {"text": preview_text[:300], "model": model}
        r = requests.post(_base() + "/voice_clone", headers=_auth() | {"Content-Type": "application/json"},
                          json=payload, timeout=180)
        res = _ok(r.json())
    except requests.RequestException as exc:
        raise VoiceError(f"連線失敗：{exc.__class__.__name__}") from exc
    except ValueError as exc:
        raise VoiceError("回應不是 JSON") from exc
    _CACHE["at"] = 0  # 讓目錄重新整理
    return {"voice_id": voice_id, "demo_audio": res.get("demo_audio") or "", "input_sensitive": res.get("input_sensitive")}


# ---------------------------------------------------------------- 專案角色聲音表
DEFAULT_ROLE = {"voice_id": "male-qn-qingse", "speed": 1.0, "pitch": 0, "vol": 1.0, "emotion": "", "locked": False}


def clean_role(r: dict) -> dict | None:
    rid = re.sub(r"[^\w-]", "", str(r.get("id") or ""))[:40]
    if not rid:
        return None

    def num(k, lo, hi, d):
        try:
            return max(lo, min(hi, float(r.get(k, d))))
        except (TypeError, ValueError):
            return d
    vid = str(r.get("voice_id") or DEFAULT_ROLE["voice_id"])[:120]
    return {"id": rid, "name": str(r.get("name") or rid)[:40], "desc": str(r.get("desc") or "")[:200],
            "voice_id": vid, "speed": num("speed", 0.5, 2.0, 1.0), "pitch": int(num("pitch", -12, 12, 0)),
            "vol": num("vol", 0.1, 3.0, 1.0),
            "emotion": r.get("emotion") if r.get("emotion") in EMOTIONS else "",
            "locked": bool(r.get("locked")), "reason": str(r.get("reason") or "")[:200]}


def roles(plan: dict) -> list[dict]:
    cast = (plan.get("voices") or {}).get("roles")
    if cast:
        return cast
    return [clean_role({"id": "narrator", "name": "旁白", "desc": "畫外音／口白", "voice_id": "presenter_male"})]


def role_map(plan: dict) -> dict:
    return {r["id"]: r for r in roles(plan)}
