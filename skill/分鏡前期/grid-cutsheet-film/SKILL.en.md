---
name: grid-cutsheet-film
description: "Multi-grid contact sheet director: grid-indexed shot control keeps long-take storyboards organized"
---

# grid-cutsheet-film

A story-driven video workflow: use GPT Image 2 to generate a "multi-cut sheet" (a single image carrying all the internal cuts/beats within one shot), then use Seedance to drive generation of that shot's video based on the sheet. The core mechanism is **cut index = the single source of truth for chronological order** — the spatial arrangement of tiles on the sheet can be arbitrary; only the numbers (1…N) printed in a fixed corner of each cell carry the story order. Human-in-the-loop collaboration on a single workflow run, pausing at key stages for user confirmation.

> Environment adaptation (Flova → our 13 tools): GPT Image 2 → `generate_image_v3`; Seedance 2.0/MultiModalToVideo → `generate_video_v3`; text_editor (Final_Video_Spec) → `write_file_v2`; video_assembler → `composite_video`; `<<<image_n>>>` character-reference markers → `reference_nodes` + `{{NodeKey}}`; reply_to_user card-style confirmations → report directly to the user and pause. Resolutions 2K (images) / 720p (video) are kept as the default recommendations; "up to 15 seconds per shot" naturally matches this environment's engine single-generation duration cap, so it is kept.
>
> **This skill is self-contained and inline; it does not depend on any other skill.**

## 7-Step Pipeline (Dependencies + Pause Points)

1. Write `Final_Video_Spec.md` (title, genre, aspect ratio, duration, visual style, language) → `write_file_v2`.
2. Generate the storyboard: key elements (key_elements), shot list (shot_list), audio layers (audio_layers). Once the storyboard is ready, first scan the context for user-provided or pre-existing assets (element images, background music, etc.), and before generating, bind each existing asset to its matching storyboard slot to avoid regenerating content the user already provided.
3. **Elements**: if the user has already uploaded element assets, bind them to `key_elements`; otherwise generate element images.
4. **Generate the multi-cut reference sheets for all shots (one call per shot)**: for each shot, write an image prompt that places every internal cut/beat from that shot's storyboard on **one canvas**, as a **multi-cut sheet** (clear cell boundaries). **The spatial tiling order on the sheet does not define cut order** — **story order is carried solely by the printed cut indices** (identical to the storyboard shot-list numbering). **Each cell's aspect ratio must match the aspect ratio locked for that shot's Seedance generation** (see `Final_Video_Spec.md`).
5. **Generate video for all shots**: generate with reference to that shot's multi-cut sheet image.
6. Generate all audio_layers from the storyboard.
7. Once all assets are ready, perform final assembly and guide the export.

**Dependencies**: 2→1; 3→2; 4→3; 5→2,4; 6→2; 7→2,5,6.

**When to pause**: do not run all steps in one go. Stop after the spec, after the storyboard, after the elements, **after each batch or group of multi-cut sheets** (or after all sheets are complete), after the shot videos, and after the audio — confirm with the user between stages.

**Note**: for user-provided media, bind first before regenerating; avoid duplicating content the user has already provided.

## Storyboard Design

**Key element design**
- Include as needed: **key subjects** (characters, objects), **key locations/scenes**, **key props**.
- **Characters**: multiple looks (outfits, ages) must be clearly described (e.g., Look 1: …; Look 2: …).
- **Tone/color reference**: if the project uses a global color grade or a reference clip, note this at generation time (keep the reference length practical, ideally ~15 seconds or less for tone extraction).
- **Locations/scenes**: placement and orientation of important objects and performance areas.
- **User-provided assets**: descriptions must **match** the reference material and must never contradict what is seen or heard.

**Shot design (long take first)**
- Prefer **long takes containing multiple internal cuts**: use the model's **full per-shot budget** (**up to 15 seconds per shot**), and when the story supports it, aim for **at least six internal cuts** per shot. Design **within** the long take, with the cutting rhythm following the narrative; **do not** split into a second shot what can be told in one long take. Maximum 15 seconds per shot (hard model limit).
- **Every shot description must include three elements**:
  - **Scene**: the location, identified via element ID (e.g., `[Element_Office_Noir]` — format example only).
  - **Story content**: action, movement, dialogue — including **exact lines** where applicable; reference characters via element ID.
  - **Camera**: shot size, angle, and camera movement for each beat.
- **Internal cut list**: list every beat in **chronological order** and assign the **stable cut indices (1…N)** to be used consistently everywhere downstream (sheet labels, prompts). This list is the **cut list** for the shot's single GPT Image 2 image: **one grid cell = one internal cut** (keyframe/state). **The cut positions on the sheet may follow any layout**; the editor and the model rely on **the index written on each cell**, not on left-to-right position.

**Standalone audio design**
- **Background music**: at least one global track; longer pieces may use multiple segments with `audio_id` and ranges.
- **Narration**: type must be `narration`; must specify the voice, intonation, exact script, and a `layout_instruction` for the shot range.

## Element and Cut-Sheet Generation

**Element asset generation**
- Generate element images with TextToImage / ImageToImage as needed; `generate_image_v3` at 2K is recommended, for quick iteration and consistency with the rest of the pipeline.
- **Characters**: one landscape 16:9 character image per character, containing from left to right a **bust close-up + full-body three views (front, side, back)**, so Seedance can read identity and outfit information.

**Multi-cut reference sheet per shot**
- Model `generate_image_v3`, resolution 2K (use 1K/4K only when the brief or pipeline explicitly requires it).
- **Modality**: when element reference images exist, prefer ImageToImage — pass in the character/scene references so the grid matches the locked looks; otherwise use TextToImage with full visual detail.
- **Rule — one shot, one image, one call**: the prompt must describe the complete multi-cut sheet and what is visible in each cut within a single generation.
- **Cell aspect ratio (highest priority)**: each cell's composition must have a width:height ratio matching the shot's specified output aspect ratio (e.g., 16:9, 9:16, 1:1 — per `Final_Video_Spec.md`). **Do not** compress cells into extreme strips whose geometry does not match the final video; matching the ratio reduces reconstruction drift when the sheet is used as a reference.
- **Layout**: a single canvas; N cells (one key still per internal cut); thin neutral divider lines; flexible spatial arrangement (rows, columns, or an irregular grid) — **do not** imply that reading direction equals story order.
- **Cut-order marking (required)**: print the **storyboard cut index (1…N, same numbering as the cut list)** in a **fixed corner** of **every** cell. The index is the **source of truth** for chronological order; the sheet's order is optional.
- **Cut count**: keep N readable — typically **2–6** internal cuts per shot on a single sheet. If the storyboard has more beats, go back to the storyboard stage and **merge** tiny beats or **split** the shot — never exceed what one grid can display legibly.
- **Style requirement**: each shot's multi-cut sheet must embed the visual style defined in `Final_Video_Spec.md` (genre, look, palette, era, references), applied consistently across **all cuts** on that sheet.

**Shot videos**
- Use `generate_video_v3` (Seedance 2.0) at 720p, with the same aspect ratio as the sheet cells and the spec.
- **Reference**: that shot's multi-cut sheet (a beat roadmap + per-cut geometry aligned with the output ratio).
- **Markers**: in the video prompt, tag each character with `<<<image_n>>>` (in this environment: `reference_nodes` + `{{NodeKey}}`), matching the element sheets; **the cut sheet is the primary still reference** — **drive motion via the numbered cut indices (1…N) visible on the sheet**, do not guess the sheet order.
## Prompt Craft A: Multi-Shot Reference Composite (GPT Image 2)

**Intent**: A **contact sheet** of N key stills for this shot. Each still sits in a cell whose aspect ratio matches the shot's final video aspect ratio (e.g., the same 16:9 or 9:16 Seedance will use). The sheet is a **layout reference**; it does not assert that tile position equals timeline order.

**Cell geometry (priority)**: State explicitly in the prompt that every cell is letterboxed or cropped to the shot's target output aspect ratio (write out the ratio, e.g., "every sub-frame is native 16:9"). This matters more than how the tiles are arranged on the canvas.

**Cut-order markers / storyboard indexing (required)**: Each cell must display, in a fixed corner (the same convention across the whole composite, e.g., top-left), the same cut numbers (1…N) as in the storyboard cut list. **Edit order follows these numbers only** — the spatial order of the tiles is optional; any spatial arrangement may be chosen for a tidy layout. Markers must be **minimal, high-contrast, small but readable**; they are production metadata, not in-frame signage unless the script calls for it.

**Opening (required standard template)**: Example wording: "A single image, a composite of [N] separate film stills. Each still is framed at [target aspect ratio, e.g., 16:9] to match the final video. Thin neutral divider lines between cells. Each cell shows a small index [1…N] in the [corner] matching the storyboard cut list. Photorealistic live-action cinematic style; characters and costumes stay consistent." (Adjust rows and columns only for a tidy layout; **do not** request left-to-right as the story order.)

**Per cut (by list index)**: For each index 1…N, in one fluent English paragraph (or clearly numbered as Cut 1/Cut 2/… to match the labels on the image), describe only **what is visible** in that still: subject pose, environment, shot size, angle, lighting, color grade, lens feel — aligned with the "6 core rules" below (woven in as natural language, not as labeled bullet-style headings in the output prompt).

**6 core rules (global + per cut)**:
1. Professional style anchor (cite an auteur/reference film where necessary).
2. Composition and lens.
3. Lighting that emphasizes negative fill/contrast.
4. Restrained color grade (a single dominant hue at roughly 90% unless the user asks otherwise; avoid the clichéd neon magenta/cyan clash unless requested).
5. Rendering quality (texture, detail).
6. Emotion and micro-expressions on dramatic beats.

**In-frame text**: Only when necessary, put the exact copy in quotation marks.

## Prompt Craft B: Video Prompt (Seedance 2.0)

**Open with `live action`**: When the **primary** reference is that same multi-shot composite, the video prompt begins with the phrase `live action` (lowercase). It subtly steers Seedance toward more realistic lighting, skin/object texture, and motion — closer to real footage than an illustrated or overly "AI-glossy" still. It is not a substitute for concrete motion or cinematography language; it merely biases the model's interpretation in the right direction.

**Then**: Tag characters with element references (`<<<image_1>>>`, …; `{{NodeKey}}` in this environment). For the composite, state explicitly: **follow the cut numbers printed on the storyboard, 1→2→…→N** — **do not** assume composite position equals chronological order. Describe the temporal flow across those numbered beats, using the four-layer structure **Camera → Subject → Space → Audio** for the dynamic parts:

1. **Camera**: movement, reframing, cuts between beats (aligned to cut 1, cut 2, … by index, not by grid position).
2. **Subject**: actions, expressions, beat-by-beat description.
3. **Space**: environment/depth/background motion.
4. **Audio**: dialogue `{...}`, sound effects `<...>`, music `(...)` only when intended; otherwise follow the silence rules below.

**Multi-beat / Shot 1, Shot 2**: You may label beats Cut 1, Cut 2, … matching the printed indices on the composite. **Do not** rely on precise wall-clock timing (e.g., "3.0–5.0s"); describe the ordered beats **by number**, not by composite position.

**Seedance wrappers**: `(...)` music, `<...>` sound effects, `{...}` dialogue (flag the language if it is not the project language), `【...】` on-screen title.

**Negative constraints (always apply)**:
- There is a separate voiceover track in the storyboard — **do not** put that narration text into the video prompt.
- Unless the shot genuinely calls for built-in score, it is almost always `no music`.
- Always `no subtitles` (subtitles are added in post).

## Related

Boundaries (don't use this skill; reroute): need storyboard images only, no video generation → storyboard-generation; single shot, no composite, direct generation → video-generation.