---
name: cartoon-flow
description: "2D animation director: any story, one click to a cartoon animation"
---

# cartoon-flow

Use this skill when producing 2D / 2.5D stylized animated videos (cartoons, anime style, non-realistic characters). From single-segment to multi-segment stories, proceed stage by stage; each stage's output feeds the 13 tools.

## Stages

1. **Scene/Story Analysis**: Clarify the story, characters, scenes, and props (structured output below).
2. **Style Definition**: Establish a unified animation art style (using the "style formula" below) as the visual baseline for the whole piece.
3. **Anchor Design Sheets (two steps: base first → then stylize)**: Never do cartoon assets in one pass. First use `generate_image_v3` to produce a **neutral base image** of the character/scene/prop (structure, proportions, and composition correct; template below), then use it as reference to **stylize** into the art style from Step 2. The `tag` maps to character/scene/prop, and the stylized image serves as the cross-shot anchor; for character consistency see character-consistency.
4. **Storyboarding**: For multi-segment stories, split shots according to the SP shot-splitting principles (CLIP fields below), defining pacing and clip head-to-tail handoffs.
5. **Shot-by-Shot Generation**: Generate shot by shot with `generate_video_v3`; reference the corresponding anchors via `reference_nodes` and bind them through `{{NodeKey}}` in the prompt; single shot ≤15s; count locks below.
6. **Compositing**: For multi-segment pieces, stitch the final video with `composite_video` (see montage, `Skill("montage")`).

## Scene Analysis Structure (Stage 1 depth)

Analysis output: narrative summary; **characters** (shorthand for cross-module reference, gender, age bracket, whether from uploads); **scenes** (shorthand, indoor/outdoor, time of day); **candidate props**; style preset inclination + rationale; total duration; **format path** (single-video for a single segment / multi-clip for multiple segments) + rationale for the choice. Shorthands persist through all subsequent stages — never rename them midway.

## Style Formula (Stage 2 depth)

Write the art style as a single-line formula, always assembled from these fixed segments:

> **[Art-style base]** animation, referencing **[style reference]** — [linework technique], [coloring technique], [palette], [accent effects], [background treatment], [animation rhythm/timing], [camera description]

- Each segment is requirement-driven; when it cannot be mapped or input is missing, fall back to the generic default (modern 2D hand-drawn + hand-inked lines with varying weight + three-value flat cel with hard shadows + saturated earth tones + halftone dots in shadow areas + hand-drawn line boil, action on twos + 24fps).
- **Applies only within 2D / hand-drawn / cartoon territory**; pixel, 3D, and photorealistic styles are out of scope.

## Base Description Templates (Stage 3 base step)

- **Character base**: age & gender + expression → hairstyle → body type & build → facial details → clothing (top→bottom→shoes; no logos/text, full coverage, realistic wrinkles at elbows/waist/knees, clean silhouette) → pose; **full-body standing portrait**, plain-color background with soft frontal diffuse light, margin above head and below feet, no props/no scene.
- **Scene base**: identification line → architecture (walls/floor/key structures/furnishings/spatial layout: left…right…background…foreground…) → lighting → atmosphere → static wide establishing shot (foreground anchor + background anchor); **empty-scene lock**: no people/silhouettes/motion, 16:9 horizontal.
- **Prop base**: identification line → material/surface details/features → isolated product-shot composition, plain-color background with diffuse light from above; **isolation lock**: no people/no hands/no other objects/no scene; usually 1:1.
- **Stylization step**: keep the base's identity/spatial layout/shape exactly unchanged, **changing only the rendering** to the style formula's art style.

## CLIP / beat Structure (Stage 4 depth)

Each CLIP records: narrative function (establishing / inciting incident / rising / climax / resolution), the character's want (Want), location + location mode (locked / transition), transition type, **camera mode** (single locked / multi-cut locked / parallax scroll), **audio mode** (ambience / narration / action / dialogue), character & prop locks, scene description, framing, climax marker (climax-token), **end state** (the character's final pose/position/expression at the end of the shot, with spatial position).
Within a CLIP, split further into **beats** (each beat: want / framing hint WS·MS·CU / prose description / climax marker / **spatial anchor**).
**Cross-shot continuity**: bridge via "spatial-anchor vocabulary + the previous shot's spatial anchor" (bridge-rule), so character position/orientation never jumps.

## Per-Shot Count Locks (Stage 5 depth)

Lock explicitly in the generation prompt: this shot has **exactly N characters** — no extra characters/passersby/background crowds, a single instance per character, never cloned/duplicated/appearing twice in the same frame; **props unique** (a single instance of each narrative prop); **scene locked** (all action in the shot happens within this location, no switching spaces).

## Principles

- One unified animation art style across the whole piece; no drift across shots.
- Key decisions such as the style formula and shot beats are made yourself per SP directing experience — never outsourced.
- Pause points: proceed to generation only after the style design sheets and the storyboard are confirmed (see SP).

## Companion Skills (loaded together with the query / also this skill's evaluation set)

| Relation | Target | Purpose | Required? | provenance |
|---|---|---|---|---|
| Dependency | image-generation | Base images + stylized anchors | Required | native |
| Dependency | video-generation | Shot-by-shot generation | Required | native |
| Dependency | montage | Multi-segment stitching (source shell Phase 6 explicitly states `Skill("montage")`) | Required for multi-clip (N≥2) | native |
| Dependency | character-consistency | Cross-shot character anchoring | When characters recur | native |

Boundaries (each has its own dedicated technique system; when matched, reroute to the standalone skill — these are not dependencies): Miyazaki-style hand-drawn (cel texture / natural vitality / flight and wind / color slots / visual state ledger) → ghibli-anime-style; needle-felt animation (needle-felted materials replicating reality / three-tier form grading / in-shot time segmentation) → needle-felt-animation; ink-wash wuxia animation (five-element color burst states / four-grid scenes / style–motion tension coupling / ink-wash emotion externalization) → ink-wuxia-animation; 90s magical girl (everyday/transformation dual forms / two-layer worldview / ritualized transformation sequence / villain visual hierarchy) → mahou-shoujo-90s.

## Style Specializations (each has its own technique system — go directly to the standalone skill)

This skill is the general 2D/2.5D animation pipeline; the following styles each have their own unique technique systems (style homage, not exact imitation). On a match, prefer the specialized skill:

- **Miyazaki-style hand-drawn** (cel texture / natural vitality / flight and wind / color slots / visual state ledger) → ghibli-anime-style
- **Needle-felt animation** (needle-felted materials replicating reality / three-tier form grading / in-shot time segmentation) → needle-felt-animation
- **Ink-wash wuxia animation** (five-element color burst states / four-grid scenes / style–motion tension coupling / ink-wash emotion externalization) → ink-wuxia-animation
- **90s magical girl** (everyday/transformation dual forms / two-layer worldview / ritualized transformation sequence / villain visual hierarchy) → mahou-shoujo-90s