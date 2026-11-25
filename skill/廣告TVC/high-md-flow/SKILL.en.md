---
name: high-md-flow
description: "High-energy brand motion graphics: peak stunt camera work for explosive brand blockbusters"
---

# high-md-flow

Use this skill when making high-energy / hyper-dynamic (kinetic / hyperkinetic) brand reels—peak action, wild camera moves, smash cuts—for brand films that need explosive power, such as sports / fashion drops / tech unveils / SaaS reveals. Three-stage progression.

**Positioning of the high tier**: hyperkinetic chaos. Motion comes primarily from the explosive action of camera and subject—the exact opposite of classic-md-flow's "steady, restrained internal choreography." The storyboard / clip rules below are calibrated to this; any language such as drift locks, slow elegant glides, or imperceptible micro-dollies does not belong in the high tier (that is the language of classic / typography / infographic—mixing it in breaks the energy level).

## Three Stages

1. **Style board (Stage A)**: If an image exists as a base, upload it (`upload`) and skip the style board; if not, use `generate_image_v3` (optionally `style_display_board`) to produce a 4-panel style board with style prompts leaning "high dynamics / high energy." The user selects one frame (`ask_human`) as the visual-world base; ignore the remaining candidate frames.
2. **Storyboard (Stage B)**: Using the selected base as the reference, `generate_image_v3` (`storyboard_panel`) produces a 6-panel storyboard, referencing the base frame.
3. **Motion clip (Stage C)**: `generate_video_v3` generates a continuous clip with the storyboard as reference; for multiple segments, composite them with `composite_video`.

## Storyboard Rules (Stage B Deep Dive)

- **Grid and base**: 6 panels in a 3×2 horizontal layout (top row 1-2-3, bottom row 4-5-6), whole board 3:2; thin hairline separators between panels (1pt / 12-20px gaps), no borders within panels, clean imagery (remove dates / fake data chips / Latin sub-captions / monospace timecodes / metadata labels). The frame selected from the style board serves as the visual-world base for the entire board.
- **Text floor**: any text inside a panel must be no smaller than roughly 10-12% of the panel height (cap-height); small Latin sub-captions / monospace timecodes must all be removed.
- **Peak-action mandate (PEAK-ACTION)**: every panel freezes at the apex of an action—the top of a jump, a splash, a shatter, an explosion, a motion-streak instant. No static subjects, no resting states, no "product in an empty scene."
- **Ambient density mandate (AMBIENT DENSITY)**: at least 2 layers of atmospheric fill behind the subject in every panel—① drifting particles (sparks / dust / streaked particles / haze) ② background gradient breathing (color-grade saturation cycles) ③ volumetric beams (rim light / god rays / spotlight) ④ surface texture (concrete / sand / liquid surface / mirror floor) ⑤ foreground depth elements (out-of-focus props in front of the subject).
- **Text anchors (Pattern A · odd-panel pattern)**: panels 1 / 3 / 5 carry a 2-4 word display headline (display typeface); panels 2 / 4 / 6 carry no text—pure peak atmosphere. Copy is generated from the project theme; no fixed boilerplate sentences.
- **Six-panel content arc (one peak + one stunt camera move per panel, calibrated panel by panel)**:
  - P01 Hook (0-2.5s) · CRASH-OUT REVEAL: instant cut from extreme-close-up detail to a wide shot as the subject leaps (apex); paired with whip-pan motion smear + a freeze-frame hold; carries the first display headline.
  - P02 · SHATTER PUSH-THROUGH (2.5-5s): the camera pushes through a membrane while the subject bursts out at the instant of shattering; refracting debris + chromatic-dispersion edges; no text.
  - P03 · VERTIGO PULL (5-7.5s): the subject jumps vertically to its apex while the camera runs a synchronized dolly-zoom; speed ramp + lens streaks; carries the second display headline.
  - P04 · DROP-DIVE PAST (7.5-10s): the camera dives vertically past a falling / spinning subject; a vortex inside the particles + a slightly warped funnel; no text.
  - P05 · HYPERKINETIC ORBITAL SWEEP (10-12.5s): the camera orbits at high speed around the subject mid-burst / mid-splash; shockwave rings + refractive mist; carries the third display headline.
  - P06 Resolution (12.5-15s): final wide shot, the subject settles into a clean hero silhouette, leftover particles sink; lingering haze + soft volumetric beams; no text.
- **Five locks (consistent across panels; write them into the prompt and restate them panel by panel)**: subject lock (the base's hero subject / motif), material lock (replicate the base's primary material identity), style lock (Tier-1 premium motion, 3D / 2.5D polished hyperkinetic-chaos tone), color lock (pull about 3 dominant hex colors from the base), atmosphere lock (replicate the base's lighting mood + haze density + depth of field).
- **No photoreal humans (HR-3)**: photorealistic humans / ARRI Alexa / 35mm grain / real-skin texture are strictly forbidden. Replace with silhouettes / abstract forms / stylized 3D / 2D illustration / motion-streaked figures / particle figures / lit volumetric silhouettes. Photoreal texture is exempted only for product-md-flow.

## Motion Clip Rules (Stage C Deep Dive)

- **Form**: one continuous full-frame 16:9; the storyboard serves only as a planning reference, not a panel grid; every shot fills the full frame.
- **Camera tone (core of the high tier · HYPERKINETIC CHAOS)**: one peak-action moment per shot (jump apex / splash / shatter / explosion); never drift locks, slow elegant glides, or imperceptible micro-dollies. Camera vocabulary—VERTIGO PULL (about 2m push-in with simultaneous zoom-out), CRASH-OUT REVEAL (extreme close-up cut to wide within 0.4s, about 3m pull-back), SHATTER PUSH-THROUGH, high-speed ORBITAL SWEEP, DROP-DIVE PAST (about 6m), MATCH-FRAME SWING (about 90° pendulum arc), WHIP-PAN (motion-smear whip). Speed ramps allowed (slow motion → extreme speed) + an about-2-frame freeze-frame hold at the moment of impact. Strong parallax: displacement ratio of about 100 / 40 / 15 across foreground / midground / background.
- **6-shot arc**: about 2-2.5s per shot, one peak action paired with one stunt camera move (e.g., ① abstract-material hero CRASH-OUT + 0.2s whip-pan; ② kinetic-environment VERTIGO PULL 1.5s + 180° orbit; ③ hard-surface macro-to-wide MATCH-FRAME SWING 90° + flash freeze; ④ architectural / abstract depth-corridor DROP-DIVE PAST 6m; ⑤ energy-core ORBITAL SWEEP 120° + push-through; ⑥ final hero frame VERTIGO PULL 0.8s → lock). Use hard-impact transitions between shots: push-through / hot-spot light sweep / object morph / inward collapse / particle dissolve (no cross-fade).
- **End-frame freeze**: force the final frame to hold from 13.7-15s, pixel-identical, no new action / elements / transitions / fades.
- **Audio**: kinetic SFX mix only—sub-bass impacts / glass collisions / prism shimmers; no music, no VO, no dialogue, no auto-captions.

## Aspect Ratio Defaults and General

| Step | Default ratio |
|---|---|
| Stage A style board | `3:2` constant |
| Stage B storyboard (3×2 six panels) | 16:9→`3:2` / 9:16→`9:16` / 1:1→`1:1` |
| Stage C clip | `16:9` default, ask if unspecified |

Stage C generation defaults to `count: 2` (two variants of the same prompt). If images are used as the base, skip the style board. The creative work for Stage B/C (storyboard / clip prompts) lives in the backend enhancer upstream; in this environment the agent writes it itself—the board grid discipline and hyperkinetic camera tone craft are already inlined in the previous two sections, not outsourced.

## Companions (queries must load these too / they are also this skill's evaluation combos)

| Relation | Target | Purpose | Required? | provenance |
|---|---|---|---|---|
| Dependency | image-generation | style board / storyboard board image generation | Required | native |
| Dependency | video-generation | Stage C shot-by-shot generation | Required | native |
| Dependency | montage | multi-clip assembly | Required for multi-clip | native |

Boundaries: classic motion → classic-md-flow; product ads → product-md-flow; typography motion → typography-md-flow; infographic motion → infographic-md-flow.

## Related

Classic → classic-md-flow; product ads → product-md-flow; typography → typography-md-flow; infographic → infographic-md-flow. (Same motion-design family, sharing the 6-cell board + three-stage pipeline; the high tier pushes camera-move energy on top of it to peak action / hyperkinetic chaos.)