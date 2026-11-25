---
name: sitcom-script-writer
description: "Sitcom: create sitcoms in the style of Friends and The Big Bang Theory."
---

## I. Analysis Framework (Three Pillars; see Sections III/IV/V for details)

**1. Essence of the Style**: Humor relies on **sharp dialogue + situational misunderstandings + live reactions**, not visual gags; stage-play + multi-camera studio shooting with a live audience tradition; slightly exaggerated acting, a beat after each punchline waiting for laughter, never breaking the fourth wall.

**2. Visuals & Sound**: Bright, warm-leaning, lightly oversaturated TV texture; **high-key flat lighting, almost no shadows, entire set visible**; fixed main sets (living room sofa / bar counter / dining table) + frontal proscenium framing; uniform-style outfits that reveal personality at a glance; multi-camera medium-wide shots, steady, cutting between "speaking ↔ reaction" via editing; **live audience / canned laughter** is the identity marker and sets the rhythm.

**3. Plot (one joke all the way through, three beats)**: Setup (normal situation) → Turn (absurd line / misunderstanding / escalation) → Landing (punchline, ending on **reaction + laughter**). One punchline per segment; pick one engine (escalation / misunderstanding / anticlimax / cringe); trim to two people — the chaos-maker + the normal person (straight man), with the humor rooted in "how the normal person reacts".

---

## II. Workflow

### Step 1 · Preliminary Confirmation (Finalize all configurations before entering Step 2)

All configurations requiring user selection **must be fully confirmed before generating characters/scenes** — character turnaround sheets and scene images consume compute to generate and bind, and once a configuration is changed, all prior assets are wasted; in particular, **aspect ratio is determined by the distribution platform and must be decided first**, otherwise the turnaround sheet/scene image compositions must be redone. Compress into **2 rounds** of `ask_user_input` (each round ≤3 questions, all with defaults and a "you decide for me" escape hatch); don't interrogate in a chain; if the user says "you decide everything," run through with defaults in one pass.

**First, triage the entry point:**

- **A. From scratch (most common)** — No characters/scenes/jokes/references → proceed with two confirmation rounds + guided joke development.
- **B. Existing idea** — User provides a one-line idea → only fill in missing configurations, don't re-ask known items; infer the humor engine from the idea, don't ask.
- **C. Reverse-engineer from reference video** — First run the Section VI frame-extraction script to read the three beats/art style/camera positions, then produce a matching piece; for configurations visible from the video (aspect ratio/duration/language), carry them over directly, only fill in what's missing.

**Round 1 · Set the Framework (3 questions):**

1. **Purpose + distribution platform → aspect ratio & tone**: Vertical 9:16 (Douyin/TikTok/Reels, default) | Landscape 16:9 (YouTube/official site/horizontal) | Square 1:1. Purpose (pure comedy / brand placement / character IP / product promotion…) only affects tonal weight, not the art style.
2. **Duration**: 15s / 30s / 60s / custom. **Generation uses 15s as one segment**; over 15s, split into multiple segments, each an independent continuous prompt (≈3-4 shots), sharing the same character/scene bindings and style-lock sentences; generate segment by segment then edit for continuity: 15s=1 segment, 30s=2 segments, 60s=4 segments, custom rounds to nearest 15s. **Every 15s is a complete joke** (its own three beats + punchline + laughter), tightly paced; 30s/60s = the same pair of characters/scene delivering 2/4 consecutive mini-skits, each with its own landing — don't stretch one joke too long (dragging it out is awkward).
3. **Humor engine**: Escalation / misunderstanding / anticlimax / cringe (**only ask in "from scratch"; infer from the idea in "existing idea"**).

**Round 2 · Set Language & Presentation (2 questions):** 4. **Dialogue language**: English (default, best matches American sitcom lip-sync) / Chinese. Write into the generation prompt. 5. **Subtitle language**: Bilingual (default, Chinese on top, English below) / Chinese / English. **Subtitles are only burned in during post-production editing, not written into the generation prompt** (see Step 7).

**Production method is fixed as image-to-video** (this skill has already generated turnaround sheets + scene images for binding, no longer asked): include the bound images during generation; the prompt focuses on camera movement / blocking / actions / dialogue / cuts, leaving appearance and set dressing to the reference images.

**Narration**: Default **off** (rarely used in sitcoms, only for single-camera); enable only if the user explicitly requests it; when enabled, add voiceover without affecting the rest of the workflow.

**Segmented generation pace** (only ask when &gt;15s): **Generate all segments at once** / **Confirm segment by segment** (generate one segment, then generate the next once satisfied — more stable but slower). Default is segment-by-segment confirmation.

After two rounds of confirmation → for "from scratch," further guide joke development: one round offering ① setting (living room / bar / dining table / office) ② the duo's personalities; based on this, pick/adapt a **one-line premise** from the Section IV idea library + assign {{Mixed N}}; once confirmed, proceed to Step 2.

### Step 2 · Define Characters & Scenes (Turnaround Sheets + Scene Image)

**First, do casting guidance (two questions, via** `ask_user_input` **multiple choice, with a "you decide for me" escape hatch):**

1. **How many characters**: 1 / 2 / 3 / custom. Sitcom skits **recommend 2 people** (chaos-maker + normal person/straight man), but follow the user's choice; with more characters, still designate one "normal person" responsible for reactions.
2. **Which persona for each character (including nationality)**: Confirm one by one ① persona archetype (see Section III styling menu: neat nerd type / sloppy slacker type / confident flamboyant type / sharp-tongued cool girl…) ② **nationality/ethnicity** (e.g., American, Asian/Chinese, Japanese, Korean, Latino, African, European…, **open choice, Asian equally applicable**). Can be one question per character or merged into a single round.

**Then determine character source (choose one):**

- ① User **uploads their own photos** → bind directly to the corresponding {{Mixed N}}, **skip turnaround sheet generation**, uploaded images take precedence.
- ② No images → generate turnaround sheet reference images per the template below, then bind (write the chosen persona + nationality into the appearance description).

**Then translate to tokens and reference images:**

- One token per character: `{{Mixed 1}}` (chaos-maker), `{{Mixed 2}}` (normal person/straight man)…. First appearance writes full appearance (including nationality/ethnic features + uniform-style signature outfit); afterward use only the token, writing only actions/expressions; for interactions, clearly specify who's primary and secondary.
- **(When no upload) produce one turnaround sheet per character** (layout: **one large close-up of front-facing face on the left, side-by-side full-body front + full-body back on the right**, unified styling, clean light-colored background), used as the {{Mixed N}} binding reference for Seedance — this keeps characters stable and consistent across shots. Turnaround sheets are rendered in **this style's high-key flat lighting, bright clean TV texture** (not Japanese-drama warm film tones); template and examples in Section III "Turnaround Reference Images". Archetype menu in Section III.
- **Then produce one scene image of the fixed main set** (empty establishing shot, frontal proscenium, high-key flat lighting), used as the scene/background binding reference for Seedance, ensuring **the same set stays consistent** across shots. Scene menu and template in Section III "Scene Image Reference".

### Step 3 · Design the Joke

Follow the "plot content" framework (Section IV): map the three beats onto numbered shots, pick one engine from the four types, apply the "chaos-maker + normal person" duo.

### Step 4 · Apply Visual & Audio Elements

Complete per the framework (Section III): bright high-key flat lighting, almost no shadows + warm lightly oversaturated TV texture + fixed main set with frontal proscenium + uniform-style outfits + multi-camera medium-wide shots, cutting between speaking/reaction + closing canned laughter beat.

### Step 5 · Output in Seedance 2.0 Format
Follow the Section 5 format: Chinese style-lock sentence + global settings → numbered shot breakdown under "Strictly follow the order of \[N\] shots:" (shot sizes, including {{Mixed N}}, use `【CUT】` to cut to reaction shots) → Chinese closing sentence. **Write the prompt in Chinese (you can read it directly); keep dialogue in the original text of the chosen language; explicitly state "no subtitles or on-screen text"—subtitles must never enter generation**. List subtitles separately in an appended "Subtitle List" (burned in at Step 7). Wrap the prompt in a code block. **When the duration &gt;15s, split it into 15s segments, outputting one prompt per segment (Segment 1/Segment 2… each in its own code block) + the corresponding subtitle list**, sharing the character/scene bindings and the style-lock sentence, **each segment forming its own joke and landing its own punchline**.

### Step 6 · After Confirmation, Generate on the Platform Canvas

Once the prompt (in Chinese) is ready, **first make sure the user understands the content, then ask if it's OK or not**:

- Not OK → revise according to the feedback (change the dialogue/engine/styling/language, etc.), then deliver another version.
- OK → generate on the **platform canvas** (each segment with its bound character three-view sheets/uploaded images + scene image), **following the pace chosen in Step 1**: generate all segments in one go / confirm segment by segment (each segment approved before generating the next); finally, edit the segments together in order.

### Step 7 · Add Subtitles After Generation (Required for the Final Video; Subtitles Appear Only at This Step)

After the platform delivers the video (with no subtitles/on-screen text at all), **the final video must carry subtitles**—burn in the chosen **subtitle language (Chinese/English/bilingual) during editing; this is the only** step where subtitles are added and it must not be skipped:

- Use the **subtitle list** attached in Step 5 to add subtitles sentence by sentence, following each shot's dialogue timeline, placing TV-style subtitles **centered at the bottom** in **white text with a thin black outline**. Bilingual = Chinese on top, English below, with the **English line noticeably smaller than the Chinese line** (Chinese primary, English secondary).
- Fine-tune the wording with a comedic ear; the punchline line must be funny in the selected language(s).
- Since text was already banned at the generation stage (`No subtitles or on-screen text`), the footage is clean, so just add the subtitles in editing.
- At this step you can also layer in standard canned laughter/heckling sounds to steady the rhythm (see Section 3 "Sound Effects").

---

## 3. Detailed Visual and Sound Elements (Including {{Mixed N}}, Three-View Sheets, and the Prototype Menu)

Always maintain: bright high-key flat lighting, almost no shadows, a warm-toned slightly-oversaturated television look, and multi-camera medium-wide framing.

### {{Mixed N}} Character Anchors

- One token per character (`{{Mixed 1}}`, `{{Mixed 2}}`), with bound reference images kept consistent.
- On first appearance, write the **full appearance** (hairstyle + uniform-style signature outfit + accessories); afterwards use only the token and describe only actions/expressions.
- In interactions, make subject and object explicit: `{{Mixed 1}} proudly announces the news to {{Mixed 2}}`.

### Three-View Reference Sheets (For {{Mixed N}} Binding)

Once the characters are set, first generate a three-view character sheet for each {{Mixed N}} to serve as the Seedance binding reference image, ensuring faces don't drift across multiple shots. **Fixed layout**: one large front-facing headshot close-up on the left, with a full-body front view + full-body back view side by side on the right. **Render in this style** (high-key flat lighting, bright clean television look), not the warm film tones of Japanese dramas, otherwise the color grade will bleed into the final video.

Template (EN, one character per image):

```
Character reference sheet of one single character on a clean light seamless background, composed
as three panels: a large close-up head-and-shoulders portrait on the LEFT, then a full-body front
view and a full-body back view side by side on the RIGHT. Same outfit, same proportions, neutral
standing pose, gentle natural expression. [Appearance: nationality/ethnicity + hairstyle and hair color + uniform-style signature outfit + accessories]. Bright high-key
even lighting with minimal shadows, clean glossy television look, consistent character design,
no props.
```

Template (ZH):

```
单个角色的角色设定图，纯净浅色无缝背景，三栏构图：左侧一张大的头肩特写正脸，右侧并排
全身正面 + 全身背面。同一套服装、同样身材比例、自然站姿、柔和自然表情。[外观：国籍/族裔 + 发型发色 +
制服化标志装 + 配饰]。明亮高调均匀布光、阴影极弱，干净有光泽的电视质感，角色设定一致，无道具。
```

Key points: layout = large front-facing headshot on the left + full-body front/back on the right; one character per image (for a duo, generate them separately to prevent face blending); the appearance description must stay **word-for-word identical** to how {{Mixed N}} first appears in the prompt; for the image tool, GPT Image-2 / Midjourney both work—once you have the sheet, bind it to the corresponding token.

### Scene Reference Image (For Fixed Main Scene Binding)

After the characters are set, generate a scene image for the **fixed main scene** as the background binding reference, keeping the set unchanged across multiple shots. By default, a **people-free establishing wide shot** (a clean backdrop is easy to reuse); when needed, you can also include {{Mixed N}} to produce an establishing frame with people in it. Take the scene content from the "Scene Setup" menu below (living room / bar counter / dining table / office), rendered in this style: frontal proscenium staging, high-key flat lighting, warm-toned television look. **The aspect ratio must match the publishing scenario chosen in Step 1** (vertical 9:16 / horizontal 16:9 / square 1:1), otherwise the composition will be wrong after binding.

Template (EN, append `vertical 9:16 / 16:9 / 1:1 aspect ratio` at the end as needed):

```
Establishing wide shot of a classic multi-camera American sitcom set: [scene, e.g. a cozy lived-in
apartment living room with a big couch, warm lamps, a cluttered coffee table and a small kitchenette
in the back], no people. Frontal proscenium staging, bright high-key three-point lighting, soft even
illumination with minimal shadows, warm slightly-saturated colors, clean glossy television look,
[vertical 9:16 / 16:9 / 1:1] aspect ratio.
```

Template (ZH):

```
经典美式多机位情景喜剧布景的全景定场镜头：[场景，如 温馨有生活感的公寓客厅，大沙发、暖色台灯、
杂物茶几，后景小厨房]，画面无人。正面镜框式舞台调度，明亮高调三点布光、柔和均匀、阴影极弱，
```
Warm tones with slight high saturation, clean glossy television look, [vertical 9:16 / horizontal 16:9 / square 1:1] aspect ratio.
```

Key points: empty by default, frontal framing, same art style as the final video (high-key flat lighting, warm tones), **same aspect ratio**; one main scene image per sketch; the scene description must be **word-for-word identical** to the global settings in the video prompt; once obtained, bind it as the scene reference.

### Color and Texture

- Bright, warm-leaning, slightly high saturation; clean glossy television look, not photorealistic.
- Generation prompt: `bright high-key, warm slightly-saturated colors, clean glossy television look`.
- Avoid: cinematic low-key shadows, documentary desaturated greenish tones, film grain (those are other styles).

### Lighting and Atmosphere (Fixed principle: high-key flat lighting, almost no shadows)

- Even three-point lighting `high-key three-point lighting`, low contrast `soft even illumination`.
- `minimal shadows / everything clearly visible`—serves multi-camera shooting from any angle, nothing hidden in shadow.
- Overall bright, warm, safe and relaxed, **no** dramatic light-and-dark contrast.

### Set Design (Fixed main scene, frontal framing)

- Living room: large sofa, warm table lamp, cluttered coffee table, visible lived-in home details.
- Bar / café: fixed bar counter, booths, neon signs, regulars' seats.
- Dining table / kitchen: dining table, open kitchen, serving path.
- Office (studio version): conference table, cubicles, break area—**note**: keep the high-key flat lighting, don't slide into mockumentary fluorescent cold light.
- Always `frontal proscenium staging`, `shot on a studio set`; the scene recurs and becomes familiar to the audience.
- **Background extras** (to enhance the American sitcom live feel): bar patrons/office coworkers/restaurant diners etc., doing only **low-key ambient activity** (drinking, typing, walking past), **not interacting with the leads, not looking at the camera, not stealing the scene, minimal movement**, to avoid interfering with the "speaker↔reaction" cutting (for English wording see the skeleton optionals).

### Character Looks (Uniformized, personality readable at a glance)

When pairing the "Chaos Maker + Straight Man" duo, pick two with strong contrast:

Type Look key points (signature outfit, almost never changed) Tidy Bookworm Neat cardigan/plaid shirt, glasses, tidy hair, earnest and reserved Scruffy Slacker Oversized hoodie, messy bun, slippers, deadpan Confident Show-off Bright shirt, flashy accessories, slicked-back hair, flamboyant posture Plain Nice Guy Everyday T-shirt and jeans, friendly and casual Stiff Office Type Suit/business attire, briefcase, tense expression Drama Queen Fashionista Flamboyant fashion, sunglasses, always performing Geeky Homebody Cartoon print tee, track jacket, lost in his own world Sharp-Tongued Cool Girl Sharp outfit, arms crossed, always ready with a jab

- Meaning of the signature outfit: instantly readable + reinforces the archetype, so the same character's outfit basically never changes.
- **Nationality/ethnicity and character archetype are two different things**: the archetype (nerd/sarcastic…) is picked from this menu; nationality/ethnicity (American/Asian/Japanese/Latino…) is asked separately in Step 2; combine both into the character's appearance.
- Skin texture can be omitted or written as `natural healthy skin under bright studio light`; no need to chase porcelain airbrushing.

### Camera Language

- Camera positions: **primarily multi-camera medium and wide shots** `medium and wide shots`, stable `stable framing`, frontal audience perspective; no flashy camera moves, no handheld, no fast push-ins.
- Cutting: rely on editing to cut between "the speaker ↔ the reactor"—`Cut to Medium Shot` / `Cut to Reaction Close-up` / `Static Two-Shot`.

### Sound and SFX (This genre's identity marker)

- **Live audience/canned laughter**: always present at the punchline, cueing when to laugh and setting the rhythm.
- **Tight, not dragged**: laughter starts almost immediately once the punchline lands (nearly on the same beat as the reaction), leaving only a very short beat; don't let it take too long to kick in (dragging kills the moment).
- **Write the pause into the performance**: deliver the joke → very short beat → laughter immediately → wrap up.
- Whooping/cheering: for kisses, twists, flirtatious moments.
- Seedance generates audio and video together, but the laughter's "cleanliness" is unstable; it's safer to layer standard canned laughter/whooping in editing.

---

## 4. Story Content Refinement (One Joke All the Way Through)

The humor lies in contrast and timing, not in piling on material or in the story. **Each 15s segment carries only one joke**; the single-episode skeleton is unnecessary (no cold open, no A-plot/B-plot, no end tag needed). First think through "why would the straight man react this way," then write the shots. **One complete joke per 15s**, with the three beats landing the punchline + laughter right away—keep the pacing tight (dragging gets awkward); 30s/60s = the same pair of characters in the same scene rattling off 2/4 small bits in a row, each one landing its own punchline.

### Three-Beat Structure (Spread Across Multiple Numbered Shots)

```
Setup  About the first 1/3: establish a normal situation, made clear in a line or two / one action (medium-wide shot, normal acting)
Turn   Middle: one absurd line / one misunderstanding / one escalation (cut to the speaker / the person things happen to)
Land   Final 1/3: punchline, cut back to the straight man's reaction + a one-beat pause + canned laughter
```

> Golden rule: the more normal the setup + the more absurd the turn + the more restrained the reaction = the funnier. The punchline almost always lands on "the straight man's face," not on the chaos itself.

### Story Structure

- Minimalist: one short video carries only one joke.
- Master template: "A straight man and a chaos maker have one misalignment in a familiar setting."

### Four Types of Joke Engines (Pick One)

- **Escalation**—a small thing suddenly spirals out of control. Example: "I just moved it a little" → the camera pans over to utter devastation.
- **Misunderstanding**—the two have asymmetric information and talk past each other. Example: A announces good news; B hears it entirely as bad news.
- **Anticlimax**—built up grandly, deflated in one stroke. Example: solemnly presenting the "feast" → it's a charred lump → silence at the whole table.
- **Cringe**—the deathly silence after saying the wrong thing. Example: A tries to compliment B → the more A says, the worse it gets → no one responds.

> Closing technique: cut to the straight man's (reactor's) reaction + pause + canned laughter. **Do not** use a glance at the camera / deadpan to camera (that's mockumentary); use reaction pauses, use freeze frames sparingly.

### Character Relationships

- Keep it to **two people**: one **chaos maker** (says/does absurd things) + one **straight man/reactor** (in charge of reacting).
- The humor almost always grows out of "how the straight man reacts."
- Long-term relationship backdrops can be borrowed (long-lost family / romantic tension / boss × subordinate), but one short video only plays out **one moment of chemistry between this pair**—no relationship arcs.

### Joke Idea Bank (Throw Out / Adapt Directly When Guiding From-Zero Users)

Pick one by "scene × engine" and adapt it into a concrete premise (just swap the characters/lines); if no scene was chosen, recommend one at random.

**Living Room Sofa**

- Misunderstanding: A excitedly announces great news → [CUT] B completely mishears it as the sky falling, hugging a pillow and sobbing → [CUT BACK] A's smile freezes into confusion → silence + laughter.
- Escalation: A calmly says "I just tidied up a little" → [CUT] the camera pans over to a living room in total chaos → B's expression freezes.

**Bar / Café**

- Cringe: A confidently strikes up conversation across the bar → [CUT] the other person replies with something that makes A die inside → [CUT BACK] A frozen in place, glass raised → laughter.
- Anticlimax: A says mysteriously, "I have a brilliant plan" → [CUT] the next beat, the plan falls apart on the spot → B drinks coffee expressionlessly.
**Dining Table / Kitchen**

- Anticlimax: A solemnly lifts the cloche and announces "a surprise feast" →【CUT】it's a charred lump →【CUT BACK】dead silence at the table → A forces a smile + laughter.
- Misunderstanding: A says "I made your favorite" →【CUT】out comes the dish B hates most → B's polite fake smile gradually crumbles.

**Office (studio version, keep the high-key flat lighting)**

- Escalation: The boss instructs "just change one small thing" →【CUT】the subordinate takes it to mean scrapping and redoing the entire project, hauling in a stack of documents → the boss freezes.
- Cringe: A tries to kiss up in a meeting →【CUT】calls the boss by the wrong name →【CUT BACK】the whole room falls silent → A wants to crawl under the table + laughter.

Variant buttons: swap the setting, swap the duo's look, swap in absurd lines, escalate a single mismatch into "a misunderstanding wrapped inside another misunderstanding" (but still just one punchline).

---

## 5. Seedance 2.0 Output Format

The final deliverable = **one numbered shot-by-shot prompt in Chinese** (Seedance supports Chinese, so it's easy for you to read; **dialogue is kept verbatim in the chosen language** — if it's spoken in English, write the original English line), wrapped in a copyable code block.

### Standard Skeleton

In the generation prompt, **write only the dialogue for lip-sync — never any subtitles/on-screen text** — and explicitly include `no subtitles or on-screen text` (to prevent the model from generating random text of its own). Subtitles go in a separate list, burned in during Step 7 once the video is generated.

```
[Style-lock sentence]. [Global setup: fixed main set + high-key flat lighting with almost no shadows + warm TV texture + aspect ratio (vertical 9:16 / horizontal 16:9 / square 1:1, per Step 1)]. Dialogue spoken in [Chinese/English]; the frame contains no subtitles or on-screen text whatsoever. Characters' relative positions are fixed (who's left/right, who sits/stands); cuts never swap them. [Optional: a few low-key background extras each minding their own business, not interacting with the leads, not looking at the camera.]
Strictly follow the sequence of [N] shots:
1. [Shot size]: [Setup — a normal situation; on {{Mixed N}}'s first appearance write their full appearance and fix relative positions, e.g. "on the left / on the right"]. {{Mixed 1}} says the line in [chosen language]: "[original line]".
2. 【CUT】[Shot size]: [Turn]. {{Mixed 2}} says the line in [chosen language]: "[original line]".
3. 【CUT】Reaction close-up: [the straight man's reaction, amplified].
4. Static two-shot: [hold the reaction for a very short beat, then live studio-audience laughter immediately surges up (don't drag)].
[Closing sentence: natural acting, precise rhythm; no subtitles or on-screen text; stable multi-camera framing.]
```

Also attach a **subtitle list (for post-production burning, not included in the prompt)**, default bilingual with Chinese on top and English below:

```
Subtitle list (bilingual, Chinese on top, English below):
1. [CN line] / [EN line]
2. [CN line] / [EN line]
...
```

Key points:

- Numbered shots, each starting with the shot size; camera setups are mainly **medium/wide**, stable and frontal. **One segment per 15s, ≈3-4 shots per segment**; 30s = 2 segments, 60s = 4 segments, each as its own prompt (see Step 1).
- Use `【CUT】` for shot transitions; the core rhythm is cutting between **the speaker ↔ the reactor**.
- **Position lock**: within a bit, the characters' relative positions (who's left/right, who sits/stands) are fixed from start to finish, and cuts never swap them (back-and-forth multi-camera cuts are the easiest way to break continuity); hard-code it in the first shot: "{{Mixed 1}} on the left, {{Mixed 2}} on the right, unchanged throughout."
- Characters use `{{Mixed N}}`: write full appearance on first appearance, then only actions/expressions.
- **Dialogue goes into the prompt and is kept verbatim in the chosen language; subtitles do not go into the prompt** (explicitly "no subtitles or on-screen text"); subtitles go in a separate list and are burned in after the video is generated.
- Global must-haves: style-lock sentence, high-key flat lighting, **aspect ratio**, "no subtitles or on-screen text", closing sentence, and the punchline's "light live studio-audience laughter" with rhythm.

### Vocabulary (Chinese, with English fallback in parentheses)

- Shot sizes: establishing wide · two-shot medium · medium shot · reaction close-up · static extreme wide.
- Cuts: `【CUT】` (cut to reaction close-up / static two-shot).
- Acting: smug announcement · misreading the situation · expression freezing · deadpan blank face · forced fake smile · a one-beat pause.
- **Forbidden** (these belong to mockumentary): glances at the camera, handheld, snap zoom, interview shots.

### {{Mixed N}} Rules

One token per character, consistent throughout; in interactions, spell out who acts and who receives; for the duo use `{{Mixed 1}}` (the chaos-maker) + `{{Mixed 2}}` (the straight man / feed).

### Sound (canned laughter is the signature of this genre)

- **Laughter chases the punchline — no delay**: the moment the punchline lands, the laughter starts almost instantly (nearly on the same beat as the reaction); leave only a very short one-beat pause, and don't wait for the actors' reaction to dawdle before it hits — drag it out and the scene goes cold. Write in the prompt: "the instant the punchline lands, live studio-audience laughter surges up immediately."
- Crowd whoops (for twists / tension moments); Seedance's laughter "cleanliness" is unstable, so just indicate the beat in the prompt; standard laughter/whoops are layered on during editing.

### Dialogue & Subtitles (language selectable; subtitles always in post)

Default is **English dialogue + bilingual subtitles (Chinese on top, English below)**. **Subtitles must never appear at the generation stage; all of them are added and burned in during post-production editing after the video is generated (Step 7).**

- **Dialogue language (Chinese / English)** — determines lip-sync/voice; **even if the prompt is in Chinese, dialogue is kept verbatim in the chosen language** (if spoken in English, write the original English line in quotes). Write "{{Mixed 1}} says the line in English: …" or "says the line in Chinese: …".
- **Explicitly state "no subtitles or on-screen text" in the generation prompt** — proactively forbid the model from rendering any text (to guard against garbled/missing/blurry characters).
- **Subtitle language (Chinese/English/bilingual, default bilingual with Chinese on top and English below)** — only affects the **post-production subtitle list** (line by line, attached after the prompt, for burning in Step 7); it does not go into the prompt.
- Translation needn't be word-for-word; localize for comedic flow, and make sure the punchline line is funny in the chosen language.
- Post-production subtitle style (Step 7): bottom-centered, white text, thin black outline, TV-caption feel; bilingual = Chinese on top, English below, with **English one size smaller than Chinese** (Chinese primary, English secondary).

### Binding & Narration

- **Fixed image-to-video**: attach the three-view character sheet + scene image bindings; **the prompt focuses on camera moves / blocking / actions / dialogue / cuts**, leaving looks and set dressing to the reference images (the global setup matches the scene image verbatim).
- **Narration**: off by default. Only add voiceover when enabled (it also counts as dialogue; subtitles in post).

### Style Lock Block (Chinese, used verbatim as the style-lock sentence at generation time)

```
经典美式多机位情景喜剧风格，在现场观众前的摄影棚布景内拍摄。明亮高调三点布光，
柔和均匀、阴影极弱，暖调、轻微高饱和，干净有光泽的电视质感，全场清晰可见。
多机位中景与宽景稳定覆盖，正面镜框式舞台调度。落点处带轻微现场观众笑声。
```

> The example demonstrates the default combination (Chinese prompt + English dialogue): **no subtitles inside the prompt** (only dialogue + "no subtitles or on-screen text"); subtitles go in a separate list and are burned in after the video is generated.

### Example A · Misunderstanding (living-room sofa, Chinese prompt + English dialogue)

```
经典美式多机位情景喜剧风格，现场观众前摄影棚拍摄。明亮高调三点布光、柔和均匀、阴影极弱，暖调轻微高饱和，干净有光泽的电视质感。温馨有生活感的公寓客厅，大沙发、暖色台灯、杂物茶几。台词说英文，画面无任何字幕或屏幕文字。角色相对位置固定、切镜不互换。严格按 4 个镜头顺序：
1. 中景：整洁认真的男人 {{Mixed 1}}（开衫+眼镜，坐在沙发左侧）满脸兴奋，说英文台词："Babe, huge news — we're finally getting a puppy!"
```
2. 【CUT】Medium shot: {{Mixed 2}} on the right (messy bun, oversized hoodie, deadpan) completely misreads it, face full of terror, saying the English line: "A BABY?! We are NOT ready for a baby!"
3. 【CUT】Reaction close-up: {{Mixed 1}}'s smug smile freezes into confusion, quietly says "...a puppy."
4. Static two-shot: the two lock eyes, one beat of dead silence, {{Mixed 2}} slowly picks up the throw pillow, then the live-audience laughter immediately surges in (don't drag it out). Natural acting, precise timing; no subtitles or on-screen text; stable multi-camera framing.
```

Subtitle list (bilingual, Chinese on top / English on bottom, burned in during post-production):

```
1. Babe, huge news — we're finally getting a puppy! / Babe, huge news — we're finally getting a puppy!
2. A BABY?! We are NOT ready for a baby! / A BABY?! We are NOT ready for a baby!
3. ...a puppy. / ...a puppy.
```

### Example B · Anticlimax (dining table, Chinese prompt + English dialogue)

```
Classic American multi-camera sitcom style, shot on a studio stage in front of a live audience, bright high-key flat lighting, warm-toned TV texture. A lived-in open kitchen + dining table with candles lit. Dialogue is spoken in English; the frame has no subtitles or on-screen text. Positions fixed, cuts never swap them. Strictly follow the 4-shot sequence:
1. Medium shot: the host {{Mixed 1}}, wearing a floral apron, grandly lifts the silver cloche, saying the English line: "Behold — my masterpiece!"
2. 【CUT】Close-up: under the cloche is a charred, smoking lump.
3. 【CUT】Reaction two-shot: the two guests {{Mixed 2}} and {{Mixed 3}} stare in dead silence, forks frozen halfway up.
4. Static extreme wide shot: {{Mixed 1}} holds the smug fake smile for one beat, quietly says "...it was supposed to be chicken.", slowly puts the lid back on, then the live-audience laughter immediately surges in (don't drag it out). Natural acting; no subtitles; stable multi-camera framing.
```

Subtitle list (bilingual, Chinese on top / English on bottom, burned in during post-production):

```
1. Behold — my masterpiece! / Behold — my masterpiece!
2. ...it was supposed to be chicken. / ...it was supposed to be chicken.
```

### Example C · cringe (bar)

Same method: {{Mixed 1}} confidently delivers a pickup line at the bar → cut to {{Mixed 2}}, who without even looking up fires back a mortifying line → cut to a close-up of {{Mixed 1}} frozen in reaction + pause + laughter. The global section likewise carries "no subtitles or on-screen text," with the subtitle list attached separately.

### Output Checklist

- \[ \] **Pre-production config fully confirmed in Step 1** (purpose + posting scenario/aspect ratio, duration, laugh engine, dialogue language, subtitle language, narration, segment pacing) before moving into Step 2
- \[ \] Style-lock sentence + high-key flat lighting with almost no shadows + **aspect ratio (9:16/16:9/1:1)** + closing sentence
- \[ \] Numbered shots, mainly medium/wide sizes, cutting between "speaking ↔ reaction"
- \[ \] **Characters' relative positions locked** (left/right, sitting/standing fixed), cuts never swap them
- \[ \] Background extras (optional) low-key, no interaction / no looking at the camera / no scene-stealing
- \[ \] {{Mixed N}} fully described on first appearance (including nationality/ethnicity + signature uniform-style outfit), reused afterward, interaction subject/object clear; three-view sheet + scene image already generated and bound (same aspect ratio)
- \[ \] Three beats: normal setup → absurd twist → reaction + laughter ending
- \[ \] The joke lands with `subtle live-audience laughter`
- \[ \] Prompt written in Chinese, dialogue kept in the original of the chosen language; **the prompt includes "no subtitles or on-screen text," so no text of any kind gets generated**
- \[ \] Subtitles listed separately in a "Subtitle List" appended after the prompt, burned in only at Step 7 after the final video (default bilingual · Chinese on top / English on bottom)
- \[ \] Image-to-video: with bound images, prompt focuses on camera movement and action; narration off by default
- \[ \] **No** glances at the camera / handheld / crash zoom / interview shots
- \[ \] When the prompt is ready, ask the user for OK first; only after OK, take it to the platform canvas to generate
- \[ \] Single language throughout, code block copyable; duration per Step 1 selection, one laugh point; duo of "chaos × normal"
- \[ \] &gt;15s already split into 15s segments, each segment a self-contained laugh point landing its own punchline, sharing the bound assets

---

## 6. Reverse-Engineering the Reference Video (Frame-Extraction Script)

Used for Entry C: first extract frames to see the three beats and the cutting clearly, then write a prompt in the same style — don't describe footage you haven't watched out of thin air. Save the script below as `extract_frames.sh` and run it; usage: `./extract_frames.sh <video> [outdir]`. It reads the specs, extracts frames according to the pacing, assembles a contact sheet, and prompts you to judge: ① the three beats (setup / twist / reaction + laughter) ② how the cuts switch between "speaking ↔ reaction" and how wide the shot sizes are ③ whether the visual style is high-key flat lighting, warm-toned, almost shadowless, with a fixed main set (confirm it's a studio-shot sitcom rather than a mockumentary) ④ in the duo, who is the chaos-maker, who is the normal one, and their signature looks.

```bash
#!/usr/bin/env bash
# For reverse-engineering the reference video: read specs + extract frames + assemble a contact sheet, to see the three-beat and cutting rhythm clearly.
# Usage: ./extract_frames.sh <video> [outdir]
set -euo pipefail

VIDEO="${1:?Usage: extract_frames.sh <video> [outdir]}"
OUT="${2:-./refframes}"
mkdir -p "$OUT"

echo "=== Specs ==="
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=codec_type,codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=0 "$VIDEO"

DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO" | cut -d. -f1)
echo "=== Duration approx ${DUR}s, extracting frames by pacing ==="

# One frame every 1.5s for short clips; every 2.5s if the clip is too long
if [ "${DUR:-0}" -le 35 ]; then RATE="1/1.5"; else RATE="1/2.5"; fi
ffmpeg -v error -i "$VIDEO" -vf "fps=${RATE}" "$OUT/f_%03d.jpg"

# Assemble the contact sheet so the whole clip's pacing and cuts can be seen at a glance
if command -v montage >/dev/null 2>&1; then
  N=$(ls "$OUT"/f_*.jpg | wc -l)
  COLS=5; ROWS=$(( (N + COLS - 1) / COLS ))
montage "$OUT"/f_*.jpg -tile "${COLS}x${ROWS}" -geometry 320x180+2+2 \
    -background black "$OUT/contact.jpg"
  echo "contact sheet: $OUT/contact.jpg"
fi

echo "Done. Review contact.jpg to judge the three-beat structure / shot cuts / art style / duo (see above)."
echo "Locate exact frames: ffmpeg -ss <start> -i <video> -t <len> -vf fps=4 ..."
```

---

## 7. General Constraints

- **All upfront configuration is finalized in Step 1** (purpose + distribution platform/aspect ratio, duration, humor engine, dialogue language, subtitle language, narration, segment pacing), then move on to Step 2 to produce characters/scenes; compress into 2 rounds of selection, no chained follow-up questions.
- **Aspect ratio is determined by the distribution platform** (vertical 9:16 / horizontal 16:9 / square 1:1); three-view sheets (fixed layout), scene images, and final-video prompts all use the same aspect ratio.
- Deliver each prompt in a single primary language throughout, with a mirror attached when needed; wrap it in a copyable code block.
- Characters: **ask about the count first** (2 recommended), **then ask about each one's look + nationality/ethnicity** (open, including Asian); use {{Mixed N}}, write in full at first appearance (including nationality/ethnicity + uniform-style signature outfit), reuse thereafter, keep interaction subject/object clear; character images can be **user-uploaded photos** or generated three-view sheets—bind after choosing one of the two; for each skit, first produce a scene image of the fixed main scene and bind it.
- Multi-camera medium-wide shots, stable; cut between "speaking ↔ reaction"; **characters' relative positions are locked and never swapped**; **do not use** glances at the camera / handheld / crash zooms / interview setups.
- **One complete laugh point every 15s**, three-beat structure, closing lands on a reaction + laughter, tight pacing; 30s/60s = 2/4 short gags strung back-to-back, each landing once.
- **Write prompts in Chinese** (dialogue kept in the original selected language); **subtitles must never appear at the generation stage**—the prompt explicitly states "no subtitles or on-screen text"; subtitles go in a separate list and are burned in only during post-production editing.
- Only generate on the **platform canvas** after confirmation (with bound character/scene images); the background may include low-key extras (no interaction / no looking at the camera / no scene-stealing).
- Frequently pair a "chaos maker + normal person" duo.
- No content involving real public figures; keep it appropriately harmless.