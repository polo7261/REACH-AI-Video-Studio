---
name: cinematic-vfx-creator
description: "Cinematic fight VFX skill: generate character film VFX from one sentence; supports text, reference images, or video"
---

# Character Battle Scene Effects Video Generation

## Core Methodology

### 1. Narrative-Driven Storyboard Architecture

A storyboard is a **temporal narrative structure within a single video**, not a collection of multiple independent video files. Each storyboard segment is a time span serving the overall story arc:

- **SB-01 Establishing Shot**: 0-25% of duration → Scene/atmosphere establishment
- **SB-02 Conflict Build-up**: 25-50% of duration → Character reveal, energy accumulation
- **SB-03 Climactic Clash**: 50-75% of duration → Core battle sequence, dense special effects
- **SB-04 Finale Frame**: 75-100% of duration → Ultimate move, environmental destruction, hero freeze-frame

Each storyboard segment must:

1. **Advance narrative momentum** (no static repetition)
2. **Escalate visual intensity** (effects complexity increases shot by shot)
3. **Maintain spatial/character continuity** (camera angles and positions follow cinematic logic)

---

### 2. Elemental Color Semantics System

Skill effects must be bound to explicit color-attribute mappings; different elemental types follow fixed visual languages:

Element Attribute Core Color Emotion Keywords Particle Form Fire Blazing Red/Orange Gold/Incandescent White Fervent, Explosive, Mighty Flame clusters, explosion halos, heat wave distortion Ice Ice Blue/Cyan White/Frost White Frigid, Condensing, Sharp Ice crystal refraction, frost flower diffusion, cold mist permeation Lightning Black Purple/Deep Blue/White Electricity Swift, Violent, Tearing Root-shaped arcs, static particles, lightning flash chains Shadow Purple Black/Dark Red/Blood Eerie, Devouring, Oppressive Churning black mist, blood-colored smoke, shadow tendrils Divine Gold White/Pale Cyan/Holy Light Dazzling, Sacred, Purifying Drifting light feathers, holy light pillars, volumetric light diffusion Nature Emerald Green/Wood Brown/Golden Yellow Vital, Spreading, Entangling Entangling vines, swirling leaves, pollen light motes

**Application Rules**:

- Skill colors must form either **high contrast** or **high fusion** with the character's costume/weapon — choose one
- A single skill may use at most 2 dominant colors to avoid color chaos
- Scene environment tones should counterbalance the skill colors (ice skills paired with dark-toned scenes, fire skills paired with cool-gray scenes)
- Once colors are set, they must remain consistent throughout; no mid-way changes

---

### 3. Character Combat Type Analysis

Upon receiving character input, perform **combat character classification**:

- **Agile Type**: Chain weapons, acrobatic moves → Focus: motion trajectories, afterimages, speed lines
- **Power Type**: Heavy armor, ground-shaking strikes → Focus: impact craters, shockwave ripples, flying debris
- **Spellcaster Type**: Energy constructs, summoning rituals → Focus: particle density, glow intensity, volumetric light

**Cross-Type Interaction Rules**:

- Agile vs Power → Speed lines colliding with shockwaves
- Spellcaster vs Agile → Spell barrages vs dodge afterimages
- Power vs Spellcaster → Physical strikes shattering energy barriers

---

### 4. Four-Layer Prompt Construction System

Every battle video prompt must contain four layers — none may be omitted:

**① Style Quality Declaration Layer** (10-15% of length)\
Defines rendering standards, overall style, and color/mood tone.\
3D Chinese anime fantasy style + Unreal Engine 5 ultimate image quality + \[Tone: dark/bright/cold\] + Cinematic \[Texture words: realistic/epic/dreamlike\] Must include: rendering engine name, tone descriptor, texture descriptor, contrast description Example: "Next-gen Chinese anime 3D, Unreal Engine 5 rendering, dark epic style, cool-toned premium texture, global illumination + motion blur + depth of field, 60fps smoothness"

**② Camera Movement System Layer** (15-20% of length)\
Defines camera movement logic, cutting rhythm, and viewpoint change patterns.\
Storyboard rhythm formula: \[Build-up segment (steady slow push-in)\] → \[Burst segment (fast cutting)\] → \[Afterglow segment (slow pull-out)\] Camera movement grammar: push in / pull out / follow / orbit / low angle / high angle Cut intensity: slow dissolve (fade in/out) vs fast jump cut (hard cut) vs flash-white burst cut Example: "Opening extreme close-up slowly pushing in to a full-body shot, low-angle tracking during the build-up segment, fast jump cut to a frontal collision close-up at the burst moment, slow pull-out and freeze from a high angle in the finale"

**③ Core Imagery Layer** (50-60% of length, most critical)\
Adopts **micro-progressive temporal narration** — breaking actions down into continuous frame descriptions at 0.5-1 second granularity.

Core principles:

- **Verb Density Rule**: Every action must use strong verbs (thundering/bursting/exploding/sweeping/breaking through); reject weak verbs (appearing/showing/occurring)
- **Sensory Stacking Rule**: Visual + auditory + motion described simultaneously ("deafening roar + shockwave bursting violently + ground cracking and spreading")
- **Scale Contrast Rule**: Create oppressive feel through size contrast ("tiny human silhouette vs giant energy sphere")
- **VFX Binding Rule**: Effects must be attached to actions ("fangs **erupt** with purple flames" rather than "purple flames appear")

Temporal breakdown template:\
\[Initial state\] → \[Trigger action\] → \[Environmental response\] → \[Effect cascade\] → \[Climax beat\] → \[Resolution pose\]

Example (0.5s granularity): 0.0-0.5s: Character assumes a casting pose, hands forming seals 0.5-1.0s: Palms begin to glow, eyes shooting out elemental radiance 1.0-2.0s: Ground rune array activates in sequence (spiraling outward) 2.0-3.0s: Energy pillar rises thunderously from the rune center 3.0-4.0s: Skill form condenses and takes shape within the energy pillar 4.0-5.0s: Skill bursts out, energy pillar exploding into particles

**④ Technical Detail Enhancement Layer** (10-15% of length)\
Maximize realism with material, particle, and physics feedback details.\
Particle details: ice crystals refracting light / spark-spray trajectories / volumetric churning smoke / static wisps entwining Material details: mirror-like reflective ice surface / metal scratches and rust / fluttering fabric folds / skin pore texture Physics feedback: ground cracking / debris flying / heat waves warping the air / shockwave ripples expanding Atmospheric oppression: congealed-air feel / volumetric light with suspended dust / low-frequency humming vibration

---

### 5. Professional Animation Impact Frame Techniques (Visualizable Description System)

Traditional numeric instructions (e.g., "brightness 246/255") cannot be precisely executed by AI models and must be converted into **visualizable descriptions of actions occurring within the frame**.

**Flash-White Frame (White-Screen Burst Flash) — Scene Burst-Point Transition**Use: Energy burst moment / Charge-to-clash / Ultimate move release\
Basic version: "The frame flash-bursts to pure white, blinding like a lightning strike, then instantly cuts back to the battle scene" Enhanced version: "Full-screen white light instantly swallows the frame, a shockwave ring expanding rapidly outward from the center, kicking up sky-filling dust and debris; as the glare fades, the scene cuts in abruptly" Screen-shake version: "At the instant of explosion the frame flashes white, the camera shakes violently, amplitude going from large to small, slowly returning to stability after 0.3 seconds"

**Black-and-White Frame (Desaturated Frame) — Build-up and Afterglow**Use: Oppressive skill charge-up / Kill-shot freeze afterglow / Calm before the storm\
Desaturated charge: "The frame's colors drain away abruptly as if ink-washed, leaving only light and dark silhouettes; elemental arcs appear exceptionally sharp in the black-and-white frame" Kill-shot freeze: "At the instant of the slash the frame freezes into a black-and-white slow shot, debris and dust suspended in mid-air as if time has stopped, with only a faint glimmer lingering in the character's eyes" Gradual desaturation: "The frame's colors ebb away slowly like a receding tide, the world gradually fading into cold gray black-and-white, the dead-silent oppressive stillness before the storm pervading"

**Impact Frame (Sudden Frame Shift) — Collision and Energy Burst**Use: Bone-crunching collisions / Energy sphere explosions / Weapon clashes\
Single impact: "At the instant two forces collide, a dazzling white light bursts out; a shockwave ring explodes and spreads outward, the ground cracks, and dust flies everywhere" Secondary energy burst: "Energy compresses to its limit at the collision point and erupts thunderously a second time; strong lens distortion appears at the frame's edges, sparks scattering like rain" High-frequency rapid strikes: "Every strike lands with a violent jolt of the frame, flashes and blasts surging one after another, the rhythm pounding like densely beaten war drums"
**Screen-Shake Effect Tiers**Light shake: the camera trembles slightly, like the aftershock of a distant explosion, recovering naturally after 0.2 seconds Medium shake: the camera shakes violently at the instant of the explosion, amplitude large first then small, slowly stabilizing after 0.3 seconds Heavy shake: the shockwave hits head-on, the camera convulses like an earthquake, motion blur appears at the frame edges, gradually recovering within 0.5 seconds Extreme shake: the ultimate move erupts, the camera shakes to its limit, the frame briefly defocuses + edge distortion, the shaking lasts 0.8 seconds then slowly subsides like an aftershock

**Complete Impact Rhythm Template (Directly Reusable**)Charging phase: the frame's colors recede slowly like a tide, fading into cold gray-black-white, the world sinking into dead silence and oppression; Eruption point: a full-screen blaze of white light instantly swallows the frame, the shockwave spreads outward from the center as a high-speed ring, kicking up dust and rubble across the sky, and the camera shakes violently, large first then small, for 0.3 seconds; Consecutive impacts: with each strike landing, the frame jolts violently, bursting with dazzling white light and shockwave ripples, energy erupting a second time at the point of impact, lens distortion + sparks flying everywhere, the rhythm as dense as war drums; Afterglow freeze-frame: after the slash, the frame freezes into a black-and-white slow-motion shot, rubble suspended as if time has stopped, colors slowly surging back like a tide, residual particles drifting away and vanishing in the volumetric light.

---

## Workflow

### Step 1: Preparation Phase (Step 2 May Be Entered Only After Everything Is Complete)

**Requirement Mining Upfront Interaction Mechanism (Mandatory, First Step of the Preparation Phase):**

After the user activates the Skill, the first thing to do is not to collect parameters directly, but to first, through professional questioning\
uncover the user's true creative intent. Users are often unable to accurately describe the effect style they want, so the Agent\
must use professional knowledge to guide the user's expression.

Trigger conditions:

- The user's description is vague (e.g., "two women fighting, very flashy")
- The user only mentioned the character/scene, not the effect style
- The user has no clear skill/move concept
- The user's statement lacks key information such as style, elements, rhythm, etc.

Prohibited behaviors:

- Directly applying default templates to generate after receiving a vague requirement ❌
- Jumping straight into the parameter collection checklist without guidance ❌
- Filling all requirements with the same cookie-cutter "fantasy 3D epic style" ❌

Correct execution procedure:

STEP 1 — Style-targeting questions (single ask_human, multiple dimensions)

Based on the user's needs, choose the 3-4 most relevant questions from the following dimensions:

【Art Style Dimension】

- Realistic-leaning (live-action texture / hyper-realistic modeling) or anime-leaning (donghua / Japanese anime / 3D cartoon)?
- Color tone leaning dark and oppressive, or bright and gorgeous?

【Special Effect Style Dimension】

- Are there any favorite game/anime skill references?\
  (e.g., Demon Slayer's Breathing Styles, Naruto's chakra jutsu, Genshin Impact's Elemental Bursts,\
  Honkai's finisher skills, Honor of Kings' ultimate effects, etc.)
- Which element attribute do you lean toward?\
  (fire/ice/lightning/shadow/holy/nature/yin-yang/mechanical/blood, etc.)
- Does the effect style lean toward 「expressive and graceful」 (e.g., xianxia ribbon-and-sword-qi) or 「hardcore explosion」\
  (e.g., shockwaves blasting the ground apart)?

【Action Style Dimension】

- Which combat rhythm do you prefer?\
  (fast, fierce combos / charged one-strike kill / elegant flowing dance style / savage\*\* suppression)
- Which combat style does the character lean toward?\
  (swordsman/assassin/mage/martial artist/summoner/gunner)

【Narrative Rhythm Dimension】

- Do you want a complete sense of story (establishment → charging → eruption → resolution)\
  or jump straight into a climactic effect showcase?
- Is there a specific scene or shot feel you would like to replicate?\
  (e.g., a particular scene from a certain movie/anime)

STEP 2 — Integrate the user's answers to generate a personalized creative plan

Based on the user's answers, the Agent needs to:

1. Convert the user's description into a concrete visual plan using professional language
2. Proactively propose 1-2 creative suggestions (extended from the user's preferences)
3. Explain to the user the effects that will be presented, for example:

Sample reply:\
"Based on your preferences, I have designed the following plan for you:

- Style: Chinese donghua 3D realism, dark-gold color tone
- Skill effects: referencing Genshin Impact's Electro Elemental Burst style, purple-gold lightning + shockwave ripples
- Combat rhythm: fast, fierce combos with afterimages on each strike, finishing blow as a charged eruption
- Narrative structure: establish the standoff → combo scuffle → finishing ultimate → heroic freeze-frame\
  What do you think of this direction? Anything you would like adjusted?"

STEP 3 — After the user confirms the creative direction, proceed to preparation phase parameter collection

Only after the user is satisfied with the creative direction do we move on to the 6-item parameter collection checklist.

Notes:

- Each round of questions should focus on 3-4 dimensions; do not throw out all questions at once
- Guide with concrete reference examples (game skill names/anime move names),\
  rather than the abstract "what style do you want"
- The Agent should proactively offer options and suggestions to lower the user's expression barrier
- Adjust the direction of subsequent questions in real time based on each of the user's answers,\
  rather than mechanically running through all questions
- The final generated script must reflect the user's personalized preferences,\
  applying generic templates is prohibited

🔴 Phase Advancement Gate (Mandatory Blocking Rule)

The following items must **all be explicitly answered by the user** before proceeding to Step 2 storyboard design:

#Checklist Item Description1 Character Asset Reference image uploaded OR AI-generated three-view sheet confirmed by the user2 Aspect Ratio 1:1 / 16:9 / 9:163 Resolution 480p / 720p / 1080p4 Scene Preference User-specified description OR left to AI design5 Video Duration 10s / 15s / 20s / 30s / 60s6 Effect Intensity Light / Medium / Extreme

**Prohibited behaviors**:

- Proceeding directly to generation after the resolution is confirmed ❌
- Treating implicit information in the requirement description as confirmed ❌
- For any item not explicitly answered by the user, inferring a substitute is prohibited; it must be completed via ask_human ❌

🔴 Character Asset Handling Rules (Mandatory)

IF the user provided a character reference image: → Use the reference image directly as the character anchor, perform character analysis, and continue collecting the remaining 4 items

IF the user has no reference image (including answers such as "no reference image"/"let the AI design freely"): → Do not skip the character asset step → Must first use generate_image to generate a character three-view sheet (front/side/back) → Show the three views to the user and confirm via ask_human whether the appearance is satisfactory → After the user explicitly confirms, use the confirmed image as the character anchor → Proceeding directly to video generation based solely on a text description is prohibited

Character Analysis Dimensions (execute after receiving/confirming the character image)

- Outfit color scheme and materials (fabric/metal/leather)
- Weapon type and grip style (sword/spear/chain/gauntlets)
- Temperament positioning (cold/alluring/mighty/mysterious)
- Combat style classification (agile type / power type / spell type)
- Visually iconic elements (e.g., "red iron chains" / "yellow heavy armor")

Scene Design Decision Tree

IF the user provided a scene description: → Extract: location type, time, weather, ambient light → Identify: interactive elements (destructible props, dynamic environment)

IF the user delegates the design to the AI: → Choose based on the character conflict type: Spell duel → ancient ruins, moonlit night, energy fissures Martial arts duel → courtyard, rainy night, stone pillars Monster battle → wasteland, storm, collapsing structures → Design principle: the environment must participate in the action (not just a backdrop)

Skill Design Checklist

- \[ \] Element attribute determined (chosen from the color semantics system)

- \[ \] Skill name and core action (e.g., "Heavenly Fierce Tiger Fist" = a single punch impact)

- \[ \] Effect priority ordering (e.g., fire = shockwave &gt; fireball &gt; heat-haze distortion)

- \[ \] Environmental feedback design (ground fissuring/ice spreading/wind-blade slash marks)

- **Character Reference Image Quality Assessment Rules (Mandatory):**

  Whether the user provided a reference image or the AI generated a three-view sheet, the following quality assessment must be performed:

  Assessment dimensions:

  - \[ \] Image clarity: whether there is blurriness, compression artifacts, or screenshot noise
  - \[ \] Detail completeness: whether clothing textures, weapon details, and facial features are clearly discernible
  - \[ \] View completeness: whether it includes all three views — front/side/back
  - \[ \] Size sufficiency: whether the character is large enough and details are visible

  IF the reference image quality is insufficient (blurry/screenshot/missing details/incomplete views):\
  → Do not use a low-quality image directly as the sole anchor\
→ Using the user-provided image as a reference, regenerate via generate_image\
  a high-quality, multi-angle, fully detailed character three-view sheet\
  → Present the newly generated refined three-view sheet to the user for confirmation\
  → After the user confirms, adopt the refined three-view sheet as the official character anchor\
  → All subsequent video generations must reference the refined three-view sheet node as reference_nodes\
  → Directly generating video from the original low-quality image is prohibited

  IF the reference image is of good quality (clear / detail-rich / multi-angle):\
  → Use it directly as the character anchor, no additional generation needed\
  → All subsequent video generations reference this image as reference_nodes

**Anchor Version Management Rules:**

- Always use the "most refined version" of the multi-view sheet as the reference anchor for all subsequent videos
- If a more refined version is generated along the way, all subsequent video nodes must switch to referencing the new version
- Clearly mark the currently used character anchor node_key in the storyboard table and the anchor checklist

---

### Step 2: Storyboard Design Phase

**Core Principle**: Storyboard segments are time divisions within a single video, not a splice of multiple independent videos. One generation call produces a single video containing the complete storyboard sequence.

**Standard Storyboard Structure**:

Storyboard Duration Share Shot Type Narrative Function SB-01 Setup First 20% Environmental wide shot → character close-up Scene atmosphere establishment + character introduction SB-02 Charge-Up 20-45% Medium shot push-in / orbit Skill preparation, energy gathering, tension building SB-03 Burst 45-80% Fast jump cuts + close-ups Skill release, dense impact frames, climax segment SB-04 Finish Final 20% Pull back to overhead → freeze frame Aftershock spreading, hero's back view, sense of closure

**Each storyboard segment must define**:

- Time range: \[start\]s - \[end\]s
- Camera movement: static / dolly / crane / orbit / handheld
- Character action: a specific pose/attack described with verb phrases
- Environmental reaction: what is shattering/moving/glowing?
- VFX keywords: 3-5 specific VFX descriptors

**Advanced Techniques**:

- Multi-character battle scenes must insert enemy shots (establish → confrontation → clash → slay)
- Each storyboard segment must include a clear "action completion point"

**Multi-Character Shot Perspective Switching Logic**:\
Protagonist perspective segment: tracking shot following the protagonist's attacks, with the enemy appearing only as an attack target at the edge of the frame Enemy perspective segment: switch to the enemy's front, showing their defensive/counterattack moves Collision perspective segment: third-person overhead shot showing the full panorama of both sides' energy colliding Finish perspective segment: return to the protagonist's back view as the enemy falls or dissipates

**Storyboard Script User Confirmation Mechanism (Mandatory):**

After storyboard planning is complete, the complete storyboard plan must be presented to the user and confirmed via ask_human:

The presentation includes:

- Time range, shot type, action content, and VFX keywords of each storyboard segment
- Character color system and elemental attribute explanation
- Scene design plan

Confirmation interaction rules:\
IF the user is satisfied:\
→ Proceed to Step 3, the prompt writing phase

IF the user is dissatisfied / requests revisions:\
→ The Agent revises the corresponding storyboard content according to the user's feedback\
→ Present the revised storyboard plan again\
→ Confirm again via ask_human\
→ Loop until the user explicitly expresses satisfaction\
→ Proceeding to the prompt writing phase without user confirmation is prohibited

Revision directions the user may propose at this stage include:

- Adjusting the action design of a specific storyboard segment
- Adding/removing VFX types or adjusting their intensity
- Modifying scene details
- Adjusting narrative pacing (speeding up / slowing down a certain segment)
- Replacing the character's action style

---

### Step 3: Prompt Writing Phase

Build according to the four-layer system, strictly adhering to the length allocation:

1. **Style Quality Layer** (10%): rendering engine + color tone + texture
2. **Camera System Layer** (15%): camera movement + cutting rhythm + perspective
3. **Core Visual Layer** (60%): micro-progressive timeline breakdown at 0.5-1 second granularity
4. **Technical Detail Layer** (15%): particles + materials + physical feedback + atmosphere

**Impact Frame Insertion Timing (Required)**:

- The charge-up segment must include a black-and-white gradient
- The instant of skill burst must include 1 white flash frame
- Every collision in the clash segment must include impact frame descriptions
- The finish segment must include a black-and-white freeze frame + color flooding back

**Prompt Length**: keep within 800-1500 words

---

### Step 4: Generation and Acceptance Phase

**Generation Rules**:

- Use the **Seedance 2.0** model
- One call produces the complete video, containing all storyboard timings
- Splitting into multiple nodes and then splicing is prohibited

**Quality Acceptance Checklist**:

- \[ \] Does the skill color scheme conform to the elemental semantic system
- \[ \] Is the character's outfit/weapon consistent with the confirmed reference image
- \[ \] Does it contain at least 1 white flash frame burst moment
- \[ \] Does it contain 1 black-and-white frame sequence
- \[ \] Is the camera movement smooth (no jarring jumps)
- \[ \] Is the VFX density up to standard (particles/shockwaves/environmental destruction)

**Iteration Strategy When Dissatisfied**:

- Skill not flashy enough → increase impact frame description density, strengthen screen shake effects
- Pacing drags → compress the charge-up segment duration, increase jump-cut frequency in the burst segment
- Visuals too dim → add "high-contrast light and shadow" to the style layer, enhance glowing particles in the skill layer
- Character deformation → add appearance-lock descriptions to the core visual layer ("silver hair / red outfit / iron-chain weapon maintained throughout")

---

## Key Constraints and Standards (Mandatory Rules Summary)

Rule Type Content Preparation Phase Gate 🔴 Mandatory Blocking Storyboard design may begin only after all 5 items are explicitly confirmed by the user Character Asset Rule 🔴 Mandatory Blocking No reference image: must first generate the three-view sheet and obtain user confirmation Resolution Inquiry 🔴 Mandatory Blocking Must ask before generating any video; assumptions not allowed Storyboard Understanding 🔴 Mandatory Storyboard segments are time divisions within a video; splitting into multiple video nodes and splicing is prohibited Single Generation 🔴 Mandatory One call produces the complete video, no splitting Color-Attribute Binding 🟡 Quality Standard Skill VFX colors strictly follow the elemental color semantic system Impact Frame Requirement 🟡 Quality Standard At least 1 white flash frame + 1 black-and-white frame + 2-4 impact frames Verb Intensity 🟡 Literary Standard Weak verbs banned; strong verbs required VFX Attachment 🟡 Technical Standard VFX must attach to the action subject and must not exist independently Timing Granularity 🟡 Narrative Standard The core visual layer must be broken down at 0.5-1 second granularity in micro-progression

---

## Advanced Techniques

### Enhanced Environmental Interaction

VFX in high-quality battle videos should not "float" above the scene, but should engage in real physical interaction with the environment:

- Fire skills: ignite the dry grass on the ground, set wooden wreckage alight, heat-haze distortion in the air
- Frost skills: ice spreading across the ground, stone pillars freezing over and bursting apart, white mist condensing in the air
- Lightning skills: piercing the ground and leaving charred marks, metal weapons discharging in reverse
- Shockwaves: whipping up dust from the ground, blasting away rubble, shattering crumbling walls

### Symbolic Prop Design

Every scene prop should serve a **dual function**: spatial element + symbolic meaning:

- Ancient stone gate → represents the realm barrier (opening = releasing power)
- Collapsing stone pillar → visualizes battle intensity (degree of destruction = magnitude of power)
- Weather changes → reflect the charac\*\* emo\*\*ional state (calm → storm = accumulating rage)

### Golden Timing for Slow Motion

Inserting 0.5x-speed slow motion at the following 3 moments can significantly boost visual impact:

1. The instant of skill burst (the 0.3 seconds as the energy orb leaves the hand)
2. The instant of weapon clash (the 0.2 seconds when blades collide and sparks burst forth)
3. The killing-blow freeze instant (the final frame before the enemy falls, stretched to 0.5 seconds)

Slow-motion description template:\
"At the moment of \[key action\], the flow of time abruptly slows and the frame enters 0.5x-speed slow motion, \[magnified detail description\]; after the slow motion ends, the flow of time returns to normal"

### Finish Freeze-Frame Hero Composition

The final 1-2 seconds of the video must deliver a **hero composition**:

- The character in a dominant position (elevated, centered, backlit)
- Environmental destruction as the compositional frame (smoke dispersing, rubble settling)
- Victory totems (weapon raised high, energy dissipating, aftershocks spreading)
- This frame must be a screenshot-grade image

---

## Complete Example
**User Input**:

- Character: Red-clad heroine, chain weapon (reference image confirmed)
- Opponent: Yellow-armored heavy warrior (reference image confirmed)
- Scene: AI-designed
- Resolution: 16:9
- Duration: 15s
- VFX intensity: Extreme

**Storyboard Planning**:\
SB-01 (0-3s): Night view of ancient temple ruins, blue energy fissures running through the ground, moonlight filtering through the damaged roof SB-02 (3-7s): The two sides face off, red vs. golden energy auras colliding, ground cracks spreading outward on both sides SB-03 (7-12s): The chain swings out wreathed in red lightning, the heavy-armored warrior blasts out a golden shockwave, the two energies collide and explode SB-04 (12-15s): Ultimate moves collide, energy pillars soar skyward, temple pillars crash down thunderously, both sides freeze back-to-back

**Generation Prompt**:\
3D Chinese anime wuxia style, epic action-blockbuster texture, Unreal Engine 5 ultimate image quality, dark epic tone, red-gold dual-color energy contrast, off-the-charts visual tension, motion blur + depth of field, smooth 60fps.

Fluid and varied camera movement, wide-angle establishing shot switching to dynamic close-ups, low-angle orbit tracking during the charge-up phase, rapid jump cut to a frontal-collision close-up at the burst moment, overhead shot slowly pulling back and freezing at the finale, extremely strong cinematic narrative feel.

0-3s: Moonlit night over ancient temple ruins, blue energy fissures spreading in all directions across the ground, broken stone pillars standing tall, moonlight piercing through the ruined roof casting cold light; the frame's colors slowly recede like an ebbing tide into cold gray-black-and-white, a deathly oppressive stillness pervades; 3-7s: The red-clad heroine and the yellow-armored warrior face off from afar, energy auras abruptly bursting forth around both, the red and golden auras colliding violently between them, ground fissures spreading outward from the collision point, debris splattering; 7-12s: The heroine swings the chain, its body wreathed in red lightning lashing out through the air, the warrior raises an arm to block and throws a heavy punch blasting out a golden shockwave; the two energies collide mid-air, a full-screen burst of white light instantly swallows the frame, the shockwave bursts outward in a ring, the camera shakes violently—large tremors first, then smaller—lasting 0.3 seconds; the energy erupts a second time at the collision point, strong

Continue generating

Continuing from the preceding text:

intense lens distortion at the frame edges, every strike lands with a violent jolt of the frame bursting out dazzling white light, the rhythm dense as war drums;\
12-15s: Both sides simultaneously charge up and unleash their ultimate moves, a red energy pillar and a golden energy pillar soaring skyward, a devastating explosion erupting at their intersection, temple pillars crashing down thunderously, dust and smoke billowing; after the strike the frame freezes into a black-and-white slow-motion shot, debris suspended in mid-air as if time has stopped, colors slowly surging back like a returning tide, finally freezing on an epic post-battle tableau of the two standing back-to-back.

Dense particle effects, finely detailed textures of lightning, shockwaves and dust, model precision maxed out, materials realistic and lifelike, natural motion blur, atmosphere and sense of oppression both maxed out.\
Execution: Generate a single video containing the complete storyboard sequence in one call, using the Seedance 2.0 model.

# Action VFX Video Generation

## Core Methodology

### Four-Layer Prompt Architecture

A structured prompt system distilled from users' actual creations, with each layer fulfilling its own role:

Layer Role Key Elements**① Style & Quality Declaration Layer**Sets tone, rendering standard, color moodUnreal Engine 5, dark cinematic, high-contrast lighting, 3D Chinese fantasy anime**② Camera System Layer**Defines camera movement, cutting rhythm, immersionDynamic tracking, seamless switching between close-ups and wide scenes, low-angle upward shots**③ Core Visual Layer**Time-micro-progressive narrative, actions broken down at 0.5s granularityThunderous rise→runes bloom→stone gate opens→charges out**④ Technical Detail Reinforcement Layer**Particles/materials/blur/atmospheric-oppression finaleModel precision maxed out, natural motion blur, fine volumetric light

**Core Principle**: Describe "what happens in the frame" instead of "what the brightness value of frame X is"

### Spell-Attribute Color Semantics System

Lock in the dominant color scheme according to skill attribute to ensure visual consistency:

Color Attribute Emotion Keywords Particle CharacteristicsRed/Orange Flame/Rage Fierce, explosive Blazing flames splashing, vapor churningBlue/Cyan Frost/Control Piercing cold, congealing Ice-crystal refraction, frost bloomingPurple/Black Lightning/Shadow Eerie, devouring Leaping electric arcs, billowing black mistGold/White Divine/Energy Dazzling, sacred Sky-piercing light pillars, holy light cascading downGreen/Emerald Nature/Life Vibrant, spreading Coiling vines, scattering leaves

### Core Literary Expression Techniques

- **Verb density**: break through, thunderously, surging, whip up, roar → reject "appear, display, occur"
- **Sensory stacking**: describe visual + auditory + motion simultaneously ("deafening roar + massive cascade + thunderous rise")
- **Scale contrast**: tiny character vs. giant creature/structure → source of oppression
- **VFX binding**: VFX must be attached to actions ("fangs **spew forth** purple flames" rather than "purple flames appear")
- **Material details**: covered in moss, ferocious demon-head patterns, whole body wreathed in purple glow → source of realism

## Workflow

### 1. Preparation Phase

**6 confirmations that must be completed first**:

1. Preparation-phase completion criteria (proceed only after all 6 items are confirmed):

   1. ✅ Character assets confirmed (reference image uploaded or three-view drawing confirmed by the user)
   2. ✅ Aspect ratio confirmed (1:1 / 16:9 / 9:16)
   3. ✅ Resolution confirmed (480p / 720p / 1080p)
   4. ✅ Scene preference confirmed (user-specified or AI-designed)
   5. ✅ Video duration confirmed (10s / 15s / 20s / 30s / 60s)
   6. ✅ VFX intensity confirmed (subtle / medium / extreme)

2. **In-depth character analysis**:

   - Costume details: color, material, adornments, degree of damage
   - Weapon features: type, size, special patterns
   - Temperament positioning: cold/stern, bewitching, commanding, nimble
   - Physique traits: muscularity/agility/power

3. **Skill-type color locking**:

   - Fire → orange-gold/scorched red/blazing white
   - Ice → ice blue/cyan-white/frost white
   - Lightning → black-purple/purple-white/electric blue
   - Physical techniques → orange-gold shockwave + beast-shaped particles

**Element checklist**:

- \[ \] Character portrait/reference image uploaded
- \[ \] Skill name and attribute specified
- \[ \] Core actions defined (charge/burst/finale)
- \[ \] Resolution confirmed

### 2. Storyboard Planning Phase

**Storyboard = time-segment divisions within the same video, not multiple independent video nodes**

Standard four-segment structure (15 seconds)

Storyboard Duration Shot Type Content Core Rhythm KeywordsSB-01 Establish0-3s Wide→Medium Scene establishment/character charging Steady buildupSB-02 Charge3-7s Medium→Close-up Energy condensation/casting hand seals Black-white gradient oppressionSB-03 Burst7-12s Close-up+rapid cuts Skill eruption/combo impacts White flash/screen shake denseSB-04 Finale12-15s Pull-back overhead Aftermath spreading/freeze close Black-white freeze, color surge back

Extended structure for martial-arts combos (optional)

For combat-type skills, emphasizing combo rhythm:

```
【Stance-building segment 0-3s】Low-angle upward shot, fighting stance, black-white gradient
【Combo-burst segment 3-8s】Afterimages increasing (triple→quadruple→sextuple), one shake per punch
【Ultimate-punch segment 8-12s】Giant beast silhouette pierces the sky, extreme shake 0.8s
【Lingering freeze segment 12-15s】Black-white slow motion→colors surge back→overhead pull-back close
```

### 3. Prompt Construction Phase

Fill in layer by layer following the four-layer architecture:

Layer 1: Style & Quality Declaration

```
3D Chinese fantasy anime style, epic fantasy blockbuster texture,
dark cinematic tone, hyper-realistic 3D rendering, Unreal Engine 5 ultimate image quality,
high-contrast lighting, strong light-dark layering, mysterious eerie atmosphere maxed out,
explosive dynamic expressiveness, overall visual tension with immense impact
```

Layer 2: Camera System

```
Camera movement fluid and full of tension, seamless switching between close-ups and wide scenes,
dynamic tracking enhances an immersive in-the-moment experience, extremely strong cinematic narrative feel
Low-angle upward shots convey oppression, side tracking heightens the sense of speed,
overhead shot slowly pulling back to close on the hero's retreating silhouette
```

Layer 3: Core Visuals (Key)

**Use time-micro-progressive narrative, breaking actions down at 0.5-second granularity**:

Fire-type skill example:

```
The warrior clenches his fist and charges up, tiger-shaped flame energy coalescing on his knuckles like orange-gold molten lava,
muscles over his whole body taut and veins bulging, his battle robe crackling in the fierce wind;
the next second the Tiangang Fierce Tiger Fist thunders out,
the fist suddenly erupts into a giant tiger-shaped particle-energy phantom,
the tiger head reared skyward in a roar, fangs fully bared, its body formed of dense orange-gold particles and raging flames,
Surging fiercely forward with the momentum of the punch, the tiger's tail drags out a blazing white light pillar that pierces the sky and breaks through the clouds;
The shockwave bursts outward from the fist's surface in an expanding ring, the ground instantly cracks and collapses,
Sky-filling debris and dense mist churn like ocean waves, blotting out the sun, as a pillar of raging fire soars into the heavens
```

Ice skill example:

```
The heroine's slender hands form a spell-casting seal, frost flowers crystallize at her fingertips, crystalline and translucent,
Mystic ice energy spreads rapidly along the iron chain like ice-blue snake shadows slithering;
In an instant a wind blade sweeps out, the ice blade's trajectory tears white frost fissures through the air,
Wherever it passes, the air abruptly condenses into ice crystal particles that burst and scatter,
The stone pillars on the ground are sliced with mirror-smooth faces, frost spreads from the cut edges in all directions like ice flowers blooming;
At the finishing instant, a freezing shockwave sweeps across the entire field, heaven and earth lock into an ice-blue frozen still,
Shattered ice suspends in the air as if time has stopped
```

Layer 4: Technical Detail Enhancement

```
Rich particle effects; mist, water flow, and purple light with delicate textures,
Model precision maxed out, materials realistic and lifelike, motion blur natural,
Atmosphere and sense of oppression both maxed out,
Dust floating in the volumetric light clearly visible,
Ice crystal refraction, motion blur, particle explosion frames, ice surface reflections
```

### 4. Impact Frame Visualization Description (Core Technique)

**Principle**: Use on-screen actions instead of frame values

White Flash Frame Visualization Method

Effect Intent Visualization Description Pure White Burst Flash The frame bursts into blinding pure white like a lightning strike, instantly cutting back to the battle scene Enhanced White Flash Full-screen white light instantly swallows the frame, the shockwave spreads outward from the center in a high-speed ring, kicking up sky-filling dust and debris, after the intense light fades the scene cuts in abruptly Screen-Shake White Flash The frame bursts white at the instant of explosion, the camera shakes violently, amplitude large first then small, lasting 0.3 seconds before slowly returning to stable

Black-and-White Frame Visualization Method

Effect Intent Visualization Description Desaturation Charge The frame's colors drain away abruptly like ink wash, leaving only light-and-dark outlines, the lightning's white arcs looking especially sharp against the black-and-white frame Killing-Blow Freeze At the instant of the slash the frame congeals into a black-and-white slow-motion shot, debris and dust suspended in the air as if time has stopped, only the character's pupils retaining a trace of faint glow Charge Gradient The frame's colors recede slowly like a tide, the world gradually fading into cold gray black-and-white, the dead-silent oppression before a storm pervading

Impact Frame Rapid-Strike Visualization Method

Effect Intent Visualization Description Single Collision The two forces collide and instantly burst out dazzling white light, the shockwave exploding outward in a ring, the ground cracking with dust flying everywhere Secondary Burst Energy compresses at the collision point to its limit and then thunderously erupts a second time, strong lens distortion appears at the frame edges, sparks scattering like rain High-Frequency Rapid Strikes Each strike lands with a fierce jolt of the frame, flashes and explosion sounds rising and falling in succession, the rhythm pounding densely like war drums Every punch landing solid

Four-Tier Screen Shake System

```
【Light Shake】The camera trembles slightly like the aftershock of a distant explosion, naturally recovering after 0.2 seconds

【Medium Shake】The camera shakes violently at the instant of explosion, amplitude large first then small, slowly stabilizing after 0.3 seconds

【Heavy Shake】The shockwave hits head-on, the camera jolts violently like an earthquake,
       motion blur appears at the frame edges, the shake amplitude decays rapidly from its maximum,
       gradually recovering stability within 0.5 seconds

【Extreme Shake】The ultimate skill erupts, the camera shakes to its limit,
       brief defocus + edge distortion, dust and debris covering the sky,
       after 0.8 seconds the shaking slowly subsides like an aftershock
```

Complete Impact Rhythm Template

```
【Charge Phase】The frame's colors slowly recede like a tide, fading to cold gray black-and-white, the world sinks into dead-silent oppression

【Burst Point】Full-screen white light instantly swallows the frame, the shockwave spreads outward from the center in a high-speed ring,
         kicking up sky-filling dust and debris, the camera shakes violently, large first then small, lasting 0.3 seconds

【Impact Rapid Strikes】Each strike lands with a fierce jolt of the frame, bursting out dazzling white light and shockwave ripples,
           energy erupts a second time at the collision point, lens distortion + sparks scattering everywhere, rhythm dense as war drums

【Lingering Freeze】After the slash, the frame congeals into a black-and-white slow-motion shot, debris suspends as if time has stopped,
           colors slowly surge back like a tide, residual particles drift and dissipate in the volumetric light
```

### 5. Martial Arts Combo Exclusive Techniques

Afterimage Density Progression System

```
First punch: Triple afterimages → Tiger claw streaks a trajectory, a first hint of speed
Second punch: Quadruple afterimages → Overlapping shadows interlace, the dazzling sensation intensifies  
Third punch: Sextuple afterimages → Overlapping shadows like a tiger pouncing on prey, density at its limit

Rule: The number of afterimages increases with each combo hit, each punch carrying 1-2 more layers than the previous
```

Beast-Form Energy Giant Silhouette · Sky-Piercing Technique

Trigger timing: The instant of the ultimate punch/ultimate skill burst

Description template:

```
A giant [tiger/dragon/bear]-form virtual particle energy silhouette suddenly appears behind the punch,
The [beast]'s head rears skyward in a roar, [fangs/dragon horns/bear claws] fully bared,
The [beast]'s body is composed of dense [orange-gold/purple-black/ice-blue] particles and [raging flames/lightning/biting frost],
Surging fiercely forward with the momentum of the punch, piercing straight into the sky,
The [beast]'s tail drags out a light pillar dozens of meters long in [blazing white/purple-white/ice-blue], breaking through the clouds,
Momentum vast and boundlessly awe-inspiring
```

Screen Shake and Impact Frame Binding Rules

Combo Round Screen Shake Intensity White Flash Intensity Afterimage Layers 1st Punch Light Shake 0.2s Basic White Flash Triple 2nd Punch Medium Shake 0.3s Enhanced White Flash Quadruple 3rd Punch Heavy Shake 0.5s Explosive White Flash Sextuple Ultimate Punch Extreme Shake 0.8s+Defocus Full-Screen Extreme White Burst Beast-Form Giant Silhouette

### 6. Generation and Iteration Phase

1. Pass the complete prompt into the video generation tool

2. Generate the complete video in a single pass (do not split it into multiple nodes)

3. Check whether the key frames land:

   - \[ \] Does the black-and-white charge phase appear
   - \[ \] Do the white flash/impact frames trigger at the burst point
   - \[ \] Is the beast-form energy silhouette clear
   - \[ \] Is the screen shake effect noticeable
   - \[ \] Is color consistency maintained

4. If the impact frame effect is not obvious, consider post-processing:

   - Use `edit_video` to insert pure white frames at the key frames
   - Apply desaturation to the specified time segment

## Key Constraints and Standards

### Process Rules That Must Be Followed

1. **Resolution confirmation**: You must ask the user for resolution requirements before generation; this is a blocking requirement
2. **Storyboard, not nodes**: Storyboard segments are time-segment divisions within the same single video, not a concatenation of multiple independent video nodes
3. **Single generation**: After all storyboard segments are planned, use one `generate_video` call to generate the video containing the complete narrative

### Color Consistency Rules

- Fire element stays locked to orange-gold/scorched red/blazing white throughout; no blue-green tones may appear
- Ice element stays locked to ice blue/cyan white/frost white throughout; no warm tones may appear
- Lightning element stays locked to black purple/purple white/electric blue throughout; no yellow lightning may appear
- Martial arts shockwaves coordinate with the character's costume color tones (orange-yellow battle robe paired with orange-gold shockwave)

### Impact Frame Precision Rules

**AI video model limitation**: Current ability to understand frame-level effect instructions precise to 0.1 seconds is limited

**Remediation measures**:

- Prompts use visualized action descriptions ("full-screen white light swallows the frame") rather than numeric values ("brightness 246/255")
- When a key impact frame fails to trigger, reinforce it through post-editing
- Describe screen shake effects by duration ("0.3 seconds") rather than frame counts ("18 frames @60fps")

### Golden Timing for Slow Motion

Three moments where a 0.5x-speed slow motion shot must be inserted:

1. **The instant the energy ball leaves the hand** - Reinforces the ceremonial feel of the skill's release
2. **The instant the weapons clash** - Amplifies the sense of power in the impact collision
3. **The instant of the killing-blow freeze** - Highlights the decisiveness of the finishing strike

### Verb Quality Standards

**Forbidden verbs**: appear, show, occur, produce, form

**Required verb categories**:

- Burst type: boom thunderously, burst forth, explode, gush out, blast open
- Motion type: fiercely, abruptly, in an instant, surge up, sweep across
- Spread type: sweep over, spread, diffuse, surge, churn
- Sound type: roar, rumble, howl, thunder, tear

## Recommended Tools and Models

Use Seedance 2.0 for video generation; this model provides good support for action effects and impact rhythm.

## Advanced Techniques

### Multi-Element Fusion Skills

When a skill involves the fusion of two elements (e.g., lightning-fire/ice-wind), adopt the "primary color + accent color" strategy:

```
Lightning-fire fusion example:
Primary color: black-purple lightning (70% of the frame)
Accent color: scorched-red flames (30%, concentrated at the collision point)
Fusion point: purplish-red energy vortex (where the two converge)
```

### Environmental Feedback Enhancement

Skill bursts must trigger environmental responses to reinforce the sense of realism:

- Fire: scorched-black ground, distorted air, rising heat waves
- Ice: frozen ground, condensed water vapor, spreading frost flowers
- Lightning element: ground fissuring, static particles, metal resonance
- Body techniques: ground collapse, air blasts sweeping across, debris flying

### Storyboard Transition Techniques

**Hard cut transition** (used for burst points): white flash frame → direct cut to the next shot

**Soft cut transition** (used for power-up segments): camera push-in → focus shift → natural transition

**Impact transition** (used for combo attacks): screen shake on every strike → rapid jump cuts → creating a dense sense of rhythm