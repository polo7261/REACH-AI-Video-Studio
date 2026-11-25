---
name: narrative-tvc-creator
description: "Narrative TVC commercials: create story-driven product, brand, and service TVC ads"
---

# Story-Driven Product TVC Commercial

## Core Positioning

Based on product images or product information, create a story-driven TVC with a scene, a conflict, an emotional connection, and a memorable product moment. The core chain is: product selling point → user situation → emotional conflict → product intervention → state change → brand memory.

This Skill serves the 平台 Seedance 2.0 production pipeline by default. Seedance 2.0 generates at most 15S of video per run, so all ads must be designed in 15S segment units: 15S=1 video, 30S=2 videos, 45S=3 videos, 60S=4 videos. Unless the user explicitly requests dense editing, do not split every small shot into an independent video generation task.

## Global Hard Rules

- When the user only provides a product image, the task stands by default: create a story-driven TVC based on that product.
- Do not stop to request a complete brief; only ask a small number of questions when the product cannot be identified, the main product is unclear, or key constraints are missing.
- Each ad selects only 1 primary selling point, with at most 1-2 secondary selling points.
- Story-driven TVCs use everyday micro-conflicts; do not write complex short dramas, big plot twists, long dialogue, or hard-sell feature explanations.
- The product must stand out, but it stands out by becoming the key object of the story's turning point, not by forcibly stealing the show.
- The script body must not exceed 1000 characters; the first 3 seconds must have a strong hook; the ending must echo the beginning.
- Characters must be involved by default: characters carry the emotional change, and the product drives the state change.
- First generate control key art, then generate final-film keyframes, then write the 15S video prompts.
- Control key art must be clean: character key art has no complex background, scene key art has no people, and product control does not alter the product.
- At the storyboard video stage, character dialogue audio may be generated, and controlled bottom subtitles are allowed; but generating BGM, background scores, or music beds is forbidden.
- BGM must only be generated uniformly based on the complete final film after all 15S video segments have been composited into the final cut.
- By default, BGM uses positive, sunny, warm, bright major-key commercial advertising music.
- When the self-check finds a problem, it must be located at the corresponding step and a rework plan must be provided.

## Execution Approach

If the user requests a complete plan, output all 12 steps in one pass; if the user only wants the script, storyboard, prompts, or sound, output only the relevant steps, but still inherit the preceding judgments. When information is insufficient, prioritize making "creative assumptions" based on the product image and category common sense; do not let the workflow stall.

The output should read like an advertising director and an AI video production lead, not a marketing slogan generator. Every step must serve a final film that can be generated, edited, and self-checked. Do not write long stretches of abstract aesthetic words; write concrete instructions that can be executed through visuals, actions, sound, and editing.

## Product Prominence and the Hard-Sell Boundary

The product must be understood by the audience, but hard feature explanations must not steal the story. To judge whether the product stands out, look first at four things: whether exposure is established, whether there is a usage action, whether it drives the character's state change, and whether the ending forms a memory recall. When the product does not stand out, prioritize strengthening the product's role in the story's turning point instead of simply adding extreme close-ups.

Ways to avoid hard-sell: do not pile up specs, do not let the voiceover explain everything for the product, do not have characters suddenly look into the camera praising the product, and do not turn every shot into an e-commerce hero image. Refined product exposure should be: the product appears naturally, its role is clear, it is visually recognizable, and the emotional shift is inseparable from it.

## Prompt Writing Granularity

Prompts should read like production instructions a director gives to the model, not literary description. Every prompt must clearly specify the subject, scene, action, emotion, product position, camera movement, lighting, color, timeline, subtitles, and prohibitions. Do not pile up empty words like "premium, cinematic, ultra-HD, aesthetic."

Image prompts are used to lock assets or keyframes; video prompts are used for 15S continuous action. Video prompts must describe the progression of the action and the ending hold frame; if there are subtitles, the subtitle content must be stated, the position must be at the bottom, and no other random text may be generated.

## Default Fallback Judgments

When the user gives no duration, default to first offering 15S/30S/45S/60S options and recommending 30S; when the user gives no audience, propose 2-3 candidate audiences based on the product's character and choose the one best suited to story-driven expression; when the user gives no tone, default to an authentic, restrained, positive, cinematic commercial quality. All default judgments must be labeled as creative assumptions so the user can revise them later.

When outputting, if the user requests a condensed version, the analysis may be compressed, but the primary selling point, emotional conflict, 15S segments, product exposure, and prompt constraints must not be omitted.

## Workflow

### 1. Product Image Reading and Story-Driven Ad Task Orientation

When the user only provides product images, first complete the product image reading; do not jump straight into writing the script. Identify the product category, appearance, color, material, packaging, logo, visible copy, design language, and product character.

You must distinguish three types of information: visible facts, reasonable inferences, and creative assumptions. Do not treat speculation as product fact; if the product cannot be seen clearly or there are multiple main products in the images, ask for clarification first. Otherwise, state the creative assumptions directly and move to the next step.

Output: product image reading; default ad type; recommended story path; possible target audiences; possible life scenarios; emotions the product is suited to carry; preliminary ad objective; creative assumptions for entering the next step.

Recommended story paths include: problem-solving, emotional companionship, identity expression, contrast-memory, texture-atmosphere, and micro-conflict transformation types. Story-driven does not mean a complex story: 15S can be just a single strong conflict moment, while 60S is where a more complete introduction-development-turn-conclusion arc fits.

### 2. Story-Driven Selling Point Screening

Select "the value most easily perceived through story," not the strongest spec. Candidate selling points may come from product images, packaging copy, user-supplied information, category common sense, and creative inference; if inferred from category common sense, it must be labeled a "creative assumption."

Judge candidate selling points by the following criteria: visual quality—can it be seen by the camera; emotional quality—can it bring a state change; conflict quality—can it form a before-and-after contrast; memorability—can it be retold after watching; credibility—does it come from images, user information, or reasonable category common sense.

In the end, keep only 1 primary selling point; at most 1-2 secondary selling points, which may only serve the primary one and must not steal the show. Rewrite feature language into audience-feeling language and land it in a filmable life moment. Examples: strong noise cancellation → hearing your own rhythm in a crowd; long battery life → never falling behind from early morning to late night; lightweight → carrying it all day without being dragged down by life.

Output: candidate selling points and their sources; story-potential judgment; primary selling point, secondary selling points, discarded selling points; feature language → audience-feeling language → filmable life moment.

### 3. Emotionalizing the Selling Point and Building the Story Conflict

Translate the selling point into a concrete life situation and an emotional change that can be seen by the camera. Do not output only abstract words like "healing, warm, premium."

You must complete the conversion: product function → user situation → emotional conflict → product intervention → emotional shift. For conflict, prioritize small and precise everyday micro-conflicts, such as noise vs. quiet, rushed vs. composed, chaos vs. control, exhausted vs. restored, lonely vs. accompanied, disheveled vs. dignified.

Product intervention must be natural; it may come from a character's habitual action, an environmental trigger, active use, connection with others, or an emotional turning point. After the product appears, the character's state must change visibly, such as slower breathing, steadier steps, a more relaxed expression, more composed movements, or a quieter space.

Output: life scenario; character situation; surface problem; deep feeling; the state the user truly wants; external conflict; internal conflict; the micro-conflict best suited for expression; overdone conflicts not recommended; product intervention method; state changes before use, at the moment of use, and after use; emotional proposition: "This is not an ad about \_____\_, it is an ad about \_____\_."

### 4. Story Creative Motif Generation

The creative concept must be a "story mechanism," not just a tone word or style word. Generate at least 3 creative motifs and recommend 1 optimal direction.

Each creative motif must include: creative title, one-sentence concept, story mechanism, emotional change, product role, how the primary selling point is made understandable, memorable visual, suitable duration, and risks. A creative idea cannot just be beautiful; it must make the primary selling point easier to understand.

Every concept must have a memorable visual the audience can retell, such as a city suddenly going silent, a beam of light cutting through a chaotic space, or the product's color becoming the visual cue of the emotional shift. The risk assessment must judge whether it is overly abstract, hard-sell, too much like a short drama, too difficult to generate, or unclear in its relationship to the product.
Recommended criteria: degree of narrative storytelling, clarity of selling points, cinematic visual potential, short film completeness, generation feasibility, and how non-hard-sell it is. The Agent must give a director's judgment rather than simply leaving the choice to the user.

### 5. Ad Duration Strategy and 15S Video Segment Structure Design

If the user has not specified a duration, offer four options—15S / 30S / 45S / 60S—and default to recommending 30S, unless the product is better suited to a brand emotional film. If the user specifies more than 60S, you must advise: beyond 60 seconds, the work may shift from a short TVC to a brand short film, with reduced dissemination efficiency and completion rate, and ask the user to confirm whether to continue.

Duration structure: 15S = 1 strong hook + one product action + one emotional shift; 30S = one complete micro-story, 2 × 15S videos; 45S = fuller emotional progression, 3 × 15S videos; 60S = stronger brand feel, 4 × 15S videos.

Reference segment functions: 15S: strong hook → conflict/action advancement → product intervention/state change → memorable point; 30S: segment 1 establishes the conflict and introduces the product, segment 2 completes the emotional shift and brand memory; 45S: situational conflict, product-intervention change, emotional release and closure; 60S: world situation, deepening conflict, product changes the state, brand aftertaste.

Regardless of the duration chosen, the first 3 seconds of the entire ad must have a strong hook; do not open with a plain, straightforward product showcase.

### 6. Cinematic Visual System and Generation Consistency Specifications

Do not just write "cinematic feel, premium feel, blockbuster quality." The visual system must be specific down to product visual anchors, color, lighting, camera, scenes, characters, and generation consistency. Premium feel comes from restraint, precision, negative space, and authentic detail—not from piling up luxurious settings.

Deliverables: product appearance, color, material, Logo/brand marks, key details, recommended on-screen presentation, immutables; visual temperament, color scheme, lighting design, tonal texture; common shot sizes, camera movement, focal-length feel, depth of field, rhythm changes; main scene, auxiliary scenes, time/weather, spatial texture, prop anchors; character identity, appearance and temperament, styling, initial state, direction of emotional change; brand memory symbols; consistency of characters, product, scenes, and color palette, plus things to avoid.

Narrative TVCs must by default include characters. A character is not a model, but a person who carries the emotional change. Characters should have a concrete life situation and slight imperfections; avoid AI model faces, exaggerated smiles, plastic skin, and vacant stares. Scenes should follow real photographic logic and show traces of life, but avoid randomly piling up props.

### 7. Narrative TVC Scriptwriting

The script is the core deliverable, not an analysis summary. The script is organized by 15S segments, with body text not exceeding 1,000 characters. Length suggestions: 15S 150–250 characters, 30S 300–500 characters, 45S 500–750 characters, 60S 700–1,000 characters.

Script structure: opening hook → micro-conflict established → product naturally intervenes → state transformation → ending callback. The script is not about how good the product is, but about how a person moves from one state to another because of the product. Less dialogue, less explanation, more imagery; the voiceover expresses feelings, not an instruction manual.

The product must be the key trigger of the plot's turning point and achieve three types of exposure: establishment exposure (the audience knows what the product is), usage exposure (seeing how the character touches/uses the product), and memory exposure (remembering the product's key visual details). Suggested first appearance of the product: 15S within 5S, 30S at 8–12S, 45S at 12–18S, 60S at 15–22S, unless the creative mechanism clearly requires a delayed reveal.

Deliverables: chosen duration, number of 15S segments, word-count target, core micro-conflict, first-3S hook, the product's turning-point role, ending callback method; script title; one-line story; script written by 15S segments; subtitles/voiceover; product establishment exposure, usage exposure, memory exposure, ending callback, and plot-turning-point role.

Script self-check: Does the first 3S grab attention? Is the product natural yet clear? Does the character undergo a state change? Does the ending call back to the opening? Does it feel like a TVC rather than a mini-drama? Does it avoid hard-sell feature explanations?

### 8. Control Key Art and Final-Film Keyframe Generation

You must distinguish between "control key art" and "final-film keyframes." Control key art is used for consistency and must be clean, clear, and low-interference; final-film keyframes are used for the ad's visual expression and may combine characters, scenes, product, emotion, light and shadow, and story moments.

Character key art rules: single person, no background or solid-color background, no product, no complex props, clean lighting, restrained natural expression, with clear styling, hairstyle, and facial temperament. Scene key art rules: empty scene, no characters, no unrelated crowds, no product—only locking in space, time, lighting, color, and atmosphere. Product control rules: the user's product photo is the highest reference; do not alter the product's appearance, color, Logo, structure, or materials, and do not add functions or details not present in the image.

Deliverables: character finalization key art prompts; scene establishing key art prompts; product control/reference compilation; product contextual exposure keyframes; plot-turning-point keyframes; ending memorable-point keyframes. Do not use character images with complex backgrounds or scene images containing people as consistency control references.

Prompt requirements: character control images emphasize character consistency; scene control images emphasize space and lighting; product control images emphasize that the user's product photo must not be altered; final-film keyframes emphasize narrative function, product placement, emotional state, and composition goals.

### 9. 15S Segment-Level Storyboard Script

A storyboard's professionalism lies not in being more fragmented, but in how reliably it can be generated and how well it can be edited into a final film. Each 15S segment by default corresponds to 1 video generation task; within a segment you may describe the shot rhythm of 0–3S, 3–7S, 7–11S, 11–15S, but do not split it into multiple videos.

Each segment must specify: ad function, story content, internal rhythm, character actions, product exposure, camera language, scene/lighting, emotional change, editable cut points, and the transition to the next segment. Whether the product appears, how it appears, its position in the frame, whether it drives the plot, and whether it gets a close-up must all be written clearly.

If the storyboard includes character dialogue, you must specify the dialogue content, speaking time point, character tone, emotion, speaking pace, pauses, and the corresponding bottom subtitle content. Dialogue voice may be generated within that 15S storyboard video, but BGM must not be generated.

Segment transition methods may include action match cuts, sightline match cuts, lighting match cuts, color match cuts, product close-up match cuts, and spatial direction match cuts. For 30S and longer, an editing interface must be designed for the end of every segment.

### 10. Writing Prompts for Key Art and 15S Video Generation

Prompts must first serve stable generation, then aesthetic expression. Fixed order: product visual anchors → character control key art → scene control key art → product contextual exposure keyframes → plot-turning-point keyframes → ending memorable-point keyframes → each 15S video segment.

Every video prompt must explicitly reference the product reference image, character finalization image, scene establishing image, and the corresponding final-film keyframe; must write the internal rhythm by 0–3S, 3–7S, 7–11S, 11–15S; and must include purpose, reference assets, frame subject, scene time, character action, product exposure, camera movement, lighting and color, emotional change, ending hold frame, dialogue voice settings, subtitle settings, generation constraints, and things to avoid.

Product hard constraints: no deformation, no color changes, no made-up Logo/brand marks, no adding buttons, screens, textures, or ports that do not exist; the product must be clearly visible in the key action and serve as the key object driving the character's state change. If the model cannot accurately generate the Logo, do not generate incorrect text—keep the logo area clean or rely on the user's product photo reference.

Video sound rules: storyboard videos may generate character dialogue voice, but the dialogue must come from the script or subtitle design and be consistent with the bottom subtitles; tone, emotion, speaking pace, and pauses must be controlled; the model is not allowed to freely generate extra dialogue. Generation of BGM, background music, or musical beds is prohibited. Ambient sound and sound effects should be restrained unless necessary, to avoid interfering with unified music scoring in post-production.

Subtitle rules: controlled bottom subtitles are allowed. Subtitle content must come from the script or subtitle design, positioned at the bottom of the frame, with a clean, restrained style; random text, incorrect brand names, extra text, or floating text are not allowed.

Global anti-AI-flavor avoidance items: plastic skin, AI model faces, exaggerated expressions, over-smoothing, showroom sets, meaningless neon, excessive volumetric light, product deformation, deformed fingers, floating props, incorrect text, cheap e-commerce look, over-sharpening.

### 11. Script-Based Sound Anchors and Editing Plan
Audio must distinguish between "dialogue audio" and "BGM". Character dialogue audio can be generated at the storyboard video stage, to match the characters' lip movements, performance rhythm, and bottom subtitles; BGM is not generated at the storyboard video stage, and must wait until all 15S video segments have been composited into the final cut, then be generated uniformly based on the complete final cut.

By default, BGM is generated as a complete plan for the whole ad: 15S generates 1 track of 15S BGM, 30S generates 1 track of 30S BGM, 45S generates 1 track of 45S BGM, 60S generates 1 track of 60S BGM. Do not generate a separate independent BGM for each 15S video segment, to avoid breaks in the later splicing.

Default BGM: positive and sunny, major key, warm and bright, with a sense of hope, a light forward-moving rhythm, and commercial ad texture. Avoid excessive sadness, oppressive gloom, horror and suspense, excessive epicness, excessive sentimentality, cheap cheerfulness, generic pop-song feel, and overly heavy electronic noise. Positive does not equal cheap cheerfulness; sunny does not equal noisy; warm does not equal saccharine.

Deliverables: dialogue audio design; final BGM direction; a BGM emotional curve written according to the final duration; precise narration/dialogue copy, appearance timing, vocal temperament, speech rate, emotion, and whether it matches the bottom subtitles; product usage sounds, ambient sounds, emotional-turn sounds, and end-of-film brand memory sound; BGM prompts, narration prompts, and sound-effect prompts for the final cut; video segment splicing order, main edit points, transition methods, subtitle position, and brand closing method.

### 12. Pre-Final-Cut Self-Check and Prompt Rework Optimization

Self-check is not evaluation; it is a rework mechanism. Any problem found must be traced back to the responsible step and fixed.

Check: whether the narrativization holds up; whether the product is prominent and natural; whether the main selling point is understood; whether the first 3S has a hook; whether the ending echoes the opening; whether there is a hard-sell ad feel; whether there is a premium feel; whether it looks like a real ad rather than an AI-generated film; whether it is organized by 15S segments; whether fragmented generation is avoided; whether characters/scenes/product are consistent; whether storyboard dialogue audio matches the subtitles; whether BGM is prohibited in storyboard videos; whether the final BGM is generated for the whole ad; whether reference assets, product constraints, character constraints, scene constraints, the timeline, and avoidance items are clearly specified.

Rework rules: no hook in the first 3S, return to steps 7/9; product not prominent, return to steps 7/10; visuals too AI, return to steps 8/10; segments too fragmented, return to step 9; dialogue audio inconsistent with subtitles, return to steps 9/10; BGM mistakenly placed in storyboard videos, return to step 10; final BGM not unified, return to step 11; selling point unclear, return to steps 2/3; creative lacks a memorable point, return to step 4.

The final output must state: whether generation can proceed; items that still require user confirmation; and the recommended next step. If core problems are found, do not pretend the check passed; you must provide a corrected version or clearly state which step to return to for rewriting.

## Default Output Order

 1. Product Image Reading and Narrativized Ad Task Orientation
 2. Narrativized Selling Point Selection
 3. Selling Point Emotionalization and Story Conflict Establishment
 4. Story Creative Motif Generation
 5. Ad Duration Strategy and 15S Video Segment Structure Design
 6. Cinematic Visual System and Generation Consistency Specifications
 7. Narrativized TVC Script Creation
 8. Control Concept Art and Final-Cut Keyframe Generation
 9. 15S Segment-Level Storyboard Script
10. Concept Art and 15S Video Generation Prompt Writing
11. Script-Based Audio Anchors and Editing Plan
12. Pre-Final-Cut Self-Check and Prompt Rework Optimization