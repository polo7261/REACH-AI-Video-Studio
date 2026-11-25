---
name: pixar-animation-story-builder
description: "Pixar animation story: companion Skill for Pixar-style animated ads, from character design and scriptwriting to multi-shot videos"
---

# pixaranimationstudios-dm3d

## Positioning

Responsible for: Using the Pixar 3D cartoon rendering style to produce a 1-3 minute animated short story episode, covering the full workflow of story direction selection, script writing, multi-angle character design sheets, expression anchors, prop anchors, style locking, storyboard planning, multi-segment video generation and composition, and cover design. Not responsible for: Brand advertisements, live-action appearances, realistic styles, or feature-length films over 3 minutes.

## Inputs

Must be provided or confirmed by the user:

- Story direction (Agent provides multiple category options, or user brings their own script/reference video)
- Protagonist settings (gender, type, appearance preferences)
- Video output aspect ratio (16:9 / 9:16 / 1:1)
- Target duration (1 minute / 2 minutes / 3 minutes)

If provided by the user, use them with priority; otherwise, the Agent decides on its own:

- Story style (heartwarming healing / comedy / action adventure / fantasy magic / everyday inspiration / emotional elevation / sports comedy)
- Number of characters and gender combination
- Scene preferences
- Whether character dialogue lines are needed
- Whether narration is needed
- Whether a video cover is needed

## Global Execution Principles

- After each step is completed, the Agent must first proactively self-check, then present: A make revisions / B proceed to the next step. Do not advance without confirmation.
- For steps requiring the user to make a choice, first list the options in the chat panel, and only generate on the canvas after the user has made a selection.
- Videos are split into segments of no more than 15 seconds each for generation. First generate 1-2 segments for the client to preview and confirm, then continue generating the remaining segments after satisfaction.
- All steps use the node_key returned by real tools; do not fabricate or guess.
- Canvas asset reuse principle: Before each generation step, first check whether the corresponding asset already exists on the canvas (character three-view sheets, scene images, etc.). If it exists, directly reuse the existing node as an anchor without regenerating, and inform the user that "the XX asset on the canvas has been detected and will be reused directly."

## Internal Workflow & Knowhow

### Step 1 · Story Direction Confirmation

If the user has not provided a script, offer multiple story direction categories for selection (A/B/C/D/E/F):

- A · Parent-child warmth: A child becomes friends with a mysterious little animal, and together they solve small troubles; heartwarming and healing
- B · Comedy: A clumsy little monster wants to learn a skill, fails repeatedly but perseveres and ultimately succeeds; joyful and hilarious
- C · Fantasy adventure: An ordinary child accidentally discovers a magical item and embarks on a short fantastical journey; action adventure
- D · Everyday inspiration: An ordinary character faces a small setback and regains confidence through effort; warm and inspiring
- E · Friendship story: Two people with opposite personalities go from meeting to becoming friends; comedy + warmth
- F · Custom / Own script / Reference video

When the user provides a reference video: Analyze the action style, scenes, and emotional rhythm in the video, and faithfully reproduce the core content structure of the reference video.

If the user provides a script: Proceed directly to Step 2, treating the script content as the factual baseline for all subsequent steps; do not alter the core plot without authorization.

### Step 2 · Character Design (Including Multi-angle Character Sheets)

Before Step 2, the following must be executed first:

**① Check existing canvas assets**

Use search_canvas_nodes to check whether the canvas already has character three-view or character sheet nodes:

- If character three-view/sheets already exist: Inform the user that "the character assets on the canvas have been detected and will be reused directly, skipping the character generation step," directly use the existing node as the character anchor, and proceed to Step 2.5.
- If not: Continue with the following workflow.

**② Ask about character information** (only when no existing assets are present)

- Character gender and type (female / male / child / little monster / animal / multiple characters)
- Number of characters and age settings
- Any appearance preferences or reference images

**③ Ask about the generation model** (only when no existing assets are present)

Before generating character sheets, must ask the user which model to use, and explain the advantages of both:

> **Which model would you like to use to generate the character sheets?**
>
> - **Midjourney V8.1**: Richer image details, stronger light and shadow texture, and more prominent Pixar 3D roundness; suitable for character designs that pursue refined textures; recommended as the first choice.
> - **Midjourney V7**: More consistent and stable style, better multi-angle consistency, and faster generation speed; suitable for scenarios that require batch generation of multi-angle sheets or uniform styling across multiple characters.

After receiving the user's choice, list the four appearance style options A/B/C/D, where D is user-defined, and generate only after the user has made a selection.

Character sheets must be generated from multiple angles, locking facial features:

Front-facing sheet (required): Front half-body of the character with a calm expression, serving as the primary character anchor

Prompts must include detailed facial feature descriptions:

- Hairstyle: Color, length, hairstyle name (e.g., mullet, side part, ponytail, etc.)
- Face: Eye color, nose features, lip features, face shape
- Special features: No tail, no wings, etc., specified one by one

Facial locking specification in video prompts: "The character's facial features are strictly locked, referencing the facial design of {{character front node}} and {{character side node}}; facial features must not change with camera angles."

Criteria for a good character: Obvious Pixar rounded modeling feel; clean background; detailed and accurate facial feature descriptions; facial consistency across multi-angle sheets; clear differentiation in styling among multiple characters.

### Step 2.5 · Expression Anchors + Prop Anchors Generation

A · Expression anchors (key exaggerated expressions generated individually)

Model: **Lib Image** (fixed, cannot be changed)

When characters in the story have multiple key exaggerated expressions, expression anchor images must be generated individually:

- Generate a separate facial close-up image for each key expression, referencing the character node
- Prompts must clearly specify expression features: the specific states of the eyebrows, eyes, mouth, and facial muscles
- Reference in video generation: "Reference the expression of {{expression anchor node}}, with the character in a {expression name} state"
- Trigger conditions: The story contains more than 3 different exaggerated expressions; or the expression is a key plot point

B · Prop anchors (two categories)

Independent props: Generate the prop image separately, without characters, showing only the prop itself

Associated props: Must reference the corresponding character node in reference_nodes, via node reference rather than text description

Precise prop prompt specifications:

1. Display side: Front/back, choose one and state it clearly
2. Display state: Laid flat / held in hand / opened, etc., stated clearly
3. Single-side principle: Flat props show only one side; the back must not be visible
4. Combined props (character + prop) are forbidden for use as video references
5. Scene props also require separate anchor generation

### Step 3 · Script Writing and Segmentation Planning

Write the script following a three-act structure:

- Act 1 (Setup): Introduce characters, worldview, and trigger the conflict
- Act 2 (Development): Characters face challenges, emotional ups and downs, key turning point
- Act 3 (Resolution): Resolve the conflict, emotional landing point, ending freeze frame

Plan segments according to the target duration (15 seconds per segment):

- 1 minute → 4 segments / 2 minutes → 8 segments / 3 minutes → 12 segments

Script quality requirements:

- Each segment contains only 3-4 core actions; do not cram too many actions into one segment
- Content differs noticeably between segments, with emotional progression forming an arc
- Action descriptions are specific and clear, facilitating accurate expression in storyboard sketches

Display the complete script outline in the chat panel and wait for user confirmation before proceeding.

### Step 4 · Style Lock Card + Storyboard Sketches

Step 4a · First output the style lock card (generate sketches only after user confirmation):

- Character design keywords (front + side nodes, including detailed facial feature descriptions)
- Expression anchor list
- Prop anchor list
- Scene planning
- Visual style

**Check canvas scene images before Step 4a**: Use search_canvas_nodes to check whether the canvas already has scene image nodes. If they exist, directly reuse the existing scene image nodes as background anchors, and note in the style lock card "reusing existing scene images" without regenerating scene images.

Step 4b · Generate storyboard sketches:

Model: Lib Image / Aspect ratio: 16:9 / Quality: 2K
Each video segment corresponds to one independent 9-grid storyboard sketch. Generate the 1st sketch separately first; after the user confirms the style, generate the remaining sketches in parallel. From the 2nd sketch onward, you must reference the 1st sketch node to lock the drawing style: "Pure pencil sketch line-art style, no coloring, no grayscale shading, with a drawing style fully consistent with {{1st Sketch Node}}"

Storyboard sketch narrative rhythm rules:

- Last panel of a non-final sketch: no closing signals allowed; the action must remain in progress
- Last panel of the final sketch: only here may a freeze-frame ending appear

After sketch generation, the Agent proactively self-checks:

- Whether all sketches share a fully consistent drawing style
- Whether character facial features stay consistent across all panels
- Whether the last panel of a non-final sketch contains a closing signal
- Whether adjacent sketches connect naturally in narrative

Step 4c · Emotion Transition Sketches (additionally generated for key emotional turning points)

### Step 5 · Video Generation

Model: Seedance 2.0 / Aspect ratio: user-specified / Quality: 720P

Generation pacing: Generate 1-2 segments first for the client to preview; only after confirmation of satisfaction, continue generating the remaining segments.

Video prompt facial lock rules (must be executed): Character facial features are strictly locked; reference the facial design of {{Character Front View Node}}, {if a side view node exists: as well as the side profile of {{Character Side View Node}}, } and facial features must not change with camera angle or shot scale. {If there are close-up shots: close-ups reference the expression of {{Expression Anchor Node}}, presenting the {expression name} state.}

Video prompts must also include:

1. Special body feature locking
2. Multi-character anti-ghosting (mandatory with 3+ characters)
3. Prop single-face principle
4. Additional reference images for physical contact actions

The video generation stage only generates sound effects and dialogue, not background music.

After video generation, the Agent proactively self-checks:

- Whether character facial features stay consistent across all shots
- Whether faces drift or deform in close-up shots
- Whether any special body features have visual errors
- Whether multi-character scenes show ghosting
- Whether the video content matches the storyboard sketches
- Proactively point out any problems found and offer fix suggestions

Criteria for a good video: character facial features consistent across shots with no drift; special body features correct; no ghosting in multi-character scenes; props displayed on the correct face; emotion conveyed effectively.

### Step 5.5 · AI Transitions (optional)

When scene changes are significant, generate 2-3 second transition clips to bridge them, ensuring smooth visuals with no jarring jump cuts.

### Step 6 · Compositing + Background Music

Step 6a · Composite the video + generate background music simultaneously (in parallel):

- videoVolume 1.0, fully preserving sound effects and dialogue

Background music rules:

- Primarily pure instrumental, no Chinese lyrics; character name call-outs may be added to enhance atmosphere
- Duration 2-3 seconds shorter than the video, ending early, endTime -5
- When the user provides a reference audio track, cite the reference audio track node and follow its style and rhythm
- The prompt precisely describes rhythm changes at the time points corresponding to each segment

Step 6b · Standard parameters for overlaying background music:

- videoVolume: 1.0 / audioVolume: 0.4\~0.8 / decibel: -12\~-6 / endTime: -5

Special case (the video's original audio has noise):

- Lower videoVolume (e.g., 0.6) to suppress the noise, but do not completely remove character sound effects
- You must inform the user of the impact of this operation

If the music rhythm does not match the visuals:

- Option A: Regenerate the background music with a more precise description of rhythm nodes
- Option B: Lower the background music volume, letting sound effects take the lead

### Step 7 · Intro & Outro (optional)

Intro: dynamic entrance of the story title, 3-5 seconds, Seedance 2.0 / 480P Outro: title + character freeze frame, 3-5 seconds, Seedance 2.0 / 480P

### Step 8 · Video Cover Design (optional)

Generate when the user needs a cover:

- Size: user-specified (commonly 3:4 portrait, 4:3 landscape, 16:9 landscape); multiple sizes can be generated simultaneously
- Reference character nodes and scene/prop nodes to keep designs consistent
- Follow the style of the user-provided cover reference image (if any)
- Cover design key points: a three-panel storyboard collage or a single large close-up composition; highly saturated, dynamic color tones; title text may be added
- Criteria for a good cover: character design consistent with the video; impactful composition; color tone unified with the video style; title clearly legible

### Step 9 · Final Compositing

In order: intro (if any) → each main video segment → outro (if any); after compositing is complete, update the task status to completed.

## Output

- Step 1: story direction confirmation text
- Step 2: character full-body art image nodes (front + side/3-4 side views); skip if the canvas already has character three-view sheets
- Step 2.5: expression anchor image nodes (Lib Image) + prop anchor image nodes
- Step 3: complete script outline text (confirmed in the chat panel)
- Step 4: style lock card + storyboard sketches (one per segment) + emotion transition sketches; reuse existing scene images on the canvas if present
- Step 5: video nodes (720P, 1-2 preview segments first, continue after confirmation)
- Step 6: composited video node (with background music)
- Step 7: intro/outro nodes (optional)
- Step 8: cover image nodes (optional, multiple sizes supported)
- Step 9: final composited video node

## Self-Check

- \[ \] Story direction confirmed, or the user's script/reference video faithfully recorded
- \[ \] Before Step 2, checked whether the canvas already has character three-view sheets/full-body art; if so, reuse and skip generation
- \[ \] Before character generation, asked the user to choose V8.1 or V7 and explained the advantages of both
- \[ \] Character full-body art generated with front + side multi-angle views; facial feature descriptions detailed and accurate
- \[ \] Multi-character designs clearly differentiated yet stylistically unified
- \[ \] Expression anchors generated for key exaggerated expressions, using the Lib Image model
- \[ \] Key props identified and anchors generated by type; single-face principle executed
- \[ \] Before Step 4, checked whether the canvas already has scene images; if so, reuse and skip generation
- \[ \] Each script segment has only 3-4 core actions, not dense
- \[ \] The script has a clear three-act structure with an emotional arc of ups and downs
- \[ \] Style lock card output and confirmed by the user
- \[ \] The 1st sketch generated separately first; the rest generated in parallel after the user confirms the style
- \[ \] From the 2nd sketch onward, each sketch references the 1st sketch's node to lock the drawing style
- \[ \] The last panel of every non-final sketch has no closing signal
- \[ \] After sketch generation, proactively self-checked style consistency and narrative flow
- \[ \] Video prompts include facial feature locking (front + side nodes), expression anchor references, special body features, multi-character anti-ghosting, and the prop single-face principle
- \[ \] Video generation previews 1-2 segments first; continue after confirmation
- \[ \] After video generation, proactively self-checked for facial drift, visual errors, and ghosting
- \[ \] The video generation stage contains only sound effects and dialogue, no background music
- \[ \] Background music primarily pure instrumental, shorter than the video, endTime -5
- \[ \] Cover generated in the corresponding size(s) (if needed)
- \[ \] Final compositing order correct
- \[ \] All node_key values are real tool return values
- \[ \] After each step, proactively self-check first, then offer A Revise / B Next step

## When to Ask the User

- Story direction / script not provided → Step 1 presents choices across multiple categories
- Character gender, type, number, age → must ask before Step 2 (only when there are no existing character assets)
- Character generation model choice (V8.1 / V7) → must ask before Step 2 generation and explain the advantages of both (only when there are no existing character assets)
- Target duration, video aspect ratio → must ask before Step 2
- Whether dialogue lines / narration are needed → ask before Step 3
- Whether a video cover is needed and its size → ask after Step 6 is complete
- Sketch has questionable points → proactively point out, ask whether to regenerate
- Video facial drift or glitches → proactively point out, offer fix suggestions
- Whether AI transitions are needed → ask after Step 5 is completed
- Whether opening and ending credits are needed → ask after Step 6 is completed
- Step 2 character plans (A/B/C/D) → must wait for user selection before generating
- Script outline → must wait for user confirmation before generating sketches
- After every 1–2 video segments are generated → ask whether satisfied, confirm before continuing to the next batch
- After each step is completed → first proactively self-check, then offer A to make modifications / B proceed to the next step
- Platform does not support Niji 7 → inform the user and confirm a replacement model