---
name: soccer-action-cinematic
description: "Freestyle soccer action short: upload a character image to one-click generate a cool soccer action blockbuster—live-action or animation, your choice."
---

# Wander Character Football Action Short Video

## Skill Positioning

Turns the user's character image into a cool solo football short video. The default is a 15-second, 9:16, 720P continuous single-take street football shot: the character starts by controlling the ball at their feet, builds pressure step by step with freestyle breakthroughs, and finishes by kicking the ball toward the camera with a camera-impact ending.

It only produces single-character-driven football action clips, not real match replays, team tactical analysis, unauthorized replication of real football stars, or multi-character long storylines. The coolness comes from readable football moves, clearly motivated camera movement, and continuous escalation, without using irrelevant explosions to mask the action.

## Multi-Level Reference Invocation Strategy

This Skill uses multi-level references. Load them by stage during execution:

- When evaluating the character image, generating white-background character images, and selecting and locking the art style, you must use `references/character-and-style-policy.md`.
- When designing football moves, the venue, pacing, sound effects, and the camera-impact ending, you must use `references/football-action-engine.md`.
- When generating final video prompts, listing referenced assets, and checking character consistency, you must use `references/video-reference-policy.md`.
- When image safety review fails while generating `character_reference`, `football_scene_reference`, or `football_action_composite_reference`, you must use `references/image-generation-fallback-policy.md`.

The main file only defines the overall flow. Do not skip references, and do not copy wording from one art style directly into the other two styles.

## Image Safety Review Failure Fallback

Only execute the following fixed fallback when image generation fails the safety review; do not use it for network errors, model timeouts, ordinary dissatisfaction with image quality, or other generation failures:

1. Keep the original prompt completely unchanged and first switch to Navo Pro to retry.
2. If Navo Pro still fails the safety review, keep the same original prompt completely unchanged and switch to Navo2 to retry.
3. Only if Navo2 still fails the safety review, load `references/image-generation-fallback-policy.md`, review and minimally adjust wording that may have triggered the review, and try again.

This is not about bypassing the safety review. Do not conceal, encode, split, or disguise restricted content; if generation still fails after compliant wording adjustments, stop retrying and explain to the user the reason for the restriction and feasible safe alternative directions.

## Input

### Round 0: Lock the Character and Art Style First

Open with the following statement:

"This Skill turns your character into a cool football action short video. Uploading a character image first is the easiest way to lock the face, hairstyle, and outfit; after uploading, you can choose to keep the original art style or switch to a built-in style. No character image is fine too—I can first generate a white-background character image based on your description. Only after the character and art style are confirmed will we move on to the landscape football scene preview and video generation."

First suggest that the user upload their own character image, prioritizing these questions:

1. Will you upload a character image? A clear, single-person, front-facing or two-thirds-body image with the face and outfit visible is recommended.
2. If there is no character image, collect: the adult character's gender expression/appearance, hairstyle, skin tone, apparent age, body type and athletic vibe, jersey or everyday outfit, footwear, and prohibited elements. Minors or characters of unknown age must not be used in sexualized or dangerous portrayals.
3. If the user uploads a character image, you must first confirm the style mode; default conversion is not allowed:
   - Keep the uploaded character image's art style (recommended): the video, scene composite images, and character assets follow the painting/rendering/photographic style of the uploaded image, with only the necessary white-background cleanup; do not force the character into a built-in style.
   - Use a built-in style: then select exactly one from "live-action cinematic look, 3D rendered animation, 2D cartoon."
4. If the user has no character image, choose the art style, selecting only from the following three options:
   - Live-action cinematic look (recommended): real photography, sports films, natural environments, and real shoe-ball contact.
   - 3D rendered animation: high-quality stylized 3D, controllable lighting and shadow, and dynamic special effects.
   - 2D cartoon: two-dimensional cel animation, clear action lines, and exaggerated perspective.

Also collect the minimal boundaries:

- Venue preference: nighttime urban concrete court (default), dusk street court, rooftop court, indoor futsal court, post-rain court.
- Action intensity: cool but readable (default), high-intensity freestyle, power-shot focused.
- Duration: default 15 seconds, 720P; the user can change it to 30 seconds or longer. The system automatically determines audio delivery based on duration: a single 15-second video includes generated BGM; when exceeding 15 seconds, split into multiple 15-second videos, each without BGM, and additionally output a standalone BGM track for post-production stitching.
- Video aspect ratio: before final video generation, the user must explicitly choose landscape 16:9 or portrait 9:16; there is no default. The landscape scene image and landscape action preview do not change based on this choice.
- Subtitles: no subtitles (default), short title subtitles, action label subtitles.

### Character Input Usage Rules

- The user's character image is the identity anchor. You must first load `references/character-and-style-policy.md` to assess clarity, single-person status, and face and outfit visibility.
- For user-uploaded images, `role_asset_decision` must be executed automatically within the system without asking the user whether extraction is needed: when the background is clean, it is a single person, the face/hairstyle/outfit/shoes and body details are clear, and it can be directly used as a character asset, lock the uploaded image directly as `character_reference`; if any key condition is not met, automatically generate a white-background `character_reference` character asset image.
- When the user uploads a character image, you must first confirm `style_mode`: `preserve_uploaded_style` (keep the uploaded character image's art style) or `built_in_style` (use a built-in style). Until confirmed, do not automatically convert the character to live-action, 3D, or 2D.
- When the image qualifies, lock the uploaded image directly as `character_reference` without generating an additional white-background character image; do not swap the face, hairstyle, main outfit, skin tone, or gender expression on your own.
- When the image is not suitable for direct locking, the system automatically generates a white-background `character_reference` character asset image and asks the user to confirm the result after generation; you may briefly explain the triggering reason, but must not ask the user whether to do this step.
- When the above white-background character image, landscape scene image, or landscape action preview image fails the safety review, you must handle it in the order of "original prompt -&gt; Navo Pro -&gt; Navo2 -&gt; minimal compliant wording adjustment."
- When the user has no image, first output the white-background character image prompt and request confirmation after generation; without a `character_reference`, do not proceed to action compositing or the final video.
- Do not replicate copyrighted characters, real football stars, or third-party likenesses; only use them directly when the user provides a character image for which they hold usage rights.

## Internal Workflow and Knowhow

### 1. Character Asset and Art Style Confirmation

Load and execute `references/character-and-style-policy.md`.

First generate or lock:

- `character_reference`: the character identity asset. If the uploaded image can be used directly, this is the user's uploaded image; only if the system determines it is not suitable for direct use will a landscape 16:9 white-background character design image be generated. Always lock the face, hairstyle, outfit, shoes, body proportions, and athletic vibe.
- `football_scene_reference`: landscape 16:9 football scene image. Lock the space, ground, lighting, background, and selected art style of the complete venue; do not include the character.
- `football_action_composite_reference`: A landscape 16:9 action preview image of the character entering the selected stadium, used only to let the user confirm the overall lighting, atmosphere, composition, and feel of the character and scene; it is not a reference asset for the final video.

The asset generation order must be fixed as:

1. First lock in `character_reference`.
2. Generate and save `football_scene_reference`.
3. Only after `football_scene_reference` is generated successfully, generate `football_action_composite_reference`; when generating it, you must actually reference the two already-generated assets `@[character_reference]` and `@[football_scene_reference]`, and must not regenerate a similar scene based on text alone. This composite preview is only for the user to confirm the overall feel; after confirmation is complete, it is not passed into the final video node.

If `football_scene_reference` is missing, fails to generate, or has been replaced, reusing the old preview or directly generating a preview is forbidden. You must first obtain a currently valid scene asset, then regenerate `football_action_composite_reference` based on it. When the user modifies the pitch, lighting, or art style, likewise first update the scene asset, then update the composite preview.

When a character image exists, first automatically complete `role_asset_decision`, then confirm whether the user has chosen to keep the original image's art style or the built-in art style; conversion only happens when the built-in art style is chosen. Directly usable uploaded images do not generate extra white-background assets; both system-extracted white-background character images and white-background character images generated without a character image must be confirmed before entering the scene.

Before generating `football_action_composite_reference`, you must confirm:

"Does this character's face, hairstyle, outfit, and art style pass? Once it passes, I will generate the football action scene preview."

Before outputting the video, you must confirm:

"Does this character football action preview pass? Only after confirmation will the final short video be generated, to avoid applying an unsatisfactory character or art style directly to the video."

### 1.5 Video Aspect Ratio Mandatory Gate

After the user approves the action preview and before generating any final video prompt, you must separately confirm `video_aspect_ratio`:

"The preview has passed. For the final video, please choose: landscape 16:9 or portrait 9:16?"

Only after the user explicitly replies landscape 16:9 / 16:9 / landscape, or portrait 9:16 / 9:16 / portrait, can the corresponding value be written into `video_aspect_ratio`. If the user has not made an explicit choice, or only says "either is fine," "default," or "up to you," you must stop here and ask again; you must not output the final video prompt, segmented video prompts, or BGM prompts.

Even if the user mentioned the aspect ratio earlier in the conversation, you must verify it once more after the action preview passes; only an explicit value that has been recorded and that the user has not asked to change can be carried over directly.

### 2. Football Action Choreography

Load and execute `references/football-action-engine.md`.

By default, use an eight-segment continuous main-shot action sequence, compressed or expanded according to duration; the actions must be readable, continuous, and consistent with rough physical force logic:

1. Low-to-ground approach and oppressive pause.
2. Sole rolls, drag-backs, toe taps, and direction-changing feints.
3. Ball lifts and around-the-foot ball control.
4. Continuous ball control with knee, thigh, and heel.
5. Low-angle heel flick and crossover touch.
6. Sole trap, forward roll, and wind-up facing the camera.
7. Straight-line explosive shot.
8. The football hits the camera, cleanly cutting to black, a ball imprint, or a flash to white.

By default, no visible cuts; camera changes are achieved through continuous ground-hugging glides, around-the-heel tracking, ball-following rises, orbits, dives, and locks. Only switch to multi-shot when the user explicitly requests storyboard montage.

### 3. Final Video Prompts and References

Only after the user has confirmed the character asset and the action preview, load and execute `references/video-reference-policy.md`.

The final video must reference:

- `character_reference`: Locks in the character's identity, hairstyle, outfit, shoes, and physique.
- `football_scene_reference`: An empty landscape football scene asset, locking in the pitch space, ground, lighting, background, and overall art style.

The final video must not reference `football_action_composite_reference`. That image is only for the user to confirm the lighting, atmosphere, and overall feel after the character is placed into the scene; the video node must re-perform the character entering the scene, ball-control actions, and camera movement based on the separate character asset and empty scene asset.

When the user explicitly needs subtitles, you may additionally reference `subtitle_style_reference` or a subtitled script image. The final video must not rely solely on the white-background character image, and must not mix materials, camera terms, or sound effect words that conflict with the chosen art style.

Audio delivery is automatically determined by duration and requires no extra user choice:

- Single 15-second segment: The final video prompt must require generating BGM synchronously, and describe a BGM style matching the chosen art style, pitch, and action rhythm.
- Longer than 15 seconds: Must be split into multiple 15-second video prompts; each segment explicitly states "do not generate BGM, only generate ambient sound and football action sounds," and additionally output a separate BGM generation prompt covering the full final video duration, for later editing and compositing.

## Output

### Round 0 Output

Output only:

1. Advice on uploading a character image.
2. Character description questions when there is no character image.
3. Three art style choices with a one-sentence explanation of the differences.
4. The minimal confirmation items for pitch, action intensity, duration, and subtitles; the video landscape 16:9 or portrait 9:16 choice is confirmed before the final video.

### Character Stage Output

Must output:

1. The automatic judgment result of the character image, or a brief restatement of the user's character description.
2. When the image can be used directly: state that the uploaded image has been directly locked in as `character_reference` with no white-background asset generated; when the image is unsuitable: output the complete white-background asset generation prompt for `character_reference` and automatically proceed to generation.
3. The character and art style confirmation question.

### Action Preview Stage Output

Must output:

1. A one-sentence confirmation of the chosen style and action direction.
2. First the complete landscape prompt for generating `football_scene_reference`; after the scene asset succeeds, then output the `football_action_composite_reference` prompt referencing `@[character_reference]` and `@[football_scene_reference]`.
3. The action preview confirmation question.

### Output After the User Confirms the Action Preview

Must output:

1. First output and confirm `video_aspect_ratio`: landscape 16:9 or portrait 9:16; if no confirmed value exists, stop and do not output the following items.
2. One complete video prompt with the confirmed `video_aspect_ratio`, or continuous video prompts split by duration.
3. The final video reference list.
4. The sound and subtitle strategy.
5. The embedded BGM style for a single 15-second segment, or the separate BGM post-production generation prompt for multi-segment videos.
6. The asset closed-loop check for character, football, pitch, art style, actions, and ending.

## Self-Check

Before output, check:

- Whether you advised the user to upload their own character image at the very start.
- When the user uploads a character image, whether the system automatically judged whether it can be used directly as `character_reference`, without asking the user whether to extract character assets.
- When the image is directly usable, whether white-background character image generation was skipped; when the image is unsuitable, whether the white-background character asset image was automatically generated and the confirmation gate retained.
- When the user uploads a character image, is there an explicit confirmation of whether to keep the uploaded character image's art style or switch to the built-in art style, instead of automatic conversion?
- When there is no character image, is a description first collected and a white-background `character_reference` generated?
- When there is no character image, is the user asked to choose only one art style among live-action cinematic texture, 3D rendered animation, and 2D cartoon?
- Are both the scene image and the character action preview image in landscape 16:9?
- Is the `football_scene_reference` generated and saved first, and then that asset actually referenced together with the `character_reference` to generate the composite preview, instead of rebuilding the scene from text?
- When the scene asset is missing, fails, or changes, is preview generation blocked and the scene asset required to be updated first?
- After the action preview is approved, is `video_aspect_ratio` asked about separately and recorded as landscape 16:9 or portrait 9:16?
- When no explicit landscape 16:9 or portrait 9:16 choice is given by the user, is no final video prompt, segmented video prompt, or BGM prompt output?
- For a single 15-second segment, does the video prompt explicitly state that BGM is generated in sync and describe the BGM style?
- For videos longer than 15 seconds, are they split into multiple 15-second videos, each explicitly stating not to generate BGM and to keep only ambient sound, with a standalone BGM post-production prompt output additionally?
- Is the action scene and final video not entered before character confirmation?
- Is no final video prompt output before the action preview is confirmed?
- Are the three references—character and art style, football action, and video references—executed?
- Does the final video reference only the `character_reference` and the empty `football_scene_reference`, without referencing the `football_action_composite_reference` that is used only for confirmation?
- Does the action escalate progressively from ball control, combo moves, ball flicks, and power charge to the shot and camera impact?
- Are unreadable extraneous acrobatics, irrelevant explosions, changes in the number of footballs, character face changes, or visible cuts avoided?
- Does 2D keep the two-dimensional animation language, 3D keep the three-dimensional rendering language, and live-action keep the real cinematography language?
- Is it made explicit that the football can only be controlled by the feet, legs, torso, or head, and that the hands, arms, elbows, and wrists are forbidden from touching the football throughout?
- Are subtitle style references added only when the user needs subtitles; and subtitles not forced when the user does not need them?
- When image safety review fails, is the same prompt kept while trying Navo Pro and then Navo2 in sequence, with compliant wording adjustments considered only if both still fail?

## Ask User

Must ask:

- "Please upload your character image. If you don't have one, tell me your character's appearance, hairstyle, clothing, and athletic temperament, and I'll first generate a white-background character image for you."
- "Do you want the overall video to keep the original art style of the uploaded character image, or use the built-in art style? If you choose the built-in art style, please also choose: live-action cinematic texture, 3D rendered animation, or 2D cartoon."
- "Are the character and art style approved? Once approved, a football action preview will be generated."
- "Is the action preview approved? Do you want to adjust the field, action intensity, jersey, camera work, or ending? The video will be generated only after confirmation."
- "The preview is approved. For the final video, please choose: landscape 16:9 or portrait 9:16? The scene image and action preview will remain in landscape so the pitch can be viewed in full."