---
name: short-film-writer
description: "Narrative short film script writing: a short film script driven by a single event from start to finish."
---

# short-film-writer

A complete writing methodology for 5-10 minute narrative short films. A short film is a **sprint** that wins through information density—every scene must advance the plot or reveal character; there is no room for idle strokes. This skill is self-contained and does not depend on any other files in this repository; if you want to specify "the specific criteria for judging which genre this short film should be—male-oriented/mystery/revenge", you may additionally consult the corresponding genre shell after writing is complete, but the genre shell is not a required prerequisite.

## Boundaries: What Not to Do

Does not produce storyboards, shot numbers, shot sizes/camera movements/composition, transition types, AI image/video generation prompts, or format constraints of any specific generation engine. Output stops at a complete written script that can be read and shot directly.

## Workflow Discipline

Execute strictly in step order without skipping steps; pause after each step is completed and wait for the user's [approve/revise/self-check] instruction; never generate all subsequent steps in one go before handing them to the user; after each step, remind the user that they may request a [self-check].

The self-check is an internal process—before writing, mentally run through the checklist for the corresponding step; there is no need to show the self-check reasoning in the output, only to ensure the delivered content has passed the checks. The user may still proactively request a [self-check]; only then do the check items need to be explicitly listed one by one with assessment results given.

## Writing Red Lines (Highest Global Priority; No Format May Violate Them)

**Absolutely never**: write psychological description ("he realized", "she understood", "a feeling welled up inside"); write parenthetical hints ("(actually concealing nervousness)"); have characters explain the setting or theme through dialogue; preachy passages, forced tear-jerking, sentimental monologues; over-metaphorical sentences, analogies, bookish AI-flavored dialogue; write anything the camera cannot capture.

**Must do**: dialogue must be colloquial, like real people talking; use action in place of explanation (action is subtext); dialogue like an iceberg, revealing only the tip; approach all content from an audiovisual perspective.

## Core of Audiovisual Writing

**Show, Don't Tell**: Psychological description is strictly forbidden; write only actions that can be seen and sounds that can be heard. If an emotion cannot be conveyed to the audience through a character's physical behavior, it should not appear in the script. Wrong example: "He finally understood his father's painstaking care." Correct approach: He stands there watching for a moment, then takes off his coat and lays it over his father.

**Subtext**: Dialogue is an iceberg—what characters say aloud is only the surface; the true meaning lies below the waterline. Avoid on-the-nose dialogue; use action, pauses, evasion, and topic shifts to convey true meaning. On the nose (wrong): "I'm terrified of losing you." Subtext (correct): "Take that coat with you when you go. ...It's cold out there."

**Action as Subtext**: All emotional communication must be capturable on camera. In a good short film, even with all dialogue removed, the audience can still roughly understand what happened.

**Dialogue Style**: Colloquial, with different characters speaking in different ways (word choice, sentence length, habitual expressions); avoid excessive metaphor and bookish AI-flavored speech; don't let characters say things both parties already know.

**Standard Script Format**:
```
【Scene X: Location / Time / Brief visual description】

Action/visual description is written directly between dialogue lines, unmarked—only write what the camera can capture.

Character A: xxxxxxxxx.
Character B: xxxxxxxxx.

Character A doesn't answer. He turns and walks to the window, fingers unconsciously tapping the window frame.

Character A: xxxxxxxxx.
```
The `【Scene label】` uses square brackets to note location/time/key visual information; `Character name:` is followed directly by dialogue; `Character name (OS):` indicates inner monologue/voiceover; action/visual description carries no marker and is written directly between dialogue lines.

## Core Characteristics

- **Duration**: 5-10 minutes
- **Characters**: 1-2 protagonists with a complete Want/Need/Arc
- **Structure**: Four-part (setup→development→climax→resolution), focused on a single core event
- **Arc**: One complete A→B change
- **Worldview**: Concise and clear; the audience understands the rules within 30 seconds
- **Pacing**: High information density; every scene must advance the plot or reveal character

## Core Constraints of the Short Film

A short film allows only one **single core event**—no subplots, no scattered focus. All scenes serve the same dramatic action—the protagonist pursues a goal, encounters obstacles, makes a choice. Unless the user specifically requests otherwise, all settings should take place in a realistic context; overly exaggerated or overly dramatic designs are forbidden.

## Character Design: No Cardboard Cutouts

**External Want vs Internal Need**: Want is the goal that drives the action—something the character is aware of and actively pursues; Need is the soul gap the character has never recognized, usually the deeper cause of the Want. The tension between the two is the engine of the character arc.

**Character Arc**: Arc = an irreversible change from state A to state B. A short film's arc is a one-time leap (A→B); unlike a feature film, it doesn't need to pass through multiple "false changes".

**Character Bio**: Backstory is not background exposition but the root of conflict. Key events should answer: Why does the character have this Want? Why can't the character see their own Need? Where does the character's inner contradiction come from?

**Contradiction**: A good character has at least one layer of contradiction—outward behavior vs inner truth (outwardly confident vs inwardly insecure; outwardly cold vs inwardly craving connection). Contradiction makes a character three-dimensional and gives subtext room to exist.

## Topic Selection Toolkit (For Internal Guidance When the User Has No Clear Idea; Not Shown Directly to the User)

When the user doesn't yet have a clear story concept, don't lay out the methodology below for the user to see; instead, judge through natural conversation which path the user's vague direction belongs to, and guide using the corresponding method.

**Path 1: Start from Theme** (user signals: an abstract proposition/a social issue/"I want to tell a story about XX", e.g., "about memory", "loneliness")—guidance method: help the user convert the abstract theme into concrete dramatic action. "About memory" is not a story; "a person about to lose all memories must choose within 24 hours which one to keep" is a story. Ask: under this theme, what kind of person, in what situation, would be pushed to the point of having no choice but to make a decision?

**Path 2: Start from Character** (user signals: a contradictory personality/"I want to write a person who is XX", e.g., "a swimming coach who is deathly afraid of water")—guidance method: extract dramatic action from the contradictory personality; the contradiction itself is the seed of conflict. Ask: what is this person most afraid of facing? What would happen if he were forced to face the thing he fears most?

**Path 3: Start from Space/Environment** (user signals: a specific location/an enclosed space/a special world, e.g., "an old teahouse", "a train that never stops")—guidance method: space is rules; a special space implies its own operating rules and power structure. Ask: in this space, who is on top and who is on the bottom? What resources are scarce? What behavior is forbidden? The more enclosed the space and the more extreme the rules, the stronger the dramatic tension.

**Path 4: Start from Relationship** (user signals: tension between two people/"I want to write a story between two XX", e.g., "a couple on the verge of divorce")—guidance method: tension in a relationship comes from the two people wanting things that contradict each other. Pin down: what is each person's Want? Why can't both be realized at the same time? In what situation would this contradiction be pushed to its extreme?

**Path 5: Start from Tags/Concept Collision** (user signals: a few keywords/a feeling/"I want to combine XX and XX", e.g., "food delivery rider + imperial examination")—guidance method: collide concepts using five tools: concept grafting (take A's mechanism + B's setting), time-space displacement (put a person/technology/institution into an era and place it doesn't belong to), metaphor made concrete (turn abstract anxiety into physical rules), reversal juxtaposition (put two things that look similar but are actually contradictory into the same scene), and rule inversion (take the opposite of a real-world rule).

**Operating Procedure**: Listen to the user's free expression (even if it's just one word) → determine which path it belongs to (the user doesn't need to know the paths exist) → use the corresponding tools to ask specific, thought-provoking questions to dig deeper (don't ask vague questions like "what are you trying to express") → produce 3-5 concrete options to choose from → don't show the methodology itself; what the user sees is that you "helped them come up with a few good ideas".
When the user has no direction at all, do not present a path menu; use natural conversation to spark ideas: "Is there any recent news/image/something around you that made you feel 'that's just too absurd'?" "If you could turn one rule of reality upside down, which one would you most want to reverse?" "Is there a space that makes you feel 'this place itself is like a story'?" "Are there two seemingly unrelated things that you think would be interesting to put together?"

---

## Complete Eight-Step Workflow

### Step 1: Premise Breakdown and Core Action

**Goal**: Establish the "core" of the short film. If the user already has an idea, use it directly; if not, guide them with the topic-selection toolkit above (do not present the path menu).

**Execution Logic**: Based on user input, brainstorm 3-5 core dramatic actions—dramatic action = Goal + Conflict, and it must be "purposeful pursuit"; ensure the events stay focused and suit the scale of a short film.

**Output Format** (strictly follow this format; do not add unmentioned content such as scenes):
* **Option A/B/C:** Protagonist / Goal (Want) / Obstacle (Conflict) / One-Sentence Story Summary (Logline)

> Please reply "Approved" to proceed to the next step, or tell me your revision suggestions. Or pick an option and ask me to [Self-Check].

**[Self-Check: Core Concept and Dramatic Action]** Is a "goal + conflict" established? Is the goal reasonable and urgent? Is it strongly tied to the obstacle? Are there clear internal/external conflicts? Is the obstacle within a reasonable scale? Is the conflict between goal and obstacle the engine that drives the story?

### Step 2: Synopsis Draft

**Goal**: Let the user form a basic judgment of the overall story direction and tone before going deeper.

**Execution Logic**: Based on the selected option, write a one-paragraph (100-200 words) story synopsis that should cover who the protagonist is, what situation they are in, what event forces them into what predicament, and what ending they ultimately head toward (it can be vague); the synopsis's tone should hint at the film's overall mood—heavy or light, warm or cold.

> This synopsis can continue to be adjusted in later steps. Please reply "Approved" to move on to character design, or tell me your revision suggestions.

**[Self-Check]** Does the synopsis convey the story's core conflict? After reading it, do you have a clear sense of "what kind of story this is"? Does the tone hint at the film's overall mood?

### Step 3: Character Depth and Arc

**Goal**: Reject flat, paper-thin characters and build internal tension within them.

**Execution Logic**: Design the Want vs Need; design the character biography (mining backstory as the root of conflict); design contradictions (outer presentation vs inner truth); unless the user specifically requests it, overly exaggerated designs are forbidden.

**Output Format**: Character [Name] / External Need / Inner Desire / Character Arc (State A → State B) / Key Points of Character Biography / Contradictory Traits (External vs Internal)

> Please reply "Approved" to proceed to the next step, or tell me your revision suggestions. You can also ask me to [Self-Check].

**[Self-Check: Character Building and Arc]** Are the external need and inner desire clear and opposed? Has an irreversible internal change been set up in advance? Does the ending show a "new normal"? Is the character contradictory? Does the behavior follow the logic of the biography?

### Step 4: Backstory and Worldbuilding (Condensed Version for Short Films)

**Goal**: Follow the principle that "film is a cross-section of real life"—the world already existed before the story begins. A short film does not need to build a complete world the way a feature does, but the following information must be clarified (the screenwriter must know it, though it does not all need to be shown to the audience):

**Output Format**: Era/Environmental Background / Key Backstory Events of the Character (before the story begins, what the protagonist experienced that led to the current situation and personality) / Relationship History (if there is an important relationship, what state it was in before the story begins) / Which Cross-Section the Story Cuts Into (why choose to start telling from this moment)

**Note**: Backstory information should be scattered naturally through the script via dialogue and visual clues; do not deliver it through concentrated flashbacks or narration. Avoid flashbacks unless necessary.

> Please reply "Approved" to move on to the structure outline, or tell me your revision suggestions.

### Step 5: Structure Outline

**Goal**: Build the short film's skeleton and ensure progressive pacing.

**Execution Logic**: Use a four-part structure; have only one single core event and avoid subplots; important backstory details from Step 4 must be shown naturally in the first and second acts (avoid flashbacks unless necessary); must include an inciting incident and an "all is lost" moment; the first 15 seconds of the opening must contain a visual hook—the very first image should carry information or suspense; the most effective choice is an everyday image that is "somehow off" (it looks normal, but one detail raises suspicion).

**Output Format**:
* **Act One: Cause** — Opening hook (the image/action of the first 15 seconds) / Setup (showing the story's normal state) / Inciting incident (breaking the balance)
* **Act Two: Development** — Conflict escalation (Obstacle 1) / Further conflict escalation (Obstacle 2, cannot be omitted) / Midpoint (false victory/false defeat) and all is lost
* **Act Three: Climax** — Final confrontation (peak of action) / Key choice and story twist
* **Act Four: Resolution** — New normal (arc completed)

> Please reply "Approved" to proceed to the next step, or tell me your revision suggestions. You can also ask me to [Self-Check].

**[Self-Check: Structure and Pacing]** Does the opening hook grab the audience within the first 15 seconds? Are the four parts clear? Are the inciting incident and the climax clearly defined? Does every part advance the plot or reveal character? Have ineffective plot points been removed? Does Obstacle 2 exist and differ in nature from Obstacle 1 (it cannot be the same resistance rephrased)? Is the time budget for each part reasonable (setup about 15%, development about 40%, climax about 25%, resolution about 20%)?

### Step 6: Scene List

**Goal**: Turn the outline into concrete audiovisual units.

**Execution Logic**: Break down each plot point from Step 5 into one or several core dramatic actions (goal → obstacle → result); ensure each major dramatic action can be broken down into several micro dramatic actions; mark each scene with an estimated duration and a dual-track rhythm state.

**Output Format**: Scene 1... (approx. X seconds) Plot: loose/medium/tight | Emotion: light/medium/heavy; Scene 2...; Cumulative duration: X min X sec / Target total duration: X minutes

> Please reply "Approved" to proceed to the next step, or tell me your revision suggestions. You can also ask me to [Self-Check].

**[Self-Check]** Does every plot point have a specific breakdown? Are the scene connections tight? Is there a plot transition between adjacent scenes? Does the accumulated scene duration match the target total duration? Are there 3 or more consecutive scenes in the same rhythm state (if so, adjust)? Is there at least one misalignment between plot rhythm and emotional rhythm (a more advanced form of storytelling)?

**If the short film's total duration exceeds 8 minutes or there are more than 8 scenes, it is recommended to trigger a memory checkpoint after completing Step 6** (see the "Memory Checkpoint" section below), locking in character states and active threads before moving into writing.

### Step 7: Scene Writing

**Goal**: Fill in the flesh and blood; execute visual writing and subtext. Ask the user to specify which scene number(s) to generate (or all of them).

**Execution Requirements**: Visual writing—psychological description is strictly forbidden; write only actions that can be seen and sounds that can be heard; Subtext—dialogue is like an iceberg; avoid being on-the-nose; use action/pauses/evasion to convey true meaning; output in standard screenplay format.

> Please reply "Approved" to proceed to the next step, or tell me your revision suggestions. You can also ask me to [Self-Check].

**[Self-Check: Scene Writing and Audiovisual Language]** Is there any psychological description (if so, Fail)? Does it tell the story through images? Is the dialogue too on-the-nose? Are subtext and body language used? Is the dialogue conversational?

### Step 8: Script Doctor and Polish

**Goal**: Diagnosis and optimization.

**Execution Logic**: Read through the entire script as a script doctor; look for logic holes, sluggish pacing, and on-the-nose dialogue; provide What-if suggestions for exploring multiple versions; check each scene's time budget—are any scenes much longer/shorter than expected? What is the impact on the overall rhythm?

**Output Format**:
* **Diagnostic Report**: Pacing issues (including dual-track rhythm diagnosis) / Duration issues (which scenes are too long or too short, whether the climax segment's duration is sufficient) / Logic holes / Dialogue issues
* **Optimization Suggestions**: (subtext rewrite for a specific scene, anti-cliché concept for the ending)

**[Comprehensive Self-Check]** Provide final comments and revision suggestions based on the four major areas (core concept, character, structure, audiovisual).

> First draft of the script is complete. Which part would you like to refine?

---

## Dual-Track Rhythm System
Rhythm is not just a single line—there is external plot rhythm (density and intensity of events: tight = high-density events / rapid dialogue / chases / revelations, loose = everyday scenes / moments alone / silence) and internal emotional rhythm (the character's emotional fluctuations: heavy = confession / betrayal / loss / fear / ecstasy, light = teasing banter / casual small talk / quiet companionship). The two tracks can move in sync or out of sync, and the mismatch itself is a powerful narrative tool:

- **Loose plot + heavy emotion**: Two people sit quietly eating a meal, nothing happens, but the audience knows one of them is leaving tomorrow. The calmer the scene, the heavier the emotion.
- **Tight plot + light emotion**: An intense car chase, but the characters are joking and the score is light. Tense events wrapped in a breezy emotional tone.
- **Tight plot + heavy emotion**: The climax—dense events and explosive emotion, the peak of the whole film, and it cannot last too long.
- **Loose plot + light emotion**: A pure breathing scene, letting the audience rest.

During the structural outline and scene breakdown stages, you should draw a "rhythm wave chart" marking the external plot intensity and internal emotional intensity of each segment, and check the contrast between rises and falls. Avoid: both lines sitting low at the same time for too long (the audience has nothing to watch and nothing to feel); both lines sitting high at the same time for too long (audience fatigue; the climax no longer feels special); either line rising monotonically with no fall (no sense of breathing).

## Runtime Estimation Methods

**Dialogue estimation**: 1 page of standard screenplay format ≈ 1 minute of final film. In a Chinese script, roughly 200–250 characters of dialogue + action description ≈ 1 minute.

**Scene estimation rules**: Pure dialogue scenes are estimated by the word count of the dialogue; action/montage scenes are estimated by the number of shots (each individual shot is roughly 3–5 seconds); silence/emotional scenes are easy to underestimate—a character just standing there doing nothing may need 10–15 seconds in the final film to carry enough emotional weight; don't forget to count transitions, usually 2–5 seconds each.

**Scene duration annotation format**:
```
【Scene 3: Hospital corridor / Night / Fluorescent lights buzzing】(approx. 1 min 30 sec)
  Plot rhythm: Medium (one key conversation)
  Emotional rhythm: Heavy (the character faces the truth for the first time)
```

**Reference runtime proportions for the whole short film (8 minutes as an example)**: Setup 1.5 min / first half of Development 2 min / second half of Development 2 min / Climax 1.5 min / Resolution 1 min. You can adjust flexibly in actual practice, but after adjusting you should be aware of what you're doing (e.g., "I'm deliberately giving the Setup 40% of the runtime because this is a slow-burn story").

**Rhythm diagnosis** (script doctor stage): Is the climax long enough? (Too short makes the climax feel compressed.) Is the setup too long? (The audience waits too long before getting to the point.) Is there any single-emotion stretch longer than 3 consecutive minutes? (Whether tense or relaxed, it stops working if it lasts too long.) Is there enough breathing room between the two high-emotion scenes? Does the film's longest single scene have sufficient reason to occupy that much time?

## Memory Checkpoint (for extra-long shorts only; most short films don't need it)

Only needs to be triggered after Step 6 is complete, if the short film's total runtime exceeds 8 minutes or it has more than 8 scenes. The checkpoint is a structured, compressed summary, not a restatement of the full text:

```
📌 Memory Checkpoint | Short film | [Current position]
【Progress so far】Which step we're on / which scene or section has been written up to
【Story core (unchanged)】Logline / core dramatic action: goal → obstacle
【Character current state】[Character name]: physical state / emotional state / what they currently know / what they currently want
【Completed sections summary】Scene 1: one-sentence summary of what happened + core value shift; Scene 2: ...
【Active threads】Threads that need follow-up later, and their status
【Rhythm state】Plot/emotional rhythm of the previous section → suggested direction for the next section
【Upcoming content preview】What the next scene to write is, and what its core dramatic action is
```

## Short Film Rhythm Techniques

**Backstory reveal**: Backstory information should be scattered naturally through dialogue and visual clues; don't deliver it all at once via flashbacks or voiceover.

**Rhythm stretch and rebound**: Stretch—use repeated actions, measured pacing, and static images to build expectation; rebound—break the balance abruptly without warning, using extremely brief audiovisual language to create a rhythmic rupture.

**Ending**: Show the "new normal" after the arc is complete—what the world looks like once the character has changed. No need to explain what the character learned; use one image and let the audience feel it for themselves.

## Cross-Format Technique Borrowing (what short films can borrow)

Short films are small in scale, but they can borrow a few concrete tools from larger or smaller formats and apply them to their own local passages:

**From features**: McKee's value-shift test can be used to check every scene in a short film—is the core value at the end of the scene different from at the start? If a scene ends with no value having changed, consider cutting it; this criterion is more actionable than "this scene feels a bit redundant." If the short film's characters feel "too flat," you can borrow the Ghost/Lie/Flaw way of thinking—no need to develop it fully, just hint that there's an unspoken reason behind the character's behavior; one detail is enough. Foreshadowing/payoff actually has greater impact at the 5–10 minute scale of a short film—because the audience still remembers: an object that casually appears in minute 1 suddenly becomes crucial in minute 8, and the effect is explosive. During the Step 5 structural outline stage, you can proactively design for "is there something that can be planted at the beginning and flipped at the end." If the short film has a secondary character, you can borrow the logic of "the B Story mirrors the theme"—let that secondary character walk the path the protagonist "didn't take," so the secondary character isn't just a plot device but another facet of the theme.

**From concept films**: The high-concept twist idea ("can the last second of a scene make the audience re-understand the first second of that scene") can be applied to a short film's ending to create a punch. The concept-purity test (can it be stated in one sentence; can it be presented visually within 5 seconds) can be used to test the short film's Logline—if it can't be stated clearly in one sentence, the core concept isn't sharp enough yet.

## Common Pitfalls

- ❌ Introducing subplots or multiple core events → a short film can only have one single core event; cut everything that dilutes the focus
- ❌ Obstacle 2 being the same kind of resistance as Obstacle 1, just reworded → you must switch to a different type of obstruction
- ❌ Delivering backstory in concentrated flashbacks or voiceover → scatter it naturally through dialogue and visual clues
- ❌ Using dialogue at the ending to summarize what the character learned → use one concrete image to let the audience feel the "new normal" for themselves
- ❌ Not doing a runtime budget, resulting in a compressed climax or an overlong setup → start annotating durations from Step 5
- ❌ More than 3 consecutive scenes in the same rhythm state → use the dual-track rhythm to check the rises and falls
- ❌ Using the opening to "slowly ease into it" → a short film has no time for warm-up; the first 15 seconds must have a visual hook
- ❌ Designing the character arc as feature-length-style multiple pseudo-changes → a short film's arc is a single jump; don't drag it out

## Relationship to the Genre-Shell Skill

This skill only covers "how to write at the 5–10 minute scale," not the specific criteria for judging "which genre this story should be told in—male-oriented / suspense / revenge." If you need genre-specific criteria, after finishing the outline you can separately consult the "this episode/section is dead" checklist in the corresponding genre-shell skill in this library; you can also perfectly well complete a short film independently without consulting it. The two are orthogonal axes, not a dependency.