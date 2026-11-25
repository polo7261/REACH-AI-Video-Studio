---
name: cinematic-motion-realism
description: "Realistic performance authenticity: say goodbye to plastic acting, inject true cinematic texture"
---

# cinematic-motion-realism

When you want realistic cinematic motion (not animation / motion graphics / UGC), use this skill to inject realism into video prompts. The full craft is inlined and self-contained — no other skills need to be attached.

> Adapted for this environment: Seedance 2.0 / MultiModalToVideo → `generate_video_v3`; realism directives such as material physics / environmental forces / restrained performance are embedded directly in the prompt text, with no separate tool calls. Embedded audio follows the SP format (sound effects `<>`, dialogue `{}`, subtitles `【】`, music `()`). Source: Seedance cinematic-grade prompt craft; the same engine applies in this environment.

## When to Use

Realistic bodily movement, natural human behavior, emotional close-ups (restrained performance), driving / intimacy / fights / action scenes, environmental interaction (wind, rain, water, drag, dust, gravity), and realistic motion generation. Stylized CGI / animation / motion graphics do not go through this skill.

## Core Principle: Realism Comes from Restraint, Not Spectacle

Five grounding pillars: ① **Bodily weight and physics** (actors have mass; movement has friction / momentum / contact force) ② **Environmental forces** (wind / water / gravity / fabric push back against the actor) ③ **Emotional restraint** (micro-expressions / held-back beats / breathing, no exaggerated telegraphing) ④ **Camera as observer** (the lens has its own physical presence) ⑤ **Continuity anchors** (light direction / wardrobe / time of day carried across shots).

## Six-Block Grounded Prompt Structure

`[Style & Mood] [Shot Direction] [Actor Behavior] [Environmental Force] [Camera Behavior] [Audio]`
1. **Style & Mood** (1 sentence): Photographer's vocabulary — '35mm anamorphic lens, naturalistic color, soft contrast' — no piling on adjectives. **No keyword soup** ('8k / masterpiece / trending'); replace it with technical description.
2. **Shot Direction** (1 sentence): Subject-verb-object + location; no adjectives that do no structural work.
3. **Actor Behavior** (2–3 sentences): **Must include** weight cues + one micro-action + one held-back beat. Use fluid transitional language, not disjointed actions like 'he runs then stops'. **Banned**: 'tears streaming down the face', 'he sprints wildly', 'a huge grin'.
4. **Environmental Force** (1–2 sentences): What pushes back against the actor — air / water / gravity / surfaces / light sources. Use physical relationships to trigger model inference (e.g. 'neon reflections on rain-wet asphalt'), not 'nice lighting'.
5. **Camera Behavior** (1 sentence): Default vocabulary — 'locked-off frame', 'slow breathing handheld', 'push in at walking pace'. Don't issue contradictory instructions in the same paragraph ('static camera' + 'orbit').
6. **Audio** (1 sentence): Ambience first, then voice, e.g. 'Ambience: interior sounds only. No dialogue, no music'. **Always write one audio line** — the engine generates audio natively; omit it and you get random sound that doesn't match the picture.

## Scene Patterns

- **Driving (in car)**: Locked-off or ultra-light handheld; hands at 9 and 3 on the wheel.
- **Emotional close-up (restrained)**: No tears, no telegraphed sadness; the performance lives in held-back beats and micro-actions.
- **Action (on-foot chase)**: Tight strides, shoulders leading; use fluid transitions, don't cram multiple actions into 4–5s.
- **Fight (limb specificity)**: Action = intent + named technique + **explicit limb** + contact point; never use vague terms like 'spinning kick' (the engine confuses left and right limbs) — write 'right leg front kick', 'left arm block'. The character taking the hit must be in **active response** (blocking / evading / countering), never passively frozen. Tension comes from **cut density**, not single-shot spectacle — for a multi-beat fight within one shot, partition by the second, one action per second, with aggressive shot-size variation (never two WIDEs in a row; every IMPACT lands on a CU/ECU).
- **Intimacy (restrained closeness)**: Built from 'non-action'; hold back the kiss / tears / whisper.
- **Environmental interaction (weather as a character)**: Wind should shape multiple elements (hair / coat / grass / seagulls).

## Continuity Anchors (multi-shot sequences; copy verbatim into every shot)

① Lighting anchor (same source, same direction) ② Wardrobe anchor (full description, identical wording) ③ Time-of-day anchor (explicit) ④ Geographic anchor (where the actor ended the previous shot) ⑤ Sound-bed anchor (same ambience signature). Avoid complex subject transformations within a single shot ('a person turns into a bird') — they break realism and temporal consistency.

## Submission Defaults and Failure Modes

Defaults: `aspect_ratio` 21:9 or 16:9; single-shot `duration` 6–10s (one action per beat, 10–15s for at most 3–4 beats); audio always on.
| Symptom | Cause | Fix |
|---|---|---|
| Floating movement | No bodily weight cues | Add weight/mass cues |
| Static environment | No environmental force | Add wind/gravity/surfaces |
| Overacted face | Used 'cry/rage' verbs | Swap for micro-actions |
| Flying camera | 'sweeping/epic' | Swap for concrete camera vocabulary |
| Studio look | No environmental force + no audio | Fill in blocks 4 and 6 |
| Continuity drift | Anchors not copied | Copy all five anchors into every shot |
| Muddy fight action / wrong limb | Vague technique words, single-shot overload | Named limb + contact point, one action per segment |
| Audio mismatch | Audio instruction omitted | Add the audio block (engine generates audio natively) |

## Usage

Write the above into the `generate_video_v3` prompt; prioritize realism-oriented description over stylized description. For multi-shot sequences, copy the continuity anchors verbatim into every shot.

## Related (boundaries, not dependencies)

Seedance comprehensive prompt architecture (operating laws / preset library / archetypes) → seedance-director; model-agnostic camera-movement vocabulary → cinematic-motion-language. Both are sister-craft references; this skill is self-contained and does not depend on them. If a combination is needed, they are loaded together via the user query.