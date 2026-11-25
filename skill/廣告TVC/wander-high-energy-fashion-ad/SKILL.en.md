---
name: wander-high-energy-fashion-ad
description: "High-tech fashion accessory ad: upload images of glasses, watches, and other accessories to auto-generate high-tempo, premium-quality fashion ads."
---

name: wander-high-energy-fashion-ad
namespace: reach-industry
title: "Wander High-Energy Fashion Accessory Ad"
description: "Create high-energy ads for fashion accessories such as eyewear, watches, necklaces, rings, and earrings. The opening first introduces the function and only asks the user to upload a product image; after viewing the image, the Agent automatically determines the product type, image quality, and white-background restoration needs, then uses one round of project confirmation to select the human-worn or pure product rendering path, style, aspect ratio, and duration. The human-appearance path must first create a storyboard to control visuals and pacing, while the pure product path is produced as a standalone film; mixing is prohibited. Defaults to a single complete 720P 15-second video node with built-in BGM."
version: 1
Wander High-Energy Fashion Accessory Ad
Functional Positioning
Used for fashion accessories as the main product: eyewear, watches, necklaces, rings, earrings, bracelets, brooches, and bag hardware. Clothing serves only as a styling and character-look background and must not overshadow the main product.
The final film can be a high-energy fashion ad with a human wearing the product, or a pure product rendering ad, but the two must be designed separately; human story shots and pure white-background product rendering shots must not be mixed in the same film.
Fixed User Guidance
Round 0: Opening introduction and only request image upload
The opening must first state:
"This Skill will turn your accessory product image into a high-energy fashion ad. I will first analyze whether the image is clear, whether the product structure and materials are complete, and whether a clean white-background product image needs to be generated first, then have you use one round of confirmation to choose between human-worn or pure product rendering, visual style, aspect ratio, and duration."
Afterwards, only ask the user to upload the single clearest accessory product image. Do not ask on the first screen what the product is, whether the image is clear, whether it has a white background, selling points, style, aspect ratio, or duration.
Round 1: After viewing the image, do only one project confirmation
After viewing the image, first give a brief assessment, then have the user confirm everything in one go:
The identified accessory category and core materials.
Image quality assessment: usable directly, or a clean white-background e-commerce image must be generated first.
Ad path: human-worn ad (recommended), pure product rendering ad.
Style selection: black-and-white minimalist editorial, nighttime neon street, cool luxury, retro film, futuristic tech.
Aspect ratio selection: 9:16, 16:9, 1:1.
Duration selection: 15-second video (recommended), 30-second video, 45-second video, 60-second video.
If the user makes no changes, the defaults are: human-worn ad, cool luxury, 15 seconds, 720P, 9:16.
Product Image and Asset Rules
The Agent judges the product image on its own; do not make the user self-assess.
Eyewear: frame, temples, lens reflections, and nose pads must be clear.
Watches: dial, crown, strap, and material texture must be clear.
Jewelry: metal edges, gemstones, chains, and setting structure must be clear.
Casual snapshots, cluttered backgrounds, hand obstruction, or overexposed reflections: generate a clean white-background product image first.
Human-worn ads must simultaneously generate: white-background product image, model image, wearing close-up image, human scene image, and 3x3 high-energy storyboard. Pure product rendering ads only generate the product studio-shoot/material/hero scene storyboard, with no humans appearing.
Asset Closed-Loop Hard Rules
Storyboards and intermediate images must enter the final video node and cannot exist only as process artifacts. Before generating the video, an asset inventory must be established:
Human-worn path: product_reference, model_reference, wearing_reference, scene_reference, storyboard_reference.
Pure product path: product_reference, material_scene_reference, storyboard_reference.
The final video prompt must begin with a "Reference Input" section:
The human-worn path must specify: use product_reference to lock the product structure and materials; use model_reference to lock the person; use wearing_reference to lock the wearing position and proportions; use scene_reference to lock the scene; use storyboard_reference to control the 0-15 second shot sequence, rhythm, and frame composition.
The pure product path must specify: use product_reference to lock the product; use material_scene_reference to lock the materials and studio environment; use storyboard_reference to control the product reveal, macro shots, lighting, and hero shot.
The final video must not read only the textual shot list without referencing the storyboard images. If the platform video node supports multi-image references, all corresponding assets must be used as reference images; if it only supports a single image reference, prioritize storyboard_reference and state in the prompt that the product, person, or materials have already been locked by that storyboard.
Storyboard Hard Rules
The human-worn path must first create a storyboard, then generate the video prompt. The storyboard should control:
Hook: close-ups of the eyes, wrist, ear, collarbone, or fingers, letting the product first appear as a partial detail.
Impact cuts: wearing motion, reflections, materials, detail cuts.
Action: putting on glasses, fastening a watch, adjusting a necklace, raising a hand and turning the head, earrings swaying gently with the movement.
Controlled moment: slow down to macro, showing lenses, dials, gemstones, and metal textures.
Energy return: low-angle push-in, rapid pose changes, or lateral tracking shots.
Brand attitude: a clear hero pose, with the person and product holding a stable freeze.
The pure product rendering path must also first create a storyboard, but it only revolves around product structure, materials, lighting, and the hero shot, without writing human actions.
Distilled Rhythm from the Original Case
The core of the original high-energy ad case is not "many short video nodes," but clearly spelling out timing, rhythm, contrast, camera behavior, and texture in a single 15-second prompt:
0-2s Hook.
2-5s Impact cuts.
5-8s Chaotic style.
8-11s Controlled moment.
11-13s Energy return.
13-15s Brand attitude.
The prompt must spell out the rhythm and camera movement, not just write "premium, fashionable, cool."
Video Generation Hard Rules
The default resolution must be 720P.
15-second mode must create only one complete 15-second video node; do not split it into 2-second, 3-second, or 5-second small nodes.
BGM is generated directly within the 15-second node. The BGM style must be written into the prompt: cool luxury uses dark luxury electronic; street high-energy uses fast trap beat; black-and-white minimalist uses minimal techno; futuristic tech uses futuristic electronic; retro film uses analog synth groove; nighttime neon uses neon cyberpop.
Also retain ambient sounds such as light metal clinks, leather friction, glass taps, and wearing motion sounds.
Only split into segments beyond 15 seconds: 30 seconds = 2 × 15-second segments; 45 seconds = 3 × 15-second segments; 60 seconds = 4 × 15-second segments.
In multi-segment mode, each segment is still a complete 15-second segment and must not be split into 4-6 second small segments.
In multi-segment mode, each video segment generates no BGM, only ambient sounds; after all segments are complete, generate the full BGM and mix it in.
The human-worn path must not insert pure white-background product rotation renders; the pure product rendering path must not suddenly include model story scenes.
Output
Output the product image assessment, white-background restoration prompt, project confirmation summary, human/pure product path selection, 3x3 storyboard, and a single complete 15-second video prompt or multiple 15-second segment prompts.
Self-Check
Before output, check: whether there is an opening function introduction; whether only one round of project confirmation is done; whether the default is 720P; whether the human path has a storyboard first; whether the pure product path is produced as a standalone film; whether the 15 seconds consists of only one complete video node; whether human story and product rendering are not mixed; and whether the final video node clearly references the storyboard and the corresponding product/person/scene reference images.