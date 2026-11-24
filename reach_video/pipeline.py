"""分鏡層：一句話 → 可追蹤的 shot list（離線、決定性；不呼叫模型）。"""

from __future__ import annotations

import hashlib
import time
from typing import Any

CAMERAS: dict[str, dict[str, str]] = {
    "locked": {"zh": "固定鏡頭", "en": "locked-off camera, no movement"},
    "pan": {"zh": "左右搖鏡", "en": "smooth horizontal pan"},
    "tilt": {"zh": "上下搖鏡", "en": "smooth vertical tilt"},
    "dolly_in": {"zh": "推軌前進", "en": "slow dolly in toward the subject"},
    "dolly_out": {"zh": "推軌後退", "en": "slow dolly out revealing the scene"},
    "tracking": {"zh": "跟拍", "en": "tracking shot following the subject"},
    "crane": {"zh": "升降鏡頭", "en": "crane up revealing the environment"},
    "orbit_180": {"zh": "180° 環繞", "en": "camera arcs 180 degrees around the subject"},
    "orbit_360": {"zh": "360° 環繞", "en": "full 360-degree orbit around the subject"},
    "bullet_time": {"zh": "子彈時間", "en": "bullet time: frozen moment, camera sweeping around"},
    "dolly_zoom": {"zh": "柯克變焦", "en": "vertigo dolly-zoom effect"},
    "whip_pan": {"zh": "甩鏡", "en": "fast whip pan with motion blur"},
    "pov": {"zh": "第一視角", "en": "first-person point of view"},
    "handheld": {"zh": "手持", "en": "handheld camera with natural shake"},
    "drone": {"zh": "無人機航拍", "en": "aerial drone shot, smooth glide"},
}

# 四鏡模板：建立 / 衝突 / 轉折 / 收束
TEMPLATE = [
    ("建立", "wide establishing shot", "drone", "清晨柔光，環境全貌"),
    ("衝突", "medium shot, subject enters frame", "tracking", "側逆光，節奏加快"),
    ("轉折", "close-up of the subject's reaction", "dolly_in", "頂光與輪廓光"),
    ("收束", "final wide shot with the subject small in frame", "orbit_180", "黃昏逆光，留白"),
]


def _slug(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]


def make_plan(
    *,
    title: str,
    idea: str,
    style: str = "電影感寫實",
    duration: float = 24.0,
    ratio: str = "16:9",
    character: str = "",
    location: str = "",
) -> dict[str, Any]:
    shots = []
    n = len(TEMPLATE)
    per = round(duration / n, 2)
    for i, (beat, framing, cam, light) in enumerate(TEMPLATE):
        start = round(i * per, 2)
        cam_zh = CAMERAS[cam]["zh"]
        parts = [
            f"{style}",
            location or "依故事設定的主場景",
            character or "主角",
            idea.strip(),
            f"{framing}，{cam_zh}",
            light,
            "cinematic lighting, film grain",
        ]
        positive = "，".join(p for p in parts if p)
        shots.append(
            {
                "id": f"S{i + 1:02d}",
                "beat": beat,
                "start_seconds": start,
                "duration_seconds": per,
                "framing": framing,
                "camera": cam,
                "camera_zh": cam_zh,
                "action": idea.strip(),
                "lighting": light,
                "positive_prompt": positive,
                "negative_prompt": "blurry, distorted hands, extra limbs, watermark, text overlay, low quality",
                "image": None,
                "video": None,
                "video_job": None,
                "video_provider": "minimax",
                "status": "planned",
            }
        )
    return {
        "schema": "reach-vidio/plan@1",
        "id": _slug(title + idea + str(time.time())),
        "title": title.strip() or "未命名影片",
        "idea": idea.strip(),
        "style": style,
        "ratio": ratio,
        "duration_seconds": duration,
        "character_lock": character,
        "location_lock": location,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cast": [],
        "script": None,
        "stage": "character",
        "shots": shots,
        "narration": None,
        "clips": [],
    }


def compile_prompt(shot: dict[str, Any], plan: dict[str, Any]) -> str:
    """把鏡頭欄位編成單段 Prompt（給影像/影片模型）。"""
    cam_en = CAMERAS.get(shot.get("camera", "locked"), CAMERAS["locked"])["en"]
    parts = [
        shot.get("positive_prompt", ""),
        f"camera: {cam_en}",
        f"style: {plan.get('style', '')}",
        f"aspect ratio {plan.get('ratio', '16:9')}",
    ]
    return "。".join(p.strip("。 ") for p in parts if p and p.strip())


def timeline(plan: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "shot_id": s["id"],
            "start": s["start_seconds"],
            "duration": s["duration_seconds"],
            "camera": s["camera_zh"],
            "status": s["status"],
        }
        for s in plan["shots"]
    ]
