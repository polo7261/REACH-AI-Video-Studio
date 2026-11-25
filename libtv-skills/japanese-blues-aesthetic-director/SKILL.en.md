---
name: japanese-blues-aesthetic-director
description: "Japanese realistic blues fresh-style director: create blues-toned fresh campus dramas or character mood pieces, daily campus and city short films"
---

# Japanese-Style Realistic Blue-Tone Fresh Live-Action Director

## 1. Delivery Goals

Transform the user's theme, story, reference images, or existing assets into images or videos that feel real, light, quiet, restrained, and breathable. Let characters belong to real spaces, and let emotion happen through time, movement, environment, and sound—not through filters, staged setups, or exaggerated acting.

First distinguish between the two types of delivery; do not mix up the terms:

- **Complete Production Plan**: delivers the creative concept, assets, per-shot first frames, per-shot prompts, editing, and review files, ready to proceed directly into generation.
- **Complete Final-Film Execution**: when available tools allow, continue on to complete asset generation, per-shot selection, editing, sound, color grading, and export; when nothing has actually been generated or exported, do not claim "the final film is complete."

When the user asks for a "complete video," a "finished film," or content of 30 seconds or more, you must not end after delivering only one idea, one first frame, or one long prompt.

## 2. Inputs and Minimal Follow-Up

First extract: theme, application scenario, duration, aspect ratio, characters, location and time, emotional shifts, reference assets, specified model, dialogue/voiceover, music, subtitles, and delivery type.

Ask follow-up questions only when one of the following gaps would materially change the result, consolidated into at most 1 round of 1-3 questions:

- A formal final film is missing duration or aspect ratio.
- Only abstract feelings are given, with no visible subject, state, or scene.
- Reference images clearly conflict in characters, clothing, lighting, or space.
- Ambiguity about multi-person left/right positioning, first/last frames, or ownership of key props.
- The user requests precise dialogue sync but provides no lines or speakers.

Fill all other gaps with restrained defaults and state the assumptions. For functional testing only, when the user has specified nothing at all, you may default to `15 seconds, 16:9, no subtitles, unified BGM in post`; formal deliveries must not silently apply the test defaults.

## 3. Hard Style Boundaries

Must do:

- Low-saturation blue-gray, pale cyan, milky white, natural wood tones, and a small amount of realistic pale-yellow lamplight.
- Blue hour, overcast diffuse light, early-morning window light, or mixed warm-cool light after rain.
- Real skin, fabric, glass, wet ground, and traces of everyday use.
- Clear relationships between people and space; backgrounds retain narrative information.
- Normal real-time speed, natural micro-movements, and motivated, restrained camera movement.
- Detail within slowness, change within stillness; emotion undergoes at least one visible but slight shift.

Must avoid:

- Influencer-style photoshoots, saccharine "sugar-water" shots, sweet-romance idol dramas, and MV-style hard beat cuts.
- High-saturation pink-blue, cyber neon, painting the whole frame blue, and pathologically cyan skin tones.
- Glass skin, excessive skin smoothing, studio shots, exaggerated backlighting, and frame-filling halos.
- Unmotivated slow motion, floaty camera moves, orbiting shots, frequent zooms, and template transitions.
- Loud crying and laughing, stagey acting, and repeated use of the same action and shot size.

For style judgment, subject-matter variants, and scoring rules, read 01\_Style System and Subject Boundaries.md.

## 4. Progressive Disclosure Routing

Read only the files the current task requires; for complete videos, read according to the mandatory items below.

Task Required files Single image, image series, reference-image conversion `01, 03` 5-second single shot `01, 03, 04` + corresponding model `05` or `06` 15-second short film `01, 02, 03, 04, 09, 10` + corresponding model; read `07` when sound is needed 30-90 second complete production plan `01-04, 08-11` + `05` or `06` + `07` Actual generation and final-film execution All files of the complete production plan, and loop through the review and remediation of `10` Test Skill Choose from `12-16` the cases closest to the task, do not load all of them

Reference files:

- 02\_Complete Workflow and Delivery Status.md
- 03\_Assets and Per-Shot First Frames.md
- 04\_Pacing, Camera Moves, and Cutting.md
- 05_Seedance2 Execution Specification.md
- 06\_Kling Execution Specification.md
- 07_BGM, Sound, Editing, and Color Grading.md
- 08_VibeCreating Translation.md
- 09\_Continuity and Multi-Person Scenes.md
- 10\_Failure Remediation and Final Review.md
- 11\_Complete Project Output Template.md
- 12\_Complete Test Prompts.md: Tests the 60-second complete production loop.
- 13_15-Second Test Case.md: Tests the three-shot high-stability structure.
- 14_60-Second Complete Test Case.md: Verifies action breakdown, duration, and continuity.
- 15\_Copyable Prompt Examples.md: Read when templates or syntax examples are needed.
- 16\_Regression Test Matrix.md: After modifying the Skill, choose 3 categories of regression tests.

## 5. Dual Layers of Creative and Execution

First judge whether the input suits Vibe Creating. Character emotions, slices of daily life, memories, and travel experiences can be distilled; for precise dialogue, industrial work orders, functional demonstrations, or when the user explicitly asks to keep parameters, retain the original structure and do not force it into prose.

### Creative Layer

Generate one creative master sentence:

```text
Visual anchor + character state/main action + 2-4 visual or sound motifs + application scenario + one slight emotional shift
```

Do not invent character relationships, secrets, twists, or plot points the user never provided.

### Execution Layer

Break the master sentence into a style bible, segments, assets, shots, first frames, start/end states, model prompts, sound, and review items. User-specified dialogue, voiceover, lyrics, music, sound effects, duration, aspect ratio, structure, and model are preserved with priority.

For detailed routing, read 08_VibeCreating Translation.md.

## 6. Complete Production State Machine

```text
Brief locked
→ Creative master sentence and emotion curve
→ Style bible
→ Character/scene/prop asset lock
→ Segments and final-film timeline
→ Per-shot production sheet
→ Full-film first-frame contact-sheet check
→ Per-shot first frames/last frames
→ Route model per shot
→ Batched generation and selection
→ Rough cut and continuity repair
→ BGM/ambient sound/subtitles/color grading
→ Technical check and export
```

Mark each stage as `Pending / Completed / Needs Rework`. When a problem is found, first return to the nearest upstream node to fix it; do not keep piling on negative prompts to mask errors.

## 7. Shot Budget and Duration

Each generated shot contains at most:

```text
1 main character action + 1 environmental event + 1 primary camera movement
```

Treat picking up, passing between hands, opening, and walking as different main actions; prop handoffs must be explicitly split into separate shots—you cannot have the previous shot "not yet holding the umbrella" and the next shot directly "already holding the umbrella open."

Record two kinds of duration simultaneously:

- **Generation duration**: choose a tier currently supported by the model interface and leave headroom before and after the action.
- **Final-film usage duration**: written into the edit timeline; the sum of all shots must equal the target duration.

Seedance execution prompts never state absolute seconds; seconds are kept only in the director's sheet and the edit sheet. For action complexity, 5-second beats, and long-film waveforms, read 04\_Pacing, Camera Moves, and Cutting.md.

## 8. Per-Shot Model Routing

- **Kling first**: bringing a high-quality single first frame to life naturally, realistic character micro-movements, wind/rain light and shadow, light tracking shots, or first/last frame transitions.
- **Seedance 2.0 first**: multimodal asset binding, multiple subjects, explicit spatial relationships, shot order, dialogue/sound-effect notation, and engineering-grade delivery.
- **Finish in post**: pacing, transitions, BGM, subtitles, and overall color grading for 30 seconds and beyond, without relying on a single model generation.

Mixing models per shot within the same project is allowed, but each shot outputs only the executable version for its corresponding model, and its source is recorded in the project sheet; do not write Seedance binding syntax into Kling prompts. For any Multi-Shot, first/last frame, or native audio feature that depends on a specific version, verify the current interface first; if the capability is unavailable, fall back to per-shot mode.

High-stability defaults: 5-second single-shot generation; 15 seconds split into 3 independent shots; 30-90 seconds generated entirely shot by shot. Full-length Multi-Shot is for efficiency testing only, never the sole deliverable.

## 9. Prompt Invariants

- Output Chinese prompts only by default; attach an English version only when the user explicitly requests it.
- Every independently submitted prompt must be self-contained, not relying on subject definitions or state memory from the previous prompt.
- Seedance subjects use either "direct binding" or "define first, then reuse"—never a mix of both.
- Leave a space before all plain `@ImageN / @VideoN / @AudioN`; never split inside `<SubjectN>@ImageN`.
- Each shot describes only one camera movement; do not write conflicting camera position changes.
- BGM is laid uniformly in post by default; per-shot videos only request the necessary ambient sound.
- No-subtitle tasks carry no-text, no-watermark, and no-logo constraints; subtitles are added only in post.
- Prompts finally sent to the video model contain only executable content, with no diagnostics, template explanations, or "optimization questions" mixed in.

## 10. Batched Delivery to Prevent Truncation

For 30-90 second projects, prioritize generating files or batched output:

1. `Project master table + style bible + asset cards`.
2. `Timeline + full-film continuity master table`.
3. `First frame + video prompts` for 4-6 shots per batch.
4. `Sound edit + failure remediation + final review`.

Reload the project master table at the start of each batch, and update completed shots and the next batch's starting state at the end. Do not deliver only the first few shots and then declare completion due to message length. Read the structure from 11\_Complete_Project_Output_Template.md.

## 11. Complete Video Exit Conditions

The complete production plan may only conclude when all of the following items are satisfied simultaneously:

- Target duration, aspect ratio, delivery mode, and default assumptions are defined.
- There is a creative thesis sentence, a style bible, an emotion curve, and a unique visual motif group.
- There are asset cards and reference mappings for characters, scenes, and props.
- The total shot durations used in the final film are accurate.
- Each shot has a unique function, start and end states, action, environmental event, camera movement, and cut motivation.
- Each shot has an animatable first-frame or first-and-last-frame plan, plus a self-contained prompt for the corresponding model.
- Prop handoffs, open/close states, character orientation, and light progression all have explicit transitions.
- There are unified BGM, ambient sound, subtitle strategy, color grading, and export specifications.
- There are A/B/C versions, pickup shots, and failure fallback paths.
- The hard-failure checks and scoring thresholds in 10\_Failure_Remediation_and_Final_Review.md are passed.

Executing the complete final film must additionally satisfy: footage has been generated and selected, the edit timeline has been implemented, sound and color grading have been completed, and the final file has been exported and actually reviewed.

The final result should feel like a moment of real life quietly observed: the viewer's attention keeps moving, characters change in small but clear ways, and the ending leaves a lingering resonance—rather than a carousel of pretty photos.