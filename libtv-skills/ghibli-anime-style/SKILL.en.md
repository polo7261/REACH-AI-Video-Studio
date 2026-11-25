---
name: ghibli-anime-style
description: "Hayao Miyazaki anime director: turns plots into heartwarming hand-drawn animated epics"
---

# ghibli-anime-style

Use this skill when reconstructing complex plots into cinematic hand-drawn animation **inspired by** Hayao Miyazaki's animation creation system. Focus: hand-drawn cel texture, natural vitality, fluid character performance, the poetic motion of flight and wind, grand fantasy worldbuilding, warm coming-of-age storytelling, and deep humanistic care. Abandon stiff static frame insertion or first-and-last-frame generation; directly bind character key_element and scene key_element as multimodal references to achieve high-fluidity, multi-perspective long-form video creation.

> **Style tribute, not precise imitation**: Reference the publicly known aesthetic features and academic analyses of the Miyazaki system (hand-drawn texture/nature worship/anti-war/environmentalism/female independent growth/romance of flying machines/fantasy architecture/daily-life details/complex conflicts without absolute good and evil/Joe Hisaishi-style symphonic emotional scoring). **Strictly forbidden to directly replicate existing animated characters, specific shots from existing films, or copyrighted names/iconic character appearances/specific scenes; instead create entirely original stories, original characters, and original worldviews.**
> Adaptation for this environment: Seedance / MultiModalToVideo → `generate_video_v3`; TextToImage → `generate_image_v3`; `text_editor` → `write_file_v2`; `video_assembler` → `composite_video`; `text_to_instrumental`/audio → `generate_audio`; `@assets`/placeholders → `reference_nodes`+`{{NodeKey}}`; consolidation of the source's "membership/1080p resolution tier/explicit model naming" (default 720p; honestly inform if higher is needed); the **voice-extraction binding chain** (the source splits audio from generated videos as later voice references) is unavailable in this environment; instead use "keep character dubbing consistent via `generate_audio` with the same parameters", as noted below. **Prompt writing/deconstruction/storyboard craftsmanship is fully inlined in this skill, with no reliance on external craftsmanship skills.**

## I. The 7 Supreme Execution Principles

1. **Reject static PPT feel and cheap animation feel**: Strictly forbid static shots with no action/no expression/slow motion to pad duration or pure PPT-style transitions; humans, animals, natural elements, and machinery must all have real motion logic; characters must have natural, vivid, nuanced emotional expressions, especially the sense of life in child characters—unsteady balance, startled blinking, hesitant pauses, panting while running, clothes hems and hair swaying in the wind, etc.
2. **Adhere to hand-drawn animation texture**: Default to a high-quality 2D hand-drawn animation style, emphasizing soft contour lines, watercolor backgrounds, layered cel texture, natural brushstrokes, hand-drawn light and shadow, subtle paper grain, and a frame-by-frame animation feel; strictly forbid cheap 3D plastic texture, overly smooth computer-animation texture, or stiff cartoon decal feel.
3. **Fully unleash the model's shot-cutting potential**: Split long scripts into multiple 15-second video segments (each shot); within each 15-second segment, plan **3–5 high-frequency shot slices** to create clear plot progression and spatial variation.
4. **Nature, wind, water, light, and machinery must be able to move**: The key is not just that characters move, but that the entire world breathes—wind blowing through grass blades, clouds drifting slowly, reflections on streams, dappled tree shadows, boiler steam, turning gears, propellers, clothing folds, animal ears and tails—all must have subtle movements consistent with physical laws.
5. **Spatial 3D depth and layered animation feel**: Reject flat sticker-like flatness. The frame must have a clear [foreground-subject-background] three-layer structure and reflect cel layering logic: foreground moves faster, midground characters move naturally, distant mountains and clouds move slowly, and the background watercolor texture stays stable.
6. **Dual-modal multi-character reference flow**: Do not generate multi-grid storyboard references; directly use character key_element design sheets + scene key_element design sheets for multimodal reference binding, maximizing character and worldview consistency.
7. **Prompt conventions**: All prompts must be written entirely and consistently in Chinese; any English words/letter marks/characters are forbidden (tool names/model names/technical asset names may retain necessary English, but visuals/style/actions/dialogue/narration/negative prompts etc. must all be in Chinese).

## II. Upfront Selections and Spec Confirmation (Phase One)

Before parsing any specific script, you must first present the following choices to the user; after confirmation, write them at the top of the spec document:
1. **Video generation model/resolution**: This environment defaults to 720p; honestly inform if a higher resolution is needed (consolidating the source's "Seedance 2.0 requires membership/1080p requires membership" tiers).
2. **Single video segment duration**: Locked to 15 seconds by default (to maximally unleash auto shot-cutting and multi-shot serialization capabilities).
3. **Aspect ratio**: 16:9 (default), 9:16, 1:1.
4. **Output language and dialect accent**: Mandarin (default) / Japanese-flavored Chinese dubbing style (gentle, restrained, and clear; still generated in Chinese) / children's natural speech / young-girl coming-of-age narrative tone / rural everyday-life accent / other user-specified languages and dialects.

After confirmation, initialize and lock the spec file using the standard template in the next section, as the single source of truth for aligned execution of subsequent steps; no unauthorized changes allowed.

### Final_Video_Spec Standard Spec Template (initialized via `write_file_v2`)

```
# Global Video Creation Spec (Final Video Spec)

## 1. Core Technical Specifications
- Video generation model: [this environment's default model / honestly inform if higher resolution is needed]
- Output resolution: [720p default / higher requires informing]
- Single video segment duration: [locked to 15 seconds by default]
- Aspect ratio: [16:9 / 9:16 / 1:1]
- Output language and accent: [Mandarin / children's natural speech / rural everyday-life accent / custom]

## 2. Story Script and Storyboard Outline
- Story synopsis: [brief outline of the story and its emotional tone]
- Original story content (red-line locked): [fully enter the user-provided or confirmed script, 100% faithful to core events, never delete or alter]
- Core coming-of-age theme: [leaving home / seeking a name / understanding nature / rejecting war / learning independence / making peace with fear]
- Worldview rules: [laws of nature / magic rules / machinery rules / deity rules, explicit and internally consistent]
- Multi-character feature control list (key_element spec):
  - Character A (element character): [name/age/personality/primary visual color/clothing material/signature props/performance and expression tendencies/binding anchor]
  - Character B (element character): [same as above]
  - Animal or spirit character (element character): [appearance/locomotion/sound/relationship with protagonist/binding anchor]
- Visual State Ledger:
  - [Record in real time the physical/props/lighting/weather/character position and emotional end-state anchors at the end of each 15s segment, for start-state inheritance verification of the next segment]

## 3. Global Color Aesthetics and Tone Design
- Primary palette scheme: [forest life colors / sky flight colors / ocean wave fairytale colors / steam machinery colors / spirited-away night lamp colors / custom]
- Color slot configuration (Color Slot System):
  - Soul color (film-wide main tone): [color value and emotional definition]
  - Identity color (character clothing/props): [Character A color value / Character B color value]
  - Nature colors (forest/sky/sea surface): [forest green / sky blue / cloud white / soil ochre]
  - Fantasy colors (magic/deities/flying stone/spirit light): [warm gold / cyan blue / soft white / faint glowing green]
  - Danger colors (war/pollution/runaway machinery): [rust red / soot black / dark purple / sickly green]

## 4. Character Voice and Sound Characteristics
- Voice language type: [follows the Phase One output language and accent choice]
- Voice description binding: voice characteristic descriptions for each character (e.g., "a clear but slightly timid girl's voice", "a gentle, steady boy's voice") + animal/spirit sound effects (purring/breathing/low humming/wind-chime-like soft sounds).
※ This environment has no capability to "extract voice timbre from generated videos for later reference": each character's voiceover is generated with `generate_audio` using the same voice description + same parameters to maintain cross-shot consistency.
- Dedicated BGM recommended configuration (audio_layer planning): [piano + strings + woodwinds + harp + accordion + light percussion]

## 5. Phase Work Tasks and Specific Execution Instructions
- [Consolidate, append specific instructions for subsequent steps and user fine-tuning constraints, ensuring subsequent steps are strictly executed without omission]
```

## III. Execution Flow (8 Phases, Pause at Each Phase, Strictly Forbidden to Run Through in One Go)

1. **Read Input and Confirm Specifications**〔Mandatory Pause〕: Confirm preliminary specifications; `write_file_v2` writes the specification document. When the user has provided a story script or explicit instructions, **record them completely without omission into the specification document** as long-term global context to avoid forgetting.
2. **Story Framework and Storyboard Script Design**〔Mandatory Pause〕: If a story exists, go directly to storyboarding; if not, first communicate to confirm the framework/protagonist growth theme/fantasy rules/nature-machine conflict core before writing the storyboard. **Miyazaki-style narrative core**: The story cannot be mere spectacle; it must have a clear growth arc and world relationships—the protagonist starts from "fear, dependence, confusion, or avoidance," passes through trials in a strange world, and gradually learns courage, labor, responsibility, empathy, or self-identity. **Multi-perspective conflict**: Strictly forbid simple good-vs-evil dichotomy; humans/nature/machines/deities/animals/villain forces should all have their own logic, and even nature-destroying parties should have survival reasons or historical backgrounds. **Ledger mechanism**: At the end of each 15s segment, record character positions/poses/props/weather/natural motion/lighting direction/emotional states, inherited at the beginning of the next segment. Each 15s segment (each shot) is split into 3–5 internal sub-shots, including [foreground-subject-background] layering, vivid facial movements, natural coherent dialogue, ambient sound effects, and details of wind/water/light/animal/machine motion. Pause to request confirmation.
3. **Multi-Character and Scene Design Image Generation**〔Ask and Pause〕: First ask the user whether to upload their own character/animal spirit/machine/scene reference images. If uploaded, pause and wait, then register them as anchor bindings upon receipt; if generation is chosen, call `generate_image_v3` to generate (see Section V). After generation, display and pause for confirmation.
4. **Character Voiceover**〔Mandatory Pause〕: Use `generate_audio` with the same voice description + same parameters to generate voiceover for each character, serving as the unified voice basis for that character in all subsequent shots, ensuring consistent voice across shots (the chain "generate 4–6s design video → extract audio as key_element_audio voice reference" is unavailable in this environment; faithfully downgrade to same-parameter voiceover). Pause to report.
5. **Video Material Generation**〔Generate Step by Step and Pause for Confirmation〕: `generate_video_v3` directly uses character/scene/machine key_element design images as multimodal input. After each 15s segment (each shot) is generated, pause to communicate and confirm, ensuring no teleportation, no stiff expressions, no cheap 3D texture, no character floating, and no mechanical motion errors. Must strictly verify against the visual state ledger whether the current segment's beginning connects with the previous segment's ending in terms of actions/props/character positions/weather/natural motion/lighting direction/emotional states.
6. **BGM Direction Confirmation and Generation**〔Mandatory Pause〕: Confirm with the user an independent audio_layer plan matching the overall emotional arc of the film; recommend a warm symphonic instrument library (piano, string ensemble, violin, cello, flute, oboe, clarinet, French horn, harp, glockenspiel, accordion, xylophone, soft choir texture, children's music box timbre). Music direction is chosen per plot (see 6.1). After confirmation, use `generate_audio` to generate pure instrumental BGM and register it as an anchor.
7. **Timeline Composition and Editing**〔Mandatory Pause〕: After all materials are generated and confirmed, call `composite_video`, importing independent audio tracks (ambient sound/dialogue/animal spirit sound effects/BGM/narration) and video tracks (each shot), with precise beat-syncing, fine volume adjustment, and seamless hard cuts. Confirm composition quality, ensuring vivid visuals, coherent plot, a living natural world, a clear character growth arc, and no rigid PowerPoint feel.
8. **Animated Film Poster Cover Design**〔Step-by-Step Extension with Pauses〕: `generate_image_v3` designs a cinematic poster cover with hand-drawn animated film feel, natural fantasy worldview, where the protagonist together with wind/clouds/forest/aircraft/animal spirits forms a narrative image. Strictly forbid replicating any existing animated characters or existing film poster compositions. Steps: ① First generate the 16:9 cover, pause to display for confirmation; ② After confirmation, extend to generate the 3:4 and 4:3 aspect ratios, completing the full deliverable output.

Dependencies: 2→1; 3→2; 4→3; 5→4,3; 6→5; 7→6,5; 8→7. Each phase's communication confirmation point is a hard pause point; if the user requests modifications, roll back to the corresponding step and re-establish.

## IV. Multimodal Deconstruction Specifications (Four Deconstructions—The Operational Layer of the "Everything Can Move" Principle) ★

### I. Character Movement and Expression Performance Deconstruction
Perform facial and physical feature analysis at the element character level:
1. **Facial Micro-movements**: Identify script emotional turning points (fear/curiosity/sulking/feeling wronged/mustering courage/surprise/relief). Children's or young girls' expressions must be delicate and natural: rapid eye blinks, slight eyebrow raises, hesitant lip-pressing at the mouth corners, slightly puffed cheeks, quick breathing followed by slow calming. Adult characters are more restrained: steady gaze, relaxed or tense jaw, brief silence before speaking. Animal or spirit characters express emotions through ears, tails, tentacles, body expansion/contraction, and changes in eye size. **Refuse expressionless faces, fake smiles, and rigid puppet-like stiffness.**
2. **Physical Interaction Feedback**: Analyze the interaction mechanics between characters and environmental props (element prop)—leaning body weight forward when pushing open a wooden door, shoe soles bending grass blades when running across a meadow, fingers gripping tight when seizing an aircraft handrail, fabric lagging and swinging when wind blows a cloak. Child characters have unstable center of gravity: body slightly leaning forward when running, stumbling steps when stopping suddenly. Flight scenes must consider wind resistance, gravity, lift, inertia, and body tilting during turns.
3. **Multi-Character Interaction and Gaze**: Plan multi-character gaze intersections and body orientations. **When Character A speaks, Character B must not stand motionless**; there must be small reactions: blinking, lowering the head, turning around, fingers clutching clothing edges, toes shifting slightly. Animal or spirit characters must genuinely interact with human characters: approaching, retreating, sniffing, nuzzling hands, hiding, following, alertly perking ears.

### II. Nature and World Motion Deconstruction
1. **Wind**: Identify all wind-affected elements (grass blades/tree canopies/hair/clothing hems/curtains/flags/clouds/smoke); wind must produce visible motion. Gentle breeze = grass blades lightly swaying, hair strands softly moving; strong wind = clothing swinging broadly, body tilting, clouds flowing rapidly; flight wind = hair and clothing stretched backward, eyes slightly narrowed.
2. **Water**: Rivers/waves/raindrops/puddles/reflections must all have a hand-drawn animation feel. **Water surface reflection colors are darker than the actual object, slightly less saturated, and slightly deformed with the ripples**. Raindrops falling on water must have three stages: impact, spreading, and disappearing.
3. **Plants and Forest Vitality**: The forest is not a static background; leaves/grass/moss/vines/petal spore particles should all have subtle motion. Distant mountains use atmospheric perspective (bluish, low saturation, low detail). Foreground plants use the clumping method and brushstroke method, with each leaf and grass stem's direction not entirely identical.
4. **Machines and Aircraft**: When aircraft/steam machines/moving buildings/boiler devices appear, analyze gears/propellers/linkages/steam valves/piston motion. **Machine motion must have weight, rhythm, and noise, and must not slide illogically like a magic decal.**

### III. Three-Dimensional Space and Cel Layering Deconstruction
1. **Foreground Layer**: Identify foreground objects that enhance depth of field (grass blades/tree branches/window frames/clouds and mist/small birds flying past the lens/nearby water droplets/boiler pipes); foreground elements should have slight defocus or rapid lateral movement, reflecting a layered animation sense of space.
2. **Subject Layer Focus**: Clarify the subject's position and motion trajectory, ensuring characters are on a clear focal plane. Hand-drawn animation does not pursue live-action photography-style excessive blur, but rather conveys depth through line clarity, color saturation, and layered motion.
3. **Background Layer Depth**: Extract the perspective relationships of distant mountains/cloud layers/buildings/forests/horizon lines. The background should have a watercolor hand-drawn texture and must not look like photographic decals.

### IV. Acoustic Purity Deconstruction
1. **Dialogue Acoustic Environment**: Determine the dialogue sound field according to the space—sounds diffuse softly in the forest, there are slight reflections inside the wooden cabin, dialogue during flight is affected by wind noise, and seaside dialogue mixes with wave sounds. Children's dialogue should be natural, without adult intonation, without over-explanation.
2. **Physical Sound Effect Positioning**: Extract subtle foley sounds and map them to the corresponding audio_layer (grass leaf rustling/wooden door creaking/boiler gurgling/steam hissing/fabric rustling/feet stepping on soil/raindrops falling on leaves/wings flapping/propeller spinning). **It is forbidden to directly write background music descriptions in video prompts; music is synthesized in post-production.**

## V. Storyboard Design Specifications (storyboard Craft) ★

### 5.1 Core Element Design
1. **Multi-character Elements (element character)**: For protagonists, prioritize ordinary people with growth potential such as boys, girls, ordinary laborers, apprentices, pilots, forest guardians, bakery assistants, mechanics, village children, and travelers. **Characters must not be perfect heroes from the start; they must have flaws** (timidity/impatience/dependence/getting lost/avoidance/stubbornness/overconfidence or ignorance of nature). Character growth must be shown through action (labor/caring for others/repairing machinery/crossing forests/protecting animals/admitting mistakes/making choices). **Female characters must be independent and not rely on male rescue** (they may be afraid, but must drive the story through their own judgment and actions). **Male characters must not only serve the savior function**; they should also have vulnerability, confusion, being helped, and a growth process. Animal, spirit, and deity characters must have independent will, not just be cute pets or decorations.
2. **Scene and Prop Elements (element scene / element prop)**: Each major scene must have complete functional structure—wooden cabins must have kitchens/stoves/storage shelves/windows/traces of life; aircraft must have control sticks/propellers/wing surfaces/engines/fuel pipes or steam pipes; towns must have street slopes/drainage ditches/bakeries/stations/clock towers/resident balconies; forests must have tree species/moss/decayed wood/streams/insects/animal tracks. Props must have narrative functions (name tags/old keys/flying goggles/hand-drawn maps/broken mechanical parts/seeds/wind chimes/lunch boxes/herb pouches/blue hair ribbons, etc.).
3. **Worldview Elements**: Fantasy rules must be clear (where magic comes from/why spirits appear/how machinery works/why nature is angry/how the protagonist builds a relationship with the world); spectacles must not be piled up without rules, and all fantasy elements must serve the theme. The worldview must include the relationship between nature and humans (symbiosis/misunderstanding/destruction/restoration/reverence or reconciliation).

### 5.2 Shot and Storyboard Design (Miyazaki Animation Visual Grammar)
Each 15s segment (one shot) is strictly broken into 3–5 high-frequency sub-shots:
1. **Composition Design**:
   - **Layered Cel Composition**: Clearly define three layers: foreground/midground/background. Foreground = grass blades/tree branches/clouds and mist/window frames/flying birds; Midground = character actions; Background = watercolor landscapes/buildings/distant mountains/sky.
   - **Natural Wide-Angle Feel**: Outdoor scenes should mostly use open compositions, expressing sky/wind/distant mountains/forests/sea surface, creating a sense of freedom and adventure.
   - **Life Detail Composition**: Indoor scenes establish a warm sense of daily life through details such as tabletops/boilers/windowsills/clotheslines/bowls and chopsticks/books/toolboxes.
   - **Aesthetic Quota System**: Exaggerated wide-angle perspective **at most 1–2 times in the entire film** (only in key scenes such as flight dives/appearance of giant creatures/machinery out of control); overly symmetrical composition **at most 1 time in the entire film**, or not at all; the remaining shots use natural, simple, narrative-serving animation film compositions.
2. **Camera Movement**:
   - **Flight Shots**: Flight is an important poetic element. If the plot allows, the film should include at least one flight or high-altitude scenery shot, but it must serve the plot; it must reflect wind resistance, body tilt, cloud depth, and differences in distant scenery movement.
   - **Low-Angle Children's Perspective**: The world of child protagonists should appear slightly enormous—door handles/tables/adult bodies/forest tree trunks can all appear taller, expressing the unfamiliarity of a child's perspective.
   - **Lateral Tracking of Running**: When the protagonist runs across grass/streets/bridges/forest paths, the foreground sweeps by quickly while the background moves slowly, creating layered animation depth.
   - **Close-ups and Micro-Actions**: Design hand-drawn animation close-ups such as fingers clutching clothing hems, shoes stepping in muddy water, eyes widening, hair blown by wind, boiler valves trembling.
   - **Quiet Nature Observation Shots**: Each segment should not be entirely plot progression; one brief nature observation shot may be added at key moments (cloud shadows sweeping across grassy slopes/dragonflies resting on water surfaces/wind blowing through clotheslines) to establish a sense of life.
3. **Rhythm Design**: Miyazaki-style rhythm is a wave-like rhythm of "**tension—relief—wonder—action—emotional settling**", not constantly high intensity. Within 15s, there can be one small action goal (chasing a hat blown away/opening a mysterious door/seeing a giant spirit for the first time/fixing a mechanical part/gathering courage to say a sentence in the rain). **Dialogue must be natural and concise; characters must not be allowed to explain the worldview at length**—the worldview should be shown through actions, environments, props, and visual details.

### 5.3 Independent Audio Track Design (audio_layer Specifications)
1. **BGM**: Planned as an independent audio_layer (type music/bgm); recommended is warm, bright, purely instrumental scoring with a sense of growth and adventure (piano/string ensembles/flute/oboe/clarinet/French horn/harp/glockenspiel/accordion/xylophone). The music should be melodic but not overly sentimental, expressing hope, wind, distant places, childhood, nature, and adventure.
2. **Ambient Sound Effects and Dialogue**: Each sub-shot must include multi-track planning of clean, precise natural and daily-life foley (audio_layer type sfx). **Dialogue is planned as a dialogue attribute embedded in the corresponding shot**, concise and sincere with a child's or young person's spoken feel, avoiding preaching/adult-style philosophical line stacking. Expressing the theme should be accomplished through one plain but powerful sentence, for example: "It's not a monster; it's just angry." / "I don't want to run away anymore." / "The wind is telling us there's still a road ahead." / "If you forget your name, you won't find your way home."
3. **Narration/Monologue (narration VO)**: Planned as an independent audio_layer (type narration); a TTS description must be explicitly set.

## VI. Multi-Segment Continuity and Narrative Logic Specifications (Visual State Ledger Operation Layer) ★

1. **Visual State Ledger Mechanism**: At the end of each 15s segment (each shot), **mandatory recording of the current timeline end-state anchor**:
   - Character physical state: position, posture, expression, clothing, hair, whether injured, whether soaked.
   - Prop state: whether the map is open, whether the aircraft is smoking, who holds the key, whether the animal is following.
   - Natural state: wind direction, rain intensity, cloud layers, sun position, forest light and shadow, water surface ripples.
   - Emotional state: fear, gathered courage, confusion, trust, dejection, relief.
   - **The next 15s segment script must inherit the previous segment's end-state anchor within the first 3 seconds.**
2. **Action Continuity**: If the previous segment ends with the character reaching out to open a door, the next segment's opening must complete the action after the door opens; if the previous segment ends with the aircraft beginning to stall, the next segment's opening must inherit the tilt, wind sound, and the character gripping the handrail; if the previous segment ends with the rain starting to intensify, the next segment's opening must show the character's clothing and the ground already wetter.
3. **Logical Progression**: Each 15s segment must serve the overall growth arc; questions raised in previous segments must be answered in later segments; **each segment's material is strictly forbidden to be mutually unrelated like independent short films**; the audience must be able to understand where the characters are, what they are going to do, why they are afraid, why they keep moving forward, and what changes have occurred in the world.
4. **Theme Control**: Anti-war expression must not become violent spectacle; it should be embodied through ordinary people's fear, ruins, aircraft shadows, children's silence, and technology out of control; environmental expression must not become slogans; it should be embodied through polluted rivers, angry animals, and forests recovering their vitality; **growth expression must not rely on narration to explain; it should be accomplished through the protagonist's actions**.

## VII. Image Asset Generation and Binding (media Adaptation to 13 Tools)
> **[Red Line Locked · Highest Priority]** All prompt content for video/image/audio generation (scene descriptions / style descriptions / action instructions / dialogue / narration / ambient sound effect notes / negative prompts, etc.) must be written entirely and fixedly in Chinese; any English words/labels/characters are strictly forbidden (tool names / model names / technical parameter names may retain necessary English). Violations are deemed serious execution errors and must be halted immediately and rewritten.

Before generating videos, ensure that the relevant image assets have been registered as anchors bound to key_element:
1. **Multi-character reference image (element character)**: Default high-quality 2D hand-drawn animation style; for Characters A/B, generate a **four-image horizontally arranged multi-view character reference sheet** respectively — a large half-body close-up on the left, followed rightward by front full-body, side full-body, and back full-body views; pure white background and soft ambient light, used to precisely define face / body shape / hairstyle / clothing / signature props. Register as an anchor.
2. **Animal/spirit character reference image**: If animals / deities / spirits / giant beasts / flying creatures are involved, generate a separate multi-view reference sheet; **the mode of locomotion must be explicitly defined** (flying / hopping / wriggling / crawling / floating / running / rolling) as well as **emotional expression organs** (ears / eyes / tail / tentacles / wings / body glow / fur puffing); bind the anchor.
3. **Scene reference image (element scene)**: Generate a scene reference image featuring true spatial perspective, hand-painted watercolor background, natural plant layering, life details, and architectural functionality; it must include a clear light source direction, weather condition, foreground layer, midground action zone, and distant background; bind the anchor.
4. **Mechanical/aircraft reference image (element prop)**: If machinery is involved, a mechanical structure reference image must be generated, **conforming to the "feasibility" principle** — gears / linkages / propellers / boilers / steam pipes / control levers / wing surfaces positioned with logical self-consistency; **empty-shell machinery with only an outer casing and no motion logic is strictly forbidden**; bind the anchor.

**Multi-shot sliced video generation**: `generate_video_v3` generates the 15s main video (for each shot), passing in the bound character / scene / machinery key_element(s) at the same time (injected via `{{NodeKey}}` placeholders), without using multi-grid storyboard references. The mouth movements of dialogue characters must be aligned with voice timbre and articulation rhythm (if video generation in this environment does not support precise lip-sync binding, honestly degrade to "dialogue rhythm matching the actions"; dialogue character consistency is guaranteed by timbre description + `generate_audio` with identical parameters); child characters retain natural pauses. **Hard constraints on animation texture**: must emphasize 2D hand-drawn texture, soft lines, watercolor background, cel layering, and natural brushstrokes; 3D plastic feel, cheap textures, and overly realistic photographic look are strictly forbidden; character motion must carry a frame-by-frame animation feel. Resolution degradation defaults to smooth downscaling to 720p, and the duration of each video segment is physically locked at 15 seconds.

**Poster cover design specification**: See workflow stage 8 — generate an artistic cover conforming to hand-drawn animated film aesthetics, with the protagonist in a natural or fantasy world, forming a narrative relationship with wind / clouds / forest / waves / aircraft / animal spirits; replicating existing animation characters / film posters / known IP scenes is strictly forbidden; first produce the 16:9 main cover for confirmation, then extend to 3:4 and 4:3.

## VIII. Prompt Writing Specifications (**Written in Chinese**, reverse engineering + lexicon + light-and-shadow fine-tuning) ★

> Top priority: all prompts must be written in Chinese. Narration/dialogue/subtitle/accent content within prompts strictly follows the specification document's output language setting.

### 8.1 Reference Image Reverse Engineering (implicitly read and replicate visual cues before writing)
- Character setting: face shape / eye proportions / hairstyle / clothing silhouette / fabric texture / signature props / character silhouette.
- Scene setting: architectural structure / natural layers / light source direction / weather / plant types / distant mountains / clouds / water surface / life details.
- Machinery setting: gears / linkages / propellers / boilers / steam pipes / cockpit / wing surfaces / metal wear and mode of movement.
- Animal/spirit reference images: body shape / fur / eyes / ears / tail / wings / tentacles / glowing parts / movement trajectory.

### 8.2 Aesthetic Style Adaptive Lexicon (6 styles, auto-mapped by script subject matter / reference images)
- **Hand-drawn 2D animation style**: soft contour lines, watercolor background, cel layering, natural brushstrokes, frame-by-frame animation feel, paper texture, warm colors.
- **Forest healing style**: soft greens, golden sunlight, dappled tree shadows, moist moss, subtly swaying grass blades, natural sense of mystery.
- **Sky flight style**: massive clouds, vast blue sky, aircraft, wind-blown clothing, atmospheric perspective on distant mountains, bright sense of adventure.
- **Wave fairy-tale style**: flat color blocks, simplified lines, rounded waves, foam, childlike colors, soft motion.
- **Steam machinery style**: brass, rust, boilers, gears, steam, oil stains, handcrafted mechanical structures.
- **Spirit-realm fantasy style**: warm yellow lanterns, wooden architecture, water reflections, night scenes, spirits, deities, strange yet rule-governed spaces.
- **Default fallback**: if there is no clear tendency, force the adoption of the high-quality hand-drawn 2D animation style.

### 8.3 Spatial Depth and Layered Animation Description
The prompt must explicitly define a three-layer structure of [Foreground] [Subject] [Background]: foreground elements slightly out of focus or moving quickly, midground characters sharp, background rendered stably in watercolor fashion. Natural micro-motions must be described (wind blowing grass blades / drifting cloud shadows / water surface reflections / swaying leaves / fluttering clothes). **Rendering the background as a static texture is strictly forbidden.**

### 8.4 Character Reference Image Prompt Specification
Pure white background, four sub-images arranged horizontally side by side, from left to right: half-body close-up (face occupying the upper two-thirds of the frame, clear and natural gaze, accurately presenting hairstyle / face shape / eyes / expression), front full-body (head to feet fully in frame, reproducing the front cut of the outfit), side full-body (preserving layers such as the side silhouette of the outfit / backpack / hat / headband / cape), back full-body (back details of the outfit fully visible for consistency in video). Background must be pure white, with no text, no watermark, no extra figures, no complex scenes.

### 8.5 Poster Cover Prompt Specification
Aesthetic core: hand-drawn animated film feel, vast sky, soft natural light, wind-swept grassland, protagonist positioned at the center of the frame or on the rule-of-thirds line, with fantasy architecture / aircraft / forest or sea surface in the distance. Frame mood: warmth, adventure, childhood, hope, awe of nature, slight melancholy ultimately turning toward the light. Typography: may include an original Chinese film title and a simple title design; cluttered text must be avoided. Prohibitions: replicating any existing animation characters / existing IP logos / cluttered layouts / low quality / photographic feel / 3D plastic feel.

### 8.6 Cinematic Light-and-Shadow and Exposure Fine-Tuning (5 rules)
- Natural facial soft light: facial lighting is soft, avoiding overly hard shadows (outdoors may use dappled light through leaves; indoors may use natural window light, warm hearth light, or oil-lamp light).
- Sky and clouds: clouds should have a sense of volume; distant clouds are low-saturation and bluish, while nearby clouds have soft edges.
- Forest light and shadow: sunlight passing through leaves forms shifting light patches; **the light patches must not remain fixed**.
- Water reflections: reflections subtly distort with the ripples, darker and softer in color than the actual objects.
- Machinery light and shadow: brass / sheet metal / oil stains / steam must show material differences; uniform plastic highlights are not allowed.

## IX. 15s Four-Module Prompt Template (Motion Stack, the most core execution asset of this source) ★

When generating 15s video prompts, **the following four-module structure must be strictly and exclusively adopted**. A single output of pure prompt text should be kept within **1500–3000 characters**, so as to fully cover spatial depth, materials, micro details, natural motion, and the transitions between adjacent segments.

```
# [Global Visual and Aesthetic Tone]
- Aesthetic style: [Explicitly state: high-quality hand-drawn 2D animation style, soft contour lines, watercolor background, cel-layered animation texture, full of natural vitality, avoiding 3D plastic feel and photographic realism]
- Camera and depth of field: [e.g.: layered-animation spatial design, foreground grass blades sweeping past quickly, midground characters moving clearly, distant mountains and clouds drifting slowly, conveying depth]
- Color and lighting: [e.g.: forest green and warm yellow sunlight as the dominant palette, soft natural light, dappled light and shadow through leaves, water surface reflections, tiny dust and pollen particles floating in the air]

# [Character and Scene Settings]
- Character assets: Reference the bound key_element image assets via {{NodeKey}} placeholders (e.g., character sheets {{CharA}}, {{CharB}}, etc.), specifying each character's age, expression, clothing, hairstyle, signature props, and action personality.
- Animal/Spirit assets: Reference {{Spirit}} etc., specifying the animal's or spirit's body size, fur, eyes, ears, tail, wings, mode of movement, and emotional expression.
- Scene assets: Reference the scene concept art {{Scene}}, clarifying the spatial structure of the forest/town/cabin/aircraft/sea surface/sky or fantasy architecture.
- Mechanical assets: If machinery is present, reference {{Prop}}, clarifying the motion logic of gears/propellers/boilers/steam pipes/control levers.

# 【Script and Action Timeline (Motion Stack)】
Each time slice strictly follows the motion description stack: Camera (camera movement) → Subject (subject actions and facial muscles) → Space (space/wind/water/mechanical resistance) → Audio (physical foley/dialogue):
- [00.0s - 03.5s]
  - Camera: [e.g.: low-angle child's-eye view, medium shot, looking toward the protagonist through foreground blades of grass. Visual state ledger inheritance: must precisely inherit the character position, posture, prop state, weather, wind direction, and lighting from the end of the previous segment]
  - Subject: [e.g.: the girl Character A stands in the middle of the forest path, arms tightly hugging an old canvas bag, eyes wide open, breathing slightly rapid, hair and clothes gently lifted by the breeze, soles stepping on and bending the damp blades of grass]
  - Space: [e.g.: wind blows from left to right, a few out-of-focus foreground blades of grass swaying left and right; in the distance, a giant camphor tree and blue-green faraway mountains; cloud shadows slowly sweep across the forest, sunlight scattering dappled flecks of light]
  - Audio: [write only physical sound effects and dialogue: wind rustling through the grass <grass blades rubbing>. Dialogue must follow the spec sheet settings; do not include background music descriptions]
- [03.5s - 07.5s]
  - Camera: [Auto cut: close-up of the face, slight hand-drawn animation-style push-in]
  - Subject: [e.g.: Character A slowly lifts her head, gaze shifting from fear to curiosity, eyebrows rising slightly, lips parting a little, a faint blush on her cheeks, the faint glow ahead reflected in her eyes]
  - Space: [tree shadows and patches of light drift gently beside her face, a warm glow suffusing the air]
  - Audio: [e.g.: she inhales softly <deep inhale sound>, the rustle of leaves becoming clearer. Dialogue: {Character A: "You... are you waiting for the wind too?"}, bound to Character A's voice timbre]
- [07.5s - 12.0s]
  - Camera: [Auto cut: over-the-shoulder medium shot, focus shifting from Character A's shoulder to the animal/spirit ahead]
  - Subject: [e.g.: a fluffy little spirit pokes its head out from behind a decaying log, ears perking up first, round eyes blinking twice, nose tip gently sniffing the air, tail slowly puffing up out of alertness]
  - Space: [e.g.: the moss on the decaying log glows faintly, a few water droplets slide down the leaves, Character A's shoulder and the edge of her hair ribbon sway in the wind, out of focus]
  - Audio: [e.g.: the little spirit emits a low <little spirit low whimper>, a soft patter of droplets landing on leaves. Dialogue: {Character B: "Don't scare it; it understands the sound of the wind."}, bound to Character B's voice timbre]
- [12.0s - 15.0s]
  - Camera: [Auto cut: lateral tracking shot, establishing the state anchor for the next segment]
  - Subject: [e.g.: Character A finally takes a step, carefully extending her right hand, palm up, stopping in front of the little spirit; the spirit does not flee, but gently draws close to her fingertips. Character A's tense expression gradually eases]
  - Space: [e.g.: in the distance the clouds crack open to let through a shaft of golden sunlight, illuminating the end of the path; wind blows from left to right and the trees sway. At this moment, the extended right hand, the spirit drawing close to her fingertips, the left-to-right wind, and the strengthening sunlight will serve as the state anchor at the start of the next segment]
  - Audio: [e.g.: the wind briefly softens <soft wind sound>, the <faint friction sound> of the little spirit gently nuzzling her fingers]

# 【Generation Constraints and Negative Prompts】
- Absolutely forbidden: generating any form of background music, melody, or rhythm track. No interface parameter descriptions regarding resolution, frame rate, or aspect ratio. No inverse-joint twisting, teleportation, or zero-gravity floating of characters. No 3D plastic texture, cheap cartoon decals, photorealistic style, or live-action skin texture. No replication of any existing animated characters, existing film scenes, or established IP logos. No backgrounds frozen like static decals, no natural elements completely motionless, no illogical mechanical motion.
```

## 10. Voice and Sound-Effect Wrappers and the Common-Sense Firewall ★

1. **Ambient and physical sound effects**: Wrap in `<...>`, describing physical attributes in detail (grass blades rubbing/creaking wooden door/steam jetting/propeller spinning/water droplet spreading/fabric rustling), mapped to audio_layer (type sfx). Descriptions such as "background music" or "melody" are strictly forbidden.
2. **Multi-character dialogue (dialogue)**: Wrap in `{Character name: "dialogue text"}`; dialogue must be in the output language specified by the spec sheet, and every speaking character's dialogue must be bound to their corresponding voice timbre. Children's dialogue must be natural, concise, and sincere.
3. **Animal/spirit sounds**: You may use `{Little spirit: "Gurgle..."}` or `<the little spirit lets out a soft, low hum>`, which must match its body size and emotion.
4. **On-screen text**: Wrap in `【...】`. Unless the user explicitly requests it, no subtitles are generated in the video.
5. **Behavioral common-sense firewall**: All actions must conform to common sense regarding gravity, inertia, friction, wind resistance, buoyancy, mechanical transmission, etc. — **aircraft turns must include banking, sudden stops while running must show inertia, and clothing movement must lag behind body motion**.
6. **Negative constraint suffix**: Every video description segment must end with: no subtitles, no music, no text, no logos, no watermarks.

## 11. Pure Instrumental BGM Prompts and Instrument Library (for `generate_audio`)

1. **Genre and emotional positioning**: Core tone = warm, clear, adventurous, childhood, nature, hope, slightly melancholic but ultimately turning toward the light; suitable for growing up, flight, forest, ocean waves, fantasy journeys, and emotional reconciliation. **Do not include the names of any well-known musicians, singers, bands, or existing works.**
2. **9-type emotion mapping of the instrument library**:
   - Piano = childhood, solitude, innocence, and inner growth.
   - String ensemble = flight, hope, epic feel, and emotional elevation.
   - Flute/oboe/clarinet = nature, forest, wind, spirits, and lightness.
   - French horn = sky, the distant, adventure, flight, and grandeur.
   - Harp = water surface, magic, dreams, mysterious glimmer.
   - Glockenspiel/music box = fairy tale, childhood, gateway to fantasy.
   - Accordion = small town, marketplace, travel, European flavor.
   - Light percussion = running, mechanical rhythm, advancing adventure.
3. **Music direction selected by plot** (Stage 6): forest healing = piano + flute + string underlay; flight adventure = French horn + string ensemble + rising woodwind melody; ocean-wave fairy tale = harp + celesta + gentle woodwinds; steam machinery = low strings + accordion + light percussion; shadow of war = deep brass + cello + sparse drumbeats.
4. **Recommended prompt structure**: `Pure instrumental, warm animated film theme, clear piano, soft string ensemble, flute melody, French horn conveying a sense of flight, harp dotting the water's faint glimmer, bright but not overly sentimental, suitable for the coming-of-age adventures of young boys and girls, warm and natural recording texture.`

## 12. Final Footage Quality Check (`composite_video`, 7 items) ★

1. **Seamless timeline splicing and narrative continuity check**: Splice the timeline with each 15s shot as the basic unit; review the whole from the viewer's perspective, checking that the plot flows smoothly / dialogue is natural / the growth arc is clear / there are no logical discontinuities; **strictly verify the visual state ledger** (character positions/postures/clothing/props/animal-spirit positions/mechanical states/weather/wind direction/lighting direction must match perfectly); if goofs / vanishing props / character teleportation / sudden weather changes / mechanical motion logic errors are found, **the corresponding segments must be precisely identified and sent back for re-production**.
2. **Multi-shot rhythm control**: Check that transitions at each auto-cut point within every shot must be natural; stiff long-axis videos without cuts, resembling a PPT or static illustrations, are strictly forbidden; when dialogue appears, camera focus or shot-size changes must sync with the speaker; natural observation shots / action-advancing shots / emotional close-ups should form a breathing rhythm, rather than stacking spectacles at high intensity from start to finish.
3. **Hand-drawn animation texture QC**: Check each shot for soft outlines / watercolor backgrounds / cel layering / natural brushstrokes / frame-by-frame animation feel; any occurrence of 3D plastic texture / live-action photo feel / cheap decal feel / static background patch feel must be sent back for rework; **characters must maintain consistent silhouettes**, with no major drift in face shape / hairstyle / clothing structure across different segments.
4. **Natural and mechanical motion QC**: Check whether wind / water / grass / leaves / cloud layers / smoke / steam have subtle motion; check whether aircraft / boilers / gears / propellers / linkages conform to physical laws; flying shots must convey air resistance / inertia / banking / depth layering, and must not look like a character decal sliding across the background.
5. **Action and expression quality control**: Characters must have normal physical mass, inertial motion, and coherent, vivid muscular micro-expressions; child or young girl characters must show genuine emotional reactions (fear / surprise / hesitation / mustering courage / joy / dejection); animals or spirits must have non-human bodily expression and cannot merely stand like dolls; **characters must not constantly stand frozen or always face the camera**—their actions must match the script's motivations.
6. **Multi-track sound assembly and foley rendering**: Dialogue and sound effects embedded in the video track are losslessly extracted and placed separately on the timeline; import the planned independent audio_layers (sfx track: wind / leaves / birdsong / water / footsteps / machinery / animal sounds; music/bgm track; narration track); precisely fine-tune each track's volume, fades, and beat-sync alignment with the shot timeline—**music is forbidden from covering character dialogue**.
7. **Transition and final output management**: Within multi-shot slices, use natural hard cuts; between 15s segments, cinematic transitions such as action-match cuts, wind-blown occlusion, passing cloud layers, doors opening/closing, flying through clouds, or grass blades sweeping across the lens may be used; **modern short-video fancy text, flash-to-white, and physically implausible show-off transitions are strictly forbidden**. Final outputs: the complete serialized video file, internal shot slice list, visual state ledger, physical sound-effect alignment nodes, and audio track layer assignment list.

## Related

- **Boundaries (do not use this skill; reroute instead)**: generic 2D animation workflow → cartoon-flow; other animation styles → needle-felt-animation / ink-wuxia-animation / mahou-shoujo-90s; famous-director live-action styles → auteur-style-director.
- This skill is self-contained and inline, **has no native cross-skill dependencies, and sets no collaboration table**.