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
from reach_video.config import DATA, PROJECTS, load_routing, public_config, resolve, save_routing, valid_choice
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
SKILLS = ROOT / "libtv-skills"

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 512 * 1024 * 1024  # 512 MB（影片上傳）
app.config["TEMPLATES_AUTO_RELOAD"] = True  # 改模板不必重啟


@app.context_processor
def _asset_helper():
    """/static 檔案加上修改時間當版本號，避免瀏覽器快取舊檔。"""
    def asset(name: str) -> str:
        f = ROOT / "static" / name
        v = int(f.stat().st_mtime) if f.is_file() else 0
        return f"/static/{name}?v={v}"
    return {"asset": asset}


# --------------------------------------------------------------------- pages
@app.get("/")
def page_home():
    return render_template("home.html")


@app.get("/studio")
def page_studio():
    return render_template("studio.html")


@app.get("/assets")
def page_assets():
    return render_template("assets.html")


@app.get("/canvas")
def page_canvas():
    return render_template("canvas.html")


@app.get("/director")
def page_director():
    return render_template("director.html")


@app.get("/api-page")
def page_api():
    return render_template("api.html")


@app.get("/docs/")
@app.get("/docs")
def page_docs():
    return render_template("docs.html", slugs=_doc_slugs())


@app.get("/skills/")
@app.get("/skills")
def page_skills():
    return render_template("skills.html")


def _skill_dirs() -> dict[str, dict]:
    """slug -> meta.json 內容（cn 名稱、版本、來源 UUID）。"""
    out: dict[str, dict] = {}
    if not SKILLS.is_dir():
        return out
    for d in sorted(SKILLS.iterdir()):
        meta = d / "meta.json"
        if d.is_dir() and meta.is_file():
            try:
                out[d.name] = json.loads(meta.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                out[d.name] = {}
    return out


@app.get("/api/skills")
def api_skills_list():
    items = []
    for slug, meta in _skill_dirs().items():
        sk = SKILLS / slug / "SKILL.md"
        if not sk.is_file():
            continue
        text = sk.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n\n", text, re.S)
        dm = re.search(r'description: "(.*)"', fm := (m.group(1) if m else ""))
        cover = next(
            (
                f"cover{ext}"
                for ext in (".webp", ".png", ".jpg", ".svg")
                if (SKILLS / slug / f"cover{ext}").is_file()
            ),
            None,
        )
        items.append(
            {
                "slug": slug,
                "cn": meta.get("cn_tc") or meta.get("cn") or slug,
                "cn_sc": meta.get("cn_sc") or "",
                "version": meta.get("version"),
                "description": {
                    "tc": meta.get("desc_tc") or (dm.group(1) if dm else ""),
                    "sc": meta.get("desc_sc") or meta.get("description") or "",
                    "en": meta.get("desc_en") or "",
                },
                "bytes": sk.stat().st_size,
                "cover": cover,
                "extras": sorted(
                    p.name
                    for p in (SKILLS / slug).glob("*.md")
                    if p.name != "SKILL.md"
                    and not re.search(r"\.(zh-Hans|en)\.md$", p.name)
                ),
            }
        )
    items.sort(key=lambda x: -x["bytes"])
    return jsonify(skills=items)


_SKILL_LANG_FILES = {"tc": "SKILL.md", "sc": "SKILL.zh-Hans.md", "en": "SKILL.en.md"}


@app.get("/api/skills/<slug>")
def api_skill_detail(slug: str):
    lang = request.args.get("lang", "tc")
    if lang not in _SKILL_LANG_FILES:
        return jsonify(error="invalid lang"), 400
    if not re.fullmatch(r"[a-z0-9\-]+", slug) or slug not in _skill_dirs():
        return jsonify(error="invalid slug"), 404
    path = SKILLS / slug / _SKILL_LANG_FILES[lang]
    if not path.is_file():  # 缺翻譯時退回繁中
        path = SKILLS / slug / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n\n", text, re.S)
    return jsonify(
        slug=slug,
        lang=lang,
        frontmatter=m.group(1) if m else "",
        markdown=text[m.end():] if m else text,
    )


@app.get("/api/skills/<slug>/<name>")
def api_skill_extra(slug: str, name: str):
    lang = request.args.get("lang", "tc")
    if lang not in _SKILL_LANG_FILES:
        return jsonify(error="invalid lang"), 400
    if not re.fullmatch(r"[a-z0-9\-]+", slug) or slug not in _skill_dirs():
        return jsonify(error="invalid slug"), 404
    if not re.fullmatch(r"[A-Za-z0-9._\-]+", name) or name.startswith("SKILL"):
        return jsonify(error="invalid file"), 404
    path = SKILLS / slug / name
    if lang == "sc":
        alt = path.with_name(path.stem + ".zh-Hans.md")
        if alt.is_file():
            path = alt
    elif lang == "en":
        alt = path.with_name(path.stem + ".en.md")
        if alt.is_file():
            path = alt
    if not path.is_file() or path.suffix != ".md":
        return jsonify(error="invalid file"), 404
    return jsonify(slug=slug, name=name, markdown=path.read_text(encoding="utf-8"))


@app.get("/api/skills/<slug>/cover")
def api_skill_cover(slug: str):
    if not re.fullmatch(r"[a-z0-9\-]+", slug) or slug not in _skill_dirs():
        abort(404)
    for ext in (".webp", ".png", ".jpg", ".svg"):
        path = SKILLS / slug / f"cover{ext}"
        if path.is_file():
            return send_from_directory(path.parent, path.name)
    abort(404)


# --------------------------------------------------------------------- config
@app.get("/api/config")
def api_config():
    return jsonify(public_config())


@app.get("/api/routing")
def api_routing_get():
    return jsonify(routing=load_routing())


@app.put("/api/routing")
def api_routing_put():
    body = request.get_json(silent=True) or {}
    try:
        routing = save_routing(str(body.get("step", "")), str(body.get("provider", "")), str(body.get("model", "")))
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(routing=routing)


@app.put("/api/projects/<pid>/models")
def api_project_models(pid: str):
    """專案層級模型覆寫；provider/model 留空 = 沿用全域設定。"""
    body = request.get_json(silent=True) or {}
    step = str(body.get("step", ""))
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    models = plan.setdefault("models", {})
    if not body.get("provider") and not body.get("model"):
        models.pop(step, None)
    elif valid_choice(step, str(body.get("provider")), str(body.get("model"))):
        models[step] = {"provider": body["provider"], "model": body["model"]}
    else:
        return jsonify(error="模型類型與步驟不符或不可用"), 400
    save_project(plan)
    return jsonify(models=models)


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
    provider, model = resolve("character", plan, body)
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
    provider, model = resolve("script", plan, body)
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
            "image": None, "video": None, "video_job": None, "video_provider": resolve("video", plan)[0],
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
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    provider, model = resolve("script", plan, body)
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
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    provider, model = resolve("keyframe", plan, body)
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

    route_provider, route_model = resolve("video", plan)
    provider = provider or shot.get("video_provider") or route_provider
    model = body.get("model") or (route_model if provider == route_provider else None) or {
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
        if job.get("node_id"):
            _canvas_job_finish(job)
        return jsonify(job=job)

    if state["state"] == "succeeded":
        url = state.get("url")
        if not url:
            job.update(state="error", message="模型回報成功但沒有 URL")
            save_job(job)
            if job.get("node_id"):
                _canvas_job_finish(job)
            return jsonify(job=job)
        try:
            data = providers.download(url, timeout=300)
        except ProviderError as exc:
            job.update(state="error", message=str(exc)[:300])
            save_job(job)
            if job.get("node_id"):
                _canvas_job_finish(job)
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
    if job.get("node_id"):
        _canvas_job_finish(job)
    return jsonify(job=job)


@app.post("/api/projects/<pid>/tts")
def api_project_tts(pid: str):
    body = request.get_json(silent=True) or {}
    voice = body.get("voice", "male-qn-qingse")
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    provider, model = resolve("tts", plan, body)
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


ASSET_TYPES = {".png": "image", ".jpg": "image", ".jpeg": "image", ".webp": "image",
               ".mp4": "video", ".mov": "video", ".webm": "video",
               ".mp3": "audio", ".wav": "audio", ".m4a": "audio"}


@app.get("/api/assets")
def api_assets():
    """素材庫：彙整所有專案 media 目錄下的圖片／影片／音訊（新到舊）。"""
    items = []
    for proj in list_projects():
        d = media_dir(proj["id"])
        for f in d.iterdir():
            kind = ASSET_TYPES.get(f.suffix.lower())
            if not kind or not f.is_file():
                continue
            st = f.stat()
            items.append({"name": f.name, "type": kind, "size": st.st_size, "mtime": st.st_mtime,
                          "url": f"/media/{proj['id']}/{f.name}",
                          "project_id": proj["id"], "project_title": proj.get("title") or proj["id"]})
    items.sort(key=lambda x: x["mtime"], reverse=True)
    return jsonify(assets=items[:500])


# --------------------------------------------------------------------- canvas（節點工作流）
CANVAS_KINDS = {"text": "script", "image": "keyframe", "video": "video", "audio": "tts"}
CANVAS_RATIOS = {"16:9": "1280x720", "9:16": "720x1280", "1:1": "1024x1024", "4:3": "1024x768",
                 "3:4": "768x1024", "21:9": "1512x648"}
_NODE_ID = re.compile(r"N\d{1,5}")
_MEDIA_NAME = re.compile(r"[A-Za-z0-9._-]{1,80}")


def _default_canvas() -> dict:
    return {"nodes": [{"id": "N1", "kind": "video", "title": "影片節點 1", "x": 0, "y": 0,
                       "prompt": "", "model": "", "mode": "t2v",
                       "params": {"ratio": "16:9", "duration": 5, "resolution": "768P"},
                       "output": None, "status": "idle"}],
            "edges": [], "viewport": {"x": 0, "y": 0, "k": 1}}


def _clean_canvas(raw: dict, old: dict) -> dict:
    """只接受版面與設定；生成結果（output/status/job）以伺服器既有資料為準。"""
    old_nodes = {n["id"]: n for n in (old or {}).get("nodes") or []}
    nodes = []
    for n in (raw.get("nodes") or [])[:200]:
        nid = str(n.get("id", ""))
        kind = n.get("kind")
        if not _NODE_ID.fullmatch(nid) or kind not in CANVAS_KINDS:
            continue
        prev = old_nodes.get(nid, {})
        params = n.get("params") if isinstance(n.get("params"), dict) else {}
        nodes.append({
            "id": nid, "kind": kind,
            "title": str(n.get("title", ""))[:60],
            "x": float(n.get("x") or 0), "y": float(n.get("y") or 0),
            "prompt": str(n.get("prompt", ""))[:4000],
            "model": str(n.get("model", ""))[:120],
            "mode": str(n.get("mode", ""))[:20],
            "params": {k: params[k] for k in ("ratio", "duration", "resolution", "voice") if k in params},
            "output": prev.get("output"), "status": prev.get("status", "idle"),
            "message": prev.get("message"), "job_id": prev.get("job_id"),
        })
    ids = {n["id"] for n in nodes}
    edges, seen = [], set()
    for e in (raw.get("edges") or [])[:400]:
        a, b = str(e.get("from", "")), str(e.get("to", ""))
        if a in ids and b in ids and a != b and (a, b) not in seen:
            seen.add((a, b)); edges.append({"from": a, "to": b})
    vp = raw.get("viewport") if isinstance(raw.get("viewport"), dict) else {}
    viewport = {"x": float(vp.get("x") or 0), "y": float(vp.get("y") or 0),
                "k": max(0.2, min(2.5, float(vp.get("k") or 1)))}
    return {"nodes": nodes, "edges": edges, "viewport": viewport}


@app.get("/api/projects/<pid>/canvas")
def api_canvas_get(pid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    return jsonify(canvas=plan.get("canvas") or _default_canvas(), title=plan.get("title"))


@app.put("/api/projects/<pid>/canvas")
def api_canvas_put(pid: str):
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    plan["canvas"] = _clean_canvas(body, plan.get("canvas") or {})
    save_project(plan)
    return jsonify(canvas=plan["canvas"])


def _canvas_upstream(canvas: dict, nid: str) -> tuple[list[str], list[str]]:
    """回傳上游節點的 (文字輸出, 圖片檔名)。"""
    by_id = {n["id"]: n for n in canvas.get("nodes") or []}
    texts, images = [], []
    for e in canvas.get("edges") or []:
        if e["to"] != nid:
            continue
        out = (by_id.get(e["from"]) or {}).get("output") or {}
        if out.get("type") == "text" and out.get("text"):
            texts.append(out["text"])
        elif out.get("type") == "image" and _MEDIA_NAME.fullmatch(out.get("file") or ""):
            images.append(out["file"])
    return texts, images


def _canvas_model(node: dict, plan: dict) -> tuple[str, str]:
    step = CANVAS_KINDS[node["kind"]]
    if "|" in (node.get("model") or ""):
        prov, model = node["model"].split("|", 1)
        if valid_choice(step, prov, model):
            return prov, model
    return resolve(step, plan)


def _data_uri(path: Path) -> str:
    import base64 as _b64c

    ext = path.suffix.lower().lstrip(".") or "png"
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    return f"data:image/{mime};base64,{_b64c.b64encode(path.read_bytes()).decode()}"


@app.post("/api/projects/<pid>/canvas/run")
def api_canvas_run(pid: str):
    """執行單一節點：文字／圖片／配音同步完成；影片建立任務後用 /api/jobs/<id> 輪詢。"""
    body = request.get_json(silent=True) or {}
    nid = str(body.get("node_id", ""))
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    canvas = plan.get("canvas") or {}
    node = next((n for n in canvas.get("nodes") or [] if n["id"] == nid), None)
    if not node:
        return jsonify(error="找不到節點（請先儲存畫布）"), 404

    texts, images = _canvas_upstream(canvas, nid)
    prompt = "\n".join([*texts, node.get("prompt", "")]).strip()
    if not prompt and node["kind"] != "video":
        return jsonify(error="請輸入提示詞，或連接上游文字節點"), 400
    provider, model = _canvas_model(node, plan)
    params = node.get("params") or {}
    ratio = params.get("ratio") if params.get("ratio") in CANVAS_RATIOS else "16:9"

    def done(output: dict):
        node.update(output=output, status="done", message=None, job_id=None,
                    ran={"provider": provider, "model": model, "at": time.strftime("%Y-%m-%d %H:%M:%S")})
        save_project(plan)
        return jsonify(node=node)

    try:
        if node["kind"] == "text":
            system = "你是影片編劇與提示詞工程師。依需求直接輸出內容，不要多餘說明。"
            text = providers.chat(provider, model, [{"role": "system", "content": system},
                                                    {"role": "user", "content": prompt}], max_tokens=1500)
            return done({"type": "text", "text": text.strip()})

        if node["kind"] == "image":
            refs = [_data_uri(media_dir(pid) / f) for f in images[:4]] if provider in ("volcano", "volcano-plan") else None
            result = providers.image(provider, model, prompt, size=CANVAS_RATIOS[ratio], references=refs)
            url = result.get("url") or ""
            if result.get("b64"):
                import base64 as _b64img

                data = _b64img.b64decode(result["b64"])
            elif url:
                data = providers.download(url)
            else:
                raise ProviderError(provider, "回應沒有圖片")
            name = _save_generated_image(pid, data, url, f"canvas-{nid}")
            return done({"type": "image", "file": name, "url": f"/media/{pid}/{name}"})

        if node["kind"] == "audio":
            audio = providers.tts(provider, model, prompt[:2000], params.get("voice") or "male-qn-qingse")
            name = f"canvas-{nid}-{uuid.uuid4().hex[:6]}.mp3"
            (media_dir(pid) / name).write_bytes(audio)
            return done({"type": "audio", "file": name, "url": f"/media/{pid}/{name}"})

        # video
        if provider in ("local-wan", "local-ltx"):
            return jsonify(error="地端影片目前請在專案工作室使用，畫布暫只支援雲端影片模型"), 400
        if not prompt:
            return jsonify(error="請輸入提示詞，或連接上游文字節點"), 400
        duration = int(params.get("duration") or 5)
        resolution = str(params.get("resolution") or "768P")
        first_frame = None
        if node.get("mode") == "i2v":
            if not images:
                return jsonify(error="首幀模式需要連接上游的圖片節點（並已生成圖片）"), 400
            if not (provider == "minimax" and model.startswith("MiniMax-H3")):
                return jsonify(error="目前只有 MiniMax-H3 支援首幀生成影片"), 400
            first_frame = _data_uri(media_dir(pid) / images[0])
        if provider == "minimax":
            duration = max(4, min(15, duration)) if model.startswith("MiniMax-H3") else (10 if duration > 6 else 6)
        created = providers.video_create(provider, model, prompt, duration=max(1, min(15, duration)),
                                         resolution=resolution, ratio=ratio, first_frame_data_uri=first_frame)
    except ProviderError as exc:
        node.update(status="error", message=str(exc)[:300])
        save_project(plan)
        return jsonify(error=str(exc)[:300], node=node), 502
    except (KeyError, ValueError, OSError) as exc:
        return jsonify(error=f"執行失敗：{exc}"[:300]), 500

    job = {"id": uuid.uuid4().hex[:12], "kind": "video", "provider": provider, "model": model,
           "project_id": pid, "shot_id": nid, "node_id": nid, "task_id": created["task_id"],
           "state": "queued", "created_at": time.strftime("%Y-%m-%d %H:%M:%S"), "duration": duration}
    save_job(job)
    node.update(status="running", message=None, job_id=job["id"])
    save_project(plan)
    return jsonify(node=node, job=job)


def _canvas_job_finish(job: dict) -> None:
    """影片任務結束時，把結果寫回畫布節點。"""
    try:
        plan = load_project(job["project_id"])
    except (FileNotFoundError, ValueError):
        return
    node = next((n for n in (plan.get("canvas") or {}).get("nodes") or [] if n["id"] == job["node_id"]), None)
    if not node:
        return
    if job.get("state") == "succeeded":
        node.update(status="done", message=None,
                    output={"type": "video", "file": job["video"], "url": job["video_url"]})
    elif job.get("state") in ("error", "failed"):
        node.update(status="error", message=job.get("message"))
    else:
        return
    save_project(plan)


# --------------------------------------------------------------------- AI 導演（對話）
DIRECTOR_MODES = {
    "original": (
        "你是資深影視編劇，擅長短劇與電影劇本原創。依使用者的題材與設定，產出：一句話梗概、角色表（姓名／外觀／性格）、"
        "分集或分場大綱、第一場的完整劇本（場景、動作、對白）。用繁體中文，結構清楚，使用 Markdown 標題與條列。"
    ),
    "adapt": (
        "你是影視改編編劇。使用者會提供故事或劇本原文，請保留核心情節與人物，改編成適合短影片／短劇拍攝的版本："
        "改編策略、角色表、分場大綱、關鍵場次劇本。指出刪減或合併了什麼。用繁體中文，使用 Markdown。"
    ),
    "direct": (
        "你是電影導演兼分鏡師。把使用者的故事或劇本拆成可拍攝的分鏡，每鏡寫：景別、運鏡、畫面動作、光線、時長。"
        "最後必須附上一個 ```json 區塊，格式為 {\"shots\":[{\"title\":\"鏡頭名稱\",\"prompt\":\"英文畫面提示詞（含主體外觀、場景、運鏡、光線、風格）\",\"seconds\":5}]}，"
        "3 到 8 鏡。其餘說明用繁體中文。"
    ),
}


def _director_state(plan: dict) -> dict:
    return plan.setdefault("director", {"messages": []})


def _canvas_brief(plan: dict) -> str:
    nodes = (plan.get("canvas") or {}).get("nodes") or []
    if not nodes:
        return "（畫布目前沒有節點）"
    lines = []
    for n in nodes[:30]:
        out = n.get("output") or {}
        result = out.get("text", "")[:200] if out.get("type") == "text" else (out.get("type") or "未生成")
        lines.append(f"- {n['id']} {n.get('title')}（{n['kind']}）提示詞：{(n.get('prompt') or '')[:160]}｜結果：{result}")
    return "\n".join(lines)


@app.get("/api/projects/<pid>/director")
def api_director_get(pid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    return jsonify(messages=_director_state(plan)["messages"], title=plan.get("title"))


@app.delete("/api/projects/<pid>/director")
def api_director_reset(pid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    plan["director"] = {"messages": []}
    save_project(plan)
    return jsonify(ok=True)


@app.post("/api/projects/<pid>/director/chat")
def api_director_chat(pid: str):
    body = request.get_json(silent=True) or {}
    text = str(body.get("text", "")).strip()[:8000]
    mode = body.get("mode") if body.get("mode") in DIRECTOR_MODES else "original"
    attachment = str(body.get("attachment", ""))[:60000]
    att_name = str(body.get("attachment_name", ""))[:120]
    if not text and not attachment:
        return jsonify(error="請輸入內容"), 400
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    state = _director_state(plan)

    provider, model = resolve("script", plan)
    if "|" in str(body.get("model", "")):
        prov, mid = body["model"].split("|", 1)
        if valid_choice("script", prov, mid):
            provider, model = prov, mid

    system = DIRECTOR_MODES[mode]
    if body.get("use_canvas"):
        system += "\n\n目前畫布節點：\n" + _canvas_brief(plan)
    user_content = text or "請依附件內容進行。"
    if attachment:
        user_content += f"\n\n【附件：{att_name or '故事原文'}】\n{attachment}"

    history = [{"role": m["role"], "content": m["content"][:6000]} for m in state["messages"][-12:]]
    messages = [{"role": "system", "content": system}, *history, {"role": "user", "content": user_content}]
    try:
        reply = providers.chat(provider, model, messages, max_tokens=2500).strip()
    except ProviderError as exc:
        return jsonify(error=str(exc)[:300]), 502

    now = time.strftime("%Y-%m-%d %H:%M:%S")
    shown = text or f"（上傳：{att_name or '故事原文'}）"
    if attachment:
        shown += f"\n📎 {att_name or '附件'}（{len(attachment)} 字）"
    state["messages"].append({"role": "user", "content": user_content, "display": shown, "mode": mode, "at": now})
    state["messages"].append({"role": "assistant", "content": reply, "mode": mode, "at": now,
                              "model": f"{provider}/{model}"})
    state["messages"] = state["messages"][-40:]
    save_project(plan)
    return jsonify(reply=state["messages"][-1], user=state["messages"][-2])


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
