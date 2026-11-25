---
name: absurdist-comedy-maker
description: "Absurdist comedy: turns any topic into a nonsense-comedy short; supports script rewriting and photo memes"
---

# Japan Camedy Film

Turn a creative idea into **a single numbered storyboard-style prompt that can be pasted directly into Seedance 2.0**. First align on the style with the "Analysis Framework" below, then produce the output following the Workflow.

---

## Analysis Framework (The Three Cornerstones of This Type of Video)

### 1. The Essence of the Style

- **Core mechanism**: Use refined, meticulously crafted retro imagery to build a seemingly serious situation; the stark gap created by the twist is the punchline — the more the setup plays like a straight drama, the harder the reversal hits.
- **Visual sources**: Borrow broadly from Japanese pop culture around the year 2000, blending the era's films, music videos, commercials, and fashion magazines; also take in street styles such as Y2K, Lolita, and Visual Kei. Not tied to any single work.
- **Performance tone**: Always restrained and earnest — characters stay dead-serious and never break character, laying the groundwork for the absurd ending.

### 2. Visual Elements

- **Color & texture**: A slight film-like texture and grain; mid-tone colors, low saturation, with an overall tint leaning a touch blue.
- **Lighting & atmosphere**: Daytime exteriors mostly natural light; nights/interiors mostly ambient light. **Faces are lit naturally and softly, with no shadows** (this is a fixed rule).
- **Set design**: Elaborate, packed with retro details. Outdoors — streets, parks, school campuses; indoors — Japanese tatami rooms, old-school cafés, izakayas hung with red lanterns, countryside courtyards, and the like.
- **Character styling**: Boldly symbolic and highly recognizable — personality legible at a glance. Common types: Lolita girl, school students, Visual Kei youth, office workers, kimono looks, etc. **Wardrobe is redesigned around "character identity + the scene they're in"; never reuse the reference image's / the character's original outfit**.
- **Camera language + VFX**: Mostly locked-off shots, with only a little push/pull/pan/tilt/follow; no flashy camera work. **The twist is pulled off mainly through a hard cut + performance**. If VFX are used, they must melt into the live-action frame — sharing the same lighting, materials, and grain, with no compositing edges (nothing that pops) — and never steal the show.

### 3. Story Content

- **Three-part narrative**: First earnestly lay out a small everyday matter → amplify the expressions/actions layer by layer (often with super slow motion) → complete the reversal via a single **hard cut or sudden swerve in performance** → after the twist, close on a deadpan pause.
- **Story structure**: Minimalist. One short film carries exactly one punchline; at bottom it always comes down to "a character is doing something ordinary, and then the unexpected happens."
- **Common twist types (seven categories — all live-action situations, no magical transformations)**: ① Emotional whiplash (**must have cause and effect; never arbitrary**) ② Identity reversal / gap moe (the fierce big shot is secretly scared of cats; the delicate girl is actually a boxing champion) ③ Anticlimax (something huge is set up with full solemnity, only to land on something tiny) ④ Dialogue reversal (one line flips the whole scene) ⑤ Awkwardness reversal (toe-curling social death / dead silence) ⑥ Attack–defense reversal / tables turned (the dominant party suddenly crumbles; the underdog presses back) ⑦ Mountain-out-of-a-molehill / scale reversal (epic slow motion and score applied to something utterly trivial). "Nested layers" is a structure, not a type: any category can take another round stacked on top. The punchline can ride on dialogue, performance, or VFX; **the twist is achieved mainly through a hard cut + performance**.
- **Character dynamics**: Usually a duo of partners with opposite personalities and sharply contrasting looks (one strong, one weak; one dynamic, one composed); the conflict is defused or overturned by an absurd twist at the end.

---

## Workflow

**Step 1 · Input**: The user provides a one-line idea; for an ad, they can also upload product images + selling points. Three entry points — pick one: from scratch (guided flow: the three questions of scene / character / twist) / existing idea (fill in only the gaps) / reverse-engineer a reference video (extract frames to study its beats before writing an imitation; never describe footage you haven't seen out of thin air).

**Step 2 · Product handling (only if product images were uploaded)**: Immediately generate the product's **three-view sheet + detail close-ups**, locking it in as `{Product1}` to keep it consistent across the whole film and clearly featured; also nail down the **1–3 core selling points** (skip the question if they were already given in Step 1). **Red line**: the skit must showcase the selling points positively — **never fabricate / exaggerate / disparage / smear the product**. The punchline must not land on a product flaw and must match the real selling points.

**Step 3 · Ask all up-front questions in one pass** (use `ask_human`; skip follow-ups wherever possible): duration **15 / 30 / 60s** · purpose (grow followers / sell products / branding) · creative device (pick one of the seven twist types, or "you decide for me") · target platform (Douyin / Xiaohongshu / YouTube…) · language (Japanese / Chinese; if Chinese, further choose **Chinese setting / keep the Japanese setting**) · subtitles (Chinese / Chinese–Japanese / Chinese–English, **not burned in at generation time; added when assembling the final video**) · slogan (optional).

**Step 4 · Character & visuals**: Model appearance — first ask **① I generate the three-view sheets / ② you upload them** (if generated: one sheet per person, left→right **face close-up ｜ full-body front ｜ full-body back**, after the wardrobe change); produce the scene image `{Scene1}` (16:9, neutral white balance, no yellow cast); the style seed (retro Japanese film / Chinese retro; neutral colors with no yellow cast; soft, shadow-free face lighting); wardrobe redesigned by "identity + scene," never carrying over the original outfits. Feed the three-view sheets / scene image back in as reference images, bound to `{roleN}` / `{Product1}` / `{Scene1}` so everything stays consistent with no continuity breaks.

**Step 5 · Design the skit + map on the visuals**: Drop the three-part structure (earnest setup → escalating layers → reversal via **hard cut / sudden swerve in performance** → deadpan afterglow) onto numbered shots, using the chosen twist type and pairing partners of opposite temperament; spell out "how to play it"; dialogue in the chosen language is **spoken only, with no burned-in subtitles**; tight pacing, no wasted shots. Complete the visuals to match the established tone (soft shadow-free face lighting / retro setting / redesigned wardrobe / mostly locked-off camera / VFX that never pop).

**Step 6 · Output the storyboard prompt → generate once satisfied → assemble the video**: Output the prompt (entirely in **Chinese**, **16:9**, first line fixed as `画面内容请参考场景氛围图 {Scene1}`, including `{roleN}` and the product's on-screen appearance); **emit the whole passage in one go, generating in 15s segments** (shot cuts within a segment are left to the model; don't hard-lock camera positions): 15s = 1 segment, 30s = 2 segments, 60s = 4 segments; **continue segment by segment** (each later segment picks up from the previous segment's last frame / the same `{roleN}` reference), produce one segment, get confirmation, then continue with the next — `{roleN}` / wardrobe / lighting / setting consistent throughout, no continuity breaks. After outputting, ask "satisfied / want changes" — **if satisfied → call the connected video-generation connector directly to kick off generation at 16:9**, no manual step; then **assemble the video**: overlay subtitles (the Step 3 choice) + voiceover + slogan / end-of-video product placement (via editing or `ffmpeg`); with no tools available, deliver the prompt + subtitle text / SRT.

## Style-Lock Block (Use Verbatim During Generation)

> Proven-effective wording for **driving the model**. **The finished prompt is entirely in Chinese, so use the ZH version below as the style layer** (the EN version is kept for reference only). **Color calibration: rich but with a neutral white balance, no yellow/over-warm cast (mid-tones, leaning slightly cool) — avoid an overall yellowish tint.** **If the Chinese setting is chosen**: swap "Y2K Japanese film" in the style-lock sentence for "Chinese retro imagery from around the millennium (classic mainland dramas / Hong Kong cinema texture)"; the color, face-lighting, and film-texture principles stay unchanged.

**EN:**

```
Fully reference the colour grading and scene set of the Y2K Japanese film. A
cinematic masterpiece, retro Y2K Japanese movie aesthetic, raw 35mm film stock
texture with strong contrast, rich colours with a neutral white balance (no overall
yellow/warm cast, slightly cool mid-tones), nostalgic film grain, soft lens flare,
2000s cinematic lighting, soft and even light on
faces with no harsh shadows.
```

**ZH:**

```
完全参考 Y2K 日本电影的色彩分级与场景设置。电影杰作，复古 Y2K 日本电影美学，
原始 35mm 胶卷质感，强对比，色彩浓郁但白平衡中性、不偏黄不过暖（中间调、略偏一点冷），怀旧胶片颗粒，柔和镜头光晕，
2000 年代电影灯光，人物面光柔和均匀、无生硬阴影。
```

---

## Full Example (Anticlimax + Attack–Defense Reversal · Chinese prompt, dialogue spoken only with no burned-in subtitles, 16:9)

```
画面内容请参考场景氛围图 {Scene1}。
完全参考 Y2K 日本电影的色彩分级与场景设置。电影级复古日影质感，原始 35mm 胶卷质感，强对比，色彩浓郁但白平衡中性、不偏黄不过暖（中间调、略偏一点冷），怀旧胶片颗粒，柔和镜头光晕，人物面光柔和均匀、无生硬阴影。16:9 横屏，老派居酒屋、红灯笼暖光、复古细节繁复，肤白无瑕；服装按场景重设。本片为严格的多镜头序列：
1. 中景（缓推、超慢动作）：气场强大的大佬 {role1} 神情肃杀，缓缓卷起袖子、拿起一把菜刀，眼神凶狠，气氛剑拔弩张。
2. 特写：{role1} 屏息凝神，刀锋映着红灯笼的光，郑重得像要大干一场。
3. 【硬切】到俯拍特写：砧板上——他一丝不苟地把刀切向……一根黄瓜，切成整齐薄片摆进小碟（反高潮）。
4. 过肩中景：对面瘦小的店员 {role2} 怯怯开口，用日语说"…不用切得这么认真啦"。
5. 反应特写：{role1} 猛地抬眼、气势回笼，狠狠瞪向 {role2}。
6. 中景：{role2} 却面无表情、慢悠悠回一句日语"…刀工不行"（攻守逆转）。
7. 反应特写：{role1} 表情一僵、气势瞬间垮掉，讪讪低头继续切菜；{role2} 淡定端走那碟黄瓜。
人物动作自然连贯、彼此同步；节奏紧凑，每一镜都在推进笑点。
```

---

## General Constraints

- The entire prompt is written in Chinese; dialogue follows the language chosen in Step 1 and is **spoken only, with no burned-in subtitles**; subtitles are added when the final video is assembled in Step 6, per the user's choice (Chinese / Chinese–Japanese bilingual / Chinese–English bilingual); wrap everything in a copyable code block.
- Use {roleN} for characters — written out in full at first appearance, reused thereafter, with clear who-does-what-to-whom in interactions; **wardrobe is redesigned around character identity + scene; never reuse the original outfit**.
- Write the performance clearly (how to play it); **the punchline can be carried by dialogue, performance, or VFX — any one of the three**; dialogue is spoken only with no burned-in subtitles, short and natural; the plot advances at a tight pace with no wasted shots.
- Locked-off camera as the default; the twist is achieved mainly through a **hard cut + performance**; any VFX used must never pop (shared lighting, materials, and grain; no compositing edges).
- One short film carries one reversal (nested layers count as an extension of it); usually paired with partners of opposite temperament.
- 15s: output in one go; 30s: output the first 15s first, then continue with the following 15s after confirmation; 60s: continue in four segments; no continuity breaks at any point.
- Product ads: confirm the selling points first; the skit must showcase them positively and show the product clearly; **never fabricate / exaggerate / disparage / smear the product** — the punchline must not land on a product flaw and must match the product's real selling points.
- **Content ethics red lines (must be observed)**: no pornography, sexual innuendo, or nudity; no violence, gore, injurious fights, weapon harm, or crime tutorials; **no tattoos**; nothing touching on death, suicide, self-harm, corpses, supernatural horror, and the like; no glamorizing tobacco, alcohol, or drugs; nothing involving hate, discrimination, or politically sensitive topics. Punchlines land only on situations, performances, and contrast — keep things light, age-appropriate, and harmless.
- Do not make content involving real public figures; keep it appropriately harmless.