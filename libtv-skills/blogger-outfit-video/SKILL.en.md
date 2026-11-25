---
name: blogger-outfit-video
description: "Outfit recommendation video: one-click generation of Xiaohongshu-style blogger outfit haul videos"
---

# FitCast · Outfit Try-On Haul Video

Flow: garment analysis + model setup → garment white-background images (base layer + target) / default close-up character three-views (if no user model) → scene image → action script → video prompt (silent) → BGM compositing

**Core tone**: authentic Xiaohongshu-blogger realism — absolutely no AI look / greasy look / cinematic look; casual smartphone-shot feel throughout.

---

## STEP 0: Opening Q&A

```
① Please choose a model: 1. AI auto-matched model / 2. Upload a model photo
② Brand/content positioning ③ Target audience ④ Scene space: living room / bedroom / entryway
⑤ Output: a 15-second single-shot video (catch garment → on-body transformation → fixed-spot pose → three-beat showcase → freeze frame); the video itself is silent (no sound effects / no voiceover), with BGM overlaid at the final compositing stage
```

---

## STEP 1: Garment Analysis + Model Setup

Analysis output: category / style tags / dominant color / material / cut / item count / accessory list (if any)

Path A matches the model by style + audience: Minimalist commuter → gentle and refined / Sweet-cool Y2K → bubbly and smiley / French vintage → laid-back and approachable / Street techwear → sunny and cheerful / Resort forest style → warm and soothing / Loungewear → relaxed and easygoing

**Default realistic model library (used when "AI auto-matched model" is selected and no specific look is specified; personality and vibe are still matched per the style tags above; this library is used to generate the STEP 2 ③ default close-up character three-views)**:

Female model: Asian woman, 165-172cm, natural makeup look, visible pore texture + light freckles, no CG / no skin-smoothing, naturally uneven hair strands, clean features that aren't influencer-face, relaxed feel > posed feel.

Male model: Asian man, 175-182cm, short hair or slightly curly fringe, natural pore texture, no CG glossiness, vibe somewhere between campus and urban, clean features without being overly refined.

Path B: analyze the user's model photo, identify body shape / skin tone / hairstyle / facial features, and output a feature card (the user's uploaded original model photo later serves directly as the character strong-reference source at the video-generation stage — see STEP 5 — no AI re-generation needed)

---

## STEP 2: Garment White-Background Images (all without people) + Default Close-Up Character Three-Views (only needed when there is no user model)

```
① Base-layer garment three-view: fitted wide-strap tank top (covers the belly, no exposed chest) + summer above-knee tight cycling shorts; white background, no people, front/side/back three angles, showing only the garment's own cut and details.

② Target garment three-view: if the user has already uploaded a garment three-view, skip this step and use it directly; if the user uploaded a single-item photo / flat-lay photo, generate a white-background, no-people, front/side/back three-view showing only the target garment itself. After generation, garment details (e.g., skirt length) can be manually fine-tuned; the adjusted result is carried by this three-view and referenced in STEP 5.

③ (Case B only — needed when "AI auto-matched model" is selected) Close-up character three-view: white background, front/side/back three-angle bust portrait (no full body; use "bust" as the precise shot-size descriptor in the generation prompt), rendering the facial features / hairstyle / skin quality defined in the STEP 1 default realistic model library.

Unified for ①②: photorealistic garment-only photography on white background, no model/person, no text/watermark/logo/shadow, accurate fabric texture/color/cut

Unified for ③: photorealistic white background bust portrait, no text/watermark/logo/shadow, soft natural frontal fill light on face (no backlight/shadow on face), skin strictly follows the default model library settings (no added dark circles/dullness/redness/blemishes), matte skin—no shine/gloss but pores/texture retained (not smoothed/CG/plastic), light natural makeup not bare-faced, alert expression, no tired look/under-eye bags
```

Confirm ①: ✅ Continue / ✍️ Edit [garment / model / base layer]

---

## STEP 3: Scene Image (scene only, no people)

Style (fixed): **Mid-century Modern Mix**, with the texture of an old European apartment; pick the matching version for each space; lighting is unified to avoid clashing with the subject's lighting.

**Living room**: matte white walls + dark solid-wood floor, low storage cabinet / steel-frame chair, geometric rug (corners naturally curling up, not perfectly flat), 2-3 framed 70s prints, warm wood + mustard yellow / brick red / cobalt blue accents, greenery (leaf orientation not perfectly symmetrical); sofa cushions casually tilted / asymmetrically placed, throw blanket naturally piled rather than neatly folded.
**Bedroom**: warm white walls + dark walnut headboard, contrast-color throw pillows, ceramic table lamp, 1-2 framed prints, palm plant, dark walnut + warm yellow / brick red / blue-grey accents; **bed sheets / duvet cover with slight natural wrinkles (not an ironed-flat look)**, pillows not perfectly symmetrically arranged and may show slight indentations, and a casually tossed light jacket or blanket may drape at the foot of the bed.
**Entryway**: matte white walls + dark solid-wood floor, floating entryway console, irregular-shaped wall mirror, 1 framed print, greenery / dried flowers, dark wood + matte metal + 1 accent color; the console top may hold casually placed keys / a bag / a pair of shoes, avoiding an absolutely tidy staged look.

**Lived-in traces (unified requirement across all three versions)**: every scene must retain slight lived-in traces (wrinkles, asymmetric placement, casually set-down items), avoiding over-refinement / perfect symmetry / show-flat feel, creating the impression of "a real, inhabited home" rather than a "studio set"; but no dirt / messy piles — the trace feel must stay restrained and natural. Repeated cloned elements in the frame are forbidden (e.g., identical leaf / floor-tile patterns, suspected stamp-copy artifacts).

Lighting (unified across all three versions): natural daylight feel, bright and airy (high-key airy daylight), soft diffused indoor light, even without overexposure, frontal front lighting, avoiding a single hard light source with localized specular reflections; dim / underexposed / moody tones are forbidden — dark tones drag the person down with them and amplify dark spots / noise.

Adjustment method: upload real photos of your home; the AI reads their aesthetics and recreates a fusion with Mid-century Modern Mix; lighting still follows the base tone above.

```
Generate [living room / bedroom / entryway], no people. [corresponding scene tone][unified lighting tone]
9:16 vertical composition; if a reference image is provided, generate by blending in its aesthetics.
shot on smartphone, bright airy daylight, natural indoor lighting, no text/watermark/logo, no cinematic lighting, no moody/dim tone
```

Confirm ②: ✅ Move on to the video stage / ✍️ Edit [scene elements / lighting] (once confirmed, this is the sole standard for the whole video)

---

## STEP 4: Action Script (single shot, 15 seconds)

**Expression baseline**: nonchalant confidence / playful light laugh / relaxed eyes looking straight into the camera (except when turning / back to camera).

**Transformation mechanism**: the item is tossed / handed in from off-frame (not "flying on and wearing itself"); both hands catch it → both hands open to display the garment itself — tops / bottoms / outerwear are all treated the same; bottoms must not skip the display step by being dropped straight down or pulled on directly. After the display, the transformation completes the instant the item meets the body: single item / one-piece — camisole + cycling shorts vanish simultaneously; multiple items — repeat the mechanism item by item, with the top's wear-in removing only the camisole and the bottom's wear-in removing only the cycling shorts (removed per body part, not simultaneously). Once on, bottoms must fit as securely as the top; no slipping-down / coming-loose shots at any point.

Once fully dressed: **fixed-spot pose** (accessories shown at the same time, if any) → **three-beat showcase**: camera locked in place, the blogger rotates counterclockwise on the spot (not the camera orbiting the blogger), with natural weight shifts, hair and hem moving along, synchronized subtle foot shifts and hand gestures (hair flip / touching the hem / hand on hip); the pauses are natural breath-like holds rather than sculpted freezes — front (brief accessory interaction) → side pause on the beat → back pause on the beat → back to front, continuous with no jump cuts → **freeze-frame ending**: walk toward the camera to interact, or close with a fixed-spot pose in place.

Timing reference: single item — transformation ~3-4s / fixed-spot pose ~1-2s / three-beat showcase ~6-7s / freeze ~2-3s; multiple items — transformation ~2.5-3s per item, with the rest following the single-item version but compressed accordingly.

**Accessories**: not added by default; shown only when the user explicitly requests them in conversation.

Confirm ③: ✅ Generate the prompt set / ✍️ Edit [actions / pacing]

---

## STEP 5: Video Prompt (the video itself is silent)

Tool: prefer Seedance 2.0; if results are unsatisfactory, switch to Kling 3.0 Pro.

**Reference-image roles (principle: use as the strong reference the image with the fewest AI generation passes, reducing compounding distortion artifacts from stacked generations)**:

- **Case A (user-uploaded model photo)**: fixed uploads: user's original model photo + base-layer garment three-view + garment three-view + scene image. Person → user's original model photo; base-layer garment look → base-layer garment three-view; target garment form → garment three-view; environment → scene image.
- **Case B (AI auto-matched model)**: fixed uploads: default close-up character three-view + base-layer garment three-view + garment three-view + scene image. Person → default close-up character three-view; base-layer garment look → base-layer garment three-view; target garment form → garment three-view; environment → scene image.

**IPHONE-CANDID aesthetic baseline**:

```
Avoid: no cinematic lighting, no hyper-realistic, no 8k/masterpiece, no oversharpening, no blown-out highlight noise across frame
Camera: static shot, phone on stand, no camera movement/zoom, consistent medium shot down to below knee/calf, centered with negative space, stable background, soft focus falloff
Color: warm neutral white balance, soft creamy undertone, gently muted tones, VSCO-style not cinematic grade, mild contrast, avoid muddy grey midtones
Lighting: soft diffused bright indoor lighting, gentle highlight falloff (no blown highlights), soft natural frontal fill light on face (no backlight/shadow on face), no hard specular source, no backlight/silhouette
Texture: shot on smartphone, subtle sensor noise/grain, matte skin (no shine, pores/texture retained, not smoothed), skin strictly follows reference (no added dark circles/dullness/redness/blemishes), natural hair strands, unposed candid feel
```

### Video Prompt

```
⚠️ Hard constraints (self-check before generation, top priority):
① No segmentation: Steps 1-4 are one continuous action sequence within a single fixed camera position, and must be generated in one pass as a single unbroken 15-second long take; splitting into multiple clips / segment-by-segment generation is forbidden, and it is strictly forbidden to split the transformation and the three-beat showcase into two separately output segments.
② Locked shot size: hold a medium shot throughout (framing may extend down to above the calf); the person always remains the frame's main subject with a stable size share; do not pull back to a full-body or wide shot because of the rotation / walking / showcase moves; camera position and focal length stay unchanged throughout.
③ No three-view bleed: the base-layer garment three-view / garment three-view are only for extracting the garment's form / cut / length and other details; the three-views' own visual elements (white background, flat-lay / hanging composition) must not bleed into the video; only the home scene appears throughout — no white-background / studio shots.
④ Subject placement: the blogger must stand in the scene's most evenly and amply lit, front-lit zone facing the main light source; avoid standing in a dark corner / backlit position.

Based on the reference images (assigned per the STEP 5 reference-image roles): character identity follows the strong reference source (Case A: user's original model photo; Case B: default close-up character three-view); the scene follows the scene image; the base-layer garment look follows the base-layer garment three-view; the final form of the target garment (including manual tweaks such as skirt length) follows the garment three-view (wearing the complete outfit from the garment three-view, scope limited per constraint ③); apply the IPHONE-CANDID baseline.
Step1: the item (for multiple items, in order: top → bottom [→ outerwear]) is tossed / handed in from off-frame (not flying on and auto-wearing); both hands catch it, then both hands open to display it (bottoms likewise must be displayed, not dropped straight down or pulled on directly); the transformation completes the instant the item meets the body (single item: camisole + cycling shorts vanish simultaneously; multiple items: repeat item by item, top wear-in removes only the camisole, bottom wear-in removes only the cycling shorts, and bottoms fit just as securely without slipping).
Step2: once fully dressed, strike a playful fixed-spot pose (if there are accessories, show the look with them at the same time).
Step3: three-beat showcase; camera locked in place, the blogger rotates continuously counterclockwise on the spot (not the camera orbiting the blogger), weight shifts natural, hair and hem moving with the motion, synchronized subtle foot shifts and hand gestures / hem touches; the pauses are natural breath-like holds rather than stiff freezes — front (accessory interaction) → side pause on the beat → back pause on the beat → back to front, continuous with no jump cuts, holding the medium shot (above the calf) throughout without pulling back.
Step4: freeze-frame ending — walk toward the camera to interact (without changing the shot size) or close with a fixed-spot pose in place, eyes on the camera.
[hair/fabric physics feedback][mood: nonchalant confidence / playful light laugh]
The video itself contains no audio (no sound effects, no voiceover, no BGM); generate it muted — music is generated separately in STEP 6 and composited at the final-cut stage.
9:16, ~15s, single continuous unbroken shot, no scene splits, medium shot down to below knee/calf throughout, no text/watermark/logo, silent/no audio
```

## STEP 6: BGM Style Library (4 categories) + Auto-Matching

The video itself is silent (no sound effects / voiceover / BGM). After generation, a separate music tool is called to generate the BGM (duration matched to ~15s), which is then composited with the video into the final cut.

**Auto-matching logic**: automatically match the BGM type based on the garment style tags parsed in STEP 1 (the user can override via conversation):

| Garment style tag | Matched BGM type |
|---|---|
| Minimalist commuter | A Mature & Sexy |
| Sweet-cool Y2K / Loungewear | B Cute & Fresh Korean Style |
| French vintage / Resort forest | C French Resort Chill |
| Street techwear | D Street Cool |

### A | Mature & Sexy
Style reference: Ravyn Lenae "Love Me Not" (retro-pop + indie-rock-textured R&B)

```
Style: retro-pop / indie-rock R&B, sweet 60s girl-group groove + gritty indie-rock guitar, not an electronic-pop arrangement
Rhythm: 114 BPM, 4/4, simple crisp drum patterns (not dense syncopation), Motown-style handclaps, prominent groovy bassline
Harmony: C major, simple chords (I-IV as the backbone, with one secondary dominant allowed)
Instruments: guitar-led — bright jangle guitar + lightly distorted gritty guitar layered across multiple tracks; clear bass underneath; handclaps + simple drum kit; no synth stacking
Mood: light and sweet with a touch of nonchalance; relaxed > tense; no dance-track sense of being rushed
Texture: warm and vintage, evoking the rough edges of old recording studios
Vocals: instrumental only; Duration: ~15s
```

### B | Cute & Fresh Korean Style
Style reference: fresh Korean acoustic-pop in the style of AKMU

```
Style: fresh Korean acoustic-pop, acoustic guitar as the backbone, light melody with a playful touch, not a heavy electronic arrangement
Rhythm: 100-112 BPM, 4/4, light bouncy groove, nimble drums, optionally accented with crisp claps / xylophone
Harmony: bright major key, simple clean chords, avoid a melancholic minor
Instruments: acoustic guitar-led + crisp keys / xylophone accents, keep heavy bass minimal, overall light and airy
Mood: healing + campus freshness + a hint of playfulness; not sexy / not heavy
Texture: clean and translucent, with a slight acoustic-recording feel
Vocals: instrumental only; Duration: ~15s
```

### C | French Resort Chill
Style reference: French chill/lounge, nu-disco-style laid-back groove

```
Style: French pop/chill lounge, lazy relaxed vacation feel, never rushing
Rhythm: 90-104 BPM, slow swaying feel, loose drumming, a blend of real drums + light electronic drums
Harmony: warm major key with a light jazz tinge (e.g., added 7ths)
Instruments: bright / lightly distorted guitar + warm bass, optionally accented with light electric keys or harmonica
Mood: relaxed and cozy + sunny feel, nothing intense or hurried
Texture: warm analog feel, looser and lazier than group A
Vocals: instrumental only; Duration: ~15s
```

### D | Street Cool
Style reference: alt-rock/street rock (scaled to the intensity of a 15-second short, not extreme heavy metal)

```
Style: alt-rock, driven by distorted electric guitar riffs, impactful but not oppressive
Rhythm: 120-140 BPM, strong straight-ahead drums, driven by snare + hi-hat
Harmony: mainly minor key / power chords
Instruments: distorted electric guitar-led, tight drums, electric bass adding thickness
Mood: rebellious confidence + boldness, high impact but kept within short-video BGM scale
Texture: modern rock mix feel, punchy and forceful
Vocals: instrumental only; Duration: ~15s
```

Confirm ④: ✅ Generate the BGM with the matched type / ✍️ Specify another type [A/B/C/D]