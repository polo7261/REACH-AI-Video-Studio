---
name: gameplay-pv-builder
description: "Gameplay demo builder: creates various game PVs with pixel-anchored, distortion-free UI for AAA-game effects"
---

name: game-promo-video\\

namespace: industrytitle: "Game Promo Demo Video"description: "Game promo demo video designer — includes two modes: ① Three-segment gameplay demo (Video A onboarding flow / Video B story flow / Video C combat flow, 15 seconds each, 45s in total), with the character concept art → four-view → 3D character card asset chain, UI pixel-anchored no-deformation zones, and consistent color LUT across the three segments; ② Open-world urban gameplay short film (character prototype library + scene templates, dual-path prototypes/user photos, fast-paced event 4-Cut formula and single-shot lifestyle slices, 5 types of exclusive camera angles, beat-synced editing rhythm). Uses generate_image_v3 + generate_video_v3 + composite_video."version: 3

game-promo-video

Use this skill when creating promo demos / gameplay demos / open-world gameplay short films for original or user-owned games. It includes two modes; choose one based on the user's needs:

Mode 1 · Three-Segment Gameplay Demo: Video A onboarding flow / Video B story flow / Video C combat flow, ~15s each, 45s in total, each segment's single-shot duration ≤15s. Full pipeline = background & style setting → three-segment script breakdown → element design (character concept art → four-view → 3D character card + UI/scene keyframes) → segment-by-segment video generation → full assembly of all segments.

Mode 2 · Open-World Urban Gameplay Short Film: draws on the visual grammar, shot organization, and character types of open-world crime/urban genres (borrowing only the visual grammar / urban vibe / shot organization / character types, without replicating any official shots, logos, UI, trademarks, license plates, or specific lines, and without naming any commercial game IP), producing a 30-60s mixed-experience short film: tropical vacation ad vibe + crime documentary texture + social media absurdity + open-world city showcase. Full pipeline = global setup → dual-path character assets → storyboard narrative (fast-paced events or single-shot lifestyle slices) → shot-by-shot video generation → audio layer → editing and compositing.

This skill ships with all the craftsmanship built in — combat dynamics / locked UI / pixel anchoring / gameplay-style shot language / beat-synced editing rhythm, etc. — and does not outsource to other skills.

Adaptation for this environment (source model names → 13 tools/SP): image2 image generation (image quality parameters confirmed via Ask user) → all via generate_image_v3 (the same image engine keeps the three segments consistent); four-view/3D character card can be paired with the character_turnaround_3view mode; Seedance 2.0 → generate_video_v3; three-segment stitching → composite_video (video layer + audio layer both enabled); Final_Video\_[Spec.md](http://Spec.md) / spec document → text_editor (write files); storyboard_designer → internal storyboard stage; multimodal_analyze_tool → multimodal image reading (3D material analysis / UI pixel anchoring / LUT extraction / user photo feature extraction); Image_A1…A5 node references → reference_nodes + {{NodeKey}} placeholders; pause/review → reply_to_user or cards; user photo ImageToImage to character → reference_nodes image-to-image path. Paid/membership semantics in the source must be stripped (including "Premium member 1080p").

Before generating images, you must Ask the user to confirm which image quality parameter of the image2 model to publish with this time, offering 4 options: 1, 2k standard quality (high value for money); 2, 2k high quality (moderate value for money); 3, 4k high quality (big spenders, feel free); 4, Other.

Before generating videos, you must Ask the user to confirm which video resolution parameter to publish with this time, offering 3 options: 1, 720p (high value for money); 2, 1080p (moderate value for money); 3, Other.

Mode 1 · Three-Segment Gameplay Demo

Pipeline and Pausing

Do not run everything in one pass. Stop after each key stage, confirm with the user, then move on to the next step (you can use cards or reply_to_user to invite review): after the spec is finalized → after the storyboard is completed → after the elements (character card + keyframes) are completed → after segment video generation → after audio/compositing.

1. Background and Style Setting

Receive the user's theme keywords, automatically set the story background, and establish the global game style (e.g., realistic / fantasy / cyber, etc.). Write Final_Video\_[Spec.md](http://Spec.md) (text_editor); fields: title, genre, aspect ratio, duration, visual style, language.

2. Three-Segment Script Breakdown (Core Skeleton)

Break the demo content into a three-segment (15s each) structured script, with a second-by-second timeline for each segment:

Video A (15s) Onboarding Flow — System Interaction and Awakening

0–3s: Cover image, simulate a breathing light effect, perform the \[Start\] button interaction.

3–10s: Character selection / skill showcase, simulate mouse-hover highlighting, display the character's 3D idle Pose or signature move.

10–15s: First-person POV, scene cut-in, transitioning from a specific viewpoint (awakening/transition) into the HDR effect of a vast environment.

Video B (15s) Story Flow — Narrative Interaction and Tracking

15–25s: NPC interaction, bring up the dialogue UI, text displays character by character, background keeps the ambient animation.

25–30s: Scene tracking, the camera follows the character moving rapidly to a specific visual landmark, creating a sense of encounter.

Video C (15s) Combat Flow — Core Combat and Settlement

30–40s: Live gameplay combat, fast-paced confrontation, UI health bars and skill slots change dynamically in real time.

40–45s: Combat settlement, Boss defeat move, pop up the victory UI and reward settlement effects.

3. Element Design (Asset Chain: Concept Art → Four-View → 3D Character Card + Keyframes)

Character Design (Core Logic)

Concept art: Produce master-level 2D design concept art of the characters (protagonist / Boss).

Character four-view: Based on the concept art, use ImageToImage to generate a white-background four-view sheet (2K recommended). Layout rules: on the left is a facial close-up (capturing facial details, skin texture, makeup); on the right, in order, are the full-body front view, full-body back view, and full-body side view (capturing body proportions and equipment layering). All views must strictly match the concept art's design, color scheme, and materials (can be paired with the character_turnaround_3view mode).

3D character card: Convert the four-view sheet into a 3D photorealistic character card.

UI/scene keyframes: Generate game UI screens and scene keyframes consistent across the entire pipeline, covering: start screen / character selection screen / loading screen / first-person opening view / third-person scene observation / entering the Boss fight. All images are forced through the same image engine to keep consistency.

Video A: Produce 5 related images (cover, character selection page, skill page, scene starting point, etc.).

Video B/C: Produce a dialogue UI image, a traversal scene image, combat first/last frames with HUD, and a settlement image.

4. Analysis Constraints (Multimodal Image Reading, for Video Generation)

3D asset analysis: Deeply analyze the materials of the 3D character card (metal reflections / skin texture / clothing textures), producing lighting description parameters.

UI pixel anchoring (core): Analyze the screenshot with HUD, record the exact pixel positions of the health bar, skill bar, and dialogue box, and mark them as "no-deformation zones for video generation".

Color and lighting consistency (LUT): Extract the global color tendency to ensure the three video segments stay highly consistent in tone and brightness from start to finish, preventing color drift.

5. Segment-by-Segment Video Generation (generate_video_v3)
Write in detail the presentation content of each scene, the UI feedback simulating highlight on mouse click, and high-intensity Boss battle actions. Four prompt instructions:

Interaction segment instruction (Video A): using Image_A1…A5 (reference_nodes+{{NodeKey}}) as nodes, simulate real keyboard-and-mouse interaction feedback (clicks, highlights, light effects), keeping the 3D models visually consistent across all interfaces.

Narrative dialogue instruction (Video B): the dialogue UI must be absolutely clear, with no trembling or blur; text display is synchronized with character states.

Action combat instruction (Video C): use the combat standoff image as the first frame and the victory results image as the final frame.

Core instruction (running through all segments): forcibly lock the UI; prohibit the health bar and skill icons from any displacement, artifacts, or deformation (aligned with the no-deformation zone in Step 4); action descriptions include high-frequency movement, particle effects, and screen-shaking impact feel.

6. Full-segment compositing and audio (composite_video)

Splice the three 15s videos logically into a complete in-game demo, with unified high-quality output (set resolution, frame rate, and motion-smoothness rendering standards). During compositing, synchronize and match the corresponding sound effects: UI sounds, ambient sounds, impact sounds. Both the video layer and the audio layer (background music) are enabled.

Gameplay Mode 2 · Open-World Urban gameplay Short Film

An independent gameplay oriented toward "open-world urban crime/street-themed in-game-feel short films": drawing only on the visual grammar, urban temperament, camera organization, and character types common to publicly available themes; not replicating any official shots, logos, UI, trademarks, license plates, or specific lines of dialogue; not naming any commercial game IP.

1. Global Settings Initialization

Create and lock Final_Video\_[Spec.md](http://Spec.md) (text_editor): the aspect ratio defaults to 16:9; the theme is positioned as "theme videos, storyboards, prompts, and visual review inspired by open-world crime/street themes". The visual style is not simply "neon crime" but a hybrid of "tropical vacation commercial + true-crime documentary + social-media absurdist short video + open-world city showcase": the surface of the frame is lively, sexy, sunny, and exaggerated; underneath, there is always the pressure of pursuit, debt, personal favors, smuggling, the music industry, gangs, and couples on the run. Duration defaults to a 30-60s short-form in-game gameplay demo unless the user explicitly requests a longer story.

2. Dual-Path Character Assets

When designing the storyboard outline, character creation offers two paths for the user to choose from:

Option 1 (Classic character archetypes): use the built-in character archetype library to create characters (see the archetype library below), and directly generate 3D-rendered reference images matching this style with an in-game 3D game feel (generate_image_v3).

Option 2 (User-customized character): the user uploads a personal photo (for creative reference only). Multimodal analysis extracts only gender and general appearance/temperament (e.g., gender, approximate age range, rough facial contours, or core expression/gaze), without describing or extracting specific details such as hairstyle, makeup, clothing, or accessories — during the image-generation stage, these details are adaptively distilled by the ImageToImage visual-reference path (reference_nodes image-to-image), with no need to rigidly specify them in prompts. Output minimal English feature words, for example: A Hispanic male in his 20s, with sharp facial features and determined eyes. Emphasize abstracting the user's real-world base appearance into the undertone of "a 3D game character of this style, third-person in-game gameplay, UE rendering", removing photo background and lighting interference. If the user additionally uploads a third-party video/GIF as a motion or color-tone reference, analyze its camera movement (third-person follow, low-angle vehicle chase, etc.) and color composition, and transcribe it for use in the storyboard and generation stages.

3. Character Archetype Library + Scene Template Library

When designing storyboard key_elements, the following high-frequency character and scene archetypes can be predefined, with flexible custom extension supported (all archetypes use generic naming, not project-specific):

Character Archetype Library

MALE_LEAD: The typical male lead (e.g., hot-blooded driver, street youth), sturdy, weary yet alert, skilled at split-second on-the-spot reactions.

FEMALE_LEAD: The typical female lead (e.g., calm decision-maker, capable strong woman), tough and decisive, finding a way out in adversity.

UNDERGROUND_BOSS: Underground industry magnate/power behind the scenes, often wearing sunglasses and luxurious attire, with an unfathomable gaze.

INFLUENCER_STREET: Social-media influencer/street loudmouth, chasing traffic and attention, often holding up a phone to livestream or loving parties.

MASTERMIND_PLANNER: A meticulous operations planner, experienced, seasoned, and elusive.

REGIONAL_SMUGGLER: Old-school island/border smuggler, gruff and untamed, representing the leftover criminal rules of a bygone era.

PARANOID_MONITOR: Paranoid eavesdropper, with a slack posture, skilled at gathering clues in dark rooms full of screens and radios.

CUSTOM_USER_HERO (Option 2 only): A custom protagonist derived from analysis of the user's photo, inheriting the user's core appearance and gaze features, with a strong sense of identity immersion.

Scene Template Library

METROPOLIS_NEON: Tropical neon metropolis, bustling beaches, elevated bridges, pink-purple streets, puddled road surfaces.

COASTAL_ISLANDS: Island smuggling belt, blue-green seawater, docks, white yachts, a long sea-crossing bridge at dusk.

WILD_SWAMP: Wetland wilderness, swamp reeds, helicopter searchlights, muddy mist.

DECAYED_HARBOR: Cheap port city, motels, Motel parking lot, old gas stations.

INDUSTRIAL_TOWN: Outlying industrial town, steel-frame factory buildings, chimneys, motorcycle convoys, billowing dust.

STORMY_MOUNTAIN: Mountain national park, dim forested mountain roads, rainstorms and lightning.

4. Narrative Structure (choose one of two)

The number of storyboard shots is controlled by default at 1-3 shots; unless the user explicitly requests a longer, more complex plot, prioritize streamlining the volume to ensure rendering efficiency and per-shot quality.

Structure A: Fast-paced event narrative (multi-cut combination, suited to trailers or action scenes) — after confirming the core plot with the user, unfold in three parts:

Opening segment · atmosphere building: mostly use wide-angle overhead views and slow skyline pans, with sound blending ambient noise, distant sirens, or radio, showing "undercurrents surging beneath a calm surface".

Middle segment · conflict spiraling out of control: close-ups of action details, character arguments, chase collisions, interspersed with social-media handheld/livestream perspectives. Rhythm shifts from gentle to high-frequency, with frequent multi-camera cuts.

Closing segment · suspense hanging: close-ups of eyes, car doors closing, rearview mirrors, etc.; music abruptly stops, leaving only engine sounds, breathing, or monotonous sound effects, leaving dramatic suspense.

Structure B: Single-shot life/gameplay slice (one continuous take, 5-12s): emphasizes high readability and a single continuous action (e.g., refueling a car, standing at a puddled intersection looking at palm trees, walking in front of a cinema, a slow-speed vehicle collision capturing the physical moment of metal crumpling, the "leaked-footage feel" of filming a game screen with a phone). Strict rules apply: within a single shot, no time/space switches or montage splicing; maintain an extremely smooth game-like third-person follow camera with delay.

5. Five Proprietary Perspectives

Camera language categories, selected as the narrative requires:

Gameplay-like third-person perspective: camera positioned low and to the side, behind the character, retaining third-person spatial awareness, with slight delay, and the game UI hidden.

In-car/beside-car hybrid perspective: camera at the passenger's shoulder, rearview mirror, or an extremely low position at the rear bumper, with the car body in the foreground and neon light streaking across the wet body and glass at high speed.

Social-media vertical perspective: simulating phone selfies and handheld livestreams, with occasional shaking, brief defocusing, and edge distortion; the aspect ratio can switch to 9:16 for insertion.

Surveillance/police bodycam perspective: CCTV fixed wide-angle with compression and noise; bodycam with strong shaking and close-range fisheye distortion.

Intimate fugue duo perspective: compositions framed through car windows, Motel doorframes, or blinds, creating "tenderness and wariness under the pressure of crime".

Audio layer: globally configure a theme music track (BGM: synthwave, modern rap, southern radio rock); for dialogue, use key_element_audio to maintain the protagonist's gruff/hoarse voice or Latin inflection.
6. Single-Shot Design Rules + Multi-Cut Rules (4-Cut Formula)

Single-shot one-take (slice-of-life / single action) design rules:

Core design intent: suited for stable 5-12 second short shots; the core is "one thing from start to finish"—the action must never be complex, and the shot must never cut erratically, thereby establishing the sense of real life and gameplay texture of an open world.

Action design constraints: keep only 1 primary action (e.g., fueling a car, handing over a hot dog, grabbing a beer, opening a car door, scanning a QR code to pay, wiping the windshield, lighting a cigarette, stuffing cash into a pocket). It is forbidden to design multiple parallel or sequential compound intense actions within a single shot (e.g., do not have a character make a phone call, draw a gun, and run while fueling).

Camera movement constraints: keep only 1 type of movement (e.g., slow push-in, lateral tracking, gameplay-style fixed or floating perspective, slight handheld shake inside a car).

Audio coordination design: the audio track must provide highly immersive ambient sound anchors, such as traffic noise, distant sirens, club bass, convenience store door chimes, and the clicking of a fuel nozzle.

Multi-cut event (chase/conflict/robbery/chaos events) design rules:

Core design intent: it is recommended to uniformly design each multi-cut event as a single 15s shot, maximizing the video generation model's best performance in a single 15-second generation at producing rich internal cuts, smooth scene transitions, and full information density.

Storyboard structure formula (classic 4-Cut flow):

Shot 1 (Environment & Threat): establish the scene, the location environment, and the sudden threat/opponent being faced.

Shot 2 (Action Detail Close-up): show close-ups of high-dynamic action details (e.g., slamming the gas pedal, shifting gears, shoving, racking a gun bolt).

Shot 3 (Reaction & Obstruction): present different camera-position shots of the character's obstructed reaction, panicking passersby, physical collisions, or flashing police lights.

Shot 4 (Suspense/Finale Impact): show the escape, the moment of impact, or a highly tension-filled freeze frame, leaving a suspense hook.

Spatial continuity constraints: high-dynamic shots must maintain consistency in space, time, and lighting. Characters and vehicles must be in the same block or space, moving in a consistent direction, avoiding jarring frame jumps and continuity errors.

Cut and audio coordination: each short shot carries only 1 clear piece of information. Shots should be intercut between wide shots, in-car shots, low-angle shots, close-ups, and social-media footage, and precise sound-effect alignment points must be reserved in the audio track for every collision, roar, and shattering sound (e.g., engine roar, glass shattering, police radio, tire screech).

7. Per-Shot Video Generation Binding Rules (generate_video_v3)

For character 3D renders, prefer generate_image_v3; in Option 2, the user's photo is input via the image-to-image path to generate a bespoke 3D-rendered full-body shot and facial profile of the custom protagonist.

Shot videos are uniformly generated at a 15s duration (multi-cut events) to bring out the finest multi-shot internal cutting and natural transition rendering effects; resolution defaults to 720p (the source's "premium members prefer 1080p" semantics has been stripped out and is not implemented).

Reference binding rules:

Visual references: must bind the asset_id of any character appearing in the shot (custom protagonist or classic archetype); must bind the asset_id of the current scene.

Continuity references: for high-intensity multi-cut chase/crash scenes, when generating Shot N, the video of Shot N-1 must be bound as a reference to ensure smooth transitions in vehicle color, damage extent, and lighting.

Sound binding: if a shot contains a character speaking to the camera, that character's exclusive voice asset must be bound in the audio information to achieve audio-visual sync.

8. Prompt Construction (write_the_prompt)

General construction principles: absolutely forbidden to include specific commercial game names, copyrighted marks, or brand logos; adopt the perspective of a "director and colorist", favoring action descriptions and concrete material words, without emotional speculation.

Four-palette mnemonic:

Urban neon night: pink and purple neon, wet black asphalt reflections, cyan highlights, dynamic sodium lights

Tropical coast dusk: golden hour glow, teal sea, distant silhouette of palms, hazy sunset sky

Morning-fog wetland swamp: olive green muddy water, dense morning fog, silver gray, intense helicopter searchlight beam cutting through haze

Daylight: harsh tropical sunlight, overexposed edges, deep dark hard shadows, heat shimmer

Character 3D render prompt structure: uniformly adopt a high-definition realistic 3D game-texture style featuring this style, 3D game, third-person game, UE rendering, to generate a "character 3D in-engine render sheet" of full body + side close-up (horizontal side-by-side layout):

A 3D game character render of \[character name\], a \[gender\] with \[hair/face features\], wearing \[outfit\], open-world game style, 3D game model, third-person game gameplay character, Unreal Engine 5 render, high fidelity, realistic game engine shaders, wet skin texture, high contrast tropical lighting.

Video prompt structure: uniformly formatted as camera position + visual reference placeholder + action/motion stack + ambient acoustic markers.

Format example: \[Camera: third-person trailing angle with slight delay\] &lt;&lt;&lt;image_1&gt;&gt;&gt; \[Character: young male protagonist\] is fueling his dusty muscle car at a neon-lit gas station, simple action of holding the gas nozzle. \[Background: wet asphalt, pink and cyan glowing neon signs, swaying palm trees, humid metropolis night atmosphere\]. \[Audio: (ambient club bass), &lt;distant police siren&gt;\]

Motion stack design: start the description with camera movement (Camera), followed by the subject character/vehicle action (Action), then spatial environment changes (Environment), and finally wrap sound effects or dialogue details in parentheses. In-video dialogue is wrapped in {dialogue} (e.g., {We are in this together, okay?}); music/atmosphere sounds use (music) / (ambient club bass); action sound effects use &lt;tire screech&gt; / &lt;siren&gt;; the end of the video prompt defaults to the negative filter words no music, no subtitles, no logo, no branding, photorealistic game trailer concept, with background music left to the audio track for unified synthesis to prevent audio overlap.
9. Recipe library (single-shot / multi-cut templates + high-frequency shot recipes)

Single-shot one-continuous-take recipe

Structure formula: one continuous shot, single simple action, \[character\] does \[action\] at \[location\], camera \[single camera move\], background shows \[representative environmental elements\], humid realistic tropical metropolis atmosphere, no cuts, no montage, no logo

Prompt template: One continuous cinematic shot in an open-world inspired metropolis. A \[character type\] performs one simple action: \[action\]. Location: \[place\]. Camera: \[slow push-in / side tracking / fixed CCTV-like frame / handheld phone follow\]. Background: palm trees, humid neon, wet asphalt, traffic, random NPCs, distant police siren. Keep the action simple and readable, no cuts, no montage, no official logos, no readable real brands.

Application examples (method-level examples; copy them and just swap words as needed):

Refueling: One continuous cinematic shot in a neon-lit metropolis gas station at night. A young male protagonist refuels a dusty muscle car, one simple action from grabbing the nozzle to putting it into the tank. Camera slowly tracks sideways from the rear wheel to his face, wet asphalt reflecting pink and cyan lights, palm trees and traffic in the background, distant police siren, humid air, no cuts, no montage, no logos.

Selling hot dogs: One continuous street-life shot in sunlit coastal city. A hot dog vendor hands a wrapped hot dog to a tourist while scooters and beachgoers pass behind them. Camera is fixed at chest height with slight handheld sway, bright tropical sun, palm shadows, ocean breeze, colorful NPC crowd, simple readable action, no cuts, no montage, no official logos.

Third-person wet-road walking: One continuous game-inspired third-person gameplay shot. A young man in a sleeveless shirt stands on a wet boulevard after rain, then slowly starts walking forward. Camera follows from behind at shoulder height with slight floating game-camera movement. The road is covered with puddles reflecting high-rise hotels, palm trees, neon signs, traffic lights and passing cars. Keep one simple movement, no cuts, no montage, optional minimal HUD feeling, no official logos.

Night-street entertainment district exploration: One continuous third-person exploration shot in a humid entertainment district at night. A playable character walks toward a bright movie theater entrance, passing food stalls, NPC crowds, LED billboards and glossy wet pavement. Camera stays behind the character with a slow forward follow, like open-world gameplay with cinematic lighting. No cuts, no combat, no logos, no readable real brands.

Multi-cut event recipe

Structure formula: multi-shot sequence, 4 fast cuts, same event continuity: Shot 1 establish location and threat, Shot 2 close-up action detail, Shot 3 reaction / obstacle, Shot 4 escape / impact / hook. Keep same characters, same location, same time of day, no official logos.
Prompt template: Create a crime-action inspired multi-shot sequence with 4 quick cuts, same characters and same location continuity. Shot 1: \[wide establishing shot, location, threat\]. Shot 2: \[close-up action detail\]. Shot 3: \[reaction or obstacle, different camera angle\]. Shot 4: \[escape / impact / cliffhanger\]. Style: humid metropolitan realism, handheld urgency, low vehicle angles, wet reflections, social media chaos in background. No official logos, no real brands, no gore.

Application examples (method-level examples):

Chase: Create a high-speed multi-shot chase sequence with 5 quick cuts, same car and same street continuity. Shot 1: wide night street outside a neon motel, a muscle car suddenly reverses as police lights appear. Shot 2: close-up on tense driver slamming the gear shift, dashboard shaking. Shot 3: low rear bumper camera as the car fishtails across wet asphalt, pink neon reflections stretching behind it. Shot 4: vertical phone video from a bystander as the car blasts past a hot dog stand and people jump back. Shot 5: car interior rear-view mirror showing police headlights closing in. Style: humid metropolitan night, handheld urgency, fast cuts, tire smoke, sirens, no logos, no gore.

Fight: Create an action-heavy multi-shot motel fight sequence with 4 quick cuts, same parking lot continuity. Shot 1: wide shot of a cheap neon motel parking lot, two men arguing beside a pickup truck. Shot 2: handheld close-up as a sharp female protagonist grabs one attacker by the shirt. Shot 3: low angle as the attacker hits the car door and beer cans scatter on wet pavement. Shot 4: male partner opens the passenger door and shouts for her to get in as police sirens rise. Style: gritty coastal harbor night, sodium lights, wet asphalt, fast handheld cuts, no gore, no logos.

Vehicle collision physics: Create a high-fidelity vehicle collision sequence with 4 quick cuts, same highway continuity. Shot 1: side-rear camera of a sports car scraping against a police cruiser on a sunlit highway. Shot 2: close-up of crumpling metal, shattered headlight glass and tire smoke as the vehicles grind together. Shot 3: overhead tracking shot as both cars drift across lanes, the police car pushing into the sports car's rear quarter. Shot 4: low bumper camera as the sports car breaks free and accelerates, leaving debris and skid marks behind. Style: realistic in-game vehicle physics, hard sunlight, road vibration, metal deformation, fast but readable cuts, no logos.

8 high-frequency shot recipes (for direct reference or invocation):

City opening: Metropolis-inspired coastal city at dusk, palm trees, high-rise hotels, neon signs turning on, wet asphalt, traffic and pedestrians, humid air, distant police siren, slow aerial push-in to street level, saturated but realistic, no logo, no real brands.

Two-person getaway: two fugitives in a motel parking lot at night, young tense couple, muscle car idling, pink neon reflected on wet pavement, cash bag and old phone, handheld camera, intimate criminal tension, police lights far away, cinematic game trailer realism.
Nightclub/social media spectacle: Coastal city nightclub exterior, crowd livestreaming with phones, luxury cars, pink and cyan neon, police cruiser nearby, people laughing and arguing, social media chaos, stabilized tracking shot through the crowd, humid night reflections, no logo.

Wetland manhunt: Tropical swamp at dawn, fog over muddy water, reeds in foreground, airboat cutting through, helicopter searchlight far away, two fugitives hiding near abandoned boat, handheld low camera, tense quiet, olive green and gold sunrise palette.

Port deal: night port deal between shipping containers, sodium orange lights, wet concrete, trucks and cranes, duffel bag exchange goes wrong, fast lateral tracking shot, sparks and police radio fragments, gritty realistic crime trailer.

Gameplay-like driving scene: Open-world inspired third-person gameplay-like driving shot, UI hidden, camera mounted low behind the side of a muscle car, driving through a humid coastal metropolis at night, wet asphalt reflecting pink neon and police lights, camera follows with slight delay and realistic shake, not a clean car commercial, cinematic in-game footage feel, no logos.

Phone onlooker: vertical phone livestream from a random bystander in a neon city, crowd filming a police chase outside a nightclub, shaky imperfect framing, people blocking the lens, pink and cyan neon, wet street reflections, comments implied but no readable UI text, chaotic social media realism, no official logos.

CCTV absurd incident: fixed CCTV camera inside a small convenience store, humid night outside, an absurd incident suddenly enters frame, compressed surveillance texture, wide-angle corner view, fluorescent lights, reflections on glass doors, grounded dark comedy, no gore, no logos.

10. Three-stage pacing of the edited composite (composite_video)

Fast-paced event narrative (multi-cut combination): opening stage single-shot duration 4-5 seconds, footage fades in and out, gentle cuts; mid-section the web of relationships spirals out of control, dense edit points (a cut every 0.8-1.5 seconds), using hard cuts with no transitions and white flashes to simulate a racing heartbeat; ending escape suspense, shots stretched to 6-8 seconds, fade out to black.

Gameplay-like life slice: one continuous take, full length 5-12 seconds with no edit points at all.

Precise audio-video alignment: Track 1 (ambient sound effects/SFX) — gunshots, collision sounds, and engine roars strictly frame-aligned with the on-screen action, with volume momentarily boosted by 6dB at the instant of physical vehicle collisions plus an added bass rumble effect; Track 2 (dialogue voice/Narration) — BGM automatically ducked by 12dB 0.3 seconds before dialogue begins, smoothly rising back 0.5 seconds after dialogue ends; Track 3 (background music/BGM) — in the final 10 seconds of the video (the suspense section), the BGM is abruptly cut out or low-pass filtered, leaving only heavy breathing and the lingering hum of a monotonous siren, heightening the end-of-the-road tension.

Output specs: the export stage must strictly follow the parameters in Final_Video\_[Spec.md](http://Spec.md); black bars or stretched frames are not allowed.

Boundaries (do not use this skill, reroute)

2D animation-style promos → cartoon-flow.

Replication of specific commercial game IPs (official footage / Logo / UI / trademarks / license plates / dialogue) → refuse; this skill only covers original works or the user's own games.