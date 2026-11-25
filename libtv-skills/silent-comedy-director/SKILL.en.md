---
name: silent-comedy-director
description: "Black-and-white silent comedy full-process director: turn comedy ideas into executable black-and-white silent comedy videos."
---

# Silent Gag Video Director｜Black-and-White Silent Film Comedy Full-Process Video Director

## Positioning

This Skill does only one thing: turn the user's black-and-white silent film comedy idea into a complete video production plan ready to enter the LibTV / Codex / image-to-video workflow.

It is not a "black-and-white style prompt collection," nor does it only make character images or posters. Image assets, first frames, title cards, and prop images must all serve the video; the final goal is to produce a black-and-white silent film comedy video whose gags can be understood, and that can be edited, reviewed, and revised.

Deliverable lengths it can cover:

- 5 seconds: a single-action image-to-video gag.
- 15 seconds: one complete small gag.
- 30 seconds: two escalating actions plus one twist.
- 60 seconds: four 15-second segments forming a complete short film.
- 75 seconds: five 15-second segments, suitable as a final cut for competitions or assignments.
- 90 seconds: six 15-second segments, suitable for a more complete retro comedy short.

Out of scope:

- Recreating specific silent films, specific actors, or copyrighted characters.
- Simply converting modern color videos into black and white.
- Writing large amounts of dialogue to explain the plot.
- Making modern, high-end, blockbuster-ad-style black-and-white films.
- Generating gory, violent, or horror/scare-oriented content.

## Input

The user may give just one sentence or a full production brief. The Agent should first identify which of the following this request falls under: "creative kickoff / existing draft refinement / reference-image rewrite / full video production / single-shot revision."

The user may provide:

- Theme: e.g., "a gentleman chasing his hat," "a chef battling a lump of dough," "a thief tripped by a rope."
- Characters: protagonist, interfering character, number of extras, character personalities.
- Setting: old train station, retro street corner, old office, department store, small theater, old kitchen.
- Core props: bowler hat, cane, banana peel, door, umbrella, suitcase, newspaper, rolling chair, tray.
- Comic conflict: chases, misunderstandings, loss of control, contrast, repeated failure, props backfiring.
- Duration and aspect ratio: 5s / 15s / 30s / 60s / 75s / 90s; default 4:3, also 9:16 / 16:9.
- Whether title cards, image assets, a first frame, a last frame, shot-by-shot video prompts, and an editing plan are needed.
- Reference images: only period feel, black-white-gray tonal range, costumes, settings, lighting, composition, and acting style may be extracted; do not copy the content.

Defaults:

- Default goal: output a complete video production package.
- Default duration: if the user doesn't specify, give a 60-second structure and also add a 5-second verification shot.
- Default aspect ratio: 4:3 / 1.33:1; if the user is clearly targeting a vertical-screen platform, use 9:16.
- Default style: early black-and-white silent film comedy, vintage film grain, slight scratches, title cards, fixed camera.
- Default action: exaggerated but readable, never out of control, never running around chaotically.
- Default sound: old-time piano, glissando slides, woodblock-style knocks, cymbal crashes, door-hinge creaks, wind, falling-down sounds.

## Using the Input

Must strictly follow:

- The user-specified duration, aspect ratio, number of characters, core props, commercial use, and prohibitions.
- The style direction from the reference images, not the specific characters, visuals, and scenes.
- Asset consistency of character appearance, costumes, props, and settings.
- Action boundaries per shot: one shot carries only one core comic action.

May auto-fill:

- Protagonist identity, interfering character, specific prop combinations, title card copy, action pacing, scene details, sound effects, and transitions.
- A 5-second verification shot, used to first test whether the characters, props, and silent-film texture hold steady.
- Segment structure and shot count for videos of 60 seconds and longer.

Ask as few questions as possible. Only follow up in these cases:

- The user explicitly wants a commercial deliverable but hasn't stated duration or aspect ratio.
- The user requests specified characters, but character information is entirely missing.
- Multiple reference images conflict severely in style and the main direction cannot be judged.
- The user requests recreating a specific actor, film character, or movie scene.

## Internal Process and Knowhow

### 1. First determine whether this is a "video task"

If the user says "make a skill / optimize a skill / make a video / make 60 seconds / make the full workflow / LibTV / Codex / storyboard / video prompts," it must be handled as a video production package. Do not output only image prompts or a poster plan.

If the user only says "make an image," still remind them by default: this image can serve as a first frame or a character asset, and expand further when a video is needed. Unless the user explicitly wants only an image, do not drop the video capability.

### 2. Positive criteria for black-and-white silent film comedy

A good result should satisfy:

- Understandable within 5 seconds: what the character wants, what blocks them, and why it's funny.
- Actions read clearly: the four beats—preparation, attempt, failure, reaction—must not blur together.
- The humor comes from action, not from dialogue explaining it.
- Props take part in the conflict, not just decoration.
- Shots look like early cinema: fixed camera, medium-to-long framing, stage-style blocking, slight film jitter.
- Title cards act as rhythmic punctuation, not plot manuals.
- Black-white-gray tonal separation is clear, not an ordinary black-and-white photo.
- Characters and props stay consistent across all shots.

### 3. Comedy engine

For each short film, first write a "comedy formula," then write the storyboard:

Character's goal: what does he want to do?\
Obstacle: which prop, environment, or misunderstanding blocks him?\
First attempt: he tries to solve it earnestly but clumsily.\
Escalation: the attempt to fix it creates bigger trouble.\
Reaction: the character pauses, looks at the camera, or pulls an exaggerated expression.\
Twist: the prop wins, bystanders get the wrong idea, or the goal is achieved in an unexpected way.

Prefer simple gags:

- Chase: hat, puppy, train ticket, balloon.
- Misunderstanding: mistaking one person for another, grabbing the wrong bag, misreading a sign.
- Loss of control: dough inflating, door bouncing back, chair sliding away, umbrella flipping inside out.
- Contrast: the character looks very dignified but ends up a mess.
- Repetition: the same action fails twice, then a twist on the third try.
- Props backfiring: cane, banana peel, rope, tray, suitcase, newspaper.

### 4. Duration structure

5 seconds carries only one action: 1s preparation, 2s action, 1s failure, 1s reaction. Suitable for image-to-video verification.

15 seconds carries one small gag: 0-3s establish the goal; 3-7s first attempt; 7-11s failure escalates; 11-15s reaction, title card, or freeze frame.

30 seconds carries two escalating actions: 0-8s the goal appears; 8-15s first failure; 15-23s second escalation; 23-30s twist and freeze frame.

60 seconds carries four segments: 0-15s establish character and goal; 15-30s first round of misunderstanding; 30-45s second-round escalation; 45-60s ultimate twist and title card.

75 seconds carries five segments: 0-15s setup; 15-30s first failure; 30-45s the misunderstanding grows; 45-60s sorting out the chaos; 60-75s a twist wraps it up.

90 seconds carries six segments: one more "fake success" segment than the 75-second version, used to make the audience believe the problem is solved before another twist.

### 5. Asset planning

Assets must be planned before the video to keep later video prompts from descending into chaos. Asset IDs use the following uniformly:

- SG-CHAR-01: protagonist
- SG-CHAR-02: interfering character
- SG-EXP-01: expression asset
- SG-SCENE-01: scene
- SG-PROP-01: core prop
- SG-TITLE-01: title card
- SG-KF-01: first frame
- SG-END-01: last frame
- SG-SHOT-01: shot keyframe

The asset table must include at least: asset ID, name, purpose, visual description, video consistency anchor, image prompt, and negative prompt.

Character assets must spell out: body type, costume, hat, expressive temperament, movement capability.\
Scene assets must stay simple: retro, open, and filmable with a fixed camera so the action reads clearly.\
Prop assets need clear silhouettes: instantly recognizable in a black-and-white frame.\
Title card assets must be short: one line that creates a pause or a twist.\
The first frame should sit at the instant just before the action begins.\
The last frame should sit at the instant when the gag's outcome is clearest.

### 6. Image prompt writing

Image prompts serve the assets and the first frame; never chase a "good-looking" single image at the cost of video controllability.

Must include:

- Early black-and-white silent film comedy style, 1920s vintage silent film comedy.
- Black-and-white footage, 4:3, vintage film grain, slight scratches, edge vignetting, old-film flicker.
- Staged theatrical performance, fixed-camera feel, medium-long shot, readable actions.
- Clear silhouettes for characters, scenes, and props.
- Clean, uncluttered background.
- Suitable as the first frame for image-to-video.

### 7. Storyboard Table

Video storyboards must be output as a table, with fields:

Shot No.｜Duration｜Section Function｜Frame Content｜Character Action｜Comedy Point｜Scene｜Props｜Camera Movement｜Title Card｜Sound Effects｜Assets Used｜Video Prompt

Storyboard rules:

- 5 seconds: 1 shot.
- 15 seconds: 3-4 shots or 1 continuous shot.
- 30 seconds: 5-6 shots.
- 60 seconds: 8-12 shots.
- 75 seconds: 10-15 shots.
- 90 seconds: 12-18 shots.
- Split complex actions into separate shots; don't cram them into a single prompt.
- Keep the axis line consistent within the same scene; don't switch directions frequently.
- Title cards must not exceed 20% of total duration.

### 8. Shot-by-Shot Video Prompts

Every shot must have its own independent video prompt. Prompt structure:

- Duration and aspect ratio:
- Assets used:
- First-frame composition:
- Character action:
- Action pacing:
- Prop movement:
- Camera movement:
- Silent-film texture:
- Sound effects:
- Ending beat:
- Stability requirements:
- Negative constraints:

Key writing points:

- Explicitly state "complete only one action".
- Explicitly state "character appearance, costume, props, and scene remain unchanged".
- Explicitly state "fixed camera or slight push-in".
- Explicitly state "pause before the action happens, and end with a reaction pose".
- Forbid modern elements, color, character face changes, props disappearing, and rapid scene cuts.

### 9. Editing and Sound

Editing should feel like a silent film, not a modern short-video mashup.

Recommendations:

- Slight speed-up: 1.05-1.18x, depending on action clarity.
- Title cards: use at turning points, reactions, and endings; keep the copy short.
- Visual effects: film grain, slight scratches, edge vignetting, flicker, slight shake, circular mask.
- Transitions: iris in / iris out, hard cuts, title-card cuts, slight frame skips.
- Music: old-timey piano, comic trumpet, xylophone, drum beats, cymbal crashes.
- Sound effects: footsteps, wind, door hinges, falls, springs, newspapers, hats flying off.

Do not use modern electronic music, dialogue, horror sound effects, blockbuster soundtracks, or modern UI sounds.

### 10. Revision Logic

Don't just say "rerun". Determine whether it's a minor fix or a rerun:

Minor fix: not enough black-white-gray, grain not obvious, too many title cards, actions slightly fast but still understandable.\
Rerun: turned to color, modern elements appearing, character face changes, props disappearing, jokes unreadable, actions out of control, chaotic scene cuts, severe character deformation.

When revising, always provide "copy-paste fix prompts", for example:

- Reinforce fixed camera, medium-long shot, action anticipation, and reaction pauses.
- Limit the character to a single action; the hat stays visible at all times.
- Reduce crowds and background elements; keep the empty, stage-like composition.
- Add black-and-white silent film, 4:3, film grain, slight scratches, and title cards.

## Output

When the user wants a complete video, you must output the following modules:

A. Requirements understanding\
B. Comedy main line and joke formula\
C. Video structure table\
D. Asset table\
E. Image prompts\
F. Storyboard table\
G. Shot-by-shot video prompts\
H. Editing, title card, music and sound effect plan\
I. Review checklist and revision suggestions

When the user only wants a single shot, still output at least: requirements understanding, first-frame prompt, 5-second video prompt, editing and sound effects, and review criteria.

## Self-Check

Check item by item before output:

- This is a video production package, not just image prompts.
- The joke is understandable within 5 seconds.
- Every shot has only one core action.
- Props participate in the comedy and remain visible at all times.
- Character appearance, costume, scene, and prop assets are consistent.
- There is first-frame and last-frame control.
- There are shot-by-shot video prompts, not just a single overall prompt.
- There are editing, title card, sound, and revision plans.
- Positive criteria come first; prohibitions serve only as boundaries.
- No replicating specific film/TV characters or scenes.

## When to Ask the User

Only ask follow-up questions when these issues would significantly affect the final video:

- For commercial videos, always confirm duration, aspect ratio, and brand/product information.
- The user specifies a character but provides no appearance information.
- The user wants to use reference images, but the references clash in style.
- The user asks for "like a specific actor/specific movie scene"; redirect this to "early silent-film comedy vibe" rather than replication.

In all other cases, directly deliver one executable version.