"""設定與 Provider 註冊表（金鑰只從 .env 讀，對外一律遮蔽）。"""

from __future__ import annotations

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
        "name": "MiniMax（中國站）",
        "base_url": env("MINIMAX_BASE_URL", "https://api.minimaxi.com/v1"),
        "kind": "minimax",
        "key_env": "MINIMAX_API_KEY",
        "models": [
            {"id": "MiniMax-M2.5", "kind": "text", "status": "ok", "note": "實測 status_code=0"},
            {"id": "image-01", "kind": "image", "status": "ok", "note": "實測 200，回 data[].url"},
            {"id": "image-01-live", "kind": "image", "status": "ok"},
            {"id": "speech-2.5-hd-preview", "kind": "tts", "status": "ok", "note": "實測回傳 27KB mp3"},
            {"id": "MiniMax-H3", "kind": "video", "status": "ok", "note": "v2 介面；5s 768P 約 91 秒、含音軌、支援首尾幀"},
            {"id": "MiniMax-H3-Highspeed", "kind": "video", "status": "untested"},
            {"id": "MiniMax-Hailuo-02", "kind": "video", "status": "ok", "note": "v1 介面；6/10 秒，無音軌"},
            {"id": "music-1.5", "kind": "music", "status": "untested"},
        ],
    },
    "local-wan": {
        "name": "地端 Wan2.2（192.168.0.219）",
        "base_url": env("REACH_WAN_BASE", "http://192.168.0.219:35331"),
        "kind": "local-wan",
        "key_env": "REACH_WAN_KEY",
        "catalog_note": "Wan2.2 TI2V-5B / 24fps / 20 steps / lazy load；同步生成（5s 約 2–4 分鐘）。需 GPU 空閒。",
        "models": [
            {"id": "wan2.2-ti2v-5b", "kind": "video", "status": "untested", "note": "服務未啟動；需先釋放 GPU（Strata 佔 16.3 GB）"},
        ],
    },
    "local-ltx": {
        "name": "地端 LTXV 2B（192.168.0.219）",
        "base_url": env("REACH_LTX_BASE", "http://192.168.0.219:35332"),
        "kind": "local-ltx",
        "key_env": "REACH_LTX_KEY",
        "catalog_note": "LTXV 2B（diffusers）/ 24fps / 704x400 / lazy load；3 秒約 1–3 分鐘。需 GPU 空閒。",
        "models": [
            {"id": "ltxv-2b-0.9.x", "kind": "video", "status": "untested", "note": "服務部署中；比 Wan2.2 5B 輕 2.5 倍"},
        ],
    },
    "volcano-plan": {
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
            {"id": "doubao-seed-2.1-pro", "kind": "text", "status": "license", "note": "僅供 Agent 工具使用；條款不允許一般 API 呼叫"},
        ],
    },
    "volcano": {
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

def key_for(provider_id: str) -> str:
    return env(PROVIDERS[provider_id]["key_env"])


def public_config() -> dict:
    out = []
    for pid, p in PROVIDERS.items():
        key = key_for(pid)
        out.append(
            {
                "id": pid,
                "name": p["name"],
                "base_url": p["base_url"],
                "extra": p.get("extra", {}),
                "kind": p["kind"],
                "key_state": "configured" if key else "missing",
                "key_mask": mask(key),
                "models": p["models"],
            }
        )
    return {
        "providers": out,
        "defaults": {"text": DEFAULT_TEXT, "image": DEFAULT_IMAGE, "video": DEFAULT_VIDEO, "tts": DEFAULT_TTS},
        "verified_at": "2026-11-21",
        "checked_seconds_ago": 0,
        "server_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
