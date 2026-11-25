---
name: neo-chinese-aesthetic-tvc
description: "Neo-Chinese aesthetic TVC: full neo-Chinese aesthetic production, from makeup and styling to set design and final ad, one-stop stunning visuals"
---

## 1. Guochao Sub-Types (Identify the sub-type from the uploaded product and take the default; the aesthetic tone is uniformly Neo-Chinese Guochao)

This skill only produces **Neo-Chinese Guochao (China-chic)** as its single visual language; it does not do Euro-American fashion films / cyber-tech aesthetics or other styles. Below are the default traits for each product sub-type, but **colors, patterns, objects, and formal language are always unified into Neo-Chinese Guochao** (ink-wash negative space, flying eaves and dougong brackets, mortise-and-tenon joinery and window lattices, cloud / huiwen fret / scrolling-vine motifs, xuan paper and silk, Chinese red with Guochao gold, porcelain and lacquerware, calligraphy and seals, silk embroidery). **Set design favors the "trendy" side**: prioritize letting these Eastern elements collide with futurism / minimalism / silver-white / mirror surfaces / metallic textures (stainless steel, matte metal, translucent acrylic, floating structures, generous minimal negative space, cool light) to create freshness, rather than pure classical replication—traditional symbols as the foundation, modern materials as the finishing touch.

- **Tea drinks / Baijiu / Traditional foods** — Traits: swirling tea mist, spirits clinging to the glass, close-ups of vessels (tea bowls / cups / porcelain jars), wooden/bamboo-woven settings, slow-motion mood; default creative approach: Emotion + Demonstration; references: Moutai, Guanfushan, CHALI
- **Beauty / Domestic skincare** — Traits: macro shots of flowing textures, Eastern skin feel, makeup styling infused with Guofeng elements (hairpins / velvet flowers / opera-makeup imagery), luxurious negative space; default creative approach: Demonstration + Emotion; references: Florasis, MAOGEPING, To Summer
- **Apparel / New Chinese-style fashion** — Traits: modernized Hanfu / New Chinese jackets and shirts, close-ups of fabric drape, blocking in courtyards/gardens, expressive freehand camera moves; default creative approach: Story / Emotion (audiovisual-spectacle style); references: HEAVEN GAIA, MUKZIN, Punk Grandpas
- **Home / Fragrance / Cultural-creative goods** — Traits: close-ups of mortise-and-tenon joinery, incense-burner smoke, xuan paper/wood/bronze textures, tranquil negative space; default creative approach: Emotion (audiovisual-spectacle style); references: To Summer, Lost & Found
- **Jewelry / Accessories** — Traits: chased gold and silver, jade luster, slow orbiting close-ups, low-key lighting picking out details; default creative approach: Demonstration + Emotion; references: Lao Feng Xiang, Mengjinyuan
- **Real estate / Cultural tourism / Spatial experiences** — Traits: aerial shots of flying-eave silhouettes, garden borrowed scenery, light and shadow through lattice windows, lifestyle imagination; default creative approach: Emotion / Story; references: Chinese courtyard residential projects, ancient-town cultural tourism
- **Domestic 3C / Trendy toys (art toys)** — Traits: the product itself grafted with Guofeng patterns, levitating display + ink-wash transitions, tradition colliding with modernity; default creative approach: Demonstration + Emotion

> Once the sub-type is set, you get: default traits + suggested creative approach + a set of default knob settings (see the notes in Section 3); **the Eastern aesthetic tone and the fixed style seed apply uniformly to all sub-types**. Clients with special requirements may override specific details, but must not depart from the overall direction of Neo-Chinese Guochao.

---

## 2. The Five Dimensions (Confirm item by item with the user in conversation)

The 5 dimensions of a TVC commercial (production method is no longer asked; it is fixed to live action). Once the product category is set, most dimensions already have defaults; the conversation only needs to fill in or correct them, without re-asking known items; **aspect ratio and resolution have no defaults—you must ask the user**.

**1. Ad purpose**: Product · Brand · Image · Promotion · Public service\
→ Determines information density and where the ending lands: Promotion = strong CTA; Brand/Image = close on a proposition/slogan; Product = selling points + CTA. (By default no logo is added; the ending relies mainly on a slogan caption or a natural close on the visuals/product.)

**2. Creative approach** (= the prompt-generation skeleton): Story · Emotion · Demonstration

- **Story**: A complete plot—setup → conflict → resolution—with the product woven into the narrative.
- **Emotion**: An emotional arc that moves people—establish character/situation → emotional peak → product as the solution → land the proposition. Use `{{Mixed N}}` to lock the character(s).
- **Demonstration**: Selling points delivered directly—pain point/scene → product entrance → one shot, one selling point → effect shown → close with slogan/CTA (by default no logo added). The product is clear in every shot.

> "Audiovisual spectacle / fashion film" is not a separate approach but a **high-production aesthetic style** (dense camera movement, aesthetics first, slow motion, generous negative space), often layered on top of Story/Emotion/Demonstration (apparel, beauty, jewelry, home fragrance), built up through the breakdown elements in Section 3.

**3. Video length**: 15s · 30s · 60s\
→ Determines the number of shots (15s ≈ 3–5 shots / 30s ≈ 6–9 / 60s more), and triggers **segmented generation in 15s chunks** (see Workflow Step 4).

**4. Aspect ratio**: 16:9 · 4:3 · 9:16 · 3:4\
→ Determines the final frame format (also used for the scene mood images and the `--ar` parameter in Seedance generation): 16:9 landscape (TV/OTT/horizontal), 9:16 vertical (social-media vertical, the first 3 seconds hit even harder), 4:3 retro square screen, 3:4 portrait. This item **must be chosen by the user**. When multiple versions are needed, a single draft can output two versions (e.g., 16:9 + 9:16).

> **Production method is no longer asked as a dimension**—this skill always uses the **live-action style** (cinematic commercial base + Neo-Chinese Guochao live-action texture), no animation/CG; the style-lock sentence is fixed to a live-action base.

**5. Generation resolution**: 480p · 720p · 1080p\
→ Determines the output-resolution parameter when invoking SD2, directly affecting final clarity and generation time/cost; this item **must be chosen by the user**, no default applied.

---

## 3. Breakdown Elements (7 Knobs · Option Menu)

Pick one setting per dimension; the italic notes are the "defaults by category".

**1. Lighting design**

- Light source: natural light / studio artificial light / mixed light
- Direction: front light / side light / side-backlight / backlight / top light / bottom light
- Lighting setup: Key light, Fill light, Rim/Edge light, Backlight, hair light, Volumetric/Tyndall light, Beauty dish, in-frame Practical sources (lanterns / candle flames / lattice-window light)
- Color temperature: cool (blue-white) / warm (gold-orange) / neutral / cool-warm contrast
- Special light effects: lattice-window light pools, candle-smoke volumetric light, silk-gauze soft light, ink-wash-style light-and-shadow gradients, lens flare
- *Default: tea/Baijiu/food = warm candlelit feel + volumetric light; beauty/domestic skincare = soft, airy warm tones + hair light; apparel = natural window light + silk-gauze soft light; home/fragrance = warm wood-toned light + smoky volumetric light; jewelry = low-key side-backlight picking out details; real estate/cultural tourism = warm soft natural light + lattice-window light pools*

**2. Color palette**

- Color temperature: warm / cool / neutral / cool-warm split-tone
- Color scheme: ink-wash black-white-gray, Chinese-red vs. Guochao-gold contrast, Morandi low-saturation Guofeng gray, cool tones of blue-green landscape painting, xuan-paper off-white low saturation, vintage aged silk tones
- Saturation: high (festival/red-gold) / standard / low (ink-wash/literati) / desaturated monochrome (ink wash)
- Texture overlays: xuan-paper texture, silk soft-glow halo, swirling mist, film grain
- *Default: tea/Baijiu/food = warm + Chinese-red vs. gold contrast; beauty/domestic skincare = low-saturation warm + xuan-paper texture; apparel = ink-wash low saturation + silk soft glow; home/fragrance = Morandi Guofeng gray; jewelry = low-key high contrast + metallic sheen; real estate/cultural tourism = cool blue-green landscape tones*

**3. Camera language**

- Camera movement: static, push/pull, pan, dolly, crane, orbit, tracking, handheld, gimbal/stabilizer, FPV fly-through
- Shot size: macro/extreme close-up, close-up, near shot, medium shot, full shot, extreme long shot, aerial
- Angle: eye level, low angle, high angle, top-down flat lay, Dutch angle (tilt)
- Composition: centered symmetry, rule of thirds, frame-within-frame, generous negative space, full-frame composition, foreground occlusion
- Lens characteristics: wide-angle distortion, telephoto compression, tilt-shift miniature effect, fisheye
- *Default: beauty/domestic skincare = macro + slow orbit; apparel = courtyard dolly + tracking + negative-space composition; jewelry = macro + slow orbit; tea/Baijiu = top-down + slow-mo macro; real estate/cultural tourism = aerial + frame-within-frame composition (lattice windows / doorways)*

**4. Sound & music**
- **BGM is fixed to "fusion music," no selection allowed**: "Electronic music performed on classical Chinese instruments" — the **real timbres of traditional instruments** such as guzheng/pipa/dizi/xiao/erhu/bianzhong bells form the melodic core, **deeply fused with modern electronic elements** (beats/synths/low-frequency groove/sampling); it is a Chinese-style × electronic fusion — not pure folk, not pure electronic, the two interwoven. Keywords: `traditional Chinese instruments (guzheng/pipa/dizi/erhu) fused with modern electronic music, neo-Chinese electronic fusion`.
- **BPM follows the film**: determined by the actual rhythm/tonality of the final cut — upbeat/beat-synced pieces lean fast with strong groove, soothing/emotional pieces lean slow with a sense of space; tempo may vary within the piece, no fixed BPM.
- **Generation timing**: **the SD2 video-generation stage is completely silent** — no BGM, no sound effects/ambient sounds, no voiceover generated; only pure visuals; BGM and voiceover are all added at Step 6 post-production compositing.
- Music functions: driving beat-synced cuts, ambient underlay, emotional heightening — choose the function level by subtype and creative approach, but the timbral foundation of "classical instruments × electronic fusion" stays unchanged.
- **No sound-effects layer**: the final cut contains no sound effects/ambient sounds (SD2 is silent, and none are added in post either); the final cut's audio has only two layers — **BGM + voiceover (if any)**.
- Vocals: male/female voiceover VO, or no vocals
- Mixing: layered mix of BGM + voiceover, with voiceover clarity prioritized (BGM must not drown out the vocals).
- *Defaults: tea drinks/baijiu = Chinese-style electronic fusion (leaning soothing groove); beauty/domestic brands = Chinese-style electronic fusion (stronger electronic feel, clear beats); apparel/home = Chinese-style electronic fusion (silk-and-bamboo timbres + soft electronic underlay); jewelry = sparse Chinese-style electronic fusion; real estate/cultural tourism = Chinese-style electronic fusion (grand, low-frequency groove) + voiceover*

**5. Editing Rhythm**

- Cutting speed: fast cuts, medium pace, slow long takes, one-shot single take
- Beat: cuts hitting the drum beats, free narrative rhythm
- Transitions: hard cut, fade in/out, match cut, seamless morph, occlusion whip cut, jump cut, liquid/light-effect transitions (**superimposition/cross-dissolve forbidden**)
- Time handling: linear narration, flashback, parallel editing, montage, freeze-frame emphasis
- Special techniques: freeze frame, speed ramp, datamosh glitch
- *Defaults: tea drinks/promotions = medium-paced beat-sync; apparel/home/jewelry = slow impressionistic long takes; real estate/cultural tourism = slow start gradually accelerating*

**6. Actors & Models**

- **Human presence: human figures are mandatory** — regardless of subtype or creative approach, every ad must feature human presence (it can be a fully on-camera model, or only hands/partial limbs, e.g., a hand pouring tea, the motion of putting on jewelry, fingertips brushing across fabric); **product-only, human-free presentation is not allowed**.
- Target demographics: young, urban white-collar, multi-generational families, children, athletic crowds
- Temperament style: premium cool, warm and approachable, athletic power, street-cool, fresh girl-next-door
- Diversity: local, internationally mixed, multi-ethnic
- Performance tone: restrained realism, slice-of-life, theatrical exaggeration (**expressions must be natural and believable; exaggerated or bizarre expressions forbidden**)
- Emotional focus: facial micro-expressions, gaze, body movements, interactions
- Wardrobe (by subtype): aligned with the neo-Chinese guochao tone — **uniformly based on modernized hanfu / neo-Chinese jackets and shirts / mandarin collars with frog buttons, with colors drawn from Chinese red, guochao gold, azure green, ink-wash gray**; beauty = moderately skin-baring but not revealing, makeup/styling infused with Chinese-style elements (hairpins/velvet flowers); apparel = premium neo-Chinese ready-to-wear with strongly draping fabrics; jewelry/home/real estate = tasteful neo-Chinese lifestyle wear
- *Defaults: beauty/domestic brands = high-fashion Eastern face + facial micro-expressions + **skin glow is the priority**; apparel = neo-Chinese styling + poised body carriage; real estate/cultural tourism = multi-generational family; tea drinks/baijiu/jewelry = human presence introduced mainly through **hands/partial-body movements** (e.g., a hand holding a teapot pouring tea, the motion of donning jewelry), with objects/products still the visual protagonist, but every shot guaranteed to include human presence*

**7. Story Type**

- Narrative type: strong narrative (complete plot) / weak narrative (linked atmospheric spectacles) / no narrative (pure display)
- Structure: three-act, linear, non-linear montage, single-point demonstration, problem—solution
- Perspective: first person, observer, product POV, parallel multi-thread
- Story archetypes: slice of life, hero's journey, before/after comparison, testimonial endorsement, demo, brand manifesto
- Closing: product hero shot, proposition/slogan caption (when a slogan exists, have the video model generate it directly), CTA (**no logo end-card by default**, unless the user explicitly requests it)
- *Defaults: real estate/cultural tourism = heartwarming three-act; apparel = atmospheric linear narrative; beauty/jewelry/tea drinks = weak narrative (linked atmospheric spectacles); home/fragrance = weak narrative or pure display*

---

## Workflow

### Step 1 · User uploads the product

The user uploads product images (or a product description / reference video). From the product, identify: its subtype (see the table in Section 1), product form/material/selling points, and whether a `{{Mixed N}}` character is needed. Once the subtype is known, it brings along the default traits + recommended creative approaches + default knob settings.\
**[Mandatory step · cannot be skipped] Immediately after upload, generate two product anchor images** (the basis for product consistency across all subsequent storyboard shots): **the [user-uploaded product image] must be used as the reference image (image reference / image-to-image); never generate purely from text** — feed the original image(s) into the generation model (GPT Image with fidelity recommended) and generate according to the real shape/color/material/proportions/brand logo; if there are multiple, feed them all. **White background, 16:9**, serving as the anchors `{{Product Three Views}}` (front/side/back) + `{{Product Detail View}}` (key details chosen by function, e.g., skincare = bottle body/pump head/texture). Both are indispensable; after generation, compare them against the originals and regenerate if shape/color scheme/logo don't match; both must exist before entering Step 2. All subsequent storyboard product visuals must follow these images.

> If **only a text description is given, with no product image**: first inform that "generation can only be text-to-image from the description and may differ from the real product," ask follow-up questions about key appearance details, then generate; if the user later uploads images, it must be redone.\
****Categories such as real estate/hotels where "the space is the product"**: there is no physical product; instead, have the user **upload 5–8 real-scene photos** (or have the skill virtually generate 5–8, at 16:9), serving as `{{Space Real Scenes}}` — **replacing the product three views while also acting as the scene anchor**. All subsequent storyboard spaces/sets/lighting must follow these; the space itself has no people, but a character must still be selected, with people appearing through lifestyle scenes (strolling / tea tasting / writing at a desk), not a film of empty shots throughout.\
****Reverse-engineering a reference video**: first use `scripts/extract_frames.sh` to extract frames and read the specs (first-3-second hook / rhythm / camera movement / landing point / which subtype it belongs to), then produce a matching piece, uniformly rewritten into the neo-Chinese guochao aesthetic (without changing the original's narrative structure and rhythm — only replacing colors/patterns/objects/styling with guochao language); never describe footage you haven't seen out of thin air. **Reverse-engineering likewise generates each 15s segment as a whole (numbered storyboard shots; one continuous prompt produces one entire segment), with 30s / 60s split into multiple sequential 15s segments — do not split it into many single shots generated separately.**

### Step 2 · One input card confirms all dimensions at once (continuous inquiry, unified recording)

**Use one** `ask_user_input` **input card to put all of the following items to the user at once** (triggered consecutively, all collected in a single card), **do not ask one step and stop**; the user fills everything in within the same card, record it all together, then proceed. Items to confirm:

1. **Purpose** (brand/image, product selling points, sales promotion…)
2. **Creative approach** (story / emotion / demonstration; production method not asked — fixed to live-action)
3. **Duration** (15s / 30s / 60s)
4. **Video aspect ratio** (16:9 / 4:3 / 9:16 / 3:4, single select, no default, required)
5. **Generation resolution** (480p / 720p / 1080p, single select, no default, required)
6. **Brand slogan** (fill in if available, used for the closing subtitle at the end; leave blank if none. **No logo by default, do not ask about the logo**, unless the user proactively requests it)
7. **Voiceover**: whether a voiceover is needed → if yes: voice (male/female/neutral, style, language) + **whether subtitles are needed (Chinese / English / Chinese-English bilingual / none)**. (The voiceover is always added in post-production via TTS/voice dubbing—there is no "write into the prompt" option; subtitles are likewise added before final compositing; the voiceover script is not filled in on this card, but is left to the storyboard table stage, where the skill drafts it first and shows it to the user for review and confirmation. **If no voiceover is selected, do not ask about subtitles.**)

For items where the category already provides a default, only confirm whether any changes are needed—do not re-ask; except for aspect ratio/resolution, every item may be answered with "you decide for me"—if the user says "you decide everything," fill in the remaining items with defaults, but aspect ratio and resolution still require an explicit choice. **Once this card is fully collected, the dimensions and voiceover preferences are locked in one go, and we move on to Step 3.**

### Step 3 · Produce the moodboard (ask for reference images first → select text options item by item → generate images per branch · user confirmation required)

**0. First ask for character reference images (before selecting the text direction; after asking, you must stop and wait for the user to upload**). If there is a model, first use `ask_user_input` to ask: **"Do you have a face reference image or a styling reference image? (You can upload a face photo, clothing/styling reference images you'd like to reference, or both.)"** After asking, you must pause so the user can upload the reference images (if any) to the chat box before moving on.

**Iron rule: face/portrait reference images are never fed to MJ** (MJ only accepts **styling reference images** as image reference); face images are fed only at the final SD2 video-generation stage, together with the three-view sheet, to lock the real face and real hair. **Whether the face on the three-view sheet is covered depends solely on whether a real face image exists: if yes → cover the face with a white circular sticker + a Chinese annotation in the bottom-right corner (see the character three-view section below for details); if no → do not cover** (the MJ face is the identity, and also serves as the SD2 face reference).

Depending on what the user uploads, there are four cases (in all of them, first "understand the reference image/text intent + flesh it out into a complete guochao styling spec"; do not simply copy the image verbatim; the workflow is uniformly **MJ produces the front-facing image → LibImage produces the three-view sheet**):

- **① Face reference image only**: the face is not fed to MJ; MJ generates the image from the text spec; the three-view sheet gets the **face-covering sticker + annotation**, and the face image is fed only at the SD2 stage together with the three-view sheet (locking the real face and real hair).
- **② Styling reference image only**: the styling image is **fed to MJ as an image reference**; the three-view sheet **does not cover the face** (the MJ face is the identity, and also serves as the SD2 face reference).
- **③ Both face and styling available**: **feed only the styling image, not the face**; the three-view sheet gets the **face-covering sticker + annotation**, and the face image is fed only at the SD2 stage.
- **④ Neither available**: proceed with the normal "select the model's image via text" flow; the three-view sheet **does not cover the face** (the MJ face is the identity).

**First lock in the direction step by step via text; generate images only after everything has been selected.** Text selections are made item by item via `ask_user_input`, one item at a time, each with 3 options + a "show another batch" fallback:

1. **Select the model's image in text (mandatory when case ④ applies—neither available; in cases ① and ③ with a face reference image, ask only about age range/temperament/hairstyle direction, with looks following the reference image, so ethnicity need not be selected again)**: give 3 image options, each = "ethnicity/region (East Asian / mixed Asian / international…) + age + gender + hairstyle"; **do not write clothing here** (clothing/styling is left for the MJ front-facing image stage, and is uniformly New Chinese-style guochao styling), for example:

   - East Asian young woman, hair in an updo with a flower pin
   - East Asian middle-aged man, neat short hair
   - Mixed-Asian young woman, long straight hair

   The image must fit the product/brand tone, not be random. **This skill mandates that every ad include a human figure; this item cannot be skipped** (even when the object/product is the visual protagonist, you must still select the character who will appear for hands/partial shots).

2. **Select the scene atmosphere**: give 3 text options, each condensing "scene/set + color palette + lighting + texture" into one sentence. **The direction is not pure classical replication, but a collision of "Chinese aesthetic elements × futurism/minimalism/metallic texture"**—combining Eastern motifs (window lattices/moon gates/ink wash/cloud patterns/garden silhouettes/vessels) with modern material languages (silver-white/mirror/stainless steel/acrylic/matte metal/minimalist vast negative space/cool light/floating structures) to create something fresh.\
   **Hard requirement on scale: it must be a large scene that can accommodate a full-body model's movement (panoramic / extreme-long-shot scale)**—a "space/building/environment one can walk into," not a tabletop installation or partial countertop; it needs depth, a ground plane, and room to stand and move, so that the later storyboard frames containing the model can place the person fully in the picture. For example:

   - Minimalist silver-white double-height exhibition hall, with a giant floating moon-gate mirror installation spanning the panorama, cool soft light + a thread of warm gold edging, vast negative space and depth
   - Futuristic metal corridor/water-feature hall, ink-wash mist drifting over a stainless-steel floor, cool white top light + low-saturation blue-gray, room for people to walk
   - Open space enclosed by a matrix of frosted acrylic screens, light faintly filtering through cloud patterns, Chinese red accents amid the silver-gray cool tones, crisp directional light + an extending ground plane

   (If the category/client leans more traditional, you may also offer a more classical version, but it likewise must be a large scene; by default, prioritize this innovative "New Chinese × future-minimalist" set design.) The user picks 1.

**After the text direction is locked, generate the reference images in order:**

- **Scene atmosphere image**: **invoke Midjourney to generate**. Expand the selected scene atmosphere **into a concrete description** (scene details/lighting/color/texture/composition). **Eastern motifs × modern materials collision**: Eastern elements (window lattices/moon gates/ink-wash negative space/cloud and fret patterns/garden silhouettes/xuan paper and silk/Chinese red and guochao gold, etc.) **combined with** futurist/minimalist/metallic languages (silver-white/mirror/stainless steel/matte metal/translucent acrylic/floating structures/minimalist vast negative space/cool light), avoiding pure classical element-stacking. **The scale must be a large scene**: explicitly write panoramic / extreme long shot / wide-angle, high-ceilinged and open, with ground and depth in the MJ prompt (e.g., `wide establishing shot, expansive interior, high ceiling, spacious, deep perspective, room to fit a full-body figure`), ensuring this empty-scene background can later fully accommodate a full-body model's movement—do not let it come out as a tabletop installation or partial close-up. **It must be a pure empty scene**: environment only; products/people/human silhouettes/hands/animals/text/logos are forbidden; explicitly add negation words to the prompt (`empty scene, no people, no product, no text, uninhabited`) so it can be reused as the background for all subsequent shots. **Style seed is fixed** `--sref 4608797467 --profile nn1ntrp` **+** `--v 8.1` (do not ask, do not display the code); `--ar` takes the ratio chosen in Step 2. **Final MJ prompt = large-scene description + empty-scene negation words + fixed seed (including** `--v 8.1` **and** `--ar`**)**. (By default, 4 images are generated to choose from; if a subject appears, or the scene is too small to fit a person, it is judged unqualified and regenerated. If the user supplies their own reference images, `--cref`/`--iw` may be stacked on top, but the fixed seed cannot be removed, nor may the empty-scene and large-scene constraints be loosened.)
- **MJ styling image (if there is a model)**: **MJ V8.1 + fixed style seed** `--sref 4608797467 --profile nn1ntrp`**, **`--ar 3:4`. **Generate only one set of front-facing images, with the composition as full-body/three-quarter-body as possible** (so the full outfit pairing / bottoms / footwear / silhouette are clearly visible—at least from the thighs up, full body if possible), face in sharp focus; run the same prompt once (4 images by default), no splitting or upscaling—go straight to picking 1 of 4. The framing must explicitly state "full-body or three-quarter-body front-facing standing pose, fully showcasing the complete outfit and footwear". **Branch per ①-④: only ②③ feed the styling image to MJ as an image reference; the face image is never fed under any circumstance**; the spec combines scene atmosphere + model look + guochao (China-chic) styling language (modernized hanfu / mandarin collar with frog buttons / Chinese red & guochao gold / cloud & fret motifs). **After generation, stop and present a pick-1-of-4 option for the user to choose**—the options must indicate each image's position in the MJ 4-grid: **1 (top-left), 2 (top-right), 3 (bottom-left), 4 (bottom-right)** (matching MJ's default 2×2 output order); proceed onward only after a selection is made.
- **Character three-view sheet (one per person, 16:9)**: **generate with LibImage** (not MJ), **expanded from the user-selected front-facing image**—white background, **full-body three views arranged left/center/right (front/side/back), not a head close-up**, with proportions/styling (including clothing) consistent with the selected front-facing image. **Face handling branches per Step 3.0**: ①③ have a face reference image → **cover each face completely with a white circular sticker (covering the faces in all three views), and add a small Chinese-text annotation at the bottom-right of the image: "人脸单独提供 · 此图仅用于服装造型参考"** (the real face is reserved for the SD2-stage face reference image to lock); ②④ have no face reference image → keep the face from the MJ front-facing image, uncovered. The three-view sheet serves as the `{{Mixed N}}` consistency anchor, with natural expressions. **If the styling reference image and the MJ result differ, the user-selected MJ front-facing image prevails.**

Attach to the images one line of concept keywords + the locked list of dial settings (one setting per each of the 7 dimensions).\
**Only after the user confirms is the visual direction locked, and only then do we move to the next step**—the subsequent storyboards are written strictly according to the selected model and scene atmosphere. The moodboard is the gatekeeping checkpoint before producing the video prompt.

### Step 4 · Segment by Duration (do not ask for a mode; unified 15s whole-segment generation)

**There is only one generation method: in 15s units, each segment is generated in one go as a single continuous prompt** (internally storyboarded with numbered shots—Shot 1 / Shot 2 / Shot 3…—each shot specifying shot size + camera movement + content, format per Step 5). **No per-shot frame-by-frame generation, and the user is not asked to choose a mode.**

- **15s**: one storyboard table for the whole piece (Step 5.0) → confirm → expand into the prompt and generate the whole segment.
- **30s**: storyboard table **delivered for the whole piece in one pass** (Segment 1 0–15s and Segment 2 15–30s all listed in one table) → single user confirmation → **both segment prompts generated concurrently and simultaneously** (each segment keeps consistency anchored on the unified `{{Mixed N}}`/outfit/scene/lighting, and they can be spliced in order). **The two segments must differ in content and advance the narrative, with no repeated shots or actions; no end-card lockup at the close of the first 15 seconds—the end-card lockup (slogan caption if there is a slogan, no logo by default) goes only at the end of the second 15 seconds.**
- **60s**: storyboard table **delivered for the whole piece in one pass** (all four segments listed in one table) → single user confirmation → **all four segment prompts generated concurrently and simultaneously** (unified anchors, spliceable in sequence). **The end-card lockup is applied only at the end of the final segment (slogan caption if there is a slogan, no logo by default); the middle segments do not close with a lockup.**

> **Two mandatory shots (see Step 5; for multi-segment, counted across the whole piece)**: ① the full video must include **at least one product-usage close-up shot** (it may be placed in any segment); ② **the end card (the last shot of the final segment) must be a medium close shot of the model together with the product** (worn if wearable; held if it can only be used/eaten/drunk).

### Step 5 · Output in the Seedance 2.0 Format (storyboard table first → then expand the prompts)

**5.0 Storyboard table confirmation (whole piece delivered in one pass; the confirmation gate is here) deliver the storyboard table for the entire piece in one go**—list exactly as much as the runtime calls for: one segment for 15s, two for 30s, four for 60s, **with all shots listed in the same table** (label the segments by their 15s divisions, e.g. "Segment 1 0–15s", "Segment 2 15–30s"), so the user sees the full picture of the entire video at once and confirms or revises in a single pass. **The storyboard table is the only gate in this stage where the user needs to confirm shot content**; once the table is confirmed, expanding the prompts and invoking SD2 for generation are internal execution—**the prompts are not thrown back to the user for a second confirmation**. Table columns: **Shot No. ｜ Segment ｜ Shot size ｜ Camera movement ｜ Visual content (**`{{Mixed N}}`**/product action) ｜ Narration/VO ｜ Duration(s) ｜ Notes**.

- **Narration/VO column**: write the narration copy corresponding to that shot in its row (one row per shot, visuals and words aligned); when a connected long sentence spans several shots, it may be merged and written across the corresponding rows. Narration must fit the confirmed purpose and end card, and be timed to the duration (approx. 30–40 characters for 15s / 60–80 for 30s / 120–160 for 60s, adjusted to speaking pace). **If narration is not needed** (narration not selected in Step 2), leave this column empty or mark "None".
- The table must reflect the two mandatory shots (product-usage close-up; end card with model and product in frame) and the closing end card. **Every shot's (including the product close-up) visual content/notes must indicate that it takes place within the selected scene**; the product close-up must note "in-scene supporting surface + shallow depth-of-field blur"; white studio/solid-color backdrops are not allowed.

> The narration's **whether needed / voice type** was already confirmed in the Step 2 inquiry card; here the copy is only reviewed together with the storyboard. Narration is **always added in post** (SD2 stays muted; it is not written into the prompt) and saved for Step 6 voiceover. (BGM is also not handled here: a fixed Chinese-style electronic fusion track, with BPM matching the piece, is generated before Step 6 compositing; **the SD2-generated video is completely silent, with no sound whatsoever**.)

**5.1 Expand the prompts and generate multiple concurrently (table already confirmed; no pausing between segments**) since the whole-piece table was confirmed in one pass in 5.0, **expand all segments of the entire piece, as divided by 15s, in one pass into their respective continuous prompts and submit them to SD2 concurrently for generation**—**no longer waiting for user confirmation segment by segment**. Each segment still keeps consistency anchored on the unified `{{Mixed N}}` / outfit / scene / lighting, can be spliced in sequence, and transitions without continuity breaks; once generation is complete, deliver everything together and move on to Step 6 compositing. For a single 15s segment, generate a single prompt.

**★ Hard constraint on product consistency (core of anti-drift, highest priority)**★ The root cause of the product "drifting more and more toward later segments, with its structure/proportions going off" is that the later segments lose the product reference. Therefore:

- **Every 15s segment generation must feed the same set of product references to SD2 as image references—not just once at the start**: every segment's input includes `{{Product Three-View Sheet}}` + `{{Product Detail Images}}`, and **every segment of the whole piece is fed the exact same two images—no substituting, no omitting, and not feeding them only to the first segment**. Each concurrent prompt must independently carry this complete set of product references.
- **The prompt body locks the product explicitly**: every shot featuring the product must state "the product's shape/proportions/structure/color scheme/logo strictly follow `{{Product Three-View Sheet}}`+`{{Product Detail Images}}`, staying fully consistent with the reference images—no deformation, no color changes, and no moving or fabricating the logo/text".
- **Ensure the product can be aligned**: Whenever the product appears, it must be **fully in frame, sharp, and not excessively occluded** (hands may show in usage shots, but the product body and logo must be clearly visible), to prevent the model from improvising and distorting it due to incompleteness/blur/large-area occlusion.
- After generation, **compare segment by segment** the product against the anchor image; as soon as the shape/proportions/logo drift, **regenerate that segment** (and check whether that segment was missing the product reference input).

Write strictly according to the confirmed moodboard + storyboard table. **The first sentence of every output prompt is fixed as a reference to the scene image**:

> Please refer to `{{Scene Atmosphere Image}}` as the scene atmosphere.\
****Real estate / hotels and other categories requiring real-shot imagery**: change the first sentence to reference `{{Real Space Photo}}`, and **every shot must take place within that real-shot scene**; fictional / imagined spaces may not be used.

The body that follows **contains only the quality lock (cinematic/ad-grade) + subject / action / camera / product**, and **no longer describes the scene atmosphere / environment / color tone in text** (the scene is always carried by the selected `{{Scene Atmosphere Image}}`; writing it into the body would be mutually exclusive with the image reference; whether the scene is right is judged by the selected image).

- **All shots stay within the selected scene, product close-ups included (jumping to a white studio is forbidden)**: **Every shot, including product close-ups / macro / usage shots, must have as its background the environment of the selected** `{{Scene Atmosphere Image}}` **— that exact environment**; never suddenly cut to a white studio / solid-color backdrop / a space disconnected from the rest of the film. Product close-ups may show the product "resting quietly on a plausible support within the scene" (e.g., a display stand/stone pedestal in a bamboo grove, a tea-room table, a floating pedestal in a showroom) with **shallow depth-of-field blur** applied to the background, highlighting the product while preserving a recognizable scene atmosphere. In the prompt, explicitly write for the product close-up shot: "the background is the environment of `{{Scene Atmosphere Image}}`, with shallow depth-of-field blur, not a solid-color studio shoot".
- **Character face lock**: For ①③ "with a face reference image", state at `{{Mixed N}}`'s first appearance: "face taken from the face reference image (real face, real hair), styling/figure taken from the three-view drawing", and feed the face image + three-view drawing together as input; for ②④ "without a face reference image", go directly by the three-view drawing (including the MJ face).
- **Output language = Chinese.**
- **Numbered storyboard format**: Within one prompt, shots are arranged in order as **Shot 1 / Shot 2 / Shot 3 / Shot 4…**; each shot specifies: **shot size** (macro/close-up/close shot/medium shot/wide shot/aerial…) + **camera movement** (static/push-pull/orbit/follow/crane…) + **content** (the actions and visuals of `{{Mixed N}}` or the product).
- **Required Shot 1 · Product-in-use close-up (indispensable)**: The storyboard **must include at least one close-up/macro shot of "the product being used"** — a brush sweeping across the powder of an eyeshadow palette, a fingertip lightly touching cream and gliding its texture over skin, a hand holding a teapot pouring tea into cups, fingertips gliding over fabric, etc. — using the real usage action of the product for the category, highlighting texture/tactile feel/functional details. **This shot's background likewise stays within the selected scene with shallow depth-of-field blur; jumping to a white studio is not allowed.**
- **Required Shot 2 · Model and product in the same frame at the end frame (indispensable)**: **The last shot (end frame) must be a medium-close shot showing the model together with the product** — **if it can be worn, have it worn** (necklace/jewelry = medium-close shot of the model wearing it; apparel = on-body effect), **if it can only be used/consumed, have it held** (beauty & skincare = holding the product; tea/liquor/beverages = raising a cup/holding a bottle), ending with the product and the person in the same frame. This shot may overlap with the closing line (slogan subtitle).
- **Whole-segment continuous prompt (the only format)**: Each 15s segment = one continuous prompt = first sentence referencing `{{Scene Atmosphere Image}}` → quality-lock sentence (cinematic/ad-grade, with no scene atmosphere or color tone description) → **Shot 1 / Shot 2 / Shot 3… (each shot: shot size + camera movement + content)** → closing line (**if there is a slogan, have the video model generate that slogan subtitle directly; no logo by default unless the user explicitly requests it**). Deliver the whole thing in Chinese as one piece, generated in a single pass, not split frame-by-frame per shot.
- **Two-level cadence: the table is confirmed once, videos run as multiple concurrent prompts**: The only confirmation gate for shot content is the 5.0 whole-film table (one pass for the entire film; no second confirmation at the prompt stage); **video generation runs multiple 15s prompts concurrently and simultaneously, with no segment-by-segment pause for confirmation**, and each segment keeps anchors consistent so the segments can be stitched in sequence.
- **Sound handling: fully silent at the SD2 stage (no sound at all)**: SD2 prompts of all durations **contain no sound whatsoever** — no BGM/background music, no sound effects/ambient sound, no narration, no single tones/scales/instrument notes/beats or any other sound; **SD2 generates pure visuals only (silent video)**. Narration and BGM are all left to be added during Step 6 post-production compositing. The prompt body only describes visuals (subject/action/camera/product), with no sound descriptions of any kind.
- **Narration**: SD2 is silent; narration is **never written into the prompt** — it is all left to Step 6 post-production, to be added via TTS/voiceover (the copy was already confirmed in the 5.0 table; the voice follows the choice on the Step 2 inquiry card).
- **Generation resolution**: Per the 480p / 720p / 1080p confirmed in Step 2, set the corresponding output resolution parameter when calling SD2 (not written into the prompt body; it is an independent parameter of the generation call).
- **Video aspect ratio**: Per the 16:9 / 4:3 / 9:16 / 3:4 confirmed in Step 2, set the corresponding frame format when calling SD2 (the Step 3 scene atmosphere image's `--ar` should match as well, ensuring the background image and the final film share the same frame); the body may state the frame format at the start (e.g., "landscape 16:9" / "portrait 9:16").
- **Tone-reinforcement sentence (always appended after the quality sentence)**: e.g., "ad-grade commercial color grading, with a clear, bright, and layered image, naturally saturated colors without graying, sharp highlights and material sheen; avoid a dark/gray/low-contrast sunken feel" — the core demands (clarity/brightness/sharpness/no graying) must be kept.
- **Motion-quality sentence (always added at the end)**: silky-smooth camera movement, stable frame rate, no dropped frames/stuttering/jitter, natural motion blur; for orbit/rotation shots, additionally write "slow, constant-speed orbiting, smooth continuous rotation" and slow them down (most prone to stuttering; prefer slow over fast).
- For details see `references/seedance-output.md` (shot size/camera movement/Cut vocabulary, continuation phrasing, and examples of each technique).

### Step 6 · Video Compositing, Narration Voiceover, Subtitles, and Music Scoring (Final Film Output)

After the user generates the clips in Seedance with the prompts above, return to this step to finalize the film:

- **Editing & compositing**: **For 30s / 60s, stitch the multiple segments in storyboard order into the complete final film** (using ffmpeg / an editing pipeline), unifying frame format and frame rate and handling inter-segment transitions; a single 15s segment can be output directly as the final film.
- **Narration post voiceover (when narration was selected in Step 2)**: The SD2 video is silent; generate the narration via TTS / voiceover with the selected voice (the copy was already confirmed in the storyboard table), align it with the visuals, and mix it in.
- **Add subtitles (when subtitles were selected in Step 2)**: Add narration subtitles per the choice — **Chinese / English / Chinese-English bilingual** — matching the narration copy and appearing on screen in sync with the narration's rhythm; the styling is simple so it doesn't compete with the picture (fitting the New Chinese guochao temperament). Subtitles are added before compositing in this step; if subtitles were not selected, do not add them.
- **Generate music (generated uniformly in this step for all durations, not produced with SD2)**: After the shots are complete and stitched into the final film, generate a guofeng-electronic fusion track (classical instruments × modern electronics, see Section 3), with the **BPM set according to the final film's actual rhythm/tonality** (fast films get strong groove, slow films get a sense of space; tempo may vary within the film), and a duration strictly matching the final film; the SD2 video is a silent picture, so mix in the BGM together with the post-production narration (if any), with the narration taking priority and the BGM not overpowering the voice, and output the final version with music + narration.

---

## Locked Style Block (Fixed Live-Action Base · Use As-Is)
This skill always uses the live-action style; the cinematic commercial base below is the sole base, with the overlay phrases below added as needed.

**Cinematic Commercial Base (Live-Action) · EN:**

```
A high-end commercial film, cinematic masterpiece, commercial-grade lighting and
color grading, crisp clean image, shallow depth of field, premium product-film
aesthetic, natural film-scan color fidelity (no over-warm filter).
```

**Cinematic Commercial Base · ZH:**

```
High-end commercial film, cinematic masterpiece, commercial-grade lighting and color grading, crisp clean image, shallow depth of field,
premium product-film aesthetic, natural film-scan color fidelity (avoid an over-warm filter feel).
```

**Overlay phrases**: demo `+ clean seamless studio backdrop, macro detail, even soft key light, product hero shot, slow-motion reveal`｜audiovisual spectacle style `+ new-Chinese-style fashion-film energy, dynamic slider/crane motion, music-driven rhythm, rich material texture`｜new-Chinese guochao `+ new Chinese aesthetic, ink-wash negative space, traditional Chinese architectural silhouettes, cloud/lattice patterns, silk and rice-paper texture, Chinese red and antique gold palette`.

---

## Reference Files

- `references/seedance-output.md` — numbered storyboard / continuous prompt formats, shot-size / camera-movement / Cut vocabulary, and examples of each creative technique.
- `scripts/extract_frames.sh` — frame extraction for reverse-engineering reference commercials + spec reading.

## General Constraints (Quick Reference · See the Corresponding Step for Details)

- **Both product-anchor images are mandatory**: after the product is uploaded and before the dimensions are confirmed, \*\*must use the uploaded product image as the reference (image-to-image, not text-to-image)\*\* to generate `{{product three-view}}`+`{{product detail image}}` (white background, 16:9); if the shape/color scheme/brand logo don't match, regenerate — this cannot be skipped; when the space itself is the product (real estate/hotel), use `{{real-space photo}}` instead.
- **Product anti-drift (feed the reference every segment)**: when SD2 generates video, **every 15s segment must have the same set of** `{{product three-view}}`**+**`{{product detail image}}` **fed in as image reference** — not just the opening segment; whenever the product appears on screen it must be complete, clear, and not excessively occluded, and the prompt must explicitly state "the product strictly follows the anchor images — no deformation / no color change / no altering the logo"; compare segment by segment, and on any drift, check whether a reference was missed and regenerate that segment.
- **New-Chinese guochao only**: scenes/props/patterns/colors/styling must all stay within the guochao (China-chic) language, with no mixing of Western fashion/cyber styles, etc.
- **Fixed style seed**: MJ uniformly uses `--sref 4608797467 --profile nn1ntrp` + `--v 8.1`; do not show the code, do not offer options, and no swapping is allowed.
- **Styling branching**: first ask for face/styling reference images; based on ① face only ② styling only ③ both ④ neither, decide whether MJ uses an image reference and whether faces in the three-view are covered (**face images are never fed to MJ, only fed at the SD2 stage**; with a face image → the three-view covers the face with a white circular sticker plus small Chinese text in the bottom-right corner "Face provided separately · This image is for outfit-styling reference only"; without → keep the MJ face). MJ outputs only one set of front-facing images (full body/three-quarter body preferred, `--ar 3:4`) and runs one round of pick-1-of-4 (options labeled 1 top-left / 2 top-right / 3 bottom-left / 4 bottom-right); after selection, LibImage expands it into a full-body three-view locked as `{{Mixed N}}`.
- **The scene atmosphere image must be a pure empty shot + large scene**: environment only; no products/people/human shadows/hands/animals/text/logo; the prompt explicitly includes negatives (no people/no product/no text/empty scene); and it must be a **panoramic/extreme-wide space that can accommodate a full-body model moving through it** (tall open ceilings and ground-level depth — not a tabletop installation or a partial counter); if it contains a subject or is too small to fit a person, it fails and must be regenerated.
- **Scenes are carried by the image**: storyboard scenes are always carried by the selected `{{scene atmosphere image}}` (or `{{real-space photo}}`); **the body text no longer describes the scene/environment/color palette in words**; in the live-action photo category, every shot must take place within the `{{real-space photo}}`, and no fictional spaces may be invented. **Product close-ups/macro/usage shots must also occur within the selected scene** (the product may rest on a support object within the scene + shallow depth-of-field blur); **jumping to a white studio/solid-color backdrop is strictly forbidden**.
- **Two-level pacing: the table is confirmed once, videos are generated concurrently**: the sole confirmation gate for shot content is the 5.0 **full-film storyboard table** (list however many seconds the film needs, output the whole film in one pass, confirm once; prompts are not confirmed a second time); **videos are multiple 15s prompts generated concurrently in parallel, with no segment-by-segment pauses for confirmation**, each segment kept consistent by the unified anchor and splicable in sequence. Prompts are delivered in Chinese as the model's internal execution layer; the user does not need to paste them manually.
- **Two mandatory shots**: the film must include **at least one product-usage close-up** (real usage actions such as a brush sweeping powder / a fingertip dabbing cream / a hand pouring tea from a pot, highlighting texture/function); **the end card must be a medium close-up with the model and product in the same frame** (worn if wearable, hand-held if it can only be used/consumed); with multiple segments, this is counted over the whole film (the end card is the final shot of the last segment).
- **Mandatory human presence**: every film must include a person (fully on screen, or hands/partial body); never a film with no people at all; camera moves still richly showcase the product/space.
- **No logo by default**: no logo at the end and no asking, unless the user explicitly requests it; if there is a slogan, the video model renders it as on-film subtitles; if not, the product hero/visuals close out naturally.
- **SD2-generated video is fully silent; all sound is post**: at the SD2 stage, **only pure visuals are produced, with no sound generated at all** (no BGM, no SFX/ambient sound, no narration, no single tones/instrument notes/beats); the finished film's audio has only two layers — **BGM + narration (if any)** — all added in Step 6 post: BGM is fixed as "a guofeng electro-fusion of Chinese classical instruments × modern electronics" (neither pure folk nor pure electronic), BPM follows the film, no asking the user, generated to match the finished film's rhythm/tonality before compositing; narration uses post TTS/voice-over per the Step 2 choice; **no SFX layer of any kind**; in the mix, narration takes priority and the BGM must not cover the voice.
- **Subtitles (only if narration was chosen)**: subtitles (Chinese / English / Chinese-English bilingual / none) may be chosen only when narration was selected in Step 2; subtitle text matches the narration script, added before compositing in Step 6, in a clean style that fits the guochao temperament; if narration was not chosen, subtitles do not apply.
- **Video aspect ratio + resolution must be chosen by the user**: aspect ratio (16:9/4:3/9:16/3:4) and resolution (480p/720p/1080p) have no defaults; Step 2 must ask, and SD2 sets the frame size and output accordingly.
- **Tonal enhancement**: After each prompt's quality sentence, always append — transparent and bright, clear layering, no grayish color, sharp luster; avoid dullness/muddiness, and maintain a premium, translucent China-chic (guochao) feel.
- **Silky camera movement**: Always add a motion-quality sentence at the end (no dropped frames / no stutter / silky + natural motion blur); orbit/rotation shots are especially prone to frame drops — write "slow, uniform-speed orbit, smooth continuous rotation" and slow it down.
- **Shot continuity**: No frame jumps, no crossing the axis (keep the 180° rule); camera positions and motion logic must be coherent. When continuing across 15s segments, keep `{{Mixed N}}` / wardrobe / scene / lighting consistent to avoid continuity errors.
- Use `{{Mixed N}}` for characters — write it in full on first appearance, reuse it thereafter, and keep subject/object clear; for demonstration videos, ensure the product is clear in every shot.
- Each video carries only one core message; hook viewers in the first 3 seconds, and the ending must land on a clear point.
- **Expressions must be natural and believable — no exaggeration or weirdness**; **no dissolve/crossfade transitions**; **no particle effects** (too tacky — use clean light effects / seamless morphing / material textures instead).
- No content featuring real public figures; no fabricated false claims about real brands; keep it appropriately harmless.