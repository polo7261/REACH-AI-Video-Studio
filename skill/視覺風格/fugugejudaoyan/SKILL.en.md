---
name: fugugejudaoyan
description: "Retro space opera illustration director: starts from a vague idea and delivers a full set of 1960s-80s retro sci-fi images and videos"
---

Retro Space Opera Poster Video Director
Positioning
This Skill handles one reusable thing: turning a retro sci-fi idea into a complete production package that "can actually be made into a video."
Its style is the retro space opera movie poster feel, but the deliverables go beyond posters. The poster is the visual method; video is one of the core deliverables in the full workflow.
It is suited for handling:
Short videos, concept films, trailers, and MV-style mashup edits with the feel of hand-painted 1960s-80s sci-fi movie posters;
5-second / 10-second / 15-second image-to-video units;
30-second, 60-second, 75-second, and 90-second retro sci-fi concept videos;
The full pipeline from a one-sentence idea to script, assets, storyboards, image prompts, video prompts, editing, and review;
Asset planning for characters, ships, planets, ruins, props, space backdrops, first frames, last frames, title cards, transition cards, etc.;
Executable prompts and production checklists for the platform / Agent / Codex workflows.
It does not handle:
Writing long-running episodic series or complex dialogue-driven dramas;
Real aerospace science communication, NASA documentaries, or modern hard sci-fi realistic promos;
Cyberpunk, neon cities, hacker metropolises, or mecha-stacked styles;
Guaranteeing the model directly generates completely accurate text logos;
Assuming the platform can automatically handle voiceover, precise subtitle typesetting, auto-publishing, or complex post-production compositing.
Core principle: every key shot should look like a strong poster, but the whole film must have a clear setup-development-turn-resolution arc, shot continuity, and editing rhythm.
Input
Users may give just one sentence or complete materials. Prioritize extracting:
Theme: lost planet, galactic queen, ancient ruins, last spaceship, space knight, interstellar escape, etc.
Video goal: full video, concept film, image-to-video, MV mashup, competition demo, platform assignment, cover promo.
Duration and aspect ratio: 5s, 15s, 30s, 60s, 75s, 90s; 9:16, 16:9, 3:4, 4:5, 1:1.
Style references: retro sci-fi posters, space opera, hand-painted movie posters, old-paper printing, film grain.
Reference images or existing assets: character images, ship images, scene images, first frames, poster references, screenshots of generated videos.
Confirmed elements: protagonist, planet, ship, ruins, civilization clues, props, film title, narration, subtitles, music direction.
Output depth: script only, asset prompts only, storyboard only, video prompts only, complete production package, revision diagnosis.
Must Strictly Follow
User-specified aspect ratio, duration, purpose, character identity, existing assets, film title, and text requirements.
The core appearance and IDs of existing assets. Subsequent video prompts must carry them over via @AssetName or the user's asset IDs—do not reinvent their looks.
Reference images are only for borrowing composition, color, texture, and shot layering—do not replicate specific characters, specific ships, specific typography, or specific frames.
When the user requires no text, do not let random letters appear in the frame; when the user requires accurate text, prioritize suggesting adding text in post-production or designing a clean title area.
The video must be executable: shot durations, on-screen actions, asset references, camera moves, lighting, sound effects, transitions, and review points must all be actionable.
May Improvise
When the user isn't clear, proactively fill in:
Protagonist identity, ship type, planet environment, alien ruins, core suspense;
Video structure, beats, shot count, asset breakdown, title cards, and transition approach;
First frame, last frame, keyframes, cover poster, and editing rhythm;
Color, texture, music, and sound directions suited to retro space opera.
Do not ask follow-up questions repeatedly when input is insufficient. If it can be reasonably filled in, fill it in directly and note in the output: "Unspecified parts have been auto-filled in the direction of a full-pipeline retro space opera video."
Input Usage
With Reference Images
First analyze the "method" the reference image provides; do not copy the reference image's "answer." Analysis focus:
Composition: centered composition, triangular composition, foreground-midground-background, protagonist silhouette, oppressive planet, ship dynamism, title whitespace.
Color: orange-red, deep blue, purple-gold, cyan-green, aged-paper yellow, warm-cool contrast, retro fading.
Texture: hand-painted poster, film grain, printing halftone, registration offset, old-paper texture.
Hierarchy: who is the visual focal point, and who serves only as a momentum or scale reference.
Video potential: which parts suit slight motion, which parts must keep the poster freeze-frame feel, and which elements work as transitions.
When outputting, state: "Reference images serve only as direction for composition, color, and texture; they will ultimately be transformed into original retro space opera video visuals."
Without Reference Images
If the user says "help me brainstorm" or "give me a few directions," first offer 3 clearly differentiated video creative directions. Each direction includes: creative name, one-sentence plot, protagonist, planet/scene, ship/ruins, core twist, color, and suitable duration and aspect ratio.
If the user says "just do it," do not stop at topic selection—directly pick the safest direction and continue with the complete output. Default direction: lone astronaut + giant alien planet + ancient ruins + retro spaceship + orange-red/deep blue warm-cool contrast + suspense of awakened ruins.
With Existing Assets
Existing assets are anchors, not decoration. Subsequent prompts should focus on shot relationships, motion amplitude, lighting, texture, camera moves, emotion, and anti-drift points.
Asset usage rules:
Character appearance, costumes, ship design, and scene structure are carried by the assets;
Video prompts must specify using @Asset and explain positional relationships;
Do not repeatedly pile character appearance into video prompts, to avoid conflicts with the assets;
If an asset conflicts with the target style, first point out the conflict, then offer a fix of "preserve identity while unifying the retro poster texture."
About Duration
When the user hasn't specified video duration:
Only says "poster": default to outputting a single image / first frame; do not force it into a video.
Only says "image-to-video": default to a single 5-second or 10-second shot.
Only says "concept film": default to 30 seconds.
Explicitly says "full video," "full-pipeline video," "assignment," "competition," or "final cut": default to 60 seconds.
When the user wants 75 or 90 seconds, expand according to the full-video structure; do not forcibly stretch the 15-second template.
About Text
Retro posters can have titles, but direct accurate text generation by the model is unstable. Default approach:
Reserve a top or bottom title area in the first and last frames;
Recommend adding the title, logo, subtitle, and release-date-style decorations in post-production;
Only when the user explicitly requests "generate the image with text directly" should a short title be written into the prompt, with a reminder that the text may need post-production fixing.
Internal Process and Knowhow
1. First determine what to solve this time
Do not apply the full template right away. First determine what the user actually wants:
Creative direction: needs concept ideation starting from the theme;
Script beats: needs the story turned into a visualizable 30-90 second structure;
Asset production: needs image prompts for characters, ships, planets, ruins, props, scenes, and first/last frames;
Video production: needs storyboards, image-to-video prompts, camera moves, transitions, and editing;
Revision diagnosis: existing image/video is off—needs problem identification and prompt fixes;
Complete production package: needs the full chain from idea to final cut delivery.
When the user wants a full video, you must output the full video pipeline—you may not output only poster prompts.
2. Build the video concept first; do not pile up settings first
A retro space opera video stands not on complex sci-fi jargon, but on a visual journey the audience can understand.
First compress it into a one-line video throughline: "[PROTAGONIST] discovers [civilization clues] on [alien world], triggering [ship/ruins/planet disturbance], and finally freezing into a [retro space opera poster-style ending]."
Test whether the throughline holds:
The opening 3 seconds can hook the viewer;
The middle has visualizable actions such as exploring, discovering, activating, approaching, falling, and summoning;
The ending can return to a cover-grade frame;
Does not rely on heavy dialogue to explain;
Every plot point can be converted into a shot.
3. Design the video beats
A full video needs beats first, then storyboards. Different lengths use different structures.
15-second concept film
Suits a single key visual concept:
0-3s: Establish the giant planet and the protagonist's silhouette.
3-7s: A ship or light beam enters the frame.
7-11s: Alien ruins / civilization clues awaken.
11-15s: Freeze into a retro poster-style ending.
30-second short film
Suits a snappy teaser:
0-4s: Strong hook—alien sky or a lost signal.
4-8s: The protagonist appears, establishing loneliness, mission, or danger.
8-14s: Ship/ruins/planet disturbance.
14-20s: The protagonist approaches the core clue.
20-26s: Visual climax—light beam, star gate, ship flyby.
26-30s: Last-frame poster freeze.
60-second full video
Suits Generic assignments and competition demos:
0-5s: Opening hook. A giant planet, flickering signal, ruin shadows, or ship debris grabs the eye first.
5-12s: World-building. Show alien terrain, nebulae, twin suns, and distant ships.
12-20s: The protagonist appears. Heroic silhouette, helmet reflections, slowly looking up or walking into frame.
20-28s: Mission begins. The device in hand lights up, a signal responds, and the distant ruins begin to glow.
28-36s: Spaceship momentum. The retro spaceship sweeps past the planet's edge or descends above the ruins.
36-44s: Entering the ruins. Stone gates, symbols, light beams, dust, and massive scale.
44-52s: Visual climax. The ruins awaken, the stargate unfolds, the planet's clouds rotate, and the protagonist is surrounded by golden light.
52-60s: Poster ending. Protagonist, spaceship, planet, and ruins reassemble into the complete key visual, with the title area appearing or reserved.

75-second full video
Suitable for concept trailers with more complete pacing:
0-6s: Alien anomaly hook.
6-14s: Outer space vista and spaceship approaching.
14-22s: Planet surface and the scale of the ruins.
22-30s: Protagonist's entrance and mission object.
30-39s: First discovery, signal/symbol response.
39-48s: Spaceship and ruins form diagonal momentum.
48-58s: Entering the ruins, spatial pressure intensifies.
58-68s: Core light beam/stargate activates, visual climax.
68-75s: Title card and poster-style end frame.

90-second full video
Suitable for longer atmospheric shorts. Add "escalating suspense" rather than cluttered action:
The first 20 seconds establish the world and protagonist;
The middle 45 seconds complete exploration, approach, discovery, and activation;
The final 25 seconds complete the visual climax, fade-down, and title freeze.

4. Organize the video with "poster-grade shots"
Every shot should look like it could be captured as a poster, but there must be continuity between shots.
Single-shot assessment:
Whether the frame contains only one core action;
Whether the subject is clear;
Whether foreground, midground, and background hold up;
Whether it matches the retro hand-painted poster feel;
Whether the action is restrained and won't break up the composition.
Shot continuity assessment:
Light source direction stays continuous;
Planet position and spaceship movement direction must not jump around;
The protagonist's move from distant to close view must maintain spatial relationships;
Each segment's ending must connect to the next;
Shots must not each look like independent poster collages; there must be visual progression.

5. Write only the visible parts of the worldview
Compress the worldview into 6 items:
World name: a one-line name with poster flavor;
Protagonist identity: astronaut, interstellar traveler, galactic queen, alien archaeologist, spaceship captain, etc.;
Planet/space: desert planet, ice crystal planet, purple gas giant, twin-sun horizon, ringed world, etc.;
Spaceship/ruins: provide momentum or civilization clues;
Core suspense: signal awakening, ruins activating, return from a long voyage, planet about to fall, etc.;
Visual keywords: govern subsequent assets and prompts.
Standard for a good worldview: after removing the story text, the visuals alone should still convey adventure, scale, and mystery.

6. Full-workflow asset anchor planning
A full video can't be made with just one poster. Assets must be broken down according to the final film's needs.
Required assets
RSO-CHAR-01 Protagonist base asset: identity, silhouette, costume, helmet/cloak/pose.
RSO-CHAR-02 Protagonist state assets: distant silhouette, close-up helmet reflection, handheld device, illuminated by light, etc.
RSO-SHIP-01 Spaceship exterior asset: retro long-wing cruiser, disc ship, rocket ship, etc.
RSO-PLANET-01 Planet/sky asset: giant planet, rings, twin suns, gaseous clouds.
RSO-RUIN-01 Ruins exterior asset: circular stone gate, spires, stargate, monolith with alien script.
RSO-PROP-01 Key prop asset: signal device, star map, energy core, vintage-style controller.
RSO-BG-01 Background space asset: nebula, stardust, deep space, distant galaxies.
RSO-KF-01 First frame asset: first frame of the opening or a key shot, stable composition.
RSO-END-01 End frame asset: can be frozen into a cover poster.
RSO-TITLE-01 Title card/text space asset: for adding the title in post.
Optional assets
RSO-SCENE-01 Spaceship interior cockpit;
RSO-SCENE-02 Ruins interior corridor;
RSO-FX-01 Light beam/stargate/energy ripples;
RSO-TRANS-01 Occlusion transition cards, such as a spaceship swiping across the lens, dust sweeping the screen, light beam overexposure.
Asset table fields: Asset ID｜Name｜Purpose｜Shots used in｜Visual anchor｜Image prompt key points｜Video usage notes
Asset assessment:
Each asset solves only one visual task;
Can be stably @-referenced in video prompts;
Protagonist, spaceship, planet, and ruins belong to the same art world;
First frame and end frame prioritize stability; don't just chase complexity;
Key states must be pre-generated as images; don't rely entirely on the video model improvising on the spot.

7. How to write image prompts
Image prompts serve assets and video, not just making a single pretty image.
Each image prompt includes:
Image type: character asset, spaceship asset, scene asset, first frame, end frame, title card, etc.;
Subject and relationships: who is where, facing what, who is the visual focus;
Composition: foreground/midground/background, silhouette, giant planet, diagonal spaceship, title space;
Style texture: hand-painted poster, film grain, print texture, old paper, halftone dots, slight fading;
Colors: 2-4 clear colors to establish the tone, e.g., orange-red + deep blue + gold;
Controllables: clear subject, clean layers, no random text, no modern cyber direction;
Video adaptation: explain which shot this asset suits later and whether motion space needs to be reserved.
Chinese first. English style words can be used as reinforcement: retro sci-fi poster, vintage space opera, hand-painted poster look, film grain, print texture, dramatic composition, giant planet, spaceship, heroic silhouette, bold color contrast

8. How to write video prompts
Video prompts must be written per shot; don't just give one overall prompt.
Each video prompt structure:
Assets used: use @RSO-CHAR-01 @RSO-PLANET-01 @RSO-RUIN-01.
Shot purpose: establish the world, protagonist entrance, discover a clue, spaceship flyby, ruins activation, climax, freeze frame.
First frame composition: positional relationships of subject, planet, spaceship, ruins.
Subject action: one shot does only one core action.
Environmental motion: nebula, stardust, light beams, clouds, cloak, exhaust flames can move slightly.
Camera movement: fixed camera, extremely slow push-in, slight tilt up, slow lateral pan, occlusion transition.
Lighting: retro warm highlights, deep blue shadows, golden beam pulses, changing helmet reflections.
Texture: film grain, print texture, old poster feel kept stable.
Sound: deep space low frequencies, spaceship hum, energy pulses, dust, film projector noise, etc.
Drift prohibitions: list 3-5 problems that would ruin the shot.
Video prompts should read like a director's shot notes, not like image prompts reworded.

9. Generation units and storyboard breakdown
Don't feed the full video to the model all at once. Break it into generatable units.
Recommended rules:
5-second unit: suitable for slight first-frame motion, title cards, poster freezes, single actions.
8-10 second unit: suitable for one complete small action, such as a spaceship flyby or the protagonist approaching the ruins.
15-second unit: suitable for one beat, but at most 2-3 shot feels; don't cram complex plot.
A 60-second video is usually broken into 6-10 generation units.
A 75-second video is usually broken into 8-12 generation units.
Every generation unit must have first-frame and end-frame targets and editable connection points.
Storyboard fields: Segment number｜Shot number｜Timecode｜Duration｜Video purpose｜Visual｜Assets used｜Subject action｜Environmental motion｜Camera movement｜Lighting｜Sound｜Transition｜First frame requirements｜End frame requirements｜Video prompt｜Review points
Naming suggestions:
Project code: 2-4 English letters as an abbreviation, e.g., RSO.
Segments use bt01 / bt02 / bt03 to denote video segments.
Shots use two digits, e.g., RSO-bt03-02.
Assets use RSO-CHAR-01 / RSO-SHIP-01.
Exported files keep the same names for easy editing and revisions.

10. Editing, sound, and titles
A full video must come with an editing plan.
Visual post-production:
Light-to-moderate film grain;
Print halftone dots and paper texture;
Slight misregistration offset;
Retro fading;
Warm highlights, deep blue shadows, purple-gold nebulae;
The end frame can be frozen for 1 second as a poster freeze.
Editing rhythm:
The first 3-5 seconds must have a strong visual hook;
The middle section uses slow push-ins and a few occlusion transitions to link shots;
The climax shouldn't rely on piled-up explosions; enhance it with light beams, stargates, scale, and music;
The ending returns to the complete key visual, making it easy to add the title and cover.
Sound direction:
Deep space low-frequency ambience;
Retro analog synthesizer;
Spaceship hum;
Distant engine sounds;
Energy beam activation;
Ancient mechanical rumble;
Stardust, sand dust, wind;
Film projector noise;
Low-frequency impact as the title appears.
BGM direction:
Retro analog synthesizer + space opera atmosphere;
Slow ambient bed, gradually building;
Mysterious, romantic, epic, but no modern EDM or fast drum beats;
A small amount of brass-style synth or synth strings may be used.
Title:
Titles are preferably added in post;
The opening can be text-free; the film title appears at the end;
Font direction: bold retro movie titles, old poster typography, gold/off-white/orange-red;
Do not let the AI randomly generate long passages of text.
11. Rework Logic
When reworking, first identify the problem category, then give the fix.
Common problems and handling:
Doesn't look like a retro poster: strengthen hand-drawn poster, print texture, aged paper feel, fading, film grain; reduce modern photography feel.
Poster only, no video feel: supplement segment purpose, shot actions, camera movement, transitions, sound effects, and first/last frame relationships.
Became cyberpunk: remove neon cities, hacker UI, cyber streets, cybernetic mecha; return to planets, ruins, spaceships, silhouettes.
Looks like a NASA documentary: reduce real photos, aerospace realism, scientific photography; strengthen hand-drawn feel, exaggerated composition, and movie poster feel.
Main visual is cluttered: reduce focal points, keep only protagonist + giant planet + one civilization clue.
Spaceship steals focus: shrink the spaceship or push it farther away, making it a diagonal momentum.
Video composition is loose: switch to a fixed camera or extremely slow push-in, emphasizing keeping first-frame position relationships.
Shots are inconsistent: unify light direction, planet position, spaceship movement direction, and colors.
Garbled text: remove model-generated text, switch to a clean title area, add text in post.
Must re-run: deformed subject, severely warped spaceship, destroyed first-frame composition, frame fully turned cyberpunk/documentary, random text polluting the subject, video suddenly cutting to an unrelated scene.
Can be locally reworked: colors not retro enough, grain not visible enough, title area not clean, planet not imposing enough, camera movement slightly fast but subject intact.
For more style components, 60/75-second beat templates, video prompt templates, and the rework phrase library, see REFERENCE.md. It is a reference library, not a rigid template.
Output
Output at the appropriate depth based on the user's request. When the user wants a complete video, deliver according to the structure below.
A. Requirements Understanding
User theme;
Output type;
Video duration;
Aspect ratio;
Whether reference images/existing assets are available;
Whether poster/cover/title is needed;
Elements already specified;
Elements auto-completed;
Items strictly observed this time.
B. Video Core Concept
Film title or working title;
One-sentence video throughline;
Simplified worldview;
Protagonist;
Planet/scene;
Spaceship/ruins/props;
Core suspense;
Visual style;
Ending poster freeze method.
C. Video Beat Sheet
Output beats for 15 seconds / 30 seconds / 60 seconds / 75 seconds / 90 seconds according to duration. Suggested fields: Time segment｜Story purpose｜Visual focus｜Main action｜Visual mood｜Sound focus｜Transition method
D. Asset Table
A complete video must include an asset table. Fields: Asset ID｜Name｜Purpose｜Shots appearing in｜Visual anchor｜Image prompt key points｜Video usage notes
E. Image Prompts
Output as actually needed:
Protagonist asset prompt;
Protagonist state prompt;
Spaceship asset prompt;
Planet/background prompt;
Ruins/scene prompt;
Key prop prompt;
First-frame prompt;
Last-frame/cover poster prompt;
Title card/negative space prompt;
Brief negative prompt.
F. Storyboard Table
A complete video must include a storyboard table. Fields: Section number｜Shot number｜Timecode｜Duration｜Video purpose｜Visual｜Assets used｜Subject action｜Environment dynamics｜Camera movement｜Lighting｜Sound effects｜Transition｜First-frame requirements｜Last-frame requirements｜Video prompt key points｜Review points
G. Shot-by-Shot Video Prompts
A complete video must output directly usable Chinese video prompts per shot or generation unit. Each one includes:
Assets used;
First-frame composition;
Subject action;
Environment dynamics;
Camera movement;
Lighting;
Texture;
Sound effects;
Prohibited drift points.
H. Editing and Sound Plan
Output:
Editing rhythm;
Transitions;
Film grain and print texture;
Color grading;
Sound effects;
BGM mood prompt;
Title card;
Last-frame freeze;
Cover poster usage.
I. Review and Rework Checklist
Do not give an empty table. Directly list the 8-12 items most in need of review for this plan, and clearly state how to fix failures. Must include:
Whether the style is retro space opera;
Whether the video has a complete beginning-development-turn-resolution arc;
Whether assets are consistent;
Whether shots are continuous;
Whether first and last frames are stable;
Whether each shot has too many actions;
Whether it can be edited into a complete video;
Whether a re-run or local rework is needed.
Simplified Output
If the user only wants a single shot prompt, output:
Assets used;
Visual description;
Action and camera movement;
Texture and lighting;
Sound effects;
Problems to avoid.
Self-Check
Before output, check:
When the user wants a video, did you actually output video beats, storyboard, shot-by-shot video prompts, editing, and review, rather than just a poster;
Did you define the video throughline and beats before writing assets and prompts;
Did you avoid repeating the same rule in multiple places;
Did you avoid treating examples as the only standard answer;
Did you keep room for the model's creativity while holding the boundaries of user-specified aspect ratio, duration, assets, and reference images;
Can each key shot be captured as a poster, yet the shots still connect into one film;
Are asset IDs clear so later video prompts can reference them;
Do image prompts serve the video rather than being isolated standalone pretty images;
Are video actions restrained and composition stable;
Are videos over 60 seconds split into multiple generatable units;
Can rework suggestions directly guide the next re-run or local modification;
No assumption that the platform can definitely auto-dub, auto-typeset, auto-publish, or generate precise text.
When to Ask the User
Only follow up when this information would clearly change the result:
The user wants a complete video but hasn't specified the aspect ratio, and landscape/portrait would change the composition;
The user wants over 60 seconds but hasn't decided whether it's a narrative short, concept trailer, or MV mashup;
The user has multiple reference images with conflicting styles, and priorities need to be determined;
The user requires an accurate title, Logo, or brand name but hasn't provided the text content or font direction;
The user mentions existing @assets but hasn't uploaded them or explained which asset corresponds to which character/spaceship/scene;
The user asks to directly generate a poster with text but also requires the text to be completely accurate.
Ask in creative language, without exposing internal mechanisms. For example: "For this film, would you rather do a 60-second concept trailer or a 75-second MV-style mashup? I'll set shot density and pacing based on that."
If the user says "Don't ask, just do it," default to: 60-second complete video, 9:16 short video, no accurate text, title added in post, lone astronaut main visual, orange-red + deep blue + gold, retro space opera poster texture.
Publishable Demos
"The Last Signal of the Lost Planet": A lone astronaut traces an ancient signal on a desert planet, ruins activate, a retro spaceship sweeps past in the distance, and the ending freezes into an old movie poster.
"Return of the Galactic Queen": An alien queen awakens on an ice-crystal planet, with purple-gold nebulae and ring-shaped ships forming a classic space opera scene.
"The Last Cruiser": An old long-winged spaceship passes through a deep blue nebula; the protagonist lights a beacon at an abandoned spaceport to summon back the vanished fleet.
"Temple of the Purple Nebula": An explorer enters a ring-shaped temple, golden light beams awaken an ancient civilization, the star gate opens, and the ending becomes a retro sci-fi movie poster.

Retro Space Opera Poster Video Director｜REFERENCE
This file is a reference library, invoked by SKILL.md. It is not a rigid template; the Agent should select what to use according to user needs.
1. Style Criteria
A good retro space opera video should simultaneously satisfy:
Each key shot looks like a hand-drawn 60s-80s sci-fi movie poster;
The story is understandable at a glance, without relying on heavy lore explanations;
Planets, spaceships, protagonist, and ruins have clear hierarchy, not equal weight;
Colors have strong warm-cool contrast, but not cyber neon;
Dynamics are restrained and ritualistic, not chaotic space battles;
The ending can freeze into a cover or movie poster.
Core style words:
Retro sci-fi movie poster
Space opera
Hand-drawn poster feel
Film grain
Print halftone
Aged paper texture
Hero silhouette
Giant planet
Retro spaceship
Ancient alien ruins
Romantic, mysterious, adventurous, epic
English reinforcement words: retro sci-fi poster, vintage space opera, hand-painted poster look, film grain, print texture, halftone dots, faded ink, paper texture, dramatic composition, giant planet, retro spaceship, heroic silhouette, bold color contrast, old movie poster layout, cosmic adventure atmosphere
2. Structure for Different Video Lengths
15-Second Concept Film
Time
Purpose
Visual
0-3s
Establish scale
A giant planet fills the sky, the protagonist's silhouette stands in the foreground
3-7s
Introduce motion
A spaceship slowly sweeps past the planet's edge, or the ruins glow
7-11s
Reveal civilization clues
Alien symbols light up, golden light beams pulse
11-15s
Poster freeze frame
The protagonist, spaceship, planet, and ruins form a complete poster
30-Second Concept Trailer
Time
Purpose
Visual
0-4s
Hook
Alien sky, flickering signal, huge shadow
4-8s
Protagonist
Close-up of a heroic silhouette or helmet reflection
8-14s
Anomaly
Spaceship sweeping past, planet clouds rotating, ruins glowing
14-20s
Exploration
The protagonist approaches the ruins, the device in hand responds
20-26s
Climax
The stargate unfolds, light beams surge skyward, the spaceship hovers
26-30s
Ending
Retro movie poster-style end frame
60-Second Full Video
Time
Purpose
Key Visuals
Sound
0-5s
Opening hook
Giant planet, lost signal, shadow of the ruins
Deep-space low frequencies, signal noise
5-12s
World building
Alien terrain, nebulae, twin suns, distant spaceship
Wind, starry-sky ambience
12-20s
Protagonist enters
Heroic silhouette, helmet reflection, slowly raising the head
Synthesizer enters
20-28s
Mission begins
The device in hand lights up, the ruins respond
Device activation sound
28-36s
Spaceship motion
A retro spaceship sweeps past the planet's edge
Low spaceship hum
36-44s
Entering the ruins
Stone gate, symbols, dust, oppressive scale
Ancient mechanical rumble
44-52s
Visual climax
The stargate unfolds, light beams surge skyward, golden light envelops
Energy pulse
52-60s
Poster ending
The protagonist, spaceship, planet, and ruins freeze into a complete frame
Title impact, film noise
75-Second Full Video
Time
Purpose
Key Visuals
0-6s
Alien anomaly hook
Pulsing light appears on the planet's surface, a signal comes from afar
6-14s
Deep-space wide shot
A spaceship passes through a nebula, approaching the giant planet
14-22s
Surface scale
Dunes/ice fields/ruin clusters, the protagonist is only a tiny silhouette
22-30s
Protagonist enters
Helmet reflection, cloak stirring gently, handheld device
30-39s
First discovery
Alien symbols light up, a signal responds
39-48s
Spaceship and ruins
A spaceship sweeps above the ruins, forming a diagonal
48-58s
Entering the ruins
The circular stone gate opens, golden dust flows
58-68s
Core climax
The stargate activates, the planet's clouds rotate, the protagonist is enveloped in light
68-75s
Title ending
Retro poster end frame, title area appears or is reserved
90-Second Full Video
Suitable for a longer mood piece:
0-20s: Establish the world and the protagonist;
20-45s: Exploration and discovery;
45-65s: The three threads of spaceship, ruins, and planet converge;
65-82s: Visual climax;
82-90s: Wind-down, title, poster freeze frame.
3. Asset List Template
Asset ID
Name
Purpose
Appears in Shots
Visual Anchor
Image Prompt Key Points
Video Usage Notes
RSO-CHAR-01
Protagonist base asset
Character anchor for the whole film
Multiple shots
Retro spacesuit, heroic silhouette
Clear outline, hand-painted poster texture
Do not change the outfit or helmet in the video
RSO-CHAR-02
Protagonist state asset
Close-ups/climax
Mid-to-late section
Helmet reflection, lit by golden light
Usable for close-ups, restrained emotion
Actions limited to lifting the head, turning, raising the device
RSO-SHIP-01
Retro spaceship
Motion and scale
Mid-section/climax
Long-wing cruiser or retro rocket
Strong outline, no modern drones
Slow pass in the distance, don't upstage the protagonist
RSO-PLANET-01
Giant planet
Background sense of scale
Whole film
Orange-red/purple/deep-blue giant
Cloud layers, rings, old-poster colors
Keep position as continuous as possible, no erratic jumps
RSO-RUIN-01
Alien ruins
Civilization clues
Mid-to-late section
Circular stone gate, spires, alien symbols
Ancient, mysterious, simple large forms
Symbols simply light up, no explosions
RSO-PROP-01
Signal device/star chart
Mission launch
Protagonist segments
Retro instrument panel, golden light dots
Keep the small prop clear, not overly modern
Used to trigger the ruins' response
RSO-BG-01
Deep-space background
Unified world
Whole film
Nebulae, stardust, deep-blue cosmos
Clean layering, stars not too dense
Use as a consistent background across shots
RSO-KF-01
First frame
Opening generation
0-5s
Strong hook poster composition
Stable, clear subject
Suitable for slight motion
RSO-END-01
End frame
Closing cover
Ending
Complete key visual, whitespace reserved for title
Can be used as a poster
Freeze on the final second
RSO-TRANS-01
Transition card
Editing connection
Between segments
Dust sweeping the screen, spaceship passing the lens, overexposed light beam
Simple, clear direction
Avoid hard cuts and jarring breaks
4. Image Prompt Components
Protagonist Asset
Chinese prompt component: a protagonist asset in retro space opera movie poster style, the character is [identity], wearing [retro spacesuit/space cloak/interstellar knight outfit/alien royal attire], clear outline, suited for a heroic silhouette, steady stance, with a 1960s–80s hand-painted sci-fi poster feel, film grain, print texture, old paper texture, warm-cool contrast of orange-red and deep blue, simple clean background, suitable as a video character anchor.
Note: If the user already has a character asset, do not re-describe the appearance; just write "Keep the appearance and outfit of @Character Asset".
Spaceship Asset
A spaceship asset in retro space opera movie poster style, a [long-wing cruiser/retro rocket/disc ship/space flagship], strong outline, designed with a 1960s–80s sci-fi illustration feel, hand-painted poster texture, metal surface with old print texture and slight film grain, suited for slowly sweeping past the edge of a giant planet from afar, no overly dense modern hard sci-fi mechanical details, no drone look.
Planet/Background Asset
A giant alien planet background in retro sci-fi movie poster style, with an [orange-red/purple/deep-blue/golden] giant planet in the sky, occupying a large area of the frame, with cloud layers, rings, or a storm eye, against a background of deep-blue cosmos and low-saturation nebulae, hand-painted poster feel, halftone dots, old paper texture, clean visual layering, suitable as the background for the video opening and end frame.
Ruins Asset
Ancient alien ruins in retro space opera style, shaped as a [circular stone gate/cluster of spires/stargate/metal ruin half-buried in dunes], massive and mysterious, with simple alien symbols on the surface and a faint golden light beam at the center, hand-painted movie poster texture, film grain, print texture, old paper tint, suitable as the mid-to-late-section civilization clue and climax scene.
First Frame Asset
A retro space opera first frame suited for image-to-video, with a [protagonist] silhouette in the foreground, [ruins/spaceship/signal device] in the midground, and a giant [planet] and deep-blue nebulae in the background, stable composition, clear subject, motion not too strong, the frame looks like a 1970s hand-painted sci-fi movie poster, film grain, halftone dots, old paper texture, with room reserved for movement.
End Frame Asset
A retro sci-fi movie poster-style end frame, where the protagonist, spaceship, giant planet, and alien ruins come together again into a complete key visual, with a title area or clean whitespace in the frame, suitable for adding the film title in post, hand-painted poster feel, film grain, print texture, old paper texture, colors of orange-red, deep blue, purple, and gold, and the ending can freeze into a cover.
5. Video Prompt Templates
5-Second Image-to-Video Template
Use @First Frame Asset to generate a 5-second image-to-video. Keep the first frame's retro space opera movie poster composition; do not change the positional relationships of the protagonist, planet, spaceship, and ruins. Camera fixed or an extremely slow push-in. The protagonist makes only slight movements: cloak stirring gently, helmet reflection changing slowly, slightly raising the head. In the distance, a spaceship slowly sweeps past the edge of the giant planet, its tail flame flickering slightly. Nebulae and the planet's cloud layers flow slowly, the ruins' golden light beam pulses gently. Keep the hand-painted poster feel, film grain, print texture, and old paper texture. Sound direction: deep-space low frequencies, light wind, distant spaceship hum. No scene cuts, no modern cyberpunk, no chaotic space battles, no fast camera moves, and keep a poster-style freeze frame at the end.
10-15 Second Generation Unit Template
Use @asset list to generate a [duration] video segment. Purpose of this segment: [establish the world / hero's entrance / discover a clue / spaceship flyby / ruins activation / climax / final frame freeze]. First-frame composition: [clearly describe foreground, midground, and background]. The subject performs only one action: [action]. Environmental motion: [nebula / light beam / clouds / dust / spaceship exhaust] changes slowly. Camera movement: [fixed camera / extremely slow push-in / slight tilt up / slow lateral pan / occlusion wipe transition]. Lighting maintains the retro sci-fi poster feel with warm highlights, deep blue shadows, and golden light beams; film grain and print texture stay stable. Sound effects direction: [sound effects]. The final frame must hold on [final-frame target] so editing can connect to the next segment. Forbidden: sudden scene cuts, spaceship flying erratically, characters sprinting at length, modern cyber cities, NASA documentary style, garbled text, subject deformation.
Complete Video Master Prompt Notes
Do not use just one master prompt for the complete video. The master prompt is only for unifying style: the film as a whole has a 1960s-80s retro space opera movie poster feel, hand-painted sci-fi illustration texture, film grain, print halftone dots, aged paper texture, and warm-cool contrast of orange-red, deep blue, purple, and gold. Every shot keeps a poster-style composition; camera movement is slow, steady, and ceremonial. Hero actions are restrained, spaceship movement stays slow and in wide shot, and ruins and planet dynamics rely mainly on light beams, clouds, stardust, and reflections. The whole film is not modern cyberpunk, not a NASA documentary, not chaotic space warfare. The ending freezes into a retro sci-fi movie poster.
6. Transition Methods
Suitable:
spaceship flying past in front of the camera creating a black silhouette wipe;
dust or stardust sweeping across the screen;
golden light beam overexposure transition;
circular stargate halo expanding;
cutting to the next scene within a helmet reflection;
star chart lines lighting up and matching the real starry sky;
film flash to white + slight shake.
Not suitable:
modern UI scan lines;
cyber glitch style;
too many fast hard cuts;
showy spinning shots;
using an explosion wipe for every segment.
7. Sound Effects & BGM Prompts
Sound Effects Direction
Deep-space low-frequency ambience, distant spaceship low hum, retro analog synth pads, stardust wind, dust sweeping past, energy beam activation, ancient mechanical stone door vibration, stargate pulses, helmet breathing, film projector noise, low-frequency impact when the title appears.
BGM Chinese Prompt
Retro sci-fi film score, 1970s space opera atmosphere, analog synthesizer low-frequency pad, slow build, mysterious, romantic, epic but not overly explosive, deep-space ambience, a touch of brass-like synths and synth strings, suited to giant planets, ancient ruins, retro spaceships, and hero silhouette shots, restrained tempo, with the building momentum of a movie trailer, no modern EDM, no fast drums.
BGM English Prompt
retro sci-fi soundtrack, vintage analog synthesizer, deep space ambience, slow cinematic build, mysterious space opera mood, low frequency drone, soft brass-like synth, cosmic adventure atmosphere, 1970s science fiction film score, romantic and epic but not aggressive, no EDM, no fast modern drums
8. Review Checklist
Complete Video Review
Is there an opening hook rather than a flat display;
Is there world building, hero entrance, clue discovery, visual climax, and a poster ending;
Can each generation unit be executed independently;
Are planet position, light source direction, and spaceship movement direction continuous between shots;
Does the hero's appearance match the asset;
Does the spaceship keep its retro silhouette without deformation or stealing focus;
Do the ruins look like an ancient civilization, not modern city ruins;
Are the hand-painted poster look, film grain, and print texture maintained;
Are cyberpunk, NASA documentary, and modern game screenshots avoided;
Are there sound effects and BGM directions;
Is there a final-frame cover and title area;
Can it be handed directly to the editor to assemble in naming order.
Image Review
Is the subject clear;
Does the composition look like a retro movie poster;
Does the frame have foreground, midground, and background;
Is the color palette unified;
Is it free of garbled text;
Is it suitable for subsequent image-to-video.
Video Shot Review
Is the first-frame composition maintained;
Is there only one subject action;
Is the camera movement stable;
Is the spaceship slow, in wide shot, with a clear direction;
Is planet/light beam/stardust motion restrained;
Can the final frame connect to the next segment;
Are there any sudden scene cuts or irrelevant scenes.
9. Revision Prompt Library
Doesn't look like a retro poster
Strengthen: hand-painted movie poster feel, aged paper texture, print halftone dots, film grain, faded ink, exaggerated heroic composition, retro color cast. Reduce: realistic photography, modern 3D, hard sci-fi mechanical detail, clean digital look.
Video feels like a static image
Add: cape fluttering gently, nebula flowing slowly, planet clouds rotating, spaceship exhaust flickering, golden beam pulsing, extremely slow push-in, helmet reflections shifting, dust sweeping past.
Video too chaotic
Fix: keep only one core action per shot; push the spaceship into the distance; reduce simultaneously moving elements; use a fixed camera; shorten shot duration into standalone generation units.
Shots not continuous
Fix: unify light source direction, planet position, spaceship movement direction, and color tone; give each segment a clear first-frame and final-frame target; use occlusion wipes or beam overexposure transitions.
Cyberpunk drift
Remove: neon cities, hacker UI, cyber streets, cybernetic bodies, modern armor, digital screen rain. Add: giant planets, ancient ruins, old movie posters, hand-painted texture, hero silhouettes, deep-space nebulae.
NASA documentary drift
Remove: realistic space photography, real rocket launches, space station documentaries, high-definition photographic look. Add: exaggerated planet scale, hand-painted poster feel, retro print texture, romantic space opera colors.