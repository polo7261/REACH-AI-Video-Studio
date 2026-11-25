---
name: micro-expression-analyst
description: "Micro-expression emotion control: say goodbye to stiff, awkward acting with precise micro-expression mastery"
---

---
name: micro-expression-control
namespace: reach-industry
title: "Fine-Grained Control of Micro-Expressions and Emotional Acting"
description: "Use for fine-grained control of an actor/character's facial expressions, micro-expressions, and emotional transitions—a Chinese emotion→micro-expression action library (sadness/shock/suppressed crying/restrained anger/remorse/guilt/shame/shyness/restrained love/jealousy/disappointment/relief, etc.), long-take single-expression evolution timeline templates, micro-expression time-anchoring tiers, emotion-blending/subtext-leakage writing techniques, an advanced FACS/AU coding precision layer, genuine-vs-fake smile determination, gaze/shot acting vocabulary, cross-shot emotional continuity, division of labor with lip-sync, and restrained-acting self-checks. Distinct from cinematic-motion-realism (full-body motion realism) and talking-head-director (script/voiceover pacing)—this skill specializes in the face. Used for the visual content field of generate_video_v3."
version: 4
---

# micro-expression-control

Use this skill to write the visual content description for `generate_video_v3` when you need fine-grained control of a character's **expressions, micro-expressions, and emotional transitions**. **The core principle aligns with cinematic-motion-realism but is more specialized: emotions cannot be expressed through abstract words—only through executable facial/body actions.** The model doesn't understand "moving," "heartbroken," or "joyful"; it only understands "drooping eye corners," "a one-sided twitch of the mouth," and "trembling eyelashes."

## Boundaries (when to use this skill vs. related skills)

- Full-body posture/environmental forces/overall realism → cinematic-motion-realism (its "emotional restraint" pillar is a condensed version of this skill; this skill is the expanded deep-dive).
- For an overall Seedance storyboard-narrative solution → seedance-cinematic-drama (its "physiological detail hard gate" references this skill's mapping tables).
- Spoken-script pacing/lines/teleprompter → talking-head-director; **this skill only governs what happens on the face when a line is spoken aloud, not what lines to write**.
- Keeping the same face from drifting across multiple shots → character-consistency; **this skill governs the expressions themselves, not facial-structure/feature consistency**; however, this skill's "expression anchor set" (see below) is an extension of that skill's pose-variation set.

## Two writing layers: Chinese action library (default, primary) vs. FACS/AU coding (advanced precision)

| Layer | How to write it | When to use it |
|---|---|---|
| **Chinese emotion→action library** (default, directly usable) | Use the Chinese micro-expression short phrases in this skill categorized by emotion, splicing them directly into the narrative prompt | The default choice for the vast majority of scenarios—idiomatic, immediately understandable, and not dependent on whether the engine recognizes the codes |
| **FACS/AU coding** (advanced; community-tested as effective but not an official guarantee) | Write action unit numbers into the prompt, e.g. `AU12+AU6`, for cases requiring precisely scheduled multiple beats or where Chinese descriptions keep getting a certain detail ignored | Multi-beat scheduling in monologues, or when cross-model/cross-engine migration calls for a universal numbering system |

The two layers are not mutually exclusive—you can A/B test within the same account to see which achieves a higher hit rate on `generate_video_v3`. **For day-to-day prompt writing, prefer the Chinese action library; FACS/AU is a backup weapon, not a requirement.**

## Emotion→micro-expression action library (core, categorized by emotion)

Each entry is a Chinese short-phrase template that can be spliced directly into a prompt—not everything should be crammed into a single shot. **Per the "restraint self-check" below, keep each shot to 1–2 key actions.** The multiple entries listed under each emotion are synonymous/escalating options to choose from by scenario, not all to be written.

| Emotion | Key actions (pick 1–2) | Example phrase |
|---|---|---|
| Sadness/suppressed crying | Gaze losing focus first, lower eyelids trembling faintly, lips pressing together, breathing turning shallow, tears hanging on the lower lashes without falling | "The gaze loses focus first, then the lower eyelids tremble subtly; the lips slowly press together, breathing turns shallow, and tears hang at the lower lashes yet never quite fall" |
| Holding back sobs (no sound) | Head dropping quickly, lips clamped tightly shut, Adam's apple rolling with effort, breath breaking into tremors, no audible sob | "He quickly lowers his head, lips clamped tightly shut, his Adam's apple rolling once with effort, his breath trembling brokenly—yet no sob escapes" |
| Shock/emotional freeze | Breath stopping abruptly, eyes widening slightly then freezing, pupils dilating faintly, hand frozen mid-air | "Her breath stops abruptly, her hand hangs mid-air, her eyes widen slightly then freeze completely, her pupils faintly dilated" |
| Anger/repression | Gaze going still and sharpening, fewer blinks, jawline tightening, nostrils flaring slightly, fingers silently clamping down on an object | "His gaze suddenly goes still, blinks grow fewer, his jawline tightens, his nostrils flare gently, his fingers silently clamp down on the rim of the cup" |
| Remorse | Gaze avoiding the other person then flitting away, brow creasing inward, words stuck at the lips, outstretched hand frozen mid-air | "He looks at the other person then quickly shifts his gaze away, his brow creasing inward, his lips parting but no words coming out, his outstretched hand suspended mid-air" |
| Guilt | Gaze dodging downward, blinks slowing, mouth corners tensing asymmetrically, shoulders drawing in slightly | "Her gaze dodges downward, her blinks slow, the corners of her mouth tense asymmetrically, her shoulders draw in slightly" |
| Shame | Head bowing lower than the gaze alone, ears and neck flushing red, lips compressing into a thin line, body turning slightly away | "She bows her head, not daring to let her eyes rest on the other person's face, her ears and neck slowly flushing red, her lips tightening into a very thin line" |
| Shyness/heart-flutter | Gaze lifting then darting away, lashes trembling faintly, a smile leaking out past suppression, fingers unconsciously pinching something | "She timidly lifts her gaze for an instant then looks away, her lashes trembling faintly, a hint of a smile escaping despite her efforts to suppress it, her fingers unconsciously pinching her sleeve" |
| Restrained love | Gaze softening first, lingering half a second longer, a smile nearly rising then pressed down, an outstretched hand stopping just short of touch | "His gaze softens first, lingering on her face half a second longer, the corner of his mouth almost lifting before being pressed back down, his outstretched hand stopping just short of her" |
| Jealousy | Looking first at "the third party", mouth corners tightening, a thin and delayed smile, gaze turning back with an edge | "She first looks at the hand resting on the other person's arm, the corners of her mouth tightening slightly, then lifts her eyes to him—her smile paper-thin, her gaze turned sharp" |
| Disappointment | Gaze sinking slowly (not dropping abruptly), a soft sigh through the nose, mouth corners sagging wearily, no further pressing | "Her gaze slowly sinks, a faint breath escapes through her nose, the corners of her mouth sag wearily, her eyes no longer pressing for answers" |
| Relief | A long exhale, jaw and brows releasing, eyes moist but calm, shoulders sinking slightly, a smile appearing only after the tension dissipates | "She lets out a long, slow breath, her tense shoulders fully relaxing, a faint smile surfacing on her face as she lifts her head to gaze into the distance" |
| Exhaustion | Rubbing the temples, leaning against a wall, eyelids sinking, a long exhale, sluggish movements | "He leans against the wall, letting out a long breath, his eyelids drooping heavily" |
| Focus | Brow slightly furrowed, gaze locked on a single point, lips pressed tight, body leaning forward | "Her brow furrows slightly, her gaze locked on a single point on the screen, lips pressed tight, her body leaning forward without her realizing" |
| Hesitation | Mouth opening then closing, gaze wandering, hand hovering mid-air, feet pacing | "He opens his mouth then closes it, his gaze wandering, his hand hanging in mid-air, never coming down" |
| Pleasant surprise | Eyes widening instantly, mouth opening into an O shape, both hands covering the mouth, a smile blooming slowly (not instantly) | "Her eyes widen in an instant, her mouth parting slightly into an O shape, both hands instinctively covering her mouth, a smile slowly blooming across her face" |

> Every example meets the hard requirement of "concrete actions, not emotion adjectives"—whenever phrases like "she is very sad" or "he is furious" appear, replace them directly with action phrases from the table above.

## Long-take single-expression evolution timeline (use when the acting is the content itself)
When the entire shot's content is "a single face performing" (monologue, silent close-up, the climactic shot of an emotional turn), don't write it as one static sentence—use the **time-segmented evolution template** instead, letting the expression transition naturally rather than jumping abruptly:

```

0–2s: \[starting state, usually calm or unaware\] 2–4s: \[the first signal of the emotion beginning, extremely subtle\] 4–6s: \[the emotion is noticeable but still restrained, add 1–2 details\] 6–8s: \[the emotion settles into a stable state, optionally add one physical reaction such as tear streaks/breathing\]

```

Example (suppressed sadness): "0-2s: The character keeps a calm expression, eyes gently lowered, lips naturally relaxed. 2-4s: The emotion begins to shift subtly—the lips slowly and lightly press together, the corners of the mouth start to press down little by little, the gaze turns dejected. 4-6s: The sadness becomes more visible but remains restrained—the brows draw together slightly, the eyes carry grievance and forbearance, the eye rims slightly moist. 6-8s: The character settles into the suppressed-sadness expression—one or two small, natural tear streaks appear on the cheek; no loud crying, no sobbing; the emotion stays quiet and restrained." Throughout, **natural transitions, no sudden changes, no exaggerated crying** are required—this is the core constraint of this template, more important than which specific movements are used.

The same structure can be reused with different emotional skeletons: shock freeze (relaxed face → smile freezes → gaze loses focus → breathing stops → jaw locks); guilt (gaze averts → blinking slows → mouth corners tighten → brow creases inward → head lowers); suppressed anger (still gaze → nostrils flare → jaw clenches → fingers tighten → eyes moisten without blinking). **Keep the camera work extremely minimal when using this shot**: locked-off or an extremely slow push-in, shallow depth of field—don't add complex camera moves or extra body movement to a facial close-up and scatter the focus.

## Time Scales of Micro-Expressions (Different Granularities Call for Different Wording—Don't Mix Them)

- **A fleeting leak (0.25–0.5 seconds)**: a nasal breath, a tightened jaw, a darting glance, a twitching smile—used for the instant signal of "the words weren't spoken but the face spoke first"; write it as "flashes past extremely fast, then recovers/gets covered up."
- **A readable transitional movement (0.5–1 second)**: a change in gaze, a paused blink, tears forming, mouth corners tightening—the transitional granularity of one normal emotional turn.
- **A complete emotional shift (1–1.5 seconds)**: one expression fully replaced by another, e.g., a smile completely fading, a forced composure collapsing.
- **A compound layered expression shift (1.5–2 seconds)**: a transition between two layers of emotion, e.g., warmth turning calculating, a smile turning cold—give enough time for the "mask swap" itself to be clearly seen.

**Always maintain natural transitions—no sudden expression jumps—unless the plot's whole point is the shock of the "sudden face change" itself.**

## Emotional Blending and Subtext Leakage (A More Advanced Technique Than a Single Emotion)

Genuinely dramatic performance is often not a single emotion but **two emotions coexisting on the same face, fighting each other**—the mouth performs one emotion while the eyes leak another, or the body posture contradicts the literal meaning of the line. How to write it: list each emotion's own movements separately, letting the "contradiction" itself become the message; don't try to blend them into a "middle emotion":

- **Forced warmth**: upturned mouth corners carrying a smile + a tightened eye area with pupils that don't relax (fear/tension movements) appearing simultaneously—the audience reads "this smile is being held up."
- **A soft refusal that says no but means otherwise**: the line is a refusal, but the gaze dodges away and secretly looks back, the body doesn't really retreat, a smile pressed down at the mouth corners leaks out—the whole thing conveys "refusing in words, already softening inside," not genuine aversion. **For this kind of contrast performance, keep the intensity in the restrained range (around 3/10) so it doesn't read as real resistance/fear.**
- **Scrutiny turning into cold, knowing clarity**: the smile is drawn away bit by bit from the eyes, the gaze darkens, the upturned curve of the mouth slowly flattens or even inverts—the effect of the true nature "peeling away" from the friendly performance; don't do it in one step—give the "drawing away" process time.

This is an advanced version of the "genuine vs. fake smile test" (next section): not one emotion first and then another, but **two emotions layered on the same face at the same time, or one layer of expression slowly surfacing beneath another**. Suited to subtext scenarios like "words not matching the heart," "hanging on desperately," "disguise with ulterior motives."

## Genuine Smile vs. Fake Smile: A Test Demonstration (Applicable to Other Emotions)

A genuine smile necessarily engages the eye area (cheeks lifted by the smile, fine lines appearing at the eye corners); only upturned mouth corners with a still eye area = polite smile/perfunctory smile/fake smile. The muscles around the eyes are nearly impossible to control consciously—this is the hardest line for judging "whether the performance is real," and it doubles as the demonstration template for judging all other emotions—**for any emotion, ask: are the eyes involved, not just the mouth or the brows.** Expressions described only through mouth movements are the most common source of the "fake-face feel" in AI generation.

## FACS/AU Coding (An Advanced Fine-Control Layer—Use for Multi-Beat Monologues or When a Numbered System Is Needed)

When you want to choreograph a multi-beat expression more precisely by "muscle unit," or when the engine keeps ignoring a certain detail in your written descriptions, switch to the AU numbering of FACS (the Facial Action Coding System). Which muscle each AU maps to is stable, established science; but "writing the numbers directly into the prompt text actually works" is a community-tested conclusion, not an official engine guarantee—don't promise users that "writing the numbers makes it precise."

| Emotion | Core AU Combination |
|---|---|
| Genuine smile (Duchenne) | AU6 (cheek raise) + AU12 (lip corner pull up) |
| Polite fake smile | AU12 only, no AU6 |
| Sadness | AU1 (inner brow raise) + AU4 (brow lower) + AU15 (lip corner depress) |
| Anger | AU4+AU5+AU7+AU23 (brow lower + eyelid tighten + lip tighten) |
| Surprise | AU1+AU2+AU5+AU26 (both brows raise + eyelids fully open + jaw drop) |
| Fear | AU1+AU2+AU4+AU5+AU7+AU20 | 
| Disgust | AU9+AU15+AU16 (nose wrinkle + lip corner depress + lower lip pressed back) |
| Contempt (the only unilateral universal expression) | AU12+AU14, one side only—bilateral symmetry is not contempt |

Multi-beat scheduling structure for a monologue (max 3–4 beats per shot; the more beats, the lower each beat's precision):

```

Beat 1 (0–Xs): \[AU combination or plain-language action\] — (optional) paired with the line "..." Beat 2 (X–Ys): \[AU combination or plain-language action\] Beat 3 (Y–Zs): \[AU combination or plain-language action\]

```

The beat durations must sum to the shot's total length; these are **expression changes within the same shot, not shot-to-shot cuts**—keep the camera to a single motion, or the engine will interpret the beat list as multiple shots.

## Gaze Vocabulary (The Strongest Performance Signal—Handle It on Its Own)

- **Gaze direction is narrative**: looking straight into the lens = confession/defiance; gaze slightly below the lens = vulnerability/avoidance; gaze passing the lens toward off-screen space = distraction/reminiscence. Write clearly where the character is looking, not "looking tenderly."
- **Blink rate**: once every 3–4 seconds in normal conversation rhythm; the rate speeds up or drops sharply when nervous/lying/emotionally turbulent (e.g., in restrained anger it can actually "decrease"); in extreme calm or focus, long stretches without blinking.
- **Averting, then glancing back, is the most commonly used signal combination**: writing "the gaze darts away for half a second, then secretly returns" is far more specific than "wandering eyes"; it applies to a wide range of scenarios—shyness, jealousy, saying one thing while meaning another.
- **A dedicated technique for speaking to camera** (digital-human/on-camera delivery scenarios; connects with talking-head-director): live actors speaking to camera often "lock their gaze on the line running from the earlobe to the lens" to prevent wandering, while sweeping the lens with peripheral vision to create a "virtual eye contact" feel; you can borrow this concrete action directly in the prompt—it's more controllable than "looking at the camera."

## Cross-Shot Emotional Continuity + Expression Anchor Set (Extends character-consistency)

The same character's emotion across consecutive shots must have cause and effect—no abrupt emotional shifts between shots: **the previous shot's expression "residue" must be carried into the start of the next shot** (e.g., if the previous shot ends with "eye rims slightly red, tears not yet fallen," the next shot should open with "still carrying the un-faded redness around the eyes" rather than resetting to a calm face).
**Expression anchor set**: character-consistency's "pose variation set" by default only varies angle/pose. If the same character needs to **precisely reproduce a few specific expressions** (not a natural emotional flow) across multiple shots, you can additionally generate a set of "expression anchor images" — using the same character anchor, varying only the expression (e.g., "neutral relaxed," "natural smile," "focused serious," or pick 3–6 expressions the scene needs from this skill's action library), then later shots reference the corresponding anchor image. It is only worth doing when you need to repeatedly and precisely reproduce the same few specific expressions (fixed expression packs for virtual streamers, a recurring "signature wry smile"); one-off / naturally flowing emotions don't need it.

The technical implementation of a consistent face across shots (no drift) goes through character-consistency's anchor mechanism; this skill only governs whether emotional continuity/reproduction lands properly.

## Division of labor and synergy with lip-sync

The emotional tone of dialogue must match the micro-expressions on the face, otherwise you get a disjointed "mouth smiling while the eyes play a different emotion" feel (unless that is exactly the "emotional blending" effect you want). **Division-of-labor principle**: dialogue voicing/lip-sync drives the lips/jaw opening and closing with phonemes; this skill's expression descriptions should **land preferentially on the eyebrows/eye area/cheeks** — muscles not directly involved in articulation — and not grab the same muscles. If you genuinely need to control expressive mouth movements (e.g., a suppressed smile constantly lingering at the mouth corners while speaking), write it as "an expression layer stacked on top of articulation," not as a replacement for the lip shape.

What dialogue actors actually do on camera is focus their attention on the **subtext** of the lines rather than the literal expression — first determine what the character truly wants / is hiding, then derive the micro-expressions backward from the subtext, rather than mapping directly from the literal emotion of the line (this is exactly the use case of the "emotional blending" section).

## Prompt assembly formula
```

\[Starting/base state\] + \[Trigger or cause, one sentence\] + \[1–2 key micro-expression actions, picked from the action library\] + \[Gaze direction and eye action\] + \[Body/breathing-type reactions, if any\] + \[Restraint-level cues: e.g., "no tears," "no gritted teeth," "extremely small movement amplitude"\]

```
Write the whole sentence into the character action/expression part of the `generate_video_v3` visual content field; splice it into the same narrative-flow sentence as the body-movement and environmental-force descriptions (cinematic-motion-realism), rather than splitting it off into a label-style "Expression: xxx" format. For long takes where performance is the content itself, switch to the time-segmented evolution template above; for multi-beat monologues, switch to the FACS/AU scheduling structure.

## Restraint self-check (overacting vs. hitting the mark)

- Keep only 1–2 key actions per shot; more than that is padding and will read as "trying too hard."
- Multi-beat monologues should have at most 3–4 beats; the more beats, the worse the precision of each beat.
- Expressions perfectly symmetric on both sides of the face (except a momentary flash of pure surprise) are mostly unrealistic — it is fine to write "one-sided" or "slightly skewed"; contempt is inherently one-sided.
- There should be a delay between the trigger and the action (0.3–1 second); zero-delay "switches expression the instant he hears it" reads most as AI-like; emotions must **transition naturally**, sudden jumps are forbidden (unless the plot calls for the impact of a "sudden face change").
- The eyes must participate in the emotion; expressions where only the mouth moves are the most common failure mode.
- Stage-style exaggeration (big sweeping movements, maxing out the whole face) is for theater audiences watching from a distance; on-camera performance should be dialed back — **the camera sees details theater audiences cannot, so smaller movements suffice on camera**.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Digital human looks like a wax figure / face slack | Only dialogue written, no expression | Add at least 1 base-state action, even just "calm focus" |
| Expression exaggerated/distorted, like pantomime | Used exaggerated verbs like "laughing wildly," "sobbing," "glaring furiously" | Swap in restrained actions from the action library |
| Fake-smile/plastic feel | Only mouth actions written | Add a line of eye-area action; refer to the genuine-vs-fake smile test |
| Long-take expression evolution muddy/changes invisible | Only one static sentence for the whole segment | Switch to the time-segmented evolution template, progressing across 4 time segments |
| Expression should change during the monologue but doesn't | No beats, whole passage glossed over in one sentence | Switch to FACS/AU or Chinese action-library beat scheduling, ≤4 beats |
| Engine keeps ignoring a certain detail in the Chinese description | That detail carries too little weight in natural language | Retry with FACS/AU encoding, A/B compare on the same account |
| Emotional shift too abrupt | No transition segment between two expressions | Add a transitional action; pick the corresponding granularity per "the time scale of micro-expressions" |
| Hollow/lifeless eyes | Only mouth/eyebrows described | Add a dedicated line of gaze vocabulary |
| Eyes wander when speaking to camera | No concrete gaze-lock action given | Replace "look at the camera" with a concrete description like "locked on the earlobe-to-camera line" |
| Expression and lip shape fight each other while speaking | Expression description grabbed the mouth/jaw muscles, conflicting with lip-sync | Move the expression description to brows/eyes/cheeks, leave the mouth to lip-sync |
| Expression mismatches the line's emotion (unintentional) | Mapped the expression directly from the literal wording of the line | Think subtext first, then set the expression |
| Emotion seems reset across shots | Each shot's emotion written independently without carrying over the previous shot's residue | Carry the previous shot's ending state as this shot's opening |
| "Leaked emotion" effect not visible | Wrote a fleeting signal as a full expression | Change to an extremely fast flash on the order of 0.25–0.5 seconds |
| Need to reproduce the same expression precisely and repeatedly, but it always drifts | Only a character identity anchor, no expression anchor | Add an "expression anchor set" |

## Related

Full-body motion realism → cinematic-motion-realism; Seedance overall storyboard solution → seedance-cinematic-drama; spoken-script/line pacing → talking-head-director; drift-free cross-shot face/expression anchor sets → character-consistency; camera-movement vocabulary/time-anchoring techniques → cinematic-motion-language.

> The Chinese emotion action library and long-take evolution template are adapted from a community solution found directly via a GitHub search (CyberJ0605/cinematic-video-prompt-engineer-skill, 54★, MIT, with field-tested demo videos); the FACS/AU encoding layer is adapted from another community solution (the higgsfield-facs sub-skill of OSideMedia/higgsfield-ai-prompt-skill, 191★, MIT). Both are rewritten to match the actual field structure of generate_video_v3 in this environment; the star counts only reflect a snapshot from when I searched and do not indicate which solution is superior — the former's Chinese actions are more idiomatic, the latter's numbering system is better suited to precise scheduling; they complement, not replace, each other.
```