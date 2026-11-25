---
name: influencer-fashion-try-on
description: "Influencer try-on seeding shorts: UGC outfit videos showcasing fit, fabric, and styling for e-commerce product seeding"
---

# ugc-try-on-flow

Use this skill when making UGC try-on videos (a creator trying on wearable products, showcasing fit and material). Persona selfie texture and hand-count / POV rules are the same as ugc-flow.

## Storyboard Structure and Narrative Arc

Each storyboard = one **21:9 horizontal strip containing 4 vertical 9:16 slots**. Board 1 standard try-on arc + slot-by-slot POV:

Slot Segment POV / Framing Key points 1 PRE_WEAR Selfie half-body Basic neutral loungewear, no product; one hand holding the phone, the other carrying the paper bag by one handle 2 WEARING Tripod full-body Hard cut reveal that the product is already worn, paper bag gone, fabric draping naturally; one brief twirl 3 TEXTURE_CLOSEUP Tripod macro Hands-free close-up of fabric details; face partially visible 4 STYLE_POSE Tripod medium-wide/full-body Different room, same outfit + simple footwear + minimal accessories, confident styling

## Workflow

Product analysis → persona anchor (or user photo) → monologue (defaults to a "personal want" mini-story) → **serial** board generation (21:9) → write video prompts board by board → `generate_video_v3` **in parallel**, shot by shot → `composite_video` compositing → `generate_audio`.

## Rules

- Character identity + **hairstyle** locked throughout (see character-consistency); hand-count / POV rules same as ugc-flow (selfie: one hand holds the phone; two-handed actions switch to tripod).
- **Wardrobe continuity**: Board1 slot1 = not wearing + kraft paper bag; slots 2–4 and beyond = product already worn, bag gone. No in-shot outfit changes, no mirrors / reflections.
- **Paper bag rule**: exactly one plain brown kraft paper shopping bag, no logos / branding / shipping stickers, bag stays closed and is not opened to show contents; appears only in slot 1, then disappears.
- **No hand-to-fabric contact in the material close-up (Cut 3)** (hand-free macro, hands completely out of frame).
- **Separate audio tracks**: Cut 1/2/4 = on-camera dialogue (lip-synced); Cut 3 = overlaid voiceover. Lip-sync detail: when facing away from the camera, the mouth stops forming words.
- **Turn beat**: only Board1 Cut2 has one brief twirl.
- No CTA ending; Seedance defaults to `count: 2`.

## Companions (query must load them together / also this skill's evaluation set)

Relation Target Usage Required? provenance dependency product-analyzer product analysis when a product is available native dependency image-generation persona / storyboard image generation required native dependency video-generation per-shot generation required native dependency montage N≥2 stitching required when N≥2 native dependency character-consistency creator identity + hairstyle locked throughout required

Boundaries: talking-head reviews → ugc-flow; product as the protagonist → ugc-product-flow; tutorials → ugc-tutorial-flow; unboxing → ugc-unboxing-flow.