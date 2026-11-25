---
name: lifestyle-travel-vlog
description: "Lifestyle travel memory vlog: turn people, cities, and moods into Asian travel footage that feels like a real phone photo album"
---

## 1. Default Invocation Principles

### When the user asks to "generate an image / create an image / make an image directly"

Do not output prompts, do not over-explain, directly invoke the image generation tool.

Image output order:

```text
Solo vlog: output the solo character design sheet first
Couple vlog: output the couple relationship board first
Friends/family: output the multi-person relationship board first
12-grid: only output the 12-grid when the user explicitly asks for a vibe check / 12-grid / collage
Snapshot image: only output a single snapshot when the user explicitly requests a cover / snapshot / low-quality photo
```

### When the user asks for "prompts"

Output copyable final prompts, do not generate images directly.

### When the user asks to "analyze / blend / fix"

Provide a structural assessment first, then updated rules or a fixed version.

---

## 2. What Not to Do

By default, do not:

- Do not generate complete video files directly
- Do not edit videos
- Do not make cinematic trailers
- Do not make travel promotional videos
- Do not make overly retouched portrait photography
- Do not make commercial-ad-style content
- Do not make gimbal-stabilized blockbuster camera moves
- Do not generate dialogue, spoken lines, voiceover, or subtitles by default

---

## 3. Single-Run Lifecycle

On each invocation, strictly follow this order:

```text
1. Determine what the user wants: generate a character / generate a couple / generate a 12-grid / generate vlog prompts / generate images directly / analyze samples / fix test results
2. Determine character structure: solo / couple / friends / family
3. Generate character assets: character master design, character design sheet, or relationship board
4. Generate relationship setup: couples, friends, and family require an explicit relationship state
5. Generate character video lock words
6. Parse location, theme, visual mode, duration, aspect ratio, sound
7. Generate location lifestyle details
8. If needed, generate a 12-grid memory collage as the aesthetic confirmation layer and shot pool
9. Extract 6–7 key memory points from the 12-grid and convert them into 15-second video shots
10. Choose the video mode: Realcam rough authentic vlog / Music Travel Montage
11. Generate the final prompts or generate images directly
12. No dialogue by default; convey emotion only through actions, laughter, ambient sound, and shot interruptions
13. Run QA checks
14. Provide fixes based on test feedback
```

---

## 4. Input Parameters

Users may provide only part of the information; missing items are auto-filled. Do not ask repeatedly.

```text
Characters: @image1 / character prompt / user-uploaded character image / new characters to be generated
Relationship: solo / couple / best friends / friends / family
Location: Tokyo / Okinawa / Korean countryside / Indonesian islands / Hong Kong night streets / Yunnan small town / any Asian travel destination
Theme: summer roaming / island vacation / night market / festival / city travel / countryside summer retreat / couple memories / solo travel
Visual mode: character design sheet / relationship board / 12-grid / rough authentic vlog / music montage vlog / snapshot image
Duration: default 15 seconds
Aspect ratio: video defaults to 16:9; character design sheet defaults to 4:5; 12-grid defaults to 4:5 or 3:4
Sound: default natural ambient sound, no dialogue, no subtitles, no voiceover
Platform: Xiaohongshu / Douyin / Bilibili / Shorts, optional
```

Default values: relationship=solo; theme=travel life moments; video mode=Realcam rough authentic vlog; duration=15 seconds; video aspect ratio=16:9; sound=natural ambient sound, no dialogue.

---

## 5. Character Structure Determination

### Solo Mode

Applies to solo travel vlogs, solo city roaming, solo island vacations, solo countryside travel, solo travel collages, solo snapshots.

Output: 1 character master design, 1 character design sheet, 1 video character lock word.

### Couple Mode

Applies to couple travel, two-person travel memories, couple 12-grid collages, couple vlogs, summer festival for two, seaside memories for two.

Output: male character master design, female character master design, couple relationship setup, couple relationship board, two-person video lock words.

### Friends / Best Friends Mode

Applies to two girls traveling, two guys traveling, three-person friend groups, small-group travel memories.

Output: 2–4 character master designs, group relationship setup, multi-person relationship board, multi-person video lock words.

### Family Mode

Applies to parent-child travel, family travel memories, travel with elders and young people together.

Output: family member basic setups, family relationship setup, family relationship board, family video lock words.

---

## 6. Character Generation Layer

Characters must be generated or locked before any video, collage, or snapshot.

The character master design should include: gender, age range, regional/cultural feel, face shape, facial features, hairstyle, skin tone, body proportions, temperament, outfit, makeup/no-makeup state, in-travel state, and avoid-list.

### Solo Character Design Sheet

Used to generate a character reference image and lock the character.

Image structure: face close-up on the left or top; front full-body, side full-body, and back full-body on the right or bottom; background pure white, off-white, or minimalist; focus on face, hairstyle, skin tone, body proportions, and clothing; no text labels.

### Couple Relationship Board

Used to generate two-person reference assets for couple travel.

Image structure: male solo view, female solo view, two-person standing full-body, small frames of natural two-person interaction; height difference, outfit pairing, and intimacy state clearly shown; clean background that doesn't compete with the characters; no text labels.

### Multi-Person Relationship Board

For best friends, friends, and family. Each person clearly distinguishable; group relationship clear; natural interactions; coordinated outfits; clear height and body-type hierarchy; clean background that doesn't compete with the characters; no text labels.

---

## 7. Character Video Lock Words

### Solo Video Lock Words

```text
@image1 = the primary subject.

Throughout the entire video, preserve the exact face, identity, hairstyle, skin tone, body proportions, outfit, and overall temperament from @image1. Keep the same outfit and accessories for the whole video. The character is an ordinary real-life traveler, not posed, not retouched, not idolized, not commercialized. Do not change the face, do not change the hairstyle, do not change the clothes, do not change the skin tone, do not alter the sense of age or body proportions.
```

### Couple Video Lock Words

```text
@image1 = Person A
@image2 = Person B

Throughout the entire video, preserve each person's exact face, identity, hairstyle, skin tone, body proportions, and overall temperament from @image1 and @image2. For the whole video, both people maintain the same couple identity and relationship, with a stable height difference, outfit pairing, and interaction state. Do not swap faces, do not change either person's hairstyle, skin tone, sense of age, body proportions, or relationship dynamic. Do not turn the two into strangers, posed models, or an advertising couple.
```

### Multi-Person Video Lock Words

```text
Throughout the entire video, preserve each person's exact face, identity, hairstyle, skin tone, body proportions, and overall temperament. Keep the same group relationship, the same outfit logic, and a stable interaction state for the whole video. Do not swap people, do not randomly change faces, do not alter the group relationship.
```

---

## 8. Mode Determination Rules

- Character design sheet mode: generate a character first, character creation, character design sheet, solo character, character master, lock character.
- Couple relationship board mode: couple, male and female leads, one man and one woman, two-person relationship, couple setup, couple travel.
- 12-grid memory collage mode: 12-grid, collage, vibe check first, a set of images first, travel photo collection, album feel, memory board, moodboard.
- Realcam rough authentic vlog mode: low-quality DV, flip phone, authentic vlog, handheld, rough, natural ambient sound, no music, home video, travel life moments.
- Music Travel Montage mode: music editing, fast-paced, Tokyo travel vlog, travel vlog, 15-second montage, beat-synced fast cuts, city travel, landmark check-ins.
- Accidental Snapshot mode: snapshot, cover, flash, blurry phone photo, quick exit from frame, low-quality phone photo, accidentally captured.

---

## 9. Visual Modes

### Realcam Rough Authentic Vlog

Suited for countryside, islands, small towns, slow living, solo travel, relaxed couple travel, tired summer roaming.
Photography terms: late 2000s personal digital camera / handheld camcorder vlog aesthetics. Handheld shooting, slight to moderate shake, imperfect composition, occasionally cropping subjects at the frame edges, autofocus hunting, lens breathing, slight exposure fluctuation, soft faded film look, low contrast, slight grain, home video flaws.

Avoid: no posed stances, no stylish outfits, no perfect composition, no stabilizer, no cinematic charm, no modern color grading, no commercial-ad feel, no retouched skin, no overacting, no background music, no subtitles, no dialogue.

### Music Travel Montage

Suitable for Tokyo, Seoul, Hong Kong, Osaka, Bangkok, Taipei, Shanghai, landmark-dense city travel, and platform short videos.

Photography terms: 26mm phone lens, deep depth of field, real skin texture, neutral phone color science, unedited snapshot feel, slight HDR, true nighttime exposure, beat-synced fast cuts, natural motion reactions.

Avoid: no cinematic color grading, no studio lighting, no light trails, no exaggerated motion blur, no commercial-ad feel, no perfect blocking, no tourism-promo feel, no dialogue by default.

### 12-Grid Memory Collage

Collage of 12 casual snapshot photos, travel memories, faded film look, low contrast, slight grain, slight blur, handheld slow shutter, natural cropping, soft highlights, slightly lifted shadows, like a summer slipping away, like a journey from memory.

### Accidental Snapshot

Low-quality smartphone photo, subject moving quickly out of frame, motion blur, automatic flash, blown-out highlights, deep dark shadows, ghosting artifacts, loose composition, authentic low-quality phone camera look.

---

## 10. Location Detail Generation Rules

Don't just write a location name; you must expand it into everyday-life details.

Format: region + specific space + ground material + architectural details + local objects + plants + animals + crowds + weather + sounds + avoid list.

Examples:

- Japanese countryside summer: old-style Japanese wooden house, tatami rooms, sliding doors, old electric fan, engawa wooden corridor, distant mountain village views, shallow river, summer watermelon, soda bottles, bicycle, tall grass, evening sky, small fireworks in the distance, summer insect sounds, curtains blowing in the wind.
- Korean countryside: dirt/gravel paths, moss-covered stone walls, hanok houses, aged clay-tile roofs, wooden fences, overgrown weeds, twisted old trees, stone water trough, hanging dried chili peppers, cracked stone steps, ceramic sauce jars, roosters roaming freely, morning cooking smoke, villagers chatting in the distance.
- Indonesian island: wooden pier, small fishing boats, pale green seawater, low-rise guesthouses, palm trees, sandy paths, small plastic-chair cafes, warung stalls, stray dogs, seabirds, distant boat engine sounds, humid sea breeze, sun-faded signs.
- Tokyo city: Tokyo Tower, Shibuya crowds, convenience-store cold white fluorescence, vending machines, subway window reflections, shrine torii gates, lantern-lit alleys, rooftop night views, street signs, pedestrian flows at intersections, straight-out-of-phone exposure, slight HDR.
- Japanese summer festival: crowds in yukata, paper lanterns, fireworks, night market food stalls, candy apples, shaved ice, goldfish scooping, shrine approach path, soft orange lighting, pale navy-blue night, low contrast, humid summer night air, distant crowd sounds.

---

## 11. Clothing and Body State Rules

Clothing must not be described merely as pretty; describe the travel state.

Available states: slight wrinkles, sweat marks, wind-tousled hair, a few strands stuck to the face and neck, water-splashed sandals, sun-reddened shoulders, natural fatigue, relaxed travel vibe, completely unadorned.

Clothing templates:

- City travel version: loose hoodie, oversized jacket, casual trousers, sneakers, crossbody bag.
- Island vacation version: swimwear cover-up, linen shirt, wide-leg pants, brown leather sandals, small gold hoop earrings.
- Countryside wandering version: loose linen shirt, dust-colored trousers, sandals, natural sweat marks, messy hair.
- Summer festival version: yukata, wooden geta sandals, holding a snack, hair simply tied up, slightly messy.
- Night market casual version: light top, short skirt or loose pants, small carry bag, holding a drink or snack.

---

## 12. 12-Grid → Video Conversion Rules

The 12-grid is not the final video; it is an aesthetic confirmation layer and a pool of shot material.

Select 6–7 key memory points from the 12-grid and convert them into timecoded shots within the 15 seconds.

Mapping rules:

```text
Close-up of the subject → opening selfie / emotional shot
Location empty shot → environment establishment
Food and drinks → everyday-life details
Water, wind, sunlight → tactile interaction
Bicycle, walking, transport → movement shots
Sunset, night views, fireworks → lingering ending
```

Do not cram all 12 images into the 15-second video.

---

## 13. Default No-Dialogue Rule

This Skill does not generate dialogue by default.

Realcam: keep only natural ambient sounds: wind, footsteps, ocean waves, birdsong, insect sounds, dog barks, market chatter, objects clinking, camera rubbing sounds, the subject's natural laughter. No background music, no subtitles, no dialogue, no on-camera speech, no narration.

Music Montage: may have music beats, may retain a small amount of ambient sound. No dialogue by default. The subject's emotions are conveyed through actions, expressions, and editing rhythm.

Only enable the dialogue module when the user explicitly requests "add a line / add dialogue / add on-camera speech / add narration". Otherwise, do not arrange for the subject to speak full sentences.

---

## 14. Video Ending Action Library

By default, do not end with dialogue; choose from the following options:

```text
The subject leans close to the camera, smiles naturally, waves gently, and the recording cuts off abruptly.
The subject covers the lens with a hand, and the frame goes black.
The camera tilts down to capture footsteps and the ground, then stops.
The wind tousles her hair; she brushes it aside with a smile, and the frame cuts.
She looks back at the camera with a smile, then turns and keeps walking.
The camera suddenly tilts to the sky, leaves, or the sea surface, and recording ends.
Amid nighttime fireworks, she looks back with a smile, and the camera gently drifts downward.
```

---

## 15. Realcam Vlog Master Template

```text
Scene – Seedance 2.0 | 15-second personal travel life clip

@image1 = main subject.
@image2 = mood reference, optional.

Throughout, preserve the exact face, hairstyle, skin tone, body proportions, clothing, and overall aura of the person in @image1. Keep the same outfit and accessories for the entire video. The person is an ordinary traveler in real life — not staged, not retouched, not idolized, not turned into an ad. Do not change the face, do not change the hairstyle, do not change the clothes, do not change the skin tone, do not alter the sense of age or body proportions.

[Character and Clothing]
{character lock terms}
{clothing state terms}
Clothing carries real travel marks: slight wrinkles, sweat marks, wind-tousled hair, water-splashed sandals, natural fatigue or a relaxed vibe. No fashion-editorial look.

[Location]
{location name}
{location life details}
Emphasize real traces of local life, old objects, ground materials, local plants, animals, stalls, architectural details, and natural weather. Avoid a modern commercial-ad feel.

[Photography]
Late 2000s personal digital camera / handheld camcorder vlog aesthetics. Handheld shooting, slight to moderate shake, imperfect composition, occasionally cropping subjects at the frame edges, autofocus hunting, slight exposure fluctuation, soft faded film look, low contrast, slight grain, home video flaws. No blockbuster-movie feel, no stabilizer, no commercial production quality.

00:00–00:02
Opening selfie shot: the subject is entering the location while moving, camera slightly tilted, the subject naturally looks at the camera or smiles.

00:02–00:04
Handheld follow shot from behind or from the side, showing local architecture, roads, stalls, or natural surroundings.

00:04–00:06
The subject interacts with water, food, flowers, stone walls, railings, merchandise, or local objects, with natural movements.

00:06–00:08
The subject has brief interactions with animals, shopkeepers, children, passersby, or natural details.

00:08–00:10
The subject continues moving through the location: wiping sweat, fixing hair, looking at a map, glancing around, or pushing a cart while walking.

00:10–00:12
The subject sits down to rest: drinking water, eating, flipping through postcards, maps, or notes, or gazing into the distance.

00:12–00:15
End with a messy selfie or a from-behind perspective. The subject smiles naturally, waves gently, or briefly covers the lens with a hand; alternatively, let the camera tilt naturally to the sky, leaves, the sea surface, or nighttime fireworks. The recording cuts off abruptly amid laughter. No clear spoken lines, no on-camera speech, no narration.

[Audio]
Use only natural ambient sound: {location ambient sounds}, footsteps, wind, distant voices, animal sounds, objects clinking, camera rubbing sounds, the subject's natural laughter. No background music, no subtitles, no dialogue, no on-camera speech, no narration.

[Avoid]
No posed shots. No fashion styling. No perfect composition. No stabilizer. No cinematic flair. No modern color grading. No commercial-ad feel. No retouched skin. No overacting. Do not suddenly switch face, hairstyle, clothing, skin tone, or body proportions.

[Aspect Ratio]
{16:9 / 9:16 / 3:4}
```

---

## 16. Music Travel Montage Master Template

```text
{City Name} TRAVEL VLOG — 15-Second Music Edit

@image1 = main subject.
Throughout, preserve the exact face, identity, hairstyle, skin tone, body proportions, and overall vibe of the person in @image1. Keep the same travel outfit and accessories for the entire video.

Subject: {person description}
Outfit: {city travel outfit}
Camera: 26mm phone lens, deep depth of field, real skin texture, neutral phone color science, unedited snapshot feel, slight HDR, realistic nighttime exposure. No cinematic color grading, no studio lighting, no light trails, no exaggerated motion blur effects.

00:00–00:01 Landmark selfie, low angle, landmark behind the person, sky or city lights slightly overexposed. Natural smile.
00:01–00:02 Walking through city crowds, turning the head to look at the camera. Background signs, streets, and crowds clearly visible. Fast cut on the beat.
00:02–00:03 Convenience store / snack shop / street stall, holding up food or a drink to the camera, natural expression.
00:03–00:04 Brief pause at a park / street corner / station, with a momentary flash of wind or ambient sound.
00:04–00:06 Food reaction shot, taking a bite or a sip, eyes widening, stepping back with a laugh.
00:06–00:07 In front of a vending machine / neon streetlight / shop window, mixed LED light on the face.
00:07–00:08 Transit shot: train window, bus window, taxi back seat, or subway platform, person looking out the window.
00:08–00:09 Local cultural spot: shrine, old street, bridge, temple, market entrance, or alley, person crossing the frame.
00:09–00:11 Signature visual shot: light show, observation deck, night view, exhibition, or a high vantage point in the city. Slightly slower pace, person looking up.
00:11–00:12 A major attraction appears; the camera tilts up from the person's face or turns to reveal the full attraction.
00:12–00:13 Night street or lantern-lit alley, following from behind, the person glancing back once.
00:13–00:14 Rooftop / seaside / bridge / intersection selfie, arm extended, city or natural scenery coming into view.
00:14–00:15 Ending with an unexpected interaction or a blooper: an animal, a friend, a passerby, wind, food, or a small accident creates a natural laugh. Fade out or hard cut to end.

[Audio]
Rhythmic music; a small amount of real ambient sound may be kept. No dialogue by default. The person expresses emotion through actions, expressions, reactions, laughs, waving, looking back, and selfie gestures.

[Avoid]
No commercial-ad feel. No movie-trailer feel. No excessive retouching. No heavy filters. No exaggerated influencer vibe. No perfect blocking. No tourist-promo-video feel. No dialogue, on-camera speech, or voiceover.
```

---

## 17. 12-Grid Memory Collage Master Template

```text
Generate a set of travel memory collages made up of 12 casual snapshots.

People: {person/relationship}
Location: {location}
Theme: {travel theme}

The images look like a collection of casually taken phone photos during a trip, not professional portraits, not a tourism promo. The photos include selfies, back views, streets, food, seaside/mountain/city night views, roadside shops, transit, partial hand movements, and accidentally blurred moments.

Overall a faded film look, low contrast, slight grain, slight blur, natural handheld framing, occasionally cropping the person at the edge. Soft colors, like a summer in memory or a trip fading into the past. The images carry a real sense of life, with imperfect compositions and a slight shakiness.

Avoid: professional photography, commercial blockbusters, movie posters, excessive sharpness, excessive retouching, strong HDR, posed portraits, uniform studio lighting, perfect composition.

Aspect ratio: {3:4 / 4:5 / 16:9}
```

---

## 18. Accidental Snapshot Master Template

```text
A low-quality casual smartphone snapshot.

People: {person/relationship}
Location: {location}
Action: {turning the head, looking back, running, raising a hand to block the lens, bursting into laughter, hair blown messy by the wind, about to walk out of frame}

The image looks like an accidentally captured moment. Loose composition, subject off-center, person possibly cropped, noticeable handheld shake, motion blur, auto flash causing blown-out highlights and deep dark shadows. Facial details slightly blurry but the overall sense of the person's identity is preserved. Low-quality colors, noticeable grain, obvious compression artifacts, like an old phone or an early digital camera.

Avoid: professional portrait, cinematic still, studio lighting, sharp focus, retouched skin, posed stance, fashion editorial, commercial-ad feel.

Aspect ratio: {3:4 / 4:5 / 16:9}
```

---

## 19. QA Check Rules

After every output, automatically check:

```text
1. Does the person keep the same face?
2. Is the hairstyle stable?
3. Is the outfit stable?
4. Are the body proportions stable?
5. Is the couple/multi-person relationship stable?
6. Does the location have real-life details?
7. Is it too cinematic?
8. Is it too commercial-ad?
9. Is it too stable, too clean?
10. Are the handheld imperfections sufficient?
11. Were dialogue, on-camera speech, or voiceover mistakenly generated?
12. Is the ending natural?
13. Do the 12-grid and the video share the same vibe?
```

---

## 20. Common Failure Fix Rules

- Face changing: strengthen the character lock, reduce drastic frontal-face switches, emphasize the same face, same hairstyle, same outfit, same age feel, same body proportions.
- Couple doesn't look like a couple: strengthen the couple's relationship: consistent height difference, natural intimacy, coordinated outfits, restrained and realistic interactions; no model-photoshoot couple or ad-couple vibe.
- Too cinematic: remove cinematic, film still, dramatic lighting, stable tracking shot. Replace with handheld vlog, imperfect framing, focus searching, home video flaws.
- Too commercial-ad: add sweat marks, wrinkles, messy stray hairs, everyday movements, accidental crops, natural tiredness. Reduce perfect lighting and retouched skin.
- Dialogue appears: delete all dialogue descriptions. The person only naturally laughs, waves, covers the lens, the camera swings away, or the recording cuts off abruptly. Keep ambient sound, footsteps, wind, laughter, and camera rustling noise. No on-camera speech, no voiceover, no subtitles.
- Footage too blurry: reduce the roughness from heavy to moderate. Keep slight handheld shake, grain, and exposure fluctuation; reduce severe motion blur.
- Location too empty: add local life objects, passersby, animals, stalls, old buildings, ground textures, signage, wind, voices, and environmental details.
- 12-grid too cluttered: pick only 6–7 key memory points for the video; do not cram all 12 images into the 15-second video.

---

## 21. Version Notes

Current version: V1.3: person-first + 12-grid preview + no dialogue by default.

Roadmap: V1.4 adds a larger Asian location library; V1.5 adds a test recycle sheet and auto-fix templates; V2 adds a stronger 12-grid-to-video converter; V3 adds multi-city batch generation; V4 adds account-based continuous content production with the same person.