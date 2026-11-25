---
name: luxury-brand-tvc-creator
description: "Luxury-brand TVC: luxury-grade visual expression and cinematic audiovisual language for international, high-end brand TVCs"
---

## I. Category Classification (Identify the Category from the Uploaded Product, Take the Defaults)

Each category comes with three fields—"rhythm tone / product appearance timing / per-shot duration" (see the rhythm table below for details); set the category and you get all three at once. Note: "per-shot duration" refers to the suggested duration of each shot **within a single clip** (for the model's reference when auto-splitting shots inside that one 15s clip); it does **not** mean you should initiate generation shot by shot at this duration.
Beauty / Skincare — Traits: macro close-ups, flowing textures, skin sheen, facial emotion, luxurious ambiance; Default creative approach: demonstration + emotion; Rhythm: medium·gradual build / product at 3–5s / per-shot 2–3s; Brands: Dior, SK-II, La Mer
Luxury / Fashion — Traits: short-film-style cinematic storytelling, artistic composition, minimalism, generous negative space; Default creative approach: story / emotion (audiovisual-spectacle style); Rhythm: slow·negative space / product at 4–6s / per-shot 3–5s; Brands: Hermès, Chanel, Prada
Food / Beverage — Traits: appetite-appeal close-ups, flowing liquids, steam/water droplets, high saturation, brisk rhythm; Default creative approach: demonstration + emotion; Rhythm: fast·beat-synced / product at 1–3s / per-shot 1–2s; Brands: Coca-Cola, McDonald's
Tech / Electronics — Traits: floating product, 360° orbit, dark tones + neon light, futuristic feel, interface animation; Default creative approach: demonstration + animation; Rhythm: medium-fast·precise / product at 2–4s / per-shot 1.5–2.5s; Brands: Apple, Samsung, Sony
Spirits / Fragrance — Traits: slow motion, light refraction, liquid texture, atmosphere over function; Default creative approach: emotion (audiovisual-spectacle style); Rhythm: slow·atmospheric / product at 4–6s / per-shot 3–5s; Brands: Moutai, Chivas, Jo Malone
Sports / Outdoor — Traits: high-speed photography, extreme scenes, sweat/muscle close-ups, inspirational emotion; Default creative approach: emotion / story; Rhythm: ultra-fast·impact / product at 1–2s / per-shot 0.5–1.5s; Brands: Nike, Adidas, The North Face
Automotive — Traits: grand scenes, aerial shots, sense of speed, extreme light and shadow, lifestyle narrative; Default creative approach: story (audiovisual-spectacle style) + demonstration; Rhythm: slow start accelerating / product at 3–5s / per-shot 2–4s→tighten at the end; Brands: BMW, Mercedes, Tesla
Finance / Insurance — Traits: family scenes, heartwarming narrative, sense of trust, steady tone; Default creative approach: story + emotion; Rhythm: medium·heartwarming / product per the plot / per-shot 2–4s; Brands: Ping An, Prudential
Real Estate / Hotels — Traits: aerial panoramas, indoor light and shadow, lifestyle imagination, sense of space; Default creative approach: emotion / story; Rhythm: medium·unhurried / the space is the product / per-shot 2.5–4s; Brands: Vanke, Four Seasons

Setting the category gets you: default traits + suggested creative approach + a set of default knob settings (see the bracketed notes in Section III) + the three rhythm fields (see the rhythm table in Section V). Override the defaults only if the client has special requirements.

> The real brands in the category names serve only as **abstract style descriptions** (to convey the tone of this kind of ad); the finished film must not reproduce any recognizable elements of any specific brand's actual campaigns (signature sets, proprietary visual symbols, real slogans/logos)—replace all logos with the product's own logo.

---

## II. Five Dimensions (Confirm Each Item Through Dialogue with the User)

The 5 dimensions of a TVC commercial. Once the category is set, most already have default values; the dialogue only needs to fill in/correct them—do not re-ask items already known.

1. Ad Purpose: product · brand · image · promotion · public service → determines information density and the closing beat: promotion = strong CTA; brand/image = logo ending; product = selling points + CTA.

2. Creative Approach (= prompt generation skeleton): story · emotion · demonstration · animation

   Story: a complete plot—setup → conflict → resolution—with the product woven into the storyline.

   Emotion: an emotional arc that moves people—establish character/situation → emotional peak → product as the solution → land the proposition. Use {{Mixed N}} to lock the character.

   Demonstration: selling points delivered directly—pain point/scenario → product entrance → one selling point per shot → results shown → logo + CTA. The product is clear in every shot.

   Animation: 2D / 3D / stop-motion; the style-lock sentence goes first; style consistency &gt; character consistency.

   "Audiovisual spectacle / fashion film" is not a standalone approach but a high-production aesthetic style (dense camera movement, aesthetics first, slow motion, generous negative space); it is usually layered on top of story/emotion/demonstration (luxury, beauty, automotive), built up by stacking the breakdown elements in Section III.

3. Video Length: 15s · 30s · 60s → **determines the number of clips (15s=1 clip / 30s=2 clips / 60s=4 clips)** and triggers the generation split (see Workflow Step 3). Within each clip, the model further auto-splits the shots according to the rhythm (15s≈4–5 shots / 6–8 shots at fast rhythm); **this is an internal matter of the clip, not a split into separate generation tasks**.

4. Production Method: live action · animation · CG composite · mashup edit → determines the base of the style-lock sentence: live action = cinematic commercial base; animation/CG = the corresponding style-lock sentence.

5. Placement Scenario: TV · OTT · social media vertical · outdoor big screen → determines aspect ratio and rhythm: TV/OTT = 16:9; social media vertical = 9:16 with an even harder-hitting first 3 seconds; outdoor big screen = strong visuals, minimal reliance on sound. When needed, one draft produces both versions.

---

## III. Breakdown Elements (7 Knobs · Options Menu)

Choose one setting for each dimension; the notes in italics are the "defaults by category".

1. Lighting Design

   Light source: natural light / studio artificial light / mixed light

   Direction: front light / side light / three-quarter back light / back light / top light / bottom light

   Lighting setup: Key light, Fill light, Rim/Edge light, Backlight, hair light, Volumetric (Tyndall) light, Beauty dish, Practical (in-frame) light

   Color temperature: cool (blue-white) / warm (gold-orange) / neutral / warm-cool contrast

   Special light effects: neon, RGB tinting, lens flare, refracted light spots, flowing light bands, strobe

   Default: beauty/food = soft, airy warm tone; tech/auto = dark tone with Rim + neon; luxury = natural window light; finance/real estate = warm, soft natural light

2. Color Grading

   Color temperature: warm / cool / neutral / warm-cool split-tone

   Tone: film-scan natural film color, teal-orange cinematic grade, vintage faded, Japanese fresh, Morandi low-saturation, cyber neon, black-and-white

   Saturation: high saturation / standard / low saturation / desaturated monochrome

   Texture overlays: film grain, light-leak halation, soft glow, glitch noise

   Default: food = high-saturation warm; luxury/fashion = low-saturation film-scan; tech = cool blue dark tone; auto = teal-orange

3. Camera Language

   Camera movement: static, push/pull, pan, dolly, crane, orbit, tracking, handheld, stabilizer, FPV fly-through

   Shot size: macro/extreme close-up, close-up, medium close-up, medium shot, full shot, extreme long shot, aerial

   Angle: eye level, low angle, high angle, top-down flat lay, Dutch angle (tilted)

   Composition: centered symmetry, rule of thirds, frame-within-frame, generous negative space, full composition, foreground occlusion

   Lens characteristics: wide-angle distortion, telephoto compression, tilt-shift miniature effect, fisheye

   Default: beauty/tech = macro + orbit; auto/sports = aerial + tracking + FPV; luxury = negative space + slow push-in; food = top-down + slow-motion macro
Supplementary Camera Moves (grouped by purpose · richer audiovisual language)

   A. Dynamic/Impact (for Food/Sports/Tech/Promo)

   - Speed ramp: normal speed → sudden slow-mo → back to speed, the beat-syncing wonder tool
   - Whip pan: fast horizontal whip transition, a "whoosh" between two shots
   - Push-in to macro: one shot pushing from medium shot right into product macro
   - Snap zoom: the focal length jolts abruptly, punctuating an instant
   - FPV fly-through: one shot flying through the scene/inside the product, immersion maxed out

   B. Precision/Showcase (for Tech/Beauty/Product hero)

   - Product orbit teardown: half orbit + components highlighted one by one (cures "logo-only close-ups")
   - Top-down flat-lay + crane: overhead shot of a product array, paired with a crane reveal
   - Dolly/slider: smooth lateral glide across the product lineup
   - Macro slider: slow glide hugging the product's surface/texture
   - Rack focus: foreground goes blurry→sharp, guiding the eye to the product

   C. Emotion/Cinematic (for Luxury/Spirits/Auto/Finance)

   - Slow push-in: inching closer to the person/product, condensing emotion
   - Crane up/down: vertical movement that opens up a scene or brings it to a close
   - Subtle handheld: documentary feel, close to real life (finance/slice-of-life)
   - Reverse shot/over-the-shoulder: characters interacting, exchanging looks, building relationships
   - Aerial orbit: grand-scale momentum (automotive/real estate)

   D. Transition/Linkage (replacing cross-dissolves)

   - Match cut: shape/action/color alignment, two shots seamless
   - Action match: the action from the previous shot is carried to completion in the next
   - Occlusion transition whip/object wipe: an object sweeps across the lens, cutting to the next scene

   Every camera move above still carries the motion-quality constraints (silky-smooth movement, no dropped frames, orbit/360/rotation types slowed to constant speed).

4. Sound Effects & Music

   Music styles: orchestral epic, electronic, pop, hip-hop, lo-fi, jazz, folk, no music (silence)

   Music function: beat-synced driving, ambient underlay, emotional amplification

   Sound effects SFX: product ASMR (bite/pour/sizzle/spray), ambient sounds, foley, mechanical sounds, transition whoosh, UI chime

   Vocals: male/female narration VO, dialogue, crowd voices, no vocals

   Mixing: spatial reverb, silent breathing room, low-frequency ambient drone

   Defaults: food=ASMR+bright; tech/auto=electronic+mechanical sounds; luxury=sparse instrumentals; finance=warm strings+voiceover

5. Editing Pacing

   Cutting speed: fast cuts, medium pace, slow long takes, one-take

   Beat: cutting on drum hits, free narrative rhythm

   Transitions: hard cut, fade in/out, match cut, whip wipe, jump cut, liquid/light-effect transitions (dissolves/overlaps forbidden)

   Time treatment: linear, reverse, parallel editing, montage, freeze-frame emphasis

   Special techniques: freeze frame, speed ramp, datamosh glitch

   Defaults: food/sports/promo=fast beat-synced cuts; luxury/spirits=slow long takes; auto=slow start building fast

6. Actors & Models

   People present: with people / no people (pure product) / hands or partial only

   Demographic: young, urban white-collar, multi-generational family, children, sports-oriented people

   Persona style: premium cool, warm and approachable, athletic power, streetwise cool, fresh girl-next-door

   Diversity: local, internationally mixed, multi-ethnic

   Acting tone: restrained realism, slice-of-life, theatrical exaggeration (expressions must be natural and believable; exaggerated or bizarre expressions forbidden)

   Emotional focus: facial micro-expressions, gaze, body movement, interaction dynamics

   Wardrobe (by category): fit the category's tone — beauty = some skin shown but not revealing, stylish, elegant and minimal, colors not jarring; luxury/fashion = premium minimalism; sports = technical sportswear; finance/real estate = tasteful everyday wear

   Defaults: beauty=premium face+facial micro-expressions+skin glow are the focus; sports=athlete+physique; finance/real estate=multi-generational family; tech/spirits=usually no people

7. Story Type

   Narrative type: strong narrative (complete plot) / weak narrative (chained atmospheric spectacle) / no narrative (pure showcase)

   Structure: three-act, linear, non-linear montage, single-point demo, problem—solution

   POV: first person, observer, product POV, parallel multi-thread

   Story archetypes: slice of life, hero's journey, before/after comparison, testimonial endorsement, demo, brand manifesto

   Closing beat: logo lockup, product hero, tagline caption, CTA

   Defaults: finance/insurance=warm three-act; sports=hero's journey; beauty/tech/spirits=weak narrative; food=slice of life or pure showcase

---

## IV. Shot Pacing (cures "too slow / product shows up too late / stiff cuts")

> The pacing rules below govern the shot arrangement **within a single 15s clip** (shot count, per-shot duration, product appearance timing), as a reference for the model when automatically splitting shots within this one clip. They **do not change the generation granularity** — the generation unit is always the full 15s clip, never a single shot.

General pacing principles (category-agnostic)

No pure empty establishing shot as the first shot: with a model → the first shot must show the model in the scene (person + environment in the same frame, action allowed); no model (pure product) → the first shot may open with atmosphere/suspense, but the product must appear in the second shot.

A hook must land within the first 3 seconds, and the product must show up no later than seconds 5–8 (promo/demo types must show the product by second 3).

Keep it to 4–6 shots within one 15s clip, with no single shot over 3–4 seconds; fast-paced categories (food/sports/tech/promo) must have 6–8 shots per clip (see hard rules below).

Cut shot sizes by "skipping three levels" (extreme wide → medium → extreme close-up); don't creep in tiny steps between adjacent levels — only then do cuts avoid feeling sluggish and stiff.

Hard cuts as the default; dissolves/overlaps forbidden; when smoothness is needed, use a match cut or an action match, not a dissolve.

Pacing table by category (all referring to within a single 15s clip)

Category ｜ Pacing Tone ｜ Product Appears ｜ Per-Shot Duration ｜ Emotional Driver
Food/Beverage ｜ Fast·Beat-synced ｜ 1–3s ｜ 1–2s ｜ Bite/pour/sizzle sounds hit the beats; slow motion + sudden stop to spark craving
Beauty/Skincare ｜ Medium·Gradual build ｜ 3–5s ｜ 2–3s ｜ Slow start → texture close-up → eyes open to camera → settle on a glow payoff
Tech/Electronics ｜ Medium-fast·Precise ｜ 2–4s ｜ 1.5–2.5s ｜ Hard cuts synced with mechanical SFX; one feature, one selling point per shot
Sports/Outdoor ｜ Ultra-fast·Impact ｜ 1–2s ｜ 0.5–1.5s ｜ High-speed photography + speed ramp to pump adrenaline
Automotive ｜ Slow start building fast ｜ 3–5s ｜ 2–4s→tightens fast ｜ Grand scenes build momentum → cut closer for details → the final stretch accelerates to ignite
Luxury/Fashion ｜ Slow·Breathing room ｜ 4–6s ｜ 3–5s ｜ Long takes + slow push-in; nurture emotion through atmosphere and negative space, no chasing speed
Spirits/Fragrance ｜ Slow·Atmospheric ｜ 4–6s ｜ 3–5s ｜ Slow-motion light refraction; liquid texture lays down immersion
Finance/Insurance ｜ Medium·Warm ｜ depends on plot ｜ 2–4s ｜ Slice-of-life storytelling, a progressive emotional arc, product as the solution
Real Estate/Hotel ｜ Medium·Expansive ｜ the space is the product ｜ 2.5–4s ｜ Expansive aerial → interior light and shadow → lifestyle imagination

Hard rules for fast-paced categories (strong constraints · Food/Beverage, Sports/Outdoor, Tech/Electronics, plus promo purposes in any category):
Within a 15s clip there must be 6–8 shots (not 4–6); every shot must be ≤ 2s (sports/outdoor ≤ 1.5s), and no shot may exceed 2.5s (except the closing product lock-up shot, which must also not exceed 3s).

Each clip's storyboard must use at least 2 kinds of dynamic camera moves/transitions (choose from speed ramp, whip pan, snap zoom, push-in to macro, beat-synced hard cut, action match); the whole clip must not be nothing but slow push-ins/static shots.

Slow words like "slow push-in," "slowly," "leisurely" are banned from dominating the storyboards of fast-paced categories; use fast shot verbs such as "slam push-in," "rapid cut," "whip to," "instant punch-in" so the motion of the model-generated footage keeps up.

Every shot must have a clear action taking place (pour, bite, open, run, light up, pop); strings of static posed shots are not allowed.

After writing a clip's storyboard, self-check that total shot count × per-shot duration ≈ 15s; if the shot count can't be met, the pacing is too slow—go back and break up shots (**write a few more shots within this one clip's prompt, not split into multiple generation tasks**).

Core: for categories that should be fast (food/sports/tech/promo), front-load the product and hook, compress individual shot lengths, and cut on the beat; for categories that should be slow (luxury/liquor), keep long shots with breathing room, but they still need an emotional landing point—must not be flat.

---

## Workflow

### Step 1 · Generate product three-views + pop up the merged question card simultaneously

The user uploads a product image (or product description / reference video). Identify the category (Section 1), form/material/selling points, and whether {{Mixed N}} characters are needed; as soon as the category is identified, pull in the default traits + suggested creative techniques + default knob positions + the three pacing fields (Section 4).

① Generate a product reference image (faithful to the product; GPT Image recommended for fidelity; white background, 16:9) as the consistency anchor:

Product Three-View {{Product Three-View}}: front / side / back. After generation, always name it "Product Three-View", for direct attachment via @Product Three-View in Step 3.

Product Detail Three-View {{Product Detail Image}}: pick key details by function (juicer = logo / blade / buttons; skincare = bottle body / pump head / texture). After generation, always name it "Product Detail Three-View", for attachment via @Product Detail Three-View.

All subsequent storyboard product visuals must be based on these two images.

Real estate / hotels and other "space-as-product" cases: there is no physical product; instead upload or virtually generate 5–8 real-scene images {{Space Real-Scene}} (virtual generation at 16:9) to replace the product three-view and double as the scene anchor.

Reverse-engineering a reference video: first run scripts/extract\_[frames.sh](http://frames.sh) to extract frames and read the specs, then produce a matching version; **generate whole segments at 15s per clip—split 30s / 60s into 2 / 4 15s clips (each clip's prompt written out in full in one pass and generated as one whole segment); never split into many single shots generated one by one.**

② While generating the three-views, immediately pop up a merged ask_human question card (don't wait for the images to finish generating—saves time), asking everything in one pass (for items where the category already provides a default, just confirm / modify, with "you decide for me" left as an option; if the user says "you decide everything," proceed through with the defaults):

Duration: 15s / 30s / 60s (→ corresponding to 1 / 2 / 4 15s clips)

Ad purpose: product / brand / image / promo / public service

Production method: live action / animation / CG compositing / mashup edit

Creative technique: story / emotion / demo / animation (can be layered with audiovisual spectacle / fashion-film style)

Placement: TV / OTT / vertical social media / outdoor big screen (aspect ratio 16:9 or 9:16 set accordingly)

Brand slogan: fill in if available (used as the ending landing point)

Voiceover: yes/no + voice (male / female / neutral + style) + one of two voiceover languages (Chinese / English); always dubbed in post (video generated muted)

Subtitles: none / single language (which language) / bilingual (primary + secondary)

Choose model look (if models are used): give 3 options = "ethnicity/region + age + gender + hairstyle" (clothing not included yet); skip for pure product

Choose scene atmosphere: give 3 text options (scene + color tone + lighting + texture combined into one sentence), pick 1

Choose style seed: display only the Chinese style names (blue-orange cinematic / premium neutral cinematic / high-saturation retro warm blue / Japanese cinematic), never expose the code

Upload outfit reference image (if any): upload if available (subsequent character three-views will reproduce it with GPT Image 2)

(See Sections 2 and 3 for the meaning of each dimension; the voiceover script is written before Step 3 generates the video and given to the user for confirmation.)

### Step 2 · Produce the moodboard (scene atmosphere image + outfit images generated in parallel · requires user confirmation)

After the question card is answered, the scene atmosphere image and outfit images are generated at the same time (in parallel, to save time):

Scene atmosphere image (must use Midjourney v8.1): expand the selected scene atmosphere into a concrete description (write only the scene/environment; the product must not appear in the frame) as the MJ prompt, append the selected style seed code at the end, and add the --v 8.1 version parameter; MJ outputs 4 images by default to choose from. Style seed mapping:

Blue-orange cinematic → --sref 1998077430

Premium neutral cinematic → --sref 1804771136

High-saturation retro warm blue → --sref 2498372592

Japanese cinematic → --sref 1998077430

> Style seeds use only publicly reusable numeric --sref values and are never bound to any personal --profile account profile; if a dedicated style is needed, switch to the profile from your own account.

Outfit images (if models are used, must use GPT Image 2): one image per person [white background, full-body display, 16:9] containing 4 full-body looks, generated with GPT Image 2 based on the character settings + category requirements (produced in parallel with the scene atmosphere image, without waiting for each other); if the product is wearable (clothing/shoes/bags/hats/glasses/accessories/watches), all 4 looks are styled around that product as the core (look = product + matching pieces, with the product reproduced per @Product Three-View).

After the user has selected the scene atmosphere image + the look number:

Character three-view (one per person; white background; 16:9; must be generated with GPT Image 2 to ensure consistent reproduction of look/outfit): generated according to the selected model look + selected look, referencing the outfit images and clearly stating which look number is used (e.g., "use look 2 from the outfit images"); from left to right: face close-up ｜ full-body front ｜ full-body back, locking in the look as the {{Mixed N}} anchor; if outfit reference images were uploaded, reproduce them with GPT Image 2 per the reference images as well. Expressions should be natural, not odd.

Wearable products (clothes / shoes / bags / hats / glasses / jewelry / watches and other products worn on the body): in the character three-view, the model directly wears / carries / puts on the product (product appearance reproduced per @Product Three-View), locking the product-on-body effect and the character look into the same anchor image in one go—subsequent storyboards base the "person + product" in-frame state on this character three-view; the 4 looks in the outfit images must also be styled around that product (look = product + matching pieces) and must not clash with the product's tone. Standalone product close-up shots still follow @Product Three-View / @Product Detail Three-View.

After generation, always name it "Character Three-View" (for multiple characters: "Character Three-View 1 / Character Three-View 2…"), for direct attachment via @Character Three-View(N) in Step 3.

After the user confirms the visual direction, lock it in before moving to the next step—subsequent storyboards are written strictly according to the selected models and scenes; the user-selected scene atmosphere image is always named "Scene Atmosphere Image" (for space categories, the real-scene image is named "Space Real-Scene"), for attachment via @Scene Atmosphere Image / @Space Real-Scene. The moodboard is the gatekeeping checkpoint before prompts are written, and also the naming checkpoint for @ anchors.
### Step 3 · Output storyboard prompt → generate once satisfied → assemble final video → auto-generate subtitles

① Duration-based splitting (15s per clip · iron rule of generation granularity)

**The generation unit = one 15s clip.** One clip = one complete, continuous prompt (internally containing numbered shots, left to the model to auto-split within that clip).

- **15s = 1 clip**: one prompt generated in a single pass.
- **30s = 2 clips**: write 2 prompts (front and back content differ, no repetition; logo only at the end of the 2nd clip).
- **60s = 4 clips**: write 4 prompts (content all non-repetitive; logo only at the end of the 4th clip).

**Strictly forbidden to generate shot by shot (hard rule)**: numbered shots "Shot 1 / Shot 2 / Shot 3…" are only an internal storyboard script for the model to read **within one clip**; **never treat each shot as an independent generation task and generate them one by one**; each 15s clip triggers **only one** generation, producing the entire 15s footage in a single pass (internal multi-shot transitions are auto-split and connected by the model). Any "generating shot by shot" or "calling Seedance shot by shot" is wrong.

**Parallel multi-clip generation (hard rule)**: prompts for all clips are written out in one pass and given to the user for confirmation all together; once confirmed, all clips call Seedance 2.0 simultaneously and in parallel—do not wait for the 1st clip's output before generating the rest. (If the user explicitly requests clip-by-clip confirmation before continuing, generation may proceed clip by clip, but **the unit is always the full 15s clip, never down to a single shot**.)

**Cross-clip consistency under parallel/multi-clip**: do not rely on last-frame continuation; instead let anchors carry it—each clip's prompt references the same {{scene mood image}} / {{product three-view}} / character three-views, and states the same {{Mixed N}}, the same outfit (which look), and the same lighting time of day; transitions between clips rely on action/framing echoes between the opening and closing shots designed in advance when writing the prompts, with no continuity breaks.

② Output format (Chinese numbered storyboard · one prompt = one 15s clip)

Fixed opening sentence (written verbatim as the first sentence of each prompt, wording must not be altered): Use @scene mood image as the scene and tone reference, use @character three-view as the character subject, and use @product three-view, @product detail three-view as product references. —— Trim the referenced objects according to the actual situation: if there is no model, remove "use @character three-view as the character subject,"; for spatial categories such as real estate/hotels, change the scene reference to "use @real space photo as the scene and tone reference" and every shot must be within the real shot location, with no fictional spaces; for multiple characters, write @character three-view 1, @character three-view 2. Apart from this, the sentence pattern and wording remain fixed.

@ references must be actually bound to anchors (hard constraint): every @name must be truly bound to the corresponding anchor image generated in earlier steps and confirmed by the user—@scene mood image = the scene mood image selected by the user in Step 2; @character three-view(N) = the character three-view generated in Step 2 (the Nth character); @product three-view / @product detail three-view = the two product reference images generated in Step 1; @real space photo = the real-location image from Step 1. When calling Seedance 2.0, attach these images as reference images along with the prompt; each @name maps one-to-one to an attached image, with names exactly matching. Before outputting the prompt, verify: every anchor referenced in the sentence has been generated and confirmed—if any is missing, go back to the corresponding step to generate it first; @-referencing a non-existent image as an empty reference is strictly forbidden. During parallel multi-clip generation, all clips attach the same set of anchor images.

The scene is carried by the image, so the body text no longer describes scene mood / environment / color tone in words (otherwise it conflicts with the image reference); the body only writes quality locks (cinematic / ad-grade) + subject / action / camera / product. The same applies to characters and products: appearance is governed by @character three-view, products by @product three-view / @product detail three-view; the body no longer repeats descriptions of the character's looks or the product's appearance.

**Within each clip** number shots as Shot 1 / Shot 2 / Shot 3…, each shot specifying framing + camera movement + content (actions and visuals of {{Mixed N}} or the product). **These numbers are only the internal storyboard given to the model for this one clip; the whole segment is generated in one pass, not shot by shot.**

Rhythm implementation: the number of shots per clip, per-shot duration, and product appearance timing follow the category rhythm table in Section 4; framing jumps three levels, hard cuts as the mainstay, no dissolves. Fast-paced categories (food/sports/tech + promo purpose) must execute Section 4's "fast-paced category hard rules" for each clip: 6–8 shots per 15s clip, per-shot ≤ 2s, at least 2 kinds of dynamic camera moves, fast action verbs for shots, action in every shot.

First-shot rule: the first shot of each clip must not be a pure empty scene shot—with a model, the model must be in the scene; without a model, the product must appear in the second shot.

Character movement speed: character actions move naturally at normal speed; unexplained slow motion or sluggish floating feel is forbidden; slow motion/overcranked shots are only for deliberately designed emphasis shots (such as texture pulling, water splash freeze), stated explicitly in that shot; all other shots are at normal speed.

Motion quality sentence (fixedly appended to the end of each clip prompt): camera movement silky and smooth, frame rate stable and continuous, no frame drops, no stutter, no jitter, natural motion blur; character actions at normal speed, natural and fluid, not sluggish; orbit / rotation slowed to constant speed. No frame skipping between shots, no crossing the axis (respect the 180° axis rule).

No background sound effects to be generated (fixedly stated in each clip prompt): video generated silent, no background sound effects / ambient sounds auto-generated; music, sound effects, and voiceover are all left to ④ post-production.

Voiceover copy is written out here for user confirmation (written in the selected voiceover language: Chinese or English); voiceover is always left to ④ post-production dubbing.

③ Generate once satisfied

After the Chinese prompt is output and the user confirms, directly call Seedance 2.0 to generate the video, no manual pasting needed; **each call generates one complete 15s clip (not shot by shot)**; when calling, attach all anchor images referenced by the fixed opening sentence (scene mood image / character three-view / product three-view / product detail three-view, or real space photo) as reference images along with the prompt, with @names matching images one-to-one; multi-clip prompts for 30s / 60s are confirmed all at once, all clips generated in parallel simultaneously (no waiting segment by segment, much less shot by shot; all clips attach the same set of anchor images), and outputs are shown to the user together after generation.

④ Assemble final video → auto-generate subtitles

Stitching: multiple 15s clips for 30s / 60s are stitched in order, with unified aspect ratio and frame rate, and clip-to-clip transitions handled; a single 15s clip becomes the final video directly.

Music (always generated in post): video is silent, no background sound effects; music is added in post—after stitching, generate one piece whose duration strictly matches the final video, according to the actual rhythm and tone (food/sports/promo beat-sync, luxury/hotel/fragrance ambient bed, jewelry/real estate warm instrumentals).

Voiceover post dubbing: generated via TTS / dubbing using the selected voice + selected voiceover language (Chinese / English, choose one), mixed in aligned to the visuals; voiceover copy is written in the selected language and was already confirmed by the user in ②.

After assembly, automatically proceed to the next step of generating subtitles (no user trigger needed): overlay subtitles per the subtitle choice set in Step 1 (none / monolingual / bilingual), and overlay the brand slogan / logo landing at the end, outputting the final video.

---

## Locked style blocks (choose per production method · use as-is)

Cinematic commercial base (live action) · EN:
A high-end commercial film, cinematic masterpiece, commercial-grade lighting and color grading, crisp clean image, shallow depth of field, premium product-film aesthetic, natural film-scan color fidelity (no over-warm filter).

Cinematic commercial-film base · ZH:

High-end commercial ad film, cinematic masterpiece, commercial-grade lighting and color grading, crisp clean image, shallow depth of field, premium product-film aesthetic, natural film-scan color fidelity (avoid an over-warm filter look).

Add-on lines: Demo + clean seamless studio backdrop, macro detail, even soft key light, product hero shot, slow-motion reveal | Audiovisual-spectacle style + fashion-film energy, dynamic FPV/slider/crane motion, music-driven rhythm, rich material texture | Tech + dark moody studio, neon edge light, glowing UI, 360 orbit.

---

## Full Example (Beauty/Skincare · Demo+Emotion · 15s = 1 clip · 9:16)

Knobs: Lighting=soft translucent light + backlit hair light | Color tone=warm + low-saturation creamy feel | Camera=macro + slow orbit + shallow depth of field | Music=ambient electronic + faint texture-spreading sound | Editing=medium pace | Model=high-fashion face + subtle facial micro-expressions | Story=light narrative · product hero finale.

(In Chinese, with numbered shots; **one 15s clip contains 5 shots internally, generated as a whole in one pass, not shot by shot**.)

```
Use @scene mood image as the scene and tone reference, use @character three-view as the character subject, use @product three-view and @product detail three-view as product references. High-end beauty commercial film, cinematic masterpiece, crisp clean image, shallow depth of field. Vertical 9:16.
Shot 1 | Medium shot / slow push-in: {{Mixed 1}} sits at the vanity area, serene in expression and exquisite in makeup, reaches out and picks up the product, movements natural and deft.
Shot 2 | Extreme macro close-up / static: a fingertip lifts a wisp from the lustrous balm, the texture slowly drawing into strands in overcranked slow motion (this shot is the deliberately designed texture-emphasis shot).
Shot 3 | Close-up / lateral tracking: the balm glides along her cheekbone, leaving a dewy sheen; the application movement at normal speed.
Shot 4 | Facial close-up / slow push-in: she opens her eyes toward the camera and shows a confident smile.
Shot 5 | Product close-up / slow steady orbit: close with an orbit around the product bottle, brand logo and one slogan line fading in.
Do not generate background sound effects (video muted, soundtrack added in post). Camera movement silky and fluid, frame rate stable and consistent, no dropped frames, no stuttering, no jitter, motion smooth with natural motion blur; character actions at normal speed, natural and fluid, never sluggish.
```

> The 5 shots above are written into **the same prompt** and generated in one pass as **one 15s clip**; for 30s, write a 2nd clip prompt like this, for 60s write up to the 4th — never split Shot 1\~Shot 5 into 5 separate generations.

---

## Reference Files

The element-deconstruction menu, style-seed mapping table, and pre-output self-check checklist are all inlined in this file.

references/[seedance-output.md](http://seedance-output.md), scripts/extract\_[frames.sh](http://frames.sh) (frame-extraction/compositing script, to be added).

---

## General Constraints

Before writing a prompt, check each item against the "Pre-Output Self-Check Checklist" at the end of this document (i.e., the checklist version of the constraints below).

- Each prompt is delivered in Chinese; once the user confirms, call SD2 directly to generate, no manual pasting needed.
- **Generation-granularity iron rule**: **one prompt = one 15s clip = one generation**; 15s=1 clip, 30s=2 clips, 60s=4 clips; the numbered shots are merely the internal shots of a single clip, left for the model to cut automatically; **never generate shot by shot / never generate individual shots one at a time**. For 30s / 60s, write all the multi-clip prompts in full at once, confirm them together, and generate all clips in parallel (if the user wants clip-by-clip confirmation, they may be generated one at a time, but the unit remains the whole clip).
- Use {{Mixed N}} for characters: fully specified at first appearance, reused afterwards, with subject and object clear; for demo-style videos, ensure the product is clear in every shot.
- Between the individual 15s clips (generated in parallel, not continued segment by segment), be sure to rely on shared anchors (the same {{scene mood image}} / {{product three-view}} / character three-view) to keep {{Mixed N}}, wardrobe, scene, and lighting consistent; the opening and closing shots between clips should be pre-designed to echo each other when writing the prompts, so the joins don't break continuity.
- Fixed opening sentence (hard constraint): the first sentence of every video prompt is written verbatim as "Use @scene mood image as the scene and tone reference, use @character three-view as the character subject, use @product three-view and @product detail three-view as product references." (Drop the character clause when there is no model; for spatial categories, change to @space real-scene; all other wording stays fixed.) Each @name must actually be attached to the corresponding anchor image generated in earlier steps and confirmed by the user; when calling Seedance, attach it along with the prompt, names matching one to one; empty references to non-existent images are forbidden — if an image is missing, go back to the corresponding step to generate it first. Scene/character/product are all carried by the referenced images, and the prompt body no longer describes scene mood / environment / color tone / character looks / product appearance in words (to avoid conflicting with the image references); correctness is judged against the selected images.
- Live-action scenes (real estate / hotels, etc.): for categories that use live-action photos, the fixed opening sentence changes to reference @space real-scene, and every shot in the final prompt must be based on the @space real-scene live-action location; fabricating fictional / imagined spaces is not allowed.
- Character expressions must be natural and believable; exaggerated or bizarre expressions are forbidden.
- First-shot rule: the first shot of each clip must not be a pure empty scenery shot — with a model, the first shot must show the model inside the scene (person + environment in the same frame); without a model (pure product), the second shot must show the product.
- Character movement at normal speed: character actions move naturally at real-world normal speed, never sluggish, floaty, or in unmotivated slow motion; overcranked/slow motion is reserved for explicitly designed emphasis shots and must be stated as such, all other shots at normal speed.
- No superimposed / dissolve transitions.
- No particle effects (too tacky); for spectacle or transitions, use clean light effects or material texture instead.
- Wearable products (clothing/shoes/bags/hats/eyewear/accessories/watches): the model wears the product directly at the character three-view stage (recreated per @product three-view), locking the worn-on-body state into the @character three-view anchor; in storyboard shots with the character in frame, the product-wearing state follows @character three-view, while standalone product close-up shots follow @product three-view / @product detail three-view; the two must not conflict (same item, same colorway).
- Without a model (pure product): camera movement should be rich (multiple angles, orbit, push-pull, macro), and don't keep ramming the logo into frame; showcase every facet of the product (e.g., phone = camera / screen / edges; sunglasses = temples / lenses / on-model wearing effect); the logo appears only at the final closing beat.
- Pacing and cuts: the number of shots within a clip, per-shot duration, and product appearance timing are controlled by that category's pacing table in Section 4; shot sizes cut with the "skip three levels" rule (no shuffling between adjacent levels), hard cuts as the default, match cut / action match where smoothness is needed, cross-dissolves/superimpositions forbidden. Fast-paced categories (food/sports/tech + promotional purpose) must follow the "fast-paced category hard rules" in every clip: 6–8 shots, each shot ≤ 2s, ≥ 2 types of dynamic camera movement, fast-action verbs, action in every shot — never write them as slow-paced.
- Camera movement must be silky smooth: always append a motion quality sentence at the end of each clip prompt (no dropped frames / no stuttering / silky smooth + natural motion blur); orbiting and rotating shots are especially prone to dropped frames — specify "slow, constant-speed orbit, smooth continuous rotation" and slow the speed down.
- Shot transitions: no frame skipping or axis crossing between shots (observe the 180° axis rule); camera positions and motion logic must be coherent.
- Do not generate background sound effects: generate the video muted, producing no ambient sound / background sound effects at all; music / sound effects / voiceover are all added in post-production.
- One video carries only one core message point; hook viewers in the first 3 seconds, and the ending must have a payoff (logo/CTA/proposition).
- Real brand names serve only as abstract style references; do not reproduce identifiable elements of any specific brand's real ads, and do not fabricate false claims about real brands; style seeds use only publicly reusable numeric --sref values, not bound to a personal profile; no content involving real public figures; keep everything appropriate and harmless.

---

## Pre-Delivery Self-Check Checklist

Confirm each item before generating the prompt; deliver only when every box is checked. These rules are equivalent to the main [SKILL.md](http://SKILL.md) "general constraints" — they are summarized here only to prevent omissions.

Generation granularity

- \[ \] **One prompt = one 15s clip = one generation? 15s=1 / 30s=2 / 60s=4 clips?**
- \[ \] **No generating the numbered shots as independent tasks one shot at a time? (Numbered shot breakdowns exist only inside a single clip and are left to the model to split automatically)**
- \[ \] For 30s/60s, are the multi-clip prompts written out in full at once and able to be generated in parallel (or the user has requested clip-by-clip confirmation)?

Language and format

- \[ \] Delivered in Chinese?
- \[ \] Within each clip, is the shot breakdown numbered as Shot 1 / Shot 2 / Shot 3…, with each shot specifying shot size + camera movement + content?

Scene and fixed opening sentence

- \[ \] Is the first sentence of every prompt the fixed sentence "Reference @scene-mood image as the scene and tone reference, reference @character three-view as the character subject, reference @product three-view and @product detail three-view as the product reference." (correctly trimmed based on presence of a model / spatial category, with wording unchanged)?
- \[ \] Does every @name in the sentence correspond to one generated, confirmed anchor image (no empty references)? When calling Seedance, are these images attached along with the prompt, with names matching one to one? Do parallel multi-clips attach the same set of anchor images?
- \[ \] Is the scene carried by the @scene-mood image, with no further textual description of scene mood / environment / color tone in the body?
- \[ \] For live-action categories such as real estate / hotels: does the opening instead reference @real-space footage, is every shot based on the real filmed scene, with no separately invented fictional spaces?

Consistency anchors

- \[ \] Is the product clear in every shot, governed by {{product three-view}}?
- \[ \] Do characters use {{Mixed N}}, with character, clothing, and lighting consistent across shots/clips and no continuity goofs at the joins?
- \[ \] For wearable products (clothing/shoes/bags etc.): does the model in the character three-view already wear the product (same style and color as the @product three-view)? Is the clothing image look styled around the product? Does the product's state not conflict between the character-in-frame shots and the product close-up shots?
- \[ \] For 30s/60s: are the multi-clip prompts written out in full at once and able to be generated in parallel? Do all clips reference the same anchor images, and have the opening and closing shots across clips been designed to echo each other?

Generation tools

- \[ \] Are scene mood images generated with Midjourney v8.1 (style seed + --v 8.1 at the end of the prompt)? Does the style seed use only a numeric --sref with no personal profile?
- \[ \] Are clothing images and character three-views generated with GPT Image 2?

Characters and visuals

- \[ \] Are character expressions natural and believable, with no exaggerated or bizarre expressions?
- \[ \] Do character actions move naturally at normal speed (no sluggishness / floating / unexplained slow motion), with slow motion used only in explicitly specified emphasis shots?
- \[ \] For no-model (pure product) videos: is the camera movement varied, showing every side of the product, without constantly shoving the logo into frame (logo only at the ending)?

Pacing and cuts

- \[ \] Is the first shot of each clip not a pure empty-scene shot: with a model = the model is in the scene; without a model = the product already appears in the second shot?
- \[ \] Is there a hook in the first 3 seconds, with the product showing up within the timing specified for the category (promotional/demo: product visible at 3s)?
- \[ \] Do the shot count and per-shot duration within a clip match that category's pacing table in Section 4 (15s clip ≈ 4–6 shots, fast-paced may go 6–8)?
- \[ \] Fast-paced categories (food/sports/tech/promotional): does each clip follow the hard rules with 6–8 shots, each shot ≤ 2s (sports ≤ 1.5s), using ≥ 2 types of dynamic camera movement, fast-action shot verbs, a clear action in every shot, and no slow-pace words dominating? Does the total shot count × per-shot duration ≈ 15s per clip?
- \[ \] Are shot sizes cut with the "skip three levels" rule, hard cuts as the default, and no shuffling between adjacent levels?

Camera movement and transitions

- \[ \] Does each clip prompt end with a motion quality sentence (no dropped frames / no stuttering / silky smooth + natural motion blur)?
- \[ \] Are orbiting/rotating shots slowed down and explicitly specified as "slow, constant-speed orbit, smooth continuous rotation"?
- \[ \] No frame skipping or axis crossing between shots (observing the 180° axis rule)?

Prohibited items

- \[ \] No cross-dissolve / superimposed transitions (use match cut / action match where smoothness is needed)?
- \[ \] No particle effects?
- \[ \] Does the prompt explicitly state "do not generate background sound effects," with the video generated muted (all audio added in post)?

Structure and payoff

- \[ \] Does one video carry only one core message point and hook viewers in the first 3 seconds?
- \[ \] Is there an ending payoff (logo / CTA / proposition)? For 30s/60s, is the logo lock-up only at the end of the last clip?

Safety

- \[ \] No real public figures involved, no reproduction of identifiable elements from specific brands' real ads, no fabricated false claims about real brands, and content appropriate and harmless?