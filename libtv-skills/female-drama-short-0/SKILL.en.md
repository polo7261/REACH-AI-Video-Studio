---
name: female-drama-short-0
description: "Sweet romance short drama director: generates sweet-romance hooks, storyboards, and finished films"
---

# Female-Oriented Sweet Romance Short Drama · Single Episode

## Positioning (Only Responsible for One Reusable Thing / What It Is Not Responsible For)
- Only responsible for: the form of "Female-Oriented Sweet Romance Short Drama · Single Episode"—turning a single sweet-romance hook into a 16:9 landscape short-drama clip with a complete emotional arc (storyboard + final footage). The core is letting viewers place themselves in the heroine's position and experience the scorching doting of "being unreasonable—breaking every rule for her alone."
- Only responsible for pacing: **step-by-step output, confirmation at each step**—script → characters / character boards → scene palettes → storyboard → final footage per shot; each step goes to the user for confirmation first, editable and revisable, never running automatically all the way through.
- Only responsible for the final-footage foundation: within a single piece, the **coherent main storyline, shot stitching, multi-camera coverage, unified art style and color tone**—these are the fundamentals of "feeling like one real drama," hard-locked by this skill.
- Not responsible for: multi-episode serials and the whole series' four-act arc (the platform does not yet support splitting into multiple episodes); the generic shot-splitting and anchor-consistency mechanisms, model specifications (already covered by the base layer—use defaults or follow the user); **which art style category to pick** (free; up to the user / the style layer; this skill only guarantees whole-film consistency once chosen); non-female-oriented, non-sweet-romance subject matter.

## How It Is Used
The user provides a sweet-romance premise, or just one line about "the kind of addictive feeling they want," and this skill produces a single-episode sweet-romance short drama step by step: script → characters / character boards → scene palettes → storyboard → final footage per shot, confirming each step before moving on.

## Inputs (Before starting, clarify with `ask_human`, one at a time, in plain language)
- **Story setting / background**: What kind of setting does this story take place in? Era, location, industry environment.
- **Names of the leads**: What are the male lead and female lead called?
- **An opening**: One sentence is enough to make clear "what situation the opening is" (e.g., "jilted at the wedding," "mistaking the big boss on the first day at work"). If left blank, the Agent will propose 1-2 openings for the user to choose from.
- **Overall art style / color tone baseline**: What visual tone do you want (warm golden luxury / cool-toned urban / soft-light film…)? This will be set as the unified visual baseline for the whole film. If hard to articulate, let the Agent propose a version to choose from.
- **Binding device**: Why are the two forced to spend day and night together (marriage before love, contract partnership, power hierarchy, reunion after a breakup, mistaken identity…)? If hard to articulate, let the Agent decide based on the premise.
- **Reference faces for the leads**: Provide 1 or more real-person reference faces (used to blend non-existent virtual people, face-locked throughout the film).
- **Character profiles / core hook** (optional): Personality and appearance, the most desired heart-fluttering moment (publicly defending her / jealous confrontation / late-night confession / the domineering male lead's facade cracking…). If hard to articulate, let the Agent fill in a version based on knowhow; confirm once it's filled in.
- Not asked: which model to use, how files are stored—the base layer handles these by default. **The whole film uses a unified 16:9 aspect ratio**, **duration is not preset** and follows the content (see below).

## Three Image Prompt Frameworks (All Inlined at the End of This File, Applied by Stage)
- This skill is **self-contained within this single SKILL.md** (loading external sub-files on the platform is not yet stable, so nothing is split into external files).
- The end of the file holds three image prompt frameworks, applied by stage: the **character board stage** uses the "Character Identity Board Framework", the **scene stage** uses the "Scene Palette Framework", and the **storyboard stage** uses the "Storyboard Framework".

## Internal Workflow and Knowhow (Main Body)

### Stage-by-Stage Progression (Hard-locked: each step outputs something first and hands it to the user for confirmation; only after confirmation may the next step begin; without the user's nod, starting any generation of the next stage is forbidden)

**Stage One · Concept**
- Use `ask_human` to ask everything from the "Inputs" above, one at a time: story setting, the leads' names, an opening, the overall art style / color tone baseline, plus the binding device / reference faces. If any missing item would significantly change the final footage, ask first—don't guess your way forward.

**Stage Two · Produce the Written Script → Confirm**
- Based on the opening the user provided, use AI to divergently generate the short-drama script. **Duration is not rigidly fixed**—follow the content (60, 90 seconds, or longer all work); the yardstick is a smooth main storyline and fully realized emotion—don't cut transitions just to squeeze under one minute.
- The script delivers the complete **four-piece set** in one go, so the user can align content, characters, settings, and tone all at the text stage:
  1. **Plot shot breakdown**: Advances according to the "Single-Episode Five-Step Arc" below and follows a "because → therefore" causal main line (see "Coherence"), including scene annotations, character actions, and shot suggestions, with **1-2 lines of dialogue written for every shot** (see "Dialogue"), using the dialogue to string the plot together.
  2. **Character image prompt table**: One prompt per character that can be fed straight into `generate_image` (looks, temperament, styling).
  3. **Scene prompt table**: One prompt per scene, clearly stating the spatial look + **the dramatic terrain this scene needs** (a corner to retreat to / a window to gaze out of / a doorway where a third party appears…, back-derived from the actions of the five-step arc), and marking which camera positions / shot sizes are needed.
  4. **Unified visual baseline**: One art style / color tone prefix shared by the whole film (color temperature, brightness, saturation, light quality, tonal key, lens texture, aspect ratio), applied to every subsequent image and shot.
- 🔒 Hand to the user for confirmation with **actionable options** (e.g., "This version works, continue / swap in a more hard-hitting opening / rework Scene X / dialogue too flowery / make the tone cooler"), not an open-ended toss of "OK?".
- Until the user confirms, **never call any `generate_*` tools**.

**Stage Three · Generate Character Images → Confirm → Produce the Character Identity Board**
- After the script is confirmed, use `generate_image` with the character prompt table + the **unified visual baseline prefix** to blend the reference faces into virtual-person images of the male and female leads for confirmation. **Do not produce white-background, ID-photo-style images**—they must be proper portraits where the face shape, temperament, and tone can be clearly seen (skin texture, natural light, realistic texture, no plastic-mannequin feel; generate the male and female leads under the same lighting and the same visual baseline, with later images referencing earlier ones, to avoid "one dark, one light, not looking like the same film").
- 🔒 Hand to the user to confirm the characters: are the faces right + is the temperament right + is the tone consistent ("Use this version / swap in another / make the male lead more coolly aloof / make the female lead more girl-next-door / the two don't match in tone—unify them"). **Before confirmation, no character boards are generated and no moving to the next step.**
- **After confirmation**, produce a **"Character Identity Board"** (CHARACTER IDENTITY BOARD, 16:9) for each main character—this is the **anchor asset** for character consistency across the film; all subsequent scene images and videos use it as the identity reference to lock the person and the styling. **When entering character board generation, follow the "Character Identity Board Framework" at the end of the file**, filling in that character's information to generate.

**Stage Four · Generate Scene Palettes (Establish and Lock the Space, 4 Images per Scene) → Confirm**
- After the characters are confirmed, first **nail down the space where the story takes place** (it is the source of spatial truth for the storyboard and final footage that follow). Following the script's scene prompt table, use `generate_image` + the unified visual baseline to generate, for each scene, **4 palette images of the actual scene, one each for different positions, camera setups, and angles** (wide establishing / medium / close-up / over-the-shoulder reverse), locking this scene's spatial look and dramatic terrain (a corner to retreat to / a window to gaze out of / a doorway where a third party appears…), keeping the same space and the same tone consistent.
- **When entering scene generation, generate each scene by following the "Scene Palette Framework" at the end of the file**, filling in that scene's information.
- 🔒 Hand to the user to confirm the scenes and the tones. Only once the space is settled does the storyboard have a basis to be laid out.

**Stage Five · Generate the Storyboard (Block the Shots in the Locked Space) → Confirm**
- After the scenes are confirmed, take the two characters' **"Character Identity Boards"** as the sole fixed leads and the **confirmed scene palettes** as the spatial reference, and use `generate_image` to generate a **16:9 black-and-white cinematic storyboard (a 12-panel director's shot breakdown)**, "rehearsing" the shot choreography and the two characters' blocking within this locked space—people and settings are both ready-made anchors; the storyboard only decides "how to shoot and how to move."
- **Once in the storyboard phase, fill in this film's info per the "Storyboard Framework" at the end of the document** to generate. The storyboard matches the final film's aspect ratio (16:9 throughout), and the final film is generated directly from its shot arrangement—no need to change aspect ratios again.
- 🔒 Submit the storyboard to the user for confirmation: are the panel order, shot language, and blocking right ("this panel version is fine / change the camera angle in panel X / push the climax later"). **Do not proceed to the next step without confirmation.**

**Phase 6 · Produce the Final Film Shot by Shot from the Storyboard**
- **Generate strictly shot by shot, following every storyboard panel**: use the "Character ID Board" to lock characters and looks, the scene palette to lock settings and colors, and apply the unified visual baseline throughout. Each `generate_video` call covers a single shot ≤15s; the full film is assembled from multiple shots via `composite_video` (total runtime follows the content, not bound by the 15s limit); `generate_audio` does the voiceover per the script's **per-shot lines** + BGM (don't deliver music with no dialogue). Stitch shots according to "Coherence"; for heart-fluttering signature scenes, use close-ups, slow motion, and shallow depth of field to convey five-senses details.
- **This chain (storyboard → shot breakdown → shot-by-shot generation) is the core lever for controlling the final-film success rate**: nail down shots and blocking on cheap static storyboard frames first, then generate the video, avoiding the loss of control that comes with generating directly.

### Coherence: One Causal Main Line + Shot Stitching (Smooth, Without Jarring Breaks)
- **Plot causality**: the five steps are not five parallel signature scenes but a "because → so" chain—each step is the direct result of the previous one. Better to drop one twist than to let the main line falter; **coherence takes priority over the number of signature scenes**.
- **Leave time for transitions**: that's what the flexible runtime is for—don't cut setup and breathing room just to cram in one more minute; emotion needs space to breathe.
- **Shot stitching**: join adjacent shots using "action matches" (the previous shot's action isn't finished; the next shot continues it), "gaze matches" (looking off-screen → the next shot shows what/who is being looked at), "sound leads in" (the next shot's audio enters half a second early), and "smooth multi-camera cutting within the same scene" (shot-reverse-shot, shot scale progressing from far to near)—not a hard collage.
- **Criterion**: watch two adjacent shots back to back—does the second shot appear "as a matter of course"? If it feels like a different film, the stitch failed.

### Dialogue: String the Plot Together with Lines, Don't Just Show Images
- **Density**: in principle, **each shot gets 1-2 lines of dialogue** (dialogue / monologue / voiceover), letting the plot advance through lines rather than making viewers stare at images guessing what happened. The film must not remain "score + images" throughout.
- **Dialogue does three things**: deliver information (who, what they want, where the conflict lies), advance causality (this line makes the next step happen), stitch adjacent shots (the previous shot's last line throws out a hook; the next shot's line catches it)—dialogue is the **second stitching thread** after visuals, meshing with "Coherence."
- **No drop in quality**: lines are short, colloquial, and individually quotable; they're "things a person would actually say," not narrator voiceover tone, not filler.
- **Silence is the exception, not the norm**: a few purely emotional shots (a close-up of an exchanged gaze, a moment of being stunned) can go without lines, but that's a deliberate breathing point, not a whole film without words.
- **Voiceover follows the script text**: `generate_audio` records line by line per the script's dialogue, colloquial feel, avoiding the AI radio-announcer tone.

### Unified Art Style and Color Tone Across the Whole Film (Like One Single Film)
- **Set one visual baseline** (look): color temperature (warm / cool), brightness, saturation, light quality (natural light / dusk golden light / studio hard light), tonality, lens texture, aspect ratio—written in Phase 2 as a **shared style prefix** used by all images and videos.
- **Free choice, consistency locked**: which art style category to choose is up to the user / style layer; once chosen, **every character image, every set of scene images, and every shot in the film applies this same baseline**—this rule is locked and non-negotiable.
- **Cross-reference**: when generating multiple characters / multiple scenes, later images reference the color tone and lighting of earlier ones; don't tune each in isolation.

### The Episode's Five-Step Arc (Write the Script to This, Strung into One Causal Main Line)
1. **Opening in a Predicament**: the heroine is thrown into a concrete, tangible predicament right at the open (coerced / humiliated / picked on—choose one or combine). The first few seconds must make the target audience "step into her shoes"—this is her situation, not background exposition.
2. **High-Impact Rescue**: the male lead enters in an unexpected way and crushes the trouble with overwhelming force. He is the heroine's fallback, not her proxy—so before he steps in, she has already spoken up / fought back once herself; the male lead is "the icing-on-the-cake finishing blow."
3. **Signature-Scene-Level Heart-Flutter**: the scene with the highest heart-flutter concentration in the film, mixing at least two of the three types of ammo below, with full close-ups and breathing space, making it "screenshot-worthy and shareable."
4. **Mini-Climax Reversal**: arrange one moment where the dominant male lead's persona "cracks," or one escalation of jealousy—creating a memory anchor and giving sweetness rises and dips so it never turns cloying.
5. **Hook Ending**: close with one weighty declaration / one ambiguous open note / one tease of a twist, in place of the whole series' "coronation ceremony," leaving the audience's wanting-more at the very last second.

### Three Types of Heart-Flutter Ammo (Mix Them in Every Film, Don't Rely on Just One)
- **Contact type**: steadying her when she loses balance, eye contact in a cramped space, tucking her hair / wiping the corner of her mouth / tying her scarf, a forehead kiss at parting. Key point: the man's action is natural and proactive; the woman's reaction is being stunned or blushing, not exaggerated pushing away.
- **Line type**: protective declarations, a jealous retort blurted out, a pet name that belongs only to the two of them, undisguised favoritism in public. Lines must be short, sharp, and quotable on their own.
- **Behavior type**: quietly noting preferences she mentioned in passing, breaking his own rules to cook for her, secretly clearing her workplace obstacles, acting childishly out of character after getting jealous.

### Write Heart-Flutter with the Five Senses (Film It, Don't Write Adjectives)
Criterion: don't generate images like "he's very charming"—break charm down into details a camera can shoot and viewers' bodies can resonate with—
- Visual: the bob of his Adam's apple, the curve of a not-quite-smile at the corner of his lips, lowered lashes as he undoes his cufflinks.
- Auditory: a low voice close to the ear, a short soft chuckle.
- Tactile: the shiver of cool fingertips brushing across skin, the lingering warmth and weight of a jacket.
- Smell (converted into visible reactions): his split-second daze when he catches the scent of her hair, her stunned stillness when enveloped by his cool fragrance.

### The Male Lead's Gap (Flash It at Least Once per Film—This Is the Strongest Thrill Point)
The man plays by one set of rules with the world (aloof, dominant, airtight) and another with the heroine (patient, indulgent, clumsy, boyish). The moments of "she's the only one in the world who can crack him"—the supremely arrogant man fumbling through cooking for the first time, the man who can command any room completely tamed by a single sentence from her, clinging to her like a big dog when sick and weak—each one is a memory anchor; give each its own dedicated shot.

### Jealousy in Three Stages (Escalating Through the Film's Phases, Showing Possessiveness)
- Entry level: witnessing the heroine talking with another man, his gaze suddenly turning cold, leaving without a word.
- Intermediate: taking the heroine away directly, closing in to interrogate "who was that just now," distance-pressure maxed out.
- Master level: appearing breezily calm on the surface while secretly making the rival unable to take a single step; or deliberately staging a scene to test her reaction.

### How to Use Conflict (Criteria, Not a Pile of Bans)
- The conflict-maker is an external third party (a rival coveting the male lead, snobbish relatives who fawn on the high and trample the low, sabotaging colleagues); no deep values-based opposition is written between the two leads.
- Even when there's a misunderstanding, it gets talked out face to face, not propped up by "I won't explain, you don't ask"—contemporary audiences have zero tolerance for dragged-out push-pull.
- Every conflict's landing point is a stage for the male lead to "perform favoritism": someone gives her a hard time → the male lead counters with crushing force → converted into one massive heart-flutter delivery.

## Output
One 16:9 landscape single-episode sweet-romance short drama, runtime following the content: the five-step arc strung into a causal main line, high-frequency heart-flutter, conflict externalized, hook ending, unified art style and color tone across the whole film, smooth shot stitching. Deliver stepwise along the way: the script four-piece set → character images + Character ID Board → scene palettes (4 images per scene, nailing down the space) → storyboard (12 black-and-white panels) → final film produced per the storyboard; each step comes with its corresponding confirmation.

## Self-Check (Quality Items Specific to This Genre of Film)
- Before starting work, did you first ask for the **story setting** and the **leads' names**, and receive the opening and the **art style / color-tone baseline**, before getting to work?
- Did you **first produce the text script (including character prompts, scene prompts, and the visual-baseline four-piece set), get user confirmation, and only then start generating any visuals**?
- Between characters, scenes, and shots, is the **color temperature / brightness / tonality consistent**—do they look like people from the same film, the same scene? (No more one-dark-one-light.)
- Is there a **visual baseline** shared across the whole film, applied to every image and every shot?
- Is the character confirmation image a **proper portrait** (not a white-background ID photo)? After the character is confirmed, was a **"Character Identity Board"** produced, and do the subsequent scene images and videos use it as the identity reference to lock the character?
- Is the scene space **nailed down first** (4 color boards from different camera positions per scene, same space, same color tone, including the dramatic terrain this scene needs) before laying out the storyboard?
- Is the storyboard a **12-panel black-and-white storyboard** laid out with **two character boards + the confirmed scene color boards**, locking spatial continuity and both characters' identities? Is the final film generated **strictly following every panel of the storyboard**?
- Are adjacent shots **stitched** (action / gaze / sound / smooth multi-camera cuts), or just hard-spliced? Does it flow smoothly when watched in sequence?
- Does **essentially every shot have 1-2 lines of dialogue**, threading the plot together through dialogue? Are there long stretches with only visuals / score and no dialogue?
- Do the five steps form one **causal throughline** (because → therefore), rather than five parallel highlight scenes? Does the runtime leave breathing room for transitions, rather than cramming everything into one minute?
- Do the first few seconds immerse the viewer in the female lead's **specific predicament**, rather than opening with background exposition?
- When the female lead runs into a misunderstanding / gets bullied, does she **speak up to clarify and strike back herself first**? Is the male lead's intervention the "final blow," or does he handle everything for her (the latter must be fixed)?
- Does the male lead's contrast moment flash on screen at least once, given a dedicated shot of its own? Does the falling-in-love beat land on **visible and audible five-sense details**, not adjectives?
- Does the conflict come from an external third party and get openly laid out face to face? Is the male lead's assertiveness built on **respect**—no frivolous / controlling / boundary-crossing shots whatsoever (this rule is locked, no exceptions).
- Swap in a sweet-romance setup with a different theme (marriage-before-love replaced by reunion-after-breakup)—does the system still hold, or can it only run the one used in the example?

## When to Ask the User
- **Every stage must stop for confirmation—this is not optional**: script, character design, scenes, storyboard—each is a hard gate; only after confirmation do you move to the next step.
- Conception stage: story setting / the leads' names / opening / art style and color tone / binding device / missing reference face—these will significantly change the final film; ask first.
- When the core hook direction has multiple reasonable options and affects the opening—give a recommendation, then confirm.
- Present options as A/B/C/D, with labels phrased as business actions (e.g., "go with this opening / make it harsher / revise scene 3 / swap the face / make the color tone cooler"), without exposing internal mechanics.
- Runtime, format, file names, tool fields—the Agent decides based on the content; don't ask.

---

## Three Image Prompt Frameworks (apply by stage; fill in the `{ }` placeholders per this film; art style / color tone carries over the unified visual baseline)

### Character Identity Board Framework (used in Stage 3)
> After the character is confirmed, generate one 16:9 Character Identity Board for each main character (the anchor asset for character consistency across the whole film). After the character boards are generated, move on to Stage 4 scenes.

```
CHARACTER IDENTITY BOARD — artistic cinematic layout (16:9)
[Subject]: Based on the reference image. Name: {character name}. Identity: {character identity}. Apply subtle color correction to create a clean, premium art-book texture—{color tone keywords}, cinematic.
Visual medium: {art style}. Pure white / soft off-white background. No environment, no logos, no watermarks.
Design direction: Do not make this a standard character reference sheet. Create a cinematic identity board that feels like a high-end animation studio's character study, fused with art-book typography. Asymmetric, elegant, impressive. Use large areas of negative space, varied image scales, and intentional imbalance. Avoid grids, blueprint-style designs, catalog-style layouts, and repetitive turnarounds.
[Important layout rules]: Do not let any character images overlap. Every view must have clear separation and breathing room. Keep all bodies, portraits, silhouettes, and detail studies visually distinct from one another. No cropped faces, hidden limbs, stacked figures, or merged poses.
[Main composition]: Place one large hero full-body view slightly off-center as the visual anchor—{signature pose + signature outfit/prop description}. Around it, arrange smaller supporting studies with clean spacing: a neutral standing full-body view, back view, side view, {2–4 poses matching the character's personality}, a top-down body angle, a low-angle heroic body angle, and several expressive portrait studies. Each view should read as an independent, clean character study, not a frame from the same scene.
[Identity lock]: Strictly maintain identity consistency across all views:
— Same face: {skin tone, eye color, facial features, signature expression}.
— Same hairstyle: {hair color + hairstyle structure + details}.
— Same outfit: {describe clothing, accessories, and footwear piece by piece from top to bottom, including colors and materials}.
— Same body proportions: {body type keywords}.
— Same posture language and visual personality: {3 personality keywords}.
[Practical reference details]: Make the character easy to reuse in future image and video generation: a clear face shape, a clear hair silhouette ({hairstyle shorthand}), a clear outfit silhouette, a clear {body type} figure, a clear {signature prop/hand state}, clear posture, and a clear expression range.
[Artistic zones]:
— Silhouette study zone: 2–3 simplified black character silhouettes ({3 representative poses}).
— Expression study zone: subtle emotional variations ({4 emotions fitting the character}).
— Detail study zone: {3–4 signature object close-ups}.
[Typography]: A stylishly minimal character ID info block, eye-catching and art-directed:
— NAME: {character name}
— ROLE: {identity in English (Chinese)}
— CORE MOOD: {English mood phrase (Chinese)}
— VISUAL SIGNATURE: {3–4 signature elements, in English and Chinese, separated by ·}
Use small handwritten-style labels only where they help. Subtle editorial arrows and annotation marks are allowed, but keep it minimal and elegant.
[Style]: Minimal, cinematic, premium, art-book feel, clean, expressive, practical for real production use. The final image should look like an artistic character identity board designed to help an AI model understand the character's face, silhouette, outfit, posture, and emotional range.
```

### Scene Color Board Framework (used in Stage 4)
> After the characters are confirmed (before the storyboard), generate a set of 16:9 live-action scene color boards for each scene (same space · 4 camera positions), **nailing the space down first**—it is the spatial source of truth for the later storyboard shot layout and the final film. The spatial elements must match the script's scene list and cover the dramatic terrain this scene needs; on-screen characters have their look locked via the "Character Identity Board." **Run once per scene, output 4 boards.**

```
Generate a set of cinematic live-action scene color boards for {scene name} (16:9 horizontal, 4 camera-position views of the same space), used to nail down the spatial look of this scene and to serve as the background and spatial anchor for the subsequent storyboard shot layout and all shots. Art style / color tone strictly carries over the film-wide unified visual baseline: {visual baseline prefix: color temperature, brightness, saturation, light quality, tonality, lens texture}. Realistic cinematic texture, like a frame grab from the final film—not a concept image, not an illustration.
[Spatial lock · fixed for the entire scene] The story takes place in {scene overview: e.g., a late-night living room in front of the floor-to-ceiling windows of a penthouse}. The following elements have exactly the same position, form, and material across all 4 boards:
— Core stage / floor: {e.g., gray stone floor + low genuine-leather sofa set}.
— Spatial boundary: {e.g., a full wall of floor-to-ceiling windows / a long corridor / a bar counter}.
— Directional anchors ×2: {e.g., fireplace on the left, spiral staircase on the right} (used to keep the space readable across different camera positions).
— Large visual anchor: {e.g., the city nightscape outside the floor-to-ceiling windows / a giant hanging painting / a neon sign}.
— Environmental props: {e.g., red wine glasses on the coffee table, rug, green plants}.
— Overall atmosphere in one line: {e.g., an aloof, restrained premium feel with a simmering undercurrent}.
```
— Dramatic terrain (the spatial elements this scene's action requires): {e.g., a corner to retreat into, a floor-to-ceiling window to turn and gaze out of, a doorway where a third party can appear, a bar counter to lean against…} — deduced backward from this scene's plot action; it must genuinely exist in the space.
【Lighting Lock】Key light: {e.g., cool blue city light outside the window}; fill / ambient light: {e.g., warm yellow floor lamp indoors}. All 4 images share the same light positions, color temperature, and light-dark relationships; only the angle of incidence changes with the camera position — the nature of the light never changes.
【4 Camera Position Recipes】Produce 1 image for each, in order, covering the shot sizes this scene's narrative requires:
— Image 1｜Establishing wide shot: establishes the entire space and the characters' positional relationships; characters small, environment large; orientation anchors and boundaries clearly visible.
— Image 2｜Two-shot medium: {the two characters' relational state in this scene: sitting across / side by side / one advancing, one retreating}; medium shot with environment, establishing relationship and distance.
— Image 3｜Shallow depth-of-field close-up: {this scene's key detail: intertwined fingers / a keepsake on the table / a glance}; background blurred but still recognizable as the same space.
— Image 4｜Over-the-shoulder reverse: looking over one character's shoulder at the other (or out the window / toward the doorway); used for shot-reverse-shot dialogue, reinforcing perspective and presence.
【Character Handling】At this stage the storyboard has not yet been generated. If characters are included, strictly use the likenesses in the 《Character ID Board》 to lock identity and styling (consistent face / hairstyle / clothing / proportions); blocking is roughly arranged according to this scene's plot action (precise shot breakdown is saved for the storyboard stage). Alternatively, you may produce pure environment empty shots, but they must be the same space with the same lighting.
【Consistency Iron Rules】These 4 images are **4 camera positions of the same real space at the same moment**, not 4 different rooms: same furnishings, same lighting, same color tone, same materials, same weather / time of day. Forbidden: changing the space, palette, or season between images, or arbitrarily adding/removing large furnishings.
【Composition Requirements】The 4 images must each differ in shot size, camera position, and depth; avoid average compositions and stiff frontality; use {orientation anchors} and {light sources} to create spatial layering and dramatic light and shadow.
【Forbidden】No text / logos / watermarks, no timestamps, no comic or cartoon feel, no UI elements, no collage / split screen (each image is an independent, complete frame).
【Style】Realistic, cinematic, high-end, true textures, refined lighting, easy to use as background anchors for video generation. The final 4 images should look like stills a cinematographer captured from 4 camera positions in the same scene of the same show.
```

### Storyboard Framework (for Stage Five)
> After the scene palette is confirmed, use the two 《Character ID Boards》 as the sole fixed leads and the confirmed 《Scene Palette》 as the spatial reference to generate a 16:9 / 12-panel black-and-white director's storyboard within this established space. The two leads strictly use the character board likenesses; the space strictly uses the scene palette. Once the storyboard is confirmed, proceed to final footage.

```
Create a {emotional tone: sweet / ambiguous / high-intensity / tear-jerking} {scene type: rainy-night confession / office kabedon / airport farewell} scene for the storyboard, focused on "{core narrative arc: the tension and rhythm of moving from state A to event B}". Use the two characters from the reference images as the sole fixed leads:
Character A ({recognizable short name}): {hairstyle and hair color, signature accessories, skin tone, clothing details, body type, expression and demeanor}.
Character B ({recognizable short name}): {same structure as above}.
Both characters must be completely consistent across all panels: same face shape / hairstyle / hair color / eye color / clothing / body proportions / visual temperament. No face changes, no swapped hairstyles, no redesigning the characters. The two identities are strictly distinguished and locked.
A 16:9 landscape storyboard table with 12 cinematic storyboard panels.
The actual drawing must be black and white only: rough pencil lines, quick gestural sketches, minimal shading, dynamic line work, strong silhouette readability, an obvious sense of being unfinished. Overall it should look like the director's storyboard manuscript of a {film type: urban romance drama}, not a finished illustration. Emphasize the feel of cinematic previsualization, camera blocking, spatial continuity, and {rhythm type: emotional rhythm}.
【Scene Lock】Strictly use the confirmed 《Scene Palette》 as the spatial reference; do not invent a new space. The story takes place in {scene overview}; layout / furnishings / boundaries / lighting / color tone fully follow the scene palette: {core stage / floor elements}, {spatial boundaries: floor-to-ceiling window / long corridor}, {orientation anchors ×2}, {background: city night view / crowd}, {key light} and {ambient light: warm yellow table lamp / neon}, {large visual anchor: rain-streaked window / signage}, {environmental props}, {one-sentence overall atmosphere}. All shots occur in the same continuous space; both characters are always present (if one temporarily leaves, it must be noted in the panel description); key scene elements stay in consistent positions — do not regenerate the scene in each panel.
【Plot Core】{5–6 short lines: starting state → shift in atmosphere → middle event → escalation / turning point → climactic moment → resolution}. The emphasis is not {to avoid: cheap melodrama / heavy-handed preaching}, but rather: {tension / ambiguous atmosphere}, {psychological games / emotional push-and-pull}, {rhythm: approaching and retreating}, {contrast: restraint and impulse}, {sense of ritual / the solemnity of a heart-fluttering moment}.
The rhythm gradually moves from "{Stage 1: still gazing / acting as if nothing is wrong}" → "{Stage 2: tentative movement / closing distance}" → "{Stage 3: eruption / confession / moment of contact}".
The two characters' actions and micro-expressions must change continuously — no static posing: {list 12–15 concrete action phrases separated by /, e.g.: lowering the head to dodge a gaze / reaching out then pulling back / brushing hair from the other's face / ear tips flushing / turning to leave but having one's wrist caught…}.
【Camera Language Library】(each panel must carry explicit camera language): slight handheld shake / orbiting rotation around the pair / low-angle shot / telephoto depth compression / top-down panorama / wide-angle spatial stretch / tilted composition / fast push-in to capture the {heart-flutter} moment / over-the-shoulder shot to reinforce the {gaze} perspective / shallow depth-of-field close-ups (hands, eyes, small gestures) / use {scene anchors} for spatial orientation / use {light sources} for dramatic light and shadow. No average compositions.
【12-Panel Functional Framework】(each panel = shot size / technique + narrative function + 3–4 lines of concrete content):
Panel 1 ― Ultra-wide / establishing space: panoramic view establishing the environment and the two characters' positions; characters small, environment large.
Panel 2 ― Medium shot / establishing relationship: both characters in frame, initial state (confrontation / chance encounter / silent coexistence), slowly pushing in.
Panel 3 ― Over-the-shoulder close-up / POV and psychology: seeing the other's face from one character's viewpoint, background blurred.
Panel 4 ― Two-shot medium / spatial change: distance widening or narrowing (retreating toward a corner / one rising to their feet / brushing past).
Panel 5 ― Low angle or close-up / building tension: emotion or action brewing (a clenched fist / words held back).
Panel 6 ― Orbiting shot / rhythm ignition: the event officially begins (music starts / the first words are spoken).
Panel 7 ― Telephoto / testing: one takes the initiative, the other responds; distance and tension shift.
Panel 8 ― Tilted composition or handheld / critical point: on the verge of tipping (closing in / about to say it / the moment a hand reaches out).
Panel 9 ― Fast push-in / explosive climax: the core event (confession / kiss or embrace), the point of contact as the focal point.
Panel 10 ― Top-down or extreme long shot / detachment and breath: overlooking the whole scene, emphasizing space and a sense of ritual.
Panel 11 ― Over-the-shoulder or close-up / response reversal: the other's reaction (embracing back with reddened eyes / turning and fleeing).
Panel 12 ― Medium shot / resolution: the state freezes or a third party intervenes; scene elements remain in place, leaving a lingering afterglow.
【Overall Temperament】Fusing: {realistic-subject reference} / {film genre reference} / {emotional keywords} / {storyboard style: J-drama atmosphere / K-drama slow motion} / {classic reference works} / {credibility: authentic, grounded emotional reactions}.
【Consistency Maintenance】: spatial continuity / both characters' identities strictly locked / scene elements fixed / character proportions stable / clearly dynamic camera changes.
【Annotation Color System】: red = character movement direction / blue = camera movement / green = composition and spatial focus / orange = light direction / purple = tension and emotion / black text = panel number and shot notes.
No timestamps, no speech bubbles, no cartoon feel; maintain the temperament of a film director's storyboard.
```