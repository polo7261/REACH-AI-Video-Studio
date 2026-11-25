---
name: beauty-blogger-reviewer
description: "Realistic beauty UGC product review: one click turns beauty selling points into visible proof and natural voiceover"
---

# Wander Realistic-Feel Beauty UGC Product Review

## Skill Positioning

Transform user-uploaded skincare, makeup, fragrance, or personal care product photos into a Seedance 2.5 vertical UGC review video that looks like a real creator personally filming it, personally trying the product, and offering limited conclusions.

The final video must satisfy all of the following:

- One clearly adult creator, defaulting to a Chinese/East Asian woman;
- Native phone camera texture, not a studio-shot ad or polished TVC;
- Try first, then observe, and finally give limited conclusions;
- The core selling point the user wants to convey must be preserved, but translated into actions, texture, makeup effects, or immediate impressions—never reading ad copy verbatim;
- Spoken Chinese triggered by in-the-moment touch and observation, retaining pauses, self-correction, and a restrained attitude;
- Product packaging, usage method, person, space, and lighting remain continuous.

Default final video: Seedance 2.5, reference image + text prompt, 24 seconds, 9:16, 720P, single video node, multi-shot timestamps, live sound + light action sounds, no BGM, no random subtitles.

Explicitly excluded:

- High-end commercial TVCs, pure product render films, forced 3×3 commercial storyboard process;
- Livestream selling, recited voiceover, impersonal narration, third-person cinematography;
- Evidence-free medical efficacy, absolute promises, exact durations, or exaggerated before/after comparisons;
- Over 30 seconds, multi-segment stitching, video/audio references, first/last frame continuation, or editing chains.

## Reference Invocation Strategy

Read by stage:

1. After reviewing the user's materials, read `references/asset-policy.md` to determine minimal sufficient assets and efficacy claim boundaries.
2. When determining the review angle, read `references/beauty-review-engine.md` to build an "observe—try—evidence—limited conclusion" chain.
3. When the user provides selling points, or when the Agent needs to recommend selling points and content hooks, it must read `references/selling-point-to-ugc.md` and generate a selling point translation card.
4. Before generating any character, scene, or usage relationship image, read `references/mobile-beauty-realism.md`.
5. Before writing the voiceover, read `references/live-review-dialogue.md`.
6. When writing timestamp prompts, read `references/timeline-patterns.md`.

The main file stores only workflow and hard constraints, and does not fully restate the references in conversation.

## Fixed User Guidance

### Round 0: Introduce the feature and request the core image

Fixed opening:

> This Skill turns your beauty or personal care product photo into a 4–30 second UGC review video that looks like a real creator personally filming and trying it. I will first assess whether your product photo can be used directly, and translate the brand selling point you want to highlight into real actions, visible evidence, and natural voiceover; afterward I will use only one round to confirm content direction, scene, duration, and necessary boundaries. Please upload your clearest product photo first; if you already have a designated influencer reference image or a selling point you want to highlight, feel free to send those along too, though they are not required.

On the first screen, only the product photo is a required input; a person image and one original selling point sentence are optional. Do not ask the user to fill in a full marketing form, complete script, music, subtitles, or shot list.

### Round 1: Automatic assessment and one-round confirmation of project boundaries

First output a brief assessment:

1. Product category, packaging, texture, or usage cues;
2. Whether the product photo can be used directly as `product_reference`;
3. Whether a `creator_reference` already exists; if not, generate one by default; ordinary usage actions do not require creating additional relationship images;
4. Which selling points can be observed from the footage, which come from user-provided information, and which are unverified efficacy claims;
5. One recommended core review question, one filmable evidence chain, and one natural voiceover direction;
6. How the user's original selling point will be preserved, downgraded, or rewritten, so users do not think the Agent dropped their commercial intent unilaterally.

Then give a consolidated confirmation, with the following default plan:

```text
Review path: first real trial + immediate experience (recommended)
Core selling point: Agent recommends 1 visualizable selling point; the user can directly reply "Highlight: ..." to replace it
Target user / context: Agent provides one reasonable assumption based on the product; the user may correct it once
Voiceover vibe: real quick test (recommended); can switch to friend sharing / light-contrast recommendation / restrained professional
Expression: preserve the selling point's meaning without reading ad copy verbatim; express it through actions, reactions, and personal conclusions
Creator: system-generated clearly adult Chinese/East Asian woman
Scene: real home vanity or bathroom sink
Aspect ratio: 9:16
Duration: 24 seconds; 4–30 seconds allowed
Audio: creator's live-synced Chinese voiceover + indoor ambience + usage action sounds, no BGM
Subtitles: no random subtitles; accurate subtitles are recommended to be added in post
Must preserve: packaging structure, primary color, logo placement, correct usage, and user-specified elements
Forbidden: medicalized conclusions, absolute promises, exaggerated skin smoothing, hard-ad recitation, third-person cinematography
```

Also provide a brief selling point translation preview:

```text
User/recommended selling point: original commercial intent
Audience's real concern: why this person would test it at this moment
Filmable evidence: what the camera can directly see
Voiceover direction: 1 natural expression triggered by an action or observation, not the final verbatim script
Expression boundaries: which words cannot be used based on a photo or a single trial
```

The user can reply "Go with the defaults" to confirm the recommended selling point, target-user assumption, and voiceover vibe; they can also simply reply "Highlight: ..." or paste a block of product selling points, and the Agent will complete the translation automatically, without requiring the user to write the voiceover themselves. Do not re-ask about already-confirmed items. When the user specifies regulated efficacy claims, exact numbers, comparison conclusions, or brand copy that must appear verbatim, first ask them to provide the final compliant text.

## Inputs and Automatic Assessment

### Product Photo

To be directly usable, most of the following conditions must be met: complete product body, clear edges, recognizable colors and materials, packaging proportions not severely distorted, unambiguous main product, and key usage structures not occluded. There is no need to promise verbatim reproduction of fine print.

Only generate a new clean `product_reference` when severe background interference, missing key structures, unclear primary product among multiple items, strong glare/hand occlusion, or a low-quality collage would break identity. The Agent makes this judgment itself and does not push the clarity assessment onto the user.

### Information Credibility

Tag each piece of information with its source:

- `Observation`: packaging, color, form, texture, and usage actions visible in the image;
- `User info`: ingredients, selling points, or brand descriptions explicitly provided by the user;
- `Creative inference`: a reasonable assumption made for review structure, not to be spoken as fact;
- `Claim needing confirmation`: strong claims such as medical, duration, exact ratios, certification, zero irritation, or suitability for all skin types.

From images alone, never confirm medical repair, anti-sensitivity, acne treatment, anti-aging effects, duration in hours, SPF values, absolute waterproofing, or "suitable for all skin types." When there is no credible claim, rewrite it as visible texture, spreadability, the on-face application process, instant glow, color, scent preference, or personal subjective impressions.

### User-Defined Selling Points

Accept selling points from the user at any level of polish: a single word, a sentence, product detail page copy, ingredient descriptions, a target audience, or a concern to be addressed. The Agent does not ask the user to rewrite them into spoken language first.

Processing order:

1. Extract the single commercial intent the user truly wants viewers to remember;
2. Determine whether it is a visible fact, a user-provided fact, a subjective experience, or a claim needing confirmation;
3. Match it with a real usage context and an audience concern;
4. Rewrite the selling point as an action or observation that the footage can prove;
5. Then rewrite the evidence as a line the creator would naturally say in the moment;
6. Check that the final script still conveys the user's original intent, rather than keeping only the "authentic feel" while losing the selling point.

When the user provides multiple selling points at once, rank them by "product relevance, filmability, credibility, and value to audience decisions," select only 1 core selling point, and keep at most 1 supporting observation; list the rest as not adopted, without silently discarding them.

## Asset Pipeline and Confirmation Gates

Use minimal sufficient assets and a single asset gate.

### Semantic Asset Names
- `product_reference`: always required; prefer the user's original image, locking packaging, proportions, primary colors, materials, and Logo placement.
- `creator_reference`: one by default. If the user has a qualified creator image, use it directly; otherwise generate an adult creator identity image.
- `product_use_reference`: not created by default. Add it only when tools are unconventional, contact positions must be precise, product size relationships are high-risk, or the first-round video already shows obvious gripping/usage errors; ordinary lipsticks, serums, creams, foundations, and standard brushes are controlled by text alone.
- `scene_reference`: created only when the user asks to replicate a specific space.
- `storyboard_reference`: created only when strict shot order or complex usage steps have failed repeatedly; not generated by default.

By default use only 2 images: the user's product image + one adult creator identity image. Do not regenerate if the user already has a qualified person image. For simple single-subject cases with low character-consistency risk, the product image alone may be used; add a third relationship or structure image only when there is an explicit risk of failure.

Dependencies:

```text
product_reference + creator_reference
    -> product_use_reference(optional after failure or when high-risk)
    -> storyboard_reference(optional after failure)
    -> final_video_prompt
```

After the creator identity image is generated, run one consolidated confirmation: whether the product is correct, whether the adult creator matches expectations, and whether the phone-shot realism holds. Confirm usage relations only if a relationship image was actually generated. When upstream assets change, update downstream assets and the final prompt in sync.

Before final output, resolve semantic names into the actual upload order:

```text
@Image1 = product_reference: locks product packaging, proportions, primary colors, materials, and Logo placement
@Image2 = creator_reference: locks the same adult creator's face, hairstyle, skin tone, real skin, and clothing
@Image3 = product_use_reference: appears only in high-risk or failure-fallback cases, locking precise dispensing, gripping, or contact relations
```

The final prompt keeps only the actual `@ImageN` references; internal asset names must not remain.

## Core Creative Methodology

### 1. Test Only One Core Question

Each video answers only one question that can be verified on camera, for example:

- Whether the texture spreads easily and whether it feels heavy;
- How the lip gloss/foundation color, coverage, or sheen looks in natural light;
- Whether the pump, dropper, or brush head is easy to control when dispensing;
- The product's immediate look across one complete usage motion;
- First impressions and personal preference for a fragrance, without describing the scent as objective efficacy.

Add at most one auxiliary observation. Do not cram six conclusions—ingredients, skin type, price, makeup longevity, scent, and packaging—into 24 seconds.

### 2. Do the Selling-Point Translation First, Not the Voiceover

User selling points must not be pasted directly into lines. First read `references/selling-point-to-ugc.md` and build an internal selling-point translation card:

```text
Original selling point
Core commercial intent
Target users and their real concerns
Credibility and claim boundaries
Filmable actions / sensory evidence
Opening expectation or small conflict
Immediate reaction
Conditional personal conclusion
Whether the user's original intent is ultimately preserved
```

"Natural" does not mean weakening the selling point, and "internet-native feel" does not mean stacking buzzwords. Effective internet-native feel comes from: a concrete concern in the first second, contrast produced by actual testing, the person pausing or self-correcting, conclusions carrying personal conditions, and variation in the pacing of shots and language.

Before generating the final script, internally produce three candidate intensities: most restrained, most natural, and slightly opinionated. After removing restating of the visuals, brand livestream-host tone, unsupported promises, and internet templates, output only the version that best matches the confirmed voiceover temperament; do not push all three candidates onto the user.

### 3. Build an Evidence Chain

Default sequence:

```text
Specific question or usage scenario
→ Camera clearly shows the product's identity
→ Correct dispensing or application
→ Close-up observation of texture/color/skin reaction
→ Creator's body and expression show an immediate reaction
→ Re-verify under natural light or from another angle
→ Deliver a conditional personal conclusion
```

Conclusions must be supported by the visible evidence before them. If the review question and conclusion would still hold unchanged with the product removed, the product is merely a prop and must be rewritten.

### 4. Real-Person UGC Shooting Contract

- All shots can be completed by the creator alone: handheld front-camera selfies, mirror selfies, phone fixed on a desk/stand, or close-up product/on-face insert shots the creator films themselves;
- Natural hard cuts between different takes are allowed, but space, person, product state, and lighting can remain continuous;
- Keep auto exposure, slight wide angle, deep depth of field, mild sharpening, partial highlights, and slight focus breathing;
- Keep pores, fine lines, lip lines, flyaway hairs, slight redness, and real makeup; no skin smoothing, no liquifying, no plastic skin;
- Product close-ups are evidence, not high-end hero shots; turntables, floating liquid, studio rim lighting, cinematic dolly moves, and ad-grade slow motion are prohibited.

### 5. Living-Person Voiceover

The voiceover first serves the person's in-the-moment reactions, while still having to deliver the confirmed selling points. 24 seconds defaults to 3–5 voiced moments, usually 4–18 Chinese characters each; half sentences, pauses, repetition, self-correction, and brief silences are allowed.

Every line must answer: "What did she see, touch, or smell a second ago that makes her speak now?" and "How does this line help viewers better understand the confirmed selling point?" If the first can't be answered, cut the line; if the second can't, rewrite it or hand the selling point to the action. Template openings, product-manual recitation, brand livestream-host tone, polished one-liners, buzzword stacking, and unsupported extreme claims are forbidden.

### 6. Limited Conclusions

Close with personal, conditional expressions such as "On me it looks…", "For my dry-leaning skin…", or "On a first application I'd prefer it thinner." Do not present a single instant trial as a long-term efficacy test. When a long-term conclusion is needed, reframe it as "first-day experience / immediate impression," or ask the user to provide real long-term footage and compliant facts.

## Final Video Prompt Rules

- The model is fixed to Seedance 2.5; use only reference images + a text prompt.
- For 4–30 seconds, use one video node; do not split into segments merely because it exceeds 15 seconds.
- Use the five-layer structure "reference assets + one-sentence overview + global settings + continuous timestamps + global wrap-up."
- The first segment starts at `00:00` and the last segment ends at the total duration; intervals are continuous, with no overlaps and no gaps.
- For 9–15 seconds write 3–5 segments, for 16–24 seconds write 4–7 segments, for 25–30 seconds write 5–8 segments.
- In segments where the product is primarily shown or used, cite the corresponding `@ImageN` again.
- Specify the total duration, 9:16, 720P, single node, and the sound and subtitle strategies.
- Default sound is sync-sound Chinese voiceover + indoor ambience + action sounds such as uncapping/pressing the pump/applying, with no BGM, no narration, and no second voice.
- By default, no random subtitles, stickers, watermarks, or irrelevant text; accurate subtitles are recommended for post-production.
- The global wrap-up lists only genre-relevant failure modes: face swapping, skin smoothing, product deformation, finger errors, incorrect usage, skin-state jumps, a third person behind the camera, hard-ad voiceover, and unsupported claims.

## Output

### Configuration/Asset Phase

Output: material assessment, selling-point source and claim risks, selling-point translation preview, recommended review question, project boundary confirmation, and creator identity image prompts only for images that are missing and will enter the final node. By default, do not generate a usage relationship image or nine-grid.

### Video Phase

Once confirmation passes, output in sequence:

1. Project settings: model, mode, duration, aspect ratio, 720P, structure, sound, subtitles;
2. Selling-point translation card: original selling point, viewer concerns, filmable evidence, voiceover strategy, expression boundaries;
3. Final voiceover script: list the single adopted version in chronological order, and explain what action or observation triggers each line;
4. Review evidence chain: core question, visible evidence, limited conclusion;
5. `@ImageN` reference list and locked purposes;
6. One directly copyable, complete Seedance 2.5 prompt;
7. Asset loop-closure check: all reference images cited, no useless intermediate images, no internal asset names, upstream changes synced;
8. Check the generated prompt item by item against the "Self-Check" below, and fix all issues before delivery.

## Self-Check

- \[ \] Does it only produce real-person UGC beauty/personal care product reviews, rather than TVCs or livestream selling?
- \[ \] Does Round 0 only request the core product images, with image quality judged by the Agent?
- \[ \] Is there only one consolidated project confirmation, allowing the user to continue with "go with the defaults"?
- \[ \] Is there only one core review question and at most one auxiliary observation?
- \[ \] Are user-defined selling points explicitly recorded, not silently replaced or omitted by the Agent?
- \[ \] Is the translation "selling point → concern → filmable evidence → on-the-spot reaction → limited conclusion" completed?
- \[ \] Does the voiceover sound like a genuine in-the-moment reaction while also letting viewers accurately understand the core selling point?
- \[ \] Is every conclusion supported by a visible action or an on-the-spot observation?
- \[ \] Are observations, user-provided information, creative inferences, and claims requiring confirmation distinguished?
- \[ \] Does it default to using only product images + creator identity images, adding assets only under an explicit risk of failure?
- \[ \] Are all of them resolved to actual `@ImageN` and repeatedly referenced during their active time ranges?
- \[ \] Is the 4–30 second duration a single node, with timestamps covering the entire video and continuous?
- \[ \] Is the voiceover triggered by in-the-moment feelings, restrained, and does it allow pauses?
- \[ \] Does it maintain the native look of phone footage, real skin, and single-person shootability?
- \[ \] Does it explicitly specify no BGM, no random subtitles, no watermarks, and subject-related prohibitions?
- \[ \] Have unresolved template placeholders such as `{...}` and `<...>` and internal asset names been cleared?
- \[ \] Are Seedance 2.0 legacy rules such as "split segments when over 15 seconds" and "generate in segments then composite" absent?

## Ask User

Only ask follow-up questions in the following cases:

1. Multiple products make it impossible to determine the primary test subject;
2. The user requests medical, certification, precise numeric, long-lasting duration, or absolute conclusions but has not provided compliant facts;
3. Brand scripts, prices, or specifications must appear verbatim, but no final text has been provided;
4. A specified influencer or space must be replicated, but the corresponding reference images are missing;
5. The user simultaneously requests mutually conflicting casual UGC shots and high-end studio/cinematic camera work.

A user merely saying "I want to highlight a certain selling point" is not a blocking issue; the Agent should directly propose filmable evidence and natural expressions. For other matters, the Agent makes recommendations and allows the user to continue with "go with the defaults."