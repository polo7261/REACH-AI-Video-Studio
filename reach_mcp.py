"""REACH AI Video Studio — MCP server（stdio，newline-delimited JSON-RPC 2.0）。

只依賴 stdlib + reach_video，不經過 Flask HTTP API（獨立於網頁端；架構中，後端串接另行處理）。

啟動：.venv/bin/python reach_mcp.py
註冊（例）：~/.omp/agent/mcp.json 加入
  "reach": {"type": "stdio", "command": "/Users/sky/REACH-AI-Video-Studio/.venv/bin/python",
            "args": ["/Users/sky/REACH-AI-Video-Studio/reach_mcp.py"]}

暴露工具：create_project / list_projects / get_project / generate_image / generate_video / get_task
"""

from __future__ import annotations

import json
import sys

from reach_video import pipeline, providers
from reach_video.config import load_routing, valid_choice
from reach_video.providers import ProviderError
from reach_video.store import list_projects, load_project, save_project

SERVER_INFO = {"name": "reach-ai-video-studio", "version": "0.4.0"}


def _text_result(data: dict | list, is_error: bool = False) -> dict:
    payload = json.dumps(data, ensure_ascii=False)
    out: dict = {"content": [{"type": "text", "text": payload}]}
    if is_error:
        out["isError"] = True
    return out


def _routing(kind: str, provider: str | None, model: str | None) -> tuple[str, str]:
    """未指定時用全域 routing；指定時驗證存在且 kind 相符。"""
    if provider and model:
        from reach_video.config import STEPS
        step = next((s["id"] for s in STEPS if s["kind"] == kind), kind)
        if not valid_choice(step, provider, model):
            raise ProviderError(provider, f"routing 不支援 {provider}/{model}（kind={kind}）")
        return provider, model
    route = load_routing()[kind]
    return route["provider"], route["model"]


def tool_create_project(args: dict) -> dict:
    idea = str(args.get("idea", "")).strip()
    if not idea:
        raise ProviderError("reach", "請提供 idea（一句話故事）")
    try:
        duration = max(6.0, min(180.0, float(args.get("duration", 24) or 24)))
    except (TypeError, ValueError):
        duration = 24.0
    plan = pipeline.make_plan(
        title=str(args.get("title", "")).strip() or idea[:16],
        idea=idea,
        style=str(args.get("style", "電影感寫實")).strip() or "電影感寫實",
        duration=duration,
        ratio=str(args.get("ratio", "16:9")),
        character=str(args.get("character", "")).strip(),
        location=str(args.get("location", "")).strip(),
    )
    save_project(plan)
    return {"project_id": plan.get("id"), "title": plan.get("title"), "shots": len(plan.get("shots", [])), "plan": plan}


def tool_list_projects(_args: dict) -> dict:
    return {"projects": list_projects()}


def tool_get_project(args: dict) -> dict:
    plan = load_project(str(args.get("project_id", "")))
    return {"plan": plan, "timeline": pipeline.timeline(plan)}


def tool_generate_image(args: dict) -> dict:
    prompt = str(args.get("prompt", "")).strip()
    if not prompt:
        raise ProviderError("reach", "請提供 prompt")
    provider, model = _routing("image", args.get("provider"), args.get("model"))
    res = providers.image(provider, model, prompt, size=str(args.get("size", "1024x1024")))
    return {"provider": provider, "model": model, "url": res.get("url"), "b64": bool(res.get("b64")), "raw": res.get("raw")}


def tool_generate_video(args: dict) -> dict:
    prompt = str(args.get("prompt", "")).strip()
    if not prompt:
        raise ProviderError("reach", "請提供 prompt")
    provider, model = _routing("video", args.get("provider"), args.get("model"))
    res = providers.video_create(
        provider, model, prompt,
        duration=int(args.get("duration", 6) or 6),
        resolution=str(args.get("resolution", "768P")),
        ratio=str(args.get("ratio", "16:9")),
    )
    return {"provider": provider, "model": model, "task_id": res.get("task_id"), "api": res.get("api")}


def tool_get_task(args: dict) -> dict:
    provider = str(args.get("provider", "")).strip()
    task_id = str(args.get("task_id", "")).strip()
    if not provider or not task_id:
        raise ProviderError("reach", "請提供 provider 與 task_id")
    return dict(providers.video_poll(provider, task_id, model=args.get("model")))


TOOLS = [
    {
        "name": "create_project",
        "description": "建立新專案：一句話故事產生劇本分鏡 plan",
        "inputSchema": {
            "type": "object",
            "properties": {
                "idea": {"type": "string", "description": "一句話故事（必填）"},
                "title": {"type": "string"}, "style": {"type": "string"},
                "duration": {"type": "number", "description": "秒，6-180，預設 24"},
                "ratio": {"type": "string"}, "character": {"type": "string"}, "location": {"type": "string"},
            },
            "required": ["idea"],
        },
    },
    {"name": "list_projects", "description": "列出所有專案", "inputSchema": {"type": "object", "properties": {}}},
    {
        "name": "get_project",
        "description": "取得專案 plan 與時間軸",
        "inputSchema": {"type": "object", "properties": {"project_id": {"type": "string"}}, "required": ["project_id"]},
    },
    {
        "name": "generate_image",
        "description": "生圖（未指定 provider/model 時用全域 routing 預設）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"}, "size": {"type": "string"},
                "provider": {"type": "string"}, "model": {"type": "string"},
            },
            "required": ["prompt"],
        },
    },
    {
        "name": "generate_video",
        "description": "生片：建立影片生成任務，回傳 task_id",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"}, "duration": {"type": "integer"},
                "resolution": {"type": "string"}, "ratio": {"type": "string"},
                "provider": {"type": "string"}, "model": {"type": "string"},
            },
            "required": ["prompt"],
        },
    },
    {
        "name": "get_task",
        "description": "查任務狀態（video_poll：queued/running/succeeded/failed + url）",
        "inputSchema": {
            "type": "object",
            "properties": {"provider": {"type": "string"}, "task_id": {"type": "string"}, "model": {"type": "string"}},
            "required": ["provider", "task_id"],
        },
    },
]

HANDLERS = {
    "create_project": tool_create_project,
    "list_projects": tool_list_projects,
    "get_project": tool_get_project,
    "generate_image": tool_generate_image,
    "generate_video": tool_generate_video,
    "get_task": tool_get_task,
}


def _handle(msg: dict) -> dict | None:
    method = msg.get("method", "")
    if not method:  # response to a request we sent（本 server 不送 request）
        return None
    if method == "notifications/initialized" or msg.get("id") is None:
        return None
    mid = msg.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": mid,
                "result": {"protocolVersion": "2025-03-26", "capabilities": {"tools": {}}, "serverInfo": SERVER_INFO}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = msg.get("params") or {}
        name = str(params.get("name", ""))
        handler = HANDLERS.get(name)
        if handler is None:
            return {"jsonrpc": "2.0", "id": mid,
                    "error": {"code": -32602, "message": f"未知工具：{name}"}}
        try:
            return {"jsonrpc": "2.0", "id": mid, "result": _text_result(handler(params.get("arguments") or {}))}
        except ProviderError as exc:
            return {"jsonrpc": "2.0", "id": mid,
                    "result": _text_result({"error": str(exc), "provider": exc.provider, "code": exc.code}, is_error=True)}
        except (FileNotFoundError, ValueError) as exc:
            return {"jsonrpc": "2.0", "id": mid,
                    "result": _text_result({"error": f"找不到專案或資料格式錯誤：{exc}"}, is_error=True)}
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"未知方法：{method}"}}


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            print(json.dumps({"jsonrpc": "2.0", "id": None,
                              "error": {"code": -32700, "message": "parse error"}}, ensure_ascii=False), flush=True)
            continue
        out = _handle(msg)
        if out is not None:
            print(json.dumps(out, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
