---
name: y2k-retro-electronics-tvc
description: "Retro-style everyday electronics TVC: upload a product photo to auto-generate a Y2K-styled TVC for portable electronics."
---

# Wander Portable Electronics Retro TVC

## Feature Positioning

For portable electronic products that can be held in the hand or carried on person: headphones, portable music players, cameras, handheld game consoles, portable speakers, smartwatches, e-readers, small voice recorders, and small shooting devices.

The primary path is the person lifestyle ad: a person picks up, wears, uses, or carries the product, placing it into real-life scenes. Pure product-render ads are also supported, but they must be standalone films and must not be intercut with person narrative shots.

## Fixed User Guidance

### Round 0: Opening introduction, requesting only an image upload

The opening must first state: “This Skill will turn your portable electronics product image into a retro TVC. I will first analyze whether the product is clear, whether the structure and logo are complete, whether the background is clean, and whether a white-background product image needs to be generated first; then I will have you confirm in one round your choice of person lifestyle or pure product render, retro era style, aspect ratio, and duration.”

Then ask the user to upload only their single clearest product image. Do not ask on the first screen what the product is, whether the image is clear, whether it is on a white background, selling points, style, aspect ratio, or duration.

### Round 1: After viewing the image, do only one project confirmation

After viewing the image, first give a brief assessment, then have the user confirm all at once:

- The identified product category and core structure.
- Image quality assessment: directly usable, or a white-background product image must be generated first.
- Ad path: person lifestyle ad (recommended), pure product-render ad.
- Style choice: 90s film campus, 2000s digital ad, city pop summer street, skate street, retro tech studio shoot.
- Aspect ratio choice: 9:16, 16:9, 1:1.
- Duration choice: 15-second video (recommended), 30-second video, 45-second video, 60-second video.

If the user makes no changes, the defaults are: person lifestyle ad, 90s film campus, 15 seconds, 720P, 9:16.

## Product Image and Asset Rules

The Agent makes its own judgment:

- Qualified: complete appearance, clear buttons and ports, accurate primary color, no severe perspective distortion.
- Unqualified: casual snapshots, cluttered backgrounds, hands blocking the product, blown-out reflections, blurry logo. Generate a clean white-background e-commerce image first.

Person lifestyle ads must also generate at the same time: white-background product image, user image, lifestyle scene image, and 3x3 TVC storyboard. Pure product-render ads generate only a product and studio-background storyboard, with no person appearing.

## Asset Closed-Loop Hard Rules

The product image, person image, scene image, and 3x3 TVC storyboard must be passed as reference inputs to the final video node. The storyboard is the visual blueprint of the final video, not an intermediate file that merely gets restated in text.

Before generating video, an asset checklist must be established:

- Person lifestyle path: `product_reference`, `user_reference`, `scene_reference`, `storyboard_reference`.
- Pure product path: `product_reference`, `studio_scene_reference`, `storyboard_reference`.

The final video prompt must begin with a “Reference Inputs” section:

- The person lifestyle path must state: use `product_reference` to lock the product appearance, buttons, ports, and logo; use `user_reference` to lock the person; use `scene_reference` to lock the lifestyle scene; use `storyboard_reference` to control the 0-15s scene establishment, product appearance, usage actions, details, and hero shot.
- The pure product path must state: use `product_reference` to lock the product; use `studio_scene_reference` to lock the studio background and retro lighting; use `storyboard_reference` to control the reveal, structural details, material macro shots, and final hero shot.

It is forbidden for the final video to read only a text version of the storyboard without referencing the storyboard image. If the platform’s video node supports multi-image references, all corresponding assets must be passed in; if it only supports a single-image reference, prefer `storyboard_reference` and state in the prompt that the product, person, or scene has been locked by that storyboard.

## Storyboard Hard Rules

A 3x3 storyboard must be made first, before generating the full video prompt. Each cell contains VISUAL / ACTION / SFX or MUSIC. The storyboard is the blueprint for the whole film and must not be split into 9 short video nodes.

A person lifestyle ad storyboard should include:

- Scene establishment: campus, street, bedroom, rooftop, skate park, or retro studio.
- Product appearance: emerging from a hand, a bag, a desk, beside the ear, or a palm.
- Usage actions: putting on headphones, pressing play, raising the camera, holding the handheld console, adjusting the volume.
- Product details: buttons, ports, screen, metal, plastic, film texture.
- Emotional peak: the person’s expression, turning around, running, a subtle reaction upon hearing the music.
- Hero shot: product clearly visible, strong brand recall.

A pure product-render storyboard should include: product reveal, structural details, material reflections, screen/button/port macro shots, retro lighting, and the final hero shot.

## Structure Distilled from the Original Case

The original Sony-style commercial method was: first create a 3x3 storyboard, then have the video model “generate a complete ad based on the storyboard.” Reusable structure:

- 3x3 storyboard layout.
- Each cell contains VISUAL / ACTION / SFX or MUSIC.
- The film is one complete 15-second video, with multiple shots achieved through editing within it.
- There must be a clear product hero shot at the end.

## 15-Second Video Structure

Person lifestyle ad:

- 0-2s: scene and person establishment.
- 2-5s: product appears and first use.
- 5-9s: dynamic usage and product details.
- 9-12s: emotional peak.
- 12-15s: product hero shot.

Pure product-render ad:

- 0-3s: product reveal.
- 3-6s: structural details.
- 6-9s: material, port, and screen macro shots.
- 9-12s: low-angle or rotating display.
- 12-15s: final hero shot.

## Video Generation Hard Rules

- The default resolution must be 720P.
- In 15-second mode, create only one complete 15-second video node; do not split the storyboard into multiple short videos.
- Generate BGM directly within the 15-second node. The BGM style must be written into the prompt: warm indie pop for 90s film campus; early-2000s electronic pop for 2000s digital; bright city pop groove for city pop; alt rock or skate punk light groove for skate street; breezy pop for summer rooftop; minimal retro electronic for pure product render.
- Also retain button sounds, shutter sounds, electronic beeps, light cable taps, and ambient room sound.
- Split into segments only when exceeding 15 seconds: 30 seconds = 2 15-second segments; 45 seconds = 3 15-second segments; 60 seconds = 4 15-second segments.
- In multi-segment mode, each segment is still a complete 15-second segment and must not be split into 4-6 second sub-segments.
- In multi-segment mode, each video segment generates no BGM, only ambient sound; at the end, generate the complete BGM in one pass and mix it in, retaining the ambient sound.
- The person lifestyle path must not insert pure white-background product rotations; the pure product-render path must not suddenly include person narrative scenes.

## Self-Check
Pre-output check: Is there an opening feature introduction; is there only one round of project confirmation; is 720P the default; does the character path have a 3x3 storyboard first; is the pure product path independent; does the 15-second segment contain only one video node; are character lifestyle and pure product rendering not mixed together; and does the final video node explicitly reference the product images, the character/scene images, and the 3x3 TVC storyboard?