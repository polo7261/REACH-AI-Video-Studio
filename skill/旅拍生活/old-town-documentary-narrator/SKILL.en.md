---
name: old-town-documentary-narrator
description: "Old-town humanistic narrative films: small-town culture shorts with understated emotional storytelling and an effortless documentary feel"
---

## name: city-memory-film\\

namespace: industry\
title: "City Memory Narrative Short Film"\
description: "Humanistic narrative short film set in small towns/old neighborhoods—driven by a chain of low-drama everyday events, building emotion through observation rather than dramatic confrontation. Core craft: six methods of script narrative construction (planting suspense threads / characters have history / key objects recurring twice with a changed state / traces left between scenes / subverted expectations / double-meaning ending), character motivation of small dignity with big stakes + roundabout dialogue phrasing, spaces that must carry social information, a three-tier shot duration table (short/medium/long) + five-part rhythm structure, and a dual-route generation strategy of 80% plain-narration first-frame-driven + 20% high-intensity multimodal. Three sets of color grading and lighting for day/night/interior, dual prompt formulas for first frame and video + vocabulary library. 10–16 shots / 1–3 minutes, 16:9 (or 4:3/2.35:1 to emphasize a sense of oppression). Belongs to the documentary-humanist family (listed alongside East Asian art-house film / Jia Zhangke style; their craft systems are mutually incompatible and must not be mixed)."
version: 1

# city-memory-film

Use this skill when making humanistic narrative short films set in small towns/old neighborhoods. **The core is not documenting suffering or nostalgia, but letting the audience feel the change for themselves through the real behavior of specific people in urban space, the recurrence of detail objects, and the causal traces between scenes**—emotion is accumulated through observation, not dramatic confrontation. The ending does not pronounce judgment: give the audience a changed space or action, not a complete answer.

> Environment adaptations: GPT Image / Image 2 → `generate_image_v3`; Happy Horse (FirstFrameToVideo) / Seedance 2.0 (MultiModalToVideo) → `generate_video_v3` (expressing the two routes as "first-frame-driven vs multi-reference + high dynamics"); resource_prepare_and_analyze → the agent does the parsing itself; text_editor → `write_file_v2`; video_assembler → `composite_video`; narration/BGM → `generate_audio`; `@asset` → `reference_nodes`+`{{NodeKey}}`. **Narration method two (generating a narration video with Seedance, then splitting out the audio via multimodal to serve as a subsequent voice-timbre reference chain) has no corresponding capability in this environment and is justifiably removed**—this environment retains the method itself of "narration longer than 15s must be generated in segments"; all segments are generated uniformly via `generate_audio` with identical parameters, without voice-timbre chain extraction. Camera-movement / realism / prompt-writing craft are all inlined in this skill, with no reliance on external craft skills.

## 1. Full-Film Workflow and Stage Dependencies

1. **Story premise acquisition (choose one of two)**:
   - **User has uploaded a script/text material**: the agent parses it itself, extracting character relationships, core conflict, scene list, key event nodes, and key objects. Output a concise one-sentence story premise summary and ask the user to confirm before entering step 2. **Do not enter step 2 before confirmation.**
   - **User has not uploaded material**: collect via card-guided prompts: the place and time period of the story, the core dilemma or decision facing the protagonist, and another key character and their relationship to the protagonist. When information is insufficient, default to: duration 1–3 minutes, genre "short drama film". After collection, output a concise one-sentence story premise for the user to confirm.
2. Confirm with the user and establish Final_Video\_[Spec.md](http://Spec.md) (film title, genre tone, scene setting, aspect ratio, target duration, visual style, output language) → `write_file_v2`
3. Generate the storyboard (key elements, shot list, audio layers). Once the storyboard is ready, scan the context for assets provided by the user or already generated, bind them to the corresponding storyboard slots, then proceed to the generation steps.
4. Set up elements:
   - If the user has uploaded element assets (character reference images, scene reference images): register them as anchors and bind them to the corresponding key elements.
   - Otherwise: generate images for all key characters and scene elements → `generate_image_v3`.
5. Generate the first-frame image (start_frame) for each shot → `generate_image_v3`
6. Generate videos via separate routes by shot type:
   - **Narrative shots 〔plain narration〕 (about 80%)**: first-frame-driven route (Happy Horse intent) → `generate_video_v3`, using the corresponding shot's start_frame as the first-frame input.
   - **High-intensity shots 〔dynamic〕 (about 20%, no more than 20% of total shots)**: multi-reference-driven route (Seedance 2.0 intent) → `generate_video_v3`, citing the corresponding element images as reference.
7. Generate BGM / narration and sound-effect layers → `generate_audio`
   - Narration: generate uniformly with `generate_audio`; if narration exceeds 15s, split it into multiple segments and generate them separately, keeping the same character parameters consistent (voice-timbre chain extraction has no corresponding capability in this environment; see the adaptation notes above).
8. Complete the full-film timeline assembly, aligning narration segments in order to their corresponding positions → `composite_video`

**Dependency order**: 2→1; 3→2; 4→3; 5→3,4; 6→3,5; 7→3; 8→6,7\
**Pause points**: Do not run the entire workflow in one go. Pause after premise confirmation, storyboard completion, element image/first-frame image completion, video batch completion, and audio generation, waiting for user confirmation before continuing.\
**When the user provides media**: prioritize binding it to the corresponding storyboard slots; do not regenerate content the user has already provided.

### Guidelines for Establishing Final_Video\_[Spec.md](http://Spec.md)

- Film title tone: fit the story's genre and emotion; avoid an overly artsy or commercial leaning.
- Aspect ratio: 16:9 recommended; choose 4:3 or 2.35:1 when emphasizing a sense of oppression or intimacy.
- Visual style: match the story genre; can be realistic, lightly stylized, or genre-film visuals; **low saturation is not mandatory**.

## 2. Script Parsing Rules

When the user has uploaded a script file or text material, parse the uploaded file (image/PDF/text; handled in this environment via the agent's file-reading capability) and extract: character relationships (protagonist + someone close yet distant + someone who brings change), a list of spaces, a stream-of-life event chain (5–8 everyday events), key objects, and key action and dialogue nodes. Output a concise one-sentence story premise summary plus structured key information, for use in Final_Video_Spec and storyboard design. **Do not make era judgments or value determinations.** If the file cannot be parsed or its content is incomplete, explain this to the user and request supplementary material.

## 3. Storyboard Design (storyboard core craft)

### 3.1 Core Temperament

- Emphasize the relationships between people, and between people and their environment. A setting is not a mere backdrop but one of the characters: the setting itself is part of the narrative expression.
- Keep dramatic conflict quiet: use explosive arguments sparingly; favor silence, waiting, detours, unspoken words, and daily routines abruptly cut short.
- The plot should feel incidental, landing in concrete everyday actions.
- The ending does not pronounce judgment: give the audience a changed space or action, not a complete answer.

### 3.2 Script Narrative Construction (six methods, core narrative craft, not one may be omitted)

Urban humanistic narrative films do not rely on dramatic confrontation but on **accumulating emotion through observation**—through the real behavior of characters in urban space, the recurrence of detail objects, and the causal traces between scenes, letting the audience feel the change for themselves.

- **Plant an unresolved thread in the opening**: no explaining, no summarizing—an action, an object, a glance—so the audience keeps watching with a question in mind.
- **Characters have history between them**: even a meeting of strangers should carry an implied reason for "why these two people"—a place, a time, an old object.
- **Key objects appear at least twice**: the first time establishes their presence; by the second time their state has changed — moved, damaged, or taken away by someone.
- **Leave traces between scenes**: what happened in the previous scene should be traceable in the following scene's space or on its characters; no causeless jump cuts.
- **Arrange at least one "expectation falling through"**: a character sets out to do something and the result differs from what was expected — not a dramatic twist, just the way life actually is.
- **The closing action carries a double meaning**: the final action or image can be leaving, staying, or doing nothing at all — but the choice must carry weight.

### 3.3 Character Design Principles

- Character motivation should be small, character dignity should be large: behind small goals lie face, old attachments, identity, family affection, or questions like "am I still a useful person."
- Dialogue should take the long way around: characters rarely state their real needs directly; they often say "it's nothing," "just passing by," "you go about your business," "maybe another day."
- Emotion is expressed through action: smoking, adjusting a collar, fingering an old phone, flicking a lighter open and shut, wiping down a table, waiting for water to boil, watching someone else pay.

### 3.4 Scene Selection

- Space selection serves the current plot relationships and character states; no hard-and-fast rules.
- Every space must carry social information: slogans, price lists, payment QR codes, old posters, construction noise, TV news, square-dancing music, dialect radio broadcasts — these details are part of the narrative, not decoration.

### 3.5 Key Element Design

- Prioritize designing **character elements** (age, appearance, clothing, what they are doing) and **scene elements** (geographic setting, time of day, lighting conditions, carriers of social information).
- Prop elements are established separately only when they have a material impact on consistency across multiple shots (e.g., a recurring old mobile phone, a bus ticket, a payment QR code placard).
- When the user provides reference material, element descriptions must match the reference content and must not contradict it.

### 3.6 Shot Duration and Rhythm Layering

Each narrative segment is built from a mix of three shot durations; changes in rhythm are themselves narrative signals — slowing down means time congeals here, speeding up means the character or the space is in motion:

Shot Type Duration Function and Usage Timing Short shot 2–3s Key-object inserts, emotional reaction cuts, urban detail capture; creates rhythmic jolts or emphasis Medium shot 6–10s Character behavior unfolding, daily interactions, movement and lingering within a space; the narrative backbone, about 60% of the film Long shot 11–15s Opening space establishment, moments of emotional settling, closing lingering resonance; at most 1–2 per narrative segment

### 3.7 Rhythm Structure of Each Narrative Segment (Five Segments)

- **Opening establishment segment**: 1 medium or long shot to ground the urban space and the character's situation — it can start from an action; no need to explain the background.
- **Observation development segment**: mainly medium shots showing the character's concrete behavior in the space; every 2–3 medium shots, insert 1 short shot (object close-up or environmental detail) to break the visual rhythm and build information density.
- **Emotional turn segment**: use 1 long shot or a slow-paced medium shot to hold time, giving the character's subtle reaction or choice enough space to be seen.
- **Dynamic rhythm segment〔Dynamic〕**: when the character crosses urban space, rushes about, or searches, use consecutive medium and short shots to drive the rhythm forward; mark as 〔Dynamic〕 and generate via the multi-reference-driven route.
- **Closing segment**: the final 1–2 shots use medium or long shots — give the outcome or emotion enough time to linger; do not end on a quick cut.

### 3.8 Whole-Film Rhythm Control

- Total shot count recommended at 10–16 (for a 1–3 minute film).
- Avoid uniform duration across the film — the rhythm's density and sparseness speaks for itself. The opening can be slow, the middle follows the character's rising and falling rhythm, and the ending leaves blank space.

### 3.9 Shot Scale

- Opening, establishing the urban space and the character's situation: medium-long shot or wide shot, letting the space speak first.
- Character interaction or solitude: two-shot medium or single medium shot, with gazes and body language that read clearly.
- Emotional buildup or turning point: close-up or extreme close-up, capturing subtle expressions and hand movements.
- Key objects: insert shot (cut-in), brief and clear (2–3s).

### 3.10 Camera Position and Movement

- Conventional observational narrative: mainly fixed camera positions, or slight handheld following of the character, prioritizing the natural presentation of character behavior and space.
- 〔Dynamic〕 scenes (characters crossing streets, rushing, searching): tracking or moving shots, noting the sense of direction and the range of movement.
- **Forbidden**: show-off camera moves, spinning shots, purely decorative aerial shots, slow motion without narrative function, multi-cut sequences, etc.

### 3.11 Composition

- Characters may sit off toward the edge of the frame, leaving large stretches of wall, street, doorframe, window, or empty chairs.
- Use doorframes, glass, railings, car windows, and counters to separate characters.
- When old and new objects are juxtaposed, don't force the contrast; let them coexist naturally in the same frame.
- **Allow the frame to be "dirty"**: clutter, dust, old tiles, plastic stools, wires, and advertising flyers should not be cleaned away.

### 3.12 Color Tone and Lighting

- Day scenes: gray-white skies, low-saturation cement tones, old red slogans, faded blue-green shop signs, dusty yellow.
- Night scenes: sodium-lamp orange, KTV neon pink-purple, the cold light of phone screens, fluorescent lights at street stalls.
- Interiors: greenish fluorescent light, cold TV glow, gray light from the window; no high-end studio polish.
- Grading: low saturation, slight grain, true dynamic range, keep the noise in the shadows.

### 3.13 Shot Description Rules

- **Every shot description must include 4 dimensions**: Scene (referenced scene elements + time-of-day lighting), subject action (mainly body language / expression), cinematographic language (shot scale + camera movement + focus strategy), sound feel (ambient sound / in-frame sound).
- **Shot tags**: note the generation-route tag at the end of each shot description — plain narrative shots tagged 〔Plain〕, strongly dynamic / cut-shot sequences tagged 〔Dynamic〕; 〔Dynamic〕 shots must not exceed 20% of the total shot count.

### 3.14 Dialogue Rules

- At most 3–6 lines of dialogue per scene; keep each line as short as possible; dialect words are allowed but don't pile them on.
- Don't state important information in full; let the audience complete it from actions and space. No voiceover explaining the theme.
- Usable lines: "You're back and didn't even say a word." / "Just passing by." / "Everyone scans this now." / "I don't have that." / "Forget it, then." / "You go ahead."

### 3.15 Audio Layer Design

- BGM (optional): if used, choose minimalist instrumental or atonal ambient soundscapes; pop-music rhythms are forbidden.
- Do not drive the narrative with dialogue.

### 3.16 QC Checklist (Self-Check Before Output)

- Are at least 60% of the shots medium-long scale, fixed camera, or slow movement?
- Are there 2 or more public spaces?
- Is there in-frame sound rather than added sentimental scoring?
- Have blunt summary lines like "he finally understood" or "this was fate's arrangement" been removed?
- Does it avoid directly reusing the characters, lines, scenes, and plots of any existing films?

### 3.17 Prohibitions

- Don't write the story as a heap of hardship or a verdict on values; characters should have humor, vanity, clumsiness, dignity, and the inertia of daily life.
- Don't use voiceover to explain the theme or the meaning of the era.
- Don't make every scene carry plot function; useless waiting and incidental passersby are allowed, but they must add to the sense of spatial realism.
- Don't over-poeticize the world. Beauty comes from observation, not from quotable lines and filters.

## IV. Asset Generation Strategy (80/20 Dual Routes, Media Adapted to 13 Tools)

### 4.1 Element Image Generation

- `generate_image_v3`, 2K.
- If the user has uploaded reference images (characters / scenes), register them as anchors and bind them to the corresponding storyboard element slots, using them preferentially in place of generation.

### 4.2 First-Frame Image Generation (start_frame for Each Shot)

- `generate_image_v3`, 2K.
- The first-frame image must strictly match the shot scale, lighting, and subject posture described in the storyboard shot description, serving as the visual anchor for video generation.

### 4.3 Shot Video Generation (Split by Route)

- **Plain narrative shots〔Plain〕 (approx. 80%)**: first-frame-driven route, using the corresponding shot's start_frame as the first-frame input, `generate_video_v3`.
- **Dynamic shot〔dynamic〕(no more than 20% of the total shot count)**: multi-reference-driven route, `generate_video_v3`; cite the character/scene element images involved in the shot as references, while also using start_frame as the first-frame reference; use only for strong-conflict, fast-cutting, or high-speed character-motion scenes.

### 4.4 Audio Layer Generation

- Narration (if any): `generate_audio`; if the narration exceeds 15s, split it into multiple segments and generate them separately, keeping the character voice-timbre description parameters consistent (the original Method 2's "generate-then-split-timbre-for-later-reference" chain has no corresponding capability in this environment—see the adaptation note at the top; legitimately removed).
- BGM: `generate_audio`, with the style described as minimal instrumental / ambient soundscape; do not generate lyric-based music.

### 4.5 Failure Handling

- If any model's generation fails, retry within the same tool first; do not automatically switch to another video generation tool—stop and inform the user, letting the user decide whether to change routes.

## 5. Prompt Writing Standards

### 5.1 First-Frame Image / Element Image Prompt

Core logic: capture the "decisive moment," emphasizing film color texture, real light and shadow, and atmosphere; drop camera-movement and rhythm vocabulary.

**Prompt formula**: \[main subject and micro-actions\] + \[spatial environment and social-information carriers\] + \[atmospheric feel\] + \[lighting state\] + \[photographic language and shot size\] + \[color system and film texture\] + \[style references\]

**Core vocabulary bank**:

- Subject and micro-actions: a figure from behind / hands smoking a cigarette / gazing out the window / a paused moment of zoning out / adjusting a collar / touching an old phone
- Spatial social information: faded slogans, payment-QR-code stickers, old posters, price lists, construction hoardings, old wall calendars
- Environment and atmosphere: pervasive dust (dusty air), early-morning moisture (morning mist), dampness, heat waves (heat haze)
- Lighting state: natural light, soft side light by the window (soft window light), greenish fluorescent light (fluorescent greenish), orange sodium light (sodium orange), overcast diffuse light (overcast diffused light)
- Photographic language: Medium shot / Full shot / Close-up (use sparingly) / minimalist composition / negative space / doorframe occlusion / glass reflections
- Color system: Kodak Vision3, Fuji Eterna, ARRI Alexa Natural, low saturation, soft highlights, detailed shadows, real skin tone, slight grain
- Style references: Jia Zhangke, Hirokazu Kore-eda, Magnum Photos, Leica Documentary

**Example Prompt (first-frame image)**:

> Real slice-of-life cinematic footage of a small Chinese town, winter evening 2001, a small shop beside a long-distance bus station; a young man in an old black jacket stands at the doorway, clutching a crumpled bus ticket, long hesitating without going in; composition: fixed medium-long shot, the figure at the right edge of the frame, foreground of a glass door covered in faded advertisements, midground of the shop counter, background of the waiting room's cold white lights and passengers coming and going; lighting and tone: gray-blue skylight mixed with greenish fluorescent light, low saturation, reflections on the concrete floor, slight grain; Kodak Vision3 film stock, real skin tone, soft highlights; Jia Zhangke aesthetics, observational, quiet, real; avoid: polished-ad look, strong backlighting, over-beautification.

### 5.2 Video Prompt

Core logic: focus on "the flow of time" and the observational feel of a long take; keep watching a moment longer even after the action completes; ambient sound takes priority over score description.

**Prompt formula**: \[real slice-of-life cinematic footage of a small Chinese town, era/season/time, location\]; \[character appearance and clothing\] is \[specific action\]; composition: \[shot size, figure position, foreground/midground/background layering, occlusion relationships\]; lighting and tone: \[lighting type\], low saturation, slight grain, lived-in texture; camera: \[movement type\], \[duration\], actions occurring naturally, pauses preserved; sound: \[ambient sound/diegetic music/broadcast/traffic sounds\]; avoid: polished-ad look, over-beautification, theatrical acting, exaggerated tears, strong movie lights, flashy camera moves

**Camera-movement vocabulary (strictly restrained)**: Fixed camera / Slight handheld breathing / Extremely slow push-in / Extremely slow pan; **forbidden**: rotation, fast push/pull, drones, MV-style rapid cutting

**Sound description references**: distant bus reversing beeps, ticket-window PA announcements, mahjong sounds, TV news sound, KTV sound leaking out, construction noise, square-dance loudspeakers, short videos played aloud on phones

**Example Prompt (plain narrative shot)**:

> Real slice-of-life cinematic footage of a small Chinese town, winter evening 2001, a small shop beside a long-distance bus station; a young man in an old black jacket stands at the doorway, clutching a crumpled bus ticket, long hesitating without going in; composition: fixed medium-long shot, the figure at the right edge of the frame, foreground of a glass door covered in faded advertisements, midground of the shop counter, background of the waiting room's cold white lights and passengers coming and going; lighting and tone: gray-blue skylight mixed with greenish fluorescent light, low saturation, reflections on the concrete floor, slight grain; camera: locked-off position for 12 seconds, the young man glances up at the station sign then lowers his head, actions occurring naturally, pauses preserved; sound: distant bus reversing beeps, ticket-window PA announcements, the rustle of plastic bags; avoid: polished-ad look, strong backlighting, exaggerated expressions, fast editing, modern upscale streetscapes.

## 6. Editing and Output (`composite_video`)

### 6.1 Pacing Principles

- Long takes first, preserving the complete sense of time flowing; never cut shots short just to be "interesting."
- Between shots, a 0.5–1s black frame or a sound-continuity transition may be used to create breathing room.
- **Forbidden**: rapid cutting, beat-synced cuts, special-effect transitions, TikTok pacing.

### 6.2 Audio-Visual Relationship

- Complete the full-film timeline assembly, aligning narration segments in order to their corresponding positions.
- BGM (if any) at 0.1x volume; fade in and out, never overpowering the picture.
- No forced audio-visual sync; picture and sound each flow naturally on their own.

## Related

- **Boundaries (do not use this skill; reroute)**: strong dramatic-conflict narratives → cinematic-flow; auteur-style full films (Jia Zhangke's rural-documentary aesthetics) → jia-zhangke-style; mood-and-atmosphere-driven East Asian art films with no event chain → east-asian-mood-film (its craft system is incompatible with this skill; the two must not be mixed).
- This skill is self-contained and inline, **with no native cross-skill dependencies and no coordination table**.