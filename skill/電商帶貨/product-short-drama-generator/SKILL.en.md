---
name: product-short-drama-generator
description: "Viral product short drama: turn a single product photo into a finished ~15-second, 3-shot shoppable drama video"
---

---
name: product-short-drama
namespace: libtv-industry
title: "Shoppable Short Drama"
description: "Upload one product image, produce a shoppable short-drama video"
version: 4
---

# product-short-drama

## Skill Positioning
- Solely responsible for: converting one product image into a finished 3-shot, ~15-second shoppable short drama (script → assets → storyboard images → storyboard videos → edited final cut), fully automated in a single run with no user confirmation along the way. Not responsible for product selection, ad placement strategy, or multi-episode serialization.

## Input
- What is needed:
  - Required: one product image
  - Optional: product name and core selling points, target audience, style preference (live-action/anime/3D, etc.), dialogue language

## Input Usage
- Strictly adhere to:
  - The uploaded original image is the sole standard for product appearance — when generating storyboard images, the original image must be used as the reference asset; the model is forbidden from improvising the product's shape, color, logo, or packaging
  - User-stated selling points and target audience (they determine the plot direction and must not be deviated from)
  - Fixed specs: 3-shot structure, ~5 seconds per shot, ~15 seconds total, 9:16 vertical
- For reference only:
  - Product category and selling points inferred from the image — inference may be wrong; note the assumptions in the creation notes of the final output
  - When style preference is unspecified, choose yourself the style best suited to the product, and explain the reasoning in the output

## Internal Workflow and Knowhow

The deliverable of this skill is not "verbally outputting a script and images," but **building a node graph on the platform canvas that runs automatically**. Each step below corresponds to one or a group of nodes on the canvas; every step must be materialized as nodes and wired together so one run completes the entire pipeline — not steps kept in your head.

- **Node chain (upstream → downstream)**: Script node (text) → Asset nodes (character design images, scene image) → Storyboard image nodes ×3 ("Plot Deduction 4-Panel," one 4-panel image per shot) → Storyboard video nodes ×3 (audio-visual sync model, e.g., Kling) → Editing node (assembles one complete final video, the sole final output of the entire graph)
- **Wiring principles (wired correctly = runs automatically)**:
  - Connect upstream output to downstream input; once the whole chain is connected, **one run executes node by node automatically — do not start nodes manually one by one**
  - The original product image, as a reference asset, feeds into every storyboard image node
  - The script node's text is distributed to the asset, storyboard image, and storyboard video nodes, each pulling the fields it needs (anchors, actions, dialogue, etc.)
  - **Cross-shot interlocking (the sole continuity rule)**: the **last panel** of the previous shot's storyboard image node serves as the reference image input for the next shot's storyboard image node, so the next shot's first panel continues from the previous shot's last panel; the video's first frame uniformly takes panel 1 of the current shot's 4-panel image. No separate video last-frame handoff is set up, to avoid conflicting rules
  - The outputs of the 3 videos converge into the editing node
- **Acceptance criterion**: the finished graph must achieve "one-click run of the wiring, no per-node manual starts, and the terminal editing node directly outputs one complete final video." If a step exists only in text with no corresponding node on the canvas, it's a missed build — add it.

### 1. Product Understanding
- From the product image, identify: category, form (handheld/wearable/placed for use), target audience, and determine the product type:
  - **Emotion-type** (jewelry, handmade goods, apparel accessories, low-ticket daily items): sells identity and the "same item" psychology; the plot follows the "product meaning reversal" route
  - **Function-type** (digital devices, home appliances, daily items with hard selling points): sells a solution; the plot follows the "real pain point → resolution" route
- Product type determines the plot strategy — this is the first and most important judgment of the whole piece
- When choosing selling points for function-type products, visually actable ones (insulation → rising steam, portability → pulled out with one hand) take priority over ones requiring narration (ingredients, specs)

### 2. Story Script Writing (Script Node, 3-Shot Structure)
What this step produces is **the output text of the script node on the canvas**: a structured script for the downstream asset, storyboard image, and storyboard video nodes to pull from — not a mental draft.

Short drama structure and product integration are two separate layers of technique — learn them separately, stack them when applying:
- First read `references/drama-script-examples.md` (breakdowns of real short dramas) to calibrate the feel for hooks, twists, and pacing
- Then read `references/product-integration.md` (product integration methodology) to turn the product into a functional component of the plot
- The order must not be reversed: write a story that stands on its own first, then validate the integration; if you think "how to sell" before crafting the story, the result will inevitably be a hard-sell ad

- Shot 1 (hook, 0-5s): open with conflict; the first 2 seconds must grab attention. The hook can be dialogue conflict (humiliation, eviction) or a **dialogue-free visual hook** (an in-your-face close-up at peak emotion right at the start, or a character staring at something to create an information gap). The product has only two possible entrance identities: **conflict focal point** (humiliated, snatched, looked down upon — the proven mainstream play; the moment the product enters the frame, the conflict is established) or **suspense object** (held back until the twist reveals it). It must never open as a "displayed item"
- Shot 2 (twist, 5-10s): the essence of the twist is **the product's meaning being flipped** — the demeaned thing turns out to be an identity token / key prop / solution. The product is the pivot of the twist, brought out through a plot action (revealed, pulled out, raised up); give it a close-up, but the close-up must happen within an action
- Shot 3 (release, 10-15s): emotional release (comeuppance / vindication / a warm landing). For emotion-type products, no selling-point dialogue appears in the main body — the gratification itself is the selling point; for function-type products, the selling point rides on the emotion, and it only passes if it still sounds like natural speech with the product name removed
- The criterion for whether the integration is natural: **remove the product from the plot — does the story still hold?** If it holds, the product is merely an overlay; rewrite until the product becomes the pivot of the twist
- Write the brand name into the story world: the in-drama group/family name directly uses the brand name (e.g., brand "Dingdang Isle" → "Dingdang Isle Group"), so the dialogue advances the plot while repeating the brand with zero ad feel
- Dialogue: ≤ 2 lines per shot, ≤ 15 characters per line, all in "plot language" (belittling, showdown, verdict, revelation) — not a single line addressed to the audience. The dialogue will be fed into downstream video nodes where the audio-visual sync model generates the talking visuals, so every line must clearly mark its **speaker**
- **The 3 shots are one continuous scene, not three posters**: the whole piece takes place in the same scene; shots connect through continuous characters and continuous action/gaze (Shot 1's action is picked up in Shot 2, Shot 2's state is resolved in Shot 3). The plot must flow continuously — this is the prerequisite for cross-shot visual interlocking later
- The script annotates each shot: scene, characters, emotion, key actions, **dialogue and speakers**, how the product appears, **the connection point with the previous shot** (continuing from the state at the end of the previous shot; may be empty for the first shot)
- Conversion copy ("get the same one," etc.) goes into the deliverable's **title copy**, not into the plot

### 3. Asset Anchor Creation and Usage (Asset Nodes)
- Characters: 1-2 people (15 seconds cannot fit more); write one anchor description per character (appearance, clothing, signature features), and generate character design images
- Scene: **the whole piece uses only 1 scene** (one short piece sticks to one scene; multiple scenes easily turn chaotic and drag down cross-shot consistency). All 3 shots happen in this single scene; create a sense of cinematography through shot scale/camera position changes, with no scene changes. Generate 1 scene image and reuse it from start to finish
- Product: directly use the user-uploaded original image as the reference asset; **do not regenerate a product image**
- Once the anchor text is written, all subsequent prompts reuse the exact same passage without changing word order — this is the foundation of cross-shot consistency

### 4. Storyboard Creation (Storyboard Image Nodes)
Each shot produces one **4-panel storyboard image**: in the platform storyboard image node, select the **"Plot Deduction 4-Panel"** option, and unfold the shot's main action over time into 4 panels (start → progression → end), clearly laying out this shot's motion trajectory. It serves as the **motion basis** for the downstream video node — the video receives a clearly decomposed action sequence rather than an information-vague single image, making generation more accurate and controllable.
- **Must use the "Plot Deduction 4-Grid" node option**: one shot = one 4-panel image. Do not use ordinary text-to-image to generate the panels one by one, otherwise the storyboard image node will spit out a big pile of scattered images at once and go out of control
- Generation references: character/scene anchors + original product image
- **4-panel deduction**: break this shot's subject action down into 4 time steps; the panel order is the chronological order. Example: Shot 2 "taking out the keepsake" → hand reaches toward the pocket → draws it out → raises it → holds still. Each panel is one instant of the action
  - Only deduce **controllable actions** (turning the head, raising, taking out, handing over, expression changes); conflict actions (hitting, grabbing, smashing, yanking) are not deduced—leave them to "implied action" (see below), expressed as "state before the action → (skip the conflict moment) → state after the action"
- **Shot-to-shot relay (the only continuity rule—do not introduce a second one)**: **the last panel's state of the previous shot's 4-panel grid = the first panel's state of the next shot's 4-panel grid**. When writing the next shot's storyboard image prompt, panel 1 must carry over the picture from the previous shot's panel 4 (same scene, a continuation of the same character poses and positions), and the previous shot's last-panel image must be fed in as the reference image for the next shot's storyboard image node to guarantee a tight match. The whole film takes place in one scene, so the relay only needs to align character poses and the product's position
- **Storyboard image prompt (its own standalone set, written separately from the video prompt; describe the picture itself only—no camera movement, no dialogue)**:
  - Structure: style prefix + character anchor + scene anchor + product integration method + a 4-step time breakdown of this shot's action + shot size/composition + lighting mood
  - Write only "what these 4 panels look like": appearance, positioning, posture, expressions, lighting. Camera movement and dialogue are the video node's business—not one word about them here
- Shot-size design: shot size is the emotion volume knob—emotional peaks get extreme close-ups; conveying information gets wide/medium shots. Shot 1 uses a medium close-up to establish the conflict (or an in-your-face close-up gives the emotion first, then pulls back for information); Shot 2 is the product's entrance—use a close-up or close shot to give the product full presence; Shot 3 closes with the character and the product in the same frame
- **Implied action**: conflict actions (hitting, grabbing, smashing, yanking) are not drawn directly; draw the state changes before and after the action (a face mid-roar → cut → a tearful face with a slap mark) and let shot cuts let the audience fill in the rest. Complex body movement is the part AI generation breaks most easily; state changes are the most stable part
- Let state details tell the story: wounds, tears, changes in the eyes, messy hair—they convey what happened without any dialogue; write them into the storyboard image prompt
- Self-check after each image is generated: does the product's appearance match the original image (shape, color, logo), does the character match the character design sheet, does the first panel pick up the previous shot's last panel? If anything is off, first check whether an anchor was rewritten, then regenerate that shot—don't blindly reroll

### 5. Storyboard Video Generation (Storyboard Video Node)
- **Model**: use an **audio-visual sync model (e.g., Kling)** so the characters' dialogue produces talking shots with matching lip movement—this is the key to getting dialogue into the film; don't use a model that doesn't support audio-visual sync
- **First frame (one uniform rule, no exceptions)**: every shot uses **panel 1 of this shot's 4-panel grid** as its first frame. Shot-to-shot continuity has already been locked in at the storyboard image step via "previous shot's last panel = next shot's first panel"; no separate continuation rule is set up here, to avoid two rules clashing and making the images mismatch
- **Video prompt (its own standalone set, written entirely separately from the storyboard image prompt—no sharing, no copying)**: describe only "movement + dialogue"; do not repeat the static information already present in the first frame (appearance, positioning, and lighting are not written out again)
  - Structure: camera movement (push in / pull out / pan / follow—pick one) + subject action + dialogue and speaker
  - **Action follows the 4-panel grid**: the trajectory of the subject action = the one deduced in this shot's 4-panel grid; generate along the motion path of the 4 panels and don't let the video model improvise—this is where "break the image down finely and the video comes out accurate" pays off
- **Audio (you want vocals, not a soundtrack—state the two things separately and clearly)**:
  - **Must have**: the **speaking voice / dialogue audio** of the characters saying their lines (sound present, lips in sync—not a silent film)
  - **Remove only**: background music / BGM / soundtrack
  - Sample prompt wording: "The character speaks the line '...' out loud, lips synced, clear vocal dialogue; no background music, no soundtrack." **Do not write words like "silent / mute / no audio"**—that will suppress the vocals along with the music, resulting in lip movement with no sound
  - Dialogue follows the script, with the speaker marked—no rewriting
- Movement restraint: give each shot only one primary movement (choose one of push in, pull out, pan, follow); stuffing two action beats into 5 seconds is guaranteed to turn messy
- Write only simple, controllable subject actions (turning the head, raising, handing over, speaking, expression changes); leave conflict actions to "implied action"—do not let the video model generate complex body movements like fighting or grabbing
- About 5 seconds per shot

> **The storyboard image prompt and the video prompt must be two separate sets, written apart**: the image prompt writes only "what the picture looks like" (appearance/static), the video prompt writes only "how it moves and what is said" (movement/dialogue). If the two prompts' content is alike = they haven't been split apart; rewrite.

### 6. Video Editing (Editing Node)
- Feed the 3 storyboard videos into the editing node in the order Shot 1 → Shot 2 → Shot 3 and stitch them into one complete finished film
- The editing node is the endpoint of the whole graph; the final output is **one complete video of about 15 seconds**, not 3 loose clips
- Confirm the final film's total duration ≈ 15 seconds and 9:16 vertical

## Output
- What gets produced (a node graph on the canvas, fully wired and runnable automatically with one click, delivered fully automatically in a single run):
  1. Script node: the 3-shot script text (with per-shot annotations, dialogue and speakers, and shot-to-shot transition points)
  2. Asset node: character design sheet and scene image (1 scene for the whole film)
  3. 3 storyboard image nodes: 3 four-panel storyboard images ("Plot Deduction 4-Grid", one per shot, the action split into 4 panels, the last panel of each shot locking into the first panel of the next)
  4. 3 storyboard video nodes: 3 storyboard videos with dialogue (audio-visual sync, spoken dialogue vocals, no background music, about 5 seconds each)
  5. Editing node: **one complete finished film of about 15 seconds** (the final output)
  6. Title copy for publishing (carrying conversion phrasing such as "the same one as in the video", with suggested hashtags)
  7. Creation notes: the product-type judgment, the design rationale behind the integration point, and assumptions made on your own (category inference, style choices, etc.)

## Self-Check
- Is the workflow built right (check this layer first, then the content):
  - Is every step realized as a canvas node: script node, asset node, storyboard images ×3, storyboard videos ×3, editing node—not a single one missing
  - Are all nodes wired up and able to run automatically with one click—no isolated nodes that must be manually started one by one
  - Does the storyboard video node use an audio-visual sync model; does the dialogue make it into the video prompt; is the audio "characters' speaking voices, no background music" (don't write "silent/mute"—that would wipe out the vocals too)
  - Do the storyboard images use the "Plot Deduction 4-Grid" node, one 4-panel image per shot (not scattered images, not 9 panels)
  - Do the shots interlock: the last panel's state of the previous shot's 4-panel grid = the first panel's state of the next shot's 4-panel grid; is the video first frame uniformly taken from panel 1 of that shot's 4-panel grid
  - **Are the storyboard image prompt and the video prompt two separate sets with non-identical content** (the image prompt writes the picture, the video prompt writes movement + dialogue; if they're alike, they haven't been split apart)
  - Does the whole film use only 1 scene
  - Is the final output one complete finished film produced by the editing node (not 3 loose clips)
- Does the content pass:
  - Does Shot 1 have a hook in its first 2 seconds; does the product enter as the "conflict focal point" or the "object of suspense" (never as a mere display item)
  - Is Shot 2's twist a reversal of the product's meaning, and does it make logical sense
  - Integration necessity: does the plot fall apart if you take the product out
  - Are the 3 shots one continuous scene (characters, setting, and action/gaze lines connect), not three isolated posters
  - Is the in-film dialogue completely free of ad-speak (conversion phrasing lives only in the title copy); is each line marked with its speaker
  - In the 3 storyboard images, does the product's appearance match the original image; do the characters match the design sheet
  - Can the dialogue be spoken within 5 seconds (≤ 2 lines per shot, ≤ 15 characters per line)
- Whether each video prompt contains only one primary motion
  - Total duration ≈ 15 seconds, 9:16 vertical

## Ask User
- When to ask the user (fully automatic principle: infer when you can; ask only when truly stuck):
  - The product image is unrecognizable (damaged image, unclear subject)
  - Multiple products appear in the image, and it is impossible to determine which one is being promoted
  - The product involves ad-compliance-sensitive categories (medical devices, health efficacy claims, etc.), and the selling-point wording needs user confirmation
```