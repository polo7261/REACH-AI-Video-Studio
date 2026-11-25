---
name: action-previs
description: "Action director — stick-figure storyboard previs: draft with stick figures, one click to a continuous action blockbuster"
---

# action-previs

Use this skill when doing action-director previs (PREVIS). Specializes in **action choreography previs** — stick-figure action storyboards + character three-view images → board-by-board continuous action videos, focused on action beats, inter-board shot transitions, character consistency, and multi-board continuity.

> Adaptations for this environment: GPT Image 2 → `generate_image_v3` (stick-figure storyboards / scene images, 2K); Seedance 2.0 → `generate_video_v3` (omni reference, ≤15s per board); `resource_prepare_and_analyze` → `analyze`; `text_editor` → `write_file_v2`; `video_assembler` → `composite_video`; `<<<image_x>>>` → `reference_nodes`+`{{NodeKey}}`; character consistency → three-view images registered as persistent anchors. Generation failures follow **no-automatic-model-switching** semantics: for storyboard images, if GPT Image 2 fails you may fall back to Nano Banana Pro (same class of image capability); for video, if Seedance fails, stop the task, explain to the user, and ask whether to switch tools. cards/reply_to_user interactions → conversational pauses + enumerated options.

## Working Modes (ask first; user confirmation required; no automatic downgrade)

- **Mode A Concept → Storyboard → Video**: user provides an action concept → generate stick-figure PREVIS storyboard images first, then generate video after confirmation.
- **Mode B Storyboard → Video**: user already has PREVIS storyboard images → `analyze` parses them image-by-image and frame-by-frame, aligns to the Storyboard, skipping storyboard generation and going straight to video. Criteria: storyboard images uploaded directly at session start, or the user explicitly says "I already have storyboards"; **must NOT auto-downgrade to Mode A because nothing was uploaded — the mode must be confirmed by the user**.
- Either mode: if the user provides character three-view images, immediately `analyze` and register them as character key_elements; if not, prompt for upload before video generation. Confirm scene-image status at the same time (provided / to be generated / none — if none, video relies only on storyboard images + three-view images).

## Workflow & Dependencies

1. **Lock specs** (`write_file_v2`): project name / total board count / aspect ratio (default 16:9) / resolution (default 720p) / visual style lock (minimal stick-figure PREVIS hand-drawn style) / per-board duration cap 15s.
2. **Analyze inputs and register assets immediately** (`analyze`+`generate_image_v3`): Mode A — analyze three-view images / scene images (storyboards not yet generated); Mode B — structured parsing of all storyboard images image-by-image and frame-by-frame to output per-board "Storyboard mappings", then analyze three-view images / scene images (order: storyboards → three-views → scenes; consolidate the summary once all are complete). **Key rule — register immediately after analysis** (do not defer): three-view images → register asset_id → bind to element character; scene images → bind to element scene; Mode B storyboard images → bind to shot (if the Storyboard isn't built yet, register and record the mapping, then backfill the binding once built); output an asset registration list (asset name → asset_id → binding target) for verification; mark any unmatched items `[pending binding]` and prompt to confirm ownership.
3. **Build the Storyboard** (`storyboard_designer`): Mode A — pre-create shot placeholders (left empty, bound after generation) + create element character/scene; Mode B — fill in the mapping outputs board by board, creating element character per identified character and element scene per inferred scene switch from the continuity pre-assessment.
4. **Generate stick-figure storyboard images** (Mode A, `generate_image_v3`, GPT Image 2, 2K): ≤8 consecutive frames per board, 2×4 grid, uniform frame size; pause for confirmation after each board is generated.
5. **Scene images**: if provided, register and bind; if not, generate per the element scene description (2K), then pause for confirmation. When the same scene recurs across boards, generate only one image and bind it to all of them.
6. **Bind assets**: bind confirmed storyboard image / three-view image / scene image asset_ids to the corresponding shot/character/scene respectively.
7. **Generate action videos board by board** (`generate_video_v3`, omni reference): pause for review and confirmation after each board is generated before moving to the next.
8. **Assemble** (`composite_video`): stitch in Storyboard order, handling inter-board transitions and audio alignment.

**Dependencies**: 3→1; 4→3; 5→3; 6→3,4,5; 7→6; 8→7.

## Multi-Board Batch Sequence Control (5+ Boards)

- **Strict sequential generation**: Board 1→N one by one; parallel/out-of-order prohibited; only after each board is confirmed is its final_shot added to the next board's reference candidate pool.
- **Batch-of-5 segmentation strategy (activated at ≥10 boards)**: split into groups of 5 (1–5, 6–10…); after board-by-board confirmation of each batch, run one inter-batch consistency pre-check (character positions / appearance / scenes), produce a pre-check summary, fix issues, then proceed to the next batch — preventing problems from accumulating until they blow up at assembly.
- **Mid-process issue handling**: ① Quality below standard (appearance drift / beat misordering) → pause immediately without continuing; show the issue + fix directions (reference weights / prompts / change references); regenerate the current board after confirmation. ② Transition break (position/orientation inconsistent with the previous board's last frame) → regenerate with a mandatory starting-position constraint added to the prompt; if it still breaks after two attempts, let the user choose (accept the jump cut and flag for assembly handling / upload a transition frame as start_frame / revise the transition note and retry). ③ The same issue on 3 consecutive boards → judge it systemic; pause the batch, explain the root cause (insufficient three-view weight / vague description), and after supplementing high-quality three-view images or revising the element character, regenerate starting from the first affected board. ④ Single-board failure → skip and continue, keep a pending list, retry uniformly after everything is done; empty boards must not enter assembly.

## Structured Pause-Point Summaries (each point must show content + decision options; never just "continue?")

- **Pause point 1 (after specs are locked)**: show project name / total board count / aspect ratio / resolution / visual style / per-board duration cap / scene-image source (user-provided / to be generated / none). Options: ① Confirm and proceed to Storyboard; ② Modify a parameter.
- **Pause point 2 (after each storyboard image is generated, Mode A)**: show board number (Board 1/N) / generated image preview / that board's frame numbers (F1–F8) + brief action beats. Options: ① Confirm and continue to the next board; ② Adjust description and regenerate; ③ Skip (mark "pending fill-in" and continue for now). If a scene image was uploaded but its binding is unconfirmed, confirm it here as well.
- **Pause point 3 (after all storyboard images + scene images are ready and the Storyboard is built)**: show a full Storyboard summary — all element characters (with source: three-view images / pending upload), element scenes (with source: user-provided / generated / none), shot list (board number + one-line core action), bound-asset list. Options: ① Confirm and proceed to per-board videos; ② Revise an element/shot description; ③ **If any element character marked "pending fill-in" is missing three-view images, this step is a mandatory pause — wait for upload before continuing**.
- **Pause point 4 (after each board's video is generated)**: show board number / duration / reference input list (storyboard image / each three-view image / scene image asset_ids, whether the previous board's reference_video was used) / how the inter-board transition note was executed. Options: ① Confirm and continue; ② Regenerate (state the adjustment direction: camera movement / action beats / character appearance / other); ③ Accept but flag for manual handling during assembly.
- **Pause point 5 (after all boards are generated, before assembly)**: show the full final_shot list (board number + duration + whether flagged issues exist), total combined duration, consistency pre-check summary (character-position jump cuts / scene drift / appearance drift — counts and locations). Options: ① Confirm and proceed to assembly; ② Targeted regeneration of a specific board; ③ Accept existing issues and assemble directly (when the montage jump-cut intent is clear).

## Storyboard Image Frame-by-Frame Parsing (Mode B core, `analyze`)

Run structured parsing on each storyboard image; the output must map directly onto Storyboard shot fields:

**① Frame inventory & layout**: count the frames (≤16), confirm the arrangement (4×4 or other); if unnumbered, auto-label F1–FN in left-to-right, top-to-bottom order and note this; for low resolution / blurry frames, mark each affected frame number + confidence ("readable / partially readable / unreadable"), **never fabricate unreadable frames — leave the slot empty and mark `[pending user input]`**.

**② Per-frame structured extraction (every frame must include all fields)**:
- **Frame number** F1–FN (auto-assigned or citing the on-image label).
- **Shot size**: pick the closest from EXTREME WIDE / WIDE / MEDIUM / MEDIUM CLOSE-UP / CLOSE-UP / EXTREME CLOSE-UP; if the image has a label, cite it and note the mapped term in parentheses (e.g., "WS → WIDE").
- **Camera movement**: push / pull / pan (direction) / track / high angle / low angle / static; inferred from in-frame arrows, label text, or perspective lines; if undeterminable, mark "static (inferred)".
- **Primary action beat**: the active party's (stick figure's) core action, in "body part + movement direction + amplitude" format (e.g., "right arm swings up-right in a large arc"); if speed lines / trail lines are present, add `[speed feel: explosive / fluid / heavy]`.
- **Hit / reaction action**: if there's a second character, describe its reaction posture and movement direction; if not, mark "single-character frame".
- **On-image label transcript**: transcribe verbatim all text labels in the image (Chinese or English); if none, mark "no text labels".
- **Motion trajectory arrows**: describe each arrow's start point / direction / inferred meaning (e.g., "character displaces from lower-left toward upper-right of frame").

**③ Whole-board camera blocking summary**: summarize the overall rhythm of camera movement (one sentence covering opening shot size → mid changes → closing shot size, e.g., "pushes from WIDE to ECU; the board is dominated by tracking movement"); identify clear cut points within the board (cut lines / "CUT" labels) and mark their positions; summarize the board's overall momentum (primary movement direction + rhythm intensity: undulating / sustained burst / gradual build-up).

**④ Multi-board continuity pre-assessment**: with multiple storyboard images, after analyzing each board additionally output a cross-board continuity summary — whether character position/orientation matches between adjacent boards' closing frame (previous board FN) and opening frame (next board F1) (if inconsistent, mark `[needs inter-board transition note]`); cross-board identity consistency of the same character (identified via body proportions / character labels); cross-board scene switches (obvious background geometry changes) — mark the new scene and recommend creating a separate element scene.

**⑤ Storyboard mapping output format** (field names aligned with the shot definition):
```
[Board N mapping]
- Associated storyboard board: [user-provided board number or auto-numbered Board_N]
- Frame range: F1–FN (N frames total)
- Action beat sequence: F1: … ; F2: … ; … ; FN: …
- Camera blocking: opening [shot size] → [movement type] → closing [shot size]; in-board cut points: [none / F_N→F_N+1]
- Inter-board transition note: [continuity statement on character position/orientation vs. previous board's last frame; for the first board write "first board, no preceding reference"]
- Duration cap: 15s
- Pending items: [list all [pending user input] or [needs inter-board transition note] marks]
```

## Three-View Image Analysis (`analyze` — extract visual anchors stably reusable across boards)

Each item requires a concrete description, not "normal / nothing special":
- **① Facial identity anchors**: face shape contour (square jaw / oval face / wide cheekbones); key facial features (eyebrow shape, thickness & color; eye shape & spacing; nose bridge height & width; lip shape & color); skin tone & texture (shade range, e.g., warm medium-tan / pale cool-toned); hairstyle structure (hairline position, parting, length, texture — straight / curly / voluminous / flat to the scalp); hair color (primary + secondary color / highlights — avoid writing just "black"; add sheen tendency: matte black / blue-black gloss).
- **② Body proportions**: overall height & build classification (tall / medium / short & stocky / slender); visual impression of shoulder width and waist-hip ratio; locally identifiable features such as hands / neck.
- **③ Wardrobe**: top (style + primary color + secondary color/pattern + collar & sleeve type); bottoms (style + primary color + length + fit — slim / loose); footwear (type + color + sole thickness); 2–3 material/texture keywords (matte cotton / shiny leather / worn denim); signature accessory (type + color + wearing position, e.g., right wrist silver chain bracelet).
- **④ Three-view consistency check**: compare front/side/back images; point out color differences or detail inconsistencies across views (e.g., wardrobe darker in side view, backpack visible from back but not reflected in the front view); note "front view takes precedence" or "user's description takes precedence"; if any view is missing, mark the missing direction and state the impact on subsequent generation.
- **Output format**: structured text segmented by ①–④, listed as short phrases / keyword groups for direct copy-citation; do not output narrative paragraphs.

**Scene reference image analysis**: identify spatial structure and key visual anchors (environment type — indoor / outdoor / specific location; main compositional elements — architectural silhouettes / ground materials / light-source direction & color / background layering; visual features stably reusable across boards), outputting the basis for a structured element scene description.

## Storyboard Design (with beat-density tiers)

- **Key Elements**: create an element character for every character that appears (description based on three-view analysis; if no three-view images provided, mark "pending fill-in" and prompt for upload); create an element scene for every major scene/location (spatial structure / light direction / background anchors / color mood — if a reference image exists, the description must match it without contradiction; if not, provide a sufficiently detailed description for generation).
- **Shot design (one board = one shot, ≤8 action beats)**: include associated storyboard board (storyboard image asset_id or board number), action beat sequence (brief per-frame notes on core action / direction / momentum), camera blocking (opening/closing framing, movement type, shot-size changes), inter-board transition note (continuity requirements vs. the previous board's last frame; leave empty for the first board).
- **Beat-density labeling (core; not a uniform ≤15s for all)**: label each board high density (burst board) / low density (transition board):
  - **Burst board**: continuous strikes / collisions / multi-person melee; tightly causal beats with no pause or wind-up segments; target **6–8s**.
  - **Transition board**: slower rhythms such as widening distance / wind-up / breathing space / large camera push-pull; target **10–15s**.
  - For mixed boards, classify by the dominant content, or note the intended segmented rhythm. **Fill duration targets per beat density; do not force a uniform 15s cap**.
- **Mode B specifics**: fill shot fields one-to-one directly from the "Storyboard mapping output", **keeping the original inferences without self-elaboration**; fields marked `[pending user input]` / `[unreadable]` keep the same marks, pending pause point 3 for filling or abandonment, and **must not be filled with speculation**; add cross-board element scenes per scene-switch detection by the analysis tool (source marked "[analysis-tool inference, pending user confirmation]"; if none detected, default to sharing the same scene); create separate character element entries per identified character, leaving description empty or with minimal features only (e.g., "tall build, active party on the right") until three-view images complete it.
- **Audio track**: plan an audio_layer if needed; **action PREVIS defaults to no narration track**.

## PREVIS Storyboard Image Prompt (generate_image_v3 — GPT Image 2)

**Core design principle: self-explanatory** — the image should carry enough visual information density that Seedance can read the action choreography / spatial relationships / camera intent directly from the image, minimizing reliance on text; every panel must be understandable from its labels / arrows / lines alone, even without reading the prompt.

**Core constraints (required in every prompt, placed first)**:
- **Style lock**: minimal, rough hand-drawn storyboard style; all characters rendered only as stick figures; real human anatomy / musculature / clothing / pants / shoes / any character detail prohibited.
- **Line style**: uneven-width hand-drawn pencil/charcoal-feel lines; slight wobble and irregularity allowed (sketch tension); smooth vector lines / digital clean-up look prohibited; key movements in heavy lines, auxiliary reference lines (perspective lines / trajectory lines) in thin dashes.
- **Background treatment**: minimal; spatial relationships indicated only by geometric outline lines (boxes = buildings/cover, horizontal lines = ground/steps, diagonals = slopes); realistic textures / filled color blocks / detail maps prohibited; overall pure-white or very light cool-gray paper tone — lines only, no gradient or shaded fills.
- **Label language**: all camera labels / action notes / technical directives in **English** (PUSH IN, WIDE SHOT, POV, IMPACT, ×2 SPEED); Chinese inside frames prohibited.
- **Multi-panel single-image layout**: declare the panel count explicitly (≤16), arranged as a 4×4 grid; each panel independently composed, separated by thin solid lines; each panel may carry a small gray frame number (F1–F16) in its top-left corner.

**Seven layers of per-panel visual information density (core — missing any layer leaves Seedance with insufficient reference information)**:
- **① Motion vector arrows**: draw a separate arrowed trajectory line for each moving limb/body part; arrow length reflects amplitude (large movement = long arrow), thickness reflects force (burst = thick arrow); draw a separate full-body displacement arc for whole-character movement, distinguished from limb arrows by line style (limbs = solid, displacement arcs = dashed).
- **② Momentum trail lines**: at the end of a moving limb (fist / toe / knee), draw 2–4 parallel trail lines pointing opposite to the motion to convey speed; for burst actions (straight punch / leg sweep), extend trails to the panel edge or very near it to convey penetrating force.
- **③ Impact / contact labels**: for any frame with contact or imminent contact, draw an explosive radiating burst (star/dahlia shape) at the contact point + an English label (IMPACT/HIT/BLOCK/GRAB); for close-range force delivery (close-quarters fighting), additionally draw concentric circles or compressed ripple lines to show force transfer.
- **④ Spatial depth markers**: every frame has a clear horizon line (thick horizontal dashed line); in multi-character scenes, each character has a ground shadow dot / short horizontal line underfoot (indicating stance); foreground characters in thick lines, background characters in thin lines to form depth layering.
- **⑤ Character ID labels**: with ≥2 characters, give each character an uppercase letter label beside the head (A/B/C); the active party marked with a circle, the party under attack marked with a box (`[B]`); labels stay consistent across all frames of the board and do not change frame to frame.
- **⑥ Camera info bar**: reserve a thin horizontal label bar at the bottom/top of each panel — shot-size abbreviation (WS/MS/MCU/CU/ECU) + camera movement (STATIC/PUSH/PULL/PAN-L/PAN-R/TRACK) + optional speed modifier (SLOW/NORMAL/SNAP); format example `MCU | PUSH | SNAP`.
- **⑦ Inter-frame transition indicators**: at divider lines between adjacent panels — small arrows (→) indicate flow for continuous action; cuts marked CUT; shot changes (scene changes) marked NEW SHOT with a double vertical line replacing the single divider.

**Prompt structure (in order)**: 1. Style constraints + the 7-layer density requirements (compressed into concise directives); 2. Panel count & layout declaration (e.g., 8-panel grid, 2 rows × 4 columns); 3. Panel-by-panel description by number (camera info + character label assignments + primary action vector directions + impact point positions + inter-frame transition types); 4. The board's overall action-choreography rhythm (one sentence on the causal chain, e.g., A breaks through the defense → closes in and lands a flurry → B/C go down one after another); 5. For ImageToImage mode, specify the reference source and reference dimensions (composition / motion / camera language), **excluding character-appearance references**.

## Character Reference Image & Scene Concept Image Prompts

See `references/prompt-library.md` (character reference images, 5 steps: two-panel layout / facial lock / three wardrobe elements / photoreal style isolated from PREVIS / fixed exclusions; scene concept images, 4 steps: 3 spatial-composition anchors / light source / style tone / exclusions).

## Video Prompt (generate_video_v3 — Seedance 2.0)

**Core principle: the storyboard image leads; the prompt fills gaps**. The PREVIS storyboard image (`<<<image_1>>>`) already encodes extensive action and camera information via motion vector arrows / trail lines / impact labels / camera info bars — it is Seedance's **primary reference source**; the prompt's sole job is to cover what the storyboard image cannot encode: speed-texture words, character causality, and sound-effect directives.

**[Mandatory Subtraction Principle]** Anything the storyboard image already expresses clearly, the prompt **must omit or reduce to 1–2 keywords** — never elaborate:
- Motion vector arrows already present → **omit** limb-action descriptions, keep only speed-texture words (e.g., explosive).
- Camera info bar already present (MCU|PUSH|SNAP) → **compress** camera movement to one phrase (medium close-up, push in); don't elaborate.
- Impact label already present (IMPACT) → **omit** contact-point descriptions, keep only the SFX tag (`<sharp impact crack>`).
- Character labels and position info already present → **omit** spatial-blocking descriptions.
- ✅ Correct (storyboard already has arrows): `F1: explosive; F2: recoils from impact, weight shifts back; F3: snapping`
- ❌ Wrong (duplicates what the storyboard already shows): `F1: right arm swings upward in a 120° arc at explosive speed, fist clenched, elbow leads`

Violating this (prompt highly duplicative of the storyboard image) causes text weight to suppress the visual reference and generation to drift from the storyboard's intent.

**Reference input binding**: `<<<image_1>>>` = PREVIS storyboard image (primary); `<<<image_2>>>, <<<image_3>>>…` = each character's three-view images (one per character, in order of appearance); `<<<video_1>>>` = previous board's final_shot (only for extremely strong continuity; omitted by default).

**Prompt structure (motion-stack order; strictly follow the hierarchy)**:
- **① Camera movement**: if the storyboard info bar already labels it, write only a one-line summary without elaboration; the added value lies in speed-texture words. Format `[opening shot size] → [movement type] → [closing shot size]`; shot sizes locked to EXTREME WIDE/WIDE/MEDIUM/MEDIUM CLOSE-UP/CLOSE-UP/EXTREME CLOSE-UP; for multi-shot switches, separate in beat order with "→ cut →", no timecodes. Example: `WIDE SHOT, swift push in → cut → EXTREME CLOSE-UP on fist impact, lock-off`.
- **② Character action**: subtraction first — where storyboard arrows are already explicit, write only speed-texture words; elaborate only for causal relationships (weight shifts back after being struck / head-on clashes). For multiple beats, follow F1→F8 order, each beat containing only 【speed-texture word + causality (if any)】, separated by semicolons; for multiple characters, primary actions first, then hit/reaction, with subject-object clarified via in response / simultaneously / recoils. **Standard speed-texture words**: explosive / snapping / fluid / heavy / weightless / sluggish; **vague words like fast/slow prohibited**.
- **③ Multi-character scene specifics (mandatory at ≥2 characters)**:
  - **Subject order**: one independent sentence per character, in "active party → hit/reaction party → secondary bystander" order, separated by "—" or line breaks; **never merge two characters' actions into one sentence**. Active party = the one initiating force/displacement in the current beat; when both sides clash synchronously, treat the visual center of the frame (usually center frame, nearer foreground) as the active party.
  - **Causal connectives**: the hit/reaction party must be introduced with an explicit causal word — in response / simultaneously / recoils from / absorbs the impact / driven back by; **simple coordination with "and" prohibited** to avoid subject ambiguity.
  - **Frame-space allocation**: lock each character with an independent frame-position term; relative phrasing ("they stand together") prohibited. Two characters: default active party frame left/center-left, receiving party frame right/center-right (if the storyboard image shows the reverse, follow the storyboard image and note it); three or more characters: layered by foreground/midground/background depth (foreground = active party, midground = hit/reaction, background = secondary), each layer described with a sense of depth distance (e.g., pushed into the background, noticeably smaller in frame). When multiple characters move simultaneously, each character's movement-direction vector must be distinct (A drives forward toward frame right; B retreats toward frame left); vague phrasing like "the two clash fiercely" prohibited.
  - **One-to-one reference binding**: bind strictly one-to-one per character, in fixed order: storyboard image (`<<<image_1>>>`) → active party's three-view images (`<<<image_2>>>`) → hit/reaction party's three-view images (`<<<image_3>>>`) → secondary characters (`<<<image_4>>>` incrementing) → scene image (final image slot); after each binding, prefix the corresponding character's description sentence with a bracketed source placeholder, format `[ref:image_2] Character A: ...`; **never merge multiple characters' three-view images into a single image placeholder — each character occupies its own slot** to keep appearance-extraction weights independent.
- **④ Spatial blocking**: characters' position changes within the frame (frame left/right/center/foreground/background/off-screen); spatial relationships with scene elements must match the PREVIS background geometry; for entrances/exits, state direction explicitly (enters from frame left / exits top frame).
- **⑤ SFX & dialogue (only when not conflicting with a standalone narration track)**: Seedance official syntax goes at the end — SFX `<sound of heavy footsteps on concrete>` / `<sharp impact crack>` / `<whooshing air burst>`; dialogue `{EN: "Get down!"}` (language code first); ambience `<ambient urban noise, distant siren>`. **Priority: action-impact SFX > ambient atmosphere > dialogue**; when all three are present, list them at the end in this order.
- **⑥ Beat-density-matched speed-texture words (per Storyboard labels; appended to the end of ②)**: burst boards add `snapping cuts, explosive action rhythm, no slow motion, rapid kinetic energy`; transition boards add `deliberate pacing, building tension, smooth camera movement`; in both cases, fast/slow are prohibited as substitutes for the standard words.
- **⑦ Fixed negatives (must be appended to the end of every prompt)**: `no subtitles, no text overlay, no wardrobe change, no style shift between cuts` (no wardrobe change keeps wardrobe consistent with the three-view images; no style shift between cuts suppresses Seedance's automatic style/color shifts within multi-beat boards).

## Video Generation Reference Inputs & Multi-Board Progression Strategy

- **Per-board reference inputs**: ① **PREVIS storyboard image** (that board's asset_id; **primary visual reference, weighted above text**; the prompt strictly follows the subtraction principle); ② character three-view images (asset_ids of all characters appearing); ③ scene image (that board's element scene asset_id; omit if none); ④ previous board's final_shot (optional; use as reference_video only when scene/character-state continuity is extremely strong, otherwise omit to avoid unwanted action carryover). Duration rounds to whole seconds per beat density (burst boards near 6s, transition boards 10–15s), never exceeding 15s.
- **Multi-board progression**: tighten the reference_video threshold as board count grows — at ≤4 boards use normal judgment; **at ≥5 boards, only boards whose transition notes explicitly state "strong continuity" may reference a reference_video**, omitting it for other boards to keep errors from compounding board by board; **keep element reference-image weights consistent** — regardless of board number, the binding method and input order of three-view + scene images must exactly match Board 1; do not reduce later boards' completeness because "the first few boards are already stable"; **boards pending repair don't block subsequent boards** — when a board is marked "needs regeneration", later boards may continue (skip that board's reference_video chain and use the most recent confirmed final_shot directly as the continuity reference); after the repair is complete, if the immediately following boards were already generated, prompt the user to assess whether those boards need regeneration due to the missing reference.

## Cross-Board Consistency (Video Generation Stage)

- **Scene image reuse**: when the same element scene appears across multiple boards, forcibly reuse the same asset_id; duplicate generation / swapping in a new image prohibited; only when the user explicitly requests a scene-state change (time-of-day shift / post-destruction scene) may a new image be generated and registered under a separate asset_id. In every board's generation, even if the main action is unrelated to the background, the corresponding scene image's stable color tone and spatial structure must be included.
- **Character position continuity**: before generating each board, read its "inter-board transition note" — if it specifies the previous board's last-frame position (e.g., "Character A at frame right, facing left"), this board's prompt spatial-blocking layer must align the starting state to avoid a jump cut; when two boards have clear action causality (strike → fall), the next board's first action beat (F1) **must start from the struck character's force-receiving posture**, not a reset neutral stance; with no transition note (first board / explicit scene change), alignment is not forced — block independently per that board's storyboard image.
- **Three-view safety net**: every board's generation must include the three-view asset_ids of all characters appearing; even a character with minimal screen time on that board must not be omitted from the references, to prevent Seedance from redrawing appearances on its own under low reference weight.

## Assembly Consistency Check (`composite_video`; required before assembly)

- **Board-to-board splicing**: splice in shot order, **hard cuts by default** (no dissolves) to preserve action impact; where notes are marked "extremely strong continuity", an **ultra-short dissolve (≤4 frames)** may assist the transition to avoid a jump-cut feel.
- **Consistency-check priority: character-position jump cuts > scene visual-anchor drift > character-appearance drift**:
  - **Character position continuity**: check each adjacent board pair's joining frames (previous board's last frame vs. next board's first frame) for every character's frame position and orientation; obvious jump cuts (teleporting from left to right / orientation flips with no causal basis) get a marker at the cut point and assembly pauses for the user to choose (regenerate the later board with a forced starting position / accept the jump cut when montage intent is clear).
  - **Scene visual anchors**: for the same element scene across boards, verify that the background's main anchors (horizon height / main light-source direction / key background objects) are stable; obvious style drift / composition breaks get flagged.
  - **Character appearance drift**: note any visual differences in the same character's wardrobe color palette / hairstyle / signature accessory across adjacent boards, and prompt the user to assess whether to regenerate the affected board with stronger three-view weighting.
  - Handle the three separately without conflating them (the first affects narrative continuity; the latter two affect visual stability).
- **Audio**: each board's Seedance action SFX is kept by default; the BGM track (if any) is laid continuously across boards and not interrupted at cut points; with no narration track, moderately raise the action SFX volume to enhance impact.
- **Export**: resolution follows Final_Video_Spec (default 720p); aspect ratio defaults to 16:9.

## Co-loading (can be loaded together in one query)

No native source dependencies (the actors within the source are all internal stages; this skill is fully self-contained).

Boundaries (don't use this skill; route elsewhere): general previs-first workflows (storyboard panels first → preview → hero) → storyboard-cheatcode (that skill already back-references this one; the mutual boundary suffices); multi-panel storyboard boards rendered as a single image → storyboard-generation; photoreal motion/performance → cinematic-motion-realism; camera-movement vocabulary → cinematic-motion-language.