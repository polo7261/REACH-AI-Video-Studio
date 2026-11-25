---
name: time-stop-cinematic-vfx
description: "Time-stop VFX short: snap your fingers and everything freezes, the hero walks alone in a still world—one shot, three segments, cinematic VFX."
---

## name: time-freeze-effect\\

namespace: industry\
title: "Time-Freeze Effect Video"\
description: "Generate a cinematic 'time-freeze' effect video — one snap of the fingers and the scene stops dead, the protagonist moves through the frozen world, and another snap brings time back. Upload a protagonist reference image to keep the look consistent throughout, and customize the scene / frozen-moment visual / closing line / aspect ratio and duration. Complete the three phases 'freeze → walk-through → restore' together with the matching sound arc within a single take. Use generate_video_v3."\
version: 1

# time-freeze-effect

Use this skill when making "time-freeze" effect short videos. Classic structure: **time in the scene stops abruptly → the protagonist is the only person still moving, walking through the frozen world → a snap / a line of dialogue brings time back**. Upload a protagonist reference image; the look stays consistent throughout. Completed in a single continuous take, via image-to-video.

> Adaptation for this environment: image-to-video goes through `generate_video_v3` (references the protagonist image, generates embedded sound effects); source is MIT, wording rewritten, not 1:1.

## Inputs

- **Protagonist reference image** (required): A clear photo of the face/body with the face visible; the look must stay consistent throughout the video.
- **Scene** (optional): The environment where time will freeze. Scenes with **strong crowd energy and lots of small objects in the air that can be "frozen"** (liquids, confetti, sparks, popcorn) work best — crowded, dimly lit, neon-lit sports bars / nightclubs / wedding venues / stadium crowds.
- **Frozen-moment visual** (optional): The signature image suspended in mid-air at the instant time stops (a suspended golden arc of beer / floating, motionless popcorn / crowd faces frozen mid-cheer).
- **Closing line** (optional): A word / short phrase the protagonist whispers before restoring time.
- **Aspect ratio**: 16:9 cinematic / 9:16 vertical for social media.
- **Duration**: 10 or 15s (10s recommended for vertical social media — tighter pacing).

## Craft: one take, three phases + snap mechanism + sound arc

**The three-phase structure is completed within a single take**, via image-to-video (reference the protagonist image, 720p, embedded sound enabled).

**Hyper-real cinematic grade (throughout the whole video)**: hyper-real texture emulating a cinema camera + 35mm lens, volumetric haze, dynamic hard shadows, shallow depth of field. This look is the prerequisite for a believable "frozen world" and must not be skipped.

Three-phase timeline:

1. **Normal state & trigger**: The opening scene runs in normal time; a frontal Steadicam medium shot tracks the protagonist confidently moving through the crowd, which erupts in cheers around them; the protagonist raises their right hand and snaps their fingers.
2. **Freeze**: At the instant of the snap, a spherical shockwave bursts from the fingertips — the air distorts and light refracts in ripples spreading outward; everything stops dead mid-motion; the frozen-moment visual hangs in the air (liquid arcs / floating particles / frozen expressions); neon light illuminates the suspended dust and liquids; absolute silence.
3. **Walk-through**: Only the protagonist moves; footsteps are soft with a slight echo; the camera pulls back, following the protagonist as they calmly move through the frozen scene, observe, and pick one suspended detail out of the air.
4. **Restore**: The protagonist stops in front of an ecstatic, frozen bystander, tilts their head to study them, and whispers the closing line; then turns to face the camera with a mischievous grin and snaps once more — a stronger reverse shockwave spreads outward and motion instantly resumes (the sound blasts back, people frozen mid-jump land); the protagonist walks away as the camera pushes through the crowd celebrating anew. Fade to black.

**Sound arc (the signature of this effect; embedded sound must be enabled — never mute)**: deafening ambient celebration → snap → deep shockwave / low-frequency rumble → absolute silence → footsteps → whisper → snap → reverse shockwave → celebration blasting back. This "snap → silence → snap" sound arc is the soul of the whole effect; if muted, the effect collapses.

**Protagonist consistency**: Explicitly bind in the prompt that "this person comes from the reference image; facial features and body proportions stay consistent across every shot of the video." If the model refuses photorealistic faces, fall back to a looser identity-matching setting (not strictly bound to photorealistic likeness) and regenerate.

## Workflow

1. Receive the protagonist image + scene / frozen visual / closing line / aspect ratio / duration; if the protagonist image is missing, ask for it first.
2. `generate_video_v3` image-to-video: bind the reference image to the protagonist; write the prompt clearly along the three-phase timeline above (normal-state trigger → freeze → walk-through → restore); spell out the snap's spherical shockwave and the reverse shockwave; spell out the specific suspended visuals of the frozen moment; spell out that set of hyper-real cinematic-grade parameters; write the sound arc into the prompt as a sound design paragraph; enable embedded sound; 720p; aspect ratio / duration per the inputs.
3. Present the finished video; the scene / frozen visual / line can be adjusted and regenerated.

## Related

One-take / first-frame-chained continuous short videos → one-shot-continuous; general camera-move effect vocabulary → cinematic-motion-language; person-swap / theme-transformation effects → theme-transformation-fx / ugc-model-swap.

&lt;!-- This skill is self-contained, with no source-native cross-skill dependencies, hence no "companion" declaration table. The "Related" above is only a boundary-rerouting hint, not a dependency. --&gt;