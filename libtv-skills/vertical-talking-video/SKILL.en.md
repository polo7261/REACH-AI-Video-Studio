---
name: vertical-talking-video
description: "Vertical talking-head short video: produce vertical shorts with no on-camera talent—one-click creation of viral voiceover shorts."
---

## Platform Presets (Shared by Both Routes)

First set the baseline by target platform; if the user doesn't specify, use the shorts default—don't stall with follow-up questions.

Platform Aspect ratio Clips per run Baseline duration sweet spot Feel YouTube Shorts 9:16 3 30–60s Must deliver a hook in the first 1 second TikTok 9:16 5 30–60s (may run slightly longer) Higher energy, faster pace Instagram Reels 9:16 3 30–60s Must deliver a hook in the first 1 second Vertical/square feed 1:1 3 Short; a static feel works fine too

- For aspect ratio, only pass the tokens the tools allow: vertical is always `9:16`, square `1:1`. Once the platform is given, don't guess the ratio; only change it when the user explicitly requests an override.
- Clip count is a baseline, not a hard quota—in the clipping route, if there aren't enough qualifying highlights, deliver fewer; don't pad the count with low-scoring junk clips. In the synthesis route, split naturally according to the script.

---

## Highlight Evaluation Framework (the core craft for picking segments / setting hooks, shared by both routes)

Whether picking from long source footage or writing a script from scratch, use this framework to judge "which segment is worth standing alone as a clip" and "what goes in the first few seconds":

The more a piece of footage / a script point hits the items below, the more it should be selected and the higher it should rank:

- **Hook moment**: a strong opening that can grab people within the first 1 second.
- **Emotional peak**: emotional high points such as laugh moments, tearjerker moments, gratification, anger.
- **Opinion bomb / counterintuitive**: strong opinions that defy common sense and dare to pass judgment.
- **Reveal moment**: information flips like "so that's it" or "actually, it's...".
- **Conflict**: opposition, disputes, face-slap moments, reversals.
- **Quotable line**: a line that can be screenshotted or quoted on its own.
- **Story climax**: the point of highest narrative tension.
- **Practical value**: actionable takeaways, checklists, and steps that can be used immediately.

For each candidate clip / script point, give three things (this is the basis for ranking and review, and also the structure for reporting back to the user):

- **Score** (0–100; the more hits, the higher);
- **Opening hook line** (what is said/written in the clip's first 1 second);
- **A one-sentence "why it works"** (which of the above points it hits).

Deduplicate overlapping/near-identical candidates by score, keep only the highest-scoring one, and don't output multiple clips whose content heavily overlaps.

---

## Route A · Long-Footage Clipping Workflow

1. **Analyze the source video**: hand the user-provided long video (trusted URL / local path) to source video analysis to obtain the segmented structure (segments) and semantic boundaries. This step is about "reading the material"; it produces no finished clips.
2. **Pick segments with the highlight framework**: score each segment one by one using the evaluation framework above, find the hook, write the "why it works", deduplicate, then take the Top-N (N = platform baseline or user-specified).
3. **Set cut points**: determine start and end times for each clip so it carries a complete "hook → climax" arc, with the hook in the first 1 second; keep within the platform's duration sweet spot.
4. **Verticalize**: crop the selected segments to the target aspect ratio (`9:16` / `1:1`). Keep the subject in frame—hold key people/subjects in the center of the vertical safe zone; when there's no automatic face-tracking capability, set the crop frame manually based on the subject's position, and for segments where the subject moves noticeably, split into shots and crop to follow.
5. **Subtitles**: add dialogue/key-point subtitles to each clip (overlaid or burned in at the compositing stage, per SP).
6. **Finishing & compositing**: use `composite_video` to output each finished vertical clip; pair with `generate_video_v3` if visuals/transitions need to be regenerated.
7. **Report back**: for each clip, give rank / score / time range / title / hook line / finished clip, so the user can pick at a glance.

> Note: this environment has no counterpart to the source tool's server-side managed clipping with "transcription + auto-ranking + dedup + face-tracking crop"—so transcription/ranking/dedup/cropping are instead carried by source video analysis + the highlight framework above + manually set cut points/crop frames; the framework itself is used as-is.

---

## Route B · From-Scratch Synthesis Workflow

1. **Topic → script**: given a topic or copy, write a narration script; break it into short sentences and arrange it by the highlight framework—hook in the first 1 second, middle sections layering emotion/opinions/reveals, and an ending that lands a quotable line or a call to action.
2. **Narration**: `generate_audio` (TTS) generates the narration from the script; specify voice timbre, emotion, and speaking rate clearly.
3. **Visuals**: sentence by sentence / section by section, use `generate_image_v3` for accompanying images, or `generate_video_v3` for dynamic footage—**no real people on camera**; carry it with B-roll / diagrams / scenes / data visualization; keep a unified visual style throughout.
4. **Subtitles**: dialogue/narration subtitles (overlaid at the compositing stage, or burned into the video, per SP).
5. **Compositing**: `composite_video` stitches clips along the narration timeline with BGM; `generate_audio` for music or sound effects. Vertical `9:16`.

---

## General Points

- **faceless**: never relies on real people on camera / lip sync; visuals are carried by images / B-roll / generated scenes / diagrams.
- **The first 3 seconds decide everything**: the earlier the hook, the better—on Shorts/Reels fight for the first 1 second; tight pacing, no buildup.
- **Vertical first**: default to `9:16`; center the subject and leave a subtitle safe zone.
- **Batch**: for multi-clip requests, track progress with task, one per finished clip.

## Common Pitfalls

- **Aspect ratio mismatch**: vertical platforms are always 9:16—don't publish landscape footage as is; the platform preset is already set, don't override it without a clear reason.
- **Padding with junk clips**: if there aren't enough qualifying highlights, deliver fewer; don't output low-score clips just to hit a count.
- **Duplicate clips**: deduplicate heavily overlapping candidates by score first, keeping only the highest one.
- **Subject out of frame**: vertical cropping must ensure the key subject stays in frame at all times and is never cropped out.

## Pairings (to be loaded together in the query / also this skill's evaluation combinations)

This skill is self-contained, with no source-native cross-skill dependencies. Only boundaries are listed, for rerouting:

```
Boundaries (don't use this skill; reroute instead): influencer-style real-person on-camera talking videos → ugc family; explanations with an on-screen avatar → talking-head type; purely beat-synced, music-driven MVs → music-video-flow.
```