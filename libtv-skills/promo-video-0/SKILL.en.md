---
name: promo-video-0
description: "Screenshot to promo video: generate promotional short films from UI screenshots"
---

# promo-video —— Generate a promo short video from a single image (with creative options)

## Positioning

Add a layer of "creative guidance + step-by-step confirmation" on top of libtv-skill: **locally** analyze the reference image → propose 3-4 differentiated style directions → user picks → go through the three steps of **script → storyboard → synthesis**, with the user reviewing each step before moving on to the next.

Unlike libtv-skill's "pure messenger" positioning, this skill **does allow local creative work at the style-selection step** (explicitly requested by the user). But once the style is chosen, the prompts for every subsequent step are still assembled according to libtv-skill's rules: only the user's goal + selected style + OSS URL / previous step's output — no piling on quality words, no decomposing the storyboard yourself (storyboards are produced by the libtv backend).

## Prerequisites

- `LIBTV_ACCESS_KEY` is set (a libtv-skill prerequisite).
- The user has provided a local image path (`.jpg` / `.png` / `.webp` etc.), size < 200MB.
- libtv-skill's scripts exist at `../libtv-skill/scripts/` (same project). If not in the same project, you need to locate libtv-skill's scripts directory using an absolute path.

## Workflow

**Key principle**: all three steps (script / storyboard / synthesis) append messages within the **same sessionId** (`--session-id`) so the libtv backend retains context; do not open a new session for each step.

### Step 1: Read the image = understand the product + brainstorm promo directions

Use the `Read` tool to open the image path the user provided. The goal of this step is **not to judge visual aesthetics**, but to **first understand the product/subject**, and only then think about "how to shoot a promo video for it" based on that understanding of the product.

**First do product understanding (jot it down locally, don't output it to the user)**:

- **What it is**: category / function / form (e.g., "a ceramic pour-over cup", "a city culture map poster", "a splash screen UI")
- **Visible selling points**: clues readable from the image — material, craftsmanship, design language, colors, details, proportions, packaging, logo / brand tone …
- **Who would buy / who would use it**: reasonable inference of the target audience profile (age range, aesthetic preferences, consumption scenarios)
- **Typical usage scenarios**: where, when, and alongside what this thing is typically used
- **Tellable differentiators**: what makes it unique compared to others in the same category, as revealed by this image (even if just a guess)

If the image doesn't provide enough information to identify the product (e.g., it's just an abstract asset, or it's the promo material itself rather than a product), **first ask the user "What is this product / what do you want to promote?"** before moving to the next step. **Do not fabricate a product positioning out of thin air**.

**Then produce 3-4 promo directions**. Each direction must be **rooted in the product**, not empty talk about style. For each direction, provide three things:

- **Style tag** (1-3 words, e.g., "dark cinematic", "Japanese fresh", "cyber neon", "minimalist premium", "documentary style")
- **Selling point angle** (one sentence stating **which selling point of the product this video starts from** — material & craftsmanship / usage scenarios / emotional resonance / contrast / user story / data & facts …)
- **One-line pitch** (one sentence clarifying what the video is about — a "selling point" written for the user to see, which must reflect the product's name or core attributes)

**Differentiation requirement**: the 4 directions must be separated on at least 2 of the dimensions "selling point angle / emotion / narrative structure". Do not end up with 4 directions all talking about "usage scenarios" with merely different style skins. At least one direction must take an emotion / story / contrast angle, set apart from a plain "product showcase".

### Step 2: Use AskUserQuestion to let the user pick a direction

Use the `AskUserQuestion` tool to present the 3-4 directions as options; each option:
- `label`: "style tag · selling point angle keyword" (short, 1 line, e.g., "dark cinematic · handcrafted")
- `description`: that pitch (it must let the user see at a glance that the video is about what **their product** does, not a vague style description)

Use "Creative Direction" for `header`. `multiSelect: false`.

If the user is unsatisfied with all the candidates, they will go with Other → take their added words directly as the final style description.

### Step 3: Upload the image + have libtv produce the **script / copy**

First upload the image: