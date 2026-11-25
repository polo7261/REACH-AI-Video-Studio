"""REACH AI Video Studio — 本機影片工作室（Flask）。

啟動：.venv/bin/python app.py（預設 127.0.0.1:35350）
不影響既有 REACH-AI-Image（35320）與其他服務。
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import threading
import time
import uuid
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request, send_from_directory

from reach_video import pipeline, providers
from reach_video.config import DATA, PROJECTS, public_config
from reach_video.providers import ProviderError
from reach_video.store import (
    list_jobs,
    list_projects,
    load_job,
    load_project,
    media_dir,
    save_job,
    save_project,
)

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 512 * 1024 * 1024  # 512 MB（影片上傳）


# --------------------------------------------------------------------- pages
@app.get("/")
def page_studio():
    return render_template("studio.html")


@app.get("/api-page")
def page_api():
    return render_template("api.html")


@app.get("/docs/")
@app.get("/docs")
def page_docs():
    return render_template("docs.html", slugs=_doc_slugs())


# --------------------------------------------------------------------- config
@app.get("/api/config")
def api_config():
    return jsonify(public_config())


@app.post("/api/config/test")
def api_config_test():
    body = request.get_json(silent=True) or {}
    provider = body.get("provider")
    if provider not in ("aliyun", "minimax", "volcano", "volcano-plan", "local-wan", "local-ltx"):
        return jsonify(error="unknown provider"), 400
    return jsonify(providers.probe(provider))


# --------------------------------------------------------------------- projects
@app.get("/api/projects")
def api_projects():
    return jsonify(projects=list_projects(), jobs=list_jobs())


@app.post("/api/projects")
def api_project_create():
    body = request.get_json(silent=True) or {}
    idea = str(body.get("idea", "")).strip()
    if not idea:
        return jsonify(error="請輸入一句話故事"), 400
    try:
        duration = float(body.get("duration", 24) or 24)
    except (TypeError, ValueError):
        return jsonify(error="duration 必須是數字"), 400
    duration = max(6.0, min(180.0, duration))
    plan = pipeline.make_plan(
        title=str(body.get("title", "")).strip() or idea[:16],
        idea=idea,
        style=str(body.get("style", "電影感寫實")).strip() or "電影感寫實",
        duration=duration,
        ratio=str(body.get("ratio", "16:9")),
        character=str(body.get("character", "")).strip(),
        location=str(body.get("location", "")).strip(),
    )
    save_project(plan)
    return jsonify(plan=plan)


@app.get("/api/projects/<pid>")
def api_project_get(pid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    return jsonify(plan=plan, timeline=pipeline.timeline(plan))


@app.patch("/api/projects/<pid>/shots/<sid>")
def api_shot_update(pid: str, sid: str):
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    shot = next((s for s in plan["shots"] if s["id"] == sid), None)
    if not shot:
        return jsonify(error="找不到鏡頭"), 404
    if "positive_prompt" in body:
        shot["positive_prompt"] = str(body["positive_prompt"]).strip()[:2000]
    if "video_provider" in body:
        allowed = {"volcano", "volcano-plan", "minimax", "local-wan", "local-ltx"}
        if body["video_provider"] not in allowed:
            return jsonify(error="unsupported video_provider"), 400
        shot["video_provider"] = body["video_provider"]
    if "camera" in body and body["camera"] in pipeline.CAMERAS:
        shot["camera"] = body["camera"]
        shot["camera_zh"] = pipeline.CAMERAS[body["camera"]]["zh"]
    if "duration_seconds" in body:
        try:
            shot["duration_seconds"] = max(1.0, min(30.0, float(body["duration_seconds"])))
        except (TypeError, ValueError):
            pass
    save_project(plan)
    return jsonify(shot=shot)


def _save_generated_image(pid: str, data: bytes, url: str, prefix: str) -> str:
    name = f"{prefix}-{uuid.uuid4().hex[:6]}{_ext_from_bytes(data, url)}"
    (media_dir(pid) / name).write_bytes(data)
    return name


def _image_bytes(provider: str, model: str, prompt: str) -> tuple[bytes, str]:
    result = providers.image(provider, model, prompt)
    if result.get("b64"):
        import base64 as _b64

        return _b64.b64decode(result["b64"]), ""
    url = result.get("url") or ""
    if not url:
        raise ProviderError(provider, "回應沒有圖片 URL")
    return providers.download(url), url


@app.post("/api/projects/<pid>/characters")
def api_character_add(pid: str):
    """角色階段：產生角色設定圖（turnaround），使用者確認後才進劇本。"""
    body = request.get_json(silent=True) or {}
    name = str(body.get("name", "")).strip() or "角色"
    desc = str(body.get("description", "")).strip()
    if not desc:
        return jsonify(error="請描述角色（外觀、服裝、氣質）"), 400
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404

    prompt = (
        "character design sheet, full body, front / three-quarter / side / back views on a neutral grey background, "
        f"consistent proportions, {desc}, {plan.get('style', '')}, clean lighting, no text"
    )
    provider = body.get("provider", "volcano-plan")
    model = body.get("model", "doubao-seedream-5.5")
    try:
        data, url = _image_bytes(provider, model, prompt)
    except ProviderError as exc:
        return jsonify(error=str(exc)), 502

    cid = f"C{len(plan.get('cast') or []) + 1}"
    sheet = _save_generated_image(pid, data, url, f"sheet-{cid}")
    entry = {"id": cid, "name": name, "description": desc, "sheet": sheet,
             "status": "draft", "provider": provider, "model": model}
    plan.setdefault("cast", []).append(entry)
    plan["stage"] = "character"
    save_project(plan)
    return jsonify(character=entry, image_url=f"/media/{pid}/{sheet}")


@app.post("/api/projects/<pid>/characters/<cid>/approve")
def api_character_approve(pid: str, cid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    for c in plan.get("cast") or []:
        if c["id"] == cid:
            c["status"] = "approved"
            save_project(plan)
            return jsonify(character=c)
    return jsonify(error="找不到角色"), 404


@app.post("/api/projects/<pid>/characters/<cid>/regenerate")
def api_character_regenerate(pid: str, cid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    target = next((c for c in plan.get("cast") or [] if c["id"] == cid), None)
    if not target:
        return jsonify(error="找不到角色"), 404
    prompt = (
        "character design sheet, full body, front / three-quarter / side / back views on a neutral grey background, "
        f"consistent proportions, {target['description']}, {plan.get('style', '')}, clean lighting, no text"
    )
    try:
        data, url = _image_bytes(target.get("provider", "volcano-plan"),
                                 target.get("model", "doubao-seedream-5.5"), prompt)
    except ProviderError as exc:
        return jsonify(error=str(exc)), 502
    sheet = _save_generated_image(pid, data, url, f"sheet-{cid}")
    target["sheet"] = sheet
    target["status"] = "draft"
    save_project(plan)
    return jsonify(character=target, image_url=f"/media/{pid}/{sheet}")


@app.post("/api/projects/<pid>/script/expand")
def api_script_expand(pid: str):
    """劇本階段：依已確認角色產生劇本節拍與分鏡（LLM），並重置既有影像。"""
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    cast = [c for c in (plan.get("cast") or []) if c.get("status") == "approved"]
    if not cast:
        return jsonify(error="請先建立角色設定圖並按「確認角色」"), 400

    cast_text = "；".join(f"{c['id']} {c['name']}：{c['description']}" for c in cast)
    idea = plan.get("idea", "")
    style = plan.get("style", "")
    n = int(body.get("shots") or 4)
    prompt = (
        "你是電影編劇兼分鏡師。只輸出 JSON，不要解釋。\n"
        f"故事：{idea}\n視覺風格：{style}\n固定角色（不得改變外觀/服裝）：{cast_text}\n"
        f"輸出格式：{{\"beats\":[{{\"beat\":\"建立\",\"description\":\"...\"}}],\"shots\":[{{\"beat\":\"建立\",\"framing\":\"...\",\"camera\":\"locked|pan|tilt|dolly_in|dolly_out|tracking|crane|orbit_180|orbit_360|dolly_zoom|whip_pan|pov|handheld|drone\",\"action\":\"...\",\"lighting\":\"...\",\"positive_prompt\":\"英文提示詞，含角色外觀與運鏡\",\"character_ids\":[\"C1\"]}}]}}\n"
        f"鏡頭數 {n}，每鏡 4-8 秒，故事要完整（起承轉合）。positive_prompt 用英文，描述具體可拍。"
    )
    provider = body.get("provider", "aliyun")
    model = body.get("model", "qwen3.7-plus")
    try:
        text = providers.chat(provider, model, [{"role": "user", "content": prompt}], max_tokens=2000)
        clean = re.sub(r"```(?:json)?|```", "", text).strip()
        data = json.loads(clean)
    except (ProviderError, ValueError, json.JSONDecodeError) as exc:
        return jsonify(error=f"LLM 產生劇本失敗：{exc}"[:300]), 502

    shots_tpl = data.get("shots") or []
    if not isinstance(shots_tpl, list) or len(shots_tpl) < 2:
        return jsonify(error="LLM 回傳的分鏡格式不正確"), 502
    per = round(float(plan.get("duration_seconds", 24)) / len(shots_tpl), 2)
    shots = []
    for i, item in enumerate(shots_tpl):
        cam = item.get("camera") if item.get("camera") in pipeline.CAMERAS else "locked"
        shots.append({
            "id": f"S{i + 1:02d}",
            "beat": str(item.get("beat", ""))[:20],
            "start_seconds": round(i * per, 2),
            "duration_seconds": per,
            "framing": str(item.get("framing", ""))[:120],
            "camera": cam,
            "camera_zh": pipeline.CAMERAS[cam]["zh"],
            "action": str(item.get("action", ""))[:400],
            "lighting": str(item.get("lighting", ""))[:200],
            "character_ids": item.get("character_ids") or [],
            "positive_prompt": str(item.get("positive_prompt") or item.get("action") or "")[:2000],
            "negative_prompt": "blurry, distorted hands, extra limbs, watermark, text overlay",
            "image": None, "video": None, "video_job": None, "video_provider": "minimax",
            "status": "planned",
        })
    plan["shots"] = shots
    plan["script"] = {"beats": data.get("beats") or [], "synopsis": idea}
    plan["stage"] = "storyboard"
    save_project(plan)
    return jsonify(plan=plan, source=f"{provider}/{model}")


@app.post("/api/projects/<pid>/script")
def api_project_script(pid: str):
    """用 LLM 重寫分鏡（六鏡），失敗時原樣保留。"""
    body = request.get_json(silent=True) or {}
    provider = body.get("provider", "aliyun")
    model = body.get("model", "qwen3.7-plus")
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    idea = plan["idea"]
    style = plan["style"]
    prompt = (
        "你是電影分鏡師。把下面的一句話故事擴寫成 6 個鏡頭的 JSON 陣列，只輸出 JSON，不要解釋。\n"
        f"故事：{idea}\n風格：{style}\n"
        '每個元素格式：{"beat":"建立|衝突|轉折|收束","framing":"景別描述","camera":"locked|pan|tilt|dolly_in|dolly_out|tracking|crane|orbit_180|orbit_360|dolly_zoom|whip_pan|pov|handheld|drone",'
        '"action":"畫面動作","lighting":"光線","positive_prompt":"英文提示詞，含風格與運鏡"}'
    )
    try:
        text = providers.chat(provider, model, [{"role": "user", "content": prompt}], max_tokens=1200)
        clean = re.sub(r"```(?:json)?|```", "", text).strip()
        data = json.loads(clean)
        if not isinstance(data, list) or len(data) < 3:
            raise ValueError("LLM 回的 JSON 不是鏡頭陣列")
        per = round(plan["duration_seconds"] / len(data), 2)
        shots = []
        for i, item in enumerate(data):
            cam = item.get("camera") if item.get("camera") in pipeline.CAMERAS else "locked"
            shots.append(
                {
                    "id": f"S{i + 1:02d}",
                    "beat": str(item.get("beat", ""))[:20],
                    "start_seconds": round(i * per, 2),
                    "duration_seconds": per,
                    "framing": str(item.get("framing", ""))[:120],
                    "camera": cam,
                    "camera_zh": pipeline.CAMERAS[cam]["zh"],
                    "action": str(item.get("action", ""))[:400],
                    "lighting": str(item.get("lighting", ""))[:200],
                    "positive_prompt": str(item.get("positive_prompt") or item.get("action") or "")[:2000],
                    "negative_prompt": "blurry, distorted hands, extra limbs, watermark, text overlay",
                    "image": None,
                    "video": None,
                    "video_job": None,
                    "status": "planned",
                }
            )
        plan["shots"] = shots
        save_project(plan)
        return jsonify(plan=plan, source=f"{provider}/{model}")
    except (ProviderError, ValueError, json.JSONDecodeError) as exc:
        return jsonify(error=str(exc)[:300]), 502


# --------------------------------------------------------------------- media gen
def _ext_from_bytes(data: bytes, url: str = "") -> str:
    if data[:8].startswith(b"\x89PNG"):
        return ".png"
    if data[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if data[:4] == b"RIFF":
        return ".webp"
    suffix = Path(url.split("?")[0]).suffix.lower()
    return suffix if suffix in (".png", ".jpg", ".jpeg", ".webp") else ".jpg"


@app.post("/api/projects/<pid>/shots/<sid>/image")
def api_shot_image(pid: str, sid: str):
    body = request.get_json(silent=True) or {}
    provider = body.get("provider", "volcano")
    model = body.get("model", "doubao-seedream-5-5-261028")
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    shot = next((s for s in plan["shots"] if s["id"] == sid), None)
    if not shot:
        return jsonify(error="找不到鏡頭"), 404

    prompt = pipeline.compile_prompt(shot, plan)
    size = {"16:9": "1280x720", "9:16": "720x1280", "1:1": "1024x1024", "4:3": "1024x768"}.get(
        plan.get("ratio", "16:9"), "1024x1024")

    # 角色一致性：把設定圖當參考圖送進模型
    import base64 as _b64i

    def _sheet_uri(name: str) -> str | None:
        pth = media_dir(pid) / name
        if not pth.is_file():
            return None
        ext = pth.suffix.lower().lstrip(".") or "png"
        mime = "jpeg" if ext in ("jpg", "jpeg") else ext
        return f"data:image/{mime};base64,{_b64i.b64encode(pth.read_bytes()).decode()}"

    cast_by_id = {c["id"]: c for c in (plan.get("cast") or [])}
    refs: list[str] = []
    for cid in shot.get("character_ids") or []:
        ch = cast_by_id.get(cid)
        if ch and ch.get("sheet"):
            uri = _sheet_uri(ch["sheet"])
            if uri:
                refs.append(uri)
    if not refs:
        for ch in plan.get("cast") or []:
            if ch.get("status") == "approved" and ch.get("sheet"):
                uri = _sheet_uri(ch["sheet"])
                if uri:
                    refs.append(uri)
            if len(refs) >= 2:
                break

    if body.get("chain"):
        shots_all = plan.get("shots") or []
        idx = next((i for i, x in enumerate(shots_all) if x["id"] == sid), None)
        if idx:
            prev = shots_all[idx - 1]
            prev_video = prev.get("video")
            if prev_video:
                vpath = media_dir(pid) / prev_video
                if vpath.is_file() and shutil.which("ffmpeg"):  # 沒裝 ffmpeg 就略過接續首幀
                    chain_path = media_dir(pid) / f"chain-{sid}.jpg"
                    subprocess.run(
                        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-sseof", "-0.15",
                         "-i", str(vpath), "-frames:v", "1", "-q:v", "2", str(chain_path)],
                        check=False,
                    )
                    if chain_path.is_file():
                        refs.insert(0, f"data:image/jpeg;base64,{_b64i.b64encode(chain_path.read_bytes()).decode()}")

    try:
        result = providers.image(provider, model, prompt, size=size, references=refs or None)
        if result.get("b64"):
            import base64

            data = base64.b64decode(result["b64"])
            url = ""
        else:
            url = result.get("url") or ""
            if not url:
                raise ProviderError(provider, "回應沒有圖片 URL")
            data = providers.download(url)
    except ProviderError as exc:
        return jsonify(error=str(exc)), 502

    name = f"{sid}-{uuid.uuid4().hex[:6]}{_ext_from_bytes(data, url)}"
    (media_dir(pid) / name).write_bytes(data)
    shot["image"] = name
    shot["status"] = "image_ready"
    save_project(plan)
    return jsonify(shot=shot, image_url=f"/media/{pid}/{name}", provider=provider, model=model)


def _local_wan_worker(job: dict, plan_id: str, sid: str, prompt: str, duration: int, ratio: str, provider: str, steps: int | None = None) -> None:
    """地端服務是同步端點（數分鐘），用背景執行緒跑並更新 job/shot。"""
    try:
        if provider == "local-ltx":
            # LTX 對英文短 prompt 明顯較好；用 LLM 轉譯/濃縮，失敗就用原文
            try:
                prompt = providers.chat(
                    "aliyun", "qwen3.7-plus",
                    [{"role": "user", "content": (
                        "Convert this shot description into ONE concise English cinematic video prompt, "
                        "max 60 words, describe only what is visible on screen, no quotes, no explanations:\n" + prompt
                    )}],
                    max_tokens=160,
                ) or prompt
            except ProviderError:
                pass
        result = providers.local_wan_generate(
            prompt, provider=provider, duration=duration, ratio=ratio,
            resolution="720P" if provider == "local-wan" else "720p", steps=steps,
        )
        data = providers.download(result["url"], timeout=900)
        name = f"{sid}-{uuid.uuid4().hex[:6]}.mp4"
        (media_dir(plan_id) / name).write_bytes(data)
        job.update(state="succeeded", video=name, video_url=f"/media/{plan_id}/{name}", meta=result.get("meta"))
        plan = load_project(plan_id)
        shot = next((s for s in plan["shots"] if s["id"] == sid), None)
        if shot:
            shot["video"] = name
            shot["status"] = "video_ready"
            save_project(plan)
    except Exception as exc:  # noqa: BLE001 — 任何失敗都要落成 job.error
        job.update(state="error", message=str(exc)[:300])
    save_job(job)


@app.post("/api/projects/<pid>/shots/<sid>/video")
def api_shot_video(pid: str, sid: str):
    body = request.get_json(silent=True) or {}
    provider = body.get("provider")
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    shot = next((s for s in plan["shots"] if s["id"] == sid), None)
    if not shot:
        return jsonify(error="找不到鏡頭"), 404

    provider = provider or shot.get("video_provider") or "volcano"
    model = body.get("model") or {
        "volcano": "doubao-seedance-2-5-flash-261115",
        "volcano-plan": "doubao-seedance-2.5",
        "minimax": "MiniMax-H3",
        "local-wan": "wan2.2-ti2v-5b",
        "local-ltx": "ltxv-2b-0.9.x",
    }.get(provider, "doubao-seedance-2-5-flash-261115")
    prompt = pipeline.compile_prompt(shot, plan)
    duration = int(body.get("duration") or min(10, max(3, round(shot["duration_seconds"]))))
    duration = max(1, min(10, duration))
    steps = body.get("steps")

    if provider in ("local-wan", "local-ltx"):
        job = {
            "id": uuid.uuid4().hex[:12],
            "kind": "video",
            "provider": provider,
            "model": "ltxv-2b-0.9.x" if provider == "local-ltx" else "wan2.2-ti2v-5b",
            "project_id": pid,
            "shot_id": sid,
            "task_id": f"local-{uuid.uuid4().hex[:8]}",
            "state": "running",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration": duration,
            "note": "地端同步生成，5s 約 2–4 分鐘",
        }
        save_job(job)
        shot["video_job"] = job["id"]
        shot["status"] = "video_queued"
        save_project(plan)
        threading.Thread(
            target=_local_wan_worker,
            args=(job, pid, sid, prompt, duration, plan.get("ratio", "16:9"), provider, steps),
            daemon=True,
        ).start()
        return jsonify(job=job)

    # 各家的參數規格不同
    resolution = body.get("resolution", "720p")
    first_frame_uri = None
    if provider == "minimax":
        if str(model).startswith("MiniMax-H3"):
            duration = max(4, min(15, duration))
            resolution = body.get("resolution") or "768P"
            # I2V 一致性：若該鏡已有關鍵影格，預設當首幀
            if body.get("use_first_frame", True) and shot.get("image"):
                import base64 as _b64

                img_path = media_dir(pid) / shot["image"]
                if img_path.is_file():
                    ext = img_path.suffix.lower().lstrip(".") or "png"
                    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
                    first_frame_uri = f"data:image/{mime};base64,{_b64.b64encode(img_path.read_bytes()).decode()}"
        else:
            duration = 10 if duration > 6 else 6
            resolution = body.get("resolution") or "768P"

    try:
        created = providers.video_create(
            provider, model, prompt, duration=duration,
            resolution=resolution, ratio=plan.get("ratio", "16:9"),
            first_frame_data_uri=first_frame_uri,
        )
    except ProviderError as exc:
        return jsonify(error=str(exc)), 502

    job = {
        "id": uuid.uuid4().hex[:12],
        "kind": "video",
        "provider": provider,
        "model": model,
        "project_id": pid,
        "shot_id": sid,
        "task_id": created["task_id"],
        "state": "queued",
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration,
    }
    save_job(job)
    shot["video_job"] = job["id"]
    shot["status"] = "video_queued"
    save_project(plan)
    return jsonify(job=job)


@app.get("/api/jobs/<jid>")
def api_job_status(jid: str):
    try:
        job = load_job(jid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到任務"), 404
    if job.get("provider") in ("local-wan", "local-ltx"):
        # 背景執行緒直接更新 job 檔；不需要向 Provider 輪詢
        return jsonify(job=job)
    try:
        state = providers.video_poll(job["provider"], job["task_id"], job.get("model"))
    except ProviderError as exc:
        job["state"] = "error"
        job["message"] = str(exc)[:300]
        save_job(job)
        return jsonify(job=job)

    if state["state"] == "succeeded":
        url = state.get("url")
        if not url:
            job.update(state="error", message="模型回報成功但沒有 URL")
            save_job(job)
            return jsonify(job=job)
        try:
            data = providers.download(url, timeout=300)
        except ProviderError as exc:
            job.update(state="error", message=str(exc)[:300])
            save_job(job)
            return jsonify(job=job)
        name = f"{job['shot_id']}-{uuid.uuid4().hex[:6]}.mp4"
        (media_dir(job["project_id"]) / name).write_bytes(data)
        job.update(state="succeeded", video=name, video_url=f"/media/{job['project_id']}/{name}")
        try:
            plan = load_project(job["project_id"])
            shot = next((s for s in plan["shots"] if s["id"] == job["shot_id"]), None)
            if shot:
                shot["video"] = name
                shot["status"] = "video_ready"
                shot["video_meta"] = {
                    "provider": job["provider"],
                    "model": job.get("model"),
                    "task_id": job.get("task_id"),
                    "requested_seconds": job.get("duration"),
                    "prompt": shot.get("positive_prompt"),
                    "camera": shot.get("camera"),
                    "camera_zh": shot.get("camera_zh"),
                    "character_ids": shot.get("character_ids") or [],
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "file": name,
                    "size_bytes": (media_dir(job["project_id"]) / name).stat().st_size,
                }
                save_project(plan)
        except (FileNotFoundError, ValueError):
            pass
    else:
        job["state"] = state["state"]
        if state.get("message"):
            job["message"] = str(state["message"])[:300]
    save_job(job)
    return jsonify(job=job)


@app.post("/api/projects/<pid>/tts")
def api_project_tts(pid: str):
    body = request.get_json(silent=True) or {}
    provider = body.get("provider", "minimax")
    model = body.get("model", "speech-2.5-hd-preview")
    voice = body.get("voice", "male-qn-qingse")
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    text = str(body.get("text") or plan.get("narration") or "").strip()
    if not text:
        text = plan["idea"]
        plan["narration"] = text
    try:
        audio = providers.tts(provider, model, text[:2000], voice)
    except ProviderError as exc:
        return jsonify(error=str(exc)), 502
    name = f"narration-{uuid.uuid4().hex[:6]}.mp3"
    (media_dir(pid) / name).write_bytes(audio)
    plan["narration_audio"] = name
    save_project(plan)
    return jsonify(audio_url=f"/media/{pid}/{name}", bytes=len(audio))


@app.post("/api/projects/<pid>/narration")
def api_project_narration(pid: str):
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    plan["narration"] = str(body.get("text", ""))[:2000]
    save_project(plan)
    return jsonify(ok=True, narration=plan["narration"])


# --------------------------------------------------------------------- media/docs
ALLOWED_UPLOAD_EXT = {".mp4", ".mov", ".webm", ".png", ".jpg", ".jpeg", ".webp", ".mp3", ".wav", ".m4a"}


@app.post("/api/projects/<pid>/uploads")
def api_upload(pid: str):
    """上傳素材（影片/圖片/音訊）到專案的 media 目錄，回傳可直接播放的 URL。"""
    try:
        load_project(pid)  # 確認專案存在
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    files = request.files.getlist("files") or ([request.files["file"]] if "file" in request.files else [])
    if not files:
        return jsonify(error="沒有檔案"), 400
    saved = []
    dest_dir = media_dir(pid)
    for f in files:
        ext = Path(f.filename or "").suffix.lower()
        if ext not in ALLOWED_UPLOAD_EXT:
            return jsonify(error=f"不支援的格式：{ext or '(無副檔名)'}"), 400
        name = f"upload-{uuid.uuid4().hex[:8]}{ext}"
        f.save(dest_dir / name)
        saved.append({"name": name, "url": f"/media/{pid}/{name}",
                      "size": (dest_dir / name).stat().st_size})
    return jsonify(uploads=saved)


@app.get("/api/projects/<pid>/uploads")
def api_uploads_list(pid: str):
    try:
        load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    d = media_dir(pid)
    items = sorted(({"name": p.name, "url": f"/media/{pid}/{p.name}", "size": p.stat().st_size}
                    for p in d.glob("upload-*")), key=lambda x: x["name"], reverse=True)
    return jsonify(uploads=items)


@app.get("/api/projects/<pid>/report")
def api_project_report(pid: str):
    """每支影片／每個角色的製作說明（Markdown）。"""
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    lines = [f"# {plan.get('title')} — 製作說明", ""]
    lines += [
        f"- 一句話：{plan.get('idea')}",
        f"- 風格：{plan.get('style')}｜比例：{plan.get('ratio')}｜片長：{plan.get('duration_seconds')} 秒",
        f"- 建立：{plan.get('created_at')}｜階段：{plan.get('stage')}",
        "",
        "## 角色",
        "",
    ]
    for c in plan.get("cast") or []:
        lines += [f"### {c['id']} {c['name']}（{c.get('status')}）",
                  f"- 描述：{c.get('description')}",
                  f"- 設定圖：`{c.get('sheet')}`（{c.get('provider','volcano-plan')} / {c.get('model','doubao-seedream-5.5')}）", ""]
    lines += ["## 分鏡與素材", ""]
    for s_ in plan.get("shots") or []:
        m = s_.get("video_meta") or {}
        lines += [
            f"### {s_['id']}｜{s_.get('beat')}｜{s_.get('camera_zh')}",
            f"- 時間：{s_.get('start_seconds')}s 起，{s_.get('duration_seconds')}s",
            f"- 景別：{s_.get('framing')}｜光線：{s_.get('lighting')}",
            f"- 角色：{', '.join(s_.get('character_ids') or []) or '—'}",
            f"- Prompt：{s_.get('positive_prompt')}",
            f"- 負向：{s_.get('negative_prompt')}",
            f"- 關鍵影格：`{s_.get('image') or '—'}`",
            f"- 影片：`{s_.get('video') or '—'}`"
            + (f"（{m.get('provider')}/{m.get('model')}，task {m.get('task_id')}，{round((m.get('size_bytes') or 0)/1048576,1)} MB，{m.get('created_at')}）" if m else ""),
            "",
        ]
    text = "\n".join(lines)
    out = ROOT / "data" / "projects" / f"{pid}-report.md"
    out.write_text(text, encoding="utf-8")
    return jsonify(markdown=text, path=str(out))


@app.get("/media/<pid>/<name>")
def media_file(pid: str, name: str):
    if not re.fullmatch(r"[a-f0-9]{10}", pid) or "/" in name or ".." in name:
        abort(404)
    directory = DATA / "media" / pid
    if not directory.is_dir():
        abort(404)
    return send_from_directory(directory, name)


def _doc_slugs() -> list[str]:
    return sorted(p.stem for p in DOCS.glob("*.md"))


@app.get("/api/docs")
def api_docs_list():
    return jsonify(docs=_doc_slugs())


@app.get("/api/docs/<slug>")
def api_doc(slug: str):
    if not re.fullmatch(r"[a-z0-9\-]+", slug):
        return jsonify(error="invalid slug"), 400
    path = DOCS / f"{slug}.md"
    if not path.is_file():
        return jsonify(error="找不到文件"), 404
    return jsonify(slug=slug, markdown=path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    import waitress

    print("REACH AI Video Studio → http://0.0.0.0:35350/ (LAN)", flush=True)
    waitress.serve(app, host="0.0.0.0", port=35350, threads=8)
