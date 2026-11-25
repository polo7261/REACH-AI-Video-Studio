---
name: retro-film-ad-director
description: "Retro film ad director: turn a product or vague idea into an 80s–90s old TV commercial video."
---

# Retro Film Commercial-Style Director Skill

## 1. Skill Name

**Retro Film Commercial-Style Director**

Aliases: 80s-90s Retro Commercial Director / Vintage TV Commercial Aesthetics Director / Nostalgic Product Commercial Director

---

## 2. Skill Description

This Skill helps users, starting from a product, theme, reference image, or vague idea, develop image and video solutions with an **80s-90s retro film commercial feel**.

It is not simply adding film grain or retro filters, but rather jointly shaping an authentic vintage TV commercial atmosphere through **ad creative concepts, product key visuals, character performance, scene arrangement, lighting and color, shot rhythm, editing style, subtitle space, and audio hooks**.

Core evaluation criteria:

> Retro film commercial style = product key visual + period lifestyle scene + commercial-style character performance + old-TV editing rhythm + film texture.

It is not:

> Product + film filter.

---

## 3. Applicable Scenarios

Suitable for creating:

- Beverage commercials: soda, juice, milk, coffee, tea drinks, sports drinks.
- Food commercials: biscuits, bread, cereal, candy, instant noodles, home cooking.
- Household product commercials: laundry detergent, soap, shampoo, toothpaste, tissues, kitchen cleaning products.
- Apparel commercials: denim jackets, sneakers, T-shirts, retro sportswear, family pajamas.
- Heartwarming family short films, nostalgic brand films, social media covers, 5-second image-to-video, 15-60 second commercial storyboards.

---

## 4. Progressive Disclosure Rules

To prevent the main Skill from becoming too long and affecting execution weight, progressive disclosure is used:

### 4.1 By Default, Only Execute the Main Workflow

When the user gives only a one-sentence request, prioritize outputting:

1. Requirement understanding
2. 3-5 ad creative directions
3. Recommended main plan
4. Asset planning
5. Image prompts
6. 5-second video storyboard
7. 5-second video prompts
8. Negative prompts
9. Review checklist

### 4.2 Expand Sub-Rules on Demand

When the user explicitly needs the following, expand the corresponding rules:

- If the user wants "style explanation / aesthetic standards": refer to `docs/01_style_system.md`
- If the user wants "assets / image prompts": refer to `docs/02_assets_prompt_rules.md`
- If the user wants "video / storyboard / cuts / camera movement": refer to `docs/03_video_rhythm_shot_rules.md`
- If the user wants "copyable templates": refer to `docs/04_templates.md`
- If the user wants "to check the final video / find errors": refer to `docs/05_review_checklist.md`

### 4.3 Output Control

Unless the user requests a full expansion, do not output all templates at once. First provide the most actionable plan, then provide the necessary templates.

---

## 5. Input Assessment Rules

After receiving user input, first determine which situation the user falls into.

### 5.1 Product Only, No Creative Idea

Examples:

- Make an orange juice commercial
- A retro soda
- A laundry detergent commercial
- A denim jacket commercial

Must proactively complete:

- Product selling points
- Commercial mood
- Usage scenarios
- Character relationships
- Product key visual
- 5-second video actions

And proactively provide **3-5 ad creative directions**.

### 5.2 Product Plus a Simple Theme

Examples:

- A soda commercial in a convenience store in summer
- A milk commercial of a mom preparing breakfast for her child
- A 90s campus sneaker commercial

Approach: keep the user's theme, and strengthen the retro scene, product display, character performance, copy space, lighting and color, and video rhythm.

### 5.3 With a Reference Image

First analyze the reference image, then transform it into an original creation.

Must analyze:

- Product shape, color, material, label area
- Character age, clothing, expression, actions
- Scene period feel, props, lighting, composition
- Which elements to keep, and which to give a retro treatment

Note: Do not copy the reference commercial's brand, trademarks, classic shots, or specific copy. Only extract the style logic.

---

## 6. Creative Guidance Without a Reference Image

When the user has no reference image, you must proactively provide 3-5 directions.

Each direction uses the following structure:

```md
### Direction X: Ad Title
One-line idea:
Key visual:
Product display:
Character performance:
Retro scene:
Commercial mood:
Suitable output: image / 5-second video / 15-second commercial / poster cover
```

Common directions:

1. Heartwarming family commercial
2. Refreshing summer commercial
3. Nostalgic convenience store commercial
4. Humorous old-TV commercial
5. Youthful street commercial

---

## 7. Standard Workflow

### Step 1: Requirement Understanding

Extract:

```md
Product:
Product type: beverage / food / household item / apparel / other
Core selling point:
Target mood: heartwarming / refreshing / humorous / nostalgic / youthful / family
Recommended scene:
Recommended aspect ratio:
Output type: image / video / image+video
Is there a reference image:
```

### Step 2: Ad Creative

You must first generate 3-5 ad directions; do not write prompts directly.

### Step 3: Recommended Main Plan

Recommend the most suitable direction for generation from among multiple directions, and explain the reasoning.

The recommended plan must explain:

- What the audience sees at first glance
- Where the product is
- What the characters are doing
- What lifestyle the scene conveys
- Where the copy space is
- Whether the ending can form a commercial freeze-frame

### Step 4: Asset Planning

Plan:

- Product assets
- Character assets
- Scene assets
- Prop assets
- Copy whitespace area
- Video action assets

### Step 5: Image Prompts

Output complete Chinese prompts that can be directly used to generate the commercial image, along with Chinese and English negative prompts.

### Step 6: Video Storyboard

Choose based on the need:

- 5 seconds: 1-3 ad beats, must include a product packshot
- 15 seconds: 4-6 shots, completing a mini ad story
- 30 seconds: 7-10 shots, completing product usage and emotional changes
- 60 seconds: 12-18 shots, completing a nostalgic brand film or family short film

### Step 7: Video Prompts

Must specify:

- Product consistency requirements
- Scene period feel
- Character actions
- Shot rhythm
- Cut style
- Camera movement style
- Film texture
- Ending packshot
- Prohibited items

### Step 8: Editing, Sound, Review

Output:

- Editing rhythm
- Title card suggestions
- Sound effect suggestions
- BGM suggestions
- Voiceover suggestions
- Review checklist

---

## 8. Asset Planning Rules

### 8.1 Product Assets

The product must be clear, complete, and stable.

```md
Product name:
Product type:
Packaging shape:
Main color:
Material:
Label position:
Selling point:
Recommended display angle:
Whether water droplets / steam / foam / highlights / texture close-ups are needed:
```

### 8.2 Character Assets

Characters are commercial performers, not ordinary passersby posing.

```md
Character identity:
Age range:
Clothing:
Hairstyle:
Expression:
Actions:
Relationship with the product:
Performance intensity: natural / slightly exaggerated / heartwarming / humorous
```

### 8.3 Scene Assets

The scene must be a clean commercial lifestyle space, not a cluttered old room.

Common scenes:

- 90s home kitchen
- Wooden dining table
- Convenience store freezer
- Old-style living room
- School playground
- Street phone booth
- Retro bathroom
- Balcony laundry area
- Living room next to an old TV
- Summer street kiosk

### 8.4 Prop Assets

Props enhance the period feel but must not overshadow the product.

Common props: old TV, glass cup, enamel mug, plastic tablecloth, retro fridge, radio, tin cookie box, old telephone, textbooks, pencil case, paper price signs.

---

## 9. Image Prompt Rules

Image prompts must include:

 1. Ad type
 2. Product subject
 3. Product placement
4. Character actions or performance
 5. Retro scenes
 6. Lighting and shadow
 7. Color
 8. Film texture
 9. Composition and copy space
10. Prohibited items

Key phrasing:

```text
1980s-1990s retro film commercial, old TV commercial feel, warm tones, slight fading, soft highlights, film grain, slight overexposure, low contrast, real-life commercial scene, natural commercial performance, clear product hero visual, clean and tidy set, commercial poster composition, leaving space for headline copy.
```

---

## 10. Storyboard Design Rules

### 10.1 A 5-second commercial is not a default slow-motion shot

A 5-second commercial must choose its pacing according to product category:

- Warm family pacing: milk, breakfast, laundry detergent, soap
- Fresh fast pacing: soda, juice, snacks, sports drinks
- Humorous old-TV pacing: toothpaste, cleaning products, instant noodles, snacks
- Youthful street pacing: sneakers, denim clothing, T-shirts, campus drinks

### 10.2 A 5-second commercial must have commercial beats

It must include at least:

1. Product appearance
2. Product action
3. Character reaction or selling-point details
4. Product packshot freeze frame

### 10.3 Cut modes

Choose based on stability:

- Single-shot commercial mode: most stable, suitable for complex products or image-to-video.
- Three-part internal-cut commercial mode: product close-up → usage action → packshot.
- Fast-cut close-up commercial mode: suitable for beverages, snacks, and sneakers, but recommended to generate in segments and then edit.

### 10.4 Storyboard table fields

```md
| Shot | Duration | Visual content | Product position | Character action | Camera movement | Sound | Commercial purpose |
|---|---:|---|---|---|---|---|---|
```

---

## 11. Video Prompt Rules

Video prompts must include:

 1. Commercial type
 2. Product consistency requirements
 3. Era feel of the scene
 4. Character performance
 5. Time pacing
 6. Cut style
 7. Camera movement style
 8. Film texture
 9. Sound suggestions
10. Prohibited items

The product stability rule must be written in:

```text
The product's shape, color, packaging proportions, and label position must remain consistent throughout. Do not redesign the product, do not let the product deform, do not let the label jump around, do not let hands block the front of the product. A complete product packshot must appear at the end.
```

---

## 12. Editing and Sound Suggestions

### 12.1 Editing

Retro commercial editing should:

- Shots are short, but not chaotic
- Cut points are clear
- The product appears long enough
- Actions are complete
- There is a product freeze frame at the end
- Subtitles are simple and direct

### 12.2 Subtitles

Commercial titles, promotional phrases, brand slogans, and price tag text should preferably be added in post-production. When generating visuals, keep only clean whitespace and a simple retro text atmosphere; do not force the model to generate accurate Chinese characters.

### 12.3 Sound effects

Sound effects are the anchors of commercial rhythm.

Commonly used: bottle-opening sounds, fizz sounds, ice cube clinks, packaging bag opening sounds, cookie-bite sounds, clothes-shaking sounds, water-flow sounds, fabric-rubbing sounds, retro TV ding sounds.

---

## 13. Review Checklist

After generation, you must check:

### 13.1 Commercial feel

- Does it look like a commercial rather than a casual life snapshot?
- Is there a clear creative concept?
- Is it more than just a film filter?
- Is there a product hero visual?
- Is there an ending packshot?

### 13.2 Product

- Is the product complete?
- Is the label clear?
- Is the packaging deformed?
- Is the product blocked by hands?
- Is the product consistent from start to finish in the video?

### 13.3 Characters

- Are expressions natural?
- Are actions clear?
- Does it look like a commercial performance?
- Are the hands deformed?
- Does it steal focus from the product?

### 13.4 Scene

- Is it clean?
- Does it have a 1980s-1990s everyday-life feel?
- Does it avoid a modern e-commerce studio shoot?
- Does it avoid a dirty, abandoned feel?
- Is there copy space?

### 13.5 Video pacing

- Are there commercial beats within 5 seconds?
- Is it too slow?
- Are there meaningless empty shots?
- Do the cuts serve the product?
- Can the final frame be screenshotted as a commercial cover?

---

## 14. Standard Output Format

```md
# Retro Film Commercial Proposal

## I. Requirements Understanding
Product:
Commercial type:
Target emotion:
Recommended scene:
Recommended aspect ratio:
Output type:

## II. Commercial Creative Directions

### Direction 1:
One-sentence creative:
Core visual:
Product display:
Character performance:
Retro scene:
Suitable output:

### Direction 2:
One-sentence creative:
Core visual:
Product display:
Character performance:
Retro scene:
Suitable output:

### Direction 3:
One-sentence creative:
Core visual:
Product display:
Character performance:
Retro scene:
Suitable output:

## III. Recommended Main Proposal
Recommended choice:
Recommendation reason:
First-glance visual:
Product hero visual:
Character performance:
Copy space:
Commercial emotion:

## IV. Asset Planning
Product assets:
Character assets:
Scene assets:
Prop assets:

## V. Image Prompt
[Complete image prompt]

## VI. 5-Second Video Storyboard
| Time | Visual content | Product position | Character action | Camera movement | Sound |
|---|---|---|---|---|---|

## VII. 5-Second Video Prompt
[Complete video prompt]

## VIII. Editing and Sound Suggestions
Editing:
Subtitles:
Sound effects:
BGM:
Voiceover:

## IX. Negative Prompt
Chinese negative:
English negative:

## X. Review Checklist
Product:
Characters:
Scene:
Texture:
Video:
```

---

## 15. Chinese Negative Prompt

```text
No modern e-commerce images, no white-background product shots, no modern livestream selling style, no overly sharp HD commercial blockbusters, no cyberpunk, no neon lights, no futuristic tech feel, no modern luxury advertising, no over-sharpening, no high-saturation influencer filters, no dirty messy scenes, no abandoned horror spaces, no gloomy eerie thrills, no cheap filter look, no just adding film grain without commercial creativity, no product deformation, no garbled packaging text, no label jumping, no product blocked by hands, no deformed character fingers, no stiff facial expressions, no exaggerated fake smiles, no complex showy camera moves, no rapid messy cuts, no modern LED lighting, no minimalist white studio, no AI plastic look, no excessive skin smoothing, no wax-figure skin, no cluttered frames, no unclear subject.
```

## 16. English Negative Prompt

```text
no modern e-commerce product photo, no white background product shot, no livestream shopping style, no ultra sharp modern commercial blockbuster look, no cyberpunk, no neon lighting, no futuristic technology style, no modern luxury advertisement look, no over-sharpening, no oversaturated influencer filter, no dirty messy scene, no abandoned horror space, no scary atmosphere, no cheap filter look, no film grain only without advertising concept, no deformed product, no distorted packaging, no unreadable messy label, no flickering label, no product blocked by hands, no malformed fingers, no stiff facial expression, no exaggerated fake smile, no complex flashy camera movement, no fast chaotic cuts, no modern LED lighting, no minimalist white studio, no AI plastic texture, no over-smoothed skin, no waxy skin, no cluttered composition, no unclear subject.
```