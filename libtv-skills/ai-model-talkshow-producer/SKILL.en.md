---
name: ai-model-talkshow-producer
description: "AI model talk show skill: auto-generates models, scenes, talk show copy and script, and outputs a complete talk show short video"
---

# Wander AI Model Solo Stand-Up Comedy Short Video

## Skill Positioning

This Skill only produces Chinese solo AI-model stand-up comedy vertical short videos; it does not do interviews, podcasts, multi-person dialogues, news anchor reads, or generic AI hosting.

The framing is fixed as a UGC perspective shot from the audience on a phone: on the stage of a small theater or brand event, a single AI model performs with a mic; the bottom edge of the frame keeps a small amount of audience backs, shoulders, hair, or raised-phone foreground, and the background can naturally incorporate a brand logo lightbox sign.

The core goal is to complete the closed loop of "user material and creative-rights confirmation + comedic persona + Chinese stand-up raw draft + user script approval + model and scene assets + performance rhythm + video prompts." Content comes before visual assets; when the script doesn't pass, you must stop and revise it — never use polished visuals to cover unusable text.

## Multi-Level Reference Loading Strategy

This Skill uses multi-level references. During execution, load the corresponding file for each task phase:

- When writing or revising Chinese stand-up scripts, you must use `references/chinese-standup-script-engine.md`.
- After generating the script and before moving to video, you must use `references/script-approval-gate.md`.
- When generating final video node prompts and asset reference strategy, you must use `references/video-reference-policy.md`.

Do not treat the references as optional suggestions; they are the core methodology of this Skill. The main `SKILL.md` only handles the overall flow; for details, the references govern.

## Inputs

### Round 0: Confirm Content Source and Creative Rights First

Open by stating: "This Skill produces a Chinese solo AI-model stand-up comedy short video. The script decides whether it can be shot, so we confirm the content first; providing your own text or bits is the easiest way to preserve your personal voice. Once the script passes, we lock in the model and stage, and finally generate the video."

In the first round, have the user choose one content source:

1. Upload or paste existing Chinese stand-up text, bits, or work-in-progress drafts (recommended).
2. Provide a real experience, real conversation, or specific rant, and the Skill helps turn it into a bit.
3. Provide only an abstract theme; the Skill first proposes 3 concrete scenarios for the user to choose from, without directly generating a final draft.

If the user provides an existing draft, first ask "Which original lines, observations, or punchlines must be kept?" Default to minimal necessary edits; do not change the user's core observations, expressive tone, or main punchlines without permission. The user has the final say.

At the same time, collect the minimal project boundaries:

- Content type: everyday-life roasting, workplace roasting, dating observations, soft product placement, brand event opener, light trending-topic jokes.
- Performer's voice: the composure she wants to maintain, real flaws, defense mechanisms, phrasing habits, main targets of her jokes, and off-limits expressions. If the user hasn't decided, offer 2 short voice cards to choose from.
- Duration: 15-second video (recommended), 30-second video, 60-second video.
- Tone boundary: gentle teasing, sharp roasting, exaggerated performance, brand-safe.

Defaults: 15 seconds, 9:16, 720P, audience-seat UGC perspective, gentle roasting. Subtitles and visual assets are confirmed after the script passes.

### Collect Visual Assets Only After the Script Passes

Only ask once the user has made an explicit selection or the script has passed:

- Whether a model image already exists. If not, automatically generate an adult AI model matching the character's voice and stage presence.
- Whether a brand logo image exists. If not, do not place one; if yes, turn it into a stage background lightbox, sign, neon sign, or logo-shaped decoration.
- Whether there is a clear stage reference. If not, automatically generate a small theater, open-mic, or brand event stage.
- Subtitle style: short-video large subtitles, variety-show bullet-comment feel, minimalist white text, stage caption bar, no subtitles.

## Input Usage

- Text, bits, and real quotes provided by the user are content asset anchors; unless the user authorizes a rewrite, make only minimal necessary edits.
- Model images provided by the user are character asset anchors, used first to generate or lock `model_reference`.
- Stage images provided by the user are scene references, used only to generate or lock `stage_composite_reference`; the final video never directly references the empty scene image.
- Logos provided by the user can only be naturally integrated into background lightboxes, signs, or stage decorations; never as a watermark.
- When the user only provides an abstract theme, do not write the script directly; you must first gather real details per the material threshold in `references/chinese-standup-script-engine.md`.
- When the user provides a complete script, first preserve its core observations, original lines, tone, and main punchlines, then run a read-aloud self-check; problems must be clearly pointed out and the user decides whether to revise — never strip creative rights in the name of "optimization."

## Internal Workflow and Knowhow

### 1. Content and Voice Anchors

First lock in:

- `source_material`: the user's original draft, real quotes, experience, or chosen scenario.
- `must_keep`: sentences, observations, and punchlines the user specified must be kept.
- `voice_card`: composure, flaws, defense mechanisms, phrasing habits, targets, off-limits expressions.
- `comedy_action`: the single main comedic action of this piece, e.g., self-exposure, collapse of composure, over-enforcement of rules, status downgrade, mismatch between emotion and behavior, escalation of specific details, or a callback.

The 15-second default allows only one core scene, one main punchline, and one optional tag. Do not force in 2-3 jokes just to hit a count.

Generate 3 clearly different raw drafts for blind selection; the differences must come from angle or comedic action, not paraphrase. Do not move to visual assets until the user has chosen or confirmed.

### 2. Chinese Script Writing

Load and execute `references/chinese-standup-script-engine.md`. Candidates may be eliminated internally, but toward the user output only necessary judgments and the raw drafts — no large mock evaluation tables.

### 3. Script Approval Gate

After generating candidate raw drafts and the necessary risk notes, load and execute `references/script-approval-gate.md`. Until the user explicitly confirms, do not create visual assets or generate video nodes.

### 4. Asset Anchors

First generate or lock in:

- `model_reference`: landscape 16:9 white-background model character sheet, locking in face, hairstyle, makeup, outfit, shoes, leg styling, posture, and performance presence.
- `stage_reference`: vertical UGC empty shot of the small-theater stage, used only to build the composite; not a final video reference asset.
- `logo_stage_reference`: generated only when the user provides a logo, used to integrate the logo into the stage background.
- `stage_composite_reference`: vertical composite image after the model is placed on stage, locking in the same model, stage, sitting or standing pose, audience foreground, lighting, and overall live-event feel.

After generating or locking in the above assets, you must stop and ask: "Are you satisfied with this model, stage, and speech preview image? Do you need a regeneration? If you want adjustments, please specify the model's styling, stage style, sitting pose/performance state, or logo presentation."

Do not proceed to video generation until the user confirms the assets.

### 5. Video Prompts and Asset References

After the user confirms the script and the visual assets, load and execute: `references/video-reference-policy.md`

The final video references only:

- `stage_composite_reference`: the model-scene composite image, as the primary video reference.
- `model_reference`: the model character asset, as the reference for identity, makeup and styling, outfit, and physique.
- If the user needs subtitles and a subtitle style image or subtitled script image has been generated, you may additionally reference `subtitle_style_reference`.

The final video does not reference the empty `stage_reference`. The empty scene image only serves composite generation and never enters the final video references.

## Asset Image Prompt Framework

### `model_reference`

```text
Generate a landscape 16:9 white-background AI actress character sheet: pure white background, studio-shot quality, layout split left and right.
Left side: the same adult female AI model in a full-body front-facing standing pose, fully showing hair, face, top, skirt/suit, leg styling, and shoes, with a confident, natural stance.
Right side: a close-up of the same model's face, clearly showing facial features, hairstyle, eye makeup, lip makeup, and camera-ready makeup.

Character direction: slender figure, clean proportions, strong stage presence, suited to small-theater Chinese solo stand-up performance.
Styling direction: high heels, short skirt or fitted suit, sheer black stockings/tights, fitted-cut top, cropped jacket, metal earrings; adjustable per persona to urban nightlife vibe, cool sharp-tongued vibe, bubbly sweet-girl vibe, or polished office-worker vibe.
Makeup direction: crisp eyeliner, curled lashes, red-brown or rose lip makeup, clean base makeup, light contouring, still legible under stage lighting.
Shooting requirements: realistic photography, clean studio shoot, clear clothing details, no text, no logo, no extra people, no complex background.
Avoid: do not generate childlike features, exaggerated influencer filters, plastic skin, excessive exposure, vulgar poses, or cluttered backgrounds.
```

### `stage_reference`

```text
Generate a vertical 9:16 empty-shot image of a small-theater Chinese stand-up stage, shot from the audience on a phone, with a strong UGC live feel.
The bottom edge and lower left/right corners must contain a small amount of blurred foreground: audience backs, shoulders, hair, or a raised phone, as if casually captured from the middle-to-back rows with a phone.
At the center of the stage: a bar stool, a handheld mic or mic stand, and a small side table/water glass; the background is a brick wall, dark curtain, open-mic lightbox, or brand event backdrop.
Lighting is a real small-theater warm spotlight; slight noise, crushed blacks, limited phone dynamic range, and slight handheld framing drift are allowed.
If the user provides a logo, render the logo as a background lightbox, wall sign, neon sign, or stage decoration — not as a watermark.
Avoid: do not generate ad-studio shoots, film-grade overly clean compositions, empty spacious lobbies, over-the-top neon nightclubs, game CG looks, or stages without audience foreground.
```

### `stage_composite_reference`

```text
Based on the same AI actress from model_reference and the same small-theater stage from stage_reference, generate a vertical 9:16 speech preview composite image.
The same model must keep her face, hairstyle, makeup, outfit, shoes, and leg styling consistent.
She sits on the bar stool or half-leans against it at center stage, holding the mic in one hand close to her mouth, the other hand resting naturally on her knee, on the stool edge, or making a slight gesture; she may naturally cross her legs and lean slightly forward, with a relaxed, confident expression carrying a hint of dry humor.
The image must look like a phone shot from the audience: the lower edge keeps audience backs/shoulders/phone foreground, the subject is lit by warm stage light, the background is slightly darker, and the framing is slightly handheld without hurting watchability.
If there is a logo, it must already be naturally integrated into the background lightbox or stage decoration.
Avoid: do not look like a professional ad-studio shoot, no excessive skin smoothing, no floating model or wrong proportions, do not remove the audience foreground, no multiple people on stage, do not turn the logo into a watermark.
```

## Outputs

### Round 0 Output

Output only:

1. The three content source options, including "Upload or paste existing Chinese stand-up text, bits, or work-in-progress drafts (recommended)."
2. The minimal project boundary questions.
3. When the user has a draft, ask what must be kept; when the user only has an abstract theme, provide 3 concrete scenarios.

### Script Stage Output

Must output:

1. A one-sentence confirmation of the material and character voice.
2. 3 clearly different 15-second raw drafts; when the user already has a polished draft, prioritize the "minimal revision version," and provide the other two versions only if the user allows exploration.
3. A one-sentence risk note per draft and a recommended version; do not show internal self-evaluation tables.
4. Only after the user picks one, output the condensed performance pauses and actions.
5. The script confirmation question.

### Asset Stage Output After the User Confirms the Script

Must output:

1. Needs confirmation for the model image, logo image, and stage reference.
2. For assets the user has not provided or locked, output the complete generation prompts for `model_reference`, `stage_reference`, the optional `logo_stage_reference`, and `stage_composite_reference`.
3. The asset confirmation question.

### Output After the User Confirms the Visual Assets

Must output:

1. The 15-second video prompt, or multiple 15-second segment prompts.
2. The final video asset reference list.
3. The subtitle reference strategy.
4. The asset closed-loop check.

## Self-Check

Before output, verify:

- Does it only do Chinese solo stand-up?
- Does it first confirm the user's text/bits (recommended), real experience, or theme scenario?
- Does it explicitly keep the original lines, observations, and punchlines the user specified?
- Does it lock the model assets and model-scene composite only after the script passes?
- Does it load and execute the Chinese writing reference when writing the script?
- When the user only gives an abstract theme, does it ask for real details first instead of writing directly?
- Does the script pass the factual, attitude, and technical layer checks simultaneously?
- Is there exactly one main comedic action, one main punchline, and an optional tag?
- Do the three candidates differ in angle rather than being paraphrases?
- Was internal elimination kept internal, without drowning the raw drafts in tables and explanations?
- Does the script fit the voice card and could not easily be said by just anyone?
- Were translationese, marketing-speak, stale internet memes, explained jokes, and forced uplifting moralizing removed?
- Did it stop after generating the script to request user confirmation?
- Did it refrain from generating video nodes before the user confirmed the script?
- Does the final video reference only `stage_composite_reference` and `model_reference`, adding `subtitle_style_reference` only when subtitles are needed?
- Does the final video avoid referencing the empty `stage_reference`?

## Ask User

Situations where the user must be asked:

- At the start, ask whether the user will upload or paste existing Chinese stand-up text, bits, or work-in-progress drafts (recommended).
- When the user has a draft, ask what must be kept.
- When the user only gives an abstract theme, ask for real details; do not write the script directly.
- After generating the script, ask "Does this version of the script pass, or does it need changes?"
- After the script passes, when model, logo, or stage references are missing, ask whether the user will provide them or they should be auto-generated.
- After assets are generated, ask whether the user is satisfied with the model, stage, and speech preview images.
- When the user needs subtitles but hasn't specified a style, ask for the subtitle style.