#!/usr/bin/env python3
"""把 ComfyUI「Export (API)」的 JSON 轉成 REACH workflow 模板（自動標佔位符）。

用法：
  python3 scripts/comfy_import.py ~/Downloads/flux_api.json --id flux-dev --kind image
  python3 scripts/comfy_import.py ~/Downloads/wan_i2v_api.json --id wan22-i2v --kind video --note "Wan2.2 I2V 14B"
輸出：workflows/comfyui/<id>.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_KEYS = ("text", "t5xxl", "clip_l", "prompt", "positive_prompt")


def is_link(v) -> bool:
    return isinstance(v, list) and len(v) == 2 and isinstance(v[0], str)


def text_node(g: dict, nid: str, seen=None) -> str | None:
    """沿 conditioning 連線往上找第一個有文字欄位的節點。"""
    seen = seen or set()
    if nid in seen or nid not in g:
        return None
    seen.add(nid)
    ins = g[nid].get("inputs", {})
    if any(isinstance(ins.get(k), str) for k in TEXT_KEYS):
        return nid
    for key in ("positive", "conditioning", "conditioning_to", "conditioning_1", "cond"):
        if is_link(ins.get(key)):
            r = text_node(g, ins[key][0], seen)
            if r:
                return r
    return None


def neg_node(g: dict, nid: str, seen=None) -> str | None:
    seen = seen or set()
    if nid in seen or nid not in g:
        return None
    seen.add(nid)
    ins = g[nid].get("inputs", {})
    if any(isinstance(ins.get(k), str) for k in TEXT_KEYS):
        return nid
    for key in ("negative", "conditioning"):
        if is_link(ins.get(key)):
            r = neg_node(g, ins[key][0], seen)
            if r:
                return r
    return None


def convert(g: dict) -> tuple[dict, dict, list[str]]:
    defaults, log = {}, []
    pos, neg = set(), set()
    for nid, n in g.items():
        ins = n.get("inputs", {})
        if is_link(ins.get("positive")):
            r = text_node(g, ins["positive"][0])
            if r:
                pos.add(r)
        if is_link(ins.get("negative")):
            r = neg_node(g, ins["negative"][0])
            if r:
                neg.add(r)
    neg -= pos
    if not pos:  # Flux BasicGuider 等
        pos = {nid for nid, n in g.items() if "TextEncode" in n.get("class_type", "")
               and any(isinstance(n.get("inputs", {}).get(k), str) for k in TEXT_KEYS)} - neg
    for nid, name in [(x, "prompt") for x in pos] + [(x, "negative") for x in neg]:
        ins = g[nid]["inputs"]
        for k in TEXT_KEYS:
            if isinstance(ins.get(k), str):
                defaults.setdefault(name, ins[k])
                ins[k] = "{{%s}}" % name
        log.append(f"{name:<9}← node {nid} {g[nid]['class_type']}")

    image_done = False
    for nid, n in g.items():
        ins, ct = n.get("inputs", {}), n.get("class_type", "")
        for k in ("seed", "noise_seed"):
            if isinstance(ins.get(k), int):
                ins[k] = "{{seed}}"
                log.append(f"seed     ← node {nid} {ct}.{k}")
        if isinstance(ins.get("width"), int) and isinstance(ins.get("height"), int) and "Upscale" not in ct:
            defaults.setdefault("width", ins["width"])
            defaults.setdefault("height", ins["height"])
            ins["width"], ins["height"] = "{{width}}", "{{height}}"
            log.append(f"size     ← node {nid} {ct}")
            for fk in ("length", "num_frames", "frames", "video_frames"):
                if isinstance(ins.get(fk), int):
                    defaults.setdefault("frames", ins[fk])
                    ins[fk] = "{{frames}}"
                    log.append(f"frames   ← node {nid} {ct}.{fk}")
        for fk in ("fps", "frame_rate"):
            if isinstance(ins.get(fk), (int, float)) and not is_link(ins.get(fk)):
                defaults.setdefault("fps", ins[fk])
                ins[fk] = "{{fps}}"
                log.append(f"fps      ← node {nid} {ct}.{fk}")
        if ct == "LoadImage" and isinstance(ins.get("image"), str) and not image_done:
            ins["image"] = "{{image}}"
            image_done = True
            log.append(f"image    ← node {nid} LoadImage（首幀/參考圖）")
    return g, defaults, log


def build_spec(g: dict, wid: str, kind: str, note: str = "") -> tuple[dict, list[str]]:
    if "nodes" in g and "links" in g:
        raise ValueError("這是 UI 格式。請在 ComfyUI 選單 Workflow → Export (API) 重新匯出。")
    g, defaults, log = convert(g)
    classes = " ".join(n.get("class_type", "") for n in g.values())
    spec = {"id": wid, "kind": kind, "status": "untested", "note": note, "defaults": defaults,
            "frame_multiple": 8 if "LTXV" in classes else (4 if "Wan" in classes or "Hunyuan" in classes else 0),
            "size_multiple": 32 if "LTXV" in classes else 16, "workflow": g}
    if kind == "image":
        spec.pop("frame_multiple")
    if "{{prompt}}" not in json.dumps(g, ensure_ascii=False):
        log.append("⚠ 沒找到正向提示詞節點，請手動把文字改成 {{prompt}}")
    return spec, log


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--id", required=True)
    ap.add_argument("--kind", choices=["image", "video"], required=True)
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    g = json.loads(Path(a.src).expanduser().read_text(encoding="utf-8"))
    try:
        spec, log = build_spec(g, a.id, a.kind, a.note)
    except ValueError as exc:
        print(f"✗ {exc}", file=sys.stderr)
        return 1
    out = ROOT / "workflows" / "comfyui" / f"{a.id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(log))
    print(f"✓ 已寫入 {out.relative_to(ROOT)}（重啟 REACH 後出現在模型清單：local-comfy / {a.id}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
