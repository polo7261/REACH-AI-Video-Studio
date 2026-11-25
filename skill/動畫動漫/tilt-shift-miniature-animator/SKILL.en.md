---
name: tilt-shift-miniature-animator
description: "Tilt-shift miniature healing animation: gentle emotional shorts staged in miniature model scenes, tilt-shift aesthetics, great for holiday greetings."
---

## name: miniature-world\\

namespace: industry\\
title: "Miniature World Tilt-Shift Emotional Short Film"\\
description: "Gentle emotional short films (holiday wishes/life stories) staged in miniature model scenes, with character arcs — tilt-shift photography aesthetics, 5-stage checkpoint pipeline, 4–6 segment narrative arc, miniature figure aesthetics, 4–8s per shot · restrained camerawork across 10–18 shots, iron rules of size consistency (large props handled by many hands / no proportion distortion / no glowing or floating), four-layer image prompt structure + four-block video timeline format, light piano-and-strings BGM. Defaults: 9:16, 60–90s."\\
version: 2

# miniature-world

Staged on miniature props and model scenes, telling gentle little stories with character arcs (holiday wishes/life stories). Refined and delicate art style, restrained camerawork, **tilt-shift photography aesthetics** — suited to emotional short films. Defaults: 9:16, 60–90s, warm and soft.

> Environment adaptation (Flova → our 13 tools): GPT Image 2/Nano Banana/Seedream/MJ → `generate_image_v3`; Seedance/Kling/MultiModalToVideo/FirstFrameToVideo → `generate_video_v3`; text_to_instrumental/text to narration → `generate_audio`; text_editor (Final_Video_Spec) → `write_file_v2`; video_assembler → `composite_video`. The "membership required" resolution/model tiers in the source = `no credit system`, no gates set. \*\***This skill is self-contained and inlined, depending on no other skill.** Long content (image/video prompt structures, multimodal analysis, assembly specs) lives in `references/` (internal files of this skill, not dependencies).

## 5-Stage Pipeline (5 Mandatory Checkpoints, Cannot Be Skipped)

- **Stage 0 Spec Confirmation**〔CP0〕: First present to the user and collect explicit choices —
  - **Aspect ratio** (single choice): 9:16 (vertical, recommended · suited to mobile) / 16:9 (horizontal) / 1:1 (square, social).
  - **Video resolution** (single choice): 720p (standard) / 1080p (HD).
  - **Target duration** (single choice): 60s (streamlined, ~10–12 shots) / 90s (standard, ~14–18 shots) / custom (user enters seconds).
  - **Image generation model / video generation model**: in this environment everything goes through `generate_image_v3` / `generate_video_v3` (the source's five-model menu → our model tiers; see references/pipeline-and-generation.md for the model tier notes).
  - After receiving the choices, use `write_file_v2` to create **Final_Video_Spec.md**, writing in: video type = miniature life-story film (emotional short film), aspect ratio \[chosen\], target duration \[chosen\], video resolution \[chosen\], image model (resolution 2K), video model + resolution \[chosen\], visual style = miniature model photography style · tilt-shift lens feel · refined and delicate · warm soft tones, audio style = light music BGM (piano/strings led) · gentle narration or no narration, output language = same as the user's interaction language.
  - **Mandatory CP0 pause**: present a summary of the confirmed parameters; do not proceed to Stage 1 before receiving explicit confirmation.
- **Stage 1 Story Script**〔CP1〕: guide the user to give a synopsis or have the AI auto-draft (characters/scenes/emotional arc); complete key element definitions (protagonist/supporting characters/main scenes/core props) + shot planning (shot size/camera movement/duration/narrative pacing, durations aligned with the Spec) + audio layer design (number of BGM tracks/narration rules). Present the full story script and shot plan (per-shot shot size/camera movement/narrative content summary) for confirmation.
- **Stage 2 Key Element Images**〔CP2〕: prioritize generating all character key element images (front-facing reference images + action/expression variants) using the model specified in the Spec; then generate scene key element images (miniature streetscapes/interior sets); if there is narration, also use `generate_audio` at this stage to generate the narration audio as the audio condition for later. **Present all element images together for confirmation**; if the user asks to regenerate any one, regenerate and then confirm again.
- **Stage 3 Shot Videos + BGM**〔CP3〕: generate all shot videos **in batch** following the shot order, **no pause-for-confirmation per batch needed**; every shot carries its corresponding character image + scene image as visual references, using the model specified in the Spec; BGM via `generate_audio` runs in parallel with the videos. Once everything is done, present the previews together for confirmation before assembly.
- **Stage 4 Rough Cut Preview**〔CP4〕: `composite_video` assembles all shot videos + narration + BGM into a rough-cut timeline, presented as a "rough cut preview" for the user to confirm overall pacing and mood; if changes are needed, return to the corresponding stage, adjust, then re-assemble.
- **Stage 5 Final Output**: after the user confirms satisfaction, `composite_video` for the final composition, then inform them of the export.

> **Stage dependencies**: CP0→CP1→CP2→CP3→CP4→Stage 5. **Narration audio (Stage 2) must finish before the videos (Stage 3)** to serve as the audio condition; **BGM and shot videos (Stage 3) may run in parallel**.

## Narrative: 4–6 Segment Arc

First break the story into **4–6 key segments** (no fewer than 4) to form the arc skeleton, then allocate shots accordingly.

- Number of segments: recommended 4 (streamlined themes) – 6 (plot-rich themes), no fewer than 4.
- Each segment corresponds to one **narrative function node**; common structure: **establish the world → triggering event → plot progression → emotional climax → lingering close**; or break down the flow for the specific theme (e.g., "holiday gift": search for materials → make the gift → wrap and wait → give the surprise → warm afterglow).
- Each segment must contain **core scene / participating characters / key action or prop / emotional tone**; segments must be **logically coherent and emotionally progressive**; causality-free jumps are forbidden.
- Internal planning format (not shown to the user): `Segment 1: [name]—[scene]—[core action]—[emotion]`… once the skeleton is confirmed sound, expand shots per segment, usually 2–4 shots per segment.

## Key Elements (Miniature Figure Aesthetics)

- **Characters**: each protagonist is an independent element — a front-facing full-body reference image (clearly showing styling/outfit/hairstyle/skin tone) + ≥1 expression/action variant image (showing emotional shifts); must fit the miniature figure aesthetics: slightly cartoonized proportions, delicate material feel (fabric texture/skin sheen), blending naturally into the model scenes.
- **Scenes**: each main scene is an independent element — a full-scene reference image (spatial structure/lighting atmosphere/prop placement) + optional day/night variants.
- **Props**: core props with narrative function (letter/bouquet/small table) each get their own element, ensuring cross-shot consistency.

## Shot List (shot_list) Specification

- **Duration pacing**: 4–8s per shot (up to 10s at emotional climaxes); whole film 60–90s, usually 10–18 shots.
- **Shot sizes and camera movement**: open with an extreme long shot/overhead panorama to build the miniature sense of space (strong tilt-shift feel); for narrative progression, medium shots dominate to show character interactions; for emotional close-ups, use facial close shots/prop close-ups to capture detailed emotion; restrained camera movement (mainly slow push-ins/pull-outs and slight pans), avoiding fast cutting that breaks the gentle atmosphere.
- **Narrative Structure**: Follow the four-part arc of "opening establishes the world → plot unfolds → emotional climax → lingering closing"; each shot description includes shot size/camera movement/frame content/character emotion/narrative connection with adjacent shots.

## Size Consistency & Action-Subject Iron Rules (Cross-Shot Mandatory · Miniature-Exclusive)

- **Large props require collective effort**: Any prop far larger than a single figure (coffee cup/envelope/flower pot) must explicitly show "multiple figures working together" to operate it; **a single figure easily using a large prop is forbidden** (otherwise disproportionately huge arms/figures may be generated).
- **Actions must map to specific subjects**: Every action must clearly state who performs it (which character, or "both together"); vague expressions such as "someone/a certain person" are forbidden.
- **No counterintuitive elements**: No glowing props, floating objects, insect riding, or other content that breaks miniature realism.
- **Cross-shot consistency**: The same character's outfit/hairstyle/prop state must stay consistent throughout; fixed props within a scene must not shift position without reason.

## Audio Layer Specifications

- **BGM**: 1–2 tracks (opening + climax, switchable); styles: solo piano / piano + strings, soft and warm, no vocals; duration must cover the entire film (recommended to generate 90s or more), with fade-in/fade-out; no well-known musicians' names in the `generate_audio` prompt.
- **Narration (optional)**: If used, the **shot_id** corresponding to each narration line must be annotated at the storyboarding stage; tone should be gentle narrative (third/first person both acceptable); voice selection: gentle female narration / warm male narration / neutral, clear female voice (chosen by mood, specified via `generate_audio`); narration must be completed as an audio condition before video generation.
- **Narration coexisting with shots carrying built-in audio**: Shots generated via FirstFrameToVideo/VideoInterp-type tools carry their own audio; the narration track for such shots must be **muted or staggered** to avoid overlap.

## Generation & Prompt Craft (fully inlined; see references/ for details)

- **Global visual style tone**, **four-layer image prompt structure** (subject size perception → miniature aesthetics CN/EN template → lighting/color-tone four-option library → atmospheric closing), character 16:9 stitched reference image spec, image negative terms → `references/prompt-image.md`.
- **Four-block video prompt** (global aesthetics → asset anchoring + size-comparison anchoring sentences → three-tier action timeline format → fixed + per-shot negatives), narration strictly forbidden in video prompts, {dialogue}/&lt;sound effect&gt; markers, CN/EN cinematography lexicon, narration copy style → `references/prompt-video.md`.
- **Video generation rules** (primary/fallback chain, 15s auto-segmentation and narrative-boundary cutting, mandatory reference binding, single-shot duration reference, model failure retry strategy), **multimodal asset analysis** (three extraction sets for images/videos/documents), **assembly specifications** (tracks/volume 40–60%/fade-in-fade-out/no speed change for lip-sync/MV-type native-audio muting) → `references/pipeline-and-generation.md`.

## Related

Boundaries (do not use this skill; redirect instead): real travel footage → travel-vlog; gourmet food close-ups → food-cinematic; wool-felt material → needle-felt-animation.