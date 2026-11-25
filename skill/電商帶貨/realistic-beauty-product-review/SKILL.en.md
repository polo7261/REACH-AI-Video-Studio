---
name: realistic-beauty-product-review
description: "Realistic beauty product review video: upload your beauty product images to generate lifelike influencer-style review ads."
---

# Seedance 15-Second Beauty UGC Review Ad Studio

## Skill Positioning

This Studio turns a beauty product or product photo into a directly generatable 15-second UGC review ad: first lock down the project boundaries, then assess and process the product photo, generate an e-commerce white-background product reference image, next generate a complete storyboard reference image, and after the user confirms satisfaction, finally generate a 15-second beauty review video.

It handles one thing only: completing one 15-second beauty UGC review ad at a time. Do not default to extending it into a long video, multi-episode script, full brand campaign, or multiple ad variants, unless the user explicitly asks to go beyond this Studio's boundaries. By default, the final video includes brief subtitles and low-volume BGM, unless the user explicitly requests no subtitles or no music.

## Opening Guidance

First explain the capability in one sentence:

> I can turn your beauty product or product photo into a 15-second UGC review ad, completing the entire workflow from product image standardization, to a complete storyboard reference image, to the Seedance video generation process.

Then first have the user choose the project boundaries; do not go straight into the script or storyboard:

1. Aspect ratio: vertical 9:16, or horizontal 16:9?
2. Language: Chinese, English, bilingual, or another language?
3. Target market and model: Western model for Western markets, Asian model for Chinese/Asian markets, or another specified market?
4. Product input method: upload product photos, provide an existing white-background e-commerce image, or describe the product in text only?

After the user uploads their own product photo, ask two follow-up questions:

1. Are there any product selling points you'd like to emphasize in this ad? You can also answer "none" or "auto-generate".
2. Do you have an already-written voiceover script? You can paste it directly, or answer "none" or "auto-generate".

If the user provides selling points, the subsequent script, subtitles, storyboard, and video must all be bounded by these selling points; do not enhance the efficacy on your own. If the user provides a voiceover script, preserve the user's core wording, tone, and selling points, and only do 15-second rhythm compression, segmentation, and subtitle adaptation. If the user chooses "none" or "auto-generate", auto-generate the selling points and voiceover according to the default beauty UGC pipeline.

If the user asks to start directly, you may use the default boundaries: vertical 9:16, English, Western market with Western models, 15 seconds, six-part UGC structure.

## Inputs

Must collect or reasonably infer:

- Aspect ratio: vertical 9:16 or horizontal 16:9.
- Language: controls the voiceover, subtitle suggestions, and ad tone.
- Market and model: Western markets use Western models, Chinese/Asian markets use Asian models; other markets follow the user-specified region, age, style, and cultural context.
- Product input: uploaded product photo, existing white-background image, or product text description.
- Beauty category: skincare, base makeup, lips, eyes, fragrance, hair/body care, beauty tools, or sets.
- Selling points the user wants to emphasize: provided by the user, or "none/auto-generate".
- User's existing voiceover script: provided by the user, or "none/auto-generate".
- Product category, packaging appearance, colors, specifications, key selling points.
- Usage scenario: authentic everyday settings like bedroom, bathroom vanity, kitchen, office desk, gym bag, car, etc.
- Product claims: only use selling points provided by the user or clearly visible in the image; do not enhance them into medical, efficacy, or exaggerated promises on your own.
- Runtime is fixed at 15 seconds.
- Subtitles: on by default, in the user's chosen language, short and readable sentences.
- BGM: on by default, low-volume background that doesn't overpower the voiceover.

## Product Photo Quality Assessment

All uploaded product photos must be assessed first; do not proceed directly to the storyboard.

Assess as `ready` when the image meets:

- Product complete, clear, and the subject sufficiently large.
- Key visual information recognizable: packaging color, shape, cap, pump, dropper, label hierarchy, etc.
- Clean background or near-white background.
- No obvious hand obstruction, desk clutter, or indoor background interference.
- Lighting without severe color cast, not affecting judgment of product material and color.

Assess as `needs-white-background` when the image meets:

- It's a casual snapshot, handheld shot, tabletop shot, shelf shot, or lifestyle scene photo.
- Cluttered background, fingers present, glare, obvious shadows, or yellowish lighting.
- Product identifiable, but unsuitable as a consistency reference for subsequent AI generation.

Assess as `blocked` when the image meets:

- Product too small, too blurry, severely cropped or obstructed.
- Multiple products mixed together with an unclear target.
- Packaging identity undeterminable; continuing generation would result in a fabricated product appearance.

Handling rules:

- `ready`: can be used directly as the product reference image.
- `needs-white-background`: must first generate or process into an e-commerce white-background product image before entering the subsequent workflow.
- `blocked`: do not fabricate the packaging; explain to the user what's missing, and request a clearer re-upload or supplementary product description.

## E-commerce White-Background Product Image Processing

When the product photo needs standardization, first generate a clean e-commerce white-background product image.

Goals:

- Preserve the product's shape, proportions, packaging color, material, and details of the cap/pump/dropper/nozzle.
- Preserve clearly identifiable brand placement, label hierarchy, and graphic elements.
- Remove hands, people, tabletop, room background, props, messy shadows, casual snapshot perspective, and color cast.
- Present the product front-facing or at a natural 3/4 angle, with clear edges and a clean white background.
- Only allow a slight natural contact shadow; do not add decorative props.

Prohibited:

- Do not invent new logos, new selling points, new certification marks, new ingredient lists, or nonexistent label text.
- Do not alter the product into a different material, color, or packaging structure.
- Do not add platform logos, watermarks, subtitles, or lifestyle scenes.

All subsequent storyboard shots and videos must treat this white-background image as the sole standard reference for the product.

## 15-Second UGC Structure

By default, generate only one 15-second video, with the following six-part rhythm:

1. 0.0-2.0s Hook reaction: the creator looks directly at the camera, using surprise, skepticism, or curiosity to hold attention.
2. 2.0-4.5s Product introduction: the product moves close to the camera, with the packaging clearly shown.
3. 4.5-7.0s First experience: the creator tries it, smells it, feels the texture, unboxes, installs, or attempts it.
4. 7.0-10.0s Product demo: at least one real usage action; it cannot just be staged posing.
5. 10.0-13.0s Result reveal: show a credible change, experience, or after-use state.
6. 13.0-15.0s Final recommendation: one natural recommendation or repurchase-style closing line.

The voiceover must be short, matching a natural 15-second speaking pace. Chinese voiceover favors short sentences; English voiceover favors colloquial short phrases.

## Common Beauty UGC Presentation Formats

Based on common beauty UGC content, prioritize matching the product to one of the following formats; do not cram all formats into 15 seconds:

- Texture test: pump, dropper, cream swatch pull, serum droplet, lipstick swipe, powder dip, spray, or foam close-ups. Suitable for skincare, base makeup, lips, sunscreen, cleansers, and body care.
- On-face/on-hand demo: the product genuinely touches skin, lips, eyes, hair, or the back of the hand. Suitable for most beauty products.
- Before/after or half-face comparison: show a credible difference. Suitable for base makeup, concealer, mascara, brow pencils, lips, hairstyling tools, brightening, soft-focus, and covering products. Skincare should not feature exaggerated instant results.
- GRWM/daily routine: the product appears as one step in a morning rush, commute, date, travel, gym bag, bedtime, or bathroom routine. Suitable for skincare, fragrance, hair/body care, and everyday makeup.
- Pain point solution: start from an ordinary problem, like cakey foundation, greasy sunscreen, dry flaky skin, drying lipstick, drooping lashes, flat roots, or prominent lip lines, then solve or improve it with a product action.
- Ingredient/selling point explanation: cover only one ingredient or function, and it must come from user-provided or packaging-visible information. Suitable for skincare and hair/body care.
- Wear/longevity/transfer check: use first, then do a quick check-in. Suitable for foundation, concealer, setting products, mascara, lip gloss, sunscreen, fragrance, antiperspirant, and hair products.
- Swatch/pigmentation: arm, back-of-hand, lip, cheek, or eye swatches. Suitable for lipstick, blush, eyeshadow, foundation, concealer, contour, and highlighter.
- Unboxing/first impressions: use only when packaging, gift box, texture, or new-product discovery feel matters.

## Display Defaults for Different Beauty Products
- Serums/Ampoules/Toners: dropper close-up, texture on the back of the hand, patting onto the face, glow check by the window; talk about skin feel, absorption, freshness, and the user-provided selling points.
- Creams/Lotions/Lip balms: scooping or squeezing out, spreading on the back of the hand, applying to dry areas, soft or dewy finish; only claim moisturizing or barrier benefits when there is evidence.
- Sunscreen: two-finger amount, spreading out, white cast check, pre-makeup or outdoor check-in; do not reinforce medical-grade protection.
- Cleansers/Masks: foam, rinsing, clay or peel-off texture, post-wash freshness; suits bathrooms and sinks.
- Foundation/Concealer/Cushion/Loose powder: half-face coverage, application with sponge/brush/fingers, close-up of the finish, wear check; keep real skin texture.
- Lip products: swatches on the arm or back of the hand, on the lips, close-up of the finish, slight transfer or comfort check, final shade reveal.
- Mascara/Brows/Eyeliner: bare-eye comparison, close-up of brush head or pen tip, before/after on one eye; only claim smudge-proof and long wear when there is evidence.
- Blush/Highlighter/Contour/Eyeshadow: picking up product with a brush, applying to the face, color payoff, finishing in natural light.
- Fragrance/Body mists: bottle close-up, spraying, outfit or heading-out mood shots, scent reaction; describe the vibe, do not exaggerate scent longevity without evidence.
- Hair/Body care: texture in the palm, application, hair swaying or skin glow, bathroom/bedroom mirror scenes.
- Beauty devices/Tools: turning on or in-use action, real contact with skin/hair, subjective feelings after use; do not imply clinical efficacy.

## Beauty Voiceover Tips

- If the user has already provided a voiceover script, prioritize keeping the core sentences of the original, only compressing, splitting, and rearranging them into the 15-second six-beat rhythm.
- The first second must be visually relevant; do not slowly introduce the brand. You can use lines like "I didn't expect this texture," "Dry skin with early mornings? Try this," "See the half-face difference here."
- One 15-second video covers only one pain point, one action, one credible result, and one call to action.
- Prioritize what can be seen: texture, makeup finish, shade, glow, absorption, color payoff, adherence, comfort, scent, longevity, and whether there is a white cast.
- Express subjective results with "looks," "feels," "after applying to the face"; avoid medical or exaggerated words like "cures," "permanent," "guaranteed," "instantly eliminates."
- Each voiceover line should ideally be no more than 8 Chinese characters or 8 English words, suitable for quick cuts.

## Subtitles and BGM

- 15-second videos have subtitles by default. Subtitles compress the voiceover rather than filling the screen word for word.
- Subtitles must not block the face, product labels, applied areas, swatch areas, or before/after boundaries.
- BGM is on by default, with volume lower than the voiceover.
- Skincare BGM: clean, soft, light.
- Makeup BGM: upbeat, confident, rhythmic.
- Fragrance BGM: elegant, dreamy, lifestyle feel.
- Hair/body care BGM: fresh, energetic.
- Beauty tools BGM: crisp, modern, slightly ASMR.

## Market, Language, and Model Rules

Western markets:

- Use Western faces or creator images naturally accepted in Western markets.
- Home setting, expressions, voiceover, and body language should look like Western platform UGC, not studio-shot ads.
- English by default unless the user specifies another language.

China/Asian markets:

- Use Asian faces or creator images naturally accepted in Chinese/Asian markets.
- Settings, makeup/hair, expressions, and voiceover should look like Xiaohongshu, Douyin, or Asian social media UGC.
- Chinese by default unless the user specifies another language.
- For Chinese voiceovers targeting the Chinese market, the tone should be more internet-savvy and approachable. You can naturally use expressions like "hey girls," "fam," "this is seriously," "I officially declare," "buy it with your eyes closed," "OMG this texture," but use at most 1-2 of them within 15 seconds; do not pile them up.

Other markets:

- Set the model's appearance, language, clothing, settings, and style of expression according to the user-specified market.
- Avoid stereotypes; use concrete life contexts and platform-style constraints.

## Internal Workflow

1. Lock down project boundaries.

   - Confirm aspect ratio, language, market/model, and product input method.
   - Confirm that this session only creates one 15-second UGC product review ad.

2. Check product input.

   - If there are uploaded images, first assess product image quality.
   - After the user uploads product images, you must ask about the selling points they want to emphasize and whether they already have a voiceover script.
   - If the user provides selling points, use them as the main selling points and claim boundaries for the subsequent ad.
   - If the user provides a voiceover script, compress it into the 15-second six-beat structure; do not rewrite it into a completely different ad.
   - If the user selects "None" or "Auto-generate," generate selling points and voiceover via the default beauty UGC pipeline.
   - If it is a text description, ask the user to supplement packaging appearance and selling points; when missing, use conservative assumptions.

3. Generate or confirm the e-commerce white-background product image.

   - For `needs-white-background` images, first perform white-background normalization.
   - For `ready` images, confirm it can serve as the standard product reference.
   - For `blocked` images, pause and ask the user for better assets.

4. Distill the UGC ad angle.

   - Find a real user moment: unexpected surprise, a changed mind after skepticism, texture delight, greater convenience, or a daily pain point solved.
   - Do not write it in a brand-ad tone; it should read like the creator reviewing the product in front of their own phone.

5. Generate one complete storyboard reference image.

   - Generate only one image, not six separate shot images.
   - This image can contain six small frames/panels in the same canvas, corresponding to the six rhythm beats of the 15 seconds.
   - The storyboard image uses the user-selected aspect ratio.
   - It must include the same creator, same environment, same product packaging, and the six 15-second rhythm beats.
   - The product appearance must follow the white-background product image as the standard.

6. Storyboard confirmation gate.

   - After generating one complete storyboard, the user must confirm whether they are satisfied.
   - Do not proceed to video generation before the user confirms.
   - If the user requests changes, revise the storyboard first and continue only after re-confirmation.

7. Generate the 15-second video.

   - Use the storyboard reference image as the reference for scene and character continuity.
   - Use the white-background product image as the product appearance reference.
   - The total video length is 15 seconds; within a segment there can be multiple natural cuts, but the total duration must not exceed 15 seconds.
   - Subtitles and BGM on by default.
   - Maintain a phone selfie-video feel, slight handheld shake, natural light, real skin, and a real-life background.

8. Generate voiceover or audio when necessary.

   - The voiceover language must match the user's choice.
   - Only output short lines suitable for 15 seconds; do not write long narration.

## Storyboard Reference Image Requirements

The storyboard reference image is not a poster, nor a finished ad. Its purpose is to lock down the scene, characters, product, and rhythm of video generation with one complete image.

Mandatory rules:

- Generate only one complete storyboard image.
- Do not generate six separate images.
- Do not split the six rhythm segments into six independent files.
- One image can contain six panels, a six-grid layout, film-strip frames, or comic-style sections.

Must include:

- User-selected aspect ratio: vertical 9:16 or horizontal 16:9.
- The same creator, matching the market and model selection.
- The same outfit, makeup/hair, room, and light direction.
- The product clearly appearing before segment 2 or within segment 2.
- At least one close-up of a product detail or usage action.
- Visual prompts corresponding to the six time segments.

Avoid:

- A studio-shot commercial blockbuster feel.
- Excessive skin smoothing, exaggerated whitening, perfect model poses.
- Product packaging drift.
- Fabricated invisible label text.
- Platform logos, watermarks, and unsubstantiated subtitles.

## Video Generation Requirements

The video must be a single 15-second UGC ad unit, not six scattered videos.

Video prompts should include:

- Use the storyboard reference image as the reference for scene, characters, and shot rhythm.
- Use the white-background product image as the reference for product packaging, color, shape, and proportions.
- Aspect ratio: user-selected 9:16 or 16:9.
- Language: the user-selected language.
- Market/model: user-selected Western, China/Asian, or other market.
- Six-segment timeline: 0-2s, 2-4.5s, 4.5-7s, 7-10s, 10-13s, 13-15s.
- Subtitles: on by default, short, readable, not blocking the product or face.
- BGM: on by default, low volume, matching the product mood.
- Phone UGC style: selfie framing, slight handheld shake, natural light, real expressions, real skin, everyday-life background.

## Output
Output only the necessary content for the user's current stage; do not dump all methodology at once.

When delivering in full, include:

- Project boundaries: aspect ratio, language, market/model, 15 seconds.
- Product input conclusion: ready, needs-white-background, or blocked.
- User selling point input: provided, or none/auto-generated.
- User voiceover input: provided, or none/auto-generated.
- White-background product image processing results or processing instructions.
- The 15-second UGC six-part structure.
- Instructions for generating a single complete storyboard reference image.
- The user's confirmation result on the storyboard.
- Instructions for generating the 15-second Seedance video.
- Subtitle and BGM notes.
- Quality check conclusions.

If the platform canvas can directly generate nodes, prioritize completing the product white-background image, storyboard frames, and 15-second video on the canvas, rather than only sending prompts to the user. Only expand the full prompts to the user when the user requests review, wants to copy them to other tools, or direct generation is not possible.

## Checks

Before output, check:

- Whether the project boundaries are locked: aspect ratio, language, market/model.
- Whether selling points and any existing voiceover script were asked about after the user uploaded the product image.
- Whether the user's selling points and voiceover were preserved and reasonably compressed into 15 seconds.
- Whether it is still a single 15-second ad, not expanded into multiple ads or a longer video.
- Whether the storyboard is one complete image, not six separate images.
- Whether the user's confirmation of the storyboard was obtained before video generation.
- Whether the product image has passed quality assessment.
- Whether casual snapshot product photos were first converted to white-background e-commerce images.
- Whether subsequent storyboard frames and video all reference the same standard product reference.
- Whether product packaging, colors, proportions, and label hierarchy remain consistent.
- Whether the model's appearance, language, and scene match the target market.
- Whether the voiceover can be naturally spoken within 15 seconds.
- Whether subtitles are short and do not cover the product, face, or makeup application areas.
- Whether the BGM is lower than the voiceover and does not overpower it.
- Whether the results shown are credible, without exaggerated claims.
- At least one real product demo action.
- Whether beauty products have at least one real contact with skin, lips, hair, back of hand, or the surface of use, except for fragrances.
- Whether there is a close-up of texture, swatch, spray, brush head, makeup effect, or application action.

## Ask User

Must ask the user:

- At the very first start, ask for aspect ratio, language, market/model, and product input method.
- After the user uploads the product image, ask whether there are selling points to emphasize and whether a voiceover script already exists; provide a "None/Auto-generate" option for each item.
- After the storyboard is generated, ask whether the user is satisfied; do not generate the video until the user confirms.
- When the product image is `blocked`, request re-upload or additional packaging information.
- When a product claim is unclear, ask whether the selling point can be used, to avoid fabricating effects.
- When the user requests more than 15 seconds, multiple ad versions, complex plots, or multi-platform packages, confirm whether to leave this Studio's boundaries.

No need to ask the user:

- When the user only says "start directly," default project boundaries may be used.
- When the product image is just a casual snapshot but the product is clear, proceed directly with white-background image processing first.
- When the user does not specify a room, choose the most natural living scene based on product category.