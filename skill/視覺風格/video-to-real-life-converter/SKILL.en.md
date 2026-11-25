---
name: video-to-real-life-converter
description: "3D-to-live-action video converter (comic drama): converts footage to live-action, 3D, anime, or overseas styles; simple and beginner-friendly—just upload your video."
---

## Purpose Introduction

This Skill focuses on precisely restyling 3D character videos into live-action photography, Japanese anime, oil painting, and various other artistic styles. Through deep integration of Lib image with Seedance 2.0, it preserves the original video's actions and camera movements while achieving extremely high costume consistency, and effectively eliminates the plastic look of 3D modeling as well as limb clipping issues.

## Applicable Inputs

- **Video format**: MP4 videos containing 3D character actions and scene interactions.
- **Content recommendations**: 3D raw footage with clear actions and distinct lighting and shadows.

## Operation Steps

1. **Intelligent Segmentation and Sampling**: Automatically perform shot segmentation, and extract multi-angle keyframes and representative still frames from each shot.
2. **Style and Costume Interactive Confirmation**:
   - **Style definition**: The user must specify the target style (e.g., cinematic realism, Japanese anime, etc.). If the live-action style is selected, the system will automatically inject cinematic hyper-realistic photography prompts.
   - **Costume anchoring**: The user confirms whether to keep the original costume or customize a new one; the system will lock in features to establish a global costume anchor.
3. **Generate Character Reference Sheet**: Based on the confirmed style and costume, generate a multi-angle (front/side/back/close-up) character composite sheet in one pass as the appearance reference for the entire film.
4. **Subject Segmentation and Anti-Clipping Processing**: Apply soft masking to the character and contact objects, add feathered edges, and ensure that interaction areas (e.g., leaning against walls, sitting on chairs) blend naturally.
5. **Seedance 2.0 Stylized Repainting**: Use the omnipotent reference mode, transmitting structure via depth maps and Softedge (the original image's RGB is strictly forbidden from entering the reference slots), combined with the character reference sheet for high-intensity stylized rendering.
6. **Stitching and Post-Processing**: Perform facial stabilization and stylized color grading, then output the final product.

## Output Requirements

- **High consistency**: The character's appearance, costume details, and confirmed style must remain absolutely uniform throughout the entire film.
- **No modeling look**: The live-action style should feature realistic skin texture and lighting layers, eliminating traces of 3D rendering.
- **Natural edges**: No flickering or sense of separation at the contact points between the character and the environment, with smoothly feathered edges.

## Notes

- **Mandatory interaction**: Style and costume confirmation is a key step for quality assurance and cannot be skipped.
- **Prompt locking**: The live-action style must use the built-in mandatory prompt library to ensure texture quality.
- **Reference constraints**: The spatial structure reference must remove the original image's RGB information, retaining only depth and edge features to prevent style residue.