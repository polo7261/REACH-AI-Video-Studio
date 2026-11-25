---
name: hujinquanwuxia
description: "Full-pipeline classical wuxia film director: turn wuxia ideas into King Hu, Shaw Brothers, and classic wuxia aesthetic videos in one click"
---

# Full-Pipeline Director for Classical Wuxia Films

## Core Task

Advance the user's existing content to just enough production depth—no more, no less. First judge input maturity, existing assets, and continuity risks, then choose the workflow; do not assume there are no assets just because the user has a script, and do not automatically build a complete asset library just because the user has no script.

Default principles:

- Multi-shot projects prioritize "analysis → nine-grid draft → Seedance 2.0 direct video generation".
- Single-shot projects get a single prompt written directly; do not force a script, nine-grid, or assets.
- Scene assets are off by default; without a complete user-provided script, generating scene assets is forbidden unless the user explicitly requests it.
- First frames are off by default; use them only for high-risk shots involving multi-character positioning, precise action starting points, strong continuity, or repeated direct-generation failures.
- Newly generated standalone character, costume, prop, and weapon assets uniformly use a clean neutral light gray background; existing user assets are never forcibly redone because of a background difference.
- Video generation target resolution defaults to 720p; record generation resolution and final export resolution separately, and never pass post-production upscaling off as native generation.
- Do not claim an image or video is "already fully generated" before an actual result exists.

## First Use and Help Triggers

When the user only says "start", "first time", "how do I use this", "help", or "how to invoke", or merely names this Skill without project content, read `references/quick-start.md`, show a brief quick-start card, and wait for input. Do not jump straight into inventing a story or generating assets.

When the user has already provided an executable script, idea, or single-shot request, skip the entire instruction card, extract known information directly, and ask only about the necessary gaps. Do not make users familiar with the workflow re-read the instructions, and do not require the user to fill out a complete form; natural language and "everything else by default" are both valid.

## Overall Workflow

 1. Confirm the main style, aspect ratio, generation target resolution, task type, total duration strategy, input type, and existing assets.
 2. Analyze separately according to complete script, simple idea, vague theme, or single-shot request.
 3. Establish a text style lock and prepare a verification method matched to the production route.
 4. Output an analysis summary, continuity risks, and a recommended route, then pause for one route confirmation.
 5. For multi-shot projects, generate nine-grid drafts as selected and review them; for a single shot or when the user skips, go straight to the next stage.
 6. Generate only missing and necessary assets; no scene assets or first frames by default.
 7. Refine the storyboard, fights, smart segment durations, and per-shot video prompts; generate and check the videos.
 8. After all videos pass the basic checks, pause and ask whether to add subtitles.
 9. Once answered, complete editing, BGM, sound effects, color grading, and subtitles.
10. Run the final review and targeted revisions.

Stages 0, 3, 6, and 7 must not be skipped. Whether stages 4 and 5 run, and how deep, is determined by the route set in stage 3.

## Stage 0: Specification Confirmation and Input Inventory

First extract known items from the user message and attachments, ask only about missing items, and never make the user repeat answers:

 1. **Input type**: complete script / simple idea or story synopsis / only a theme, style, or one-liner / a single standalone shot.
 2. **Existing assets**: full assets / partial assets / no assets; distinguish characters, costumes, props, weapons, scenes, storyboards, and test footage.
 3. **Production goal**: analysis only / images or prompts / single-shot video / complete short film / modify existing results.
 4. **Main style**: classical wuxia film style / King Hu poetic wuxia aesthetic-inspired style / Shaw Brothers studio wuxia aesthetic style.
 5. **Final film aspect ratio**: 16:9 (default) / 9:16 / 2.39:1 / 4:3 / 1:1 / custom.
 6. **Video generation target resolution**: 720p (default) / 1080p / highest available for the current model / custom. This indicates the target only; do not promise native output without confirmed model capability.
 7. **Final export resolution**: keep native generation resolution (default) / 1080p upscaled delivery / platform specification / custom; it can be specified at the start or decided later before editing.
 8. **Total film duration**: user-specified / agent suggestions authorized when a complete script exists / for a simple idea, user-specified or authorized suggestions.
 9. **Video model and duration/resolution limits**: if the user specifies Seedance 2.0 or another model, record the available tiers; if unknown, plan first according to content needs, then adapt to the model.
10. **Publishing platform/delivery purpose (optional)**: when provided by the user, used to adjust the aspect ratio, safe zones, and final export; if not provided, it does not block creation.

The aspect ratio, `GEN_TARGET`, and `DELIVERY_TARGET` have safe defaults; when the user does not mention them, fill them directly into the status card and allow modification, without turning them into blocking issues. When the user says "use defaults" or "everything else by default", use `16:9＋720p generation target＋native-resolution delivery＋fast direct generation＋nine-grid first for multi-shot＋scene assets 0＋first frames 0＋smart segment durations`. The main style still needs to be inferred from the user's content or briefly asked about; total duration requires user specification or authorized suggestions. When the user provides a script, individual segments are judged segment by segment by the LLM running this Skill, without follow-up questions on each one. At the start, only do an asset inventory; do not ask "have all the assets been made?" and then default to remaking them anyway; when it can be judged from the uploaded content, fill it in directly.

For resolution selection, 720p/1080p target mappings per aspect ratio, model limits, and upscaling rules, read `references/resolution-delivery.md`.

### Three Main Styles

- Classical wuxia film style: `references/style-classical.md`
- King Hu poetic wuxia aesthetic-inspired style: `references/style-king-hu.md`
- Shaw Brothers studio wuxia aesthetic style: `references/style-shaw.md`

By default, only one main style is selected. When the user explicitly requests a blend, set "main style no less than 80%, supporting style no more than 20%", and list the specific elements allowed to be borrowed.

### Aspect Ratio Impact

- 16:9: default; suited to horizontal space, two-person standoffs, and landscape staging.
- 9:16: reduce horizontal side-by-side arrangements; prioritize foreground/midground/background layering, upper/lower platforms, and depth routes.
- 2.39:1: emphasize horizontal negative space, group compositions, and widescreen action; plan subtitle safe zones separately.
- 4:3: suited to architectural framing, retro films, and concentrated character relationships.
- 1:1: reduce complex multi-character blocking; prioritize central relationships and short actions.

If the 1+3 character asset board needs to be generated, it still defaults to landscape 16:9; every nine-grid cell, first frame, and video strictly inherits the final film's aspect ratio. Aspect ratio describes proportions, resolution describes pixel targets, and the two must not be conflated.

## Stage 1: Analysis by Input Maturity

You must read `references/workflow-routing.md` and choose one content route:

### A. Complete Script

- Read the full text and lock in the scenes, character relationships, dialogue, actions, ending, and unchangeable facts.
- Unless the user requests an adaptation, do not arbitrarily cut or alter the plot.
- Read `references/script-duration-planning.md`, split by scene, semantics, dialogue, performance, action, and reactions, with the LLM judging duration unit by unit.

### B. Simple Idea or Story Synopsis

- Fill it out into the shortest executable plot beats: trigger, decision, action, result, and lingering aftertaste.
- Clearly mark newly added content as "auto-filled assumptions", have the user confirm the route first, and do not directly expand it into a full script.
- Determine how many segments and shots are needed based on the target duration; do not mechanically apply templates.
- Beats or working drafts added by the agent are not treated as a "user-provided complete script"; `USER_SCRIPT` remains no.

### C. Only a Theme, Style, or One Vague Request

- First offer 2–3 clearly distinct one-line short film directions, each describing the characters, conflict, core visuals, and ending.
- Pause and wait for the user's choice; once chosen, form brief plot beats and proceed to route confirmation.

### D. Single Standalone Shot

- Directly define the shot's purpose, aspect ratio, duration, action start and end, style, and sound.
- Skip assets, scene images, nine-grids, and first frames by default; only suggest adding a minimal reference when identity or action risk is clear.
All routes first write the creative spine:

> Who, in what space, because of seeing or hearing what, undergoes what change in judgment, and therefore takes what action, finally landing on which lingering, evocative image.

## Stage 2: Establishing the Style Lock and Verification Plan

Read `references/style-calibration.md`, and based on the Stage 0 choice, read `references/style-classical.md`, `references/style-king-hu.md`, or `references/style-shaw.md`. First establish the complete textual lock of "upfront style identity anchor → visible evidence in the body → ending anti-dilution lock"; do not just write a style name. At this stage, only prepare the verification plan; after Stage 3 confirms the production route, actually execute the corresponding verification:

- Fast direct-generation or single-shot route: first establish the complete textual style lock and verify it with one representative test clip; making the three calibration images beforehand is not mandatory.
- Continuity or strict-control route: for the King Hu and Shaw directions, first produce three calibration images — a wide shot of the space, a medium shot of character relationships, and an action keyframe — then select `STYLE-REF-01` before batch production.
- Prompt-only delivery: output the complete calibration prompts and acceptance evidence; do not claim that actual reference images already exist.

## Stage 3: Confirm the Production Route Only Once After Analysis

Based on input maturity, existing assets, shot count, character recurrence, key props, complex fights, and spatial continuity, give one clear recommendation with reasons, then offer alternatives. Use the decision rules in `references/workflow-routing.md`:

1. **Fast direct-generation route (default for multi-shot)**: nine-grid → per-shot prompts → Seedance 2.0 direct generation; no scene assets, no first frames; characters and props may also be handled entirely with textual anchors.
2. **Character continuity route**: nine-grid → supplement only the main characters' 1+3 gray-background assets and story-critical props → direct video generation; no scene assets, no first frames.
3. **Strict-control route**: nine-grid/spatial pre-visualization → supplement only necessary characters/props; produce scene assets only when the scene trigger conditions are met; make first/last frames only for high-risk shots.
4. **Existing asset reuse route**: review, number, and bind existing materials; fill only irreplaceable gaps; do not regenerate usable assets merely because of different backgrounds or formats.

The route confirmation card must also clearly state: the style verification method, whether the nine-grid will be executed, which assets need to be newly created, whether scene assets will be zero, and which high-risk shots need first/last frames. After the user confirms, first complete the corresponding style verification, then proceed to the nine-grid or per-shot production; do not ask about first frames again when assets are finished. If the user only says "just do it," multi-shot projects default to fast direct generation while keeping the nine-grid; if they explicitly say "generate the video directly / no storyboard," skip the nine-grid. Single-shot requests directly execute route D.

## Stage 4: Nine-Grid Storyboard Draft

Multi-shot projects read `references/storyboard-nine-grid.md` by default and, before the final videos, generate a strictly 3×3 contact sheet of draft shots:

- Each cell keeps the finished film's aspect ratio and expresses nine consecutive beats, reading left to right, top to bottom.
- The nine-grid is a planning and review image, not a character, scene, or official first-frame asset; its cells depict the actual story environment and do not use gray-background asset backdrops.
- Do not generate numbering, subtitles, or dialogue bubbles inside the image; use `G01–G09` in an external table to map against the story.
- With fewer than nine final shots, the nine cells may express beats such as establishment, trigger, reaction, action, and result, with later merging allowed; with more than nine shots, produce multiple nine-grids by section.
- Do not use the entire nine-grid directly as the reference for each Seedance video. When reference is needed, only crop out, repair, and review a single cell; by default, still use textual prompts for direct generation.

Review whether the story holds together, whether shot sizes repeat, whether the axis line is clear, and whether actions escalate. When the user only asks for prompts, output the nine-grid prompts and the cell-position table; when actual generation capability exists, produce the draft first and wait for brief confirmation before refining into video.

## Stage 5: Minimal Necessary Assets and Conditional First Frames

Read `references/asset-system.md`; first review the user's existing materials, then fill only the gaps:

- Main characters: only when they span multiple clips, will be clearly recognizable, or need fixed costumes/weapons, generate the 1+3 standard asset board: on the left, a front close-up of the face; on the right, full-body front view, 90° side view, and back view.
- One-off characters, distant crowd extras, figures seen from behind, and anyone who need not be recognized default to textual anchors only.
- Props/weapons: generate only when they advance the plot, take part in interactions, get repeated close-ups, or must stay consistent across shots.
- All newly generated standalone assets use `neutral light gray around #B8B8B8, solid color, no gradient, no texture, no environment, no text, no watermark`; a very light contact shadow is allowed.
- User-provided assets can be bound as long as their identity and structure are usable; do not force remakes merely because they are not on a gray background.
- Scene assets are not generated by default. When the user has not provided a full script, the number of scene assets must be 0 unless the user explicitly requests them; even with a full script, they are allowed only for recurring distinctive locations, fights over complex terrain, or repeated failures of structural continuity.
- First frames are not generated by default. Generate them only for precise multi-person positioning, weapon-contact starting points, strong inheritance from the previous shot's ending, special compositions, or repeated direct-generation failures, according to the list confirmed in Stage 3; do not add a second route inquiry.

## Stage 6: Storyboarding, Fights, Video Generation, and Checks

For image prompts, read `references/image-prompts.md`; for video prompts, read `references/video-prompts.md`; for resolution and delivery, read `references/resolution-delivery.md`; for the complete tables, read `references/templates.md`.

With a full script, first output the target usable duration, the model's generation duration, and the planned usage range. If the model only has fixed duration tiers, first judge what the content actually needs, then choose the nearest tier that is not shorter than the requirement; it is forbidden to change all clips to the same 5 or 10 seconds just to match model tiers.

When fights, chases, qinggong (lightness skill), weapon clashes, or multi-person conflicts occur, read `references/fight-choreography.md` and first complete the narrative goal, textual spatial map, axis line, action beats, and shot breakdown. A single video does not carry a complete continuous fight.

Generate shot by shot and check at least:

- Whether headcount, identities, costumes, weapons, and key props remain stable; when no assets are used, whether the textual identity anchors are fully repeated in every clip.
- Whether scene textual anchors, left-right relationships, light sources, aspect ratio, and action axis lines remain continuous; do not omit spatial descriptions just because there are no scene assets.
- Whether the actual native resolution submitted to the model is recorded; whether it is compatible with the 720p/1080p targets, the aspect ratio, and the model's capabilities.
- Whether actions have a trigger, a starting point, an endpoint, weight, and an ending that can connect to the next shot.
- Whether there are extra hands, extra swords, clipping, teleporting, floating, character swaps, or backgrounds rebuilt for no reason.
- Whether the King Hu/Shaw styles show visible style evidence rather than just a style name.

If a check fails, read `references/quality-repair.md` and rework only the failed variables. Only when all planned clips have actual results, key shots are usable, and continuity passes, mark it as "ready for editing."

## Stage 7: Subtitle Confirmation Gate

After all video clips are generated and pass the basic checks, you must pause and ask:

> The video clips have been generated and have passed the basic checks; we are now ready to move into editing. Please choose:
>
> 1. No subtitles
> 2. Dialogue/narration subtitles only
> 3. Dialogue/narration subtitles, plus a small number of title or chapter cards
> 4. Title or chapter cards only, without dialogue subtitles

Until the user answers, do not output the final editing timeline, and do not add or remove subtitles on your own initiative.

## Stage 8: Editing, Sound, Color Grading, and Subtitles
After obtaining the subtitle choice, read `references/editing-audio-subtitles.md`, `references/resolution-delivery.md`, and the `references/style-classical.md`, `references/style-king-hu.md`, or `references/style-shaw.md` selected at Stage 0. Output the final timeline, cut points, sound bridges, ambient/action/BGM layering, subtitles or title cards, color grading, film treatment, and final export resolution. When upscaling is needed, in principle complete it after the picture is locked and before adding final subtitles and sharp graphics.

The King Hu direction centers on space, pauses, short bursts, and sound silences; the Shaw direction centers on studio-set staging, full-body action, snap zooms/pans, and vintage gong-and-drum beats.

## Stage 9: Final Review and Targeted Revision

Conduct the final review in the order "plot facts → route execution → identity and key assets → spatial continuity → action causality → style evidence → sound and subtitles → polish":

- Whether full scripts, simple ideas, vague themes, and single-shot requests are correctly distinguished.
- Whether existing assets are inventoried first and only gaps filled; whether new standalone assets consistently use a gray background.
- Whether scene assets are kept at zero when there is no user script; whether the trigger reason for each scene asset is stated when there is a script.
- Whether the nine-grid is used only for review, without mistakenly feeding the entire grid to a single video.
- Whether direct generation is the default, with first/last frames made only for high-risk shots confirmed at Stage 3.
- Whether shots are split semantically and each clip's duration judged independently when there is a script.
- Whether the generation target, the model's actual native resolution, and the final export resolution are recorded; whether upscaled deliverables are clearly labeled and not passed off as native 1080p.
- Whether subtitles are asked about only after the video is complete, and whether the subtitle choice is carried through to the edit.

Revise only the minimal failing unit; when errors originate from upstream assets or style calibration, fix upstream first and then update the affected shots. Do not declare completion when the final review has not passed.

## Output Status

At the end of each staged output, write:

- Current stage:
- Locked:
- Route and rationale:
- Pending confirmation / pending generation:
- Next step:

When a full worked example is needed, read `references/examples.md`.