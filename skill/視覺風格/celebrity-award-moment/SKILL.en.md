---
name: celebrity-award-moment
description: "Celebrity award-moment short: a 15-second cinematic awards scene, spotlight locking onto them in the crowd"
---

## name: award-ceremony-video\\

namespace: industry\
title: "Award Ceremony Video"\
description: "Generates a 15-second cinematic award ceremony video — the host takes the stage to announce the winner, a spotlight finds them in the crowd, they walk up to the podium and accept the award, and the LED screen reveals the name and the award. Winner/host dual-character identity lock, multi-camera broadcast feel. For use with generate_image_v3 + generate_video_v3."\
version: 1

# award-ceremony-video

Use this skill when creating personalized honor/fun videos of the "award ceremony" type. One 15-second cinematic one-shot: the host announces on stage → the spotlight sweeps to the winner in the crowd → they stand and walk to the podium → receive the award → the LED screen lights up with the name and the award. **Image order = identity order: the first image = the winner =** `@image_1`**, the second image = the host =** `@image_2`**; swapping them would swap "the announcer" and "the one going on stage."**

> Adapted for this environment: the source is a MUAPI/Seedance 2.0 image-to-video recipe, with the wording rewritten under MIT. Seedance → `generate_image_v3` (character anchors) + `generate_video_v3` (image-to-video, ≤15 seconds per call); `@image_1/@image_2` → `reference_nodes` + `{{NodeKey}}` in the prompt; technical specs (`aspect_ratio`/`resolution`/`duration_sec`/generated audio) go in fields, not in the prompt body.

## Inputs

| Name | Required | Default | Description |
| --- | --- | --- | --- |
| Winner photo | Yes | — | A clear frontal face photo. Used as `@image_1` (the first image); identity strictly locked throughout the video. |
| Host photo | Yes | — | A clear frontal face photo. Used as `@image_2` (the second image); the only host on stage. |
| Winner's name | No | Olivia | Spoken aloud by the host, and rendered on the LED screen above "THE BEST ACTOR". Confirm the spelling with the user before generating (it appears in both the audio and on the LED screen). |
| Award name | No | THE BEST ACTOR | The award title displayed on the LED screen. |

## Workflow

### 1. Confirm inputs

If either photo is missing → ask the user to upload it first. Before generating, confirm the winner's name and the award name — both will appear in the final video (audio + LED screen text), and a wrong spelling means the video has to be re-rendered.

### 2. Register the two character anchors

Use `generate_image_v3` to produce one stable character reference image each for the winner and the host, to serve as persistent identity anchors (winner `{{Winner}}`, host `{{Host}}`). **Order is identity**: the winner's anchor goes into `reference_nodes` first (mapped to `@image_1`), the host's second (mapped to `@image_2`). If both already have reusable anchors, reuse their node_key directly and skip re-creation.

### 3. Generate the final video

Use `generate_video_v3` for image-to-video and produce the finished video in one step: pass `reference_nodes` in the order \[winner, host\]; `aspect_ratio=16:9`, `resolution=720p`, `duration_sec=15`, with generated audio enabled. The prompt covers the five aspects below + the 15-second timeline:

**Style & tone**: Hyper-realistic live-action award ceremony scene, multi-camera broadcast feel — cutting between polished TV broadcast camera positions and intimate handheld documentary shots; Oscar/Grammy-level production values; genuine human reactions, no overacting.

**Lighting**: A grand indoor awards venue. Dramatic stage lighting — warm-gold spotlight on stage, cooler ambient light over the audience, broadcast camera lights, colored light cast by the LED screen. The moment the winner is announced — a beam of warm light sweeps across and locks onto the winner in the crowd.

**Scene**: A top-tier awards venue on the scale of the Grammys/Oscars. A big stage with towering LED screens, an elegant podium, a live orchestra pit, thousands of formally dressed attendees seated in rows, media cameras lining both sides of the aisle, overhead big screens playing the live feed — the whole venue exudes grandeur and scale.

**Strict identity lock**:

- `@image_1` the winner "{name}" — @image_1 as the strict identity: formally dressed, no sunglasses, face and build unchanged; initially seated among the formally dressed crowd in the audience.
- `@image_2` the host — @image_2 as the strict identity: the sole host at the podium; exact face/build/features preserved; formally dressed, face and build unchanged.

**Audio**: Elegant orchestral background music, the host's mic voice projected through the venue speakers, crowd murmur that then bursts into applause and cheers, chairs shifting, footsteps up to the stage, the trophy/medal being handed over, emotional reactions from the audience.

**15-second timeline (re-state the identity anchors at every point across shots to prevent drift)**:

- **0–3s Announcement**: Broadcast close-up on @image_2's face (tight, cinematic), standing at the podium mic under a warm-gold spotlight, composed and charismatic, deliberately building suspense; holding an envelope/card, one last glance at it, eyes straight into the lens, a beat of silence, then leaning into the mic to slowly say "And the winner is..."; the camera stays locked on @image_2's face — lips, expression, tension; crowd murmuring in the background.
- **3–6s The winner**: Hard cut to the audience — a low-angle broadcast camera pushes through the rows of seats and finds @image_1 seated among the guests, relaxed and unsuspecting; @image_2's voice keeps booming the name through the speakers; a spotlight suddenly locks onto @image_1 from above, their expression shifting from genuine shock (eyes wide, mouth slightly open) to an unguarded smile, glancing left and right at those nearby in disbelief; applause and cheers erupt across the house, people around standing to clap and pat their shoulder.
- **6–9s Standing and walking**: @image_1 straightens up, composes themselves, and stands; the handheld documentary camera immediately picks them up from the aisle — moving forward with them toward the stage, slightly shaky, close-in, real; applause keeps thundering; the overhead broadcast screen cuts to a live shot of their face; @image_1 walks forward with composure — formal attire crisp, posture straight, expression warm and slightly moved.
- **9–12s Reaching the stage**: The handheld camera follows @image_1 up the steps, and the bright stage spotlight hits full as they step on; @image_2 comes forward from the podium with a warm smile, medal held in both hands; @image_1 reaches the podium, takes it with both hands, looks down at it for a beat — a real moment; the two share a natural smile and a brief handshake; behind them the giant LED screen: a large portrait of @image_1's face, their name rendered in bold, elegant type "{name}", with "{award name}" beneath; the screen glowing, celebratory graphics pulsing across it.
- **12–15s Freeze frame**: The camera settles into a full-stage broadcast wide shot — @image_1 standing at the podium holding the medal, @image_2 standing beside them, the LED wall behind blazing with their name and face; the spotlight locked on @image_1; applause fills the venue, the standing ovation rippling outward in waves; @image_1 raises the medal slightly toward the crowd, smile composed and sincere; @image_2 leading the applause beside them; the final frame freezes — full stage, blazing LEDs, roaring crowd, @image_1 standing at the center; no fade to black.

Once the video is generated, deliver this 15-second final cut to the user.

## Trigger words

Award ceremony, awards video, Oscars video, Grammy ceremony, best actor award, winner announcement video, red carpet award; award ceremony, awards show video, oscars video, grammy ceremony, best actor award, winner announcement video, red carpet award.

## Related (boundaries, not dependencies)

Boundaries (do not use this skill; route elsewhere): inserting yourself into iconic scenes/sports highlights → sports-self-insert; a still photo with a celebrity → celebrity-selfie.\
The cross-shot identity-locking method is inlined and self-contained in this skill; if the same character persona also needs to be reused elsewhere, you can load `character-consistency` alongside and keep using the same anchors (optional, not required).