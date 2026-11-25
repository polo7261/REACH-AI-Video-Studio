---
name: aesthetic-tone-consistency
description: "Aesthetic tone-consistent short film: one sref code locks the whole film's look — no aesthetic drift, consistent tone shot by shot"
---

## name: aesthetic-film\\

namespace: industry\
title: "Aesthetic-Defined Short Film"\
description: "Art short films centered on a Midjourney aesthetic style (sref tone-setting): first use MJ to lock in the visual tone for the whole film, then Seedance produces the finished film shot by shot. For 'turning a short story / mood piece into a finished film with one unified cinematic aesthetic baseline.' Two modes — A: MJ directly outputs key frames per shot → Seedance; B: MJ outputs an element reference board → Nano Banana lightly composites/edits into key_frame → Seedance. Pure image aesthetics (no video) → image-generation; general multi-shot narrative (not MJ aesthetic-defined) → cinematic-flow."\
version: 3

# aesthetic-film

Use this skill when creating **art short films centered on a Midjourney aesthetic style (sref tone-setting)**: first use MJ to lock the film's visual tone into a single unified baseline, then have Seedance generate the finished film shot by shot. The core is not narrative complexity but **aesthetic consistency** — the entire piece maintains one look through a single set of sref / style descriptions. This skill is self-contained: the sref tone-setting mechanism, shot design, cinematic prompts, Seedance sequences, and audio & compositing rules are all inlined, not outsourced to other skills.

## Two Modes

- **Mode A (MJ directly outputs key frames, source #16)**: For each shot, MJ directly generates the key frame image → Seedance produces the film. Suited to cases where the visuals are driven directly by the texture of MJ-generated images.
- **Mode B (MJ reference board → Nano refinement, source #17)**: MJ outputs an **element reference board** (appearance anchored by sref), then Nano Banana performs **lightweight compositing/fine-tuning** on the MJ reference images to produce each shot's key_frame → Seedance produces the film. Suited to narrative pieces that need subject positions/poses precisely arranged per the storyboard while strictly keeping the MJ style lock.

Mode selection is confirmed with the user during the spec finalization stage; both modes share the sref tone-setting, shot design, prompt, and compositing rules below.

## Stages (per the SP full workflow)

Do not run all stages in one pass. Pause at each key stage (spec finalization / style-path confirmation / storyboard confirmation / element images complete / key frames complete / after per-shot video / after audio) and use `ask_human` or a card to invite the user to confirm before proceeding. Before continuing, use a card or a reply to invite the user to review.

1. **Spec finalization**: Write `Final_Video_Spec.md` (title, genre, aspect ratio, duration, visual style, language, model preference) → `write_file_v2`. At the same time, **confirm the aesthetic style path** (see "Style Path & sref Tone-Setting") and Mode A/B.
2. **Storyboard**: Generate shot_list + audio_layers (Mode B additionally includes key element design) → see "Storyboard Design".
3. **Element/key frame images**: In Mode A, output one key frame image per shot; in Mode B, first output the MJ element reference board, then Nano-refine each shot's key_frame → `generate_image_v3` (see "Element & Key Frame Generation"). For existing user assets, first bind them to the corresponding storyboard positions via `get_node_info`; do not regenerate.
4. **Per-shot video**: `generate_video_v3` shot by shot, with `reference_nodes` referencing key frames / element images and `{{NodeKey}}` bindings; each shot ≤15s (engine single-run limit). Write prompts per the inlined rules in "Per-Shot Video Prompts".
5. **Audio layers**: `generate_audio` generates all independent audio layers (≥1 global BGM; long pieces may use multiple BGM segments, each with its own `audio_id` and range; if there is voiceover / narration, set up a narration layer).
6. **Compositing**: `composite_video` assembles the finished film in storyboard and timeline order, then guides the user to export.

**Stage dependencies** (source Flova #16/#17): 2→1; 3→2; 4→3; 5→2; 6→2,3,4,5.

**Existing user assets** (mainly affect steps 3–5): Before filling in generated content, first use `get_node_info` to bind and assign user-provided / existing assets to the corresponding storyboard positions; avoid regenerating assets the user has already provided.

## Style Path & sref Tone-Setting (Core Craft)

Before spec finalization and asset generation, **first confirm with the user the path for generating the aesthetic style image with MJ** (choose one of two):

- **Path 1 (style description words)**: Define the style via prompt descriptions. When the user has specified style proper nouns or preferences, record the style description in `Final_Video_Spec` and **always reuse** this set of style description words in **all subsequent element generation**.
- **Path 2 (sref code tone-setting)**: Use `--sref` codes as the style benchmark to build storyboard content, **rather than** rewriting the style from `Final_Video_Spec` into every MJ prompt.

`--sref` **selection rules (Path 2)**:

- First ask the user whether they have Midjourney `--sref` style codes. If not, the agent picks one itself (typically an integer in **0–4294967295**; random or content-fitting both work); **record the code used and reuse it in all subsequent MJ calls in the project**, unless the user changes it.
- Syntax is `--sref <code1> <code2> …`, with tokens **separated by spaces** (e.g., `--sref 5877700996 4815442863`). Each value must be an integer in 0–4294967295. **Multiple codes can be stacked**; if the user provides multiple, record the full list and reuse it throughout. When inventing codes without user preference, **prefer a single auto-picked integer for simplicity**, unless the user explicitly requests stacking.

**Tool adaptation**: MJ images are generated by `generate_image_v3` (with `ai_model` set to `Midjourney V8.1`). **If the current engine does not support** the `--sref` **parameter**: fall back to Path 1 (style description word reuse) + pass the style benchmark image in as a style reference via `reference_nodes` — the mechanism (one style lock for the whole film, reused across shots) is preserved, with the implementation point adapted.

## Storyboard Design

### Key Element Design (Mode B / when recurring elements exist)

- Cover **key subjects** (characters, objects), **key locations / scenes**, and **key props** (if any).
- **Explicitly list multiple character states**: When a character has multiple looks / appearances in the project (different outfits, ages), state them explicitly in the description (Look 1: …; Look 2: …).
- **Object positions and orientations in the scene**: Describe the position and orientation of important objects (especially props and the areas where the main action / performance takes place).
- **User assets must be matched**: For assets the user provided and designated as key elements, the description **must match them** and must not contradict what is seen / heard.

### Shot Design (three elements per shot)

Every shot description must include:

- **Scene**: Reference the location / set using the scene element ID (e.g., `[Element_Office_Noir]`).
- **Narrative content**: The actions / dynamics of characters and key objects, lines and performance; write out the **exact lines** (spoken dialogue or inner monologue / OS), and reference characters via element IDs.
- **Camera language (cinematography)**: Shot size (wide / medium / close-up), camera angle (low / high), and camera movement (static / pan / dolly).

### Independent Audio Design

- **Background music**: Design at least one global BGM track. When the video is long (e.g., ≥3 minutes) and has clear act breaks / turning points, multiple music segments may be planned (each with its own `audio_id` and scope).
- **Narration**: When driving the story with voiceover / narration, design it here (type `narration`): define the voice characteristics, tone, and exact script; use `layout_instruction` to confine it to the relevant shots.

## Element & Key Frame Generation

### Key Element Images (MJ baseline, shared by both modes)

Load the user-selected style path (Path 1: use the style description recorded in `Final_Video_Spec`; Path 2: use `--sref` tone-setting).

- Use `generate_image_v3` (`Midjourney`-family engines) to produce **style / scenes, character / prop bases, and large-scale scenes**.
- **Prompt rules**: Describe the content (people / things / places, recognizable silhouettes, environment) and append `--sref` per the rules above. **Do not** stuff the long "intended video / image style" copy from the spec into MJ, and do not treat the MJ step as one that must execute that document — **sref + subject / scene description is enough**.

### Role of the MJ Reference Board (Mode B)

- The MJ board is the **source of truth for appearance**: appearance is anchored by `--sref`.
- In Mode B, MJ is the **reference board factory** for the subsequent Nano work, **not a color-grading step at final assembly** — don't expect MJ to produce finished frames in one step.

### Nano Banana key_frame Refinement (Mode B core · anti-pattern)

- Use `generate_image_v3` image-to-image (`Nano Banana Pro`-family engines) to produce **each shot's first frame**, aligned with the shot description in the storyboard; set resolution to **2K–4K** per the project spec.
- **Inputs**: Scene / style / character / prop element references routed per shot (`reference_nodes`).
- **Prompts must be concise**: Specify **which reference image provides environment / texture** and **which provides style / lighting vocabulary**, and **only** relate what the storyboard script requires (pose, layout, who holds what). **Never** paste paragraphs re-describing color grading / lighting / cinematic references / mood — **that forces the model to fully repaint and weakens adherence to the MJ reference image**. Nano only performs **lightweight compositing / fine-tuning** on top of the MJ reference image, not a rebuild of the whole image from a long prompt.

## Per-Shot Video Prompts (fully inlined, not outsourced)

### Language Rules (highest priority)

When the user inputs in Chinese or a Chinese locale is loaded, prompts are **written in Chinese**; but the narration / dialogue content inside prompts strictly follows the Output Language of `Final_Video_Spec`.

### Six Core Rules for Image Prompts (apply globally when writing MJ `key_element` images)

A prompt is not merely a description of "what's in the image"; it is like a professional film director + colorist giving instructions to the team. Write these 6 rules as **one fluent, natural English paragraph**, **woven together** — do not output them as labeled sections:

1. **Professional style anchors**: Combine professional art / film terminology with style words; introduce an "author" and concrete cinematic visual anchors (e.g., `Neo-Noir style, David Fincher Style, inspired by Se7en`), not just a generic `Neo-Noir`.
2. **Composition & camera**: Specify cinematic composition (`Over-the-shoulder shot` / `Dutch angle`) and shot size (`Close-up` / `Medium shot`).
3. **Lighting (including negative light)**: Detail the key light and emphasize "negative light" to create contrast and drama (`Strong chiaroscuro contrast` / `dramatic interplay of light and shadow` / `deep facial shadows emphasizing facial structure`).
4. **Color grading (90% single dominant hue · no red-blue neon)**: Restrained high-end Hollywood grading (`deep teal-cyan shadows dominating 90%, zero warm fill` / `muted watercolor wash`); unless the user explicitly requests it, **never use clashing red-blue neon** (banned: `crimson bleed`, neon magenta vs. cyan); about 90% of the frame uses only **one dominant hue** — extreme restraint.
5. **Visual rendering**: Describe overall visual quality and texture (fine rendering, richly intricate details, soft focus with subtle gaussian blur).
6. **Atmosphere & subtext**: Describe the character's "subtext" and micro-expressions, freezing action at a dramatic moment (`oppressive suffocation` / `no mercy` / `predatory stillness`); for inanimate objects, describe their state (a sense of fate / a piercing gaze / cold detachment). Reject stiff, posed setups.

- **Conditional element · in-frame text** (only when relevant): When text appears in the scene (e.g., on-screen text), integrate it naturally, wrapping the exact text to be rendered in **quotation marks**, e.g., `A neon sign in the background reads "DANGER".`.

### key_frame Section (Mode B · the 6 rules do not apply)

- `key_frame`**(Nano Banana) is the exception**: **do not** apply the lengthy six core rules — heavy cinematic text makes Banana ignore / fight the MJ reference image and repaint. Prefer only "**slot tags + storyboard alignment**".
- **Core rule**: The shot description in the storyboard is the script of "what must happen" (who / where / action / camera rhythm) in this still image. The prompt only needs **minimal routing text** so the model uses the MJ element images as references and fine-tunes for that rhythm — not a second full treatment of content and style in words. The more exhaustively you describe the desired look and content, the more Banana leans toward regenerating and dropping the MJ style lock.
- **Ideal short-prompt pattern (example)**: `Reference environment texture Element_Dark_Void_img, and style Element_Glowing_Cube_img.` (then append only what the storyboard requires, such as subject position or `cube centered, static, push in before` — keep it short.)

### key_element Prompt Structure (when writing element definitions)

Structure around: **subject & identity** (what the character / prop / scene / creature is; characters include age, build, ethnicity (if specified), distinctive features, voice) → **characteristic details** (prioritize features that must stay consistent across shots: for characters, facial features / makeup / the material, cut, color, and condition of clothing and accessories; for props, shape / material / color / size / condition & age / unique markings) → **atmospheric & emotional tone** (tense / melancholic / hopeful / serene / uneasy / warm / oppressive / fearful / nostalgic / isolated / intimate…). For Path 2, append `--sref` after the main prompt (verify each token is in 0–4294967295, normalized to space-separated; if none is set, pick a code, record it, and reuse it throughout).

### Video Prompts · Reference Image Naming

First **assign each reference image a role** so Seedance reads the face and look correctly: pass reference images via `reference_nodes` and reference nodes with `{{NodeKey}}`. Template: Subject 1 — facial-feature reference `{{Face_1}}` (head close-up); hairstyle / makeup / wardrobe reference `{{Body_1}}` (full-body shot). Continue numbering with Subject 2.

### Video Prompts · Seedance Four-Layer Order (camera → subject → space → audio)

Append action / motion prompts in this order:

1. **Camera**: Movement or camera / cut changes (`static → push in`, `cut to new angle`, `orbit`, `pan`).
2. **Subject**: Actions and expressions (who does what, facial demeanor).
3. **Space**: Position / environment changes (positions of subject or camera relative to the space, background motion, depth / layout transitions).
4. **Audio**: Dialogue (if any), sound effects, and a note when the model omits music (see negative constraints).

- **Action details**: Base them on **specific body parts** (hands / legs / head / shoulders) and add **degree** (amplitude / speed / force, e.g., `slowly raises one hand`, `snaps head left`, `pushes hard off the ground`); with multiple beats in one prompt, order them by story chronology: **primary action → secondary actions**.
- **Multi-beat**: When the tool accepts long prompts, you may mark **Shot 1 / Shot 2 / Shot 3** within a single generation to indicate a sequence of camera or story beats.
- **No second-by-second clock timing**: Precise clocks ("0–3 s", "at 2 s…") **cannot be reliably executed** — do not hard-split by exact seconds or write a second-by-second plan; describe **what happens in sequence**, not a shot list divided by time.
- **Optional polish** (for live-action briefs): You may add slight handheld micro-shake / subtle film grain, kept subordinate to the four-layer order above.

### Wrapper Conventions (Seedance engine syntax)

The engine accepts natural language; these wrappers help the model distinguish music / sound effects / dialogue / on-screen text:

- **Music** (describing what is playing): `(...)`, e.g., `(fast-paced rock playing in the background)`.
- **Sound effects**: `<...>`, e.g., `<distant dog barking>`.
- **Spoken dialogue**: `{...}`, e.g., `{Hello, world}` — when the line is not in the project's main language, tag the language before the braces, e.g., `Says in Japanese: {こんにちは}`.
- **On-screen titles / chapters / subtitle text**: `【...】`, e.g., `【Chapter One: Departure】`.

### cut to Multi-Stage Actions

For highly complex / multi-stage action within one shot, describe the sequence **in order**, using `cut to` labels for transitions (shot A…, cut to shot B…, cut to shot C…). Example:\
`Shot1: {{image_1}} his hands carefully open a dusty wooden box, with the sound of a soft creak. {{image_1}} His expression is focused and curious. The camera is a fixed shot, and the background attic is static. Shot2: cut to a bright blue light emanates from the artifact inside, casting an ethereal glow on his face and creating long, shifting shadows in the room. {{image_1}} His expression changes from focused to shocked awe as the camera begins a slow zoom in on his face. Shot3: cut to {{image_1}} he looks up with determination, the blue light reflecting in his eyes, as he slightly turns his head to the left to look past the camera. (no dialogue, no music, no subtitles)`

### Three Negative Constraints (always include in video prompts)

- When the storyboard indicates a shot has a **separate narration track**, do **not** write narration text in the video prompt, to avoid audio conflicts.
- To prevent the model from adding unwanted BGM, include `no music` **almost always**.
- Subtitles are added in post; **always** include `no subtitles`.

## Compositing (Embedded Audio Muting Rule)

`composite_video` assembles all shots, narration tracks, and BGM in storyboard and timeline order; once the edit is ready, guide the user to export. **If a final shot has no in-shot dialogue or narration, mute that shot's / video layer's embedded audio** and rely only on the designed **audio layers** (BGM / SFX), so the shot's own sound effects do not conflict with the mix.

## Variants & Boundaries (do not use this skill; reroute)

- **Pure image aesthetics (no video; aesthetic stills only)** → image-generation.
- **General multi-shot narrative shorts (not MJ aesthetic-defined; story / character / dialogue-driven)** → cinematic-flow.

(This skill is self-contained with no source-level cross-skill dependencies, hence no "cooperating skills" declaration table. Generation primitives = tool calls such as `generate_image_v3` / `generate_video_v3` / `generate_audio` / `composite_video` / `write_file_v2`, not cross-skill dependencies.)