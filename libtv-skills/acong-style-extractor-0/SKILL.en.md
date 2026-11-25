---
name: acong-style-extractor-0
description: "Subject style extraction: extract a transferable style from a reference image"
---

# Subject-Replaceable Style Extraction

## Skill Positioning

This Skill is used to split a reference image into two types of information:

1. **Subject/content prompt**: Describes the core content in the image that can be replaced.
2. **Style prompt**: Describes the transferable, reusable visual style.

This is not ordinary image-to-prompt reverse engineering. The default goal is not a 1:1 replication of the original image, but rather to support replacing subjects, recombining scenes, or generating new images while preserving the visual style.

## Applicable Scenarios

Use this Skill when the user has the following needs:

- Uploading a reference image and wanting to extract its style;
- Uploading a reference image and asking to "replace it with XXX";
- Uploading a reference image and asking to "generate a new image in this style";
- Needing to split the reference image into a "replaceable subject" and a "reusable style".

## Inputs

The user may provide:

- A reference image;
- Optionally, a new subject, new image requirements, or replacement instructions;
- Optionally, preservation requirements, such as "keep the background unchanged", "replace only the character", or "keep the composition unchanged".

## Core Principles

- By default, this is for secondary creation, not for replicating the original image.
- The subject/content prompt only describes replaceable content.
- The style prompt describes the transferable visual language, and may also preserve visual motifs and spatial grammar that carry stylistic value; do not bind it to specific subjects or objects in the original image, such as specific people, products, vehicles, animals, platforms, tracks, or transportation facilities.
- When the user provides both a reference image and new image requirements, use the user's new image requirements as the subject/content prompt, with the reference image serving only as the style source.
- If the user only says "replace it with XXX", interpret this by default as a full replacement of the original subject/content; preserve the reference image's visual style, visual motifs, and spatial grammar, but do not by default preserve the original image's specific scene, specific facilities, or specific object combinations.
- Only migrate the reference image's scene skeleton when the user explicitly requests preserving the scene, background, spatial structure, or worldview.
- Do not output negative prompts by default unless the user explicitly requests them.
- Do not output transferability analysis by default, to avoid lengthening the workflow.
- Output language is Chinese.

## Transfer Mode Determination

This Skill has two transfer modes. First determine the transfer mode, then extract the subject/content prompt and the style prompt.

### Default Mode: Style and Visual Motif Transfer

When the user says:

- "Keep this style"
- "Use this image's style as a reference"
- "Generate ... in this style"
- "I want this feel, but change the image to ..."
- "Replace the subject with XXX"

By default, only transfer the reference image's visual style, visual motifs, and spatial grammar; do not transfer the original image's specific subject, specific objects, specific scene identity, or specific facility combinations.

Content transferable by default includes:

- Style type;
- Color characteristics;
- Lighting and shadow characteristics;
- Materials/textures;
- Atmosphere and mood;
- Composition/camera language;
- Visual motifs and spatial grammar with stylistic value;
- Image quality/rendering approach.

Visual motifs / spatial grammar refer to visual organization methods in the reference image that carry stylistic recognizability and remain valid after the subject is replaced, for example:

- Recurring shape language;
- Signature line flow;
- Spatial hierarchy organization;
- Material combinations;
- Visual relationships between architecture, nature, people, or objects;
- The sense of rhythm, symmetry, depth, or decorative language in the image;
- Scene grammar that is stylistically recognizable but not equivalent to a specific subject.

For example, when the reference image is in a futuristic glass sci-fi style, you can extract visual motifs such as "streamlined curved structures, transparent glass spaces, champagne metallic frames, mirror-reflection spaces, utopian futurism".

Content not transferred by default includes:

- The original image's specific people, vehicles, animals, or products;
- The original image's specific subject or object, such as "capsule train";
- The original image's specific facilities, such as "platform", "track", or "specific transportation facilities";
- The original image's specific scene identity, such as "transit platform" or "a certain futuristic city block";
- The original image's specific object combinations, such as "a train parked beside a glass track";
- The original image's worldview elements, unless the user explicitly requests preservation.

### Scene Skeleton Transfer Mode

Only when the user explicitly says:

- "Keep this scene"
- "Keep the background unchanged"
- "Keep this worldview"
- "Keep this spatial structure"
- "Keep this futuristic city scene"
- "Keep this city background"
- "Keep this architectural spatial structure"
- "Replace only the character/subject, keep everything else unchanged"
- "Generate ... based on this scene"

may the reference image's scene skeleton, spatial structure, architectural language, or worldview elements be written into the subject/content prompt or related descriptions.

## Workflow

### 1. Determine User Intent

Choose the processing approach based on user input:

- **Extraction only**: The user provides only a reference image, without specifying a new subject or new image.
- **Subject replacement**: The user asks to keep the style and replace the subject with a new object.
- **Style-transfer generation**: The user asks to generate a new image or scenario using the reference image's style.

At the same time, determine whether the current task is default style and visual motif transfer, or scene skeleton transfer. If the user has not explicitly requested preserving the scene skeleton, treat it as style and visual motif transfer.

### 2. Extract the Subject/Content Prompt

The subject/content prompt should include:

- Specific objects;
- Key actions;
- Key spatial relationships;
- Necessary scene relationships.

The subject/content prompt should not include:

- Style words;
- Style information such as color, lighting/shadow, material, or rendering approach;
- Trivial details that do not affect the validity of the secondary creation;
- Overly fine-grained positional relationships.

In the default style and visual motif transfer mode, the subject/content prompt should follow the user's new requirements and should not automatically inherit the reference image's original specific scene.

For example, if the user says "I want this style, but generate two people in a standoff", the subject/content prompt should be similar to: