---
name: ecommerce-ugc-ad-planner
description: "North America e-commerce UGC: plans sub-30-second localized UGC shoppable feed videos for cross-border sellers"
---

# Going-Global UGC Feed Ad Production

Turn a product into a native-feeling UGC ad that fits the target market and placement platform. Verify product and compliance facts first, then design the creative; the sense of authenticity must not rest on fabricated experiences, fake testimonials, or cultural stereotypes.

## Mandatory Model Constraints

```yaml
video_model: Seedance 2.5
video_model_fallback: forbidden
image_model_priority:
  - Lib Image
  - Seedream
  - other capable image model
max_single_video_duration_seconds: 30
default_aspect_ratio: "9:16"
```

- All videos use only `Seedance 2.5`. If the model is unavailable, stop video generation, report the blocker, and never silently switch models.
- For images, prefer `Lib Image`, then `Seedream`; choose another image model only when both are unavailable or the task is clearly unsuited to them, and log the reason.
- Treat 30 seconds as the hard cap for this Skill. If the platform or the current model entry point imposes a shorter limit, follow the shorter limit.
- By default, produce one 15–25 second, 9:16, portrait, mobile-first ad; extend to 30 seconds only when the content genuinely requires it.

## Read References on Demand

- Read references/market-research.md before starting market research.
- Read references/compliance.md before reviewing selling points, testimonials, disclosures, sensitive categories, and platform rules.
- Read references/asset-pipeline.md before handling product images, logos, talent, voice, and consistency assets.
- Read references/creative-production.md before writing voiceover, shots, Seedance prompts, and deliverables.

## Workflow

### 1. Build the campaign brief

Extract information from user input and attachments first; do not ask again for what has already been provided. Record:

```yaml
product:
  name: ""
  category: ""
  variant: ""
  verified_features: []
  prohibited_or_unverified_claims: []
target:
  country_or_region: ""
  language: ""
  audience: ""
  platform: "TikTok | Instagram Reels | Facebook Reels | YouTube Shorts | other"
offer:
  price: ""
  discount: ""
  shipping: ""
  returns: ""
creative:
  objective: "conversion | traffic | awareness"
  duration_seconds: 20
  aspect_ratio: "9:16"
  talent_mode: "real creator | actor reenactment | AI synthetic talent | hands-only"
assets:
  product_images: []
  official_logo: ""
  packaging_images: []
  proof_documents: []
```

Before entering final generation, the target country/region, the final video's language, the platform, the product identity, and at least one verifiable selling point must be clear. If other information is missing, produce a draft with clearly stated assumptions instead of stalling the whole workflow.

### 2. Conduct fresh market research for this run

On every run, research the target market online; do not rely solely on the Skill's static knowledge. Per `market-research.md`, look up:

1. The latest rules from local advertising regulators and platforms.
2. Category-specific ad bans and restrictions, claim requirements, labeling, evidence, and age requirements.
3. Actual local language usage, forms of address, tone, units, currency, date, and number formats.
4. Recent local platform content, creator expression, seasonality, festivals, and commercial music trends.
5. Cultural sensitivities, religious contexts, gestures, clothing, family roles, and visual-symbol risks.

Output a `market_evidence` record with dates and links. Keep "regulatory facts", "platform rules", "observed creative patterns", and "inferences/pending verification" separate. Use at least two reliable sources; for high-risk categories, include at least three types of sources: regulators, platform policies, and category governing bodies.

### 3. Build the claim ledger and compliance gate

For each selling point, record the original wording, evidence, permitted phrasing, prohibited phrasing, and applicable markets. Price, discounts, inventory, shipping, returns, review figures, environmental, health, safety, performance, and comparative claims all require evidence.

- Do not fabricate reviews, sales figures, star ratings, media endorsements, certifications, scarcity, or before/after comparisons.
- AI models must not claim to have actually purchased the product, used it long-term, or personally achieved results; reword as a demonstration, feature explanation, or an explicitly presented actor.
- For real creator testimonials, use only their actual experiences and authorized content.
- Disclose advertising, sponsorship, gifted products, affiliate relationships, and AI-generated content clearly, per target-region and platform requirements.
- For high-risk categories such as pharmaceuticals, supplements, weight loss, beauty efficacy, finance, alcohol, gambling, children's products, weapons, and politics, stop before final generation until dedicated verification is complete.

Run `python scripts/validate_campaign.py campaign.json` to check structural hard constraints; it cannot substitute for legal or platform review.

### 4. Standardize product and brand assets

Follow `asset-pipeline.md`.

- Multiple product images: prefer real front, side, back, and detail shots; do not regenerate facts that already exist.
- Only one real photo: generate a three-view image on a pure white background, front, side, and back from left to right; mark unseen structures as "AI-inferred" and have the user confirm them before using them as the video's identity anchor.
- Logo: prefer cropping, correcting, background removal, and upscaling from the original image, verifying every character and shape; never let the image model redraw it from scratch. If the logo is blurry, obscured, or unverifiable, request official files.
- Establish non-drift constraints for the product: silhouette, proportions, colors, materials, ports, buttons, packaging, logo placement, and text.

### 5. Design local UGC talent

Design 2–3 candidates based on the target market and audience, but do not reduce nationality to ethnicity or stereotyped appearance. Prioritize matching everyday scenarios, language ability, age range, usage needs, and style of expression.

Default visual direction: an ordinary adult creator, shot on a phone front camera or handheld, natural indoor lighting, realistic skin texture with subtle pores and fine lines, natural hair, no heavy skin smoothing, no studio advertising lighting, slight handheld shake, and lifestyle framing. Do not use real celebrities, unauthorized likenesses of real people, or sensitive portrayals of minors.

If the product doesn't need a face, involves privacy, or carries high talent-consistency risk, proactively offer alternatives: `hands-only`, POV, tabletop demonstration, or real-person narration with product close-ups.

### 6. Write the localized script

Write native-sounding spoken copy in the target language first, then provide the strategy explanation in Chinese; do not write Chinese first and translate it line by line. Use:

`Hook → Wow moment → Solution → How it works → Outcome → CTA`

Their business meanings, in order: pain point/desire, a visual twist, the product's entrance, a minimal feature demo, a scenario-based outcome with credible proof, and a call to action. Stages may be merged, but the Hook, product evidence, and CTA must all be present.

Also produce at least 3 hooks: pain-point, curiosity/contrast, and result/demo types. The hook should introduce the product proposition within 0–3 seconds and complete its main grab within the first 6 seconds; it must not use fear-mongering, humiliation, false urgency, or absolute wording that cannot be substantiated.

Time it at a realistic reading speed and proofread by reading aloud. Better to shorten lines than to cram the full 30 seconds. Subtitles should accommodate sound-off viewing; voiceover, on-screen text, and on-screen demonstration must all convey the same fact.

### 7. Design a single Seedance 2.5 final video

By default, generate one continuous 15–25 second video in a single pass; keep 3–6 shot events, avoiding excessive cutting within 30 seconds that would cause product, character, or logo drift.

Structure the prompt as:

1. Referenced assets and their respective roles: the product three-view controls the product, the logo image controls the brand, and the talent image controls the person.
2. Duration, 9:16, UGC realism, target platform, and target language.
3. Second-by-second timeline: visuals, actions, voiceover, subtitles, sound effects, transitions.
4. Physical continuity of product interaction and key demonstration steps.
5. Identity and brand consistency constraints.
6. Negative constraints: face swapping, product deformation, garbled logo/text, extra fingers, wrong packaging, excessive beautification, studio look, flickering, abrupt jumps, subtitle occlusion.

If a single-pass generation cannot reliably handle complex interactions, simplify the events and shots first; if it remains unstable, then — with the user's consent — split into multiple Seedance 2.5 clips and edit them together; the video model still must not be changed.
### 8. Quality Check and Delivery

At minimum, check:

- Duration does not exceed 30 seconds; the video model is Seedance 2.5.
- Product structure, color, packaging, and Logo match the confirmed assets.
- The model is an adult, with consistent identity, hands, lip-sync, voice, and language.
- The proposition is clear within the first 3 seconds, a hook is formed within the first 6 seconds, the product demo is visible, and the CTA is clear.
- Lines sound natural; units, currency, subtitle line breaks, punctuation, and taboos are adapted to the target region.
- Every factual selling point is traceable to the claim ledger; no fabricated experiences or testimonials.
- Disclosures, subtitles, and CTA sit within platform safe zones; music, fonts, Logo, and likeness all have commercial usage rights.
- The landing page fully matches the ad on product, price, offer, and promises.

By default, deliver one main version plus two low-cost A/B variants. Each variant changes only one primary variable at a time—for example, the Hook, model, CTA, or demo order—to make attribution easy.

## Output Format

```markdown
## 1. Brief and Assumptions
## 2. Market Research and Sources
## 3. Compliance Conclusions and Claim Ledger
## 4. Asset List, Three-View Renderings, and Logo Processing Results
## 5. Model Candidates and Final Setup
## 6. Target-Language Voiceover + Chinese Strategy Explanation
## 7. Second-by-Second Storyboard Table
## 8. Image Generation/Processing Prompts
## 9. Full Seedance 2.5 Prompt
## 10. Subtitles, Sound, CTA, and Placement Notes
## 11. QA, Failed Self-Check Items, and Items Pending User Confirmation
## 12. A/B Variants
```

Do not present inferences as facts. If the current environment can only generate a plan and cannot call the models, state clearly that what is being delivered is an "executable prompt and production package"; do not claim the finished video has already been generated.