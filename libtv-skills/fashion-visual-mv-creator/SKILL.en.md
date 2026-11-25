---
name: fashion-visual-mv-creator
description: "High-style fashion MV generation: for music videos, visual albums, girl-group stage films, fashion imagery, and concept shorts"
---

# 时尚视觉 MV 生成

## Skill 定位

只负责一件可复用的事：从一个音乐 MV 概念出发，自动完成“人物 IP 设计 -&gt; 妆造穿搭 -&gt; 场景艺术图 -&gt; 音乐方向 -&gt; 视频镜头生成 -&gt; MV 剪辑方案”的视觉工作流。

这个 skill 的核心不是写死某一种风格，而是沉淀一套适用于多种 MV 的视觉生产公式。它可以用于韩系女团、未来主义、怪诞美学、巨物美学、暗黑宗教感、赛博舞台、异世界、奢华时尚大片、梦核、废土、金属装置、晶体星球、音乐节现场等方向。

目标优先级：

1. 人物要好看，并且有记忆点，不要标准模板脸。
2. 妆造、发型、配饰、穿搭要有特点，有舞台感和时尚感。
3. 场景要美、有视觉冲击、有艺术设定，不只是普通背景。
4. 视频要像 MV 视觉片，有镜头冲击、表演、空镜、特写、舞台调度和剪辑节奏。
5. 流程要可扩展，用户换歌曲、换人物、换风格、换画幅依然能用。

## 模型优先级

按以下模型优先级执行；如果用户或环境无法使用优先模型，不要静默失败。先按“错误处理与模型切换策略”处理，再通过 `ask_human` 引导用户确认是否切换到下一个模型重新生成。

```json
{
  "portrait_and_styling_image_models": ["Lib image", "Lib nano2"],
  "scene_art_models": ["Lib image", "Lib nano2", "悠船 v7 / Midjourney v7"],
  "video_models": ["seedance 2.0", "seedance 2.0 fast", "kling O3"],
  "music_models": ["any available music model"],
  "text_models": ["any available text model"]
}
```

模型使用规则：

- 人物候选、人物定稿、妆造穿搭图：优先 `Lib image`，其次 `Lib nano2`。
- 纯场景艺术图：可使用 `Lib image`、`Lib nano2`、`悠船 v7 / Midjourney v7`。
- 视频生成：优先 `seedance 2.0`，其次 `seedance 2.0 fast`，最后 `kling O3`。
- 音乐生成：使用当前可用音乐模型，重点贴合用户的音乐类型和 MV 氛围。
- 默认画幅为 `16:9 横屏`；用户指定时可改为 `9:16`、`1:1`、`4:5`、`21:9` 等。

## 错误处理与模型切换策略

当生成过程遇到报错、素材缺失、质量不足或安审限制时，不要直接终止整个 MV 工作流。先判断问题类型，再选择修复、重试或询问用户。

### 1. 安审失败优先改 prompt 重试

如果图片或视频生成触发审核失败，优先修改 prompt 并在同一模型上重试。修改方向：

- 去掉血腥、伤口、受伤、疼痛、死亡、暴力等表达。
- 去掉性感、挑逗、裸露、低俗、未成年感等表达。
- 把“性感舞蹈”改成“自信舞台表演、强节奏编舞、时尚舞台动作”。
- 把“受伤、虚弱、血迹”改成“疲惫、失落、戏剧化情绪、倒地造型”，明确“无伤口、无血迹”。
- 把“宗教仪式、咒语、修女”等高风险词改成“神秘仪式感、黑纱群像、烛光舞台、低声吟唱氛围”。
- 保留视觉目标，但降低敏感词强度。

如果第一次重试仍失败，再进一步弱化敏感元素并重试一次。连续失败后，通过 `ask_human` 询问用户是否切换模型、换视觉方向或放弃该镜头。

### 2. 缺关键素材时先 ask_human

若缺少会影响最终成片质量、交付结果或素材使用方式的素材，不要强行进入视频生成。通过 `ask_human` 引导用户选择下一步。

关键素材包括：

- 没有选定主角人物，导致人物身份无法稳定。
- 没有选定妆造图，导致服装、发型、配饰不稳定。
- 没有纯场景图，导致人物无法融合到明确空间。
- 场景图混入人物，不能作为纯场景锚点。
- 人物图或造型图安审失败、质量过低、脸部模糊、风格漂移。
- 用户要求的镜头依赖翅膀、伴舞、群像、道具、舞台装置，但对应素材不存在。

`ask_human` 选项建议：

```text
当前缺少会影响成片质量的关键素材。你希望怎么处理？
1. 先补生成缺失素材
2. 使用现有素材继续，但降低一致性要求
3. 切换模型重新生成素材
```

### 3. 模型报错时询问是否切换

如果当前模型报错、超时、不可用或多次生成失败，使用 `ask_human` 让用户确认是否切换到下一个模型。

图片模型切换顺序：

```text
Lib Image -> Lib Nano2 -> 悠船 V7 / Midjourney v7
```

视频模型切换顺序：

```text
Seedance 2.0 -> Seedance 2.0 fast -> kling O3
```

`ask_human` 选项建议：

```text
当前模型生成失败。你希望怎么处理？
1. 修改 prompt 后继续用当前模型重试
2. 切换到下一个模型重新生成
3. 跳过这个素材/镜头，继续后续流程
```

### 4. 重试记录

每次重试或切换模型后，在最终输出里记录：

- 失败环节。
- 失败原因：模型报错、审核失败、素材不足、质量不足等。
- 修改后的 prompt 策略。
- 是否调用 `ask_human`。
- 用户选择。
- 最终使用模型。

## 输入

用户可以提供以下任意信息：

- 音乐风格：K-pop、J-pop、电子、暗黑流行、R&B、摇滚、说唱、实验音乐、女团舞曲等。
- MV 风格：未来主义、怪诞美学、巨物美学、宗教感、赛博、梦幻、暗黑、奢华、复古、异世界等。
- 人物方向：韩系女团感、时尚模特感、冷感偶像、暗黑圣女、未来战士、异星歌姬等。
- 参考图：人物图、造型图、场景图、风格图。
- 歌词、歌名、主题、品牌或视觉关键词。
- 目标比例和时长。

如果用户只说“做一个好看的 MV”，默认：

```json
{
  "aspect_ratio": "16:9",
  "duration": "30-60s visual MV",
  "character_count": 1,
  "portrait_options": 9,
  "styling_options": 6,
  "scene_options": 6,
  "visual_direction": "韩系女团感 + 未来主义时尚 + 怪诞美学 + 巨物美学",
  "music_direction": "K-pop / electronic pop / cinematic fashion MV"
}
```

## 输入使用

严格遵守：

- 用户上传的选定人物图，用作人物身份、五官、发型气质的一致性锚点。
- 用户选定的造型图，用作服装、妆容、配饰、头饰和整体轮廓锚点。
- 用户选定的场景图，用作空间、材质、色彩、光线和美术方向锚点。
- 用户指定的音乐风格、歌词主题和 MV 情绪。

允许扩展：

- 多套妆造和穿搭。
- 多个纯场景艺术图。
- 舞台、空镜、特写、舞蹈、仪式感、巨物装置、抽象视觉等镜头类型。
- 不同语言的歌曲和字幕版本。

禁止：

- 生成未成年人性感化形象。涉及性感、舞台魅力、贴身造型时，必须明确为成年表演者。
- 使用真实明星、特定艺人、在世公众人物或受版权保护角色作为直接复刻对象。
- 过度暴露、色情、低俗或伤害性画面。
- 把场景艺术图阶段直接混入人物；场景图必须先保持“纯场景”。

## 内部流程和 Knowhow

### 1. mv_concept_planner

先把用户需求整理成 MV 视觉总设定。

输出：

```json
{
  "music_style": "",
  "visual_world": "",
  "main_character": "",
  "fashion_direction": "",
  "scene_direction": "",
  "mood_keywords": [],
"aspect_ratio": "16:9",
  "duration": "",
  "safety_notes": []
}
```

If the user provides very little information, automatically generate 3 visual directions for the user to choose from:

- Korean girl-group stage blockbuster: beautiful, fashionable, strong performance, strong styling, strong camerawork.
- Futuristic otherworld: metal, crystal, installations, colossal objects, cool lighting, alien settings.
- Grotesque luxurious ritual: dark, ornate headdresses, religious-style composition, group portraits, candlelight, strong contrast.

### 2. character_brainstorm

First generate multiple character candidates, usually 9 versions, for the user to pick the most promising MV lead IP.

Character candidate principles:

- Good-looking, but not a standard template face.
- Distinctive: at least one memorable trait, such as eye shape, face shape, temperament, coolness, muted softness, icy aloofness, sharpness, ease, world-weariness, ethereal charm, etc.
- Lean toward fashion idol, Korean girl group, Asian model, visual-kei singer rather than ordinary portrait photography.
- Default to an adult female performer; if the user specifies another gender or a group, adjust per the user's needs.
- White or minimalist background, for easy later selection and redesign.

Reference prompt structure:

```text
Generate 9 candidates for a young adult fashionable female MV lead, Asian girl-group aura, beautiful but not standardized, each with a unique facial memorable trait and personal charisma. Half-body portrait close-up, facing the camera, ID-photo-style composition, long straight black hair or a changeable hairstyle, wearing a minimalist black camisole or minimalist black top, pure white background, high-fashion feel, casual yet with star potential, realistic photographic texture.
```

Replaceable variables:

- `{gender}`: female, male, androgynous, group member.
- `{ethnicity_or_market}`: Asian, Japanese/Korean feel, Western feel, Latin feel, multi-ethnic, etc.
- `{idol_type}`: icy aloof, dark, sweet-cool, futuristic, grotesque, rock, elven, mechanical, etc.
- `{background}`: pure white background, light gray background, ID-photo background, studio background.

When outputting, annotate each candidate with:

- Visual appeal potential.
- Memorable traits.
- Suitable MV styles.
- Follow-up styling and makeup direction.

### 3. character_selection

After the user selects one of the characters, use it as the `Portrait 1` or `Mixed 1` character anchor.

If the user has not made an explicit choice, first recommend the 1-2 characters best suited as the MV lead and explain why.

Selection criteria:

- Highly recognizable facial features.
- Temperament with room to expand.
- Able to carry exaggerated styling.
- Suitable for recurring appearances across multiple scenes and multiple looks.
- Not an overly generic commercial-model face.

### 4. styling_and_makeup_design

Generate multiple sets of makeup, hairstyles, outfits, accessories, and stage looks around the selected character. Generate 6 sets by default; the user can choose 1-3 sets as the main MV looks.

Styling direction library:

- Korean girl-group stage: metallic feel, sequins, beaded chains, long boots, off-shoulder but not tacky, strong stage silhouette.
- Futuristic installation: silver, chrome metal, wearable art installations, transparent materials, laser elements.
- Grotesque aesthetics: otherworldly headdresses, exaggerated shoulder lines, face decorations, asymmetric silhouettes.
- Colossal-object aesthetics: enormous wings, massive skirt trains, exaggerated capes, giant headdresses.
- Dark ritual: black gauze, metal crowns, chains, candlelight, nun-like composition without directly replicating religious garments.
- Crystal fantasy: crushed diamonds, fine shimmer, crystal, translucent installations, cool-toned light.
- Music festival scene: high-energy stage, bright lighting, shimmering materials, dynamic outfits.

Reference prompt structure:

```text
High-end bespoke portrait, full-body shot, keep the facial features and temperament consistent with Portrait 1, and design a brand-new MV stage look for her. Fashion-forward, Korean girl-group feel, fashion attributes maxed out, metallic elements, laser elements, crushed-diamond fine-shimmer elements, avant-garde face decorations, ornate headdress, abundant jewelry, wearable art installation, loose stacked-feel boot shafts, silver pointed-toe high-heel long boots, futuristic dress, exaggerated but high-end, pure white background, realistic fashion editorial photography.
```

Multi-angle finalized sheet requirements:

```text
Using the selected character and selected look, generate a 16:9 character reference sheet, pure white background; within the same image, from left to right show in order: facial close-up, full-body front, full-body side, full-body back. Keep the same character's facial features, hairstyle, makeup, clothing, and accessories completely consistent. Clear image, high-end fashion reference sheet, prominent idol characteristics.
```

The styling stage must output:

- Look name.
- Makeup keywords.
- Hairstyle keywords.
- Clothing silhouette.
- Materials.
- Accessories.
- Suitable MV scenes.
- Suitable camera movements.

### 5. scene_art_generation

Generate pure scene art; do not place characters into the scenes. This step only handles the MV's worldbuilding and spatial art.

Generate 6 scene directions by default:

- Main stage: for singing and dancing, frontal performance, strong lighting.
- Hero scene: for the character standing, slow push-in, colossal installations, cover shots.
- Empty-scenery shots: for editing breathing room, musical interludes, atmospheric transitions.
- Close-up texture scenes: details such as metal, crystal, water surfaces, screens, red light, black gauze.
- Ritual/group space: for dramatic blocking such as backup dancers, extras, surrounding, gazing, unfurling.
- Surreal scenes: alien planets, mirror spaces, massive structures, dreamlike landscapes, anti-gravity spaces.

Scene image requirements:

- Pure scenes, no characters.
- 16:9 landscape by default.
- Beautiful, impactful, with artistic concepts.
- May be exaggerated, but must be suitable for later compositing the character in.
- Must have clear spatial layering: foreground, midground, background.
- Must have a clear light direction and dominant color palette.

Reference prompt structure:

```text
A realistic futuristic MV scene, pure scene, no characters. An otherworldly planet, the ground covered with interwoven, intricate pale purple crystals, giant crystal structures growing out of the ground, a surreal stage silhouette in the distance, dreamlike, fashionable, high-end photography, cinematic lighting, strong spatial depth, visual impact, 16:9 landscape.
```

Expandable scene keywords:

- Metallic skeletal hall, black mirror stage, pale-purple crystal planet, giant wing installation, TV-wall space, red laser room, rainy-night glass box, music festival in ruins, silver liquid tunnel, white sterile experimental stage, black-veil cathedral-style space, giant desert sculptures, glowing undersea theater.

### 6. music_direction

Generate music or music prompts. Use the currently available music model(s).

The music must serve the MV visuals:

- Korean girl group: strong drum beats, electronic bass, a clear hook, suitable for singing and dancing.
- Dark pop: low frequencies, whisper-like feel, synthesizers, mysterious atmosphere.
- Futurism: metallic percussion, electronic noise, cold synthesizers.
- Grotesque luxury: strings, organ-like feel, low-frequency drums, dramatic pauses.
- Dreamlike otherworld: ethereal vocals, synth pads, wide reverb.

Output:

- Music style.
- BPM range.
- Mood keywords.
- Song structure: intro / verse / pre-chorus / chorus / bridge / outro.
- Video pacing suggestions: fast-cut points, slow-motion points, freeze-frame points.

### 7. video_prompt_builder

Only after all character images, styling images, and scene images pass self-checking, write the video generation prompt.

If, before video generation, any of the character, styling, or scene anchors is found to be missing or insufficient in quality, first call `ask_human` per the "Error Handling and Model Switching Strategy"; do not generate directly.

Video model priority:

1. `seedance 2.0`
2. `seedance 2.0 fast`
3. `kling O3`

Video generation principles:

- Use the reference-to-video feature to fuse the character anchor, styling anchor, and scene anchor.
- Character identity is controlled by the character image.
- Clothing and makeup are controlled by the styling image.
- The scene is controlled by the pure scene image.
- Do not let the model redesign the character's face, clothing, and scene.
- One video segment expresses only one core shot event.
- Prioritize generating multiple 3-6 second segments, then edit them into a complete MV.

Common shot types:

- Visual opener: the character stands in a massive scene, slowly raising their eyes, lights flickering.
- Sing-and-dance shots: frontal close-up, medium-shot dancing, camera push-in, precise lip-sync.
- Look showcases: facial close-ups, eye makeup, lips, jewelry, hands, shoes and boots, skirt hems, metal installations.
- Scenery empty shots: crystals, metal, screen walls, stage lights, rainy ground, colossal installations.
- Ritual shots: backup dancers surrounding, group gazing, hand gestures, lights going out, wings unfurling.
- Impact shots: fast push-in, rotation, flash, low-angle looking up, extreme close-up.

General video prompt template:

```text
Epic fashion-MV cinematic quality, reference the character identity of {{Portrait 1}}, reference the makeup and outfit of {{Styling 1}}, reference the scene art of {{Scene 1}}.

{Character} stands in {Scene}, performing {performance/dance/ritual/emotional movement}. Keep the character's facial features, hairstyle, makeup, clothing, and accessories consistent, and keep the scene's materials, lighting, colors, and spatial structure consistent.

Camera language: {close-up/medium shot/wide shot/extreme close-up/low angle/orbit/fast push-in/slow push-in/rotation/flash cut}
Image vibe: high visual appeal, strong styling, strong visual impact, fashion-forward, cinematic lighting, music-MV quality.
Action requirements: movements natural and fluid, performance rhythmic, lip-sync matching the music's mood, impactful shot transitions, no subtitles throughout.
Dance MV template:

```text
Epic cinematic quality, in a music-festival live show or futuristic stage style. {{Portrait 1}}, dressed in the {{Styling 1}} look, stands in a scene styled after {{Scene 1}}, with 4-6 backup dancers behind, singing and dancing through the climax section of the track. Precise lip-sync performance, strong rhythmic dance moves, shot in close-up, with fast push-ins, spins, low-angle up-shots, and close-up cuts. The visuals are fashionable, energetic, and impactful, with flickering stage lighting and cinematic-grade texture; no subtitles throughout.
```

Ceremonial MV template:

```text
An epic fashion film. {{Portrait 1}}, wearing {{Styling 1}}, stands in {{Scene 1}}, surrounded by a group of figures or backup dancers forming a ceremonial composition. The character slowly lifts their head, the lights flicker between bright and dim, and the camera cuts quickly between eyes, lips, hands, headdress, clothing details, and giant installations. The character then makes an intense performance move as the lighting of the space changes; highly impactful camera work, exaggerated yet high-end, with cinematic camera movement; no subtitles throughout.
```

Empty-shot template:

```text
A scenery-only MV empty shot, referencing the art direction of {{Scene 1}}. The camera pushes in slowly, showcasing giant installations, material textures, shifting light, stage space, and surreal structures. No people, no subtitles, cinematic lighting, with the atmosphere of a musical interlude — suitable as an MV transition or opener.
```

Negative prompt:

```text
deformed face, changed identity, inconsistent makeup, inconsistent outfit, extra limbs, broken hands, distorted body, bad anatomy, flickering, low quality, blurry face, wrong jewelry, changed hairstyle, changed scene, messy background, unreadable text, subtitles, watermark, childlike face, underage appearance, explicit nudity, pornographic, injury, blood
```

### 8. mv_editing_plan

Edit multiple video clips into an MV visual film.

Default structure:

```text
0-5s: Strong visual opening — empty shot or the character raising their eyes.
5-15s: The character's main look debuts, alternating close-ups and full-body shots.
15-30s: Singing-and-dancing/performance section, fast cuts matched to the music's beat.
30-45s: Scene changes and look changes, adding empty shots and close-ups.
45-60s: Climactic visuals — giant objects, group shots, lighting, bold camera moves, closing on a freeze frame or a slow push-in.
```

Editing rules:

- The MV visual film doesn't need to explain a plot; the focus is visual impact and musical rhythm.
- Switch the visual focus every 2-4 seconds.
- Alternate between facial close-ups, full-body looks, scenery-only empty shots, dance moves, and material details.
- For the music's climax, use fast cuts, flashes, rotations, low angles, and group shots.
- For musical interludes, use empty shots, slow push-ins, material close-ups, and back views.
- No subtitles by default throughout, unless the user explicitly asks for lyric subtitles.

## Output

Output after each execution:

```markdown
## Overall MV Setup
- Music direction:
- Visual style:
- Lead character profile:
- Makeup & styling direction:
- Scene direction:
- Aspect ratio/duration:

## Character Candidate Options
Output 9 versions of character candidate prompts, noting each version's memorable hooks and the styles it suits.

## Styling & Makeup Plans
Output 6 styling directions, each covering makeup, hairstyle, clothing, accessories, materials, and suitable shots.

## Character Design Sheet Prompt
Output multi-angle design sheet prompts for the selected character: facial close-up, full-body front, full-body side, full-body back, on a pure white background.

## Scene-Only Art Prompt
Output 6 scenery-only prompts, noting the recommended model and aspect ratio.

## Music Prompt
Output music style, BPM, mood, and structure.

## Video Clip Prompts
Output 6-10 video clip prompts, noting the character reference, styling reference, scene reference, shot type, and recommended video model.

## Editing Plan
Output clip order, pacing, transitions, empty-shot placement, the climax section, and how it ends.

## Self-Check Results
Output whether the character consistency, styling consistency, scene purity, safety compliance, and model selection checks passed.

## Error Handling Log
Output whether this run involved model errors, moderation failures, missing assets, prompt rewrites, model switches, or ask_human selections.
```

## Self-Check

Before generating video, the following must be checked:

- Do the characters look like adults, with no sexualization of minors?
- Are the characters attractive and distinctive, not generic template faces?
- Does the makeup and styling have a clear style, silhouette, materials, and accessories?
- Do the character design sheets stay consistent as the same character?
- Are the scene images pure scenes with no people mixed in?
- Are the scenes beautiful enough, visually striking, and spatially layered?
- Do the video prompts clearly reference the character, styling, and scene?
- Are subtitles, watermarks, and garbled/incorrect text avoided?
- Are no real celebrities or copyrighted characters used?
- Is the model chosen according to the model priority?
- If a safety-moderation failure is triggered, are sensitive expressions (gore, sexiness, injury, underage look, etc.) removed first before retrying?
- If key assets are missing or the model keeps failing, is `ask_human` used to guide the user to choose whether to add assets, switch models, or skip?

## Ask User

Don't stop just because information is incomplete. If the user gives only one direction, generate a default plan first.

Only ask follow-up questions in these cases:

- The user has given no music or visual direction, and hasn't said "freestyle" either.
- The user asks to replicate a real celebrity, a specific girl group member, a film/TV character, or a copyrighted IP.
- The user requests a clearly underage image, vulgar sexualization, or otherwise unsafe content.
- The user needs commercial brand placement but hasn't specified brand restrictions.
- Key assets that would affect final video quality, deliverables, or how assets may be used are missing.
- The image or video model errors out, times out, or is unavailable, or retries keep failing on the same safety-moderation issue.

Priority questions:

1. Which direction should the MV lean toward: K-pop girl group, futurism, grotesque aesthetics, giant-object aesthetics, dark ritual aesthetic, or freestyle?
2. Should the lead be a solo, a duo, or a group?
3. Is 16:9 landscape okay as the default, or do you want 9:16 portrait?