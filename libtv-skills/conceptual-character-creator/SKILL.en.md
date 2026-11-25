---
name: conceptual-character-creator
description: "SSS-tier conceptual character showcase: input a character idea to auto-generate an original concept character, character sheet, and 15-second video"
---

## 2. Agent Auto-Run Hard Rules

### 2.1 Default Execution Mode

When the Agent has usable image / video generation tools, this Skill enters by default:

```text
Agent Auto-Run Mode
```

In this mode, merely handing prompts to the user for manual copying is forbidden.

The Agent must execute the following directly whenever possible:

```text
MJ character concept image generation
Image model character board generation
Video preflight check
SD2.0 final 15-second video generation
```

### 2.2 Text Fallback Mode

Enter the following mode only when the current Agent has no corresponding generation tool, the tool is unavailable, or the user explicitly requests prompts only:

```text
Prompt Fallback Mode
```

Fallback mode must explicitly state:

```text
The corresponding generation tools currently cannot be called directly, so copyable prompts are being output.
```

It must not pretend that images or videos have already been generated.

### 2.3 TEXT ONLY Is No Longer the Default

V0.6 abolishes the old "text output only by default" rule. The new rule is:

```text
If tools exist, execute; only output prompts when there are no tools.
```

When "character board", "keyframe", "success frame", or "video" is involved and tools are available, this is understood by default as requiring asset generation, not merely prompt writing.

---

## 3. Credit-Saving Hard Rule: No Video Before Validation

Although V0.6 supports automatic video generation, the final 15-second video still cannot serve as a tool for initial testing.

The following checks must be completed before final video generation:

```text
1. Character anchor confirmation
2. MJ concept image quality confirmation
3. Image model character board quality confirmation
4. Skill mechanism confirmation
5. Skill causality chain confirmation
6. Weapon / medium dominance confirmation
7. Real contact and physical feedback confirmation
8. Confirmation of the 3 success frames
9. Failure risk prediction
10. Confirmation of character personality, current emotion, performance micro-instructions, and emotional arc
11. Confirmation of final prompt reinforcement items
```

If any item is unclear, the Agent must first make a low-cost fix and must not burn final video credits directly.

Executable strategy:

```text
First fix the MJ concept image
Then fix the Image character board
Then fix the skill mechanism
Only then generate the 15-second SD2.0 video
```

---

## 4. Standard Automated Production Workflow

### 4.1 When No Character Input Is Provided

When the user has not provided a character image, character design, or character board:

```text
1. Call the character library and present 6 character directions.
2. If the user requests "auto / fully automatic / you choose", the Agent directly selects the character best suited for an SSS skill showcase.
3. Use MJ 8.1 + --preview to automatically generate a single-character concept image.
4. Run a quality check on the MJ concept image.
5. If multiple characters, half-body framing, a missing weapon, a poster-like look, or an unclear character appear, automatically rework the MJ concept image.
6. Once the MJ concept image passes, use the Image model to generate the character board.
7. Character board parameters are fixed at: 16:9 / high image quality / 2K.
8. Once the character board passes, it becomes the sole character anchor.
9. Automatically carry out character understanding, skill mechanism design, and the Video Preflight Gate.
10. After Preflight passes, use the SD2.0 video model to generate one complete 15-second video in a single pass.
```

### 4.2 When an MJ Character Concept Image Is Available

```text
1. Do not go straight to video.
2. First check whether the MJ concept image shows a single person, full body, a clear weapon, and a readable clothing structure.
3. Once it passes, use the Image model to automatically generate the character board.
4. Character board parameters are fixed: 16:9 / high image quality / 2K.
5. After the character board passes, move on to skill rehearsal and the final video.
```

### 4.3 When a Character Board Is Available

```text
1. Treat the character board as the sole character anchor.
2. Analyze the character's identity, weapon medium, visual motif, and skill dynamics.
3. Automatically output a skill mechanism rehearsal.
4. Automatically execute the Video Preflight Gate.
5. If it passes, use SD2.0 to automatically generate one complete 15-second video.
```

### 4.4 When a Failed Video Is Available

```text
1. Analyze the failed video.
2. Determine where the failure occurred: character anchor, weapon dominance, skill causality, camera work, physical feedback, or model misreading.
3. Rework the upstream prompts or the character board first; do not keep burning videos.
4. Must output the blocking points and correction strategy before the next video generation.
```

---

## 5. Midjourney Character Concept Generation Rules

Character concept images use Midjourney by default:

```text
--v 8.1 --preview
```

`--preview` must be placed at the end of the MJ prompt parameters; it invokes the 8.2 test version.

### 5.1 Single-Character Control Rules

When the goal is a single-character concept image, parallel structures that easily generate multiple characters are forbidden:

```text
A warlord, a gunslinger, a blade-bearer
```

It must be rewritten as:

- `A single character ...`
- `A single lead character who combines ...`
- `A xxx-xxx-xxx hybrid character`

and append:

```text
solo, one person only, single character, full body, centered composition, no group, no lineup, no multiple characters, no extra people
```

### 5.2 MJ Concept Image Quality-Check Hard Rules

Before a character concept image can proceed to the character board, check:

- Are there multiple characters / a character array?
- Is it half-body / cropped feet / a headshot?
- Is the main weapon or core medium missing?
- Is it overly poster-like?
- Is the clothing structure readable?
- Is the identity misunderstood?
- Were multi-views / multi-panels generated prematurely?
- Is there text, logo, UI, or garbled-character interference?

If it fails, first call `references/mj-common-error-repair-library.md` for repair; do not proceed to the character board.

---

## 6. Image Model Character Board Generation Hard Rules

V0.6 explicitly corrects:

```text
The character board is not generated by continuing with MJ; it is generated with the Image model.
```

Character board generation parameters are fixed as:

```text
Model: Image model
Aspect ratio: 16:9
Image quality: High quality
Resolution: 2K
Input reference: The final MJ character concept image as {{Image 1}}
Output target: Professional character turnaround sheet / character reference model sheet
```

The character board must include:

- Facial close-up
- Front view
- Back view
- Left-side profile
- Right-side profile
- A vertical height measurement scale next to the full-body view
- An information panel in the lower-left corner
- A white studio background
- Soft, even studio lighting
- Identity, proportions, clothing, weapon, and materials consistent across all views

After the character board is generated, run quality checks:

- Is it the same character?
- Are all five views present?
- Is the full body clear?
- Does the weapon / medium appear?
- Is the clothing structure readable?
- Are there no extra characters?
- Are there no misalignments / deformities / extra hands or feet?
- Is it suitable as the sole video reference anchor?

For templates, see:

```text
templates/image-model-character-board-template.md
templates/character-board-from-mj-template.md
```

---

## 7. Character Board Sole Anchor Rule

Once the character board is generated, it becomes the **sole character anchor** for all subsequent skills and videos.

The following are forbidden:

- Falling back to mixing in the MJ concept image
- Mixing in other unrelated reference images
- Redesigning the face, clothing, weapon, or body type
- Arbitrarily changing the identity to fit a skill's needs

Video prompts must preserve the following from the character board:

- Facial structure
- Hairstyle and hair color
- Perceived age
- Skin tone
- Body type and proportions
- Clothing silhouette and materials
- Weapon / props / accessories
- Core aura and sense of identity

---

## 8. Character Personality and Emotional Performance Hard Rules

V0.6.2 adds a new hard rule: the final video must not lock in only the appearance, weapon, and skill; it must also lock in the character's personality, current emotion, and performance drivers.

Before any character enters final SD2.0 15-second video generation, the following must be completed:

```text
【Character Personality Anchor】
Core personality axis:
Aura keywords:
Behavioral style:
Intimidation style:
Emotional expression style:
Forbidden performances:

【Current Emotional State】
Current emotion:
Emotional intensity: /10
Trigger reason:
Eruption style:
Closing afterglow:

【Performance Micro-Instructions】
Gaze:
Mouth expression:
Breathing:
Head movements:
Shoulder and neck state:
Hand state:
Pause before eruption:
Post-eruption reaction:
Closing state:

【15-Second Emotional Arc】
0-3 seconds: Emotion establishment
3-7 seconds: Rising pressure
7-11 seconds: Eruption
11-15 seconds: Aftershock / convergence / personality and attitude revealed
```

If any of the above parts is missing, the Agent must not directly generate the final video.

### 8.1 The Character Must Not Be Just a "Shell That Casts Skills"

Wrong direction:

```text
The character stands, casts the skill, and strikes a pose at the end.
```

Correct direction:

```text
The character performs the skill in a way consistent with their own personality and current emotion; movement rhythm, gaze, breathing, pauses, eruption, and closing all serve the character's personality.
```

### 8.2 New Fields Required in the Final Video Prompt

The final SD2.0 video prompt must include:

```text
【Character Personality Anchor】
【Current Emotional State】
【Performance Micro-Instructions】
【15-Second Emotional Arc】
【Closing Emotional Afterglow】
```

These fields must not be compressed into a single sentence, nor reduced to single words like "cold" or "angry".

For details, see:

```text
references/character-personality-and-emotion-system.md
templates/personality-emotion-preflight-template.md
```

---

## 9. Video Preflight Gate

Before final video generation, the following must be completed automatically:

```text
【Character Personality and Emotion】
Core personality axis:
Current emotion:
Performance micro-instructions:
15-second emotional arc:

【Skill Causality Chain】
Character action:
Weapon / medium action:
Real contact:
First visual result:
Environmental reaction:
Final convergence:

【Weapon / Medium Dominance Check】
Does the dominant action come from the weapon / medium:
Are the effects triggered by the weapon / medium:
Is there real contact and physical feedback:
Can the audience tell at a glance that the result was caused by that weapon:

【3 Success Frames That Must Appear】
1.
2.
3.

【Failure Risks】
1.
2.
3.

【Rehearsal Conclusion】
Pass / Blocked
```

If the conclusion is "Blocked", the Agent must not generate the final 15-second video and may only automatically repair the upstream assets or prompts.

---

## 10. Skill Dynamics Priority Rule

All characters are forbidden from defaulting to the homogenized structure of "standing charge-up + circular magic circle + ultimate burst".

The character's dynamics must be determined first:

- Speed type
- Heavy-strike type
- Weapon-trajectory type
- Firearm-trigger type
- Ritual-scepter type
- Summoning type
- Corruption type
- Environment-rewriting type
- Illusion-displacement type
- Close-quarters suppression type
- One-strike finisher type
- Domain expansion type
- Cape-carrier type
- Gunshot-judgment type
- Path-delayed burst type
- Reality-cropping type
- Fate-stitching type
- Withering-finale type

For details, see: `references/skill-dynamics-library.md`

---

## 11. Anti-Template Checker

Before any output / execution, check:

- Has it once again been written as an ordinary magic circle?
- Is it yet another fireball / lightning / black mist / light pillar / laser?
- Are all characters swinging swords or raising a hand for an ultimate?
- Do the effects lack a medium source?
- Do the character's features vanish during the ultimate?
- Does the facial close-up exceed 0.5 seconds?
- Is the shot a single medium shot the whole way through?
- Is there no heroic closing shot?
- Has the video been split into segments?
- Is the video being used as the initial test?
- Were only prompts output without calling the available generation tools?

Hard rule:

```text
Facial close-ups are kept to 0.5 seconds or less and serve only to confirm character identity. Do not hold a long gaze. Character recognition should be continuously conveyed through clothing silhouette, weapon, movement style, and the heroic closing shot.
```

---

## 12. SD2.0 Video Generation Hard Rules

All final skill showcase videos use the **SD2.0 video model** by default.

Hard requirements:

```text
Model: SD2.0 video model
Duration: 15 seconds
Generation method: Directly generate the complete 15 seconds in one pass
Forbidden: Segmented generation / multi-segment stitching / storyboard-image auto-generation
Aspect ratio: 16:9 or 21:9
Output quality: Fixed 720p, not 1080p
Sound: Must have sound
Reference image: Use only the character board as the sole character reference anchor
Prerequisite: Must pass the Video Preflight Gate
```

When the Agent has video tools, it must generate the video directly. Only when it has no video tools may it output the final prompt as a fallback.

The final video prompt must explicitly state:

- one continuous 15-second video
- no segmented generation
- SD2.0 video model
- 16:9 or 21:9
- fixed 720p output, not 1080p
- with sound
- character board as the only reference anchor

---

## 13. Final Default Output Format

### 12.1 When the Agent Auto-Runs

```text
【Execution Status】
Current stage:
Assets generated:
Next action:
Blocking points: None / Yes

【Character Assets】
MJ character concept image: Generated / Pending / Reworked
Image model character board: Generated / Pending / Reworked

【Preflight Result】
Pass / Blocked

【Final Video】
SD2.0 15-second video: Generated / Not generated
Video settings: 15s / 16:9 or 21:9 / fixed 720p / with sound / one pass

【Failure Risks and Rework】
```

### 12.2 When Tools Are Unavailable (Fallback)

```text
【Current Limitation】
The current Agent cannot directly call the corresponding generation tools, so copyable prompts are being output.

【MJ Character Concept Prompt】
【Image Model Character Board Prompt】
【Video Preflight Gate】
【SD2.0 Video Prompt】
```

---

## 14. Key Document Index

```text
references/agent-auto-run-workflow.md
references/tool-execution-policy.md
references/image-model-character-board-generation.md
references/auto-run-asset-handoff.md
references/role-archetype-library.md
references/role-understanding-engine.md
references/skill-dynamics-library.md
references/weapon-medium-binding-library.md
references/anti-template-checker.md
references/mj-common-error-repair-library.md
references/video-preflight-gate.md
references/skill-causality-chain.md
references/weapon-dominance-check.md
references/three-success-frames.md
references/failure-risk-prediction.md
references/sd2-video-production-workflow.md
references/low-cost-validation-workflow.md

templates/mj-character-concept-template.md
templates/image-model-character-board-template.md
templates/character-board-from-mj-template.md
templates/skill-preflight-template.md
templates/three-success-frames-template.md
templates/sss-skill-prompt-template.md
templates/sd2-video-final-template.md
templates/agent-auto-run-status-template.md
templates/full-auto-user-command.md
templates/repair-prompt-template.md

examples/agent-auto-run-example.md
examples/no-character-to-sd2-video-example.md
examples/tailor-preflight-example.md
examples/tailor-final-video-example.md

evals/qa-scorecard.md
```

---

## 4. Video Prompt Language and Density Hard Rules

V0.6.2 adds a new hard rule: when the Agent auto-runs, the final video prompt must not be compressed into short English phrases.

### 4.1 Default Language

The final SD2.0 video prompt uses a **full-structure Chinese prompt** by default.

A small number of English technical terms may be kept, for example:

```text
cinematic realism, PBR, 0.25x slow motion, one continuous 15-second video, no segmented generation
```

However, the full video prompt must not be rewritten as a short English caption.

### 4.2 When a Tool Prefers English

If a video tool mandates or clearly prefers English, the Agent must perform a **full-structure translation**, not a summary compression.

Wrong approach:

```text
A powerful warrior strikes the ground with a hammer, cinematic, epic, 15 seconds.
```

Correct approach:

```text
Fully retain the character anchor, weapon lock, skill causality chain, 15-second timeline, camera work, physical feedback, sound, and negative constraints, then translate the whole prompt into English.
```

### 4.3 Minimum Density of the Final Video Prompt

The final SD2.0 video prompt must contain no fewer than the following structures:

```text
【Character Board Sole Anchor】
【Video Goal】
【Character and Weapon Lock】
【Character Personality Anchor】
【Current Emotional State】
【Performance Micro-Instructions】
【15-Second Emotional Arc】
【Skill Core】
【Skill Causality Chain】
【3 Success Frames That Must Appear】
【15-Second Timeline】
【Camera Language】
【Physical Feedback】
【Sound Design】
【Video Parameters】
【Negative Constraints】
```

If the Agent calls a video tool in auto-run mode, the prompt passed to the tool must be the full production prompt — not a status summary, not a one-line prompt.

### 4.4 Short-Prompt Usage Restrictions

Short prompts may only be used for:

- When the user explicitly asks for "the short version"
- Quick direction previews
- Agent status bar summaries
- File names / task names

Short prompts must not be used for final 15-second video generation.

### 4.5 User-Visible Output vs. Tool Execution Output

The Agent may give the user a brief status in chat, for example:

```text
Preflight passed. Now generating the 15-second video with the full Chinese-structure prompt.
```

However, the internal video prompt passed to SD2.0 must be complete, structured, and include the timeline and constraints.

For the full templates, see:

```text
templates/sd2-full-video-prompt-template.md
references/prompt-language-density-control.md
references/video-resolution-lock.md
```

### V0.7 Newly Added / Merged Documents

```text
references/prompt-language-density-control.md
references/character-personality-and-emotion-system.md
references/video-resolution-lock.md
templates/personality-emotion-preflight-template.md
templates/sd2-full-video-prompt-template.md
```