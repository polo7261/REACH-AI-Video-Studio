---
name: storyboard-scene-creator
description: "Ad TVC production skill: full pipeline from script → storyboard → final video."
---

# Full-Pipeline TVC Producer

Takes the topic, materials, or reference images provided by the user from **creative script** all the way to a **finished video**. Full-pipeline coverage: creative script → assets (character three-view sheets + prop design sheets) → storyboard → per-shot videos → final composite. Defaults to **16:9, 4K**; the storyboard supports three-panel/multi-panel layouts and retains the six-color arrow legend at the bottom.

## When to Use / When Not to Use

- **Use**: The user wants to produce a TVC / commercial film and needs to go from creative script to finished video; or only wants one segment of the process (e.g., just the storyboard).
- **Don't use**: Pure static illustration (no storyboard panels, no annotations), or casual videos without a script.
- **Video intent**: When signals such as TVC, duration (e.g., 30 seconds), or video are detected, **proactively inform the user that this Skill can go from a static storyboard all the way to a finished video**, and confirm the target duration, aspect ratio, and resolution.

## Inputs

Supports three starting points; choose based on what the user actually provides:

- **With image**: The user provides a storyboard/reference image → analyze its visual content and layout, then adapt and re-layout it to the target ratio.
- **Without image**: The user provides a topic or written script → the AI generates the creative script and storyboard. **Must first pass the "Phase 1 · Creative Script Confirmation Gate."**
- **Scattered materials**: The user provides multiple images + a piece of copy → integrate them into a coherent storyboard.

## Three DIY-able Elements (Slots)

The following three items are **decided by the user**; each one supports three modes: "user specifies directly / user provides materials / let the AI generate." Do not hard-code them to the specific values from the reference image:

Element Reference-image value (example only) Replaceable with Scenario Ancient Chinese imperial palace pantry Modern restaurant, home-style kitchen, Western, Japanese, or any other style Product Eight-Treasure Duck, Crab-Roe Lion's Head, Jade Shrimp, Osmanthus Cake, Candied Plums Any dish or non-dish product Character Ancient-costume woman Shen Fuyao Any look / gender / era / appearance Style Hand-drawn sketch / line-art style Modern realistic photography style or any other style

**Confirm these three elements before generating**: If the user has not explicitly specified them, ask via `ask_parent_agent`, or make a reasonable inference from the topic the user has given and ask them to confirm; do not default to the ancient-style pantry setting from the reference image.

---

## ⚠️ Core Principle: The Number of Storyboard Shots Must Match the Number of Video Segments One-to-One

**The number of shots determined in Phase 3 (e.g., 30 seconds split into 15 shots) = the number of video segments that must be generated shot by shot in Phase 4 (15 segments).**

- **Do not merge them back into 3 large shots on your own during the video stage** (e.g., merging 15 shots into 3 segments of 10 seconds each) — this would decouple the storyboard from video production and is an error that must be avoided.
- **Each video segment strictly corresponds to one storyboard shot**: duration, shot size, focal length, camera movement, lighting, mood, props, facial expressions, and actions all follow that shot's storyboard.
- **Handling minimum-per-segment duration conflicts**: If the video model's minimum per-segment duration exceeds a shot's duration (e.g., some models have a 5-second minimum), **you must check with the user at the storyboard confirmation stage** — either choose a model that supports shorter durations, or regroup the shots according to the model's limitations and clearly inform the user; **do not silently drop storyboard shots**.

### Duration Allocation for the 15 Shots (from this test run, 30 seconds total)

Shot 123456789101112131415 Duration (s) 222221.51.51.522222.52.53

---

## Standard Execution Steps (Full Pipeline)

### Phase 0 · Requirements and Scope

1. Receive the topic / materials.
2. When signals such as TVC, duration (e.g., 30 seconds), or video are detected, proactively explain that this Skill can go from a static storyboard all the way to a finished video.
3. Confirm the target **duration, aspect ratio, and resolution**.

### Phase 1 · Creative Script Confirmation Gate

1. In the no-image branch, the AI first writes a creative script containing: **creative core, storyboard shots, duration allocation, dialogue / voiceover**.
2. **Any image generation requires prior user confirmation; do not generate images directly.**
3. When the user requests changes, revise the script first, then re-confirm.

### Phase 2 · Assets First (Anchors)

Before producing the storyboard, first generate:

1. **Character three-view sheet**: full-body front / side / back views, including complete body proportions and fashionable outfit styling.
2. **Prop design sheet**: the products and props used in this film, from multiple angles.

These two serve as the **unified anchors** for the subsequent storyboard and videos.

### Phase 3 · Storyboard

1. **Subdivide shots by duration**: 30 seconds can be split into **13–15 shots, averaging about 2 seconds per shot** (15 shots in this test run).
2. **At least one full-body shot**.
3. **Annotate every shot**: shot number/time, shot size, lens focal length, camera movement, lighting, mood, props, and facial expression.
4. **Layout**: supports a standalone single-shot storyboard, or 3 1:1 shot panels per image assembled into a 16:9 overview sheet; retain the **six-color arrow legend** at the bottom (red = subject action, blue = camera movement, green = framing/composition, orange = lighting, purple = sound/emotion, black = shot notes and tags).
5. The storyboard **must reference the character three-view sheet and prop sheet** to ensure character consistency and product consistency across shots.
6. **Confirm the number of shots and each shot's duration**, and verify compatibility with the video model's minimum duration limit (see "Core Principle").

### Phase 4 · Video Generation (Per-Shot Production)

1. **Create and generate 15 video segments shot by shot according to the 15 shots**, each referencing the corresponding character three-view sheet `{{i-vmkk42rkfd7d}}` and prop sheet `{{i-hjbz7a7j8g3p}}` to ensure character and product consistency.
2. Each segment's prompt includes: **that shot's scene / action / shot size / focal length / camera movement / lighting / mood** + **realistic skin texture** (natural pores, skin-tone gradations, restrained highlights; strictly no plastic look / waxwork look / over-smoothed AI fake faces).
3. **Specs**: 16:9, 4K.
4. **Model selection**: With multiple reference images (character + props), use **Seedance 2.0**, which supports multiple references; **Kling 3.0** only supports text-to-video / single-image-to-video / first-and-last frames, and **does not support multi-image references**.
5. **Create in batches, approve and run in batches.**

### Phase 5 · Final Composite (Joining the 15 Segments)

1. **Join the 15 video segments in Shot 1 → Shot 15 order into a single 30-second finished film**, not 3 segments.
2. The composite **does not call generation models and incurs no charges**; resolution is **2160p, i.e., 4K**.
3. Optionally overlay BGM, sound effects, voiceover, subtitles, and brand logo / slogan cards.

---

## Hard Rules (Anchors, Immutable)

1. **Number of shots = number of video segments**: the number of shots in Phase 3 must equal the number of video segments generated in Phase 4; no merging.
2. **Three-panel/multi-panel layout is fixed**: the storyboard keeps its three-panel/multi-panel layout; the panel-count structure does not change with input or aspect ratio.
3. **Bottom color arrow legend is always retained**: red = subject action, blue = camera movement, green = framing/composition, orange = lighting, purple = sound/emotion, black = shot notes and tags.
4. **Character consistency across shots**: the same character's look, gender, era, and appearance must be consistent across all shots.
5. **At least one full-body shot**: the storyboard must include at least one full-body shot showing the complete figure and outfit.
6. **Asset consistency**: the storyboard and videos must reference the character three-view sheet and prop sheet to ensure character and product consistency across shots.
7. **In the no-image branch, no images may be generated before the script is confirmed.**

## Compliance Rules

When characters involve sexiness / body emphasis, **compliant phrasing must be used**: describe them with wording such as high fashion, stylish outfits, and ambiance, to avoid triggering safety review.

- The outfit direction follows the fashion style specified by the user, not default choices like a black suit that don't match the creative concept.
- **If generation is rejected by the safety review, rebuild with compliant wording** (tested: the first two versions of a character three-view sheet were rejected due to spaghetti straps + body emphasis; after changing to fashion-outfit / modest phrasing, they passed). Do not give up or bypass the review.

## Optional Parameters

- **Aspect ratio**: default 1:1 (storyboard); optional 16:9 / 9:16; finished videos default to 16:9.
- **Resolution**: video defaults to 4K (2160p).
- **Chinese annotations**: provide Chinese annotations based on the visuals — shot, lighting, action, emotion, camera movement, framing/composition notes, etc. **Whether annotations are kept is the user's choice**.

## Notes

- The three DIY elements are slots, not anchors; layout, legend, character consistency, full-body shots, asset consistency, and storyboard panel count = video segment count are anchors, not slots — do not confuse them.
- If the user has not specified the three elements, ask before generating; do not silently reuse the reference image settings.
- No-image branch: **do not generate any images before the user confirms the script**.
- Whenever sexiness / body emphasis is involved, always use compliant expressions such as high fashion, fashion styling, or atmospheric mood.
- At the video stage, always include requirements for realistic skin texture to avoid AI fake faces.
- For multi-reference-image scenarios, do not use Kling 3.0 (it does not support multi-image references); use Seedance 2.0 instead.
- **At the video stage, strictly avoid merging multiple storyboard panels into a single large shot**; when a single segment's duration is limited by the model, check with the user before grouping — never drop storyboard panels by default.