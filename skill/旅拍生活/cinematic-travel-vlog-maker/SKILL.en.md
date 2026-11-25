---
name: cinematic-travel-vlog-maker
description: "Travel-film master: turns travel locations, character references, and copy into cinematic travel short films"
---

# Cinematic Travel Video Master

## Skill Positioning

This is the root-level main Skill. It handles only routing, assignment, and gating; it does not carry the full creative details.

When executing, it must work in this order:

1. First, determine which type of problem the user is currently trying to solve.
2. Based on the "Main Routing Table", read one or more exact sub-Agent files; do not guess file names on your own.
3. The sub Skill then reads the exact rule files according to its own "Required Skill References".
4. After output is produced, read or use `agents/sub-agent-travel-quality-reviewer.md` to perform quality review.
5. If quality review fails, return to the exact sub-Agent files already read in this round to revise, looping at most 3 times.

Do not stop at the main Skill alone; whenever work enters concrete creation, assets, prompts, or delivery, you must read the exact sub-Agent files listed in the "Main Routing Table". Files under `subskills/` are rule references, not sub-Agent entry points; unless a sub-Agent explicitly names a specific file, do not treat guide files directly as entry points.

## Inputs

The user may provide:

- Destination, travel theme, short-video purpose, video aspect ratio, video duration, platform.
- Reference images of people, character images, three-view drawings, half-body photos.
- Real-scene reference images, scene asset requirements, prop asset requirements.
- Stories, essays, travel notes, excerpts from original works, narration copy.
- The video generation model, BGM generation model, voiceover generation model, resolution, and video prompt requirements they want to use.
- Cover, title, punchy quotes, platform promotion requirements.

Hard rules must be preserved and passed to all sub Skills.

## Main Routing

Choose one or more sub Skills based on the user's latest message. On each routing, you may only read the exact file names in the table below, and you must pass the user's requirements, existing materials, hard rules, and current stage to that file together.

| User Intent | Sub Skill File to Read First |
| --- | --- |
| Complete travel shoot, theme through to a finished film, project progress | `agents/sub-agent-travel-production-controller.md` |
| Story, essay, travel notes, original-work excerpt, narration, script adaptation | `agents/sub-agent-story-script-director.md` |
| Character images, character assets, three-views, half-body, character consistency | `agents/sub-agent-character-asset-director.md` |
| Seedance, Seedance2.0, fast, mini, 15-second video prompts | `agents/sub-agent-seedance-prompt-engineer.md` |
| Check, self-check, whether it passes, not satisfied, regenerate, evaluate assets or prompts | `agents/sub-agent-travel-quality-reviewer.md` |
| Cover, title, promotion, Xiaohongshu, Douyin, WeChat Channels, delivery | `agents/sub-agent-travel-delivery-archivist.md` |

### 1. Complete Travel Shoot Workflow

When the user wants "theme all the way to a finished film / complete travel shoot / travel blockbuster / travel shoot workflow / project progress":

First read `agents/sub-agent-travel-production-controller.md`.

This sub Skill handles stage planning, generation gates, user confirmation, and the credit-saving order.

### 2. Story and Script

When the user provides a story, essay, travel notes, an original-work excerpt, or narration copy, or asks for "more emotion / turn it into video / faithful to the original text / no drastic rewrites / convert to a script":

First read `agents/sub-agent-story-script-director.md`.

This sub Skill handles free adaptation, faithful scripting, narration, and the emotional curve.

### 3. Character Assets

When the user uploads character images, or mentions "character assets / three-views / half-body / character consistency / character continuity":

First read `agents/sub-agent-character-asset-director.md`.

This sub Skill judges whether the user's images can be used directly as character assets; if character assets must be generated, the fixed character-asset prompt must be used; after generation, the assets must be evaluated for acceptability, and if they fail or are risky, first ask the user whether to regenerate.

### 4. Seedance2.0 Series Prompts

When the user mentions "Seedance / Seedance2.0 / fast / mini / prompts / 15 seconds / storyboard prompts / video generation prompts":

First read `agents/sub-agent-seedance-prompt-engineer.md`.

This sub Skill has the user choose the specific Seedance2.0 series model and resolution, and writes complete prompts in the fixed format.

### 5. Quality Review and Rework

When the user asks to "check / self-check / whether it passes / not satisfied / regenerate / evaluate assets / evaluate prompts", or after any stage's output is complete:

Read `agents/sub-agent-travel-quality-reviewer.md`.

This sub Skill handles stage quality review, continuity checks, generation gates, and up to 3 rework loops.

### 6. Cover, Promotion, and Delivery

When the user mentions "cover / title / Xiaohongshu / Douyin / WeChat Channels / promotion / delivery / archiving":

Read `agents/sub-agent-travel-delivery-archivist.md`.

This sub Skill organizes the final plan, prompts, cover and title, platform copy, and the delivery checklist.

## Execution Order

If multiple stages match at the same time, unless the user explicitly asks for a later stage, start from the earliest missing prerequisite stage:

```text
Requirements brief
→ Story/Narration/Script
→ Character asset judgment or generation
→ Real-scene reference judgment or scene image generation
→ Timeline and material unit planning
→ Seedance2.0 series model and resolution selection
→ Video prompt generation item by item
→ Quality review
→ After user confirmation, generate images or videos
→ Cover and promotion
→ Delivery
```

## Generation Gates

Images and videos consume credits. Before entering image or video generation, the following must all be satisfied:

- The video aspect ratio has been asked about and confirmed; if the user has not chosen one, default to 16:9. Available ratios are 16:9, 9:16, 21:9, 3:4, 4:3, and 1:1.
- The video duration has been asked about and confirmed.
- The video generation model to be called has been asked about and confirmed.
- The script, narration, or visual narrative has passed quality review.
- Character assets have been judged usable; if new character assets were generated, the post-generation evaluation has been completed.
- When real scenes are involved, the user has been asked whether they will upload scene reference images; if the user does not upload, scene images must be generated first and quality evaluation completed — going straight into video generation is not allowed.
- Scene images must feature cinematic-grade lighting design, rich color, clear light-and-shadow layering, and a clean, stable visual texture; if they fail, rework first or ask the user.
- The timeline and the function of each material unit are already clear.
- The video prompts have been fully written in the target model's format and have passed self-check.
- When generating video materials, video audio generation must be enabled so that sound effects such as ambient sound, footsteps, wind, water, and rustling fabric are generated along with the visuals; generating BGM within video materials is still forbidden.
- Before the video is composited, BGM must already have been generated, and the user must have manually selected the BGM generation model; do not generate directly with a default model.
- If narration is needed, the user must first choose a voiceover generation model, and the voice design prompts must then be completed; voice prompts must be written in sufficient detail following "profession + character traits + voice characteristics + speaking pace", so that the narration has emotional ups and downs, pauses, and pace changes.
- The user has confirmed to continue generating, or the user's current request is explicitly to generate.

If character assets fail or are risky, do not continue generating videos; first alert the user to the specific problems, and ask whether to regenerate or to accept the current assets and continue.

## Quality Review Loop

Run this in every stage:

```text
Production → Quality review → Revision → Re-review → Pass → Next stage
```

If quality review fails, return to the exact sub-Agent files already read in this round to revise, looping at most 3 times. If it still does not pass on the 3rd attempt, stop advancing and explain to the user the sticking points, risks, and information that needs confirmation.

## Output

Depending on the current stage, output:

- Project progress check.
- Sub Skills read and executed.
- Current stage outputs.
- Quality review conclusions.
- Next-step suggestions.
- Questions requiring user confirmation.

## Self-Check

Before outputting, check:

- Have the exact sub-Agent files in the Main Routing Table been read, instead of creating directly from the main Skill alone?
- Has each sub Skill read the exact rule files according to its "Required Skill References"?
- Is it script and prompts first, then image and video generation?
- Has the user been asked about the video aspect ratio, video duration, and video generation model; and if no aspect ratio was chosen, is 16:9 used as the default?
- Has the BGM generation model been asked about, and has BGM been generated before compositing?
- When narration is needed, has the voiceover generation model been asked about, and has a detailed voice design been completed covering profession, character traits, voice characteristics, and speaking pace?
- When real scenes are involved, have scene reference images been asked about; and if the user did not provide any, were scene images generated and evaluated first?
- When generating video materials, was video audio generation explicitly enabled, with BGM generation forbidden within the materials?
- Have the user's hard rules been passed to subsequent sub Skills?
- Has quality review been completed; and on failure, was the loop kept to at most 3 times?
- When character assets are involved, has the judgment of "usable directly / needs generation / post-generation acceptability" been completed?
- When Seedance2.0 series prompts are involved, has the user been asked to choose the model and resolution?

## Ask User

You must ask the user in the following cases:

- The destination, characters, purpose, or whether narration is needed is missing — anything that would change the direction of the finished film.
- When no aspect ratio has been chosen, ask the user to choose from 16:9, 9:16, 21:9, 3:4, 4:3, and 1:1; if the user does not choose, default to 16:9.
- When video duration has not been chosen, it must be asked.
- When the video generation model has not been chosen, it must be asked; if it is the Seedance2.0 series, then have the user choose Seedance2.0, Seedance2.0 fast, Seedance2.0 mini, or another compatible model.
- When the BGM generation model has not been chosen, it must be asked; BGM must not be generated directly with a default model.
- When narration is needed but the voiceover generation model has not been chosen, it must be asked; the voiceover must not be generated directly with a default model.
- When narration is needed, detailed voice design prompts must be given first; generate only after the user confirms or adjusts them.
- When real scenes are involved, the user must be asked whether they will upload scene reference images; if the user does not upload, generate scene images first and evaluate them.
- When no resolution has been chosen, you may state that you will continue at 720p.
- When generated character assets fail or are risky, the user must decide whether to regenerate.
- When it is unclear whether the story/original text the user provided calls for free adaptation or faithful scripting.