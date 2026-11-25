---
name: episodic-series-writer
description: "Multi-episode series scriptwriting: multi-episode arc budgeting with full-pipeline series scripts"
---

# episodic-series-writer

A complete writing methodology for multi-episode series. **A feature film's arc is one complete journey; a series' arc is budget-based** — the amount of character change across N episodes must be allocated across the individual episodes, kept under "budget control". This skill is self-contained and does not depend on any other files in this library; if you need to specify "the criteria for judging which genre's specific content this series should tell — male-oriented / mystery / revenge", you may additionally consult the corresponding genre shell after writing is complete, but a genre shell is not a required prerequisite.

## Boundaries: What It Does Not Do

It does not produce shot lists, shot numbers, shot sizes/camera moves/composition, transition types, AI image/video generation prompts, or format constraints for any specific generation engine. Output stops at a complete written screenplay that can be read directly and shot directly.

## Workflow Discipline

Execute strictly in step order without skipping steps; after each step is completed, pause and wait for the user's [approve/revise/self-check] instruction; never generate all remaining steps in one go before handing them over to the user; after each step, remind the user that they may request a [self-check].

Self-check is an internal process — before writing, mentally run through that step's checklist; there is no need to show the self-check reasoning in the output, only to ensure the delivered content has already passed the checks. The user may still proactively request a [self-check]; only then do the check items need to be explicitly listed one by one, with evaluation results given.

## Writing Red Lines (Globally Highest Priority; No Format May Violate Them)

**Never**: write psychological description ("he realized", "she understood", "something surged up inside"); write parenthetical hints ("(actually concealing nervousness)"); have characters explain worldbuilding or themes through dialogue; preachy passages, forced tear-jerkers, sentimental monologues; over-metaphorical sentences, analogies, bookish AI-flavored dialogue; write anything a camera cannot capture.

**Always**: make dialogue colloquial, like real people talking; replace explanation with action (action is subtext); make dialogue an iceberg showing only the tip; approach all content from an audiovisual perspective.

## Audiovisual Writing Core

**Show, Don't Tell**: if an emotion cannot be conveyed to the audience through a character's physical behavior, that emotion should not appear in the script. **Subtext**: dialogue is an iceberg — avoid being explicit; use action/pauses/evasion/topic shifts to express the true meaning. **Dialogue style**: colloquial, with each character having a distinct way of speaking (word choice, sentence length, habitual expressions) — series have many characters appearing over long stretches, so the distinctiveness of dialogue style matters more than in other formats; the audience should be able to tell who is speaking even with the names covered; avoid over-metaphor and bookish AI-flavored language; never let characters say things both parties already know.

**Standard screenplay format**:
```
[Scene X: Location / Time / Brief visual description]

Action/visual description written directly between lines of dialogue, with no labels, only what a camera can capture.

Character A: xxxxxxxxx.
```
`[Scene heading]` marks location/time/key visual information in square brackets; `Character name:` is followed directly by dialogue; `Character name (OS):` indicates inner monologue/voiceover; action/visual description carries no label and is written directly between lines of dialogue.

## Core Characteristics

- **Episode count and runtime**: defined by the user (common configs: 8-24 episodes, 10-60 minutes each)
- **Characters**: full Ghost/Lie/Flaw/Want/Need, with the arc distributed across the whole season
- **Structure**: two nested layers — intra-episode structure + season arc
- **Worldbuilding**: complex and released in layers; requires information management
- **Pacing**: each episode independently compelling + inter-episode hooks + season-level progression
- **Memory**: requires a continuity management system

## Character Depth Design (Same Depth as a Feature Film)

**Ghost (backstory trauma)**: events from the character's past that shaped their current worldview and behavior patterns. **Lie (the lie the character believes)**: the false belief about themselves/the world that the character formed because of the Ghost. **Flaw (character flaw)**: the concrete behavioral manifestation of the Lie. **Want vs Need**: Want is the goal that drives action, what the character actively pursues; Need is the soul-gap the character has not yet recognized. **Ghost→Lie→Flaw→Want→Need causal chain**: when writing character bios, you should be able to derive step by step along this chain.

**Key difference between series and features**: a feature's arc is one complete journey; a series' arc is **budget-based** — the amount of character change across N episodes must be allocated across the individual episodes; early episodes must not let the character change too much, or there is no room left later. A feature's world can be built in one go; a series' world must be **released in installments** — the first few episodes show only surface rules, the middle reveals the operating logic, and the season finale exposes the underlying truth; when writing Episode 1 you must already know what the final episode will reveal. A feature is one story; a series is a bigger story made of N stories — every episode, pulled out on its own, must be an independently good micro-story (standalone quality), while also laying bricks for the season's big arc (continuity); when the two conflict, **a good single episode takes priority**.

---

## First: Confirm the Series Configuration

Before starting creative work, confirm the following parameters with the user:
```
Series configuration sheet:
- Total episodes: __
- Runtime per episode: __ minutes
- Intra-episode structure preference: Four-part / Save the Cat (compressed) / Story Circle / Internal Beats
- Series type: Anthology (independent story per episode) / Serial (one big story told across episodes) / Hybrid (standalone stories + a continuous hidden thread)
- Season arc: yes / no (a pure anthology may have none)
- Worldbuilding complexity: simple (plug-and-play) / medium (needs layering) / complex (needs an information-release schedule)
```
Once the configuration is confirmed, the episode counts and time allocations in all templates below adapt automatically; "N" below stands for the total episode count set by the user.

## Series Types and Structural Strategy

Different types weight "per-episode independence" vs. "season continuity" differently:

| Type | Per-Episode Independence | Season Continuity | Reference Works |
|------|-----------|-----------|-----------|
| Pure anthology | 100% | 0-10% (minor character growth) | Black Mirror, Tales of the Unusual |
| Anthology + hidden thread | 70-80% | 20-30% (hidden-thread advancement) | Love, Death & Robots, Addressee Unknown |
| Semi-serialized | 40-60% | 40-60% (standalone events within episodes but serving the main line) | Breaking Bad, Stranger Things |
| Heavily serialized | 10-20% | 80-90% (each episode is one chapter of a big story) | Game of Thrones, Attack on Titan |

Depending on the type the user chooses, adjust the weights of all subsequent templates — anthologies favor making the current episode shine; serials favor advancing the season arc.

---

## Dual-Layer Structure

### Layer One: Intra-Episode Structure

Choose based on per-episode runtime and preference: short episodes (10-15 minutes) → four-part structure; medium episodes (20-30 minutes) → extended four-part or compressed Save the Cat; long episodes (40-60 minutes) → Save the Cat / Story Circle / McKee all work.

**Four-part intra-episode template (proportionally allocated, adapts to any runtime)**:
```
[Cold open / opening hook (strongly recommended)]
  Every episode needs an opening hook — not just the first one. The cold open is what plays before
  the opening theme; its only job is to make the viewer decide to "keep watching". Strategies:
  - A high-tension scene that throws the viewer straight into the tension (commercial series)
  - A seemingly unrelated, self-contained slice that pays off at the end of the episode (mystery/anthology)
  - Continuation and resolution of the previous episode's cliff-hanger (serial)
  - A highly stylized passage that anchors this episode's emotional tone (art-house series)
  The cold open of Episode 1 carries the heaviest load — simultaneously establishing the worldview,
  the characters, the genre tone, and the seed of the season's core conflict. The first two minutes
  of Episode 1 decide whether the viewer will watch the entire season.

I. Setup (~15% of runtime): this episode's normal state; may continue from the previous episode or jump to a new scene. Inciting incident — the trigger of this episode's core conflict.
II. Development (~40% of runtime): the conflict escalates (at least two escalations). The B Plot is woven through this segment. Seeds of the season's hidden thread are scattered naturally through dialogue and behavior.
III. Climax (~25% of runtime): the peak of this episode's core conflict. The character makes a choice — it should embody or challenge the character's Lie.
IV. Resolution + end-of-episode hook (~20% of runtime): the close of this episode's story, showing "this episode's new normal". End-of-episode hook (cliff-hanger or tease) — plants anticipation for the next episode; it need not be a big suspense — an unsettling detail or an unanswered question will do.
```

### Layer Two: Season Arc

Divided by proportion into four stages:
```
Stage 1: Setup (first 25% of episodes, i.e., E1~E[N×0.25]) — the worldview's surface rules are presented; the protagonist's Want and Lie are clearly established; the core relationship web is fully built; the seed of the season's core conflict is planted.
Stage 2: Development (episodes 25%-65%) — the season's core conflict escalates step by step; the worldview's operating logic is gradually revealed; the protagonist goes through multiple false changes (looks like growth, but the Lie is never truly broken); the B Plots and hidden threads of individual episodes begin to interweave.
Stage 3: Crisis (episodes 65%-85%) — the season's "all is lost" moment; the protagonist faces their own Ghost and Lie; the most important relationship is threatened or breaks.
Stage 4: Climax and Resolution (final 15% of episodes) — the worldview's underlying truth is revealed; the protagonist makes a season-level pivotal choice; the arc is completed and the new normal is shown; the season finale can either fully conclude or leave a hook for the next season.
```

**Proportion adaptation example**:
| Total Episodes | Setup | Development | Crisis | Climax |
|--------|------|------|------|------|
| 8 episodes | E1-2 | E3-5 | E6-7 | E8 |
| 10 episodes | E1-3 | E4-6 | E7-8 | E9-10 |
| 12 episodes | E1-3 | E4-8 | E9-10 | E11-12 |
| 16 episodes | E1-4 | E5-10 | E11-13 | E14-16 |
| 24 episodes | E1-6 | E7-16 | E17-20 | E21-24 |

---

## Arc Budget Allocation

Arcs cannot happen arbitrarily across episodes — you need to plan each episode's "change quota."

```
Character: [Name]
Season arc: from [State A] → to [State B]
Lie: [The lie the character believes]
Total episodes: N

Ep  | Arc Event | Change Direction | Change Magnitude | Cumulative Progress
E1  | [Event] | Lie reinforced | Faint | 0%
... | ... | ... | ... | ...
E[N]| [Event] | Key choice → new normal | Complete | 100%
```

**Proportionality rules**: cumulative progress over the first 25% of episodes must not exceed 15%; include at least one regression after a false change (usually positioned in the 40%-60% range); the 65%-85% range is the acceleration zone (the largest amount of change); not every episode needs an arc event — some episodes can pass without any character change; purely episodic series can downplay or even skip the arc budget, keeping only character state tracking.

## Worldbuilding Information Release Schedule

```
Info Layer | Content | Release Point (by proportion) | Release Method
Surface rules | [How the world basically works] | First 10-15% (E1-E2 range) | Shown directly
Surface details | [Interesting extensions of the rules] | 15-30% | Character encounters / B Plot
Operating logic | [Why the world is the way it is] | 40-55% | Character investigation/discovery
Logical extensions | [Deeper implications of the logic] | 55-75% | Leaked through relationship dialogue
Underlying truth | [The ultimate truth of the world] | Final 20% | Revealed at the climax
Foreshadowing payoff | [Earlier details take on new meaning] | Final 1-2 episodes | Audience realization
```
**Principles**: each layer of information requires at least 1-2 episodes of foreshadowing groundwork before its release; information is delivered through character actions and discoveries, not through narration or subtitles; releasing new information must change the audience's understanding of what they already know; don't release too much new information in a single episode — at most one new layer per episode.

---

## Essential Series Elements (Included by Default Unless the User Specifies Otherwise)

### Foreshadowing and Payoffs (Cross-Episode Level)

Foreshadowing in a series is more powerful than in a feature — the time span is longer, and when a detail seen in episode 2 pays off in episode 8, the impact is amplified by the wait.

**Classification**: **Intra-episode foreshadowing** (planted and paid off within the same episode — same as in features); **short-range foreshadowing** (paid off across 1-3 episodes; the payoff lands while the audience still remembers, producing a "just as I thought" effect); **long-range foreshadowing** (paid off across 5 or more episodes; the payoff lands after the audience has forgotten, producing a "so it was there from the very beginning..." effect); **season foreshadowing** (planted in episodes 1-2, paid off in the season finale, recontextualizing the whole season — the most powerful foreshadowing of all).

**Density recommendations**: at least 1 intra-episode foreshadowing per episode; at least 1 short-range foreshadowing paying off every 3 episodes; at least 2-3 long-range foreshadowings per season; at least 1 season foreshadowing. Track all foreshadowing in the "Seed Plant/Payoff Registry" (see Continuity Management below).

### Secondary Characters and the Ensemble

Secondary characters in a series are fuller than in features — more runtime means secondary characters don't have to be merely functional; they can have small arcs of their own. **Functions same as features**: mirror characters, catalyst characters, thematic characters, pacing characters.

**Additional series requirements**: important secondary characters should have their own cross-episode micro-arcs (they don't need to be as complete as the protagonist's, but they need perceptible change); a micro-arc should cross the protagonist's arc at some point (influencing each other); each episode may have 1-2 one-off characters (this episode's NPCs), but if an NPC serving the same function recurs across multiple episodes, consider merging them into a recurring secondary character; ensemble shows need a character relationship matrix, updated each episode with the current relationship states.

### Hidden Thread (Series Level)

More complex than in features, because there is more time to plant and reveal. **Quantity recommendation**: 1-3 threads; each must have a clear starting point (which episode begins planting it) and a clear endpoint (which episode reveals it). **Advancement rules**: a hidden thread must not advance in every episode — then it wouldn't be "hidden"; hints should be buried in scenes that "appear to mean something else on the surface"; when the hidden thread surfaces, it should change the audience's understanding of many earlier episodes; manage it with the "Hidden Thread Progress Tracker" (see below).

### Subplot Management (Series Level)

More complex than in features — some subplots run across episodes: **Intra-episode A Plot** (the episode's core story); **Intra-episode B Plot** (the episode's secondary storyline, usually tied to character arcs); **Running Subplot ("runner")** (a continuing storyline spanning multiple episodes — not present in every episode, but the audience remembers it); **Season Arc** (the season's overall story, advanced in fragments each episode).

**Interweaving principles**: each episode's A Plot must be independently complete; the B Plot may take 1-2 episodes to resolve; the Running Subplot advances every 2-3 episodes, and each advance must be substantial enough to matter; Season Arc advancement must not disrupt the current episode's A Plot pacing — when they conflict, cut the Season Arc material; no more than 3 subplots running simultaneously (including the Running Subplot).

---

## Runtime Estimation and Dual-Track Pacing (Series Level)

Each episode's runtime budget should be made as early as the episode-outline stage, allocated according to the four-part proportions, then refined down to the scene level during the scene-breakdown stage.

**Scene annotation format**:
```
[Scene X: Location / Time / Visual description] (approx. X minutes)
  Plot pacing: Loose/Medium/Tight
  Emotional pacing: Light/Medium/Heavy
```

**Intra-episode pacing check**: within a single episode, don't run more than 3 consecutive scenes in the same pacing state; the climax segment (tight plot + heavy emotion) should occupy 20-30% of the episode's total runtime (too short and it doesn't satisfy; too long and the audience tires); every episode needs at least one mismatched segment — "loose plot + heavy emotion" or "tight plot + light emotion" — these are the most flavorful moments.

**Inter-episode pacing check**: is there contrast between the average plot intensity of adjacent episodes (you can't have several high-intensity episodes in a row); is there contrast between the average emotional intensity of adjacent episodes (you can't have several heavy-emotion episodes in a row); are the mid-season "breather episodes" actually "breathing" (both plot and emotion need to come down).

---

## The Four-Piece Continuity Management Toolkit

After finishing each episode, update the following four tracking tables:

**A. Character State Tracking**:
```
Character | State at end of this episode | Key changes | Points to carry into next episode
[Name] | [Physical/emotional/relational state] | [Changes this episode] | [Points the next episode must address]
```

**B. Hidden Thread Progress Tracking**:
```
Hidden thread | Current progress | Advanced this episode | Next advancement plan (which episode)
[Hidden thread 1] | [Progress description] | [What was done this episode] | E[X]
```

**C. Seed Plant/Payoff Registry**:
```
Seed content | Planted in episode | Scene | Planned payoff episode | Payoff method | Paid off?
[Seed description] | E[X] | [Scene number] | E[Y] | [How it pays off] | ✅/❌
```

**D. Revealed Information List**:
```
Information | Episode revealed | How revealed | Who knows (at the character level) | Who doesn't know
[Information] | E[X] | [Shown/hinted] | [Character list] | [Character list]
```

**Usage instructions**: update all four tables immediately after each episode's script is completed; consult them to confirm the current state before starting a new episode; if a continuity conflict is found, prioritize revising the new episode's content rather than revising already-finalized old episodes.

---

## Series Workflow (Two Phases)

Series creation happens in two phases: first complete "season planning + episode outlines" to lock in the season's skeleton and each episode's concept; then, episode by episode, enter the eight-step workflow to write each episode's script.

### Phase One: Season Planning and Episode Outlines

Done only once, but it may require multiple rounds of iteration. Goal: before writing the full script for any single episode, get the entire season's skeleton firmly in place.

**Step A: Season Planning**
1. **Confirm series configuration**: episode count, per-episode runtime, series genre (see the configuration table in the first section)
2. **Season premise**: the season's overall story, summed up in one sentence (Logline level)
3. **Season synopsis draft**: a one-page season story summary (300-500 words), giving the user a basic read on the season's direction and tone; it can continue to be revised later
4. **Protagonist's season arc**: from State A to State B, and what the Lie is
5. **Backstory and worldbuilding** (follow the cross-section principle — the world has been running long before the story begins): era background (what era/social environment the story takes place in, and which traits of that era shape the characters); protagonist backstory (each major character's key life events before the story begins, especially the Ghost event); relationship history (the history of the relationships among major characters before the story begins); worldbuilding design (the three-layer model: surface rules/operating logic/underlying truth + information release schedule); cross-section choice (why episode 1 cuts in at this particular moment)
6. **Arc budget allocation**: first draft of the arc budget tables for the protagonist and major supporting characters
7. **Hidden Storyline Planning**: the starting and ending points of cross-episode hidden storylines (if any)

> Please reply "Approved" to move on to the episode outlines, or tell me your revision notes.

**Step B: Episode Outline** — **This is the most critical step in series creation.** Before writing the script for any single episode, first lay out the outlines for all N episodes end to end. Why this must come before the scripts: the episode outline is the "map" — setting off without one means getting lost; only by viewing the whole season at once can you judge whether the pacing waves are reasonable; arc budget consumption can only be verified from a global vantage point; and seed planting and payoffs require coordination between earlier and later episodes — without the full pass, things fall through the cracks.

**Episode Outline Template (fill in one per episode)**:
```
Episode [X]: "Title"

[Episode Core]
  One-line story (this episode's Logline):
  This episode's core dramatic action: goal → obstacle → outcome
  This episode's emotional tone: (Setup / Light / Tension / Breather / Collapse / Climax / …)

[In-Episode Structure Overview] (with runtime budget)
  Cold open / opening hook (approx. X seconds): specific content — would this opening be compelling on its own?
  Setup (approx. X minutes): plot pacing: loose/medium/tight | emotional pacing: light/medium/heavy
  Development (approx. X minutes): obstacle 1 → obstacle 2 → plot pacing: loose/medium/tight | emotional pacing: light/medium/heavy
  Climax (approx. X minutes): plot pacing: loose/medium/tight | emotional pacing: light/medium/heavy
  Resolution + end-of-episode hook (approx. X minutes): plot pacing: loose/medium/tight | emotional pacing: light/medium/heavy

[Season Connections]
  Arc budget consumed: What changed for the characters this episode? What's the cumulative progress?
  Hidden storyline advancement: Which hidden storyline did this episode advance? How?
  Worldbuilding release: Does this episode release a new layer of information?
  Seeds planted: What seeds does this episode plant? Which episode are they slated to pay off in?
  Payoffs: Which earlier seeds does this episode pay off?
  Secondary character dynamics: How did the secondary characters' states change this episode?

[Inter-Episode Relationships]
  Carry-over from the previous episode: What state from the last episode does this one start from?
  Hand-off to the next episode: What does this episode leave for the next one when it ends?
  Pacing contrast with adjacent episodes: this episode's average plot intensity vs. the previous/next episode? This episode's average emotional intensity vs. the previous/next?
```

**Episode Outline Self-Check**: Is each episode's opening hook compelling enough? Does Episode 1's opening establish the worldview, the characters, and the genre tone all at once? With all N episodes of the season laid out end to end, is there a clear four-phase season arc? Do the inter-episode rhythms form waves (the same emotion can't run unbroken)? Do plot intensity and emotional intensity each rise and fall between episodes (no 3 or more consecutive episodes at the same intensity)? Is the arc budget reasonable (no more than 15% consumed in the first 25% of progress)? Is information released in layers (no single dump)? Does each episode's Logline hold up when the episode is pulled out on its own? Are there "breather" episodes that give the audience a rest, with both plot and emotion dialed down? Are no more than 3 hidden storylines/subplots running at the same time? Is the end-of-episode hook a natural extension of the episode's story rather than something forced? Is the season's foreshadowing distributed sensibly (with plants at every level: intra-episode / short-range / long-range / season)? Does each episode's runtime budget add up to match the total per-episode runtime? Does every secondary character have a function, and do the cross-episode characters have micro-arcs?

> Once all the episode outlines are complete, please reply "Approved." We will write the scripts episode by episode starting from Episode 1. You can also ask me to run a [self-check] on the entire outline.

### Phase Two: Episode-by-Episode Scripts (Eight-Step Workflow)

Once the episode outline is approved, go through the eight-step workflow episode by episode. **Note**: For a series, Step 2 (Synopsis) and Step 4 (Backstory & Worldview) have already been completed during Phase One's season planning, so in per-episode writing they are simplified to "confirm against the episode outline" — unless the episode's actual development has drifted from the outline and an update is needed.

**Step 1 (Concept) additional requirements**: The core dramatic action must match what's set in the episode outline; check whether this episode's concept provides pacing contrast with the surrounding episodes.

**Step 2 (Synopsis) — confirm against the outline**: Revisit this episode's Logline and structure overview in the episode outline and confirm they still hold; if deviations from the outline in earlier episodes mean adjustments are needed, update this episode's synopsis here.

**Step 3 (Characters) additional requirements**: Tag each secondary character appearing in this episode with their function (mirror/catalyst/theme/pacing); for cross-episode secondary characters, check their micro-arc progress.

**Step 4 (Backstory/Worldview) — confirm against the outline**: Revisit the worldview established in season planning and confirm whether this episode needs to release a new layer of information; if new characters debut this episode, add their backstories.

**Step 5 (Structural Outline) additional requirements**: In-episode structure + end-of-episode hook design; opening hook design — every episode's cold open/first scene must have a sufficiently strong visual hook, and Episode 1's opening carries the heaviest load; note this episode's advancement of any hidden storyline (if any); note this episode's arc budget consumption; check against the episode outline for drift, and if drifted, assess the ripple effects; refine the runtime budget.

**Step 6 (Scene Breakdown) additional requirements**: Tag each scene with its estimated runtime and dual-track pacing state; check intra-episode pacing — are there 3 or more consecutive scenes in the same pacing state; check that scene runtimes add up; **if this episode has more than 6 scenes, trigger an intra-episode memory checkpoint after completing Step 6**.

**Step 7 (Scene Writing) additional requirements**: **During a single episode's writing, trigger an intra-episode memory checkpoint roughly every 6 scenes completed**; while writing, check against the checkpoint to keep things consistent; backstory information should be scattered naturally through dialogue and visual cues.

**Step 8 (Script Doctor) additional requirements**: Continuity audit — check for contradictions with previously completed episodes; update all tracking tables (character states / hidden-storyline progress / planted seeds & payoffs / information already revealed); check whether the end-of-episode hook lands; opening hook quality check — is this episode's cold open gripping enough; foreshadowing audit — has the foreshadowing planted this episode been logged, and has everything due to pay off this episode actually paid off; pacing diagnosis — use the scene runtime totals to check this episode's pacing; secondary character audit; if the episode deviates from the outline, assess the ripple effects; **after this episode is complete, an inter-episode memory checkpoint must be triggered**.

---

## Inter-Episode Pacing Management

An N-episode season can't carry the same emotion every episode — it needs pacing waves.

**Emotional Tone Type Library** (choose one dominant tone per episode from this list; blending is allowed but there should be a clear dominant): Setup (the audience acclimates to the world and meets the characters; typically used in the first few episodes); Light (strong comedic feel, centered on character interactions, builds audience goodwill); Tension (the core conflict escalates, pressure mounts); Breather (pacing slows and character relationships deepen, providing an emotional anchor); Turn (a major event occurs and the landscape changes); Pressure (internal and external pressure keeps tightening with almost no room to breathe); Collapse (all is lost — the lowest point); Darkest Hour (the character confronts the Ghost and the Lie head-on); Counterattack (the character strikes back armed with new understanding); Climax (resolution of the season's core conflict).

**Pacing Wave Principles**: No 3 or more consecutive episodes on the same tone; after a Tension/Pressure episode there must be at least 1 Breather or Light episode; Collapse and Darkest Hour may run back to back (forming a "low valley"), but there must be contrast before and after the valley; the season's midpoint (the 40%-60% position) is well suited for a Turn episode — it changes the direction of the second half of the season; a Breather episode is not a filler episode — its function is to deepen character relationships and move the B Plot forward.

**Reference Pacing Template (as a proportion of total episodes)**:
```
First 10%: Setup
10-20%: Light / Setup
20-30%: First Tension
30-40%: Breather
40-50%: Turn (mid-season major event)
50-60%: Transition + escalation
60-70%: Pressure
70-75%: Breather or false climax
75-85%: Collapse / Darkest Hour
85-95%: Counterattack
Final 5-10%: Climax + denouement
```
The above is only a reference; the actual pacing should be adjusted to fit the story itself — the key is creating rises and falls in emotion.

---

## Memory Checkpoint System

A full season can run past 100,000 characters; checkpoints prevent contradictions between earlier and later material by periodically generating structured "snapshots." There are two tiers:

**Inter-Episode Checkpoint (triggered after each completed episode; the most important)** — adds the following on top of the generic template:
```
[Episode Completion Summary] This episode's Logline / this episode's core events / this episode's arc budget consumed: What changed for the characters? Cumulative progress?
[Continuity Tracking Update] Character state changes (compared with the previous episode) / hidden storyline advancement (what this episode advanced) / newly planted seeds / seeds paid off / newly revealed information
[Season Progress] Which of the season's four phases are we currently in? How much of the arc budget has been consumed? What is the core of the next episode's outline?
```

**Intra-Episode Checkpoint (triggered when a single episode's content runs long, i.e., more than 6 scenes)**: the generic template works as-is; the focus is on recording the character states and active threads within this episode:
```
📌 Memory Checkpoint | Series | [Current Position]
[Progress So Far] Which step we're currently on / which scene of this episode we've written up to
[Story Core (unchanged)] Logline / core dramatic action: goal → obstacle
[Character Current State] [Character name]: physical state / emotional state / what they currently know / what they currently want
[Completed Sections Summary] Scene 1: one-line summary + core value shift; …
[Active Threads] Threads that need follow-up later, and their status
[Foreshadowing Status] Planted, not yet paid off: [content] → planned payoff at [location]; paid off: [content]✅
[Pacing Status] Previous section's plot/emotional pacing → suggested direction for the next section
[Up Next] What the next scene to write is, and what its core dramatic action is
```

**How to use**: While writing, review the most recent checkpoint before starting each new section; when resuming across conversations, ask the user for the last checkpoint's contents to restore context; during the Script Doctor pass, string all the checkpoints together and read through them to quickly spot a plant that never got paid off, a character state that jumps abruptly (a continuity error), pacing that hasn't changed for a long stretch, or a hidden storyline/Subplot that hasn't advanced in a long time.

## Cross-Format Techniques (What Series Can Borrow)
**Borrowed from concept films**: The high-concept flip can be used in a series' cold opens / end-of-episode hooks — can the final second of the scene make the audience re-understand the first second of that scene? The progressive-collapse structure can be used in segments showing "a character trapped in a repeating pattern" — the same morning, the same argument, the same failure; the loop itself is the narrative. Split screen, from the audiovisual-language arsenal, can be used in a series' recap segments; jump-cut montage can be used in time-passage segments; picture-sound disjunction can be used in scenes that call for an ironic effect; silence can be used after the climax segment that follows a high-density stream of information; color restriction can be used to mark narrative layers in specific segments (memories in desaturated tones, fantasies in high saturation, reality in natural tones).

**Borrowed from short films**: Information-density montage can be used in time-passage segments showing a character adapting to a new situation; single-variable extreme extrapolation is especially suited to "bottle episodes" (limited space and cast, taking one facet of a complex story and reducing it to a single variable for extrapolation); zero-degree expression (the bigger the disaster, the flatter the tone) works well in collapse episodes.

**Borrowed from feature films**: McKee's value-shift test can be used in the script-doctoring stage — check whether the core value at the end of each scene differs from where it began; scenes with no value shift should be considered for deletion.

## Common Series Pitfalls

- ❌ Skipping the per-episode outline and writing individual episodes directly → You must work through the full season before starting to write
- ❌ Sacrificing individual-episode quality for the season arc → Every episode must hold up when pulled out on its own
- ❌ Releasing information too fast (dumping the whole worldview in the first few episodes) → Release it in layers
- ❌ Arc budget overrun (characters change too much in the early episodes, leaving nowhere to go later) → Strictly follow the budget ratios
- ❌ Continuity errors (character behavior contradicting earlier episodes) → Check the tracking sheet before writing each episode
- ❌ Overly forced end-of-episode hooks (manufacturing conflict just for suspense) → The hook should be a natural extension of the episode's story
- ❌ Episodes with structures that are too similar (the audience can predict the rhythm) → Use inter-episode rhythm management to create variation
- ❌ Too many Running Subplots for the audience to keep track of → No more than 3 running at the same time
- ❌ Per-episode outlines that are only a one-sentence summary → An outline must include a complete in-episode structure summary, a runtime budget, dual-track pacing, and season connections
- ❌ Deviating from the outline while writing an episode without updating the later episodes → Any deviation requires evaluating the knock-on effects on subsequent episodes
- ❌ Not estimating runtime, so the climax gets compressed or the setup runs too long → Start runtime budgeting at the per-episode-outline stage
- ❌ Several consecutive episodes of high-intensity plot + heavy emotion → Audiences will fatigue; use dual-track pacing to check episode-to-episode contrast
- ❌ Planting setups and forgetting to pay them off → Audit them one by one against the plant/payoff registry
- ❌ Supporting characters who appear only when needed and vanish when not → Supporting characters also need their own logic for existing
- ❌ Plot pacing and emotional pacing always in sync → Deliberately misaligning them (loose plot + heavy emotion) is an advanced technique

## Relationship to the Genre-Shell Skill

This skill only governs "how to write at the scale of a multi-episode series"; it does not govern "the specific criteria for deciding which genre — male-oriented, suspense, or revenge — this story should be told in." If you need genre-specific judgment criteria, you can, after finishing the per-episode outline, separately consult the technical-difficulty checklist of the corresponding genre-shell skill in this library; you can also perfectly well complete an entire series independently without consulting it. The two are orthogonal axes, not a dependency.