---
name: life-observed-doc
description: "Observational documentary shorts: film people before places, restrained rather than sentimental"
---

# documentary-flow

Use this skill when creating **humanistic documentary shorts** — observational imagery with a unified global/international aesthetic, focused on real human life. The core is **observing life rather than shooting stories**: authenticity and human emotion > strong dramatic conflict. Use the first-frame design image as a visual anchor, then use subtle-motion image-to-video to generate documentary shots with restrained camera movement.

> Environment adaptations: GPT Image 2 (first-frame/element images) → `generate_image_v3` (2K); Happy Horse FirstFrameToVideo (first-frame image-to-video) → `generate_video_v3` (first-frame-driven path, starting at 720p); ElevenLabs narration / Suno·Mureka instrumental BGM → `generate_audio`; Final_Video_Spec.md and structured text → `write_file_v2`; storyboard design → done within the storyboard phase; video_assembler → `composite_video`; `@asset`/asset binding → `reference_nodes`+`{{NodeKey}}`; membership/credits-type tools: none. **All narrative/camera-movement/visual-texture/prompt-writing craft is inlined within this skill, with no reliance on external craft skills and no native cross-skill dependencies.**

## 1. Workflow (pause for confirmation at each stage; never run through in one go)

1. **Stage 0 · Final_Video_Spec**: Use `write_file_v2` to create Final_Video_Spec.md, locking in: film title, subject region, aspect ratio, target duration, visual style, output language (see Section 2).
2. **Stage 1 · Reference material analysis** (if the user uploads reference images/videos): extract signals for downstream use (see Section 3).
3. **Stage 2 · Storyboard**〔pause〕: produce key elements, shot list, audio layers (see Sections 4, 5, 6). Once the storyboard is ready, **scan the context** for assets the user has provided or that were generated earlier and match storyboard entries (element images/BGM, etc.); for each match, before generating, use `reference_nodes` to **bind the asset to the corresponding storyboard slot** to avoid regenerating content the user already has. Present for confirmation.
4. **Stage 3 · Element setup**〔pause〕: If the user has already uploaded element resources (character images/reference characters) → bind them directly as assets for the corresponding key_element; otherwise, use `generate_image_v3` to generate images for all elements (see Section 7).
5. **Stage 4 · First-frame images**〔pause〕: For each shot, use `generate_image_v3` to generate a start_frame, which must match the shot description's framing/lighting/subject pose and serves as the visual anchor (see Sections 7, 8).
6. **Stage 5 · Shot videos**〔pause〕: Referring to the step 4 first-frame images, feed the start_frame as the first-frame input to `generate_video_v3` to generate subtle-motion videos (see Sections 8, 9).
7. **Stage 6 · Audio layers**〔pause〕: Use `generate_audio` to generate narration (if any) / BGM (see Sections 6, 7).
8. **Stage 7 · Assembly and delivery**: Use `composite_video` to complete the full-film timeline assembly (see Section 10).

**Dependency order**: Stage 2→0; 3→2; 4→2; 5→4; 6→2; 7→5,6.
**Pause points**: Pause after storyboard completion, after element images/first-frame images are complete, after videos are complete, and after audio generation; wait for user confirmation before continuing.
**Existing materials first** (mainly affects Stages 3–5): Before filling in generated content, first bind and assign it to suitable storyboard positions; do not regenerate content the user has already provided.

## 2. Final_Video_Spec Creation Guide

1. **Film title**: Should match the tone of a "humanistic documentary"; avoid overly commercial or flashy naming.
2. **Subject region**
   - **Region scope**: Guide the user to choose from the following regions — Asia, Africa, the Middle East, South America, Eastern Europe, Southeast Asia, island nations, developing countries.
   - **Core subject constraint**: The subject must focus on "**real people**" and "**ordinary people's lives**"; **reject "city promotional films"**.
3. **Aspect ratio**: Recommend 16:9 landscape, or the documentary-standard 2.35:1 widescreen.
4. **Visual style (four-reference lock + pitfall list)**: Lock to "like a real photographer on a long-term on-site assignment," "like an Oscar/international film festival documentary," "Netflix documentary style," or "National Geographic-style observational footage." **Explicitly "avoid" styles (pitfall list): strictly no AI feel, no commercial ad feel, no strong dramatic feel, no influencer style.**
5. **Visual texture requirements**
   - **Airiness**: dust, moisture, humidity, heat haze, wind.
   - **Lighting constraint**: natural light only (morning light, dusk, overcast, window light).
   - **Preserve imperfections**: allow and deliberately retain slight out-of-focus, exposure fluctuations, and a sense of authentic messiness.

## 3. Reference Material Analysis Rules

If the user uploads reference images or videos, extract the following signals for downstream use; **output structured descriptions without subjective judgment**:
- Subject identity and physical appearance;
- Scene location and environmental atmosphere;
- Lighting conditions (direction / color temperature / quality);
- Frame color tone and saturation style.

## 4. Narrative Standards (storyboard core)

### 4.1 Core narrative philosophy: observe life, don't "shoot a story"
- **De-dramatization**: Abandon strong dramatic conflict and commercial-ad-style plot design. The focus is not on "telling a story with a full dramatic arc," but on presenting "real human life in the real world."
- **Sense of spontaneity**: Scenes and events should show no trace of "deliberate directorial arrangement"; they must convey the natural state of "something a photographer happened to observe during a long-term stay."
- **Unified global documentary aesthetic**: Like Netflix documentaries or National Geographic-style observational footage, create humanistic narratives that audiences worldwide can understand and empathize with, avoiding stereotyped single-region styles (pure influencer style, purely Euro-American style).

### 4.2 Narrative subject and entry point: film "people" first, not "the city"
- **Reject promotional-film logic**: Never make "city appearance" or "grand landscapes" the primary subject — this is not a city promotional film.
- **Focus on real humans**: The narrative always starts from "people," reflecting the culture and environment behind them through the real living conditions of ordinary people.

### 4.3 Plot details and action design (the most empathetic descriptive points)
When writing the script and scene descriptions, focus on depicting the following detailed actions rather than grand events:
- **Focus on hand labor**: cooking, sewing, laundry, writing, handcraft work.
- **Figures' backs and their states**: Favor "back views" as the main visual — more refined and more open to story imagination than directly showing the face.
- **Small everyday actions**: lighting a cigarette, sipping tea, zoning out, gazing out the window — use these purposeless "small actions" to build a sense of real time flowing.

## 5. Region-based Scene/Subject Planning Library

When planning scripts for different developing countries or regions, directly select from the following scenes and events that best embody the local native humanistic atmosphere:
- **Asian subjects**: morning breakfast stalls, idle chatter in old teahouses, bustling traditional markets, unspoiled fishing villages, beside old railway tracks.
- **African subjects**: the journey home through dusk dust, lively marketplaces, children running, daily life in the rainy season, traditional handcraft labor.
- **South American subjects**: spontaneous street music performances, old town quarters full of everyday life, daily life by the sea, street/dirt-road football pitches, the warm everyday bustle of night markets.
- **Middle Eastern subjects**: sunlight cutting through a traditional market, focused handicraft-making processes, devout moments of prayer, everyday life amid dust and sand.

## 6. Key Elements and Audio Layer Design

### 6.1 Key element design
- Prioritize designing **character elements** (age, appearance, attire, what they are doing) and **scene elements** (geographic setting, time of day, lighting conditions, air texture).
- Prop elements are established as standalone entries only when they have a substantial impact on consistency across multiple shots.
- When the user provides reference materials, element descriptions must match the reference content and must not contradict it.

### 6.2 Audio Layer Design
- **BGM (optional)**: If used, choose minimal instrumental music or atonal ambient soundscapes; **pop music rhythms are prohibited**.
- **The narrative must not be driven by dialogue.**

## VII. Storyboard Shot Design Principles (★ Core of Observational Documentary Craftsmanship)

- **Duration**: Each shot is **6–12 seconds**; **no shots shorter than 5 seconds**.
- **Observational narrative**: Shots do not "design stories" but rather "catch glimpses of life by chance". Prioritize filming hand labor, figures seen from behind, and subtle everyday actions (lighting a cigarette, drinking tea, spacing out, looking out the window); avoid frontal, performative compositions.
- **Minimal camera movement (ordered by priority)**: Each storyboard entry describes only one shot.
  1. Fixed shot (most recommended)
  2. Slight handheld (breathing feel only / slight drift)
  3. Extremely slow push-in or extremely slow pan
  - **Prohibited**: rotation, fast push/pull, drone flying, flashy camera moves, cutting between shots.
- **Each shot description must include**:
  - **Scene**: Cite the scene element IDs, specifying the time of day and lighting;
  - **Subject action**: The subtle action the person is performing, centered on body movement and expression, **no dialogue needed**;
  - **Camera language**: Shot size (close-up / medium shot / long shot) + camera movement type + focus strategy.
- **Visual texture**:
  - **Natural light first**: morning light, dusk, overcast diffused light, soft side light from windows; any sense of artificial fill lighting is prohibited.
  - **Atmospheric feel is mandatory**: choose one from dust, vapor, heat haze, dampness, or light mist and write it into the shot description.
  - **Imperfection is allowed**: slight out-of-focus, minor exposure fluctuation, and brief pauses by the subject all count as plus points for realism.
- **Color tone system**:
  - Low saturation with layered depth: soft highlights without overexposure, detailed shadows without crushed blacks, realistic skin tones.
  - Reference color styles: **Kodak Vision3 / Fuji Eterna / ARRI Alexa Natural**.
- **Sound design in the video**: market noise, wind, rain, street sounds, etc.

## VIII. First-Frame Prompt Writing Standards (`generate_image_v3`)

**Core logic**: Focus on capturing the "decisive moment", film color texture, and authentic light, shadow, and atmosphere. **Abandon any camera-movement or pacing vocabulary.**

**Universal formula**:
> [Main subject and subtle action] + [Environment and atmospheric feel] + [Lighting condition] + [Camera language and shot size] + [Color system and film texture] + [Core spirit keywords and master references]

**Core modules and vocabulary bank**:
- **Subject and micro-actions**: a figure seen from behind / hands smoking a cigarette / gazing out the window / a paused moment of spacing out.
- **Environment and atmospheric feel**: diffuse dust (dusty air), morning mist, dampness, wind stirring the hem of clothes (wind blowing).
- **Lighting condition**: natural light, soft side light from a window (soft window light), overcast diffused light.
- **Camera language**: Medium shot / Close-up / minimalist composition / negative space.
- **Color system (use as-is)**: Kodak Vision3, Fuji Eterna, ARRI Alexa Natural, low saturation, soft highlights, detailed shadows, real skin tone.
- **Style and master references**: Magnum Photos, Leica Documentary, National Geographic, Hirokazu Kore-eda, Jia Zhangke.

**Example (method-level template; reusable by replacing the subject/region)**:
> (EN) A medium shot of an old man's weathered hands rolling a cigarette, sitting in a dimly lit traditional tea house. Morning mist and dust particles floating in the soft window light. Kodak Vision3 film stock, low saturation, soft highlights, real skin tone. Magnum Photos style, Leica Documentary, observational, honest, real, quiet, timeless. Hirokazu Kore-eda aesthetic.
> (ZH) Medium shot: the weathered hands of an old man rolling a cigarette in a dimly lit old tea house. Morning mist and dust particles floating in the soft window light. Kodak Vision3 film texture, low saturation, soft highlights, real skin tone. Magnum Photos style, Leica Documentary, observational, honest, real, quiet, timeless. Hirokazu Kore-eda aesthetic.

**First-frame image and visual anchors**: The first-frame image must match the shot size, lighting, and subject posture described in the storyboard shot, serving as the visual anchor for video generation. If the user has uploaded reference images (characters/scenes), register them as anchors (`reference_nodes`) and bind them to the corresponding element or shot slots, prioritizing them for replacement generation (the ImageToImage path).

## IX. Video Prompt Writing Standards (`generate_video_v3`, first-frame-driven)

**Core logic**: Focus on "the flow of time", "extremely slow pacing and camera movement", "subtle changes in the environment", and "the observational feel of a long take". Use the start_frame of the corresponding shot as the first-frame input.

**Universal formula**:
> [Extremely restrained camera movement] + [Continuous subtle action of the subject] + [Subtle passage/change in environment and light] + [Color system] + [Documentary pacing and cinematic references] + [Core spirit keywords]

**Core modules and vocabulary bank**:
- **Camera movement (must be restrained)**: Fixed camera / Slight handheld breathing / Extremely slow push-in / Extremely slow pan.
- **Action and environmental passage**: continuous subtle movement / light shifting slowly over time / continuous gentle breeze.
- **Pacing and editing instructions**: Long take / Slow pacing / No fast cuts / Breathing space.
- **Color system**: Sony Venice Documentary LUT, ARRI Alexa Natural, cinematic color grading, cinematic shadows.
- **Video style and references**: Netflix Documentary (Chef's Table, Our Planet), Oscar Documentary (Nomadland, Honeyland), Hou Hsiao-hsien pacing.

**Example (method-level template)**:
> (EN) Fixed camera with slight handheld breathing. A slow long take of a South American woman washing clothes by the river. Her back is to the camera. The damp morning air slowly blows her hair. Natural overcast light with subtle environmental shifts. ARRI Alexa Natural, Sony Venice Documentary LUT, low saturation, soft highlights. Cinematic pacing, breathing space, no fast cuts. Nomadland and Honeyland style, Netflix documentary vibe, observational, slow, human, quiet, timeless.
> (ZH) Fixed camera with subtle handheld breathing. A slow long take: a South American woman washing clothes by the river, her back to the camera. The damp morning breeze gently stirs her hair. Natural overcast light with subtle environmental shifts. ARRI Alexa Natural, Sony Venice Documentary LUT, low saturation, soft highlights. Cinematic pacing, breathing space, no fast cuts. Nomadland and Honeyland style, Netflix documentary vibe, observational, slow, human, quiet, timeless.

## 10. Asset Generation and Failure Handling

- **Element images / first-frame images**: `generate_image_v3`, 2K; first-frame images serve as visual anchors (see Section 8). If the user has uploaded reference images → register `reference_nodes` bindings, prioritized in place of generation.
- **Shot videos**: `generate_video_v3`, starting at 720p, using the corresponding shot's start_frame as the first-frame input (FirstFrameToVideo intent).
- **Audio layers**: Narration (if any) `generate_audio`; BGM `generate_audio`, with style described as minimalist instrumental / ambient soundscape, **do not generate lyrical music**.
- **Failure handling**: If video generation fails, **retry first with the same parameters on the same path**; do not switch on your own to an alternative path with a large stylistic difference. If the retry still fails, **stop and inform the user**; do not silently degrade by switching models.

## 11. Editing and Output (`composite_video`)

**Pacing principles**:
- **Prioritize long takes**, preserving the complete sense of temporal flow; **never shorten shots for the sake of being "interesting"**.
- Between shots, you may use **0.5–1s black frames or sound-continuity transitions** to create a sense of breathing room.
- **No fast cuts, music beat-syncing, VFX transitions, or TikTok pacing.**

**Audio-visual relationship**:
- BGM (if any) volume **lower than the video layer's sound**; fade in/out, never overpowering the visuals.
- **No forced audio-visual sync**; visuals and sound each flow naturally on their own.

## Related

- **Boundaries (do not use this skill; reroute instead)**: Strong dramatic narrative / short films with clear story arcs → cinematic-flow; urban memory / old neighborhoods with specific people and spaces (80/20 plain narration + high dynamic ratio) → city-memory-film; East Asian art films (emotion-driven / plain narration with subtle motion throughout / audio-visual separation) → east-asian-mood-film; traditional craft documentation (literature analysis → six-panel storyboard matrix → 15s per group) → craft-documentary; master-director documentary style (Jia Zhangke-esque) → auteur-style-director routing.
- This skill is self-contained and inline, with **no native cross-skill dependencies and no coordination table**.