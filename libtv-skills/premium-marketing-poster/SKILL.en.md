---
name: premium-marketing-poster
description: "Premium marketing posters: high-end marketing ad poster generation for a wide range of campaign scenarios"
---

---

## name: premium-ad-posters\\

namespace: industry\
title: "Premium Ad Posters"\
description: "Generate premium promotional posters, retail/tech ad creatives, social media ad images, and marketing images with text overlays—prioritizes typography fidelity, hardware/product precision, layout discipline, and brand consistency. A 6-item technical realism checklist avoids common AI flaws (hardware mechanical symmetry / screen UI layer depth / normal anatomy / background artifact protection / high-contrast typography / reference mapping vs target format), includes a Prompt structure template (subject/style/instructions/text/constraints). Image-only; use generate_image_v3 (high quality, 2k or 4k resolution). For full brand visual systems use brand-visual-kit, for logo design use logo-design, for product hero/scene images use product-photoshoot, for Amazon compliance image sets use amazon-product-listing."\
version: 1

# premium-ad-posters

Use this skill when creating premium posters, ad creative images, and social media ad images (with text overlays). Image-only; use `generate_image_v3`.

> Environment adaptation: source main model `imagegen_2_0` (GPT Image 2.0) + fallback `flux_2`/`nano_banana_2` → we have no corresponding external model options, so uniformly consolidate to `generate_image_v3` (`no such model`, see adaptation removal ledger #41).

## Model and Specifications

Poster/ad success hinges on typography fidelity, hardware precision, layout discipline, and brand consistency. Use `generate_image_v3`, \*\*choose high quality, 2k (or 4k) resolution\*\* to ensure glyph shapes and hardware seams stay crisp.

Choose the aspect ratio by placement:

- `1:1` — Square Meta feed / carousel ads
- `9:16` — Stories / Reels / TikTok ads
- `4:5` — Instagram feed
- `3:4` — Portrait poster
- `16:9` — Banner

## Technical & Realism Checklist (scene-specific craft · inlined, proactively avoid common AI flaws in the prompt)

When designing product ads that integrate hardware and text, you must proactively steer the prompt to avoid the following common AI flaws:

1. **Hardware integrity / mechanical symmetry**

   - Problem: asymmetric smartwatch bezel, crown/dial looking warped or "melted" into the case, strap seamlessly fused with the case.
   - Fix: explicitly write "perfect mechanical symmetry, uniform bezel, clearly defined mechanical parts. The digital crown/dial must be a separate metal entity with precise knurling, separated from the bezel; natural lug connection attaching the strap to the case."

2. **Screen-layer UI integration (not flat stickers)**

   - Problem: on-screen graphics (recording waveform, numbers, buttons) stuck on the display glass look completely flat, lack real glass depth, or appear composited on in post.
   - Fix: explicitly write "interface rendered beneath the watch crystal glass, with subtle natural glare, reflections, and light refraction on the protective glass layer. Glowing UI elements (waveforms, numbers) should genuinely glow from behind the glossy reflective screen glass."

3. **Normal anatomy**

   - Problem: wrist lacking bone structure, transition joints under the strap collapsing softly, deformed fingers when wearing the device.
   - Fix: explicitly write "clear wrist skeletal anatomy (ulnar prominence), natural knuckles, realistic skin pores and natural skin texture, under soft filtered window light."

4. **Background artifact protection**

   - Problem: keys/buttons of keyboards, phones, and other objects in the background bokeh warped or oddly proportioned, undermining the professional ad quality.
   - Fix: explicitly specify background shapes, writing "background clean and tidy with no clutter. If keycaps or other objects appear in the out-of-focus background, they must follow standard rectangular forms, or simplify the background to a light wood texture to reduce clutter."

5. **High-contrast typography**

   - Problem: text overlays placed directly on light textures (e.g., light wood desktop) lack contrast, making the text hard to read.
   - Fix: explicitly write "all text overlays must use a clean, modern, dark sans-serif font with high contrast. If overlaid on varied textures, add a subtle drop shadow or ambient occlusion behind the text layer to ensure maximum readability."

6. **Reference mapping vs target format**

   - Problem: when the user provides an aesthetic reference from one device (e.g., iPhone lock screen) but asks for a different specific target product (e.g., a CarPlay display), the model generates the reference device instead of the target product.
   - Fix: only extract and map the reference image's **aesthetic attributes** (typography, color zoning, textures, UI element shapes) onto the **requested product's format and environment**; never change the subject device into the reference platform's device unless the user explicitly requests it.

## Prompt Structure Template

Split the prompt into the following distinct sections to help the model correctly construct the layout and aesthetic requirements:

```
[Subject/Hero]: Detailed description of the product with sharp details of the hands/model. Include anatomy and structure rules here.

[Style]: High-end product photography, soft window light, airy kitchen/office countertop, narrow depth of field, restrained editorial design sensibility, true warm tones.

[Instructions]: hardware mechanical symmetry, defined lug connection, screen-depth realism (glare/refraction on the crystal), background keyboard shape constraints, clean whitespace around the headline.

[Text]: Give the exact copy text blocks in quotes—headline/subheadline/caption, including specific font size, weight descriptions, color details, and placement zones (top/bottom/overlay).

[Constraints]: aspect ratio of [1:1/9:16]; no warped buttons, no melted casing, no blurry text, no deformed keys.
```

When batch-producing multiple images as a set and needing to consistently lock brand visual assets (palette/fonts/lighting), see brand-visual-kit.

## Related

Product hero/scene images (non-text-overlay ad images) → product-photoshoot; Amazon compliance image sets → amazon-product-listing; general image prompt craft methodology → image-prompt-director; full brand visual systems (palette/templates/lighting) → brand-visual-kit; logo design proper → logo-design; multi-page brochure layouts → brochure-designer.

Boundaries (do not use this skill; reroute instead): product multi-angle sets/hero scene images → product-photoshoot; full brand visual system establishment → brand-visual-kit; logo design → logo-design; multi-page brochures → brochure-designer.