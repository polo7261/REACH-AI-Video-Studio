---
name: cuyezhuyi
description: "Soviet Brutalism: deeply builds raw Soviet aesthetics, one-click generating monumental visual epics"
---

# Soviet Brutalist Style Skill

SKILL: Soviet Brutalist Cinematic Short Film
Skill ID: reach-industry/brutalist-film
Version: 3.1
Use case: generation of Soviet brutalist-style cinematic short films, guaranteeing character consistency, style stability, and cinematic aesthetic value.

## I. Skill Positioning and Objectives

This Skill generates brutalist-style short films with the following features:

- 🏗️ Style anchoring: Base Prompt + color palette spec + hard-locked prohibitions (the immovable style core)
- 🌊 Maximum divergence: theme, story, scenes, characters, atmosphere, narrative structure, props, dialogue, sound effects, and transitions are all improvised by the AI, with no fixed asset library
- 🧍 Character consistency: the protagonist's look is generated via Lib Image, locked, and reused across every shot
- 🖼️ Environmental tone-setting: MJ V8.1 generates 3 environmental atmosphere reference images that lock in the scene tone and palette of the whole film; all subsequent storyboard frames are anchored to these references
- 🎬 Shot-size variety: multi-shot-size distribution is enforced; consecutive shots of the same size are forbidden
- 💬 Character dialogue: each shot can include generated dialogue/monologue, with Chinese/English/Russian options
- 🎞️ High-density storyboarding: default 2.5 seconds per shot with fast cutting; Beats are split into micro-shots to heighten dramatic tension
- 🔊 Fitted sound design: cinematic-grade ambient sound effects generated to match the story's atmosphere (no background music)
- 📦 Reusable workflow: a 6-step standard process that anyone can follow to produce a high-quality finished film

## II. Style Core Anchors (required throughout the film; randomization forbidden)

This is the only part that must never change. Everything beyond the anchors is improvised by the AI.

### Base Prompt — required in every shot

```
Soviet brutalist architecture, raw concrete texture, colossal geometric structures, monumental scale, cold grey atmosphere, volumetric fog, cinematic lighting, 8k resolution, photorealistic
```

### Color Palette Specification

- Primary palette: cold grey / rust red / bone white
- The only warm color: amber light in a single distant window (symbolizing the interior of the system)
- Forbidden: saturated warm colors, greenery, modern elements

### Mandatory Shot-Size Diversity Rules

- A 6-shot short must cover at least 4 shot sizes; 8 shots or more must cover at least 5
- Shot-size codes and reference figure-to-frame proportions:
  - ELS (extreme long shot): figure occupies ≤3% of the frame, emphasizing the oppression of the environment
  - LS (long shot): figure occupies 5–15% of the frame, recognizable but still tiny
  - MS (medium shot): figure from the waist up, occupying 30–50% of the frame
  - MCU (medium close-up): figure from the chest up, occupying 50–70% of the frame
  - CU (close-up): face/hands/prop details, occupying 70–90% of the frame
  - ECU (extreme close-up): eyes / material texture, occupying 90%+ of the frame
- No two consecutive shots may use the same shot size

### Camera Movement Rules

- ✅ Allowed: Hitchcock zoom / dolly zoom, push in, pull back / zoom out, tilt up/down, pan left/right, slow tracking, slow crane up/down, slow orbit
- ❌ Forbidden: buildings moving/rising/collapsing/deforming, ground caving in / bulging / shifting, the sky rotating, clouds shifting rapidly, any physically implausible movement of objects
- For close shots/close-ups, prefer static or an extremely slight push in; large movements are forbidden

## III. AI Improvisation Rules (maximum divergence beyond the style core)

There is no fixed asset library. The AI improvises all content under the constraints of the style anchors.

### Creative Principles

- Style first: all improvised content must conform to brutalist aesthetics (concrete megastructures, systemic oppression, human smallness, cold grey palette)
- Different every time: each run of the Skill must produce a completely different story/scenes/characters/atmosphere; reusing the previous run's plan is forbidden
- Concrete, not abstract: the generated story must have concrete characters, actions, spaces, and emotions — not abstract conceptual description
- Brutalist temperament check: for every element it generates, the AI should ask "Does this belong to a brutalist world?" — if not, regenerate

### AI Improvisation Checklist (fully regenerated on every run)

| Creation Dimension | Rule | Style Constraint |
|---|---|---|
| 🎭 Story theme | The AI improvises a complete story: a one-line premise + 5 Beats | Must unfold in a brutalist architectural environment, with tiny figures and a sense of systemic oppression |
| 🌫️ Environmental atmosphere | The AI improvises a baseline environmental atmosphere | Must belong to the cold grey family; extreme weather/lighting conditions preferred |
| 🏛️ Scenes | The AI improvises a brutalist scene for each shot | Must be concrete megastructures/Soviet-style architectural spaces; no scene repeated across shots |
| 🧑 Character design | The AI improvises the protagonist's appearance/clothing/temperament | Soviet-era clothing; temperament of repression, endurance, numbness, or resolve |
| 🗝️ Symbolic props | The AI improvises 1–2 props that recur across shots | Soviet-era objects, symbolically charged, carrying narrative function |
| 📖 Narrative arc | The AI improvises the narrative structure | Must have a clear emotional trajectory; the ending may be tragic, cyclical, nihilistic, or an awakening |
| 💬 Dialogue | The AI improvises the dialogue for each shot | Short, cold, hard-edged lines; dialogue extends the imagery rather than explaining it |
| 🔊 Sound effects | The AI improvises the ambient sound description | Pure ambient sound, no score, matched to the atmosphere |
| 🎞️ Transitions | The AI improvises a transition for each shot junction | crossfade/fadeblack/dissolve, with no repeats between adjacent shots |

### Story Generation Guidance (not a fixed template; the AI may reference it but is not limited to it)

When creating a story, the AI should consider the following classic brutalist motifs (they may be combined, mutated, or subverted — and the list is not exhaustive):

- The system and the individual: queuing / approvals / waiting / being refused / being forgotten
- Memory and forgetting: old addresses / old photographs / old objects / a room that cannot be found / traces that have vanished
- Loops and predicaments: repeated routes / endless corridors / destinations never reached / returning to the starting point
- Solitude and waiting: vast empty squares / deserted stations / the person who never arrives / the ceremony that will never be held
- Power and smallness: people beneath colossal buildings / looking up at the dome / facing the high wall / deep inside the system
- Time and decay: buildings slated for demolition / forgotten monuments / derelict public spaces / snow covering everything

These motifs are reference directions only; the AI should freely diverge and invent new motifs, as long as they fit the brutalist aesthetic.

## IV. Standard Workflow (6 Steps)

### ▶ STEP 1: Style Confirmation + AI Improvisation

Trigger: runs immediately after the user starts the Skill.

Process:

1. The AI improvises 3 completely different story proposals (each containing: title + one-line premise + 5 Beats + environmental atmosphere + protagonist overview)
2. Present the 3 proposals to the user, who picks one or asks for regeneration
3. Once the user has chosen, the AI improvises the remaining elements: symbolic props, narrative arc structure, sound style, and dialogue language

Items to ask (4 in total):

- Story proposal (choose one):
  - Proposal A: [AI-improvised]
  - Proposal B: [AI-improvised]
  - Proposal C: [AI-improvised]
  - 🎲 Regenerate (the AI produces 3 brand-new proposals)
  - Custom (the user describes what they want, and the AI generates a story from it)
- Dialogue language (choose one):
  - Chinese
  - English
  - Русский (Russian)
  - No dialogue (purely environmental storytelling)
- Aspect ratio (choose one):
  - 16:9 (landscape, cinematic feel)
  - 21:9 (ultrawide, epic feel)
  - 9:16 (vertical, for social media)
- Total duration × storyboard pacing (choose one):
  - 15 seconds (6 shots × 2.5 seconds) — fast-paced short
  - 30 seconds (12 shots × 2.5 seconds) — standard short
  - 40 seconds (16 shots × 2.5 seconds) — extended short
  - 60 seconds (24 shots × 2.5 seconds) — full short film
  - Custom

⚙️ STEP 1 self-check:

- The 3 story proposals have been presented and the user has chosen one
- The chosen proposal includes: title/premise/5 Beats/environmental atmosphere/protagonist overview/symbolic props/narrative arc/sound style
- Dialogue language confirmed
- Shot count = total duration ÷ 2.5 seconds; calculated and recorded
- All chosen parameters written to the anchor file
- The story proposal passes the brutalist temperament check (concrete megastructures/systemic oppression/human smallness/cold grey palette)

### ▶ STEP 2: Environmental Atmosphere Reference Image Generation (MJ V8.1)

Objective: use MJ V8.1 to generate 3 environmental atmosphere reference images that lock in the scene tone, palette, and architectural texture for the whole film. All subsequent storyboard frames use these 3 images as their visual anchor.

Generation rules:

- Model: Midjourney V8.1, at the aspect ratio chosen in STEP 1
- Number of images: fixed at 3, corresponding to:
  - Reference image 1: panoramic environment — a long shot / extreme long shot of the story's core architectural space, showing the brutalist megastructure in full
  - Reference image 2: mid-range space — the main setting where the character moves (corridor/plaza/interior, etc.), showing the scale relationship between people and the architecture
  - Reference image 3: atmospheric detail — material textures / close-ups of light and shadow / weather mood, establishing the palette and texture foundation
- Prompt structure for each image:
  [Base Prompt], [STEP 1 environmental atmosphere keywords], [reference image type description], [AI-improvised scene details], [lighting], [emotional atmosphere], Blade Runner 2049 visual quality
- No people in the reference images — pure environment/architecture/atmosphere
- The 3 images must share one palette (cold grey/rust red/bone white + amber window light) and one consistent visual style
- Show the images to the user after generation; proceed to STEP 3 only once the user is satisfied with the palette/atmosphere/architectural texture

Reference image usage notes:
These 3 images are not storyboards — they are the visual anchors of the entire film. In the later STEP 4, when Lib Image generates the storyboard for each shot, it will reference these 3 reference images to pin down the environmental mood and color tone. The reference images keep the scene style consistent across the whole film, with no jarring shifts from shot to shot.

### ⚙️ STEP 2 Self-Check Checklist:

- The 3 environment reference images have been generated (panoramic environment / medium-shot space / atmospheric detail)
- Unified color tone across the 3 images (cold grey / rust red / bone white + amber window light)
- The reference images contain no people
- Consistent architectural texture across the 3 images (brutalist concrete megastructures)
- The 3 node_keys have been written to the anchor file
- The user has confirmed the environmental atmosphere effect

### ▶ STEP 3: Protagonist Image Generation (Lib Image)

**Goal:** Design the protagonist together with the user and generate the protagonist anchor image.

**Questions to ask (ask_human):**

- 🎲 One-click random protagonist (the AI improvises a character description, then generates the image directly)
- Manual item-by-item setup (5 items in total):
  - Gender: male / female / ambiguous
  - Age group: young adult (20-30) / middle-aged (35-50) / elderly (55+)
  - Clothing: Soviet worker's padded cotton coat / military greatcoat / worn civilian padded jacket / minimalist long black garment / custom
  - Accessories (multi-select): old leather hat / knitted wool hat / rust-red scarf / battered briefcase / none
  - Temperament: silent and stoic with hollow eyes / weary but resolute / utterly numb / angry and repressed

**One-click random rule:** The AI improvises the character's full profile (gender/age/clothing/accessories/temperament), links the accessories to the symbolic prop selected in STEP 1, generates the complete character description, and shows it to the user for confirmation.

**Protagonist anchor image generation:**

- Model: Lib Image (default)
- Prompt: `[Full character description], full body front view, neutral grey concrete background, character reference sheet, Soviet brutalist atmosphere, cinematic lighting, 8k resolution, photorealistic, no action, standing pose`
- Optional: cite the STEP 2 environment reference images for background anchoring — `reference: {{Environment Reference Image NodeKey}}`
- After user confirmation, write to the anchor file, marked Protagonist Anchor · Confirmed ✅
- If Lib Image output is unsatisfactory, switch to MJ V8.1 as a fallback

### ⚙️ STEP 3 Self-Check Checklist:

- All character parameters finalized (random or manual)
- Symbolic prop ↔ character accessory linkage checked
- Protagonist anchor image generated and confirmed by the user
- node_key written to the anchor file, character description fully recorded

### ▶ STEP 4: Storyboard Planning + Storyboard Image Generation (Lib Image)

**Goal:** Plan the complete storyboard narrative structure and use Lib Image to directly generate storyboard images containing the protagonist (with the STEP 2 environment reference images as visual anchors).

**Storyboard planning rules:**

- **Beat-driven storyboarding:** unfold according to the story's 5 selected Beats + the narrative arc. High-density storyboarding (2.5 seconds per shot). Beat-splitting rules:
  - Split each Beat into 2-5 micro-shots (based on total duration and Beat density)
  - Within a Beat, micro-shots create rhythm through shot-scale changes, viewpoint shifts, and action decomposition
  - Separate Beats with transition markers (fadeblack = time jump, dissolve = memory transition)
  - Example: Beat 1 "Arrival" can be split into [ELS panorama] → [MS mid shot] → [CU hand close-up] → [MCU hesitation on the face]
- **Scene improvisation:** the AI improvises a brutalist scene for each shot; the same scene may not appear twice (except in the loop arc, where the first and last shots may be identical)
  - Scenes must fit the style core: concrete megastructures, Soviet-style architectural spaces, an oppressive sense of colossal scale
  - Each shot's scene must be tagged with its narrative function (departure / progression / turning point / arrival / desolation, etc.), matched to the narrative arc
- **Each shot must contain four narrative elements:**
  - A concrete action (what the character is doing — not merely "standing" or "walking")
  - Narrative information (what this shot establishes — discovery / turning point / obstacle / confirmation / giving up)
  - Emotional shift (how this shot's emotion moves compared with the previous one — escalation / subsiding / stagnation / eruption)
  - Dialogue/monologue (if a language has been selected): one line of dialogue per shot, ≤20 characters/words; types include: spoken aloud / inner monologue / memory fragment / muttering to oneself / silence
- **Dialogue writing rules:**
  - Chinese: short sentences, cold and hard style, ≤20 characters. Examples: "This used to be a post office." "No one is left." "The wind is too strong."
  - English: short sentences, cold and minimal. Examples: "No one here." "The address is wrong."
  - Russian: short sentences, severe style. Examples: "There is no one here." "Too late."
- **Dialogue rhythm:** sparse dialogue in the first third (1-2 lines), dense in the middle stretch (1 line per shot), tapering off sharply or falling silent at the end
- **Dialogue–image relationship:** dialogue extends the image rather than explaining it — the image shows "a person standing in an empty room," and the dialogue says "he moved out" (a supplement), not "this is an empty room" (a repetition)
- **Symbolic prop:** the 1-2 props improvised by the AI appear at clearly designated moments in the storyboard; a prop's appearance/disappearance is itself a narrative signal
- Tag each shot with a shot-scale code (ELS/LS/MS/MCU/CU/ECU)
- **Shot-scale distribution check:** cover ≥4 types (6 shots) / ≥5 types (8+ shots); no two consecutive shots with the same scale
- **Pacing checks:**
  - At least 2 action shots in the first two-thirds (character moving / doing something / interacting with the prop)
  - At least 1 emotional shot in the final third (close-up or extreme close-up, emotional eruption or settling)
  - A shot-scale jump (e.g., ELS→CU) every 3-4 shots to create visual impact
  - At least 1 silent shot in the whole film — a static shot with no action and no dialogue, only the environment
- Show the user the storyboard outline (with columns for Beat number / micro-shot number / scene / shot scale / action / narrative information / emotional shift / dialogue / symbolic prop); generate the images only after confirmation

**Storyboard image generation rules:**

- Model: Lib Image (directly generates storyboard images containing the protagonist — no character replacement needed afterward)
- Per-shot prompt structure:

```
[Base Prompt], [environment mood keywords], reference: {{Environment Reference Image 1 NodeKey}}, reference: {{Environment Reference Image 2 NodeKey}}, reference: {{Environment Reference Image 3 NodeKey}}, character: {{Protagonist Anchor NodeKey}}, [shot-scale keywords], [AI-improvised scene details], [protagonist action description], [shot-scale-matched figure placeholder], [symbolic prop appearance description (if applicable)], [lighting], [emotional atmosphere], [camera movement hint], Blade Runner 2049 visual quality
```

- Shot-scale-matched figure descriptions:
  - ELS/LS: a lone figure in the distance / a solitary silhouette far away
  - MS: a lone figure from the waist up
  - MCU: a lone figure from the chest up, face partially visible
  - CU: close-up of a figure's weathered hands / close-up of a figure's hollow eyes
  - ECU: extreme close-up of cracked concrete texture and a figure's eye reflection
- Shot-scale adaptation: for close-up/extreme-close-up shots, additionally emphasize focus on [face expression / hands / clothing texture], maintain the [MCU/CU/ECU] framing, figure fills the frame
- For shots where the symbolic prop appears, additionally emphasize: [prop description] clearly visible in [hand/pocket/shoulder], [prop details]
- Up to 10 images in parallel; beyond that, execute in batches

**Storyboard image quality standards:**

- ✅ Protagonist appearance consistent with the STEP 3 anchor (clothing/accessories/temperament)
- ✅ Environmental mood consistent with the STEP 2 reference images (color tone/architectural texture/atmosphere)
- ✅ Shot scale matches the storyboard plan
- ✅ In close-ups/extreme close-ups, character details are clear and emotions readable
- ✅ Symbolic prop clearly visible in the designated shots
- ❌ Protagonist appearance deviates → strengthen the protagonist anchor description and regenerate
- ❌ Environmental mood shifts abruptly → strengthen the references to the environment reference images and regenerate
- ❌ Character still too small in close shots → add figure fills the frame and regenerate

### ⚙️ STEP 4 Self-Check Checklist:
The storyboard outline contains Beat number / micro-shot number / scene / shot size / action / narrative info / emotional turn / dialogue / symbolic prop columns, and has been confirmed by the user
Each shot's scene is AI-improvised and conforms to the Brutalist style
No shot reuses the same scene (except the start and end of the loop arc)
Each shot contains a concrete action + narrative info + emotional turn + dialogue (in the selected language, if any)
Dialogue rhythm: sparse in the first 1/3, dense in the middle, dropping sharply or falling silent at the end
Dialogue and visuals do not duplicate each other
Each Beat is split into 2–5 micro-shots
At least 2 action shots in the first 2/3, at least 1 emotional shot in the last 1/3
A shot-size change occurs every 3–4 shots
At least 1 silent shot across the whole film
Shot-size distribution: ≥4 types (6 shots) / ≥5 types (8+ shots), no consecutive repeats
All image aspect ratios match STEP 1
Each image includes Base Prompt + ambient atmosphere + shot-size keywords + environment reference-image reference + protagonist anchor reference
The protagonist's appearance matches the STEP 3 anchor
The environmental tone matches the STEP 2 reference images
Figure size in close shots / close-ups matches the shot size
The symbolic prop is clearly visible in the designated shot
All images generated, node_key written into the storyboard file
The user has confirmed the storyboard images
▶ STEP 5: Sound Effect Generation (No Score)
This Skill only generates ambient sound effects, not background music. The sound effects serve as the auditory support for the visual atmosphere and do not dominate the emotional narrative.
Goal: AI-improvises cinematic-grade ambient sound effects that precisely match the film's ambient atmosphere.
Execution rules:
Model: Seedance 2.0 (sound effect mode)
Sound duration = total video duration + 5-second buffer
Based on the ambient atmosphere improvised at STEP 1, the AI generates a sound-effect prompt:
Cinematic environmental sound design, [AI-improvised sound description], continuous [ambient duration] seconds, no music, no dialogue, no voiceover, pure atmospheric audio, Soviet brutalist soundscape, high quality audio, realistic field recording style
Sound design guidance (AI reference, not limited to the following):
Blizzard type: howling wind gusts, ice crystals colliding, muffled distant industrial hum, footsteps crunching on packed snow
Indoor echo type: heavy reverb, droplets, echoing footsteps, distant mechanical drone
Industrial type: continuous factory drone, steam releases, heavy machinery idling, metallic resonance
Near-silence type: near-total silence, breath, clothing rustle, footsteps on concrete or snow
Ruins wind type: wind through broken windows, door panels banging, desolate uninhabited echoes
⚙️ STEP 5 self-check checklist:
The sound description is AI-improvised and matches the STEP 1 ambient atmosphere
Sound duration ≥ total video duration
node_key written into the storyboard file's compositing record
▶ STEP 6: Video Generation and Compositing (Seedance 2.0)
Pre-execution double confirmation (ask_human):
Video aspect ratio (same as STEP 1, confirmed here)
Seconds per shot (same as STEP 1, confirmed here)
Resolution (720p / 1080p)
Original video audio: muted (always off)
Video generation rules:
Model: Seedance 2.0
start_frame_image_node: the storyboard image generated at STEP 4
sound: off (sound effects are attached uniformly at the compositing stage)
Prompt structure:
[Base Prompt], [ambient atmosphere keywords], {{image NodeKey after replacement}}, [shot size code], [character action: static or minimal], [symbolic prop state], [environmental motion (natural phenomena)], [emotional atmosphere], cinematic, Blade Runner 2049 visual quality
Allowed environmental motion descriptions:
Snow: snow drifting slowly / frost forming on concrete surface
Fog: fog rolling slowly through frame / mist thickening
Light: light flickering slowly / amber glow pulsing faintly
Steam/smoke: steam rising from vent / distant smoke column
Water: condensation dripping / ice melting slowly
Fabric: scarf moving gently in wind / coat rustling
Forbidden environmental motion descriptions:
❌ Buildings moving, rising, deforming, or collapsing
❌ Ground collapsing, bulging, or shifting
❌ Sky spinning, clouds shifting rapidly
❌ Any structure producing physically implausible motion
Camera movement suggestions:
Establishing shot (ELS): slow push forward / slow crane up
Traveling shot (LS/MS): static with figure walking / subtle dolly follow
Confrontation shot (MS/MCU): slow upward tilt / static
Overhead shot (ELS): slow zoom out / slow crane down
Emotional / close-up shot (MCU/CU): static (preferred)
Hitchcock zoom (reserved for emotional climax points): dolly zoom
Close-up warning: for CU/ECU, prefer static; if movement is unavoidable, use only an extremely subtle push in (<5%); zoom / dolly zoom / orbit are forbidden.
Generation failure troubleshooting procedure:
Self-inspection: check whether the prompt contains forbidden camera movements / out-of-range environmental motion
Prompt fine-tuning: switch to static or a camera movement from the allowed list and regenerate
If it still fails (within 3 attempts): conclude that faces occupy too much of the frame → change the composition to reduce face coverage (≤20%) and regenerate
For more than 3 consecutive failures, flag it and inform the user; try changing the scene or shot size
At most 10 shots in parallel; beyond that, execute in batches.
Transition rules:
The AI improvises a transition for each shot-to-shot join; adjacent shots must not use the same transition:
crossfade (direct dissolve)
fadeblack (via black frame, emphasizing a time jump)
dissolve (grainy dissolve, emphasizing a sense of memory)
Transition duration 1.0–1.5 seconds (1.0s for 5-second shots, 1.5s for 10-second shots, 0.5–0.8s for 2.5-second shots)
Compositing rules:
Tool: composite_video (using transition mode)
videoList: in storyboard order 01→last shot
transitions: filled in shot by shot with the AI-improvised transition types
audioList: STEP 5 sound effects, startTime:0
videoVolume: 0, audioVolume: 1
⚙️ STEP 6 self-check checklist:
Video parameters double-confirmed
All video nodes generated successfully (no failed/discarded nodes)
Troubleshooting procedure executed on failed nodes
Nodes with more than 3 consecutive failures are flagged, with reasons noted
Video order strictly matches the storyboard table
Transition styles assigned, no repeats between adjacent shots
Sound-effect node_key correctly attached
Compositing node_key written into the storyboard file and the task; task marked completed
5. File Specifications
Anchor file: /anchor/{project_name}_anchors.md
markdown
Copy
Project anchor checklist: {film title}
Style anchors (fixed)
Base Prompt: Soviet brutalist architecture, raw concrete texture...
Color palette: cold gray / rust red / bone white; the only warm color = amber window light
Aspect ratio: [16:9 etc.]
Resolution: [720p/1080p]
AI improvisation parameters
Story title: [AI-generated]
Story premise: [AI-generated one-liner]
5 Beats: [AI-generated]
Narrative arc: [AI-generated]
Ambient atmosphere: [AI-generated]
Sound style: [AI-generated]
Symbolic props: [AI-generated, 1–2 items]
Dialogue language: [Chinese/English/Русский/No dialogue]
Protagonist anchor
Description: [full appearance: gender/age/clothing/accessories/temperament]
Standard anchor image node_key: [confirmed ✅]
Scene anchors (by shot number)
Shot 01 shot size: [ELS/LS/MS/MCU/CU/ECU]
Shot 01 scene: [AI-improvised scene] (narrative function: [tag])
Shot 01 storyboard image (LibImage): [node_key]
... (and so on)
Environment reference images (MJ V8.1)
Reference image 1 wide environment: [node_key]
Reference image 2 mid-range space: [node_key]
Reference image 3 atmosphere detail: [node_key]
Sound effects
Sound effect node_key: [node_key]
Duration: [seconds]
Transition assignment: Shot 01→02: [type] / Shot 02→03: [type] / ...

Storyboard file: /story_boards/{project_name}_storyboard.md

```markdown
Storyboard: {film_title}
Story premise / narrative arc / environment atmosphere / dialogue language / total duration / shot count

Shot 01 — {title} (2.5s) [Shot size: ELS] [Beat: 1-A]
Narrative info: [what this shot establishes — discovery / turning point / obstacle / confirmation / giving up]
Emotional shift: [direction of change vs. the previous shot — escalation / fall-off / stagnation / outburst]
Action: [what the character is concretely doing]
Dialogue: [in the chosen language] Type: [spoken aloud / inner monologue / memory fragment / talking to oneself / silence] Content: [≤20 characters/words]
Shot size: ELS / LS / MS / MCU / CU / ECU
Scene: [AI-improvised scene] (narrative function: [tag])
Composition:
Camera movement: [static / slow push in / dolly zoom / etc.]
Symbolic prop: [present / absent — if present, describe]
Transition to next shot: [crossfade/fadeblack/dissolve]
Reference image (MJ): [N/A — see environment reference images]
Storyboard image (LibImage): [node_key]
Video (Seedance): [node_key]
Status: [pending → reference image done → replaced → video done]

Compositing log
Sound effect: [node_key]
Final cut: [node_key] ✅
```

## VI. Quality Red Lines

| 🚫 Red line | Description |
|---|---|
| Style anchor breached | Base Prompt / color tone / forbidden items are absolutely fixed; AI improvisation must not breach them |
| Character inconsistency | Every storyboard image must reference the protagonist anchor node_key; the protagonist's look stays uniform across all shots |
| Environment tone jumps | Every storyboard image must reference the STEP 2 environment reference images; color tone/texture stays uniform across all shots |
| Inconsistent aspect ratio | All images/videos in the film must match the aspect ratio chosen in STEP 1 |
| Missing Base Prompt | Every shot prompt must include the universal style anchor |
| Shot sizes lack variety | 6 shots: ≥4 types; 8+ shots: ≥5 types; no 2 consecutive shots the same |
| Figure still tiny in close shots | In MCU/CU/ECU shots the figure must fill the frame |
| Repeated scenes | No scene repeats across shots (except the first/last of a loop arc) |
| Improvisation drifting off-style | AI-generated scenes/characters/props/story must pass the Brutalist vibe check |
| Symbolic prop continuity broken | The chosen symbolic prop must appear clearly in its designated shots |
| Adjacent transition repeat | Adjacent shots must not use the same transition type |
| Skipping user confirmation | STEP 2 reference images and the STEP 3 protagonist image require user confirmation before continuing |
| Failed nodes entering compositing | Check nodes one by one before compositing; deprecated nodes must not be included |
| Video contains background music | This Skill uses ambient sound only; background music is forbidden |
| Skipping STEP 5 | Sound effects must be generated; do not skip |
| Skipping steps | The 6 steps must run in order; none may be skipped |
| Dialogue duplicating the visuals | Dialogue must extend the image, not explain it |
| Generating dialogue before the language is chosen | Dialogue may only be generated after the language is chosen in STEP 1 |
| No silent shot | The film must contain at least 1 silent shot with no action and no dialogue |
| Reusing the previous run's concept | Every run must produce a brand-new story/scene/character/atmosphere |

## VII. Common Issue Handling

| Issue | Resolution |
|---|---|
| Dissatisfied with all 3 story concepts | Regenerate 3 brand-new concepts; loop until satisfied |
| User's custom story doesn't fit Brutalism | The AI adapts the user's request into the Brutalist framework, preserving the user's core intent |
| Dissatisfied with the one-click random character | Re-roll the character description, or switch to manual setup |
| Reference image figure doesn't match the protagonist | Normal — STEP 2 locks only the environment, not the character; in STEP 4, Lib Image directly generates storyboards containing the protagonist |
| Protagonist off-model in the Lib Image storyboard | Strengthen the protagonist anchor description and regenerate |
| Environment tone jumps in the Lib Image storyboard | Strengthen the environment reference image references and regenerate |
| Figure too small in close shots of the Lib Image storyboard | Add figure fills the frame and regenerate |
| Video generation failed (1st attempt) | Self-check the prompt for descriptions of forbidden camera movements; fix and regenerate |
| Video generation failed (2nd attempt) | Fine-tune again, switch to static, and regenerate |
| Video failing repeatedly (3+ attempts) | Face share too large → reduce its share of the composition (≤20%) and regenerate |
| AI-improvised scene not Brutalist enough | Check for concrete/megastructure/Soviet architecture elements and regenerate |
| Dialogue too literary, not cold and hard enough | Rewrite as short spoken lines; cut the embellishments |
| Dialogue repeats information already in the image | Check whether the dialogue adds information the image lacks; rewrite it as extension, not explanation |
| Too many micro-shots, choppy rhythm | Merge same-scene micro-shots where appropriate; keep 2-3 micro-shots per Beat |

## VIII. Skill Launch Message

When the user triggers this Skill, output the following, then immediately proceed to STEP 1:

```
🎬 Soviet Brutalist Short Film Workflow launched v3.1
Style anchors unchanged: Base Prompt / color tone spec / shot-size diversity / camera movement spec
Everything else is improvised: story / scene / character / atmosphere / props / narrative arc / dialogue / sound effects / transitions
6-step workflow:
STEP 1 AI improvises 3 story concepts → choose one → confirm language/aspect ratio/duration
STEP 2 MJ V8.1 generates 3 environment atmosphere reference images (wide/mid-range/detail) → locks in the film's visual tone
STEP 3 Design the protagonist (Lib Image by default; one-click random supported)
STEP 4 Storyboard planning + Lib Image directly generates storyboards containing the protagonist (with the environment reference images as the visual anchor)
STEP 5 AI improvises ambient sound effects (no score)
STEP 6 Seedance 2.0 batch video generation + improvised transitions + sound effects composited into the final film
Now starting step one — the AI is improvising 3 story concepts...
```

## IX. Model Division of Labor Overview

| Step | Purpose | Model |
|---|---|---|
| STEP 1 | Story creation: AI improvises story/scene/character/props | LLM (current model) |
| STEP 2 | Environment reference images: 3 atmosphere images setting the tone (wide/mid-range/detail) | Midjourney V8.1 |
| STEP 3 | Character anchor: generating the protagonist's standard look | Lib Image (default) / MJ V8.1 (alternative) |
| STEP 4 | Storyboard planning + image generation: storyboard planning + direct generation of storyboards containing the protagonist | LLM + Lib Image |
| STEP 5 | Sound effects: cinematic ambient sound generation (no score) | Seedance 2.0 (SFX mode) |
| STEP 6 | Video: image-to-video | Seedance 2.0 |
| STEP 6 | Compositing: stitching + transitions + sound-effect mixing | composite_video |

## X. Divergence Dimensions Overview

| Dimension | Status | Description |
|---|---|---|
| Story theme | 🌊 AI-improvised | Fresh creation every run; no fixed library |
| Environment atmosphere | 🌊 AI-improvised | Fresh creation every run; no fixed library |
| Scenes | 🌊 AI-improvised | Improvised per shot; no fixed library |
| Characters | 🌊 AI-improvised | Fresh creation every run; no fixed library |
| Symbolic prop | 🌊 AI-improvised | Fresh creation every run; no fixed library |
| Narrative arc | 🌊 AI-improvised | Fresh design every run; no fixed template |
| Dialogue | 🌊 AI-improvised | Created improvised in the chosen language |
| Sound effects | 🌊 AI-improvised | Improvised based on the environment atmosphere |
| Transitions | 🌊 AI-improvised | Improvised choice for each shot-to-shot link |
| Base Prompt | 🔒 Fixed | Core style anchor; untouchable |
| Color tone spec | 🔒 Fixed | Core style anchor; untouchable |
| Camera movement spec | 🔒 Fixed | Allowed/forbidden list is untouchable |
| Shot-size diversity rule | 🔒 Fixed | Type coverage + no consecutive repeats |
| Aspect ratio | 🔒 User choice | Affects all tool parameters |
| Resolution | 🔒 User choice | Affects all tool parameters |
| Dialogue language | 🔒 User choice | Chinese/English/Русский/no dialogue |
| Background music | 🚫 Forbidden | Ambient sound effects only |