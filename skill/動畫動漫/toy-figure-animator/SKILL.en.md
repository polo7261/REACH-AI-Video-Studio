---
name: toy-figure-animator
description: "Toy figure animation: no modeling needed—easily generate shorts in three styles: Japanese tokusatsu, art toys, and felt stop-motion."
---

# Figure Animation Short Video Generation Skill (Generic Edition)
 
## ⚠️ Highest-Priority Output Rules
 
Options are output only once and must not be printed repeatedly. All confirmation questions must be sent as separate messages, apart from the content above.
 
---
 
## Overall Workflow Overview
 
```
User uploads figure image/video
        ↓
[Step 1] Specs + background setting + style selection (ask everything at once)
        ↓ (user replies)
[Step 2] Internal analysis → output creative script + storyboard script + BGM direction, user confirms once
        ↓ (user confirms)
[Step 3] Ask about turnaround views + scene image (combined question) → generate → confirm together
        ↓ (user confirms)
[Step 4] Output grouping plan and complete video prompts, generate all clips + BGM simultaneously → merge into the final video
```
 
---
 
## Step 1: Specs + Background Setting + Style Selection
 
The first thing to do after receiving the image is to ask all preliminary questions at once; do not analyze the figure beforehand.
 
**If the user's initial message already contains a background setting, skip the background question and ask only about specs and style.**
 
First send a greeting:
```
We've received your figure! Before we start creating, let's confirm a few basic details:
```
 
Then send the following multiple-choice questions separately:
 
```
⏱️ Duration:
  · 15 seconds
  · 30 seconds
  · 60 seconds
  · Custom
```
 
```
📐 Aspect Ratio:
  · 9:16 portrait
  · 1:1 square
  · 16:9 landscape
  · 4:3
```
 
```
🎞️ Resolution:
  · 480p
  · 720p (recommended)
  · 1080p
```
 
```
🗣️ Video Language:
  · Chinese
  · English
  · Japanese
  · Custom
```
 
```
💡 Story Background (optional):
  · I have an idea, I'll tell you
  · No, create one for me
```
 
```
🎥 Visual Style:
  · 🎞️ Stop-motion animation style
  · ✨ Modern art toy style
  · ⚡ Tokusatsu style
```
 
After receiving the reply, internally analyze the figure's temperament (design/form, body shape, craftsmanship & materials, IP background), then proceed to Step 2. **No internal analysis is output to the user.**
 
---
 
## Step 2: Creative Script + Storyboard Script + BGM Direction
 
After the user confirms the specs and style, **output all three items at once**, then ask the user for confirmation.
 
### Creative Dimensions (internal selection, not shown to the user)
 
Before choosing a concept, ask yourself: **What kind of person or moment from everyday life does this figure's temperament most resemble?** Build the story from there instead of applying a formula.
 
**Banned stale tropes**: striking a domineering pose only to be ignored, an office worker slacking off, transforming to defeat the villain and win, and the forced "actually fragile on the inside" contrast. These are the most boring clichés—never use any of them.
 
| Dimension | Core Logic | Suitable Signals |
|------|---------|---------|
| **Unboxing Comes Alive** | The toy has just been unpacked and is seeing the world for the first time—fresh and curious about everything, still wobbly when walking, startled by the most ordinary things | Works for any figure, especially cute/chibi styles |
| **Just Enjoying Life** | No plot, no goal—just a little fellow enjoying some tiny thing: eating, sunbathing, zoning out, listening to music. No twist needed; the atmosphere itself is the content | Soft and cute / plush texture / adorable design |
| **Daily Dose of Cuteness** | The character does a very ordinary everyday chore, but it's inexplicably adorable when done by a toy—e.g., earnestly wiping the table, fitting itself into a cup, or practicing expressions in the mirror | Chibi / figures with distinctive facial expressions |
| **Slice of Mundane Life** | Capture a boring but real everyday moment—waiting for the bus, queuing, a dead phone, food delivery that hasn't arrived. No resolution needed; it's just about that feeling | Office-worker vibe / everyday styling |
| **Plug in Trending Memes** | Take currently trending memes/scenes/moods and drop them straight into the figure's world—e.g., "corporate drone aura," "unhinged literature," "introvert social anxiety," "OOTD check-in." Act it out with the figure and the contrast naturally emerges | Figures with a contemporary, of-the-moment vibe |
| **Whimsical Universe** | Completely counterintuitive—dinosaurs are warriors protecting the princess, rubber ducks are deep-sea detectives, and a cute teddy bear actually rules the entire city. The more absurd yet earnestly acted, the better | Figures with strong visual impact or quirky designs |
| **Imitating Human Activities** | The toy character earnestly does things only humans do—playing tennis, watching a match, being a referee, holding meetings, going on dates, buying coffee. The more serious, the funnier; size contrast and earnest execution are the core of the humor. No plot needed—the scene itself is the content | Suits any figure, especially ones with hands and feet that can perform actions |
| **Multi-Character Relationships** | Multiple figures share a clearly defined relationship, and the relationship itself is the story—cop and robber, partners, meal buddies, commute buddies, rivals, one hustling while the other slacks. Just act this relationship out in a concrete scene and you're done | Multiple figures with complementary or contrasting temperaments |
 
### Three Major Visual Styles (internal reference)
 
| Code | Style Name | Core Features |
|------|---------|---------|
| A | Stop-motion animation style | Visible material textures, subtle micro-movements at the joints, fixed camera position, no voiceover—expression purely through body movement |
| B | Modern art toy style | 3D-modeled characters + realistic large-space rendering; overall like a brand animation short, not miniature photography |
| C | Tokusatsu style | 4:3 aspect ratio, tape-grain texture, emulating the Showa-era studio-shot tokusatsu look, with color tone following the story |
 
### Output Format
 
```
🎬 Creative Script

🎭 Character Setup: [each character's role and relationships, one per line]
📖 Script Outline: [setup-development-turn-resolution or emotional arc, within 150 words]
🎥 Visual Style: [style name] — [one sentence on why it fits]

---

📋 Storyboard Script

📐 Video Specs: [duration] | [aspect ratio] | [resolution]
🎬 Editing Grammar: [style name]-specific grammar

【Shot 1】Character: [CHAR-XX] | Duration: [Xs]
Shot size: [wide shot/full shot/medium shot/close-up/extreme close-up]
Camera movement: [style-specific tag]
Frame: [character actions, scene props, composition key points]
Ambient sound: [background noise of the space]
Sound effects: [specific physical sounds]
Interjections/Voiceover: [none/interjections/lines]

(Subsequent shots follow the same format, and so on)

---

🎵 BGM Direction

Emotional arc: [description] | Rhythm distribution: [description]
Prompt: [style/instruments/rhythm/mood/volume-restraint requirements]
BGM principle: stay restrained and don't overpower the visuals; keep the melody simple; it must fade out at the end.
```
 
```
Do you confirm the creative script, storyboard, and BGM direction above?
```
 
```
  · ✅ Confirmed, proceed to the next step
  · ✏️ Needs revision
```
 
---
 
## Step 3: Turnaround Views + Scene Image
 
After the user confirms Step 2, ask about the turnaround views and the scene image together:
 
```
Next, we need two types of reference images to ensure the consistency of characters and scenes in the video:
```
 
```
📸 Character Turnaround Views (front/side/back + expression variations):
  · 📎 I have turnaround views, uploading directly
  · ❌ Don't have them, generate for me
```
 
```
🎨 Scene Reference Image (generating the scene image first gives stronger consistency in the video's set design, props, and color tone):
  · ✅ Yes, generate it for me
  · ❌ Not needed
```
 
### Turnaround View Generation Specifications (when the user doesn't have them)
 
**Generation model**: Lib Image, with the original figure photo as input. For each character, generate **one 16:9 character reference sheet** on a pure white background: the upper zone contains the turnaround views (front/side/back, taking 60%) + the lower zone has 4–6 expression variations (taking 35%, each labeled with an emotion word). Keep expressions restrained, with ranges matching the toy's actual articulation. For figures with multiple forms, generate one sheet per form.
Immediately after the three-view images are generated/uploaded, establish the **character asset file**: character ID format `[CHAR-01]`, multi-form `[CHAR-01-FORM-A/B]`. Voice-over parameters (Style C speaks lines by default; other styles have no spoken lines by default, only vocal tics): when creating the file, lock in voice characteristics, speech tempo and rhythm, emotional tone, and signature vocal tics (3-5); when there are spoken lines, additionally lock in speaking style/voice intonation/timbre description/prohibited variations; all parameters are strictly carried over in subsequent segments.
 
### Scene Image Generation Specification (when the user selects "Yes")
 
**Generate only one main composition per scene**—that is, the most essential frame of that scene, containing the main background, prop placement, and overall color tone. **No matter how many moments or shots occur at the same location, it counts as one scene with only one image generated**. It is strictly forbidden to turn different moments/angles of the same location into multiple sub-images. Scenes at different locations each get one image, all merged into a single image, arranged side by side horizontally, with the scene name labeled below each sub-image. **Generating multiple separate images is strictly forbidden**.
 
 
**Scene images must be cartoonized. Neon lights/neon colors/neon glow effects are strictly forbidden; photorealistic photography style is prohibited; using the MJ model to generate is prohibited:**
- Style A: handcrafted miniature sets, cardboard/felt/fabric materials, cartoonized colors
- Style B: cartoonized 3D-rendered large space, vivid saturated colors, rounded exaggerated shapes
- Style C: cartoonized Showa miniature-model texture, bright colors, simplified shapes. When generating scene images, the prompt must include: "1970-80s Showa-era Japanese children's tokusatsu TV style, with image texture simulating the Showa effect: slight tape grain, low-saturation retro filter, and slightly faded colors."
**When generating scene images, all character reference images must be attached at the same time.**
 
### Scene Design Rules
 
**Rule 1**: When characters are highly saturated, the background automatically drops to low-saturation gray tones; the background must never steal the show.
**Rule 2**: Emphasize a warm, handcrafted feel, not a purely digital industrial feel.
**Rule 3**: Scene materials must match character materials:
- Style A: plush characters → felt backgrounds; clay characters → cardboard backgrounds; resin characters → wooden board backgrounds
- Style B: 3D-rendered large space, smooth and refined materials
- Style C: Showa miniature-model texture, rough handmade feel
After generation is complete, present the three-view images and scene images together to the user for confirmation:
 
```
All character reference images and scene reference images have been generated. Please check them on the canvas.
```
 
```
Anything that needs adjusting?
  · ✅ All good, proceed to video generation
  · ✏️ Needs adjustment
```
 
---
 
## Step 4: Grouped Video Generation
 
After the user confirms the reference images, directly output the grouping plan and complete video prompts. **No user confirmation needed—start generating immediately**.
 
### Style-Specific Editing Grammar
 
**Style A | Stop-motion animation style**: The camera barely moves; the sense of motion comes from characters jumping between frames. **Allowed**: `[Fixed Camera]` `[Step-frame Pan/Tilt]`. **Forbidden**: smooth camera moves, motion blur. Material textures are clearly visible; slight inter-frame flicker is allowed.
 
**Style B | Modern art toy style**: Commercial-grade smooth camera movement. **Allowed**: `[Crash Zoom]` `[Smooth Dolly In/Out]` `[Snorricam]` `[360° Orbit]` `[Dutch Angle]`. **Forbidden**: choppy frame-stepping feel, retro lo-fi, miniature photography texture. High saturation and high contrast; normal-proportioned large space.
 
**Style C | Tokusatsu style**: Tripod-mounted mechanical movement. **Allowed**: `[Fixed Shot]` `[Mechanical Pan]` `[Mechanical Tilt]` `[Crash Zoom]` `[Low-angle Fixed]`. **Forbidden**: Orbit/Dolly/handheld shake. 4:3 aspect ratio + tape grain. No exaggerated facial expressions; drama comes from sound effects/camera work/body language. Describing facial details in prompts is forbidden.
 
### Grouping Rules and Prompt Iron Rules
 
**Merging rule (strictly enforced)**: For all adjacent shots, as long as the total duration after merging does not exceed 15 seconds, they must be merged into one segment; do not generate each shot as a separate segment. Regardless of whether scenes are the same, merge as long as the duration allows. Only create a new segment when it exceeds 15 seconds.
 
For example: Shot 1 (3s), Shot 2 (4s), Shot 3 (4s), total duration 11s < 15s—they must be merged into Segment 01, not split into three segments.
 
**Simultaneous generation**: Once the prompts for all segments are confirmed, **launch generation of all segments at the same time**; do not generate one and only then the next.
 
**Video prompt iron rules**:
- Include the line "The video contains no background music; keep only ambient sounds, sound effects, and voice-over, with the audio track kept on"
- All shot descriptions merged in full; no shot may be omitted
- Each segment prompt must carry over, word for word, the complete voice-lock descriptions of all characters
- All prompts use Chinese
- When attaching the scene image, the prompt must clearly state **which sub-scene** of the scene image to reference (e.g., "reference Scene 1 in the scene image: Watching a Movie"), because the scene image is a single image with multiple scenes; without specifying the sub-scene, the model cannot determine which part to reference
**Set continuity** (all segments are generated simultaneously, so consistency descriptions must be written at the prompt stage):
- When outputting the grouping plan, write the set description for each segment in advance based on the storyboard (scene/layout/floor/walls/lighting/color tone/character positions/prop list)
- For all segments in the same scene, the set description must be completely identical, copied verbatim, updating only camera movement/character actions/narrative content
- Segments that switch scenes get their own set descriptions, with visual style and tone kept consistent with the whole film
### Grouping Plan Output Format
 
```
To ensure coherent shot rhythm and visual consistency within the same scene, here is the grouping plan and complete video prompts:
 
📦 Video Segment Grouping Plan
 
[Segment 01] Shots X, X | Total duration: Xs | Scene: [Scene name]
  → Characters appearing: [Chinese name] | Attach: character reference image + scene image sub-scene [X]: [Sub-scene name]
  → Complete prompt: [All merged shot descriptions + set file + voice-over parameters + no-BGM declaration]
 
[Segment 02] Shots X, X | Total duration: Xs | Scene: [Scene name]
  → Characters appearing: [Chinese name] | Attach: character reference image + scene image sub-scene [X]: [Sub-scene name]
  → Complete prompt: [All merged shot descriptions + set continuity + voice-over parameters + no-BGM declaration]
 
[X] segments in total. Immediately start generating all segments simultaneously.
```
 
---
 
## Step 5: Generate Video and BGM Simultaneously, Merge and Output the Final Film
 
Launch directly after the grouping plan is output; no user confirmation needed:
 
1. **Start generating all segments simultaneously**: Seedance 2.0 generates all segments at the same time (not sequentially), while generating the BGM (based on the BGM prompt locked in Step 2)
2. After each segment is generated, present it on the canvas for the user to view, then continue automatically; no per-segment user confirmation needed
3. Once all segments are generated, splice them together in order
4. Composite the video with the BGM in sync and output the complete final film
---
 
## Global Constraints
 
1. **Stage gating**: Steps 1/2/3 must wait for user confirmation before advancing; Step 4 proceeds directly to generation after outputting the grouping plan, no confirmation needed
2. **Creative dimensions chosen internally**: The user has already selected the style in Step 1; creative dimensions are chosen internally by the AI based on the figure's temperament and the style, and are not output to the user
3. **Character asset IDs run through the entire process**: every storyboard and segment generation node must reference them
4. **Separate files for multi-form figures**: each form has its own three-view images and ID
5. **Visual style consistent throughout**: once the style is confirmed, the editing grammar/sound effects/BGM tone must remain consistent
6. **High-fidelity reproduction of the figure's appearance**: always based on the actual images uploaded by the user
7. **Do not output options repeatedly**
8. **Do not expose internal style codes**: refer to styles by name only; never say "Style A/B/C" to the user
9. **Do not proactively add on-screen text/titles**: unless the user requests it
10. **Do not reference real brands or copyrighted IP names**
11. **All prompts use Chinese**