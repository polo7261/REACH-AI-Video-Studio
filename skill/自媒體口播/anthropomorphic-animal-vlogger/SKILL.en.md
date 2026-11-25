---
name: anthropomorphic-animal-vlogger
description: "Anthropomorphic animal vlogger videos: animal influencer talks on camera in funny short videos, realistic vertical-screen style"
---

## name: animal-vlogger\\

namespace: industry\
title: "Anthropomorphic Animal Vlog"\
description: "Make hyper-realistic, funny short videos of anthropomorphic animals appearing on camera like human Vloggers — specify animal type / location / outfit / dialogue (embedded lines drive the lip-sync) in real-world vertical scenes. Image-to-video workflow: use generate_image_v3 for the character image + generate_video_v3 for the final video."\
version: 2

# animal-vlogger

Use this skill when making viral comedy content of the "anthropomorphic animal blogger" kind: an animal dressed in clothes, walking upright, with human expressions, holding a selfie stick and talking to the camera in real-world locations just like a human Vlogger. The core selling point is the comedy of **hyper-realism + anthropomorphic contrast + everyday-life griping**.

> Environment fit: image / image-to-video engines → `generate_image_v3` (generates the anthropomorphic animal character image) + `generate_video_v3` (image-to-video, talking to camera, embedded lines drive the lip-sync). Source is a muapi recipe (MIT); wording has been rewritten and tool vocabulary adapted; self-contained, no external dependencies.

## Inputs

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| Animal type | No | Monkey | Dog / cat / bear, etc.; the more expressive, the better |
| Location | No | Bustling everyday street | Real-life settings (busy streets, markets, subway entrances…), providing environmental detail and a lived-in feel |
| Outfit | No | Bright red T-shirt | A single, memorable bright-colored garment that heightens the anthropomorphic contrast |
| Dialogue | No | — | Lines to lip-sync, in any language/dialect; a casual everyday-gripe tone works best |

If an input is missing, fall back to the default or ask the user one quick follow-up question — don't just sit and wait.

## Workflow (Two Stages, Image-to-Video)

### Stage A — Generate the anthropomorphic animal character image (`generate_image_v3`)

A single call generates the base character image, with all composition points inlined into the prompt:

- **Subject**: a hyper-realistic, cinematic close-up of the {animal type}; **anthropomorphized** — upright, wearing the {outfit}, holding a selfie stick, with the demeanor of a believable blogger.
- **Comedic micro-expressions**: add scene-appropriate "in-character" details (e.g., in hot weather, "lightly sweating, looking slightly irritated") — this is where the humor comes from; don't settle for a neutral expression.
- **Setting & background**: place it in the {location}, with a background full of everyday details (roadside stalls, people eating, vibrant city streetscapes) to create an authentic lived-in feel.
- **Image quality**: photorealistic, high detail, cinematic texture.
- **Aspect ratio**: `aspect_ratio` = 9:16 (vertical vlog). Technical specs go in fields, not in the prompt body.

Once the image is generated, ⏸ present it to the user for confirmation before moving on to Stage B.

### Stage B — Image-to-video final cut (`generate_video_v3`)

Use the image confirmed in Stage A as the reference image (`role: image` first frame / reference) and bring it to life in a single call:

- **Motion & camera**: opens in selfie mode with a slightly wide-angle shot; the {animal type} is highly expressive and can carry a comedic "mildly displeased / disdainful" emotion while talking naturally; intersperse quick push-in close-ups on the displeased face; smooth gimbal-style camera movement.
- **Dialogue lip-sync**: embed the {dialogue} lines into the prompt's `Audio:` section to drive the lip movements and voiceover (the engine renders audio natively); add ambient sound in the same section (busy street noise). **There is no standalone lipsync tool — lip movement is generated from the embedded lines.** BGM is not embedded; if needed, generate the audio separately and mix it in at the compositing stage.
- **Tone**: hyper-realistic + comedic, with ambient sound present.
- **Duration / aspect ratio**: `duration_sec` as an integer ≤ 15 (single shot; for longer segments, split into separate shots and chain them by using the previous segment's last frame as the first-frame anchor of the next); `aspect_ratio` = 9:16.

Once the video is generated, present the final cut.

## Trigger words

Anthropomorphic animal video, funny monkey video, animal blogger, animal vlog, animal lip-synced talking video.

## Integration

No cross-skill dependencies; this skill is self-contained (sourced from a standalone muapi recipe, references no other skills).\
Boundaries (do not use this skill; route elsewhere instead): talking babies → talking-baby-video; real-person talking heads / explainer videos → talking-head-director; cute-pet everyday at-work vlogs without anthropomorphic lip-sync → pet-worker-vlog.