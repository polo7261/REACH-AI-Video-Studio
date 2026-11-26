"""設定與 Provider 註冊表（金鑰只從 .env 讀，對外一律遮蔽）。"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
DATA = ROOT / "data"
PROJECTS = DATA / "projects"
JOBS = DATA / "jobs"
MEDIA = DATA / "media"
for p in (DATA, PROJECTS, JOBS, MEDIA):
    p.mkdir(parents=True, exist_ok=True)


def load_env() -> None:
    if ENV_PATH.is_file():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


load_env()


def env(key: str, default: str = "") -> str:
    return os.environ.get(key, default).strip()


def mask(secret: str, tail: int = 6) -> str:
    if not secret:
        return "(未設定)"
    if len(secret) <= tail + 8:
        return "•" * max(0, len(secret) - 4) + secret[-4:]
    return f"{secret[:6]}…{secret[-tail:]}"


# 實測結果（2026-11-21）標記在每個模型的 status：
#   ok        = 真實呼叫成功
#   quota     = 認證/路由正常，但方案用量上限
#   untested  = 尚未打通（需 endpoint id 或正確路由）
PROVIDERS: dict[str, dict] = {
    "aliyun": {
        "scope": "cloud",
        "name": "阿里雲 MaaS（token-plan 閘道）",
        "base_url": env("ALIYUN_BASE_URL", "https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"),
        "extra": {"anthropic": env("ALIYUN_ANTHROPIC_URL")},
        "kind": "openai-compatible",
        "key_env": "ALIYUN_API_KEY",
        "models": [
            {"id": "qwen3.7-plus", "kind": "text", "status": "ok", "note": "實測回覆正常"},
            {"id": "glm-5.2", "kind": "text", "status": "ok", "note": "實測回覆 READY"},
            {"id": "qwen3.6-flash", "kind": "text", "status": "ok", "note": "快速寫稿"},
            {"id": "qwen3.8-max", "kind": "text", "status": "untested", "note": "未實測"},
            {"id": "wan2.7-image", "kind": "image", "status": "untested", "note": "閘道 /images/generations 回 url error，路由待確認"},
            {"id": "wan3.0-video", "kind": "video", "status": "untested", "note": "閘道 video 路由待確認"},
            {"id": "qwen-audio-3.0-tts-plus", "kind": "tts", "status": "untested", "note": "TTS 路由待確認"},
            {"id": "qwen-image-3.0-pro", "kind": "image", "status": "untested", "note": "未實測"},
        ],
    },
    "minimax": {
        "scope": "cloud",
        "name": "MiniMax（中國站）",
        "base_url": env("MINIMAX_BASE_URL", "https://api.minimaxi.com/v1"),
        "kind": "minimax",
        "key_env": "MINIMAX_API_KEY",
        "models": [
            {"id": "MiniMax-M2.5", "kind": "text", "status": "ok", "note": "實測 status_code=0"},
            {"id": "image-01", "kind": "image", "status": "ok", "note": "實測 200，回 data[].url"},
            {"id": "image-01-live", "kind": "image", "status": "ok"},
            {"id": "speech-2.5-hd-preview", "kind": "tts", "status": "ok", "note": "實測回傳 27KB mp3"},
            {"id": "MiniMax-H3", "kind": "video", "status": "ok", "note": "v2 介面；5s 768P 約 91 秒、含音軌、支援首尾影格"},
            {"id": "MiniMax-H3-Highspeed", "kind": "video", "status": "untested"},
            {"id": "MiniMax-Hailuo-02", "kind": "video", "status": "ok", "note": "v1 介面；6/10 秒，無音軌"},
            {"id": "music-1.5", "kind": "music", "status": "untested"},
        ],
    },
    "local-wan": {
        "scope": "local",
        "name": "地端 Wan2.2（192.168.0.219）",
        "base_url": env("REACH_WAN_BASE", "http://192.168.0.219:35331"),
        "base_env": "REACH_WAN_BASE",
        "kind": "local-wan",
        "key_env": "REACH_WAN_KEY",
        "catalog_note": "Wan2.2 TI2V-5B / 24fps / 20 steps / lazy load；同步生成（5s 約 2–4 分鐘）。需 GPU 空閒。",
        "models": [
            {"id": "wan2.2-ti2v-5b", "kind": "video", "status": "untested", "note": "服務未啟動；需先釋放 GPU（Strata 佔 16.3 GB）"},
        ],
    },
    "local-ltx": {
        "scope": "local",
        "name": "地端 LTXV 2B（192.168.0.219）",
        "base_url": env("REACH_LTX_BASE", "http://192.168.0.219:35332"),
        "base_env": "REACH_LTX_BASE",
        "kind": "local-ltx",
        "key_env": "REACH_LTX_KEY",
        "catalog_note": "LTXV 2B（diffusers）/ 24fps / 704x400 / lazy load；3 秒約 1–3 分鐘。需 GPU 空閒。",
        "models": [
            {"id": "ltxv-2b-0.9.x", "kind": "video", "status": "untested", "note": "服務部署中；參數量約為 Wan2.2 5B 的 2/5"},
        ],
    },
    "local-comfy": {
        "scope": "local",
        "name": "地端 ComfyUI（192.168.0.240）",
        "base_url": env("COMFYUI_BASE_URL", "http://192.168.0.240:8188"),
        "base_env": "COMFYUI_BASE_URL",
        "kind": "comfyui",
        "key_env": "COMFYUI_API_KEY",
        "key_optional": True,
        "catalog_note": "RTX PRO 6000 96GB；模型＝workflows/comfyui/*.json（用 scripts/comfy_import.py 匯入）。",
        "models": [],
    },
    "volcano-plan": {
        "scope": "cloud",
        "name": "火山方舟 Agent Plan",
        "base_url": env("VOLC_PLAN_BASE_URL", "https://ark.cn-beijing.volces.com/api/plan/v3"),
        "kind": "ark-plan",
        "key_env": "VOLC_PLAN_API_KEY",
        "catalog_note": "專屬 base（/api/plan/v3）與專屬 key；影片模型僅 Large/Max 套餐可用。",
        "models": [
            {"id": "doubao-seedream-5.5", "kind": "image", "status": "ok", "note": "實測 200，回圖片 URL"},
            {"id": "doubao-seedream-5-0-pro", "kind": "image", "status": "untested"},
            {"id": "doubao-seedream-5.0-flash", "kind": "image", "status": "untested"},
            {"id": "doubao-seedance-2.5", "kind": "video", "status": "quota", "note": "UnsupportedModel：影片需 Large(¥500/月)/Max 套餐"},
            {"id": "doubao-seedance-2.5-flash", "kind": "video", "status": "quota", "note": "同上"},
            {"id": "doubao-seedance-2.0", "kind": "video", "status": "quota", "note": "同上"},
            {"id": "doubao-seed-2.1-pro", "kind": "text", "status": "ok", "note": "實測 200（plan 端點，帳號 ark-6332…）；一般 ark 同名需開通"},
        ],
    },
    "volcano": {
        "scope": "cloud",
        "name": "火山方舟 Ark",
        "base_url": env("VOLC_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
        "kind": "ark",
        "key_env": "VOLC_API_KEY",
        "catalog_note": "/api/v3/models 回傳 55 個可存取模型；未開通者呼叫回 ModelNotOpen。",
        "models": [
            {"id": "doubao-seedream-5-5-261028", "kind": "image", "status": "ok", "note": "實測 200，回 1024x1024 PNG（1.6 MB）"},
            {"id": "doubao-seedream-5-0-flash-260915", "kind": "image", "status": "untested"},
            {"id": "doubao-seedream-5-0-pro-260628", "kind": "image", "status": "untested"},
            {"id": "doubao-seedream-4-5-251128", "kind": "image", "status": "untested"},
            {"id": "doubao-seedance-2-5-flash-261115", "kind": "video", "status": "quota", "note": "ModelNotOpen：需在方舟控制台開通"},
            {"id": "doubao-seedance-2-5-260628", "kind": "video", "status": "quota", "note": "ModelNotOpen：需開通"},
            {"id": "doubao-seedance-2-0-mini-260615", "kind": "video", "status": "quota", "note": "ModelNotOpen：需開通"},
            {"id": "doubao-seed-2-1-pro-260915", "kind": "text", "status": "quota", "note": "ModelNotOpen：需開通"},
            {"id": "deepseek-v4-pro-ga-260813", "kind": "text", "status": "quota", "note": "ModelNotOpen：需開通"},
            {"id": "glm-5-3-flash-260828", "kind": "text", "status": "quota", "note": "ModelNotOpen：需開通"},
        ],
    },
}

DEFAULT_TEXT = {"provider": "aliyun", "model": "qwen3.7-plus"}
DEFAULT_IMAGE = {"provider": "volcano-plan", "model": "doubao-seedream-5.5"}
DEFAULT_VIDEO = {"provider": "minimax", "model": env("MINIMAX_VIDEO_MODEL") or "MiniMax-H3"}
DEFAULT_TTS = {"provider": "minimax", "model": "speech-2.5-hd-preview", "voice": "male-qn-qingse"}

# 製作流程步驟 → 需要的模型類型與預設模型
STEPS: list[dict] = [
    {"id": "script", "label": "劇本／分鏡", "kind": "text", "default": DEFAULT_TEXT},
    {"id": "character", "label": "角色設定圖", "kind": "image", "default": DEFAULT_IMAGE},
    {"id": "keyframe", "label": "分鏡關鍵影格", "kind": "image",
     "default": {"provider": "volcano", "model": "doubao-seedream-5-5-261028"}},
    {"id": "video", "label": "影片生成", "kind": "video", "default": DEFAULT_VIDEO},
    {"id": "tts", "label": "旁白配音", "kind": "tts", "default": DEFAULT_TTS},
]
STEP_MAP = {s["id"]: s for s in STEPS}
ROUTING_PATH = DATA / "routing.json"


def refresh_comfy() -> None:
    """ComfyUI 的「模型」= 內建預設（240 檔案齊全才出現）＋ workflows/comfyui/*.json。"""
    from . import comfyui

    PROVIDERS["local-comfy"]["models"] = comfyui.models_for_config()


def find_model(provider_id: str, model_id: str) -> dict | None:
    if provider_id == "local-comfy":
        refresh_comfy()
    p = PROVIDERS.get(provider_id)
    if not p:
        return None
    return next((m for m in p["models"] if m["id"] == model_id), None)


def valid_choice(step: str, provider_id: str, model_id: str) -> bool:
    s = STEP_MAP.get(step)
    m = find_model(provider_id, model_id)
    return bool(s and m and m["kind"] == s["kind"] and m.get("status") != "license")


def load_routing() -> dict:
    """全域：每個步驟目前使用的 provider/model（存在 data/routing.json）。"""
    saved: dict = {}
    if ROUTING_PATH.is_file():
        try:
            saved = json.loads(ROUTING_PATH.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            saved = {}
    out = {}
    for s in STEPS:
        c = saved.get(s["id"]) or {}
        if valid_choice(s["id"], c.get("provider", ""), c.get("model", "")):
            out[s["id"]] = {"provider": c["provider"], "model": c["model"]}
        else:
            out[s["id"]] = {"provider": s["default"]["provider"], "model": s["default"]["model"]}
    return out


def save_routing(step: str, provider_id: str, model_id: str) -> dict:
    if not valid_choice(step, provider_id, model_id):
        raise ValueError("模型類型與步驟不符或不可用")
    routing = load_routing()
    routing[step] = {"provider": provider_id, "model": model_id}
    ROUTING_PATH.write_text(json.dumps(routing, ensure_ascii=False, indent=2), encoding="utf-8")
    return routing


def resolve(step: str, plan: dict | None = None, body: dict | None = None) -> tuple[str, str]:
    """優先序：請求參數 > 專案設定 > 全域設定 > 內建預設。"""
    body = body or {}
    if body.get("provider") and body.get("model"):
        return body["provider"], body["model"]
    override = ((plan or {}).get("models") or {}).get(step) or {}
    if valid_choice(step, override.get("provider", ""), override.get("model", "")):
        return override["provider"], override["model"]
    r = load_routing()[step]
    return r["provider"], r["model"]


def set_local_base(provider_id: str, url: str) -> str:
    """地端服務網址寫回本機 .env（不經任何雲端），並即時生效。"""
    import re as _re

    p = PROVIDERS.get(provider_id) or {}
    key = p.get("base_env")
    if p.get("scope") != "local" or not key:
        raise ValueError("只能修改地端 Provider")
    url = url.strip().rstrip("/")
    if not _re.match(r"^https?://[\w.\-]+(:\d{1,5})?(/[\w./\-]*)?$", url):
        raise ValueError("網址格式錯誤，例：http://192.168.0.240:8188")
    lines = ENV_PATH.read_text(encoding="utf-8").splitlines() if ENV_PATH.is_file() else []
    for i, line in enumerate(lines):
        if line.split("=", 1)[0].strip() == key:
            lines[i] = f"{key}={url}"
            break
    else:
        lines.append(f"{key}={url}")
    ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    os.environ[key] = url
    p["base_url"] = url
    return url


def key_for(provider_id: str) -> str:
    return env(PROVIDERS[provider_id]["key_env"])


def public_config() -> dict:
    refresh_comfy()
    out = []
    for pid, p in PROVIDERS.items():
        key = key_for(pid)
        out.append(
            {
                "id": pid,
                "name": p["name"],
                "base_url": p["base_url"],
                "editable": bool(p.get("base_env")),
                "extra": p.get("extra", {}),
                "kind": p["kind"],
                "scope": p.get("scope", "cloud"),
                "key_state": "configured" if key else ("optional" if p.get("key_optional") else "missing"),
                "key_mask": mask(key),
                "models": p["models"],
            }
        )
    return {
        "providers": out,
        "defaults": {"text": DEFAULT_TEXT, "image": DEFAULT_IMAGE, "video": DEFAULT_VIDEO, "tts": DEFAULT_TTS},
        "steps": [{k: s[k] for k in ("id", "label", "kind")} for s in STEPS],
        "routing": load_routing(),
        "verified_at": "2026-11-21",
        "checked_seconds_ago": 0,
        "server_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
