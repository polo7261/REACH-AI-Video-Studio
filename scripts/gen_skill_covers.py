#!/usr/bin/env python3
"""為沒有 cover 的 Skill 產生 SVG 封面（依 Skill 用途選插圖主題）。

用法：python3 scripts/gen_skill_covers.py [--force]
只寫入缺少 cover.* 的 skill/<分類>/<slug>/cover.svg；--force 只重畫本腳本產生過的 cover.svg，不動手作封面。
"""
from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skill"
W, H = 1600, 900
GEN_MARK = "<!-- generated: gen_skill_covers.py -->"

PALETTE = {  # 分類 → 漸層
    "分鏡前期": ("#1d2b4a", "#3f6fb5"), "劇本喜劇": ("#3a1f2b", "#b5523f"), "動畫動漫": ("#2a1d4a", "#8a5bd6"),
    "廣告TVC": ("#1f2f2a", "#3f9a7a"), "短劇漫劇": ("#3a2416", "#c27b3a"), "通用技能": ("#1f2730", "#5b7a96"),
    "電商帶貨": ("#3a1a22", "#d0566e"), "MV音樂": ("#24163a", "#c04fa8"), "專業影視": ("#121820", "#4a5a6e"),
}
S = 'fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round"'


def frame(x, y, w, h, op=".9", sw=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" {S} stroke-width="{sw}" opacity="{op}"/>'


def lines(x, y, w, n, gap=30, sw=8, op=".55"):
    return "".join(f'<path d="M{x} {y + i * gap}h{w * (0.6 + 0.4 * ((i * 7) % 5) / 4):.0f}" {S} stroke-width="{sw}" opacity="{op}"/>' for i in range(n))


def cam(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="0" y="20" width="150" height="100" rx="16" {S} stroke-width="8"/>'
            f'<path d="m150 50 70-35v110l-70-35" {S} stroke-width="8"/>'
            f'<circle cx="40" cy="0" r="22" {S} stroke-width="7"/><circle cx="105" cy="0" r="22" {S} stroke-width="7"/></g>')


def face(x, y, r=110, op="1"):
    return (f'<g opacity="{op}"><circle cx="{x}" cy="{y}" r="{r}" {S} stroke-width="8"/>'
            f'<path d="M{x - 45} {y - 20}q15-14 30 0M{x + 15} {y - 20}q15-14 30 0" {S} stroke-width="7"/>'
            f'<path d="M{x - 35} {y + 40}q35 26 70 0" {S} stroke-width="7"/></g>')


def storyboard():
    cells = "".join(frame(560 + c * 270, 150 + r * 190, 240, 160) +
                    f'<path d="M{590 + c * 270} {280 + r * 190}l50-55 40 35 40-50 60 70" {S} stroke-width="5" opacity=".6"/>'
                    f'<text x="{572 + c * 270}" y="{182 + r * 190}" fill="#fff" opacity=".7" font-size="22" font-family="ui-monospace,Menlo">{r * 3 + c + 1:02d}</text>'
                    for r in range(2) for c in range(3))
    return cells + cam(1200, 600, .8)


def faceswap():
    return (face(620, 330) + face(1060, 330, op=".75") +
            f'<path d="M760 250q80-60 160 0M920 410q-80 60-160 0" {S} stroke-width="8"/>'
            f'<path d="m905 225 18 26-30 6M775 435l-18-26 30-6" {S} stroke-width="8"/>' + frame(500, 520, 680, 120, ".5"))


def script():
    return (frame(640, 120, 420, 540) + lines(690, 200, 320, 12, 34) + frame(700, 90, 420, 540, ".35") +
            f'<path d="m1150 520 120-120 40 40-120 120h-40z" {S} stroke-width="8"/>')


def cctv():
    roof = f'<path d="M560 520l240-120 240 120M600 520v140h400V520M680 660v-90h80v90" {S} stroke-width="8" opacity=".8"/>'
    return (frame(470, 110, 680, 600, ".9", 5) + roof +
            f'<path d="M1010 200h120l20 30h-160z" {S} stroke-width="7"/><path d="M1030 230v40" {S} stroke-width="7"/>'
            '<circle cx="520" cy="160" r="14" fill="#ff5b5b"/>'
            '<text x="545" y="171" fill="#fff" font-size="34" font-family="ui-monospace,Menlo" opacity=".9">REC  0921-03-14 23:59:07</text>'
            '<text x="900" y="690" fill="#fff" font-size="26" font-family="ui-monospace,Menlo" opacity=".7">CAM 02</text>')


def microexpr():
    wave = "".join(f'{"M" if i == 0 else "L"}{560 + i * 20} {620 + (40 if i % 4 == 1 else -30 if i % 4 == 3 else 0) * (1 if 8 < i < 24 else .3):.0f} ' for i in range(31))
    return (face(860, 330, 170) +
            f'<path d="M780 255q20-30 50-12M890 243q30-18 50 12" {S} stroke-width="6" opacity=".7"/>'
            f'<circle cx="790" cy="430" r="60" {S} stroke-width="5" stroke-dasharray="10 12" opacity=".7"/>'
            f'<path d="{wave}" {S} stroke-width="6" opacity=".8"/>')


def reverse():
    return (frame(470, 220, 360, 260) + f'<path d="M500 450l100-110 70 60 80-90 90 140" {S} stroke-width="7"/><circle cx="560" cy="290" r="26" {S} stroke-width="7"/>'
            f'<path d="M870 350h140m-40-40 40 40-40 40" {S} stroke-width="9"/>' +
            frame(1050, 200, 330, 300) + lines(1090, 260, 250, 7, 32) +
            '<text x="1090" y="560" fill="#fff" opacity=".8" font-size="30" font-family="ui-monospace,Menlo">prompt:</text>')


def talking():
    return (f'<circle cx="800" cy="260" r="90" {S} stroke-width="8"/><path d="M640 560c20-120 90-180 160-180s140 60 160 180" {S} stroke-width="8"/>'
            f'<rect x="980" y="300" width="60" height="110" rx="30" {S} stroke-width="8"/><path d="M955 380a55 55 0 0 0 110 0M1010 435v50" {S} stroke-width="8"/>'
            + frame(520, 600, 560, 70, ".85") + lines(560, 636, 470, 1, 0, 9, ".8"))


def viral():
    return (frame(560, 140, 380, 500, ".6") + lines(610, 220, 280, 10, 36) +
            f'<path d="M1000 620l90-120 70 60 140-220" {S} stroke-width="10"/><path d="m1260 330 40 10-10 40" {S} stroke-width="10"/>'
            f'<path d="M1150 220c30 40 70 60 50 120-10 30-40 50-70 50s-60-25-60-60c0-30 20-40 30-70 10 25 30 30 30 30-10-30 0-50 20-70z" {S} stroke-width="7"/>')


def polish():
    return (frame(480, 250, 320, 200) + '<text x="640" y="375" text-anchor="middle" fill="#fff" font-size="88" font-weight="700" opacity=".9">中文</text>'
            f'<path d="M840 350h120m-40-40 40 40-40 40" {S} stroke-width="9"/>' +
            frame(1000, 250, 320, 200) + '<text x="1160" y="378" text-anchor="middle" fill="#fff" font-size="88" font-weight="700" font-family="ui-monospace,Menlo" opacity=".9">EN</text>'
            f'<path d="M1330 200l14 36 36 14-36 14-14 36-14-36-36-14 36-14z" {S} stroke-width="6"/>')


def camera_move():
    return (cam(720, 300, 1.2) +
            f'<path d="M520 620q380 170 760 0" {S} stroke-width="7" stroke-dasharray="18 16"/><path d="m1250 600 35 25-40 15" {S} stroke-width="7"/>'
            f'<path d="M560 220q-70 130 0 260M1240 220q70 130 0 260" {S} stroke-width="6" opacity=".6"/>'
            '<text x="800" y="760" text-anchor="middle" fill="#fff" opacity=".7" font-size="30" font-family="ui-monospace,Menlo">DOLLY · PAN · TILT · ORBIT</text>')


def img2video():
    strip = (frame(1000, 210, 400, 280) + "".join(f'<rect x="{1020 + i * 64}" y="226" width="34" height="22" rx="4" fill="#fff" opacity=".6"/>'
                                              f'<rect x="{1020 + i * 64}" y="452" width="34" height="22" rx="4" fill="#fff" opacity=".6"/>' for i in range(6))
             + '<path d="M1170 300v100l85-50z" fill="#fff" opacity=".9"/>')
    return (frame(480, 220, 340, 260) + f'<path d="M505 455l90-100 60 50 75-80 75 130" {S} stroke-width="7"/>'
            f'<path d="M860 350h110m-40-40 40 40-40 40" {S} stroke-width="9"/>' + strip)


def video_prompt():
    return img2video().replace('<path d="M505 455l90-100 60 50 75-80 75 130"', '<path d="M505 455l0 0"') + lines(510, 270, 280, 6, 34)


def _grid(n_cols=3, n_rows=2, x0=560, y0=150, w=240, h=160, gx=270, gy=190, inner=True):
    out = ""
    for r in range(n_rows):
        for c in range(n_cols):
            x, y = x0 + c * gx, y0 + r * gy
            out += frame(x, y, w, h)
            if inner:
                out += f'<path d="M{x + 30} {y + h - 30}l50-55 40 35 40-50 60 70" {S} stroke-width="5" opacity=".6"/>'
            out += f'<text x="{x + 12}" y="{y + 32}" fill="#fff" opacity=".7" font-size="22" font-family="ui-monospace,Menlo">{r * n_cols + c + 1:02d}</text>'
    return out


def sb_upgrade():  # 普通分鏡 → 專業分鏡
    plain = frame(470, 230, 300, 200, ".5") + lines(510, 300, 220, 3, 40, 7, ".4")
    pro = frame(950, 180, 420, 290) + f'<path d="M990 430l90-110 60 50 80-100 110 160" {S} stroke-width="6"/>' + \
        f'<path d="M950 180h420M1160 180v290M950 325h420" {S} stroke-width="2" opacity=".35"/>' + \
        f'<path d="M1120 285h80v80h-80z" {S} stroke-width="4" opacity=".9"/>'
    arrow = f'<path d="M810 330h100m-35-35 35 35-35 35" {S} stroke-width="9"/><path d="M860 240v-50m-20 20 20-20 20 20" {S} stroke-width="6" opacity=".7"/>'
    return plain + arrow + pro + '<text x="960" y="520" fill="#fff" opacity=".75" font-size="26" font-family="ui-monospace,Menlo">CU · 35mm · DOLLY IN · RIM LIGHT</text>'


def sb_director():  # 導演提案：分鏡 + 審核勾選
    checks = "".join(f'<path d="M1210 {210 + i * 70}l18 18 32-36" {S} stroke-width="7"/>' + lines(1280, 220 + i * 70, 120, 1, 0, 7, ".6") for i in range(5))
    return _grid(2, 2, 520, 170, 280, 180, 310, 210) + frame(1180, 160, 260, 380, ".6") + checks


def sb_prompter():  # 分鏡 → 出圖提示詞
    return _grid(2, 2, 480, 170, 250, 170, 280, 200) + f'<path d="M1060 360h80m-30-30 30 30-30 30" {S} stroke-width="8"/>' + \
        frame(1170, 190, 260, 340) + lines(1200, 250, 200, 7, 38) + \
        '<text x="1200" y="210" fill="#fff" opacity=".8" font-size="22" font-family="ui-monospace,Menlo">/imagine</text>'


def sb_manga():  # 漫劇：不規則漫畫格 + 對話框
    panels = (f'<path d="M480 140h420l-30 260H480z" {S} stroke-width="7"/><path d="M920 140h400v170H890z" {S} stroke-width="7"/>'
              f'<path d="M880 330h440v250H860z" {S} stroke-width="7"/><path d="M480 420h370l-20 160H480z" {S} stroke-width="7"/>')
    bubble = f'<path d="M560 200h230a40 40 0 0 1 0 80H640l-40 40v-40h-40a40 40 0 0 1 0-80z" {S} stroke-width="6"/>' + lines(590, 240, 160, 1, 0, 6, ".7")
    speed = "".join(f'<path d="M{960 + i * 40} 520l60-140" {S} stroke-width="4" opacity=".45"/>' for i in range(8))
    return panels + bubble + speed + '<text x="1180" y="270" fill="#fff" font-size="64" font-weight="800" opacity=".85">!!</text>'


def sb_period():  # 古裝劇情：飛簷 + 分鏡
    eave = (f'<path d="M520 300q60-10 120-70h520q60 60 120 70" {S} stroke-width="8"/><path d="M600 300v260M1200 300v260M560 560h680" {S} stroke-width="8" opacity=".8"/>'
            f'<path d="M700 230q200-90 400 0" {S} stroke-width="6" opacity=".7"/>')
    return eave + _grid(3, 1, 650, 360, 160, 110, 175, 0, False) + f'<circle cx="1320" cy="190" r="50" {S} stroke-width="6" opacity=".6"/>'


def sb_seconds():  # 逐秒分鏡腳本：時間軸
    ticks = "".join(f'<path d="M{500 + i * 55} 560v{-30 if i % 5 == 0 else -15}" {S} stroke-width="5" opacity=".7"/>' for i in range(16))
    labels = "".join(f'<text x="{492 + i * 275}" y="600" fill="#fff" opacity=".7" font-size="22" font-family="ui-monospace,Menlo">{i * 5:02d}s</text>' for i in range(4))
    clips = "".join(frame(500 + i * 275, 380, 250, 140) for i in range(4))
    return _grid(3, 1, 560, 150, 250, 170, 280, 0) + clips.replace('opacity=".9"', 'opacity=".55"') + f'<path d="M500 560h830" {S} stroke-width="6"/>' + ticks + labels


def cctv():
    roof = (f'<path d="M540 470q50-5 90-50h340q40 45 90 50" {S} stroke-width="8"/><path d="M640 420q160-70 320 0" {S} stroke-width="6" opacity=".7"/>'
            f'<path d="M600 470v190M1000 470v190M570 660h460M760 660v-110h80v110" {S} stroke-width="8" opacity=".85"/>')
    return (frame(470, 110, 680, 600, ".9", 5) + roof +
            f'<path d="M1010 200h120l20 30h-160z" {S} stroke-width="7"/><path d="M1030 230v40" {S} stroke-width="7"/>'
            '<circle cx="520" cy="160" r="14" fill="#ff5b5b"/>'
            '<text x="545" y="171" fill="#fff" font-size="34" font-family="ui-monospace,Menlo" opacity=".9">REC  0921-03-14 23:59:07</text>'
            '<text x="1040" y="690" fill="#fff" font-size="26" font-family="ui-monospace,Menlo" opacity=".7">CAM 02</text>')


THEMES = {
    "cinematic-storyboard-upgrader": sb_upgrade, "director-storyboard-planner": sb_director,
    "cinematic-storyboard-prompter": sb_prompter, "manga-storyboard-agent": sb_manga,
    "period-drama-storyboard-prompter": sb_period, "storyboard-script-generator": sb_seconds,
    "seedance-video-face-swapper": faceswap, "ai-film-script-builder": script, "viral-script-architect": viral,
    "viral-script-reformer": viral, "ancient-cctv-creative-video": cctv, "micro-expression-performance-framer": microexpr,
    "reverse-prompt-engineer": reverse, "talking-head-script-writer": talking, "image-prompt-polisher": polish,
    "camera-movement-spec-source": camera_move, "image-to-video-prompt-extractor": img2video,
    "sd-video-prompt-generator": video_prompt,
}


def build(category: str, slug: str, meta: dict) -> str:
    c1, c2 = PALETTE.get(category, ("#1f2730", "#5b7a96"))
    title = escape(meta.get("cn_tc") or meta.get("cn") or slug)
    desc = escape((meta.get("desc_tc") or meta.get("description") or "")[:34])
    art = THEMES.get(slug, script)()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{GEN_MARK}
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<radialGradient id="v" cx=".5" cy=".45" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
<pattern id="d" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="#fff" opacity=".08"/></pattern></defs>
<rect width="{W}" height="{H}" fill="url(#g)"/><rect width="{W}" height="{H}" fill="url(#d)"/>
<g>{art}</g>
<rect width="{W}" height="{H}" fill="url(#v)"/>
<rect x="64" y="64" width="{len(category) * 34 + 48}" height="56" rx="28" fill="#000" opacity=".35"/>
<text x="88" y="102" fill="#fff" font-size="30" font-family="-apple-system,'PingFang TC','Noto Sans TC','Noto Sans CJK TC','Noto Serif CJK TC',sans-serif" opacity=".9">{escape(category)}</text>
<text x="64" y="{H - 110}" fill="#fff" font-size="68" font-weight="700" font-family="-apple-system,'PingFang TC','Noto Sans TC','Noto Sans CJK TC','Noto Serif CJK TC',sans-serif">{title}</text>
<text x="66" y="{H - 58}" fill="#fff" font-size="32" opacity=".75" font-family="-apple-system,'PingFang TC','Noto Sans TC','Noto Sans CJK TC','Noto Serif CJK TC',sans-serif">{desc}</text>
</svg>
'''


def main() -> None:
    force = "--force" in sys.argv
    made = 0
    for d in sorted(p for p in ROOT.glob("*/*") if p.is_dir()):
        existing = list(d.glob("cover.*"))
        ours = all(p.suffix == ".svg" and GEN_MARK in p.read_text(encoding="utf-8", errors="ignore") for p in existing)
        if existing and not (force and ours):
            continue  # 有手作封面就不動；--force 只重畫本腳本產生的
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8")) if (d / "meta.json").is_file() else {}
        (d / "cover.svg").write_text(build(d.parent.name, d.name, meta), encoding="utf-8")
        made += 1
        print("✓", d.relative_to(ROOT))
    print(f"完成：{made} 張")


if __name__ == "__main__":
    main()
