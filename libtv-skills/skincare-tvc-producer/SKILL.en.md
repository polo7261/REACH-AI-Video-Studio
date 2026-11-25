---
name: skincare-tvc-producer
description: "Premium skincare TVC: upload product images to auto-generate models and scripts, completing a high-end skincare commercial."
---

# Wander Skincare 3x3 Commercial

## Functional Positioning

Used to turn skincare or beauty bottled products into high-end commercial short films. The main path is the "model application ad," showcasing the product, texture, application on face or hands, skin radiance, and the final hero shot; it also supports the "pure product render ad," showing only the bottle, ingredient imagery, materials, and lighting.

The model application path and the pure product render path must be kept separate. Do not suddenly insert a pure white-background rotating product render into a model application ad, and do not suddenly introduce narrative characters into a pure product ad.

## Fixed User Guidance

### Round 0: Opening Introduction and Requesting Only an Image Upload

The opening must first state: "This Skill will turn your skincare/beauty product image into a 15-second high-end commercial. I will first analyze whether the image is clear, whether the bottle is complete, whether the background is clean, and whether a white-background product image needs to be generated first; then I will ask you to confirm in a single round your choice of model application or pure product render, visual style, aspect ratio, and duration."

Afterwards, ask the user to upload only the clearest product image. Do not ask on the first screen what the product is, whether the image is clear, whether it has a white background, its selling points, style, aspect ratio, or duration.

### Round 1: After Viewing the Image, Perform Only One Project Confirmation

After viewing the image, first give a brief assessment, then have the user confirm everything in one go:

- The identified product type and bottle characteristics.
- Image quality assessment: can be used directly, or requires generating a white-background product image first.
- Ad path: model application ad (recommended), pure product render ad.
- Style choice: clear water-fresh, luxury repair, clinical tech, natural organic, premium fragrance.
- Aspect ratio choice: 9:16, 16:9, 1:1.
- Duration choice: 15-second video (recommended), 30-second video, 45-second video, 60-second video.

If the user makes no changes, the defaults are: model application ad, clear water-fresh, 15 seconds, 720P, 9:16.

## Product Image and Asset Rules

The Agent makes its own judgment:

- Acceptable: complete bottle, clear packaging structure, accurate main color, no hands blocking.
- Unacceptable: casual phone snapshots, cluttered backgrounds, overexposed reflections, tilted or deformed bottles, severely blurry text. Generate a white-background e-commerce image first.

Model application ads must simultaneously generate: product white-background image, model image, clean bathroom/vanity/natural-light scene image, and a 3x3 commercial storyboard. Pure product render ads generate only product, material, ingredient imagery, and hero scene storyboards.

## Asset Closed-Loop Hard Rules

Product images, model images, scene images, and the 3x3 storyboard must be used as reference inputs for the final video node. The storyboard is not a text outline but an image blueprint that controls the final visual structure.

Before generating the video, an asset inventory must be established:

- Model application path: `product_reference`, `model_reference`, `scene_reference`, `storyboard_reference`.
- Pure product path: `product_reference`, `texture_reference`, `ingredient_scene_reference`, `storyboard_reference`.

The final video prompt must begin with a "Reference Inputs" section:

- The model application path must state: use `product_reference` to lock the bottle; use `model_reference` to lock the model; use `scene_reference` to lock the bathroom/vanity/natural-light environment; use `storyboard_reference` to control the 0-15s shot sequence, product appearance, texture close-ups, model application, and the hero shot.
- The pure product path must state: use `product_reference` to lock the bottle; use `texture_reference` to lock the serum/cream/water-drop textures; use `ingredient_scene_reference` to lock the ingredient imagery; use `storyboard_reference` to control the reveal, macro shots, material reflections, and the final hero shot.

The final video must not rely solely on text shot descriptions without referencing the storyboard image. If the platform's video node supports multiple image references, all corresponding assets must be passed in; if it only supports a single image reference, prioritize `storyboard_reference` and state in the prompt that the product, model, scene, or texture has already been locked by the storyboard.

## Storyboard Hard Rules

A 3x3 storyboard must be used to control the film first, before writing the full video prompt.

The model application ad storyboard should include:

- Product macro: close-up of the bottle or pump head.
- Texture close-up: serum, cream, water droplets, balm textures.
- Model application: dispensing, dabbing, spreading, gentle pressing.
- Skin / mood shot: skin radiance, natural expression, soft lighting.
- Ingredient story: botanical, water-fresh, tech ingredient, or fragrance imagery.
- Luxury hero shot: a closing shot with a clear relationship between the product and the model.

The pure product render storyboard should include: product reveal, bottle structure, texture, ingredient imagery, material reflections, low-angle hero shot, with no model appearing.

## 15-Second Video Structure

Model application ad:

- 0-2s: Establish the product and scene.
- 2-5s: Texture close-up.
- 5-8s: Model dispensing and applying.
- 8-12s: Skin radiance, mood, and lighting.
- 12-15s: Product hero shot.

Pure product render ad:

- 0-3s: Product hero reveal.
- 3-6s: Texture and ingredient imagery.
- 6-9s: Macro shots of materials, cap, pump head, glass.
- 9-12s: Light sweeping across and gentle rotation.
- 12-15s: Final hero shot.

## Video Generation Hard Rules

- The default resolution must be 720P.
- In 15-second mode, create only one complete 15-second video node; do not split each storyboard cell into short videos.
- Generate BGM directly within the 15-second node. The BGM style must be written into the prompt: clear water-fresh uses soft ambient piano; luxury repair uses slow luxury cinematic ambient; clinical tech uses minimal clean electronic; natural organic uses gentle acoustic ambient; premium fragrance uses elegant downtempo.
- Also preserve ambient sounds such as water droplets, the soft click of the cap, cream being spread, and glass gently touching.
- Only split into segments when exceeding 15 seconds: 30 seconds = 2 15-second segments; 45 seconds = 3 15-second segments; 60 seconds = 4 15-second segments.
- In multi-segment mode, each segment is still a complete 15-second segment; do not split into 4-6 second sub-segments.
- In multi-segment mode, each video segment generates no BGM, only ambient sounds; at the end, generate the complete BGM uniformly and mix it while preserving the ambient sounds.

## Compliant Language

Avoid claims of curing, permanent change, medical efficacy, or absolute before-and-after comparisons. Use expressions such as clear visuals, soft radiance, hydrating texture, soothing ambiance, and ingredient inspiration.

## Self-Check

Before output, check: whether there is an opening function introduction; whether only one round of project confirmation is performed; whether the default is 720P; whether the model application path has a 3x3 storyboard first; whether the pure product path is independent; whether 15 seconds produces only one video node; whether model application and pure product rendering are not mixed; and whether the final video node explicitly references the product image, model/texture image, scene image, and 3x3 storyboard.