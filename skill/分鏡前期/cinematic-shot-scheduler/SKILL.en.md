---
name: cinematic-shot-scheduler
description: "Automated cinematic shot scheduling: AIGC professional shot-blocking storyboard video workflow for story segments"
---

# Cinematic Storyboard-to-Video Generation Formula

## Skill Positioning

This skill is responsible for one reusable thing only: transforming a film reference image or a film scene idea into an executable cinematic storyboard, then using the storyboard and the original image to generate a video, automatically orchestrating shot execution.

Core goals:

- Reduce the time users spend creating storyboard images.
- Automatically expand a single frame into 12 cinematic shots.
- Let the storyboard be responsible for "shot design, motion direction, emotion, composition, and shot choreography".
- Let the original image be responsible for "characters, scene, lighting, texture, and visual style".
- Use seedance 2.0 fast or seedance 2.0 to generate videos whose style matches the original image and whose shot choreography is clearer.

## Model Restrictions

This skill may only use the following models:

```json
{
  "image_model": "Lib image",
  "video_models": ["seedance 2.0 fast", "seedance 2.0"]
}
```

Model selection rules:

- Image generation, storyboard, and reference-image completion: use only `Lib image`.
- Video generation: prefer `seedance 2.0 fast`; if unavailable, fall back to `seedance 2.0`.
- Do not use any other image models.
- Do not use any other video models.
- If a specified model is unavailable, stop and inform the user; do not automatically switch to another model.

## Input

The user may provide any one of the following inputs:

- A reference image: serves as the anchor for characters, scene, style, and lighting.
- A text scene description: e.g., "In a rainy-night alley, a detective chases a man in black."
- A reference image + text: the best input combination.
- A story fragment, ad concept, MV scene, short-drama beat, or cinematic mood keywords.

Optional supplementary information:

- Genre: drama, suspense, action, romance, comedy, horror, commercial, MV, documentary feel, etc.
- Mood: tense, romantic, lonely, epic, absurd, warm, oppressive, psychedelic, etc.
- Video duration: default 8-12 seconds; can also be generated at 5, 10, or 15 seconds.
- Aspect ratio: default 16:9.
- Shot intensity: realistic, cinematic, handheld, action-driven, dreamlike, stage-like, etc.

## Input Usage

Strictly follow:

- The protagonist, main scene, period feel, costume, lighting, and visual style from the reference image.
- The shot order, shot-size changes, character movement, camera movement, and compositional intent from the storyboard.
- Story events, actions, and emotions explicitly specified by the user.

Use as reference:

- Story background not explicitly specified by the user.
- Character relationships not visible in the reference image.
- Dialogue, music, sound effects, and editing rhythm that were not provided.

Do not fabricate:

- IPs, brands, real people, movie titles, or copyrighted characters not provided by the user.
- Key character identities that do not exist in the reference image.
- New worldviews that conflict with the original image's style.

## Internal Workflow and Knowhow

### 1. scene_intake

First determine which case the user's input falls into:

```json
{
  "has_reference_image": true,
  "has_text_scene": true,
  "needs_base_image": false,
  "target_video_duration": "8-12s",
  "aspect_ratio": "16:9"
}
```

If the user provides only text and no image:

1. First use `Lib image` to generate an original film scene image.
2. Use this image as the subsequent `Mixed 1` original image reference.
3. Then proceed to storyboard generation.

If the user has already uploaded an image:

1. Use the uploaded image directly as `Mixed 1`.
2. Do not redesign the characters or scene.
3. Only supplement shot events and emotion based on the user's text.

### 2. base_image_prompt

Used only when the user has not uploaded a reference image. Use `Lib image` to generate an original film scene image.

Output an image-generation prompt for a film scene suitable for Lib image. It must include:

- The main character or main event.
- The scene space.
- Emotion and dramatic conflict.
- Lighting direction.
- Cinematic shot feel.
- Film texture.
- 16:9 aspect ratio.

Avoid generating a complex plot in one pass; generate only a single keyframe that can serve as a visual anchor.

### 3. storyboard_prompt_builder

Based on the `Mixed 1` original image and the user's scene, rewrite a storyboard image-generation prompt for use with `Lib image`.

The fixed system prompt must be preserved:

```text
Create a storyboard panel, focusing on emotional expression and shot-size planning. Use the reference image as the character.

A 16:9 storyboard sheet with 12 cinematic-style panels. The actual storyboard drawings must be black and white only: rough pencil lines, minimal detail, quick gestural drawing energy, simple anatomical construction, and strong silhouette readability. Keep the artwork light, dynamic, and unfinished, like an early choreography preview.

Use cinematic art-style photographic techniques with handheld energy, fast pans, arcing movement, overhead shots, side profiles, aggressive close-ups, telephoto compression, and extreme negative space.

Annotation color system:
Red arrows = body movement
Blue arrows = camera movement
Green marks = framing / composition notes
Orange marks = lighting direction
Purple marks = sound / emotional emphasis
Black text = brief shot notes and panel labels

No timestamps.
```

Storyboard image-generation prompt template:

```text
A 12-panel black-and-white storyboard generated from the prompt in the text node. Now, based on the prompt structure in the text node, rewrite an image-generation prompt whose main content is creating a film scene.

Use @图片1 as the reference image, keeping the characters, scene, period feel, costume, lighting, and visual style consistent.

Story event: {user scene or auto-completed film event}
Core emotion: {emotion}
Shot choreography goal: use 12 cinematic-style panels to convey character action, camera movement, emotional progression, compositional changes, and lighting direction.

Output requirements:
A 16:9 storyboard sheet with 12 cinematic-style panels. The actual storyboard drawings are black-and-white rough pencil lines only, with minimal detail, quick gestural drawing energy, simple anatomical construction, and strong silhouette readability. Keep the light, dynamic, unfinished feel of an early choreography preview.

Photographic techniques:
Handheld energy, fast pans, arcing movement, overhead shots, side profiles, aggressive close-ups, telephoto compression, extreme negative space.

Annotation color system:
Red arrows = body movement
Blue arrows = camera movement
Green marks = framing / composition notes
Orange marks = lighting direction
Purple marks = sound / emotional emphasis
Black text = brief shot notes and panel labels

No timestamps.
```

### 4. storyboard_generation

Use `Lib image` to generate the `Mixed 2` storyboard.

The storyboard must meet the following requirements:

- 16:9.
- 12-panel grid.
- Black-and-white pencil lines as the main body.
- Specified colors allowed only for annotation arrows and text.
- A clear shot size or camera intent in every panel.
- No full-color final-footage imagery.
- No timestamps.
- Not drawn as a detailed comic, poster, or final-film screenshot.

### 5. storyboard_interpreter

Read the generated storyboard and organize the 12 panels into a shot plan.

Output structure:

```json
{
  "panel_id": 1,
  "shot_size": "wide / medium / close-up / extreme close-up / overhead",
  "character_action": "",
  "camera_motion": "",
  "composition_note": "",
  "lighting_note": "",
  "emotion_or_sound_note": "",
  "video_use": "primary / optional"
}
```

If the user only needs one short video, there is no need to generate all 12 clips panel by panel. Choose the 3-6 core panels with the strongest continuity and use them to guide seedance in generating one complete video.

### 6. seedance_video_prompt_builder

Generate the seedance video prompt based on the `Mixed 1` original image and the `Mixed 2` storyboard.

The base prompt must be preserved:

```text
Reference the storyboard in {{Mixed 2}} and the imagery in {{Mixed 1}} to generate a video with the same visual style.
```

Recommended extended template:

```text
Reference the storyboard in {{Mixed 2}} and the imagery in {{Mixed 1}} to generate a video with the same visual style.

Maintain the characters, costumes, scene, period feel, lighting, color, lens texture, and overall art style from {{Mixed 1}}.
Use the 12-panel storyboard from {{Mixed 2}} as the shot choreography reference: follow the character movement directions, camera movement, shot-size changes, compositional focus, lighting direction, and emotional emphasis.

Video content:
{Summarize the story event in 1-3 sentences}

Shot language:
{Extract 3-6 key shots from the storyboard: opening, action progression, emotional close-up, spatial relationships, climax action, closing frame}

Motion requirements:
Natural cinematic camera movement; avoid sudden deformation, avoid character identity changes, avoid scene jumps. Motion should be continuous, lighting should be stable, and characters should match the original image.

Style requirements:
cinematic, live action, same visual style as reference image, coherent motion, dramatic composition, emotional performance, natural camera movement.
```

Negative constraints:

```text
do not change character identity, do not change costume, do not change location, no extra characters unless storyboard shows them, no distorted face, no deformed hands, no broken body, no flicker, no sudden style change, no cartoon style, no storyboard lines in final video, no timestamps, no subtitles, no text overlay
```

### 7. video_generation

Use the video models to generate the video:

1. Prefer `seedance 2.0 fast`.
2. If higher quality is needed or fast is unavailable, use `seedance 2.0`.
3. Inputs must include the `Mixed 1` original image and the `Mixed 2` storyboard.
4. Do not use any other video models.

If the generation results are unstable:

- Shorten the video duration.
- Reduce the number of shot events.
- Pick 3-4 key panels from the storyboard to generate a single video segment.
- Or split into multiple 3-5 second segments and then stitch them together.

## Prompt Guide

### Lib image Storyboard Prompt Evaluation Criteria

A good prompt should:

- Clearly state that this is a "storyboard," not a final frame.
- Clearly specify the 12-panel grid, 16:9, and black-and-white pencil lines.
- Clearly require preserving the characters and scene from the reference image.
- Clearly specify cinematic shot techniques.
- Clearly specify the color annotation system.
- Clearly state no timestamps.

A poor prompt typically:

- Only says "generate a storyboard image" with no shot choreography.
- Does not require a black-and-white pencil storyboard.
- Lets the artwork become overly detailed or turn into a comic.
- Does not explain the arrows and color annotations.
- Does not constrain character and scene consistency.

### seedance Prompt Evaluation Criteria

A good prompt should:

- Reference both the original image and the storyboard.
- Clearly assign visual style to the original image and shot choreography to the storyboard.
- Describe the video event in 1-3 sentences.
- Extract 3-6 core shots instead of forcing the model to execute all 12 panels.
- Explicitly prohibit character, costume, scene, and style drift.

A poor prompt typically:

- Only says "generate a video referencing the storyboard" without mentioning the original image.
- Asks for too many shots in one go.
- Does not constrain character consistency.
- Carries storyboard lines, arrows, and text into the final video.

## Output

After each execution, output:

```markdown
## Skill Execution Summary
- Input type:
- Models used:
- Original image source:
- Storyboard source:
- Video model:

## Film Scene Analysis
- Main character(s):
- Scene space:
- Core action:
- Core emotion:
- Visual style:

## Lib image Storyboard Prompt
Output the full storyboard image-generation prompt.

## 12-Panel Storyboard Shot Plan
Use a table to output panel_id, shot size, character action, camera movement, composition, lighting, and emotion/sound emphasis.

## seedance 2.0 Video Prompt
Output the full video prompt.

## Generation Recommendations
- Recommended duration:
- Whether to recommend seedance 2.0 fast or seedance 2.0:
- Whether split-into-segments generation is recommended:
- Questions requiring user confirmation:
```

## Self-Check

Before outputting, check:

- Whether only `Lib image`, `seedance 2.0 fast`, and `seedance 2.0` are used.
- Whether no other models are recommended or invoked.
- Whether the storyboard is explicitly 16:9, a 12-panel grid, with black-and-white pencil lines.
- Whether the storyboard keeps the color annotation system while the main drawings remain black and white.
- Whether there are no timestamps.
- Whether the seedance prompt references both the `Mixed 1` original image and the `Mixed 2` storyboard.
- Whether "the original image controls style" and "the storyboard controls shot choreography" are clearly distinguished.
- Whether storyboard lines, arrows, and text are kept out of the final video.
- Whether character, costume, scene, and period-feel drift are avoided.

## Ask User

Follow-up questions are needed only in the following cases:

- The user has uploaded neither an image nor provided any scene text.
- The user asks to generate a specific IP, a character from a real film or TV work, a celebrity, or a copyrighted character.
- The user wants a very long video but has not specified the plot structure.
- The requested video action is too complex, and splitting it into multiple segments must be confirmed.

Ask 1-3 of these questions first:

1. Do you want to use the uploaded image as the original image, or generate a new film scene image first?
2. What is the core emotion of this segment: tension, romance, action, suspense, warmth, epic, or something else?
3. How many seconds do you want the final video to be, and do you accept splitting it into multiple segments and stitching them together?