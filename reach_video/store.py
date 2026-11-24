"""JSON 檔案儲存（專案、任務）。原子寫入，不覆寫他人專案目錄。"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from .config import JOBS, MEDIA, PROJECTS


def _safe(pid: str) -> str:
    if not re.fullmatch(r"[a-f0-9]{10}", pid or ""):
        raise ValueError("invalid project id")
    return pid


def _atomic_write(path: Path, obj: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def save_project(plan: dict) -> dict:
    pid = _safe(plan["id"])
    _atomic_write(PROJECTS / f"{pid}.json", plan)
    return plan


def load_project(pid: str) -> dict:
    path = PROJECTS / f"{_safe(pid)}.json"
    if not path.is_file():
        raise FileNotFoundError(pid)
    return json.loads(path.read_text(encoding="utf-8"))


def list_projects() -> list[dict]:
    out = []
    for path in sorted(PROJECTS.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
        try:
            plan = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        out.append(
            {
                "id": plan.get("id"),
                "title": plan.get("title"),
                "style": plan.get("style"),
                "ratio": plan.get("ratio"),
                "duration_seconds": plan.get("duration_seconds"),
                "created_at": plan.get("created_at"),
                "shots": len(plan.get("shots") or []),
                "images": sum(1 for s in plan.get("shots") or [] if s.get("image")),
                "videos": sum(1 for s in plan.get("shots") or [] if s.get("video")),
            }
        )
    return out


def media_dir(pid: str) -> Path:
    d = MEDIA / _safe(pid)
    d.mkdir(parents=True, exist_ok=True)
    return d


def save_job(job: dict) -> dict:
    _atomic_write(JOBS / f"{job['id']}.json", job)
    return job


def load_job(jid: str) -> dict:
    if not re.fullmatch(r"[a-f0-9]{12}", jid or ""):
        raise ValueError("invalid job id")
    path = JOBS / f"{jid}.json"
    if not path.is_file():
        raise FileNotFoundError(jid)
    return json.loads(path.read_text(encoding="utf-8"))


def list_jobs() -> list[dict]:
    out = []
    for path in sorted(JOBS.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[:30]:
        try:
            out.append(json.loads(path.read_text(encoding="utf-8")))
        except (OSError, ValueError):
            continue
    return out
