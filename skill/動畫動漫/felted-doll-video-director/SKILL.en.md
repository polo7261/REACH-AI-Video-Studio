---
name: felted-doll-video-director
description: "Felted doll healing-style director: creates wool-felt, fluffy-doll, soft-cute, warm fairy-tale videos"
---

# Felt Doll Healing-Style Director Skill

## 0. Skill Positioning

This Skill helps users create image and video assets in the style of "wool felt, fluffy plush toys, soft cute healing, miniature model scenes, and warm fairytale charm."

It is not generic 3D cute-toy style, not plastic figurine style, not blind-box toy style, and not a cheap cartoon filter. Its core is making images show the texture of real handmade wool felt: short-pile fibers, needle-felting puncture texture, a matte felt surface, imperfect handmade edges, miniature model sets, warm lighting, shallow depth of field, and a quiet sense of companionship.

This Skill must be able to start from the user's vague idea and complete the full production pipeline:

 1. Requirement understanding
 2. No-reference-image creative guidance or reference-image analysis
 3. Character ideation
 4. Felt character assets
 5. Miniature scene assets
 6. Prop assets
 7. Image prompts
 8. Storyboard design
 9. 5-second image-to-video prompts
10. Multi-shot short film prompts
11. Editing, sound, and subtitle suggestions
12. Review and rework rules

---

## 1. Use Cases

Suitable for creating:

- Cute pet IP
- Small animal character images
- Little monster, little sprite, little mushroom person, and little cloud characters
- Children's story visuals
- Holiday greeting short videos
- Healing short videos
- Goodnight story short videos
- Warm brand visuals
- Social media covers
- 5-second image-to-video
- 15-second mini short films
- 30- or 60-second warm healing short films
- Avatar series, character state images, prop images, and miniature scene images

Not suitable for creating:

- Horror dolls
- Gore and thriller content
- Dirty, tattered dolls
- Realistic animal fur
- Highly reflective plastic toys
- Ordinary 3D cartoon animation
- Hard sci-fi mechanical scenes
- Fast fights, running, chases
- Intense flash cuts and glitch transitions

---

## 2. Core Style Constraints

Every time this Skill runs, it must first ensure the following style:

### 2.1 Must Keep

- Wool felt material
- Fine, dense short-pile fibers
- Needle-felting puncture texture
- Imperfect handmade edges
- Matte felt surface
- Small rounded body shapes
- Short arms and short legs
- Simple, gentle facial features
- Miniature model scenes
- Soft warm-yellow lighting
- Macro photography
- Shallow depth of field
- Handcrafted set texture
- A quiet, companionable, warm, healing mood

### 2.2 Must Avoid

- Plastic look
- Resin figurine look
- Blind-box toy look
- Generic 3D animation look
- Overly realistic glass eyes
- Real animal fur
- Dirty, matted long fur
- Horror-doll expressions
- The look of a high-saturation cheap toy commercial
- Large-scale movements
- Limb stretching and deformation
- Violent camera shake

---

## 3. Progressive Disclosure Interaction Rules

This Skill uses "progressive disclosure" by default — do not dump everything on the user at once. Output in layers based on how developed the user's input is.

### 3.1 L0: User has only a one-line idea

User examples:

- "I want to make a felt bunny."
- "Make a Christmas healing short video."
- "Help me make a cute little monster."

Output:

1. First determine the user's goal.
2. Proactively offer 3-5 creative directions.
3. For each direction, give only the character, scene, props, mood, and feasible video actions.
4. Do not output extra-long prompts directly.

Output format:

```markdown
## Creative Directions
| Direction | Character | Scene | Props | Mood | Suitable Video Actions |
|---|---|---|---|---|---|
```

---

### 3.2 L1: User has chosen a direction

User examples:

- "Pick #2, and make it a little fox."
- "I want a little fox with a scarf on a snowy night."

Output:

1. Character design
2. Scene design
3. Prop design
4. Color and mood design
5. Image asset planning

Do not output all the long-video prompts directly unless the user explicitly asks.

---

### 3.3 L2: User wants to generate images

Output:

1. Character asset image prompts
2. Scene asset image prompts
3. Prop asset image prompts
4. First-frame image prompts
5. Chinese negative prompts
6. English negative prompts

---

### 3.4 L3: User wants a 5-second video

Output:

1. Video mode determination: single-shot light action / single-shot micro-story / multi-shot edited version
2. 5-second timeline
3. Image-to-video prompt
4. Sound effect suggestions
5. Review priorities

---

### 3.5 L4: User wants a video of 15 seconds or longer

Output:

1. Story structure
2. Storyboard table
3. An independent video prompt for each shot
4. Editing rhythm
5. Sound design
6. Review and rework checklist

Principles:

- Do not generate an entire long film from a single long prompt.
- Long films must be split into multiple 3-5 second shots.
- Each shot controls only one main action.

---

## 4. Input Assessment Rules

### 4.1 No Reference Image

If the user has not provided a reference image, you must proactively offer 3-5 creative directions.

Each direction includes:

- Direction name
- Character type
- Appearance features
- Felt material design
- Miniature scene
- Props
- Mood keywords
- Feasible images
- Feasible video actions

Example direction:

```markdown
### Direction 1: Goodnight Star Bunny
Character: a white wool-felt bunny, round and chubby, big head and small body, hugging a yellow felt star.
Scene: a miniature bedroom with a small wooden bed, a cotton quilt, and a warm yellow nightlight.
Mood: quiet, companionship, goodnight, healing.
Video actions: the bunny blinks, gently hugs the star tighter, and its ears twitch slightly.
```

---

### 4.2 With a Reference Image

When analyzing a reference image, extract only the elements that can be adapted — do not copy the original.

Must analyze:

1. Subject type
2. Shape and structure
3. Primary and accent colors
4. Expression and mood
5. Pose
6. Clothing and accessories
7. Scene atmosphere
8. Parts that can be converted to wool felt
9. Parts that must be re-created from scratch

Conversion rules:

- Simplify complex structures into rounded body shapes.
- Turn real fur into short-pile wool felt fibers.
- Turn glossy materials into matte felt materials.
- Turn large scenes into tabletop miniature sets.
- Turn high-conflict plots into warm little moments.

---

### 4.3 User Already Has a Character Design

Keep the user's core design and fill in:

- Wool felt material
- Needle-felting texture
- Handmade edges
- Miniature scene
- Prop interaction
- Emotive actions
- Animatability for video

---

### 4.4 User Wants a Video

First determine whether the user wants:

- A 5-second single-image-to-video
- A 5-second multi-shot edit
- A 15-second short film
- A 30-second short film
- A 60-second short film
- A longer series of videos

If the user just says "make a video," default to the 5-second single-shot micro-story version first.

---

## 5. Standard Workflow

### Step 1: Requirement Understanding

Identify:

- What the user wants to make: character image / scene image / image series / first frame / 5-second video / long video
- Whether there is a reference image
- What the subject is
- What the mood is
- What it will be used for
- What the aspect ratio is

Default aspect ratios:

- Character assets: 1:1
- Short-video first frames: 9:16
- Landscape stories: 16:9
- Xiaohongshu covers: 3:4 or 4:5
- Image series: one unified ratio

---

### Step 2: Creative Directions

If the user has not set anything specific, output 3-5 directions.

---

### Step 3: Asset Planning

Assets fall into:

1. Character assets
2. Scene assets
3. Prop assets
4. Character state assets
5. First-frame assets
6. Video shot assets

---

### Step 4: Image Prompts

Output:

- Character image prompts
- Scene image prompts
- Prop image prompts
- First-frame image prompts
- Image series prompts
- Negative prompts

---

### Step 5: Storyboard Design

If the user wants video, storyboard first.

For 5 seconds, use 1 shot, or an edit of 2-3 shots.\
For 15 seconds, 3 five-second shots are recommended.\
For 30 seconds, 6 five-second shots are recommended.\
For 60 seconds, 10-12 five-second shots are recommended.

---

### Step 6: Video Prompts

Every video prompt must include:

- First-frame or asset reference
- Character lock
- Material lock
- Scene lock
- Action control
- Camera movement control
- Timeline
- Negative constraints
- Review checkpoints

---

### Step 7: Editing and Sound

Output:

- Editing rhythm
- Transition style
- Subtitle style
- Sound effect cues
- BGM mood
- Review checklist

---

## 6. Asset Planning Rules

### 6.1 Character Assets

Characters must have:

- Rounded body shapes
- Big-head-small-body or short-and-chubby proportions
- Short arms and short legs
- Simple facial features
- Gentle expressions
- Visible short-pile wool fibers
- Subtle needle-felting puncture texture
- Imperfect handmade edges
- Matte felt surface
- Clean and soft, never dirty or messy

Recommended characters:

- Bunny
- Bear
- Fox
- Cat
- Puppy
- Fawn
- Penguin
- Lamb
- Bird
- Mushroom person
- Little cloud
- Little star sprite
- Little monster
- Holiday dolls
- Anthropomorphized food characters

---

### 6.2 Scene Assets

Scenes must be a "tiny little world," not a large scene.
Recommended scenes:

- Miniature forest
- Little wooden cabin
- Warm-lit bedroom
- Tabletop kitchen
- Windowside on a snowy night
- Garden corner
- Little mushroom house
- Pile of holiday gifts
- Bedside night light
- Tiny world beside a teacup
- Cotton-ball cloud sky
- Mini theater with a cardboard backdrop
- Wooden tabletop model scene

Scene keywords:

- Miniature model scene
- Tiny little world
- Tabletop set
- Handmade set
- Warm yellow lighting
- Shallow depth of field
- Macro photography
- Soft background blur
- Warm fairy-tale feel
- Clean, soft, quiet

---

### 6.3 Prop Assets

Props should be small, soft, warm, and interactive.

Recommended props:

- Little star
- Little moon
- Little scarf
- Little hat
- Little bell
- Little gift box
- Little mushroom
- Little flower
- Little cup
- Little cookie
- Little envelope
- Little candle
- Little string of lights
- Little blanket
- Little snowman
- Little paper boat

---

## 7. Image Prompt Rules

### 7.1 Must Include

A complete image prompt must include:

 1. Subject
 2. Wool felt material
 3. Fuzzy fibers
 4. Needle-felted texture
 5. Handmade imperfect edges
 6. Matte surface
 7. Rounded proportions
 8. Expression and emotion
 9. Miniature scene
10. Warm light
11. Shallow depth of field
12. Composition and proportions
13. Negative prompt

---

### 7.2 Material Reinforcement Phrasing

Chinese reinforcement keywords:

- Real handmade wool felt doll
- Fine, dense short fuzzy fibers
- Needle-punched felting texture
- Visible handmade needle-felting marks
- Matte felt surface
- Soft, slightly rough texture
- Slightly irregular edges
- Handmade feel, not perfectly symmetrical
- Warm handcrafted texture
- Clean, soft, fuzzy surface

English reinforcement keywords:

- handmade wool felt doll
- needle felted texture
- visible tiny wool fibers
- soft fuzzy felt surface
- matte wool material
- subtle needle-punched marks
- slightly uneven handmade edges
- clean fluffy fibers
- handcrafted miniature doll
- cozy handmade texture

---

### 7.3 Phrasing to Avoid a Plastic Look

Must include:

- Not a plastic toy
- No smooth, glossy, reflective surfaces
- No resin figurine look
- No blind-box toy look
- No generic 3D cartoon look
- Material is matte wool felt
- Surface has fibers, not smooth skin

---

## 8. Video Rhythm Rules

### 8.1 Core Rhythm

A felt doll video is neither completely static nor fast-paced animation; it is:

**Gentle slow pacing + micro-movements + small rhythm beats + steady shots + soft cuts.**

The frame should feel like a small handmade wool felt world being gently awakened. Character movements must be light and camera movements must be steady, but every shot still needs a clear rhythmic change to avoid becoming a static display.

---

### 8.2 5-Second Video Rhythm

A 5-second video must be broken into 3-5 small rhythm beats.

| Time | Content | Purpose |
|------|---------|---------|
| 0-1 sec | Steady display of the character and scene | Establish the frame |
| 1-2 sec | First light movement: blink, ear twitch, head lowered | Bring the character to life |
| 2-3.5 sec | Second light movement: hugging a prop, waving, nodding | Build emotion |
| 3.5-4.5 sec | Environmental response: lights come on, snow falls, stars twinkle | Add visual change |
| 4.5-5 sec | Hold on a cute expression or warm pose | Make looping and editing easier |

---

### 8.3 Three Modes for 5 Seconds

Mode A: Single shot with light movements

Suited for character showcases, animated avatars, and first-frame motion effects.

Characteristics:

- One continuous shot throughout
- Fixed camera or extremely slow push-in
- The character makes only 1-2 light movements
- Stable frame, suitable for looping

---

Mode B: Single-shot micro story

Suited for children's stories and the openings of healing short videos.

Characteristics:

- No cuts
- But small events happen within the frame
- Props or the environment take part in the story

Example:

- The little bunny sees a star
- The little bunny gently hugs the star
- The star gives off a warm glow
- The little bunny blinks happily

---

Mode C: Multi-shot edited 5-second version

Suited for more rhythmic short-video covers, holiday greetings, and ad openings.

It is recommended to generate 2-3 separate shots and then edit them together in post.

| Shot | Duration | Visual |
|------|----------|--------|
| 1 | 1 sec | Prop close-up: felt star glowing |
| 2 | 2.5 sec | Medium shot of the character: little fox hugging the star |
| 3 | 1.5 sec | Close shot of the character: looks up and smiles as the warm light comes on |

Note: When the image-to-video model is unstable, do not force multiple cuts within a single prompt. The more reliable approach is to generate each shot separately and then edit them together.

---

## 9. Long-Video Storyboard Rules

### 9.1 15-Second Structure

A 15-second video should be split into three 5-second shots.

| Shot | Duration | Content |
|------|----------|---------|
| 1 | 5 sec | Establish the scene: the character appears in a miniature world |
| 2 | 5 sec | Character interacts with a prop: discovering, approaching, hugging, handing over |
| 3 | 5 sec | Emotional payoff: lights come on, the character smiles, a caption appears |

---

### 9.2 30-Second Structure

| Segment | Duration | Content |
|---------|----------|---------|
| Opening | 0-5 sec | Show the miniature scene and the character |
| Discovery | 5-10 sec | The character spots a small prop or a small problem |
| Attempt | 10-15 sec | The character gently approaches, touches, or hugs it |
| Response | 15-20 sec | The prop glows and the environment changes |
| Emotion | 20-25 sec | The character shows happiness, reassurance, or a sense of being accompanied |
| Wrap-up | 25-30 sec | Hold on a warm frame; a caption may be added |

---

### 9.3 60-Second Structure

| Segment | Duration | Content |
|---------|----------|---------|
| 1 | 0-10 sec | Establish the character and the world |
| 2 | 10-20 sec | A little wish or little problem appears |
| 3 | 20-30 sec | The character tries to solve it |
| 4 | 30-40 sec | A prop or companion brings help |
| 5 | 40-50 sec | The scene turns warm and the emotion is released |
| 6 | 50-60 sec | The character looks toward the camera, completing a blessing or healing message |

Long videos don't need strong conflict; the focus is on "a small problem being gently solved."

---

## 10. Camera Movement and Cutting Rules

### 10.1 Recommended Camera Movements

- Fixed camera position
- Extremely slow push-in
- Extremely slow lateral tracking
- Slight high-angle shot
- Macro close-up
- Gentle move from the prop to the character
- Slow push-in from the warm background light to the character's face

### 10.2 Forbidden Camera Movements

- Fast orbiting
- Large sweeping pans
- Handheld shake
- Fast zooming
- Follow shots of running
- High-speed fly-throughs of the scene

### 10.3 Recommended Cuts

- Character wide shot → prop close-up
- Prop close-up → character close shot
- Character profile → character front view
- Empty scene shot → character appears
- Close-up of hands hugging a prop → close shot of the character's expression
- Lights come on → character smiles
- Snowflakes / starlight / petals close-up → character reaction

### 10.4 Forbidden Cuts

- Rapid flash cuts
- Shaky transitions
- Glitch transitions
- Large rotating shots
- Fast push-in/pull-out shots
- Action-movie-style editing
- Complex continuous movement

---

## 11. Video Action Library

### 11.1 Light Character Movements

- Blinking
- Nodding
- Ears twitching gently
- Tail swaying gently
- A little wave of the hand
- Body swaying gently
- Looking down at a prop
- Looking up at the camera
- Hugging the little star tight
- Touching the scarf
- Gently moving closer to the gift box

### 11.2 Environment Actions

- Warm light softly coming on
- Little string lights twinkling faintly
- Snowflakes falling slowly
- Stars giving off a soft glow
- Petals drifting gently by
- Little paper boat rocking gently
- Moonlight outside the window softening
- Background light spots drifting slowly

### 11.3 Forbidden Actions

- Running
- Jumping
- Large turns
- Fast waving
- Exaggerated expressions
- Fighting
- Falling down
- Talking with a wide-open mouth
- Realistic animal-style movement
- Limb stretching and deformation

---

## 12. Editing and Sound Suggestions

### 12.1 Editing Rhythm

- A 5-second single shot can be used directly.
- For 15 seconds, 3 shots are recommended, with soft fades between shots.
- For 30 seconds, 6 shots are recommended, each carrying one emotional action.
- For 60 seconds, 10-12 shots are recommended, keeping 2-3 environmental empty shots.
- No fast cuts, no jarring transitions.

### 12.2 Caption Style

Captions should be short, gentle, and sound like picture-book narration.

Examples:

- You've worked hard today too.
- Even a little warmth can shine.
- Good night — remember to give yourself a hug.
- Winter is cold, but you're not alone.
- It saved the star for you.

### 12.3 Sound Effects

Recommended:

- Soft fabric rustling
- Soft little footsteps
- Little bell chimes
- Distant wind chimes
- Little wooden cabin ambience
- The faint sound of falling snow
- The soft tinkle of little string lights
- The sound of small pieces of paper flipping

Avoid:

- Screaming
- Jump-scare sound effects
- Mechanical noise
- Strong drumbeats
- High-pitched piercing sounds
- Exaggerated cartoon sound effects

### 12.4 BGM

Recommended:

- Xylophone
- Music box
- Soft piano
- Acoustic guitar
- Warm string pads
- Light music with a children's picture-book feel
- Light holiday bell music
- Bedtime-story ambient music

BGM prompt:

```text
A warm, healing music box melody with soft piano and xylophone accents, slow tempo, as quiet as a bedtime story, with a fairy-tale feel and a sense of companionship; no strong drumbeats, nothing sad, nothing tense.
```

---

## 13. Standard Output Format

Each time this Skill is executed, output according to the level of the user's needs.
### 13.1 Ideation Stage Output

```markdown
# Healing-Style Felt Plush Toy Creative Direction

## Requirements Understanding
- User goal:
- Visual type:
- Mood direction:
- Reference images available:

## Creative Directions
| Direction | Character | Scene | Props | Emotion | Suitable Video Motion |
|---|---|---|---|---|---|
```

### 13.2 Asset Stage Output

```markdown
# Asset Planning

## Character Assets
| Asset Name | Appearance | Material | Expression | Pose | Purpose |
|---|---|---|---|---|---|

## Scene Assets
| Asset Name | Scene | Lighting | Props | Atmosphere | Purpose |
|---|---|---|---|---|---|

## Prop Assets
| Asset Name | Material | Color | Function | Interactive (Yes/No) |
|---|---|---|---|---|
```

### 13.3 Video Stage Output

```markdown
# Video Production Plan

## Story Pacing

## Storyboard Table
| Shot | Duration | Visual | Action | Camera Movement | Lighting | Sound Effects | Emotion |
|---|---|---|---|---|---|---|---|

## Per-Shot Video Prompts

## Editing Suggestions

## Review Checklist
```

---

## 14. Review Checklist

### 14.1 Material Review

- Does it look like wool felt?
- Does it have fine, dense fibers?
- Does it show needle-felting texture?
- Is it matte?
- Do the edges have slight handmade imperfections?
- Are plastic reflections avoided?
- Is the resin-figurine look avoided?
- Is the generic 3D-animation look avoided?

### 14.2 Character Review

- Is it round and cute?
- Are the facial features simple and clean?
- Is the expression warm and comforting?
- Does it feel like a creepy doll?
- Are there overly realistic glass eyes?
- Is there any dirty or messy fur?
- Has it turned into a real animal?
- Are the proportions distorted?

### 14.3 Scene Review

- Does it look like a tiny miniature model?
- Is there warm lighting?
- Is there shallow depth of field?
- Is it clean and soft?
- Does it feel like a tiny little world?
- Are the props proportionate to the character?
- Is the scene too empty?
- Is the scene too cluttered?

### 14.4 Video Review

- Does the character stay consistent with the first frame?
- Are the motions gentle enough?
- Are there no large movements?
- Is the camera stable?
- Are there no material changes?
- Do no strange new objects appear?
- Is there no character deformation?
- Is it suitable for looping?
- Is the mood warm and calm?