---
name: avatar-script-studio
description: "Digital human talking-head director: pick a persona, write lines, and set up lip-sync"
---

# talking-head-director

Use this skill when producing talking-head / explainer / spokesperson / digital-human on-camera videos. You are the director + script architect: choose the avatar, write the on-camera performance script, calibrate per platform, and deliver a **production-ready script + scene direction** — not a content plan.

> Environment adaptation: the source is a talking-head director built for Higgsfield Lipsync Studio + Seedance 2.0. The Lipsync Studio / Soul ID training mechanism doesn't exist in this environment → replaced with an **avatar character anchor** (first use `generate_image_v3` to produce one finalized look anchor image; reusing that same image across the whole video delivers identity continuity) + **`generate_video_v3` per shot, referencing the same anchor and lip-syncing**; voiceover goes through `generate_audio`; multiple segments are composited with `composite_video`. The avatar archetypes / script craft / delivery calibration below are fully inlined — nothing is outsourced.

## Avatar Selection (lock it in before writing the script — it determines the script's tone / pacing / word choice / credibility)

Choose the avatar before writing a single word. The avatar choice sets the script's tone, pacing, vocabulary register, and credibility baseline.

**Expert / Authority**
Look: professional attire, clean and crisp, neutral/dark tones, direct eye contact with camera.
Used for: educational content, thought leadership, how-to explainers, coaching, B2B.
Script voice: steady, confident, clear, no fluff, complete sentences.
Avoid: slang, casual contractions, overly enthusiastic phrasing.

**Relatable Creator**
Look: casual styling, warm/lifestyle backdrop, natural range of expression.
Used for: UGC-style content, product recommendations, personal stories, social proof.
Script voice: first person, casual, uses contractions, natural pauses allowed.
Avoid: corporate speak, formal sentence constructions, any script-reading feel.

**Brand Character / Persistent Persona**
Look: a character anchor trained/locked in and matched to the brand identity.
Used for: brand campaigns, AI influencer content, series requiring character continuity.
Script voice: defined by the character persona — set it before writing.
Avoid: any tone that contradicts the character bible.

**Neutral Presenter**
Look: clean, minimal, professional but not formal.
Used for: product demos, app walkthroughs, announcements, multi-audience content.
Script voice: clear, benefit-oriented — neither corporate nor casual.
Avoid: strong personality.

### Avatar × Platform Match

| Platform | Best avatar archetype | Why |
|---|---|---|
| TikTok | Relatable Creator | Authenticity is this platform's currency |
| Instagram Reels | Relatable Creator or Brand Character | Personal or brand-consistent content converts better |
| YouTube Shorts | Expert/Authority or Neutral Presenter | Viewers want information and credibility |
| LinkedIn | Expert/Authority | Professional credibility is required |
| Web/landing page | Expert or Neutral Presenter | Trust and clarity beat personality |

## Script Architecture (4 sections — written for the ear, not the eye)

Every talking-head video follows a 4-section structure.

**1. Opening (0–5s)**
Start inside the viewer's world. Never open with a brand name / self-introduction / generic welcome.
- Strong opening (pain point first): "Most people get [X] wrong — and it costs [consequence]."
- Strong opening (bold claim): "[Specific thing] changed my [result] in [timeframe]."
- Strong opening (the right question): "Ever wondered why [common frustration]?"
- Weak openings: "Hey everyone, welcome back…" / "Today I want to talk about…" / "I'm [name]…"

**2. Body (5s to duration−10s)**
One idea per sentence, max 2 ideas per block. Pick the structure by content type:
- Explainer/education: problem → cause → solution → proof
- Product demo: context → feature → benefit → proof
- Thought leadership: claim → evidence → impact → thought-provoking close
- Personal/story: situation → tension → turn → takeaway

**3. Bridge to CTA (final 5–8s of the body)**
Consequence bridge: "Which means if you [don't/do], you'll [negative/positive outcome]."

**4. CTA (final 5s)**
One action, a directional verb, a specific destination.
- Strong: "Tap the link in bio to start your free trial."
- Weak: "Let me know what you think in the comments."

## Teleprompter Script Format (written for an AI digital human's on-camera delivery, not for reading)

- **Sentence length**: max 15 words per sentence; if longer, split it.
- **Delivery markers**: `[PAUSE]` half-second pause after a strong statement · `[EMPHASIS]` stress the next word/phrase · `[SLOWER]` slow down for complex/important information · `[FASTER]` raise the energy for lists/build-ups.
- **Paragraph breaks = breath breaks**: max 2–3 sentences per paragraph.
- **Write all numbers and symbols as spoken words**: `$47`→forty-seven dollars; `3x`→three times; `#1`→number one.
- **Avoid**: mid-sentence parentheticals, em dashes within sentences, ellipses — they disrupt the lip-sync rhythm.

## Platform Delivery Table

| Platform | Duration | Energy | Pacing | On-screen text |
|---|---|---|---|---|
| TikTok | 15–45s | High (peak at open and hold it) | Fast | Mandatory (many watch muted) |
| Instagram Reels | 15–60s | Medium-high | Medium | Important (boosts completion) |
| YouTube Shorts | 30–60s | Medium | Slightly slower | Supporting (reinforces key points) |
| LinkedIn | 30–90s | Medium-low, authoritative calm | Unhurried | Optional (usually watched with sound) |
| Web/landing page | 60–120s | Medium-low, credible | Measured | Minimal |

## Workflow (mapped to our tools)

1. **Set platform and goal** — where does it run; what should the viewer do after watching?
2. **Pick the avatar archetype** — match it to platform and content type (see table above).
3. **Set duration** — fix the cap before writing.
4. **Write the opening first** — the first sentence matters most.
5. **Build the body** — choose the structure that fits the content type.
6. **Write the CTA** — one action, one directional verb, one destination.
7. **Format for teleprompter** — apply the sentence-length, delivery-marker, and paragraph-break rules.
8. **Output the talking-head Brief** — full structured brief + scene direction + two variants.
9. **Generate the final video**: for the avatar character anchor, use `generate_image_v3` (or a user-uploaded photo) to produce one finalized look image as the identity anchor; use `generate_video_v3` per shot, referencing the same anchor image with lip sync; embed lines or voice them with `generate_audio`; composite multiple segments with `composite_video`. Reusing the same anchor image across the whole video achieves avatar continuity — no identity training needed.

## Output: Talking-Head Brief

```
TALKING-HEAD BRIEF
Platform / Avatar (archetype + description, or persistent character anchor name) / Duration / Framing (chest-up / medium / full) / Backdrop / Lighting (soft frontal / warm lifestyle / clean studio) / Energy level
Script: [full teleprompter script + delivery markers]
On-screen text: [key phrases + approximate timestamps]
Scene direction: [eye contact, range of expression, gestures]
CTA: [exact one-liner — one action, directional verb, specific destination]
Variant A (shorter cut): [trimmed for 15s platforms — hook + CTA only]
Variant B (different avatar archetype): [same script rewritten for a different avatar's energy]
```

## Common Failure Diagnosis

| Problem | Root cause | Fix |
|---|---|---|
| The digital human sounds robotic | Written for reading, not speaking | Read each line aloud; split anything over 15 words |
| Lip sync is off | Numbers/symbols left in raw form | Write everything as spoken words |
| Viewers drop off after 5 seconds | Opening starts from the speaker/brand | Open from the viewer's pain point / a bold claim instead |
| Video runs too long | Kept everything, cut nothing | If a line can go without losing a proof point or the CTA, cut it |
| CTA gets no results | Soft/vague | Directional verb + specific destination |
| Avatar doesn't fit the content | Chosen by aesthetics, not function | Professional content → Expert/Authority; personal stories → Relatable Creator |
| Works on one platform, fails on another | Delivery not calibrated per platform | Re-run the platform delivery table; adjust pacing/energy/duration |

When improving an underperforming script: find the line where viewers stop watching, diagnose why, and rewrite from that line onward.

## Pairings (loaded together when the query requires / also this skill's evaluation combos)

This skill's source (Higgsfield Talking Head Video Director) is a self-contained director/script recipe — avatar selection, script architecture, teleprompter craft, and platform calibration are all inlined, and generation relies on this environment's tools (`generate_image_v3` / `generate_video_v3` / `generate_audio` / `composite_video`). The source references no other skill (Lipsync Studio / Seedance / Soul ID are Higgsfield backend generation capabilities, adapted into this environment's tools — not cross-skill dependencies). Hence no source-native cross-skill dependency.

Boundaries (reroute, don't depend): product-endorsement talking-head → ugc-flow; digital-human single-scene product pitch (hard constraint: product must be on camera / single camera, single keyframe) → digital-avatar-product-pitch; podcast conversation → podcast-flow.