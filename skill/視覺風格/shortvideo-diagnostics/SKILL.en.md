---
name: shortvideo-diagnostics
description: "Short video diagnostic analyst: break down hooks and retention, or analyze and revise shot instructions."
---

# content-analyzer

A utility skill — a set of content analysis patterns that grows incrementally. Each pattern parses a user's **existing piece of concrete content material** (video, clip, or a finished video pointed to by a URL) into **structured, downstream-oriented** analysis. Invoked by workflows (or directly) during the analysis phase, positioned before any downstream editing/marketing/generation steps: use it when a specific piece of content must first be broken down into structured, purpose-oriented analysis.

Pick **one** pattern based on your intent, run only the matching one, do not pull both.

## Pattern Selection

| Intent | Output |
|---|---|
| Analyze a video for marketing | Marketing breakdown of the video — hooks (visual/auditory/semantic), retention beats, CTA, shareability (STEPPS) |
| Analyze a video for editing | Change-point analysis for a single add/delete/modify/replace, landing on instructions to regenerate the corresponding storyboard shots |

First use `analyze_video_clip_storyboard` to obtain the storyboard, pacing, and cinematography, as the shared **structural foundation** for both patterns; then perform the corresponding pattern's distillation on top of that structure.

## Pattern 1 · Marketing Breakdown (marketing-analyze)

On top of the structural foundation, distill layer by layer:

- **Hook (grabbing attention in the first 1-3 seconds)** — located separately along three channels:
  - Visual hook: the anomaly/tension/information gap in the opening frame (who/what/abnormal state).
  - Auditory hook: the ear-catching point of the opening sound effects/voiceover/music.
  - Semantic hook: the suspense, promise, or conflicting proposition raised by the copy/voiceover.
- **Retention beats** — mark the moments along the timeline that sustain viewing: the rhythm of information release, twist/reveal points, visual gear shifts, the "wait a little longer and you'll get it" suspension; point out which beats prevent drop-off.
- **CTA** — the timing of the call to action, its form (visual/voiceover/subtitle), wording, and the next-step action it points to.
- **Shareability (six STEPPS elements)** — judge item by item the mechanism by which this content triggers sharing:
  1. **Social currency**: Does sharing it make people appear knowledgeable/cutting-edge/tasteful?
  2. **Triggers**: Is the content bound to high-frequency everyday scenarios/objects, so people are repeatedly reminded of it?
  3. **Emotion**: Does it evoke high-arousal emotions (awe/anger/amusement/anxiety) or low-arousal ones (contentment)? High arousal is more likely to be shared.
  4. **Public**: Is the use of the content/product visible, imitable, leaving public traces?
  5. **Practical value**: Does it provide useful information that can be passed on to others (saving money/effort/useful tips)?
  6. **Stories**: Is the core message wrapped in a story carrier that will be retold?

Output as structured bullet points (itemized/table), not prose-style retelling.

## Pattern 2 · Edit Change Analysis (edit-video-analyze)

Analysis targeting a **single change point** the user wants to make to the finished video (add / delete / replace / modify an element).

- First **locate on the structural foundation which storyboard shot/which segment of the timeline** the change lands in, clearly stating the object, position, and desired effect of the change.
- **This environment has no video-to-video direct editing capability**: videos are regenerated via `generate_video_v3` using text + anchors. Therefore the output of the change analysis is not a v2v edit instruction, but rather **rewriting the affected storyboard shot into a new generation instruction** — keep the anchors of unchanged shots intact, rewrite only the prompt/composition/action/duration of the changed shot, and hand it to downstream to regenerate that shot before splicing.
- Handle only one change point at a time; multiple change points are broken down one by one, each landing on the regeneration instruction for its corresponding storyboard shot.

## Output Destination

The structured analysis from both patterns is written into the target storyboard table / anchor list (`write_file_v2`), for direct consumption by video-generation or replication workflows.

## Boundaries (Do not use this skill; reroute)

- Only analyzes **existing concrete content**; trend / viral hit / creator discovery research is not covered here.
- Product input preprocessing (parsing a product image/URL into category/use/opening mechanism) → product-analyzer.
- Brand asset extraction (getting logo, color scheme from a brand homepage) → brand-analyzer.
- Image / video generation itself → the corresponding generation capability or workflow process.