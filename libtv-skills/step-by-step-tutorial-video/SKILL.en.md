---
name: step-by-step-tutorial-video
description: "Step-by-step tutorial short video: a blogger demonstrates product usage step by step; ideal for influencer recommendation shorts."
---

---

## name: ugc-tutorial-flow\\

namespace: industry\
title: "UGC Tutorial Video"\
description: "UGC-style tutorial video—an influencer demonstrates how to use a product step by step, with 'Step N — Heading' step captions on screen. Storyboard panels are 21:9 horizontal strips containing 4 vertical 9:16 slots, one usage step per slot, step numbering globally continuous, CTA only in the last cell of the last panel. Covers usage analysis→persona anchor→monologue→serial panel generation→per-shot generation→compositing."\
version: 3

# ugc-tutorial-flow

Use this skill when making UGC-style tutorial videos (an influencer **demonstrating how to use a product step by step**, with "Step N" step captions on screen). You do the creative work (persona / monologue / storyboard prompt) yourself—the source delegates it to a backend enhancer, which this environment doesn't have. You handle control flow, gating, timing, and stitching.

One pipeline covers all UGC tutorial / product usage videos: **each storyboard slot = one physical step of using the product**.

## Storyboard structure (tutorial-specific · differs from the talking-head base)

- Each **storyboard panel = one 21:9 horizontal strip containing 4 vertical 9:16 slots** (the talking-head base is 16:9 with 3 slots; the tutorial override is 21:9 with 4 slots).
- Each slot displays a "Step N — Heading" caption.
- **Total steps = 4 × panel count**; **step numbering is globally continuous** (no reset across panels).
- The **CTA tail** appears only in the **last cell of the last panel**.

## Flow

1. **Parse requirements + product usage analysis** (product-analyzer): derive steps from the real usage flow, producing the `step_captions` array. **Mandatory**.
2. **Persona generation**: `generate_image_v3` produces the influencer character anchor (or the user provides photos). Identity is locked to a **single character anchor node** (the `character_media_id` concept); reuse the same `{{NodeKey}}` throughout—see character-consistency.
3. **Upload / register the product** as an anchor.
4. **Monologue script**: write the complete spoken script, corresponding step by step to each usage step.
5. **Storyboard panel generation**: set the panel count based on duration (see below); `generate_image_v3` generates panels **serially** (later panels reference earlier ones to maintain coherence)—**21:9 horizontal strip containing 4 vertical 9:16 slots**, each slot with a "Step N — Heading" caption.
6. **Per-shot prompt writing + generation**: write Seedance-style prompts for each panel in parallel (one batch); submit `generate_video_v3` **in one parallel batch**; `reference_nodes` referencing the persona / product / storyboard panel anchors.
7. **Stitching**: N≥2 segments via `composite_video` (see montage); voiceover via `generate_audio`.
8. **Report**.

## Duration → Panel count

Total durationPanel count N4–15s116–30s231–45s346–60s4

(Steps = 4 × N; step numbering is globally continuous across panels.)

## Persona generation rules (Step 2 in depth · shared across the UGC family)

The influencer anchor must have the look and feel of a **real phone selfie**, not a magazine portrait:

- **Composition**: arm-extended front-camera selfie, head and shoulders filling the frame, slightly off-center / imperfect framing (not posed, not studio-centered); the phone-holding hand / wrist may faintly appear at the edge of the frame.
- **Realism**: keep phone-sensor grain and skin pore texture; no retouching, no skin-smoothing filter, no studio lighting / professional sheen; subject sharp, background naturally blurred.
- **Clothing**: fully covering the chest / torso, no logos, no visible text.
- **Lighting / environment**: soft cool-neutral daylight (side window), clean, no warm tones, no flattering halo.

## Hand count / POV rules (shared across the UGC family · critical)

- The character has **exactly two hands**.
- **Selfie POV**: one hand holds the phone (off-frame or faintly visible at the edge), the other hand performs the action—**never hold two objects at once in selfie POV**.
- Actions that need **both hands** (e.g., steps that actually operate / use the product) → switch to **Tripod POV** (phone not in frame).
- POV may switch between shots / slots; switches are **aligned hard cuts**.

## Shot / rendering rules

- Each slot = one usage step being demonstrated; photographic-style UGC, natural light, casual realism.
- Demonstrated steps progress in actual usage order; in-slot actions match that Step's Heading.
- **Grip physics**: the product's heaviness / lightness rendered as the real object would behave; grips and load-bearing must be realistic.
- When the product is shown, **label facing forward, no rotation**, exactly one product in frame.
- **Energy tone**: high-energy influencer by default, **adjustable to the brand's tone** (no forced exaggerated shouting).
- No mirror / reflection shots; no deformed hands / third arms; **no extra text / brands / logos on screen** (except the "Step N" step captions).

## Key rules

- **English-only**: captions, monologue, and CTA all in English; step captions use the "**Step N — Heading**" format with an **en-dash (—) separator**.
- **Product usage analysis is mandatory**: steps are derived from the real usage flow, not invented.
- **CTA tail** (last ~0.5–1s of the last cell of the last panel): influencer on camera + gesture + "Link in bio" / "Subscribe!".
- **Persona identity lock**: a single character anchor node runs through the whole video; do not regenerate the influencer per shot.
- **Panels serial, clips parallel**: storyboard panels are generated serially (for coherence); Seedance clips are submitted in one parallel batch.
- **Opening word constraint**: the first spoken word must **not** start with fillers like OK / Okay / So / Um—go straight into the hook.
- **Audio / stability**: slight handheld shake for selfie shots, locked static frame for tripod shots; the final video has no on-screen text, no subtitles, no watermark (step captions excepted).
- Seedance per-shot default `count: 2`.

## Companions (queries must load these together / also this skill's evaluation portfolio)

RelationTargetPurposeRequired?provenanceDepends onproduct-analyzerproduct usage analysis, deriving step_captionsrequiredsource-nativeDepends onimage-generationpersona / product / storyboard panel image generationrequiredsource-nativeDepends onvideo-generationper-shot generationrequiredsource-nativeDepends onmontageN≥2 stitching (the montage source text explicitly lists ugc-\* calling this skill when N≥2)required when N≥2source-nativeDepends oncharacter-consistencyinfluencer identity lockrequiredsource-native

Boundary (rerouting, not dependencies): product as the protagonist → ugc-product-flow; try-on → ugc-try-on-flow; unboxing → ugc-unboxing-flow; talking-head review (no step-by-step demonstration) → ugc-flow; model-swap recreation → ugc-model-swap.

## Related

Talking-head review base → ugc-flow; product as the protagonist → ugc-product-flow; try-on → ugc-try-on-flow; unboxing → ugc-unboxing-flow.