# Cinematic Visual Storytelling

## Core Methodology

### Framework 1: Layered Element Isolation

Treat every visual output as independently controllable layers:

- **Layer 1 (Character Identity)**: face, body proportions, skin tone — generated once as reference image, locked across all subsequent scene outputs
- **Layer 2 (Costume/Equipment)**: clothing, accessories, gear — can vary per scenario while maintaining identity consistency
- **Layer 3 (Environment)**: scene setting, architecture, landscape — varies based on narrative context
- **Layer 4 (Atmosphere)**: lighting, color palette, weather — driven by style routing logic
- **Layer 5 (Composition)**: camera angle, shot size, focal length simulation — varies to create visual rhythm

**Why this matters**: Locking character identity in a separate reference image prevents model drift across scene variations. Environment and atmosphere can be freely manipulated without corrupting character consistency. This is the foundational structure for serialized visual storytelling.

### Framework 2: Style-Driven Prompt Architecture

Style routing is a pre-generation decision tree that maps user intent to visual parameters:

**Input signals**: user's descriptive keywords (e.g., "冷寂" cold desolation, "压迫感" overwhelming scale, "废土" wasteland, "科技" high-tech)

**Routing logic**:

- Apocalyptic loneliness → low saturation cool gray-green, widescreen 2.39:1, destroyed urban environments, solitary figure at small scale
- Overwhelming creature scale → extreme low-angle perspective, subject occupies &gt;60% vertical frame, deep shadows, atmospheric haze for depth perception
- High-tech futurism → clean geometric forms, cyan/blue bioluminescent accents, wide-angle lens distortion, reflective metallic surfaces
- Cold noir atmosphere → high-contrast chiaroscuro, rain/wet reflections, desaturated palette with single accent color

**Parameter mapping**: Each style route translates to concrete technical specifications:

- Color: specific HSV ranges (e.g., H: 180-200° cyan, S: 40-60%, V: 30-50%)
- Composition: named shot types ("extreme low-angle hero shot", "wide environmental establishing", "tight medium close-up")
- Lighting: directional logic ("single high-key backlight", "diffused overcast ambient", "hard rim light with fill bounce")

### Framework 3: Model-Specific Constraint Adaptation

Different AI models have fundamentally different prompt processing capabilities. This framework ensures prompt structure matches model architecture:

**Midjourney (MJ)**:

- Character limit: hard cap 1024 characters, target &lt;800 to leave buffer
- Structure: comma-separated keyword phrases only, no subordinate clauses
- Order: \[subject + action\], \[shot size + angle\], \[environment\], \[camera + lens\], \[lighting\], \[color palette\], \[mood\], \[style anchors\]
- Forbidden: long descriptive sentences, stacked realism paragraphs, Chinese characters
- Realism condensing: replace full technical paragraphs with 5-6 tokens ("photorealistic, cinematic film still, clean deep shadows, dense midtones, filmic tonal range, optical sharpness")

**Seedream 5.0 Pro / Lib Image (image2)**:

- Supports longer natural language prompts with hierarchical structure
- Can handle technical photography terminology ("shallow depth of field", "bokeh", "chromatic aberration control")
- Mandatory quality suffix for image2: "Low ISO, no visible grain noise, no heavy film grain, no dirt, no mud spots, no mold marks, no dust spots, clean optical clarity"
- Supports resolution specifications and aspect ratio control

### Framework 4: Reference Image Propagation Logic

When a character/object reference image exists, all subsequent prompts must maintain visual DNA:

**Hard constraints**:

- Face structure: bone structure, eye shape, nose bridge, lip contour — zero tolerance for deviation
- Body proportions: height-to-head ratio, shoulder width, limb length — must match reference silhouette
- Signature details: scars, tattoos, facial hair, unique costume elements — must appear in all outputs

**Flexible dimensions**:

- Pose and gesture: can vary freely as long as body proportions remain consistent
- Lighting and color grading: can shift to match scene atmosphere without changing identity
- Camera angle: different perspectives are allowed but facial features must remain recognizable

**Technical implementation**: Use reference image placeholder `{{node_key}}` early in prompt structure. Follow with minimal identity reinforcement text (3-5 keywords max) rather than re-describing the entire character.

## Workflow

### 1. Preparation Stage

**Mandatory Two-Phase Confirmation** (cannot be skipped or merged):

**Phase 1 — Character Appearance Lock**

Present user with choice:

- Option A: Generate reference image first to lock character appearance (face, hair, costume), then proceed to full scene
- Option B: Direct text-to-image generation without reference locking

If Option A chosen, follow with sub-questions:

- Character archetype (e.g., Asian features / Western features / non-human)
- Costume style (e.g., black trench coat / nano-tech suit / fantasy armor)
- Any signature visual elements (e.g., cybernetic implants / glowing tattoos / specific accessories)

**Phase 2 — Scene Foundation**

Present user with choice:

- Option A: User provides reference image for scene/environment style
- Option B: AI autonomously generates scene based on keywords

If Option B chosen, extract atmosphere keywords from user's description and perform style routing.

**Asset Inventory Checklist**:

- \[ \] Character reference image (if Phase 1 = Option A)
- \[ \] Scene reference image (if Phase 2 = Option A)
- \[ \] Style routing completed (if no references provided)
- \[ \] Target model identified (MJ / Seedream / image2)
- \[ \] Batch size confirmed (see Batch Generation Control below)

### 2. Initial Design Stage

**Step 1: Generate Character Reference (if required)**

Prompt structure for character reference:

```
[Character archetype] + [Costume description] + [Pose: neutral standing or sitting] + [Background: solid black or simple gradient] + [Lighting: even front light for clear feature visibility] + "character design sheet, full body visible, clear facial features, high detail"
```

Generate 4 variations, present to user for selection. Locked reference becomes `{{node_key}}` for all subsequent scenes.

**Step 2: Build Scene Prompt**

For MJ:

```
{{node_key}}, [subject action/pose], [shot size + angle], [environment keywords], [lighting type], [color palette], [mood], photorealistic, cinematic, [aspect ratio]
```

For Seedream/image2:

```
{{node_key}}, [detailed scene description with hierarchical structure: foreground → midground → background], [camera specifications: lens type, depth of field, angle], [lighting setup: direction, quality, color temperature], [atmospheric effects: fog, rain, dust], [color grading: specific tonal range], [technical quality markers: sharpness, clarity, texture detail]
```

For image2 specifically, append mandatory suffix:

```
Low ISO, no visible grain noise, no heavy film grain, no dirt, no mud spots, no mold marks, no dust spots, clean optical clarity
```

**Step 3: Batch Generation Control (Critical Rule)**

NEVER generate multiple variations without explicit user permission.

**Default behavior**: Generate 1 output only

**When multiple outputs are allowed**:

- User explicitly requests "多生几组" (multiple sets) or "给我几个版本" (give me several versions)
- Agent asks "是否需要多生几组图片作对比?" (Do you need multiple sets for comparison?) and user confirms

If user does NOT confirm multi-generation request, produce exactly 1 output.

### 3. Iteration Stage

**Optimization Dimension 1: Composition Adjustment**

If user feedback indicates compositional issues:

- "太近了" (too close) → reduce subject scale, pull camera back, wider shot
- "看不清细节" (can't see details) → tighter framing, closer shot, increase subject scale
- "角度不对" (wrong angle) → adjust camera height (low-angle for power, high-angle for vulnerability, eye-level for neutrality)
- "不够震撼" (not impactful enough) → extreme perspective (fisheye distortion, dramatic low-angle, overhead god's-eye view)

**Optimization Dimension 2: Atmosphere Refinement**

If user feedback targets mood:

- "不够冷" (not cold enough) → reduce color temperature (shift blue), increase desaturation, add fog/mist
- "太暗了" (too dark) → lift shadows while maintaining contrast, add rim lighting or practical light sources
- "颜色太饱和" (colors too saturated) → reduce saturation by 20-30%, shift toward muted/dusty palette
- "氛围不够压抑" (atmosphere not oppressive enough) → lower horizon line, increase shadow mass, add claustrophobic framing (tight crop, blocked exits)

**Optimization Dimension 3: Scale and Detail Balance**

For scenes involving massive creatures or structures:

- Include scale reference objects (human figures, vehicles, buildings at 1:50+ scale ratio)
- Use atmospheric perspective (haze, fog layers increasing with distance)
- Employ extreme depth of field (keep foreground and distant subject both in focus for size comprehension)
- Add foreground framing elements (archway, tree branches) to create layered depth

**Cross-Output Consistency Audit**

When producing series with same character:

- \[ \] Face structure identical across all outputs (check: eye spacing, nose shape, jawline)
- \[ \] Body proportions maintained (check: height ratios, limb length)
- \[ \] Signature costume elements present (check: specific accessories, color blocking)
- \[ \] Lighting can vary but should not alter core facial features
- \[ \] If inconsistency detected, regenerate using original reference `{{node_key}}` with stronger identity reinforcement

**When to Accept vs. Regenerate**

Accept output when:

- Core identity features match reference (if reference exists)
- Composition serves narrative intent
- Atmosphere matches style routing target
- Technical quality meets standard (sharp focus, clean rendering, no artifacts)

Regenerate when:

- Character face does not match reference (facial structure drift)
- Composition obscures critical narrative elements
- Atmosphere contradicts style routing (e.g., warm tones in cold noir scene)
- Technical defects present (blurry, distorted, nonsensical anatomy)

## Key Constraints & Standards

### Immutable Rules (Never Violate)

1. **Two-Phase Confirmation Mandatory**: Every new project must execute character confirmation → scene confirmation sequence. Cannot skip, cannot merge into one question.

2. **Batch Generation Consent Required**: Default = 1 output. Multiple outputs only if user explicitly requests or confirms when asked. Agent cannot autonomously decide to generate 4 variations.

3. **Reference Image Lock**: Once character reference is generated and user selects one, that `{{node_key}}` must appear in ALL subsequent scene prompts for that character. No exceptions.

4. **Model-Specific Prompt Limits**:

   - MJ: ≤800 characters (hard cap 1024), keyword phrases only
   - Seedream/image2: no hard limit but maintain structured hierarchy

5. **image2 Quality Suffix**: When using Lib Image (image2) model, mandatory append: "Low ISO, no visible grain noise, no heavy film grain, no dirt, no mud spots, no mold marks, no dust spots, clean optical clarity"

### Fidelity Rules (Quality Standards)

**Character Consistency**:

- Face structure deviation tolerance: 0% (regenerate if facial features differ)
- Body proportion deviation tolerance: ±5% (minor pose-induced perspective shifts allowed)
- Costume signature elements: 100% retention required

**Atmospheric Coherence**:

- Color palette deviation from style routing: ±10° hue shift, ±15% saturation shift allowed
- Lighting direction can vary but quality (hard/soft) must match scene context
- Weather/atmospheric effects (fog, rain, dust) must be consistent within a scene series

**Technical Quality**:

- Focus: primary subject must be sharp unless intentional blur for motion/depth effect
- Rendering: no visible AI artifacts (malformed hands, nonsensical architecture, text gibberish)
- Composition: rule of thirds adherence for balanced shots, intentional breaking allowed for tension/unease

### Scene-Specific Constraints

**Apocalyptic/Wasteland Scenes**:

- Color palette: desaturated earth tones (browns, grays, muted greens), avoid vibrant colors
- Architecture: must show decay (crumbling concrete, rusted metal, overgrown vegetation)
- Scale: include distance markers (mountains, ruined skyscrapers) to establish environment scope
- Human presence: isolated figures, avoid crowds (contradicts desolation theme)

**High-Tech/Futuristic Scenes**:

- Geometry: clean lines, no organic irregularity unless intentional bio-tech fusion
- Lighting: must include artificial light sources (neon, holograms, bioluminescent panels)
- Materials: reflective metals, transparent polymers, glowing energy conduits
- Scale: massive structures (space stations, megacity towers) to convey technological advancement

**Creature/Monster Scale Scenes**:

- Size ratio: creature must be ≥10x human scale for "overwhelming" effect, ≥50x for "cosmic horror" effect
- Perspective: extreme low-angle mandatory, camera positioned at human eye level looking up
- Atmospheric depth: use haze/fog to prevent creature from looking like foreground cutout
- Reaction elements: include human figures showing fear/awe to anchor emotional context

**Noir/Cold Atmosphere Scenes**:

- Contrast ratio: deep blacks (shadow mass ≥40% of frame), controlled highlights
- Wet surfaces: rain-slicked streets, window condensation, reflective puddles mandatory for noir feel
- Color temperature: cool (blue-shifted) or monochromatic with single warm accent
- Isolation: solitary figure composition, avoid groups or busy backgrounds

## Recommended Tools & Models

**Midjourney (MJ)**: Best for stylized, artistic interpretations with strong aesthetic coherence. Use when user requests "极具特色" (highly distinctive style) or specifies "用MJ模型". Requires strict prompt compression (≤800 chars, keyword phrases only).

**Seedream 5.0 Pro**: Optimal for high-resolution photorealistic outputs with complex scene details. Supports natural language prompts with technical photography terminology. Use for "高清" (high resolution) or "写实" (photorealistic) requests.

**Lib Image (image2)**: Specialized for image-to-image refinement and upscaling. Mandatory for "放大4K" (upscale 4K) or "重塑细节" (detail enhancement) requests. Always append quality suffix: "Low ISO, no visible grain noise, no heavy film grain, no dirt, no mud spots, no mold marks, no dust spots, clean optical clarity".

## Advanced Techniques

### Multi-Scene Narrative Sequencing

For serialized visual storytelling (e.g., character journey across multiple environments):

1. Lock character reference in Scene 1
2. Generate 3-5 key narrative beats as separate scenes, each with:
   - Same character reference `{{node_key}}`
   - Progressive environmental shift (e.g., wasteland → abandoned city → underground bunker)
   - Compositional variety (wide establishing → medium action → close-up emotion)
3. Maintain consistent lighting quality (hard/soft) across sequence even as direction/color shifts
4. Use recurring visual motifs (e.g., same red scarf, same weapon) as continuity anchors

### Hybrid Style Synthesis

Combine elements from multiple style routes for unique aesthetics:

- **Apocalyptic + High-Tech**: Decayed megastructures with flickering holograms, rust + neon
- **Noir + Creature Horror**: Urban rain scene with cosmic monster emerging from fog, chiaroscuro + Lovecraftian scale
- **Wasteland + Bioluminescent**: Desert ruins with glowing alien flora, muted earth tones + cyan/magenta accents

When synthesizing, maintain dominant style (70% composition) and subordinate style (30% accent). Do not 50/50 split — results in visual confusion.