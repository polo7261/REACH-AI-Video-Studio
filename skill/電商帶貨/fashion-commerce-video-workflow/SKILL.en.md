---
name: fashion-commerce-video-workflow
description: "Lifelike womenswear shoppable video generation: upload womenswear photos to one-click create 15-second vertical social-media sales videos"
---

1. Low-friction entry question First output a one-sentence introduction, then ask only: Do you have product photos of the women's clothing you want to sell? If so, just send this one photo first. Do not, in the first step, also ask for the model, scene, brand, copy, publishing platform details, or a full brief.
2. Product image analysis and product image threshold After receiving the product image, first classify it: Casual phone snapshot: cluttered background, handheld angle, shadows, wrinkles, or obvious interference from a hanger or a person's body. Clean white-background image: the product is relatively isolated and can be used directly or with light cleanup. Model try-on image: shows the on-body effect, but the garment itself needs to be extracted. Flat-lay image: the structure is clear, but it lacks a real sense of how the garment looks when worn. Mixed-scene image: the product is visible, but the background and props will interfere with compositing. Then assess product structure coverage: Whether the neckline/collar is visible. Whether the sleeves/shoulder straps are visible. Whether the waistline and hem are visible. Whether the garment length, skirt length, or pants length is clear. Whether the fabric texture and color are clear. Whether the overall silhouette and cut are clear. Whether the front-facing subject is sufficiently complete. Whether key selling-point details are visible. At the same time, run a "sellable outfit and accessories inventory": Identify whether the image contains visible styling items such as stockings, socks, shoes, bags, belts, hats, scarves, jewelry, hair accessories, gloves, and glasses. Determine whether these accessories are part of the product, part of the outfit set, or merely shooting props. If the user has not explicitly ruled them out, by default list strongly garment-related wearable pairings such as stockings, socks, shoes, bags, belts, and jewelry in the "accessories-to-keep list", and do not delete them outright during white-background extraction. If you are unsure whether a particular accessory should be kept, output an "accessories-to-confirm list" and have the user confirm, rather than removing it on your own. Assessment result: Pass: you can proceed to product extraction. Conditional pass: the structure is basically usable, but white-background extraction must be done first, and the user should be alerted to possible detail risks. Fail: the garment is too blurry, heavily occluded, cropped too much, or missing core structure; ask the user to swap in a different image.
3. Extract the white-background product image If the product image is not a clean white-background product shot, first generate a white-background image containing only the garment. Product extraction prompt: Extract the women's clothing product itself and the sellable outfit elements that need to be kept from the reference image, removing people, hands, hangers, cluttered background, and shadows; generate a clean white-background product image, shown front-facing, with the neckline, sleeves, waistline, hem, length, fabric texture, and key design details clearly visible. Preserve the original color, material, tailoring, proportions, and cut; do not add new patterns or alter the design. If the frame contains visible accessories strongly related to this outfit, such as stockings, socks, shoes, bags, belts, hats, scarves, jewelry, hair accessories, gloves, or glasses, first add them to the accessories-to-keep list and do not delete them by default. If the accessories belong to the outfit being sold: Extract the complete sellable outfit from the reference image, including {accessory list}; the items the user has confirmed to keep, such as stockings/socks, shoes, bags, belts, and jewelry, must be preserved in full and placed together on a clean white background. Each item keeps its true color, material, proportions, texture, pattern, and relative style; do not add new accessories, and do not mistakenly delete accessories as background props. Output requirements: A clean white-background women's clothing product image. An assessment of product structure completeness. Sellable outfit/accessory list: write the three categories — already kept, pending confirmation, and deletable — separately. Risk points that still need user confirmation.
4. Ask about the model and scene at the same time While preparing to extract the white-background product image, also ask: I'm about to generate a clean white-background product image for you. Do you have any photos or preferences for the model and scene? If not, I can also generate a model-and-scene set that suits this piece of women's clothing. If the user provides model/scene images, do reference image analysis. If the user has no reference images, generate: One adult female fashion model reference image, which must be a white-background landscape two-view layout: a full-body view on the left showing body proportions, and a facial close-up on the right showing facial feature details, skin texture, and makeup and styling. 2-3 completely different portrait-orientation realistic scene candidate images; have the client choose one first before moving on to try-on master template generation; do not generate just one generic, empty scene image at a time. If multiple scene, model, or master template options are generated, you must have the client choose which one they prefer. By default, have the client choose the scene first, then create the try-on master template. Model reference prompt: Generate a white-background, landscape-orientation reference image of an adult female fashion model, laid out as a two-view left-right composition: on the left is a full-body standing shot of the model, fully showing body proportions, shoulders and neck, waistline, leg proportions, and overall posture, with a natural, relaxed stance suitable for later try-on of {product type}; on the right is a facial close-up of the same model, clearly showing facial feature details, skin texture, makeup and styling, hairstyle, and overall presence. Both sides must be the same adult female model with a consistent identity and consistent makeup and hair; clean white background, landscape composition, usable for commercial product-selling videos; avoid exaggerated poses, over-sexualization, multiple people, complex backgrounds, and occlusion. Model image output checks: It must be white-background landscape; do not produce a portrait-orientation single-person image. The left side must show complete full-body proportions. The right side must be a facial close-up of the same model, with the facial features, skin texture, and makeup clearly visible. Do not generate two different models, and do not let the facial close-up turn into a second person. Scene reference prompt: Generate 2-3 completely different portrait-orientation realistic indoor scene candidate images, for use in the try-on master template of a women's clothing product-selling video. Each one must look like a living space or small shooting corner captured on a real phone, not like a blank studio, a staged model home, a 3D render, or an over-retouched mansion. Each scene must leave room for an adult female model to stand at full height and walk around slightly; the background must not steal attention from the garment as the subject, and must contain no readable text, watermarks, brand logos, or cluttered crowds.
Scene A: Realistic natural-light bedroom / fitting-mirror corner. The frame contains a full-length mirror or clothing rack, a window, light-colored curtains, wooden flooring or a soft rug; afternoon natural light enters from the side, casting soft shadows on the floor, and the space shows slight lived-in traces without being messy.

Scene B: Minimalist living room / sofa corner. The frame contains a gray or off-white sofa chair, crisp or soft natural light from the window, low-saturation walls, and a clean floor; suitable for the model sitting back, standing, and showcasing bags/shoes/hems. The cushions, upholstery, and shadows must look real.

Scene C: Vintage white brick wall / sheer-curtain shooting corner. The frame contains a white brick wall, a floor-to-ceiling window or sheer curtains, natural-light boundaries, and clean wall layering; suited to cool-toned or premium womenswear showcases. The sheers may carry an extremely faint sense of breeze, but no exaggerated billowing.

Scene candidate output requirements:

- Each scene must be clearly distinct: space type, background materials, light direction, and prop vibe must not repeat.
- Tag each scene with the outfit styles it suits, e.g., office/commute, sweet, cool-toned, premium, everyday UGC.
- Scene realism takes priority over "looking pretty": keep natural window light, floor shadows, curtains/sheers, sofa/rug/wall materials, and slight lived-in traces.
- Do not generate scenes that are overly luxurious, overly empty, pure-white studio shots, strongly AI-looking, plastic-feeling, overloaded with background decorations, or likely to upstage the product.
- Have the user pick one of the 2-3 scene images as the scene reference for the try-on master that follows.

5. Generate the try-on master image

Composite the white-background product image, the adult model image, and the scene image into a try-on master image.

Master image prompt:

Accurately put the womenswear from the white-background product image onto the adult female model, preserving the garment's original color, material, cut, silhouette, neckline, sleeves, waistline, and hem structure. The model stands in the reference scene, in a 9:16 vertical commercial product-seeding frame, with natural body proportions, the outfit fully and clearly visible, soft and realistic lighting, a stable background, and no changes to the product design.

When using the references:

{{Product Image}} locks the womenswear's structure and material, {{Model Image}} locks the adult model's identity and build, {{Scene Image}} locks the scene layout and lighting; dress the model in the product accurately and generate a 9:16 vertical try-on master image with the outfit fully and clearly visible, natural body proportions, and a stable background.

After generating multiple master candidates, you must ask:

Which of these do you like best as the master for the final video? All subsequent videos will be based on it.

6. Refine the master image

Make only narrow-scope corrections; do not overhaul the product, model, scene, and pose all at once.

Refinement prompt:

Keep the person's identity, the scene, and the garment design unchanged; fix only {issue}, making the garment structure clearer, the body proportions more natural, and the frame better suited to a 9:16 shoppable video.

Common fixes:

- Fix deformations in the hands, shoulders, waist, knees, or feet.
- Make the skirt hem, waistline, neckline, or cuffs clearer.
- Remove clutter from the background.
- Get the model's full body completely into frame.
- Improve fabric texture and image sharpness.

7. Final video shooting perspective choice

Before generating the video, first have the user choose a shooting perspective:

Which shooting perspective do you want for the final video?

A. Third-person camera: the model showcasing the outfit is filmed from a photographer's perspective; the footage looks more like a commercial product-seeding video.

B. UGC selfie: the girl naturally films herself in the mirror; more slice-of-life, more like a real user sharing.

C. Both perspectives: generate one third-person version and one UGC selfie version at the same time, for easy comparison testing.

If the user chooses C, do not mix the two perspectives in a single 15-second video; instead output two independent Seedance 15-second video prompts. Each video still uses only one Seedance video node of its own, and each completes its one-take or multi-shot segmentation within that same single 15-second node.

8. 15-second video structure choice

Then have the user choose the 15-second structure:

Which structure do you want for this 15-second video?

A. One-take showcase: a single continuous shot completes the full outfit showcase; more natural, more like real filming.

B. Multi-shot segmentation: within the same 15-second video node, naturally cut between multiple storyboarded shots showing the full body, the upper body, fabric details, and a closing freeze frame; this does not mean generating multiple separate videos.

If the user makes no explicit choice, default to "multi-shot segmentation", but keep the focal length of the phone or fixed camera consistent, and do not suddenly switch to telephoto close-ups.

9. Final video model and structure

Default model and specs:

- Model: Seedance 2.0 VIP; if the backend model tags do not include VIP, use Seedance 2.0.
- Resolution: 720P.
- Aspect ratio: 9:16.
- Duration: 15 seconds.
- Node: create and use only one Seedance video node, outputting a single complete 15-second long video. Multi-shot segmentation is written only into the [15-second shots] timecodes of the same prompt; do not split it across multiple video nodes or multiple short clips.
- Audio: by default generate light BGM whose style matches the outfit and route — e.g., upbeat and casual, cool and premium, relaxed commuter, or refined product-seeding — while keeping an appropriate amount of natural ambient sound, footsteps, and fabric rustle.

Hard rules:

- If one-take is chosen, it must be written as a single continuous yet layered, real-filming shot: the person, camera, or phone may move forward and back, with the action flowing from full-body showcase into details, then back out to a natural close.
- If multi-shot segmentation is chosen, it must be written as "natural editing within the same 15-second video node", with natural transitions between shots: full-body hook, upper-body details, fabric/hem dynamics, and a final hero shot. Do not output flows like "generate 4 video segments", "3 seconds each", or "generate separately then stitch together".
- Multi-shot segmentation must have clearly visible edit points and at least 3 distinct cuts; it must not be written as a one-take of continuous push-ins, pull-outs, pans, and tilts. Each timecode segment must differ in composition, subject distance, action focus, and where the frame lands; the prompt must state "edit points clearly visible — do not use continuous camera movement to disguise it as a one-take".
- If the backend video node has a "multi-shot / shot cut" toggle, turn it on first when multi-shot segmentation is chosen; but even without it, you must constrain this with explicit editing language inside the same Seedance 15-second prompt.
- Each timecode segment must specify the shot size, camera strategy, the model's action, the garment-showcase purpose, and where the frame lands.
- Do not use different focal lengths to create jarring changes. Keep a common phone wide-angle/standard-wide perspective throughout, around 23mm-28mm; detail showcases are achieved by pushing the camera in, moving the body closer, pointing with the hand, or lowering the phone — never by suddenly switching to a long telephoto close-up.

Reference image usage rules:

- {{Product Image}} locks the product's design, material, color, cut, and details.
- {{Omni Reference Image}} takes the final try-on master or template image as the input for Seedance's omni reference mode, locking the adult model, the on-body look of the outfit, the scene, composition, lighting, and overall style.
- Do not describe {{Omni Reference Image}} as the first frame, last frame, opening frame, or ending frame.
- Do not ask to generate a first-frame image before generating the video; the final video prompt must directly drive the same single Seedance 15-second video node.

10. Garment showcase action library

When generating the final 15-second prompt, pick and combine 3-5 actions from the action library below, so the model isn't standing still the whole time with thin or stiff movements. Actions must serve the garment showcase and must not block the product just to "look good".

Canvas 3-second action absorption rules:

- What's excluded is the production path of "generating multiple 3-second video nodes separately and then stitching them together", not the action know-how from the canvas's 3-second nodes.
- The canvas's 3-second actions must be absorbed as "action atoms" into the same single 15-second Seedance video node, scheduled into internal timecode segments such as 0-3s, 4-7s, 8-11s, and 12-15s.
- Each action atom must clearly state: action name, trigger pose, subject dynamics, scene setup, detail supplements, and entry timecode.
- The subject dynamics must be a concrete action chain, not an abstract slogan; write it as "where it starts -&gt; how it moves -&gt; where it stops -&gt; how the gaze/expression changes".
- The detail supplements must include at least 2 natural details: breathing rise and fall, fabric stretching, skirt-hem/trouser-leg inertia, hair strands stirring slightly, stocking texture under tension, a shoe tip tapping the ground, a bag chain swaying, lens reflections, nail highlights, cushion indentations, curtains stirring slightly, light-shadow transitions.
- You must write "normal 1x speed, no slow motion, fluid continuous movement, stable frame rate, consistent with biomechanics and real gravity", to keep the model from turning showcase actions into stiff posing or exaggerated slow motion.
- Do not just write "natural showcase, strike a pose, turn around, look at the camera"; those phrases must be replaced with concrete action chains.

Action atom library:

- Relaxed deep breath: the person releases from hands-folded or arms-crossed, lets both arms fall naturally down to the sides with shoulders sinking slightly, takes one clearly visible deep breath, and lets the gaze drift toward the window; the chest's rise and fall ripples the top's wrinkles, and the arms fall with real gravity.
- Hands-on-hips fit showcase: after the hands fall naturally to the sides, they come to rest on the hips; the upper body angles slightly to the side and the hips sway gently once, showing the waistline, the fitted cut of the skirt/trousers, and leg proportions; the hem genuinely pulls in response to the hips.
- Waist stroke, hem smooth: the right hand glides slowly from the collarbone to the waistline while the left hand lightly smooths the skirt edge or hem, stopping at the garment's selling point; highlights travel along the arm, with fabric texture and drape clearly visible.
- Gentle hair tuck: the right hand lightly brushes the cheek and tucks stray hair behind the ear, the head tilts slightly before turning back to the camera, and the left hand rests naturally on the hip or at the waist; strands float softly with the hand movement, and the light on the face transitions smoothly.
- Hair tuck with toe tap: the legs subtly shift weight in place, the right toe lightly taps the ground, the right hand sweeps hair behind the ear, and the gaze settles naturally on the camera; stocking texture or leg highlights shift subtly with the tension.
- Fingertip to lips: the left hand rises and the index finger lightly touches the lower lip; the head dips slightly, then lifts, eyes looking up into the camera; the finger movement is delicate, with subtle shifts of light on the neck and collarbone.
- Chin lift / glasses nudge: the hand rises slowly from the waist and lightly tips the chin or nudges the glasses' bridge; the chin lifts slightly and the gaze returns from the side to the camera; lens reflections, nail highlights, and a faint tremble at the hair tips.
- Bag-chain caress: seated leaning or standing at an angle, the person lifts the bag chain with the right hand and runs the fingers up and down the chain once, the gaze drifting slowly from the window back to the camera; sequins or leather catch the light on the bag, and the body's weight leaves a cushion indentation or sets the chain gently swaying.
- Sweet heart sign: both hands dart up to the chest to form a heart, the weight sways gently left and right once, with a natural smile or a wink; hair at the cheeks, skirt pleats, and light and shadow all flow with the movement.
- Sudden realization: the gaze snaps back quickly from the upper side to the camera, lightly bites the lower lip, then parts the lips slightly, while the left hand rises a little, palm up; the eye's reflection turns with the gaze, and the hand movement is crisp, never sluggish.

Full-body movement:

- The model walks naturally from one side of the frame toward the window or mirror in small steps, showing the full silhouette first.
- A half turn in place or a 45-degree side angle to show the waistline, the side cut, and skirt/trouser-leg length.
- The legs subtly shift weight, toe tapping the ground or a half step back, bringing the full-body proportions into frame.
- When sitting or leaning back, the body settles against the backrest to one side with weight shifting backward, leaving real indentations in the garment and cushion.

Upper body and hands:

- One hand adjusts the neckline, cuff, or strap while the other rests naturally at the waist.
- The right hand lightly brushes stray hair by the ear, the head tilts slightly, and the left hand stays on the hip, creating a natural eye-line exchange.
- After both hands fall naturally to the sides, they come to the hips; the upper body angles slightly to show the fit.
- Fingers lightly tap the chin, touch the lower lip, nudge the glasses, or raise the palm slightly — used as micro-expression transitions.
- The right hand glides from the collarbone to the waistline while the left hand lightly strokes the skirt or hem, emphasizing the waistline and the fabric's drape.

Garment detail showcase:

- A hand lightly tugs the garment corner, cuff, hem, or skirt edge to bring out the fabric's texture, stretch, and cut.
- The camera/phone pushes in to the upper body or waistline, keeping the 23mm-28mm phone perspective, with no cut to telephoto.
- The hem, skirt, or trouser legs swing naturally with turns or weight shifts, showing the material's weight.
- Light sweeps across the neckline, shoulder line, waistline, and fabric surface, emphasizing texture without changing color.

UGC selfie actions:

- Throughout, the girl films with the same phone held in the same hand; the phone's edge, the wrist holding it, or the phone's reflection in the mirror must remain plausibly and continuously present.
- At the opening, the phone is held at chest-to-face height; the frame first shows the upper body and the main body of the outfit, the holding hand stays steady, and the free hand rests naturally at her side.
- For detail showcases, the phone in the holding hand lowers naturally to the waistline and hem while the free hand points at the fabric, lightly tugs the garment corner, or adjusts the cuffs; never let both hands leave the phone at once.
- For the full-body mirror shot, the girl takes a half step back or turns gently halfway to the mirror; the phone must stay in her hand, with the phone or holding arm visible in the mirror, to show proportions and length.
- When returning to a medium close-up, the phone is still held in the same hand while the free hand lightly tidies hair or a collar, closing on a natural, satisfied everyday expression.
- Avoid actions that require both hands at once — heart signs with both hands, hands on both hips, adjusting clothes with both hands; the selfie route can only use the structure "steady filming hand + free hand showcasing the outfit".

Action combination rules:

- Do not cram more than 5 major actions into 15 seconds.
- Every pair of actions needs a natural link, e.g., "adjust the collar -&gt; half turn -&gt; lightly stroke the hem -&gt; look into the camera to close".
- Keep real gravity, breathing, fabric stretching, subtle hair movement, and light-shadow changes.
- Avoid exaggerated runway strutting, over-the-top flirtation, mechanical posing, sudden large jumps, or complex dance.

Prompt guide

Scene realism patch

Scene-building rules absorbed from the canvas:

- Don't just write "clean indoor space, soft light" for the scene. You must write concrete spatial anchors: by the window, floor-to-ceiling window, sheer curtains, white brick wall, sofa chair, full-length mirror, clothing rack, wooden floor, rug, wall material.
- Don't just write "natural light" for the lighting. You must write the light's source and where it lands: afternoon side-window light, sun shadows on the floor, crisp light through the window, transitions across the lit side of the face, highlight boundaries on the legs, soft reflections on the wall.
- Realism comes from subtle environmental details: curtains/sheers swaying barely at all, minimal shifts of the floor shadows, sofa cushions denting under weight, fabric materials, low-saturation walls, and a space with slight lived-in traces but no clutter.
- Do not casually add new scene elements during video actions. Most shots keep "the indoor environment unchanged, the sense of space as it was, no new elements intruding"; only micro-changes like light and shadow, the sheers, and fabric indentations are allowed.
- The background must serve the garment showcase: leave a clear path for full-body movement, don't block the hem, shoes, stockings, or bag, and no eye-catching text, logos, crowds, or heavy decorations.

Route A: Third-person commercial product-seeding

For womenswear showcases that lean more refined, commercial, lookbook-like, and product-seeding in feel.

[Asset lock]

{{Product Image}} locks the womenswear product's color, material, cut, and key design; {{Omni Reference Image}} uses omni reference mode to lock the final try-on master's person, the on-body look of the outfit, the scene, composition, lighting, and overall style. {{Omni Reference Image}} is not the first frame and must not be used as a first frame.
【Style】 15-second vertical commercial product-seeding video, shot from a third-person photographer's perspective showing an adult female model presenting womenswear, with realistic indoor natural light. The scene has clear spatial anchors: window / window gauze / sofa chair / white brick wall / full-length mirror / wooden floor, etc., retained according to the selected scene; floor shadows, wall reflections, and fabric textures are realistic. The look of a common wide-angle shot from a phone or fixed camera: keep an approximately 23mm-28mm field of view throughout, with no sudden switches to telephoto close-ups; the camera may move slightly forward and back, detail shots are accomplished by pushing in closer, and slight natural wide-angle distortion at the frame edges is acceptable. Skin tones are natural, fabric texture and tailoring are clear, and the camera serves the garment showcase. By default, generate a lightweight fashion BGM, keep faint fabric-rubbing and footstep sounds, do not be overly cinematic, and do not use exaggerated slow motion.

【15-Second Shots】 Generate one complete 15-second video within the same Seedance video node; the following are the natural editing storyboards inside that video, not split into multiple video segments: 0-3s: Open on a medium-full shot, filmed steadily from the photographer's third camera position; the model takes small steps into the frame from one side or turns gently toward the camera from a still standing pose, first letting the outfit fully enter the frame; shoulders relaxed, arms falling naturally at her sides, she takes a slight deep breath, the rise and fall of her chest creating real folds in the top/outerwear, so the overall silhouette is clear at first glance. 4-7s: Cut to a medium shot, still keeping the same phone wide-angle look; the model slides one hand from her collarbone down to her waistline while the other lightly adjusts the neckline, cuffs, or shoulder straps, with the movement pausing at the garment's selling point; highlights travel along the arms, neckline/shoulder lines/fabric texture are clear, and hair strands sway slightly and naturally. 8-11s: Cut to an above-the-knee shot or a full-body side angle; the model naturally shifts to hands on hips, tilts her upper body slightly, sways her hips gently once or taps her toe on the floor once; the skirt hem/lower hem/trouser legs/stocking texture stretch and sway realistically under the applied force, showing the cut, length, and on-body proportions. 12-15s: Cut to a medium-close shot ending on a product hero frame; the model lightly brushes the loose hair by her ear or rests a hand on her waistline, then looks toward the camera to close, expression natural and not stiff; fabric, hair strands, bag chain, or shoe tips retain subtle inertia, the outfit is complete and clear — a fitting ending for a product sales video.

【Multi-Shot Editing Constraint】 If the user chooses multi-shot splitting, this 15-second video must contain clearly visible edit points inside it; do not disguise it as a one-take with continuous camera movement. There must be clear transitions between 0-3s, 4-7s, 8-11s, and 12-15s: subject distance, composition, action focus, and where the frame settles must all differ; hard cuts, slight jump cuts, or match cuts common in real phone-shot content may be used, while still keeping the same space, same person, same outfit, and the same phone focal-length look.

【Natural Motion Constraint】 Each timecode segment uses atomic action writing: clear subject motion, a basically stable scene, and ample supporting details. Normal 1x speed, no slow motion; motion is smooth and coherent, frame rate stable, consistent with biomechanics and real gravity; use breathing, fabric stretch, subtle hair movement, light-and-shadow transitions, stress on stocking texture, toe taps, or slight bag-chain sway to enhance realism.

【Negative Exclusions】 Do not change the garment design, do not swap colors, do not add patterns, do not omit confirmed accessories such as stockings, socks, shoes, bag, belt, or jewelry, no limb deformation, no facial drift, no random background changes, no readable text watermarks, no sudden telephoto switches or perspective compression, no mixing of different focal lengths, no excessive glossy ad-campaign look, do not split into multiple video nodes, and do not use the omni reference image as the first frame. Route B: UGC Natural Selfie — suitable for authentic sharing, everyday-life content, user product-seeding, and natural mirror showcase. 【Asset Lock】 {{产品图}} locks the womenswear product's color, material, tailoring, and key design details; {{全能参考图}} uses omni-reference mode to lock the person, the on-body garment look, scene, composition, lighting, and overall style of the final try-on master. {{全能参考图}} is not the first frame and is not used as the first frame.

【Style】 15-second vertical UGC selfie video, where a girl shows today's outfit to the mirror like a real user. She must hold the same phone in the same hand for the entire shot; the phone is a continuously trackable prop: the phone's edge, the holding arm, or the holding wrist should be visible, or the phone's reflection in the mirror visible during the full-body mirror segment. Maintain the look of a common ~23mm-28mm phone front-facing/handheld lens, no sudden telephoto switches, no cutting to a third camera position; natural and everyday, with slight handheld shake but a stable picture. Detail shots are achieved by the holding hand lowering the phone, bringing it closer, or raising it again; slight natural distortion at the frame edges is acceptable. Real indoor lighting; retain the real spatial anchors of the chosen scene, such as windows, curtains/window gauze, mirror, sofa, wooden floor, or white brick wall; skin and fabric textures are not over-retouched, the tone feels like casual sharing rather than a polished ad, and the focus remains clearly on showing the outfit. By default, generate a lightweight everyday-life BGM and keep faint ambient sound.

【15-Second Shots】 Generate one complete 15-second video within the same Seedance video node; the following are the natural editing storyboards inside that video, not split into multiple video segments: 0-3s: Open on a selfie medium shot; the girl raises the phone with the same hand to chest-to-face height, with a slight shake at the frame edges that feels like a real handheld selfie; the frame first shows the upper body and the main garment, she naturally looks at the phone screen, gives a light nod or takes a slight deep breath, shoulders relaxed, the fabric rising and falling realistically with her breath, while her free hand rests naturally at her side. 4-7s: Cut to a selfie angle on the waistline and hem; the holding hand still grips the same phone and moves the camera down naturally — the phone must not disappear; the girl uses her other free hand to glide from the waistline to the hem, lightly tugging the garment corner, adjusting cuffs, or pointing at fabric details, with the movement pausing at the garment's selling point; hand movement is smooth and continuous, and fabric texture, drape, and stretch are clear. 8-11s: Cut to a full-body-in-the-mirror or half-step-back selfie frame; the girl still holds the same phone in hand, with the phone/holding arm visible in the mirror or at the frame edge; she naturally turns half a circle or taps her toe once, showing the overall outfit proportions, garment length, and how the stockings/socks/shoes or bag coordinate; the hem, trouser legs, bag chain, and hair strands keep subtle inertia with the movement. 12-15s: Cut back to a medium-close shot; the holding hand raises the same phone back to chest-to-face height, and the other free hand lightly brushes the loose hair by her ear or adjusts the collar before looking back at the phone screen, closing with a natural, everyday satisfied expression; the frame ends with the outfit clearly visible, and the phone, holding arm, and selfie perspective remain continuous and plausible.

【Multi-Shot Editing Constraint】 If the user chooses multi-shot splitting, this 15-second video must contain clearly visible selfie edit points inside it; do not disguise it as a one-take with continuous handheld camera movement. There must be obvious jump cuts between 0-3s, 4-7s, 8-11s, and 12-15s, or a sense of transition after re-raising the phone: the four compositions — upper body, waistline and hem, full body in the mirror, and back to medium-close — must all differ; still keep the same space, same person, same outfit, same phone, same holding hand, and the same phone focal-length look. The start of each edited segment must re-confirm that "the phone is still in her hand," avoiding the phone suddenly disappearing.

【Natural Motion Constraint】 Each timecode segment uses atomic action writing: clear subject motion, a basically stable scene, and ample supporting details. Normal 1x speed, no slow motion; motion is smooth and coherent, frame rate stable, consistent with biomechanics and real gravity; use breathing, fabric stretch, subtle hair movement, light-and-shadow transitions, stress on stocking texture, toe taps, or slight bag-chain sway to enhance realism.
【Negative Exclusions】
No overly commercial blockbuster look, no exaggerated runway walk, no altering the garment design, no changing colors, no adding new patterns, no omitting confirmed accessories such as stockings, socks, shoes, bags, belts, or jewelry, no face drift, no deformed fingers, no erratic background changes, no readable text watermarks, no sudden cuts to telephoto close-ups, no mixing different focal lengths, no splitting into multiple video nodes, and do not use the omni-reference image as the first frame.
On the UGC selfie route, it is strictly forbidden for the phone to suddenly disappear, for both hands to leave the phone, for the phone to float, for the shot to suddenly switch from the selfie perspective to a photographer-style third-person camera, or to adjust the clothes with both hands while maintaining the selfie framing.

Structure A: One-Take Showcase Template
When the user selects the one-take option, use the structure below and do not split it into multiple shots:
If the shooting perspective is a UGC selfie, every "camera or phone movement" below must be understood as performed by the girl holding the same phone in the same hand; the other free hand may adjust the collar, point at the fabric, or lightly tug the hem, but both hands must never leave the phone at the same time.

【15-Second Shot】
0-4s: Continuous medium-full shot from the phone or a fixed camera. The model starts from a natural standing pose, turns slightly toward the camera, lets her arms drop naturally, and takes one slight deep breath as the full outfit enters the frame.
5-8s: The camera or phone slowly pushes in. With one hand the model glides from her collarbone down to her waistline or adjusts the collar/cuffs, while the other hand rests lightly on her waistline; the movement stops at the selling point, showing the upper-body construction and fabric texture. Maintain a roughly 23mm-28mm phone perspective.
9-12s: The model does a half turn in place or takes a half step back, taps a toe against the ground or gives one slight hip sway, and a hand lightly tugs the garment edge/hem; the fabric, stocking texture, and skirt hem/pant legs sway naturally with the motion, showing the length and cut.
13-15s: The camera stays steady as the model returns to a natural front-facing or slightly angled pose and lightly adjusts her hair or collar; her hair and clothing retain a subtle follow-through inertia, the outfit is clearly visible, and the shot settles into a closing freeze frame.

Structure B: Multi-Shot Split Template
When the user selects multi-shot splitting, use the structure below. Note: this is still one 15-second video inside the same Seedance video node; you are only describing the internal edited shots in the prompt. Do not generate several separate videos and do not output multiple video nodes.
If the shooting perspective is a UGC selfie, after every shot change you must re-confirm the phone is still in the same hand — a jump cut must not make the phone vanish; in full-body mirror segments, the phone or the arm holding it should plausibly appear in the mirror/at the edge of the frame.

【15-Second Shot】
Generate one complete 15-second video inside the same Seedance video node; the timecodes below are different shots naturally cut within that single video. The cut points must be clearly visible — do not use continuous camera movement to fake a one-take. There must be at least 3 clear cuts, and after each cut the subject distance, composition, action focus, and product-showcase focus must all be different.
0-3s: Open on a medium-full shot from a common phone/fixed-camera wide-angle perspective, letting the full outfit enter the frame first.
4-7s: Cut to a medium shot, keeping the same phone-focal-length texture; the model uses one action atom to show the upper body: adjusting the collar/cuffs/straps, or gliding a hand from collarbone to waistline, with the movement stopping at the garment's selling point.
8-11s: Cut to a waistline/knee-up/full-body side angle; the model uses one action atom to show the lower body and the cut: a half turn, a toe tap, a light hip sway, or lightly tugging the hem, showing the waistline, hem, skirt hem/pant legs, and the motion of the stockings/shoes.
12-15s: Cut back to a medium close-up or a full-body hero shot; the model closes with one action atom: brushing her hair back, resting a hand lightly on her waistline, looking at the camera, giving the bag chain a light swing, or a natural smile, with the outfit and confirmed accessories fully and clearly visible.

Route C: Generating Both Perspectives Simultaneously
When the user selects "I want both perspectives":
Output two separate video plans: Video 1: third-person camera commercial product-seeding, and Video 2: natural UGC selfie.
Both videos default to 15 seconds, 9:16, 720P, Seedance 2.0 VIP / Seedance 2.0.
Each video uses only one Seedance video node. Do not cut the third-person camera footage and the selfie footage together into one 15-second video unless the user explicitly requests a mashup.
Both videos use the same set of product images, omni-reference images, selected scene, and garment constraints, to make A/B testing easy.
If the user also selects "multi-shot splitting," both videos must enforce the clearly-visible-internal-cut-points constraint.
Video 2: natural UGC selfie
The phone continuity constraint must be enforced: the same hand, the same phone, with the phone's edge/the arm holding it/its mirror reflection continuously and plausibly present; the phone must never suddenly disappear.

Output
Depending on the stage, output the following:
A one-sentence Skill introduction.
In the first round, ask only for the product images.
An analysis of the product image type and garment structure.
Whether the product images pass the entry threshold.
The white-background product-image extraction prompt or extraction plan.
The fallback plan for image-node failures: a neutralized rewrite of the prompt, a Lib Image retry, and trying Lib Navo Pro / Lib Navo 2 in parallel or in sequence.
The retention checklist for sellable outfits/accessories, specifically checking whether stockings, socks, shoes, bags, belts, jewelry, etc. need to be kept.
Asking about model/scene requirements.
The white-background landscape model-reference-image prompt or reference-image analysis.
2-3 prompts for completely different real-scene candidates, and have the client choose one scene.
The try-on master generation prompt.
Client choice points.
The shooting-perspective choice: third person, UGC selfie, or both perspectives generated simultaneously.
The structure choice: one-take or multi-shot split.
Seedance 2.0 VIP / Seedance 2.0 720P video prompts; if a single perspective is chosen, output one 15-second single-node prompt; if both perspectives are generated simultaneously, output two independent 15-second single-node prompts.
Multi-shot splitting must be written as a shot-by-shot description inside the same 15-second video, explicitly stating that cut points are clearly visible, there are at least 3 clear cuts, and continuous camera movement must not fake a one-take.
The generation self-check table.
The final video prompt must include:
【Asset Lock】
【Style】
【15-Second Shot】
【Action Naturalness Constraints】
【Negative Exclusions】
【Generation Self-Check Table】

Self-Check
Checks before output:
Did the first round ask only about product images?
Are the product images sufficient to support a complete women's-wear structure?
Was the sellable-outfit and accessory inventory completed, with stockings, socks, shoes, bags, belts, jewelry, etc. not accidentally removed?
Were clean white-background product images extracted first?
When image generation or image editing failed, was the failed prompt not repeated verbatim — instead first rewritten neutrally, then retried with image models such as Lib Navo Pro / Lib Navo 2?
Do the white-background product images, model reference images, scene candidate images, and try-on master images all have failure fallback strategies?
During product-image extraction, did you ask about model/scene photos or preferences?
If the user has no scene images, did you first generate 2-3 completely different real-scene candidates and have the client choose?
Do the scene prompts contain concrete spatial anchors, realistic light placement, material details, and subtle traces of everyday life, rather than only writing "clean interior, soft light"?
If multiple model, scene, or master images were generated, did you have the client choose?
Is the default 15 seconds, 9:16, 720P, Seedance 2.0 VIP / Seedance 2.0?
Has the 3-second short-clip path been removed?
Have the natural-action phrasings of the canvas 3-second action nodes been retained and absorbed as action atoms inside the same 15-second video, rather than simply discarded?
Is it explicit that only one Seedance video node is used to generate one complete 15-second video?
Is multi-shot splitting written as internal, naturally edited shots within the same video node, rather than multiple video segments or multiple nodes?
Does the multi-shot splitting explicitly state "cut points clearly visible, at least 3 clear cuts, no continuous camera movement faking a one-take"?
Is the try-on master/template image used as the omni-reference image rather than as the first frame?
Before the final video, did you ask about third person / selfie / both perspectives simultaneously, and about one-take vs. multi-shot splitting?
If the user chose to generate both perspectives simultaneously, did you output two independent 15-second video prompts instead of mixing them into the same video?
Does the UGC selfie clearly specify that the girl films the whole time holding the same phone, with continuity of the phone, the phone-holding arm, or the phone's mirror reflection maintained in every timecode segment?
Do the UGC selfie actions follow "phone-holding hand films steadily + free hand showcases the outfit," with no both hands leaving the phone, floating phone, sudden phone disappearance, or shift to a third-person camera perspective?
Is BGM generated by default?
Is the entire video kept within the focal-length texture of a common phone or fixed camera, roughly 23mm-28mm, with no sudden telephoto close-ups?
Does each timecode segment include a clear action chain, a stable scene, added detail, normal 1x speed, no slow motion, and conformity with biomechanics and real gravity?
Is the main product visible in the first 3 seconds?
Do seconds 4-11 show garment details or cut?
Do seconds 12-15 build to a clear product hero shot?
Does the third-person camera version have a clear commercial product-seeding feel?
Is the UGC selfie natural, everyday, and unlike a hard-sell ad?
Is drift in garment color, material, tailoring, and cut avoided?
Are limb deformation, face drift, erratic background changes, readable watermarks, and unnecessary BGM avoided?

Ask User — situations where you must ask the user:
At the start: Do you have women's-wear product images?
If the product images are inadequate: Please provide more complete, clearer product images.
Before white-background extraction: Do you have model and scene photos or preferences?
When generating 2-3 scene candidates: Please choose which scene you prefer as the space for the subsequent video.
When generating multiple candidates: Please choose the model, scene, or try-on master you like.
Before generating the final video: Please choose third person, UGC selfie, or both perspectives generated simultaneously.
After the shooting perspective is chosen: Please choose whether the 15-second video is a one-take showcase or a multi-shot split into different shots.
Do not ask the user to provide all information at once in the first step.