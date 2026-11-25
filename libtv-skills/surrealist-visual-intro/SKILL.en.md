---
name: surrealist-visual-intro
description: "Surrealist title sequence design: create surrealist visual intros in the style of Severance and Westworld."
---

## Global Fixed Parameters (Must Not Be Changed at Any Stage)

Parameter Values **Image generation model** Mandatory Midjourney V8.1; no other version or other image generation model may substitute it Visual style Locked for the entire run once selected in Stage 1 (choose one of three seeds, see §1.2) Storyboard image aspect ratio 16:9 (`--ar 16:9`) Video aspect ratio 21:9 (`--ar 21:9`, must be noted in the prompt) Video model Unrestricted; any first/last-frame video generation tool available to the user may be used, 720p or above Number of video segments N − 1 segments

---

## Workflow Overview

```
Step 1: Visual style/duration/aspect ratio/BGM style/whether to add the film title—confirm all at once         → User confirmation
Step 2: Present the script content                                               → User confirmation
Step 3: Chain-generate all storyboard images, one confirmation upon completion                           → User confirmation
Step 4: Present the video prompts, generate all videos in one go, auto-generate the BGM, then merge                → Automatic execution
Step 5: Merging complete, ask about the end credits (needed/not needed, one image/one image per person)          → User confirmation (optional)
```

**Stages with confirmation steps must wait for the user's response before continuing; stages without confirmation steps execute automatically.**

---

## Stage 1: Script Analysis and Theme Extraction

### 1.1 Read the Script or Story

The user may provide material in the following ways: uploading PDF / TXT, pasting script text, describing a story synopsis, or verbally describing the story theme. **Even just a story synopsis or character profiles are enough to begin the design**; a complete script is not required.

After reading, internally distill five dimensions (as the basis for subsequent design):

Dimension Extracted content **Core conflict** The protagonist's most fundamental inner conflict (one sentence) **Protagonist's state** The protagonist's core situation or psychological state, plus appearance/visual image description (costume, posture, signature features, and other visualizable details) **Signature space** The most visually charged location in the script—the core scene used internally by the agent to define the title sequence; the term "Matrix" is not used with the user **Core prop/totem** A key object carrying narrative meaning that will repeatedly appear or evolve across scenes **Emotional theme** The grand thematic keyword driving the entire work

### 1.2 Step One: Present the Theme Summary + Storyboard Plan, Then Confirm All Options at Once

**Execution order: complete the internal visual style matching and script planning first, then present to the user—first use a few paragraphs of natural language to clearly explain the theme and storyboard concept, then immediately use selection boxes to ask everything requiring the user's decision in one go.**

**Presentation format: short paragraphs, layered structure, no dense walls of text.**

- First paragraph: one or two sentences pinpointing the core tension
- Second paragraph: title sequence concept—the main throughline, how the camera roughly moves, the overall atmosphere, color tone, and texture
- Third paragraph: storyboard plan—how many storyboard frames and video segments are planned, the global camera-movement throughline, the trajectory of the early/middle/late sections, and the emotional arc
- Fourth paragraph (immediately after the above): selection boxes, asking all options at once **Selection boxes (presented using the ask_user_input_v0 tool; each question is a separate multiple-choice question):**

```
Question 1: Visual style
Options:
- Seed A · Workplace dystopia/Cold War espionage/Absurdist comedy
- Seed B · Eastern aesthetics/Xuanhuan fantasy/Mythology/Apocalyptic philosophy
- Seed C · Hard sci-fi/AI awakening/Heavy psychological suspense
- I'll specify
(The agent adds "(Recommended)" after the recommended option's text and states the reason for the recommendation in the question description; one sentence suffices)
 
Question 2: Title sequence duration
Options:
- 60 seconds (Recommended)
- 75–90 seconds
- Over 90 seconds
- I'll specify
 
Question 3: Aspect ratio
Options:
- 21:9 widescreen (Recommended)
- 16:9 standard
- Other
 
Question 4: BGM style (the agent fills in 2–3 concrete options based on the script's emotional tone)
Options:
- [Agent fills in option 1]
- [Agent fills in option 2]
- [Agent fills in option 3]
- I'll specify
 
Question 5: Should the film title be added at the end?
Options:
- Add the film title
- Not needed
```

Internal rules for visual style (used by the agent to select the recommended option; not presented to the user)

Seed code Best-fit script types `--sref 6507535497 --profile vjh5v84` Workplace dystopia, Cold War espionage metaphor, psychological absurdist comedy `--seed 890818711 --profile kcpmlj9` Neo-Eastern aesthetics Xuanhuan, mythic fables, historical epics, apocalyptic philosophy `--sref 4647687707 --profile xq9mmje` Hard sci-fi, AI awakening, heavy psychological suspense (memory fragments / schizophrenia)

**Seed selection rules:**

- Only one seed may be selected at a time; mixing is forbidden
- If the script spans multiple genres, defer to the emotional motif
- After confirmation, record the selected seed; all subsequent MJ V8.1 prompts must uniformly append that seed code at the end

### 1.3 Platform Content Compliance Rules (Enforced Throughout)

**Core principle: rewrite the wording, not the meaning.** Whenever any text content involves high-risk expressions that could trigger platform moderation, immediately and automatically rewrite it into compliant phrasing, without weakening the original visual intent or emotional intensity. Do not ask the user; do not interrupt the workflow.

---

## Stage 2: Script View (N-Frame Chain + Camera Movement Plan)

### 2.1 Determine the Number of Storyboard Frames and the Duration Allocation per Segment

Before outputting the script view, the agent first states the planned total number of storyboard frames N, the core scene, and the preset duration of each segment.

**Decision reference for the number of storyboard frames:**

Decision factor Reference value Target title sequence duration The sum of all segment durations approaches the target duration Number of core images in the script Each imagery evolution node usually requires 1–2 storyboard frames Emotional arc complexity The more complex the arc, the more nodes; minimalist stories can use 8–10 frames

**Scene design principle: scenes are not fragmented, but crossing between scenes is allowed.**

- The title sequence does not have to be locked to a single scene throughout—scenes may be crossed, but every crossing must have a visual connective logic (echoing shapes, continuing textures, light-and-shadow transitions); hard cuts are not allowed
- Adjacent storyboard frames within the same segment must be continuous in their material/lighting system; sudden switches of art style are not allowed
- Cross-scene transitions are realized through "motif transitions": a visual element from the previous frame (shape, pattern, light) carries over into the new scene in a transformed way, letting viewers subconsciously sense the connection **Typical reference**: 30-second title sequence ≈ 3–4 storyboard frames; 60-second title sequence ≈ 5–7 storyboard frames; 75-second title sequence ≈ 6–8 storyboard frames; 90-second title sequence ≈ 7–10 storyboard frames. Each segment runs 8–15 seconds, with the overall pacing mixing fast and slow.

### 2.2 Script View Format

The script view is output in table form; no style board is generated:

```
Frame No. | Timecode | Preset segment duration | Scene title | Core imagery (position within the space + local form description) | Visual continuity with the previous frame | Camera movement design | Shot size | Emotional motif
```

**"Visual continuity with the previous frame"** explicitly states the type of transition relationship between the two consecutive frames. Every pair of adjacent storyboard frames must belong to one of the following five relationship types, noted in the script view:
Relationship Type Description Mandatory Constraint Typical Camera Movement **Same Environment · Different Subject** Space, lighting, and materials fully continuous; the subject is replaced, appears, or dissolves Environmental materials/lighting must match the previous frame `MORPH-LOCK` / `STATIC` / `PAN` **Same Subject · Different Environment** Subject form continuous; the surrounding space/materials undergo slow deformation The subject's silhouette must remain recognizable from the previous frame `MORPH-LOCK` / `BREATH-FLOAT` **Light & Shadow Change** Subject and space essentially unchanged; light source direction/intensity/color temperature shifts extremely slowly Subject and space composition essentially consistent with the previous frame `STATIC` / `BREATH-FLOAT` / `TILT` **Same Scene · Different Angle or Shot Size** Exactly the same space and the same subject; the camera switches viewpoint or shot size **When the scene is the same, there must be a change in shot size or angle; adjacent frames with identical shot size and angle are forbidden** `PAN` / `PUSH-S` / `ORBIT-S` / `TILT` **Motif Transition · Scene Leap** The scene switches entirely, but the previous frame's core visual motif (shape/texture/symbol) is embedded into the new scene in a transformed form The new scene's information density must differ noticeably from the previous frame, with the space fully readable; motif elements appear through transformation rather than duplication `MORPH-LOCK` / `STATIC`

### 2.4 Camera Movement Design System

Speed Principles

**Ultra-slow/slow is the sole keynote throughout; any fast camera movement is forbidden.** Ultra-slow + slow segments together must account for ≥80%; medium speed is already the upper limit; fast movement is forbidden throughout.

Global Camera Movement Narrative Arc (plan the whole first, then design each segment)

**The camera movement design of the video prompts must proceed from a global perspective: first determine the camera movement narrative direction of the entire chain, then write concrete instructions for each video segment.** Designing each segment's shots in isolation leads to a confused sense of direction and a broken rhythm.

**Steps for global planning:**

1. **Choose one camera movement main line for the entire chain**, to serve as the visual narrative backbone running through the whole piece
2. **Design rhythm changes within the main line**: rises and falls in speed, turns in direction, pauses in motion
3. **Determine where the turning points are**: which segments are the main line's "turns," and what the camera movement direction is before and after each
4. **Derive each video segment's camera movement design from the main line** rather than deciding it independently **Typical camera movement main line examples:**

Main Line Type Description Suitable Emotional Arc **Continuous push-in → turn to stillness** Slowly push into the depths of the frame throughout, coming to a sudden stillness at the emotional core, letting the frame's content speak for itself Lost, deeply trapped in obsession **Continuous pull-out → return** Slowly pull out from an extreme close-up as the scene gradually unfolds, echoing the opening's initial shot size Awakening, release **Push-in → pause → pull-out** Push in deeply in the early segments, stillness/deformation in the middle, slow pull-out in the later segments, releasing A complete enter-core-release arc **Continuous lateral tracking scan** The camera slowly tracks sideways through the space, as if reading a passage of narrative Observer's perspective, sense of detachment **Deformation-led** The camera barely moves; the narrative is advanced through the slow deformation of the on-screen content Sense of fate, irresistible force

Advanced Transition Techniques

Transition Brief Description **Match transition** The subjects of consecutive frames match in shape; the camera is locked; the shape slowly morphs across **Occlusion transition** A foreground object slowly fills the frame; when it is removed, the next frame is revealed **Focus transition** Focus shifts from foreground to background; the background becomes the next frame's content **Light & shadow flood** Light expands to fill the frame; as it recedes, the next frame is revealed **Material permeation** The previous frame's material texture permeates and covers the frame; the next frame emerges from within it **Mirror symmetry** The frame folds along its central axis and unfolds into the next frame

**Annotate in the script view's camera movement column, in the format:** `slow push-in + match transition`

**Lateral movement interleaving rule:** Across the entire chain, PAN / TRACK / TILT / ORBIT-S / BREATH-FLOAT-type camera movements must together account for no less than 30%. The script view's "Camera Movement Design" column uses plain-language descriptions (e.g., "slow push-in, shifting into a slow pan to the left"); do not write code directly.

Allowed and Forbidden

**Allowed:** Slow deformation, slow panning, subtle pushing movement, gradual light-and-shadow shifts, material breathing, details emerging, parallax drift, and the six advanced transitions (match/occlusion/focus/light & shadow flood/material permeation/mirror symmetry)

**Forbidden:** Any fast camera movement (dives, fast slider runs, high-speed fly-throughs, cheap spins), excessive motion, bouncing/jitter, and glow effects such as glowing halos and light beams

### 2.5 Pause Prompt After Script View Confirmation

Once the script view table has been fully displayed, present a confirmation dialog using the ask_user_input_v0 tool:

```
Question: Script content confirmation
Options:
- Confirm, proceed to storyboard image generation
- The content of some frames needs adjustment
- The duration and pacing need adjustment
- The camera movement design needs adjustment
```

---

## Phase 3: All N Storyboard Images (chained generation, one-time confirmation after all are complete)

**Before entering storyboard image generation, first inform the user:**

> "Alright, we will now begin generating the storyboard images. There are \[N\] in total; each image, once generated, will immediately be linked to the next image's reference input to continue generation, and once all are complete, they will be shown to you together for confirmation."

### 3.1 Generation Strategy: Chained Image-by-Image Generation, One-Time Confirmation After All Are Complete

**Hard constraint: the storyboard images must be generated with Midjourney V8.1; the agent performs all operations in the canvas (creating nodes, connecting wires, triggering generation) and does not hand execution over to the user.** If the environment is not connected to Midjourney V8.1, inform the user and provide the prompts for the user to run on their own.

S02 can only have its node connected and generation triggered after S01 has produced its image; the chain advances without interruption throughout, and only after all N images have finished generating are they shown to the user all at once for confirmation.

Specific operations:

- Create the S01 node in the Midjourney V8.1 canvas (Canvas), fill in the prompt, and trigger generation
- After S01 produces its image, immediately create the S02 node, **connect the wire from the S01 node's output port to the S02 node's image reference input port** (`--iw 0.3`), fill in the S02 prompt, and trigger generation
- Continue in this way, generating through to SN; once all are complete, present them to the user all at once **All node wiring is performed by the agent in the canvas; no manual wiring by the user is required.**

**Purpose and boundaries of the chained reference:**

- ✓ Carry over: light source direction, dominant color-tone leaning, material coarseness, shadow density
- ✗ Do not copy: composition, subject position, shot size, or specific frame content

**Every prompt must clearly specify the following four points:**

1. **Shot size**: extreme wide / wide / medium / close / close-up / extreme close-up / micro (state it explicitly)
2. **Angle**: front / side / back / high-angle / low-angle / oblique (state it explicitly)
3. **Frame content**: what the subject is, where in the scene it is located, and its material and state
4. **Which part of the previous frame it references**: explicitly indicate which specific region or element of the previous image is referenced (e.g., "reference the textured pattern on the left wall of S01", "reference the cool tone of the central light patch of S02"); do not merely say "reference the previous image"

### 3.2 Global MJ V8.1 Rules

All Midjourney V8.1 prompts:

- Must append: **the complete style seed code confirmed in Phase 1** (written at the end of every prompt; it must not be omitted)
- Append by default: `--ar 16:9` (MJ V8.1 does not support 21:9; storyboard images uniformly use 16:9; 21:9 is used again at the video stage)
- The prompt body is written in **Chinese**; Chinese is the default
- Forbidden keywords: `neon, vibrant, warm fill, photorealistic skin, anime`
- Texture terms are adjusted according to the selected style seed: | Style Seed | Mandatory Texture Terms | Forbidden Texture Terms | |---------|---------|---------| | `--sref 6507535497 --profile vjh5v84` | cracked clay texture, weathered stone grain, low-saturation dark background, auxiliary gold-paste reflections | high-saturation colors, neon, smooth plastic feel | | `--seed 890818711 --profile kcpmlj9` | ink-wash bleed, gold-foil crack patterns, bronze-casting feel, low-saturation antique hues | cyber elements, digital interfaces, modern industrial feel | | `--sref 4647687707 --profile xq9mmje` | holographic fragments, data noise, cold blue metallic texture, high-contrast glowing edges | warm color palette, organic textures, clay feel |

### 3.3 Storyboard Image Prompt Structure

**The film-title choice in Step 1 only affects the prompt of the final video segment and does not affect storyboard image generation. The storyboard image generation phase completely ignores the film title; no content related to the film title may appear in the prompts. It is strictly forbidden to create extra storyboard frames specifically for the film title (such as a "film title frame", "title frame", etc.)—the film title is only overlaid onto the picture with a fade-in in the prompt of the final video segment VID_N-1; it is not a standalone storyboard image.**

Prompts are strictly forbidden from containing:

- Any dynamics, camera movement, or temporal descriptions
- **Any font design, text typography, or title design elements**
- **Elements that do not match the script's historical era**
- the agent's internal analysis notes (shot-size labels, transition-type annotations, etc.) **Prompt format (no structured tags; describe the picture directly, written as continuous, natural cinematography instructions):**

```
[First line of S02 and beyond: {{Image N}} Reference the [specific area/element] in the previous frame's picture and continue its [color tone/texture].]
 
[Picture description: shot size, viewpoint, space, subject, lighting, materials, atmosphere.
Forbidden content: write according to the actual picture, e.g. "no people, no text, no faces", etc. Use static composition only.]
 
[Style seed code] --ar 16:9 [--iw 0.3, only from S02 onward] --no text, letters, subtitles, watermark, logo
```

**Visual difference requirement for adjacent storyboard frames:** Two adjacent frames in the same scene must have a genuinely perceptible change in shot size or angle, so that the difference is obvious at a glance when placed side by side.

### 3.5 Pause Prompt After Storyboard Image Confirmation

After all N storyboard images have been generated, present the following using the ask_user_input_v0 tool:

```
Question: Storyboard image confirmation
Options:
- Satisfied, proceed to video generation
- A few images need adjustment (please specify which ones)
```

After the user confirms, proceed directly to video prompt generation and video node building, automatically triggering generation.

---

## Phase 4: Video Prompts + Canvas Node Building

### 4.1 Core principle: write prompts from the images, the agent builds the nodes

**Video prompts must be designed based on the actual storyboard images on the canvas; do not copy the storyboard images' text prompts verbatim.** After the user adjusts the images, the picture may deviate from the text description, so the prompts must be faithful to the final images.

**Workflow:**

1. After the user confirms all storyboard images, the agent observes the actual picture of each pair of adjacent frames on the canvas and writes out all N-1 video prompts (including VID_N-1; the film title was already confirmed in Step 1)
2. When the actual images do not match the scripted plan, adjust the camera movement based on the actual images
3. Present all video prompts to the user for review, then the agent builds all the nodes in the canvas and connects them, directly triggering generation segment by segment, with no further user confirmation needed
4. **After all videos finish generating, immediately and automatically enter Phase 5: composite the videos first, then generate the BGM and overlay it, without waiting for user instructions. Video aspect ratio:** all video prompts must specify `--ar 21:9`.

**Strong first/last frame constraint:** Each video segment must use the actually generated MJ V8.1 storyboard images as its first and last frames fed into the video model; **the omni-reference mode (single-image reference/full-image reference) is forbidden—first/last frame mode must be used**. Text descriptions may not substitute for images, and videos may not be generated from a single frame alone. Without first and last frame images, no video can be generated.

### 4.2 Segment Structure

Each video segment corresponds to one pair of adjacent storyboard frames:

```
VID_01: S01 (first frame image) → S02 (last frame image)
VID_02: S02 (first frame image) → S03 (last frame image)
...
VID_N-1: S(N-1) (first frame image) → SN (last frame image)
```

All video segments must use the user's finally confirmed MJ V8.1 generated images as first and last frames; text descriptions are not a substitute.

### 4.4 How to Write Video Prompts: Plan Globally First, Then Write Segment by Segment

**Step One: Global camera-movement narrative planning (complete after receiving all storyboard images, before writing any single segment's prompt)**

Observe all N storyboard images and make the following judgments:

1. **Choose the global camera-movement main line**: What is the overall direction of camera movement across the whole chain? (Refer to the typical main-line examples in §2.4)
2. **Mark the turning points**: Which segments are the "direction changes" of the main line? What is the motion state before and after each change?
3. **Mark where advanced transitions will be used**: Which pairs of adjacent frames are suitable for match transitions, occlusion transitions, etc.?
4. **Mark the deformation-dominated segments**: In which segments is the camera nearly still, advancing through slow deformation of the picture content? Once planning is complete, write the prompts directly segment by segment; there is no need to output a camera-movement plan table for the user to confirm.

**The sole duty of a video prompt is to describe camera behavior, not picture content.** The picture content of the first and last frames is already locked inside the images; the video generation model reads it from the images themselves, so the prompt does not need to describe it again.

**The prompt contains only four things:**

1. First frame image reference
2. **Intrinsic picture dynamics**: How elements already present in the first frame image move slightly (particles drifting, smoke flowing, a figure walking slowly, light trembling faintly, etc.)—only derive from content already in the image, never add anything not in it; one sentence is enough
3. Camera movement instruction: direction, speed, plus a camera-behavior description for advanced transition techniques (only say how the camera moves)
4. Last frame image reference (as the camera's landing point) How to write advanced transitions: match transitions, occlusion transitions, focus transitions, light-and-shadow engulfment, material permeation, mirror symmetry—one sentence in the prompt in Chinese stating the transition action is enough; no elaboration needed.

How to write camera movement (in plain language, not code):

Camera action phrasing examples push in the camera pushes in extremely slowly pull back the camera pulls back slowly pan left/right the camera pans left extremely slowly left/right tracking pan the camera pans left slowly following the subject slow tilt down/up the camera tilts down extremely slowly slow orbit the camera orbits the subject extremely slowly push-through the camera slowly pushes through the surface, transitioning to the interior static the camera is completely still and locked deformation the camera stays locked while the picture content slowly deforms breathing float the camera has no deliberate movement, only an extremely slight organic float

### 4.5 Video Prompt Template

```
[VID_XX · SXX → SXX+1 · Duration: Xs · --ar 21:9]
 
<<<image_1>>>
[Intrinsic picture dynamics: slight movement of elements already present in the first frame image, one sentence, derive only, add nothing]
[Camera movement instruction: direction, speed, 1–2 sentences, camera behavior only]
[If there is an advanced transition: description of the transition's camera behavior]
<<<image_2>>>
 
--ar 21:9
no music, no BGM, ambient sound and environmental audio allowed, sound enabled
```

### 4.6 Verification Checklist

```
□ The whole chain has a clear camera-movement main line, with advanced transitions used in at least 2 places
□ Each segment's prompt contains only the four things, with no picture content description
□ Adjacent segments: last frame = next segment's first frame, speed ramp continuous, no hard cuts
□ PAN/TRACK/TILT/ORBIT-S/BREATH-FLOAT account for ≥30%
□ Ultra-slow + slow-speed shots account for ≥80%, no rapid camera movement, no glow effects
□ Step 1 has determined whether to add a title; the VID_N-1 prompt has been handled according to that choice
```

---

### 4.7 The Final Video Segment VID_N-1

VID_N-1 uses S(N-1) as its first frame and SN as its last frame; its structure is fully identical to all other segments. If the user chose to add a title in Step 1, the agent designs an A24-caliber typography scheme (typeface, weight, letter spacing, position) based on the script's style and the color palette of the SN frame; **the title fades in overlaid on the last frame SN, without cutting to a black screen**, and is marked in the prompt with `【Title · Fade-in】`. The title appears only in this segment's prompt and is completely unrelated to storyboard image generation.

```
[VID_N-1 · S(N-1) → SN · [Xs] · --ar 21:9]
 
<<<image_1>>>
[Intrinsic motion within the frame]
[Camera movement instruction]
<<<image_2>>>
【[Title · fade-in, overlaid on the SN frame, if Step 1 chose "yes"]】
 
--ar 21:9
no music, no BGM, ambient sound and environmental audio allowed, sound enabled
```

---

## Stage 5: BGM Generation + Video Assembly (executes automatically after all videos are generated, no user trigger required)

### 5.3 BGM Design

The user has already selected a BGM style in Step 1; output the Suno / Udio prompt directly based on the selected style, with the BGM duration matching the total video duration.

### 5.2 Assembly

After the BGM is generated, stitch all video segments together in order on the canvas and overlay the BGM:

```
VID_01 + VID_02 + … + VID_N-1
```

- Completed by the agent on the canvas; segments are joined directly with first/last frames aligned, with no transition effects added
- The sound toggles on the video nodes must be turned on; do not generate music/BGM, sound effects and ambient audio are allowed; the BGM is generated in this stage and then overlaid

---

## Stage 6: Opening Credits (optional)

### 6.1 Credits Design

After video assembly is complete, use the ask_user_input_v0 tool to ask:

```
Question: Do you need opening credits?
Options:
- Yes, generate all names in a single image
- Yes, one image per name
- No
```

The credits layers are **generated directly by the agent using the image tool**, without using Midjourney V8.1 and without attaching a style seed.

### 6.2 Generate the Credits Layers

Collect the content the user wants to display (lists and ordering of director, screenwriter, lead actors, etc.), then:

- Use the image generation tool to create layers with a **pure black background**, with text colors designed from the actual color palette of the final video—taken from contrasting or complementary colors of the frame—to ensure readability and consistency with the overall visual style
- Output layer files the user can overlay directly in editing software by changing the blend mode, with no need for keying/cutouts

Font scheme recommendations

Scheme Font Use case **Industrial Engraved** Bebas Neue / ZCOOL GaoDuanHei sense of power **Minimalist Modern** Futura PT / Source Han Sans clear and readable **Organic Hand-Carved** Freight Display / HYQiHei literary texture **Classical Serif** Trajan Pro / FZSongKeBenXiuKai epic feel

---

## Design Principles

1. **No literalism** — Do not present classic scenes from the script directly; transform them into visual metaphors.
2. **No illogical hard cuts** — Scenes may leap across, but every leap must maintain overall coherence through a unified color palette, continuous material language, and visual anchor points between consecutive frames.