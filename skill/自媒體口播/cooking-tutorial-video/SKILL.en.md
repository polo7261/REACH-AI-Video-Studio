---
name: cooking-tutorial-video
description: "Character cooking short: turn a single photo into a cinematic cooking tutorial in seconds"
---

# cooking-tutorial-video

Use this skill when turning a single photo of a person into a polished, cinematic cooking-tutorial short video (default 15s). Core mechanism: first synthesize a **production reference card** (character look + kitchen environment + a 9-panel cooking action board), then use **dual-image reference** to render a continuous, single-take cooking process, with the person's face / outfit / kitchen locked throughout. Unlike food-cinematic (A-Bite-of-China-style aesthetic food b-roll, no real person cooking): this skill is a **real-person, step-by-step tutorial video**.

> Environment adaptation: the reference card and final video run on Seedance → `generate_image_v3` (production reference card) + `generate_video_v3` (dual-image reference, continuity to video, generated audio); source is MIT, wording has been rewritten.

## Inputs

- **Person photo** (required): the identity reference; **the same photo is used for both the reference card and the final video** — it is the anchor that locks the face across the whole video.
- **Dish** (optional, default handmade pasta): sushi / wood-fired pizza / matcha latte, etc.; drives the concrete steps of the 9-step action board.
- **Kitchen style** (optional, default warm modern Italian rustic): minimalist Tokyo / bright Scandinavian / dark industrial, etc.
- **Outfit** (optional, default a clean casual look with apron): worn consistently throughout the video.
- **Duration** (optional, default 15s): 15s covers the full 9-step action arc; at ≤8s, compress the action board to 5–6 panels (see the short-take rule).
- **Aspect ratio** (optional, default 16:9): use 9:16 for vertical Reels.
- **Resolution** (optional, default 720p): 480p / 720p.

Anything missing falls back to defaults, but **the cooking process itself must break down into an ordered sequence of 9 steps** — if the dish is too simple to fill 9 steps, cut the panel count rather than padding it.

## Workflow

Submit a two-step sequential plan; step 2 depends on step 1's output.

### Step 1 — Production reference card (synthesized storyboard)

Use `generate_image_v3` with the person's photo as the reference to generate **one** high-end production reference board (not a poster, not crammed with text; a clean, whitespace-rich, gridded production reference with a photoreal cinematic feel). This image must carry three blocks at once:

- **Action/choreography board**: 9 numbered cinematic action panels that break the dish down, in order, into a 9-step cooking process from raw ingredients to plating.
- **Character reference card**: 100% preserve the uploader's face / hair color / hair texture / eye color / skin tone and all facial features; provide four views — facial close-up, full-body front, side/working pose, and back; dressed in the specified outfit; a grounded, approachable, professional, cinematic presence.
- **Environment reference card**: scene images of the kitchen in that style, with tactile materials, natural light through large windows, hanging cookware and herbs, and a premium cooking atmosphere that suits the cuisine.
- Overall style: photorealistic, cinematic, warm natural light, shallow depth of field, tactile food photography, premium cooking-show aesthetic, rich surface materials. At the bottom, place only minimal icons (duration / aspect ratio / photoreal / cinematic / natural camera movement), not dense text blocks — let the visuals carry the information.

**The reference card must be large (e.g., the 3840×2160 tier)**: at low resolution the 9 action panels go blurry and the video model can't read the choreography.

Once you have the reference card, **⏸ show it to the user and confirm the likeness + kitchen vibe before moving to step 2** — step 2 is the expensive one.

### Step 2 — Cooking final video (dual-image reference to video)

Use `generate_video_v3`, **feeding it both reference images at once**: the original person photo (identity anchor) + the step-1 reference card (choreography + environment guide), to generate a single-take, continuous cooking video.

- **Identity**: the person photo is the subject; 100% preserve their face / hair / eye color / skin tone and facial features in every frame.
- **Choreography**: strictly follow the reference card's 9 steps, beat by beat, from raw ingredients through prep to the final plating close-up; structure is driven by the reference card.
- **Motion style**: slow, unhurried, satisfying transitions between each step; natural hand and body movement with clearly readable cooking intent; continuous flow, no jump cuts; a warm, immersive rhythm.
- **Camera**: hand close-ups for stirring / kneading / chopping / plating; medium shots as the person works at the counter; pull back slightly on the final plating to reveal the whole kitchen; shallow depth of field focused on hands and food with the background softened; no hard cuts — smooth match cuts and fluid transitions.
- **Look**: warm natural light through large windows; material textures consistent with the reference card's environment; rich color, warm cinematic grade.
- **Consistency**: one person across the whole video (face = person photo), one outfit, one kitchen environment (= reference card).
- **Audio** (audio generation on): soft kitchen ambience + light cooking SFX (chopping, sizzling, pouring) + a light cinematic underscore; **no dialogue, no narration**. You must spell out the audio direction in the prompt, otherwise the soundtrack is random.
- **Ending**: run strictly to the specified duration and close on a beautiful close-up of the finished dish; an overall premium cooking-show feel.

After the video is done, give the user the playback link and proactively offer follow-ups: a vertical 9:16 re-render (Reels), an extended 30s version, or a rerun with the same person photo but a different dish.

## Key points

- **Dual-image reference is the whole trick**: the person photo locks identity; the reference card locks choreography + environment. Both are indispensable — run with just one image and you'll lose either the face or the kitchen. Always feed both into step 2.
- **Reference card large enough**: the 9 action panels must be crisp; if they blur, the video model can't read the steps (see resolution in Step 1).
- **Audio direction must be written**: once audio generation is on, no direction means a random soundtrack; always write "ambience + cooking SFX + light underscore, no dialogue".
- **Real human faces supported**: because the person photo is the user's own subject, and this goes through the dual-image-reference-to-video path (not the restricted image-to-video-only variant), photorealistic faces are supported here.
- **Non-cooking isomorphic variants**: latte art / plating tutorials / cocktail making, etc. reuse the same two-step structure — just swap the dish and the 9-step description.
- **Short-take rule**: for videos ≤8s, trim the action board to 5–6 panels; cramming 9 beats into 8s will wreck motion quality.

## Pairings (queries load both together / also this skill's evaluation combos)

No source-level cross-skill dependencies; self-contained (scene-specific craft is inlined in full). Only boundary redirects are listed:

Boundaries (don't use this skill; reroute): A-Bite-of-China-style aesthetic food b-roll (no real person cooking) → food-cinematic; craft cooking animations like needle felting / stop-motion → needle-felt-animation; real person talking to camera explaining → talking-head-director.