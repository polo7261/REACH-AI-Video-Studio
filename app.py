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

from flask import Flask, abort, jsonify, redirect, render_template, request, send_from_directory

from reach_video import pipeline, providers, voices
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
SKILLS = ROOT / "skill"

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
    return {"asset": asset, "PLUGIN_DL": PLUGIN_DL}


# Blender 插件 zip 的下載直鏈（GitHub Release 資產；attachment header 直接觸發下載）
# 注意：repo 目前是 private——匿名訪客需 repo 公開（或協作者已登入 GitHub）才下載得到。
PLUGIN_DL = {
    "macos": "https://github.com/polo7261/REACH-AI-Video-Studio/releases/download/plugins-v0.1.26/blender-macos.zip",
    "windows": "https://github.com/polo7261/REACH-AI-Video-Studio/releases/download/plugins-v0.1.26/blender-windows-x64.zip",
}


@app.get("/download/blender")
def download_blender():
    """依訪客 User-Agent 直接導到對應平台的插件 zip；無法判別（如 Linux）→ /plugins 選擇頁。"""
    ua = request.headers.get("User-Agent", "")
    if "Windows" in ua:
        return redirect(PLUGIN_DL["windows"])
    if "Mac OS" in ua or "Macintosh" in ua:
        return redirect(PLUGIN_DL["macos"])
    return redirect("/plugins")


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


@app.get("/workbench")
def page_workbench():
    return render_template("workbench.html")


@app.get("/director")
def page_director():
    return render_template("director.html")


@app.get("/plugins")
def page_plugins():
    return render_template("plugins.html")


@app.get("/libtv")
def page_libtv():
    return render_template("libtv.html")


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
    """slug -> {meta, dir, category}，結構 skill/<分類>/<slug>/。"""
    out: dict[str, dict] = {}
    if not SKILLS.is_dir():
        return out
    for cat in sorted(SKILLS.iterdir()):
        if not cat.is_dir():
            continue
        for d in sorted(cat.iterdir()):
            meta = d / "meta.json"
            if d.is_dir() and meta.is_file():
                try:
                    m = json.loads(meta.read_text(encoding="utf-8"))
                except (ValueError, OSError):
                    m = {}
                out[d.name] = {"meta": m, "dir": d, "category": cat.name}
    return out


@app.get("/api/skills")
def api_skills_list():
    items = []
    for slug, info in _skill_dirs().items():
        meta, d = info["meta"], info["dir"]
        sk = d / "SKILL.md"
        if not sk.is_file():
            continue
        text = sk.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n\n", text, re.S)
        dm = re.search(r'description: "(.*)"', fm := (m.group(1) if m else ""))
        cover = next(
            (
                f"cover{ext}"
                for ext in (".webp", ".png", ".jpg", ".jpeg", ".svg")
                if (d / f"cover{ext}").is_file()
            ),
            None,
        )
        items.append(
            {
                "slug": slug,
                "category": info["category"],
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
                    for p in d.glob("*.md")
                    if p.name != "SKILL.md"
                    and not re.search(r"\.(zh-Hans|en)\.md$", p.name)
                ),
            }
        )
    items.sort(key=lambda x: (x["category"], -x["bytes"]))
    return jsonify(skills=items)


_SKILL_LANG_FILES = {"tc": "SKILL.md", "sc": "SKILL.zh-Hans.md", "en": "SKILL.en.md"}


@app.get("/api/skills/<slug>")
def api_skill_detail(slug: str):
    lang = request.args.get("lang", "tc")
    if lang not in _SKILL_LANG_FILES:
        return jsonify(error="invalid lang"), 400
    info = _skill_dirs().get(slug)
    if not re.fullmatch(r"[a-z0-9\-]+", slug) or info is None:
        return jsonify(error="invalid slug"), 404
    path = info["dir"] / _SKILL_LANG_FILES[lang]
    if not path.is_file():  # 缺翻譯時退回繁中
        path = info["dir"] / "SKILL.md"
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
    info = _skill_dirs().get(slug)
    if not re.fullmatch(r"[a-z0-9\-]+", slug) or info is None:
        return jsonify(error="invalid slug"), 404
    if not re.fullmatch(r"[A-Za-z0-9._\-]+", name) or name.startswith("SKILL"):
        return jsonify(error="invalid file"), 404
    path = info["dir"] / name
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
    info = _skill_dirs().get(slug)
    if not re.fullmatch(r"[a-z0-9\-]+", slug) or info is None:
        abort(404)
    for ext in (".webp", ".png", ".jpg", ".jpeg", ".svg"):
        path = info["dir"] / f"cover{ext}"
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


@app.put("/api/config/local")
def api_config_local():
    """Provider 網址／金鑰：存本機 .env（雲端、地端皆可），即時生效。"""
    from reach_video.config import set_provider_config

    body = request.get_json(silent=True) or {}
    try:
        out = set_provider_config(str(body.get("provider", "")),
                                  str(body.get("base_url", "")),
                                  str(body.get("api_key", "")))
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(ok=True, **out)


@app.get("/api/comfy/models")
def api_comfy_models():
    try:
        return jsonify(ok=True, models=providers.comfyui.installed())
    except providers.comfyui.ComfyError as exc:
        return jsonify(ok=False, error=str(exc)[:200]), 502


@app.post("/api/comfy/workflows")
def api_comfy_import():
    """上傳 ComfyUI「Export (API)」JSON → workflows/comfyui/<id>.json。"""
    import importlib.util

    f = request.files.get("file")
    wid = re.sub(r"[^\w.\-]", "-", (request.form.get("id") or "").strip())[:60]
    kind = request.form.get("kind", "image")
    if not f or not wid or kind not in ("image", "video"):
        return jsonify(error="需要 file、id、kind(image|video)"), 400
    try:
        graph = json.loads(f.read().decode("utf-8"))
        spec_mod = importlib.util.spec_from_file_location("comfy_import", Path(__file__).parent / "scripts" / "comfy_import.py")
        mod = importlib.util.module_from_spec(spec_mod)
        spec_mod.loader.exec_module(mod)
        spec, log = mod.build_spec(graph, wid, kind, request.form.get("note", ""))
    except (ValueError, UnicodeDecodeError) as exc:
        return jsonify(error=str(exc)[:300]), 400
    out = Path(__file__).parent / "workflows" / "comfyui" / f"{wid}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    return jsonify(ok=True, id=wid, log=log)


# --------------------------------------------------------------------- voices
@app.get("/api/voices")
def api_voices():
    data = voices.catalog(refresh=request.args.get("refresh") == "1")
    return jsonify(**data, emotions=voices.EMOTIONS)


@app.post("/api/voices/clone")
def api_voice_clone():
    f = request.files.get("file")
    if not f:
        return jsonify(error="請選擇音檔（10 秒～5 分鐘，mp3/m4a/wav）"), 400
    data = f.read()
    if len(data) > 20 * 1024 * 1024:
        return jsonify(error="音檔超過 20MB"), 400
    try:
        res = voices.clone(data, f.filename or "voice.mp3", str(request.form.get("voice_id") or "").strip(),
                           str(request.form.get("preview_text") or ""))
    except voices.VoiceError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(ok=True, **res)


@app.get("/api/projects/<pid>/voices")
def api_project_voices(pid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    return jsonify(roles=voices.roles(plan))


@app.put("/api/projects/<pid>/voices")
def api_project_voices_put(pid: str):
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    roles = [r for r in (voices.clean_role(x) for x in (body.get("roles") or [])[:30] if isinstance(x, dict)) if r]
    seen, uniq = set(), []
    for r in roles:
        if r["id"] not in seen:
            seen.add(r["id"]); uniq.append(r)
    plan["voices"] = {"roles": uniq}
    save_project(plan)
    return jsonify(roles=uniq)


@app.post("/api/projects/<pid>/voices/preview")
def api_project_voice_preview(pid: str):
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    role = voices.clean_role(body.get("role") or {}) or voices.clean_role({"id": "narrator"})
    text = str(body.get("text") or "").strip()[:200] or f"你好，我是{role['name']}。這是我在這部片裡的聲音。"
    prov, model = resolve("tts", plan)
    try:
        name = _tts_cached(pid, prov, model, text, role)
    except ProviderError as exc:
        return jsonify(error=str(exc)[:300]), 502
    return jsonify(url=f"/media/{pid}/{name}")


AUDIO_PLAN_PROMPT = """你是影片的聲音導演。依劇本與每段畫面，決定「角色聲音表」與「每段台詞／口白」。
只輸出 JSON（不要其他文字）：
{"roles":[{"id":"英文小寫id","name":"中文角色名","desc":"年齡性別個性","voice_id":"從音色清單挑","speed":1.0,"emotion":"","reason":"為何選這個音色"}],
 "clips":[{"node_id":"N3","orig":"keep|duck|mute","lines":[{"role":"角色id","text":"台詞"}]}]}
規則：
1. 一定要有 id 為 narrator 的旁白角色；主角、配角各一個 id。同一角色整部片只用一個音色，音色需符合年齡、性別、個性。
2. voice_id 只能從【音色清單】中挑；標記「鎖定」的角色維持原音色不要改。
3. 台詞要符合劇本與該段畫面，中文約每秒 4 字，總長不可超過該段秒數減 0.5 秒；不需要台詞的段落 lines 給空陣列。
4. 有台詞或口白的段落 orig 用 duck（原聲壓低）；畫面原聲是重點（環境音、音樂）時用 keep；原聲雜亂時用 mute。
5. emotion 只能是：""、neutral、happy、sad、angry、fearful、disgusted、surprised。"""


@app.post("/api/projects/<pid>/canvas/<nid>/audio-plan")
def api_audio_plan(pid: str, nid: str):
    """AI 依劇本＋場景：配角色音色、寫每段台詞／口白，寫回專案聲音表與合成節點。"""
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    canvas = plan.get("canvas") or {}
    node = next((n for n in canvas.get("nodes") or [] if n["id"] == nid and n["kind"] == "compose"), None)
    if not node:
        return jsonify(error="找不到合成節點"), 404
    clips = _compose_clips(canvas, node)
    if not clips:
        return jsonify(error="請先把影片節點連到合成節點"), 400
    seg = []
    for c in clips:
        n = c["node"]
        f = (n.get("output") or {}).get("file") or ""
        dur = _ffprobe(media_dir(pid) / f)[0] if f and (media_dir(pid) / f).is_file() else float((n.get("params") or {}).get("duration") or 5)
        dur = max(0.5, dur - c["cut_in"] - c["cut_out"])
        seg.append({"node_id": n["id"], "title": n.get("title"), "seconds": round(dur, 1), "畫面": (n.get("prompt") or "")[:600]})
    sessions = ((plan.get("workbench") or {}).get("sessions") or {}).values()
    script = next((x.get("script") for x in sessions if x.get("script")), "") or json.dumps(plan.get("script") or {}, ensure_ascii=False)
    cat = voices.catalog()
    vlist = "\n".join(f"- {v['id']}：{v['name']} {v['desc']}"[:120] for v in cat["builtin"][:80])
    vlist += "".join(f"\n- {v['id']}：（克隆音色）{v['desc']}"[:120] for v in cat["cloned"][:30])
    current = voices.roles(plan)
    locked = [r for r in current if r.get("locked")]
    user = (f"【劇本】\n{script[:8000]}\n\n【專案】{plan.get('title')}；角色設定：{json.dumps(plan.get('cast') or [], ensure_ascii=False)[:1500]}\n\n"
            f"【鎖定角色】{json.dumps([{k: r[k] for k in ('id', 'name', 'voice_id')} for r in locked], ensure_ascii=False)}\n\n"
            f"【音色清單】\n{vlist}\n\n【段落】\n{json.dumps(seg, ensure_ascii=False)}")
    prov, model = resolve("script", plan)
    try:
        raw = providers.chat(prov, model, [{"role": "system", "content": AUDIO_PLAN_PROMPT}, {"role": "user", "content": user}],
                             max_tokens=3000, timeout=180)
    except ProviderError as exc:
        return jsonify(error=str(exc)[:300]), 502
    data = _wb_json(raw) or {}
    valid_ids = {v["id"] for v in cat["builtin"] + cat["cloned"]}
    roles = {r["id"]: r for r in current}
    for x in data.get("roles") or []:
        r = voices.clean_role(x if isinstance(x, dict) else {})
        if not r:
            continue
        old = roles.get(r["id"])
        if old and old.get("locked"):
            continue
        if r["voice_id"] not in valid_ids and cat["source"] == "api":
            r["voice_id"] = (old or {}).get("voice_id") or voices.DEFAULT_ROLE["voice_id"]
        roles[r["id"]] = r
    if "narrator" not in roles:
        roles["narrator"] = voices.roles({})[0]
    plan["voices"] = {"roles": list(roles.values())}
    by_node = {x.get("node_id"): x for x in data.get("clips") or [] if isinstance(x, dict)}
    pc = node.setdefault("params", {}).setdefault("clips", [])
    for c in clips:
        x = by_node.get(c["node"]["id"]) or {}
        ent = next((e for e in pc if e["id"] == c["node"]["id"]), None)
        if ent is None:
            ent = {"id": c["node"]["id"], "on": True, "cut_in": 0.0, "cut_out": 0.0}
            pc.append(ent)
        ent["lines"] = [{"role": ln.get("role") if ln.get("role") in roles else "narrator", "text": str(ln.get("text") or "")[:500]}
                        for ln in (x.get("lines") or []) if isinstance(ln, dict) and ln.get("text")][:20]
        ent["orig"] = x.get("orig") if x.get("orig") in ("keep", "duck", "mute") else ("duck" if ent["lines"] else "keep")
    save_project(plan)
    return jsonify(roles=plan["voices"]["roles"], node=node)


@app.post("/api/config/test")
def api_config_test():
    body = request.get_json(silent=True) or {}
    provider = body.get("provider")
    if provider not in ("aliyun", "minimax", "volcano", "volcano-plan", "local-wan", "local-ltx", "local-comfy", "libtv"):
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
        allowed = {"volcano", "volcano-plan", "minimax", "local-wan", "local-ltx", "local-comfy"}
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
                if vpath.is_file() and _ffbin("ffmpeg"):  # 沒裝 ffmpeg 就略過接續首幀
                    chain_path = media_dir(pid) / f"chain-{sid}.jpg"
                    subprocess.run(
                        [_ffbin("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y", "-sseof", "-0.15",
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
        "local-comfy": providers.comfyui.default("video") or "",
    }.get(provider, "doubao-seedance-2-5-flash-261115")
    prompt = pipeline.compile_prompt(shot, plan)
    duration = int(body.get("duration") or min(30, max(3, round(shot["duration_seconds"]))))
    duration = max(1, min(30, duration))
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
    elif provider == "local-comfy" and body.get("use_first_frame", True) and shot.get("image"):
        img_path = media_dir(pid) / shot["image"]
        if img_path.is_file():
            first_frame_uri = _data_uri(img_path)  # workflow 沒有 {{image}} 時會自動忽略

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
        vext = ".webm" if ".webm" in (url or "").lower() else ".mp4"
        name = f"{job['shot_id']}-{uuid.uuid4().hex[:6]}{vext}"
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
CANVAS_KINDS = {"text": "script", "image": "keyframe", "video": "video", "audio": "tts", "compose": ""}
COMPOSE_TRANSITIONS = {"cut", "fade", "fadeblack", "dissolve"}
CANVAS_RATIOS = {"16:9": "1280x720", "9:16": "720x1280", "1:1": "1024x1024", "4:3": "1024x768",
                 "3:4": "768x1024", "21:9": "1512x648"}
_NODE_ID = re.compile(r"N\d{1,5}")
_MEDIA_NAME = re.compile(r"[A-Za-z0-9._-]{1,80}")


def _clean_params(kind: str, params: dict) -> dict:
    out = {k: params[k] for k in ("ratio", "duration", "resolution", "voice") if k in params}
    if kind == "video" and "audio" in params:
        out["audio"] = params["audio"] is not False
    if kind == "compose":
        out = {"transition": params.get("transition") if params.get("transition") in COMPOSE_TRANSITIONS else "cut"}
        try:
            out["tdur"] = max(0.2, min(2.0, float(params.get("tdur") or 0.5)))
        except (TypeError, ValueError):
            out["tdur"] = 0.5
        clips = []
        for c in (params.get("clips") or [])[:60]:
            if not isinstance(c, dict) or not _NODE_ID.fullmatch(str(c.get("id", ""))):
                continue
            def num(v):
                try:
                    return max(0.0, float(v or 0))
                except (TypeError, ValueError):
                    return 0.0
            lines = []
            for ln in (c.get("lines") or [])[:20]:
                if isinstance(ln, dict) and str(ln.get("text") or "").strip():
                    lines.append({"role": re.sub(r"[^\w-]", "", str(ln.get("role") or "narrator"))[:40] or "narrator",
                                  "text": str(ln["text"]).strip()[:500]})
            clips.append({"id": str(c["id"]), "on": c.get("on", True) is not False,
                          "cut_in": num(c.get("cut_in")), "cut_out": num(c.get("cut_out")),
                          "orig": c.get("orig") if c.get("orig") in ("keep", "duck", "mute") else "keep",
                          "lines": lines})
        out["clips"] = clips
    return out


def _ffbin(name: str) -> str | None:
    """找 ffmpeg/ffprobe：PATH 找不到時，再找 Homebrew 常見路徑（Finder／背景啟動時 PATH 常不完整）。"""
    hit = shutil.which(name)
    if hit:
        return hit
    for d in ("/usr/local/bin", "/opt/homebrew/bin", str(Path.home() / ".homebrew/bin"), "/usr/bin"):
        p = Path(d) / name
        if p.is_file():
            return str(p)
    return None


def _ffprobe(path: Path) -> tuple[float, bool, tuple[int, int]]:
    """回傳（秒數, 是否有音軌, (寬, 高)）。"""
    import subprocess as _sp

    r = _sp.run([_ffbin("ffprobe") or "ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height",
                 "-show_entries", "format=duration", "-of", "json", str(path)],
                capture_output=True, text=True, timeout=30)
    info = json.loads(r.stdout or "{}")
    streams = info.get("streams") or []
    v = next((x for x in streams if x.get("codec_type") == "video"), {})
    return (float((info.get("format") or {}).get("duration") or 0),
            any(x.get("codec_type") == "audio" for x in streams),
            (int(v.get("width") or 1280), int(v.get("height") or 720)))


def _compose_clips(canvas: dict, node: dict) -> list[dict]:
    """上游影片節點，依面板排序；沒排過的依「分鏡 N」號碼、再依位置。"""
    by_id = {n["id"]: n for n in canvas.get("nodes") or []}
    ups = [by_id[e["from"]] for e in canvas.get("edges") or [] if e["to"] == node["id"] and e["from"] in by_id]
    ups = [n for n in ups if n["kind"] == "video" and (n.get("output") or {}).get("type") == "video"]
    def natural(n):
        m = re.search(r"分鏡\s*(\d+)", n.get("title") or "")
        return (int(m.group(1)) if m else 9999, n.get("y", 0), n.get("x", 0))
    saved = {c["id"]: (i, c) for i, c in enumerate((node.get("params") or {}).get("clips") or [])}
    ups.sort(key=lambda n: (saved[n["id"]][0] if n["id"] in saved else 10_000, natural(n)))
    out = []
    for n in ups:
        c = saved.get(n["id"], (0, {}))[1]
        out.append({"node": n, "on": c.get("on", True), "cut_in": c.get("cut_in", 0.0), "cut_out": c.get("cut_out", 0.0),
                    "orig": c.get("orig", "keep"), "lines": c.get("lines") or []})
    return out


def _compose_run(pid: str, canvas: dict, node: dict) -> dict:
    import subprocess as _sp

    ffmpeg = _ffbin("ffmpeg")
    if not ffmpeg or not _ffbin("ffprobe"):
        raise RuntimeError("伺服器找不到 ffmpeg／ffprobe（brew install ffmpeg）")
    clips = [c for c in _compose_clips(canvas, node) if c["on"]]
    if not clips:
        raise RuntimeError("請把已生成完成的影片節點連到這個合成節點")
    params = node.get("params") or {}
    trans, tdur = params.get("transition", "cut"), float(params.get("tdur") or 0.5)
    mdir = media_dir(pid)
    items = []
    for c in clips:
        f = (c["node"]["output"] or {}).get("file") or ""
        path = mdir / f
        if not _MEDIA_NAME.fullmatch(f) or not path.is_file():
            raise RuntimeError(f"{c['node'].get('title')} 的影片檔不存在")
        dur, has_a, size = _ffprobe(path)
        a = min(c["cut_in"], max(0.0, dur - 0.5))
        b = max(a + 0.5, dur - c["cut_out"])
        items.append({"path": path, "a": a, "b": b, "d": b - a, "audio": has_a, "size": size,
                      "vol": {"keep": 1.0, "duck": 0.25, "mute": 0.0}.get(c.get("orig"), 1.0), "lines": c.get("lines") or []})
    W, H = items[0]["size"]
    W, H = W - W % 2, H - H % 2
    if trans != "cut" and len(items) > 1:
        tdur = min(tdur, min(it["d"] for it in items) / 2)
    args = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y"]
    for it in items:
        args += ["-i", str(it["path"])]
    for it in items:  # 沒音軌的片段補靜音
        if not it["audio"]:
            args += ["-f", "lavfi", "-t", f"{it['d']:.3f}", "-i", "anullsrc=r=44100:cl=stereo"]
    fc, silent_idx = [], len(items)
    for i, it in enumerate(items):
        fc.append(f"[{i}:v]trim=start={it['a']:.3f}:end={it['b']:.3f},setpts=PTS-STARTPTS,"
                  f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,"
                  f"setsar=1,fps=24,format=yuv420p[v{i}]")
        if it["audio"]:
            fc.append(f"[{i}:a]atrim=start={it['a']:.3f}:end={it['b']:.3f},asetpts=PTS-STARTPTS,"
                      f"aresample=44100,aformat=channel_layouts=stereo,volume={it['vol']:.2f}[a{i}]")
        else:
            fc.append(f"[{silent_idx}:a]aresample=44100,aformat=channel_layouts=stereo[a{i}]")
            silent_idx += 1
    n = len(items)
    if trans == "cut" or n == 1:
        fc.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[vo][ao]")
    else:
        xf = {"fade": "fade", "fadeblack": "fadeblack", "dissolve": "dissolve"}[trans]
        prev_v, prev_a, offset = "v0", "a0", 0.0
        for i in range(1, n):
            offset += items[i - 1]["d"] - tdur
            ov, oa = ("vo", "ao") if i == n - 1 else (f"vx{i}", f"ax{i}")
            fc.append(f"[{prev_v}][v{i}]xfade=transition={xf}:duration={tdur:.3f}:offset={offset:.3f}[{ov}]")
            fc.append(f"[{prev_a}][a{i}]acrossfade=d={tdur:.3f}[{oa}]")
            prev_v, prev_a = ov, oa
    # 台詞／口白：依角色聲音表 TTS，對齊每段在成片中的起點
    dialog = []
    if any(it["lines"] for it in items):
        cast = voices.role_map(load_project(pid))
        tprov, tmodel = resolve("tts", load_project(pid))
        start = 0.0
        for i, it in enumerate(items):
            t = start + 0.3
            for ln in it["lines"]:
                role = cast.get(ln["role"]) or cast.get("narrator") or voices.clean_role({"id": "narrator"})
                f = _tts_cached(pid, tprov, tmodel, ln["text"], role)
                d, _, _ = _ffprobe(mdir / f)
                dialog.append((mdir / f, t))
                t += d + 0.25
            start += it["d"] - (tdur if trans != "cut" and n > 1 else 0)
    base_idx = len(items) + sum(1 for it in items if not it["audio"])
    for k, (path, t) in enumerate(dialog):
        args += ["-i", str(path)]
        ms = int(t * 1000)
        fc.append(f"[{base_idx + k}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[d{k}]")
    out_a = "ao"
    if dialog:
        fc.append("[ao]" + "".join(f"[d{k}]" for k in range(len(dialog)))
                  + f"amix=inputs={len(dialog) + 1}:duration=first:dropout_transition=0:normalize=0[am]")
        out_a = "am"
    name = f"compose-{node['id']}-{uuid.uuid4().hex[:6]}.mp4"
    args += ["-filter_complex", ";".join(fc), "-map", "[vo]", "-map", f"[{out_a}]",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(mdir / name)]
    r = _sp.run(args, capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        raise RuntimeError("ffmpeg 合成失敗：" + (r.stderr or "")[-240:])
    total, _, _ = _ffprobe(mdir / name)
    return {"type": "video", "file": name, "url": f"/media/{pid}/{name}",
            "duration": round(total, 2), "clips": len(items), "transition": trans, "lines": len(dialog)}


def _tts_cached(pid: str, provider: str, model: str, text: str, role: dict) -> str:
    """同一音色＋文字只合成一次（存在專案 media）。"""
    import hashlib

    key = json.dumps([provider, model, text, role.get("voice_id"), role.get("speed"), role.get("pitch"),
                      role.get("vol"), role.get("emotion")], ensure_ascii=False)
    name = f"tts-{hashlib.sha1(key.encode()).hexdigest()[:12]}.mp3"
    path = media_dir(pid) / name
    if not path.is_file():
        path.write_bytes(providers.tts(provider, model, text, role.get("voice_id") or "male-qn-qingse",
                                       role.get("speed", 1.0), role.get("pitch", 0), role.get("vol", 1.0),
                                       role.get("emotion", "")))
    return name


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
            "params": _clean_params(kind, params),
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

    if node["kind"] == "compose":
        try:
            out = _compose_run(pid, canvas, node)
        except (RuntimeError, OSError, ValueError) as exc:
            node.update(status="error", message=str(exc)[:300])
            save_project(plan)
            return jsonify(error=str(exc)[:300], node=node), 400
        node.update(output=out, status="done", message=None, job_id=None,
                    ran={"provider": "ffmpeg", "model": out["transition"], "at": time.strftime("%Y-%m-%d %H:%M:%S")})
        save_project(plan)
        return jsonify(node=node)

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
            refs = [_data_uri(media_dir(pid) / f) for f in images[:4]] if provider in ("volcano", "volcano-plan", "local-comfy") else None
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
        if node.get("mode") == "i2v" and not images:
            if not prompt:
                return jsonify(error="首幀模式需要連接上游的圖片節點（並已生成圖片）"), 400
            node["mode"] = "t2v"  # 上游沒有圖片：自動改用文字生成影片
        if node.get("mode") == "i2v":
            if not ((provider == "minimax" and model.startswith("MiniMax-H3")) or provider == "local-comfy"):
                return jsonify(error="目前只有 MiniMax-H3 與地端 ComfyUI 支援首幀生成影片"), 400
            first_frame = _data_uri(media_dir(pid) / images[0])
        if provider == "minimax":
            duration = max(4, min(15, duration)) if model.startswith("MiniMax-H3") else (10 if duration > 6 else 6)
        created = providers.video_create(provider, model, prompt, duration=max(1, min(30, duration)),
                                         resolution=resolution, ratio=ratio, first_frame_data_uri=first_frame,
                                         generate_audio=params.get("audio", True) is not False)
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


def _director_settings(body: dict, state: dict) -> dict:
    """Skill 庫帶來的設定：skill / models(image,video) / gen_mode；存在專案裡。"""
    old = state.get("settings") or {}
    st = {
        "skill": str(body.get("skill", old.get("skill", "")))[:80],
        "models": {},
        "gen_mode": "auto" if body.get("gen_mode", old.get("gen_mode")) == "auto" else "manual",
    }
    models = body.get("models", old.get("models")) or {}
    for k in ("image", "video"):
        v = str(models.get(k) or "")
        if "|" in v and len(v) < 160:
            st["models"][k] = v
    if st["skill"] and (not re.fullmatch(r"[a-z0-9\-]+", st["skill"]) or st["skill"] not in _skill_dirs()):
        st["skill"] = ""
    state["settings"] = st
    return st


def _skill_prompt(slug: str) -> str:
    info = _skill_dirs().get(slug)
    if not info:
        return ""
    path = info["dir"] / "SKILL.md"
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n\n", text, re.S)
    body = text[m.end():] if m else text
    name = info["meta"].get("cn_tc") or info["meta"].get("cn") or slug
    return f"【本次指定 Skill：{name}（/{slug}）】以下是此 Skill 的完整工作規範，請嚴格遵循其流程、格式與風格要求：\n\n{body[:24000]}"


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
    state = _director_state(plan)
    return jsonify(messages=state["messages"], title=plan.get("title"), settings=state.get("settings") or {})


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

    settings = _director_settings(body, state)
    system = DIRECTOR_MODES[mode]
    if settings["skill"]:
        system += "\n\n" + _skill_prompt(settings["skill"])
    if settings["models"]:
        names = "、".join(f"{'圖片' if k == 'image' else '影片'}模型 {v.split('|', 1)[1]}" for k, v in settings["models"].items())
        system += f"\n\n後續將使用：{names}。畫面提示詞請針對這些模型撰寫（英文、具體、可直接生成）。"
    if settings["gen_mode"] == "auto":
        system += "\n\n生成模式：自動。不要反問使用者，直接產出完整可執行的結果。"
    else:
        system += "\n\n生成模式：手動。若關鍵資訊不足，可先列出假設並在結尾詢問是否進入生成。"
    if body.get("use_canvas"):
        system += "\n\n目前畫布節點：\n" + _canvas_brief(plan)
    user_content = text or "請依附件內容進行。"
    if attachment:
        user_content += f"\n\n【附件：{att_name or '故事原文'}】\n{attachment}"

    history = [{"role": m["role"], "content": m["content"][:6000]} for m in state["messages"][-12:]]
    messages = [{"role": "system", "content": system}, *history, {"role": "user", "content": user_content}]
    try:
        reply = providers.chat(provider, model, messages, max_tokens=8000, timeout=300).strip()
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
    return jsonify(reply=state["messages"][-1], user=state["messages"][-2], settings=settings)


# --------------------------------------------------------------------- Skill 工作台（劇本＋分鏡）
WB_PROTOCOL = """你在 REACH AI Video Studio 的「Skill 工作台」，目標是與使用者一起產出【劇本】與【分鏡表】。一律使用繁體中文（英文提示詞除外）。

回覆規則（務必遵守格式）：
1. 若缺少會「顯著影響結果」的關鍵資訊（交付形式、片長、風格、主角設定、要拍哪一場等），先提問，不要產出劇本：
   用 1–2 句說明為何要問，接著輸出一個 ```ask 區塊（JSON）：
   {"questions":[{"q":"問題","options":["選項1","選項2","選項3"]}]}
   最多 3 題，每題 2–5 個簡短選項；使用者也能自行輸入其他答案。
2. 資訊足夠時，產出成品：
   ```script
   （完整 Markdown 劇本：片名、一句話梗概、角色表、分場與對白）
   ```
   ```shots
   {"shots":[{"title":"鏡頭名稱","seconds":5,"desc":"畫面描述（繁中）","camera":"景別／運鏡／光線（繁中）","prompt":"英文圖片提示詞（主體外觀、場景、構圖、光線、風格，可直接生圖）","negative":"英文負面提示詞","motion":"英文影片運動描述（鏡頭與主體動作）"}]}
   ```
   區塊外只寫 1–3 句重點說明，不要重複區塊內容。
3. 使用者要求修改時，只輸出需要更新的區塊（script 或 shots），內容為完整的新版本。
4. 每鏡 seconds 介於 4–10；同一角色在每鏡的 prompt 中外觀描述必須一致。
   shots 欄位格式優先於 Skill 內的任何輸出格式：prompt 只寫「單張靜態畫面」的英文生圖提示詞（60–120 個英文詞，不含時間軸、不含中文、不含 Camera/Audio 分段）；
   motion 只寫該鏡的英文鏡頭與主體動作（1–3 句）；Skill 要求的時間軸、音效等細節放進 camera 或劇本。
5. 不要使用受版權保護的角色名稱或品牌，改用原創描述。"""

_WB_ID = re.compile(r"[a-f0-9]{8}")


def _wb(plan: dict) -> dict:
    return plan.setdefault("workbench", {"sessions": {}})


def _wb_summary(sid: str, ss: dict) -> dict:
    return {"id": sid, "title": ss.get("title") or "未命名", "skill": ss.get("skill", ""),
            "skill_name": ss.get("skill_name", ""), "updated": ss.get("updated", ""),
            "shots": len(ss.get("shots") or []), "has_script": bool(ss.get("script"))}


def _wb_blocks(text: str) -> dict:
    """解析 ```ask / ```script / ```shots；容許最後一個區塊沒有收尾（被截斷）。"""
    out: dict = {}
    for kind in ("ask", "script", "shots"):
        m = re.search(r"```" + kind + r"[^\n]*\n(.*?)(?:```|\Z)", text, re.S | re.I)
        if m:
            out[kind] = m.group(1).strip()
    shown = re.sub(r"```(?:ask|script|shots)[^\n]*\n.*?(?:```|\Z)", "", text, flags=re.S | re.I).strip()
    out["text"] = re.sub(r"\n{3,}", "\n\n", shown)
    return out


def _wb_json(raw: str):
    raw = raw.strip()
    try:
        return json.loads(raw)
    except ValueError:
        m = re.search(r"\{.*\}", raw, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except ValueError:
                return None
    return None


def _wb_clean_shots(items) -> list[dict]:
    shots = []
    for x in (items or [])[:40]:
        if not isinstance(x, dict):
            continue
        try:
            sec = max(4, min(10, int(float(x.get("seconds") or 5))))
        except (TypeError, ValueError):
            sec = 5
        shots.append({k: str(x.get(k) or "")[:3000] for k in ("title", "desc", "camera", "prompt", "negative", "motion")}
                     | {"seconds": sec})
    return [s for s in shots if s["prompt"] or s["desc"]]


@app.get("/api/projects/<pid>/workbench")
def api_wb_list(pid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    items = [_wb_summary(k, v) for k, v in _wb(plan)["sessions"].items()]
    items.sort(key=lambda x: x["updated"], reverse=True)
    return jsonify(sessions=items)


@app.post("/api/projects/<pid>/workbench")
def api_wb_create(pid: str):
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    sid = uuid.uuid4().hex[:8]
    ss = {"title": str(body.get("title") or "")[:60], "messages": [], "script": "", "shots": [],
          "created": time.strftime("%Y-%m-%d %H:%M:%S")}
    _director_settings(body, ss)  # 共用：skill / models / gen_mode 檢查
    ss.update(ss.pop("settings"))
    info = _skill_dirs().get(ss["skill"]) if ss["skill"] else None
    ss["skill_name"] = (info["meta"].get("cn_tc") or info["meta"].get("cn") or ss["skill"]) if info else ""
    if not ss["title"]:
        ss["title"] = ss["skill_name"] or "自由創作"
    ss["updated"] = ss["created"]
    _wb(plan)["sessions"][sid] = ss
    save_project(plan)
    return jsonify(session=ss | {"id": sid})


@app.get("/api/projects/<pid>/workbench/<sid>")
def api_wb_get(pid: str, sid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    ss = _wb(plan)["sessions"].get(sid) if _WB_ID.fullmatch(sid) else None
    if ss is None:
        return jsonify(error="找不到工作階段"), 404
    return jsonify(session=ss | {"id": sid})


@app.put("/api/projects/<pid>/workbench/<sid>")
def api_wb_put(pid: str, sid: str):
    """手動編輯劇本、分鏡、標題、模型與生成模式。"""
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    ss = _wb(plan)["sessions"].get(sid) if _WB_ID.fullmatch(sid) else None
    if ss is None:
        return jsonify(error="找不到工作階段"), 404
    if "script" in body:
        ss["script"] = str(body["script"])[:60000]
    if "shots" in body:
        ss["shots"] = _wb_clean_shots(body["shots"])
    if "title" in body:
        ss["title"] = str(body["title"])[:60] or ss.get("title")
    if "models" in body or "gen_mode" in body:
        tmp = {"settings": {"skill": ss.get("skill", ""), "models": ss.get("models", {}), "gen_mode": ss.get("gen_mode", "manual")}}
        _director_settings({k: body[k] for k in ("models", "gen_mode") if k in body}, tmp)
        ss["models"], ss["gen_mode"] = tmp["settings"]["models"], tmp["settings"]["gen_mode"]
    ss["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    save_project(plan)
    return jsonify(session=ss | {"id": sid})


_CAM_KEYS = [("子彈", "bullet_time"), ("柯克", "dolly_zoom"), ("甩", "whip_pan"), ("航拍", "drone"), ("無人機", "drone"),
             ("第一視角", "pov"), ("POV", "pov"), ("升降", "crane"), ("推軌後", "dolly_out"), ("拉遠", "dolly_out"),
             ("推軌", "dolly_in"), ("推進", "dolly_in"), ("跟拍", "tracking"), ("跟隨", "tracking"), ("手持", "handheld"),
             ("搖鏡", "pan"), ("橫搖", "pan"), ("俯仰", "tilt"), ("直搖", "tilt"), ("固定", "locked")]


def _wb_camera(text: str) -> str:
    return next((k for kw, k in _CAM_KEYS if kw in (text or "")), "locked")


def _wb_plan_shots(ss: dict, video_provider: str) -> list[dict]:
    """工作台分鏡 → 專案分鏡表（plan.shots）。"""
    out, t = [], 0.0
    for i, x in enumerate(ss.get("shots") or []):
        cam = _wb_camera(x.get("camera", ""))
        sec = float(x.get("seconds") or 5)
        out.append({
            "id": f"S{i + 1:02d}", "beat": (x.get("title") or f"分鏡 {i + 1}")[:40],
            "start_seconds": round(t, 2), "duration_seconds": sec, "framing": x.get("camera", "")[:120],
            "camera": cam, "camera_zh": pipeline.CAMERAS[cam]["zh"],
            "action": x.get("desc", ""), "lighting": "",
            "positive_prompt": x.get("prompt") or x.get("desc", ""),
            "negative_prompt": x.get("negative") or "blurry, distorted hands, extra limbs, watermark, text overlay, low quality",
            "motion": x.get("motion", ""),
            "image": None, "video": None, "video_job": None, "video_provider": video_provider, "status": "planned",
        })
        t += sec
    return out


def _wb_canvas_nodes(ss: dict, canvas: dict) -> int:
    """把工作台分鏡加進畫布（圖片 → 影片），最後接一個合成節點。回傳新增組數。"""
    shots = ss.get("shots") or []
    nodes, edges = canvas.setdefault("nodes", []), canvas.setdefault("edges", [])
    nxt = max([0] + [int(n["id"][1:]) for n in nodes if n["id"][1:].isdigit()])
    y0 = (max(n["y"] for n in nodes) + 360) if nodes else 0
    models = ss.get("models") or {}
    vm, im = models.get("video") or "", models.get("image") or ""
    vids = []
    for i, x in enumerate(shots):
        y, t = y0 + i * 300, f"分鏡 {i + 1}"
        img = {"id": f"N{nxt + 1}", "kind": "image", "title": f"{t}・畫面", "x": 0, "y": y,
               "prompt": x.get("prompt") or x.get("desc", ""), "model": im, "mode": "t2i",
               "params": {"ratio": "16:9"}, "output": None, "status": "idle"}
        vid = {"id": f"N{nxt + 2}", "kind": "video", "title": f"{t}・{(x.get('title') or '影片')[:20]}", "x": 460, "y": y,
               "prompt": "\n".join(v for v in (x.get("motion"), x.get("prompt") or x.get("desc")) if v), "model": vm,
               "mode": "i2v" if ("|MiniMax-H3" in vm or vm.startswith("local-comfy|")) else "t2v",
               "params": {"ratio": "16:9", "duration": max(2, min(30, int(x.get("seconds") or 5))), "resolution": "768P"},
               "output": None, "status": "idle"}
        nxt += 2
        nodes += [img, vid]
        edges.append({"from": img["id"], "to": vid["id"]})
        vids.append(vid["id"])
    if vids:
        nxt += 1
        cmp_ = {"id": f"N{nxt}", "kind": "compose", "title": "影片合成", "x": 920,
                "y": y0 + (len(vids) - 1) * 150, "prompt": "", "model": "", "mode": "",
                "params": {"transition": "cut", "tdur": 0.5, "clips": [{"id": v, "on": True, "cut_in": 0.0, "cut_out": 0.0} for v in vids]},
                "output": None, "status": "idle"}
        nodes.append(cmp_)
        edges += [{"from": v, "to": cmp_["id"]} for v in vids]
    return len(vids)


@app.post("/api/projects/<pid>/workbench/<sid>/to-project")
def api_wb_to_project(pid: str, sid: str):
    """mode=new：以這個 Skill 對話建立新專案（分鏡表＋畫布，對話一起搬過去）；mode=current：加到目前專案畫布。"""
    body = request.get_json(silent=True) or {}
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    ss = _wb(plan)["sessions"].get(sid) if _WB_ID.fullmatch(sid) else None
    if ss is None:
        return jsonify(error="找不到工作階段"), 404
    if not ss.get("shots"):
        return jsonify(error="還沒有分鏡表"), 400

    if body.get("mode") != "new":
        canvas = plan.get("canvas") or {"nodes": [], "edges": [], "viewport": {"x": 0, "y": 0, "k": 1}}
        n = _wb_canvas_nodes(ss, canvas)
        plan["canvas"] = canvas
        save_project(plan)
        return jsonify(ok=True, pid=pid, shots=n, created=False)

    vm = (ss.get("models") or {}).get("video") or ""
    vprov = vm.split("|")[0] if "|" in vm else "minimax"
    title = (str(body.get("title") or "") or ss.get("title") or "Skill 專案")[:60]
    first = (ss["shots"][0].get("desc") or "")[:200]
    new = pipeline.make_plan(title=title, idea=first or title, style=str(body.get("style") or "電影感寫實"),
                             duration=sum(float(x.get("seconds") or 5) for x in ss["shots"]), ratio="16:9")
    new["shots"] = _wb_plan_shots(ss, vprov)
    new["script"] = {"beats": [{"beat": x.get("title") or f"分鏡 {i + 1}", "description": x.get("desc", "")}
                               for i, x in enumerate(ss["shots"])],
                     "synopsis": (ss.get("script") or first)[:2000], "text": ss.get("script", ""),
                     "source": "workbench", "skill": ss.get("skill", "")}
    new["stage"] = "storyboard"
    canvas = {"nodes": [], "edges": [], "viewport": {"x": 0, "y": 0, "k": 0.6}}
    n = _wb_canvas_nodes(ss, canvas)
    new["canvas"] = canvas
    _wb(new)["sessions"][sid] = ss
    save_project(new)
    _wb(plan)["sessions"].pop(sid, None)  # 對話搬到新專案
    save_project(plan)
    return jsonify(ok=True, pid=new["id"], sid=sid, title=new["title"], shots=n, created=True)


@app.delete("/api/projects/<pid>/workbench/<sid>")
def api_wb_delete(pid: str, sid: str):
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    _wb(plan)["sessions"].pop(sid, None)
    save_project(plan)
    return jsonify(ok=True)


@app.post("/api/projects/<pid>/workbench/<sid>/chat")
def api_wb_chat(pid: str, sid: str):
    body = request.get_json(silent=True) or {}
    text = str(body.get("text", "")).strip()[:8000]
    if not text:
        return jsonify(error="請輸入內容"), 400
    try:
        plan = load_project(pid)
    except (FileNotFoundError, ValueError):
        return jsonify(error="找不到專案"), 404
    ss = _wb(plan)["sessions"].get(sid) if _WB_ID.fullmatch(sid) else None
    if ss is None:
        return jsonify(error="找不到工作階段"), 404

    provider, model = resolve("script", plan)
    if "|" in str(body.get("model", "")):
        prov, mid = body["model"].split("|", 1)
        if valid_choice("script", prov, mid):
            provider, model = prov, mid

    system = WB_PROTOCOL
    if ss.get("skill"):
        system += "\n\n" + _skill_prompt(ss["skill"])
    if ss.get("models"):
        names = "、".join(f"{'圖片' if k == 'image' else '影片'}模型 {v.split('|', 1)[1]}" for k, v in ss["models"].items())
        system += f"\n\n後續將使用：{names}。prompt 與 motion 請針對這些模型撰寫。"
    if ss.get("script") or ss.get("shots"):
        system += "\n\n【目前的劇本】\n" + (ss.get("script") or "（尚無）")[:12000]
        system += "\n\n【目前的分鏡表 JSON】\n" + json.dumps({"shots": ss.get("shots") or []}, ensure_ascii=False)[:12000]
    if ss.get("gen_mode") == "auto":
        system += "\n\n使用者偏好：盡量少提問，資訊不足時用合理假設直接產出，並在說明中標註假設。"

    history = [{"role": m["role"], "content": m["content"][:4000]} for m in ss["messages"][-10:]]
    messages = [{"role": "system", "content": system}, *history, {"role": "user", "content": text}]
    try:
        reply = providers.chat(provider, model, messages, max_tokens=8000, timeout=300).strip()
    except ProviderError as exc:
        return jsonify(error=str(exc)[:300]), 502

    parts = _wb_blocks(reply)
    ask = _wb_json(parts["ask"]) if parts.get("ask") else None
    questions = []
    for q in (ask or {}).get("questions") or []:
        if isinstance(q, dict) and q.get("q"):
            questions.append({"q": str(q["q"])[:200], "options": [str(o)[:120] for o in (q.get("options") or [])[:6]]})
    updated = []
    if parts.get("script"):
        ss["script"] = parts["script"][:60000]
        updated.append("script")
    if parts.get("shots"):
        data = _wb_json(parts["shots"])
        shots = _wb_clean_shots((data or {}).get("shots") if isinstance(data, dict) else data)
        if shots:
            ss["shots"] = shots
            updated.append("shots")
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    ss["messages"].append({"role": "user", "content": text, "at": now})
    ss["messages"].append({"role": "assistant", "content": reply, "text": parts["text"], "questions": questions,
                           "updated": updated, "at": now, "model": f"{provider}/{model}"})
    ss["messages"] = ss["messages"][-60:]
    ss["updated"] = now
    save_project(plan)
    return jsonify(session=ss | {"id": sid})


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
