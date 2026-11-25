# Fast-Cut Sensory TVC Production

## Core Methodology

### Anchor-Driven Consistency Framework

All visual outputs must reference pre-established anchor images to maintain brand/product identity across fragmented cuts. The anchor system consists of 4 layers:

**Layer 1 (A1 - Subject Identity)**: Three-view reference of the product (front/side/45° angle) encoding core visual DNA (color palette, body proportions, material finish, signature details)

**Layer 2 (A2 - Visual Style)**: Lighting quality and tone reference (natural light, studio lighting, dramatic backlighting, etc.) — defines the cinematic grammar

**Layer 3 (A3 - Scene Context)**: 2-3 environment references matching user-selected locations (racetrack, desert, urban streets, etc.) — ensures spatial coherence

**Layer 4 (A4 - Composition Language)**: Camera angle and framing reference (low-angle heroic, overhead tracking, close-up detail shots) — establishes visual hierarchy

Critical rule: All shot generation prompts MUST reference the corresponding anchor(s) via node_key placeholders (e.g., `{{i-xxxxxx}}`) to trigger visual inheritance.

### Five-Act Sensory Bombardment Structure

The TVC follows a proprietary five-act narrative arc optimized for information flow engagement:

**Act 1 (Symbol Establishment) — 10-15% duration**: Dark background → scanning light reveals product → brand emblem illumination (single shot, no cuts) Objective: Brand imprinting through mystery-to-revelation

**Act 2 (Personification) — 8-10% duration**: Human element introduction → driver/user approaching product → human-product fusion moment (1-2 shots) Objective: Emotional transfer from product to aspirational identity

**Act 3 (Mechanical Trigger) — 8-10% duration**: Start button → instrument cluster awakening → exhaust flame/mechanical detail (2-3 ultra-fast cuts) Objective: Sensory priming through machine ritual

**Act 4 (Speed Detonation) — 40-50% duration**: 5-7 high-frequency impact shots alternating between scene contexts (racetrack → desert → mountain pass), visual glitches (RGB chromatic aberration, negative film effect, white flash transitions) Objective: Dopamine spike through sensory overload

**Act 5 (Symbol Return) — 15-20% duration**: Hero pose freeze frame in primary scene → brand emblem gradual fade to black (2-3 shots with reverb tail) Objective: Brand closure with lingering impression

### Multi-Stage Confirmation Gate Protocol

IMPERATIVE: The workflow includes MANDATORY user confirmation checkpoints. The agent MUST NOT proceed to the next stage without explicit user approval:

**Gate 1 (Information Collection)**: Present 5 key questions (product subject, visual type, lighting style, scene selection, duration/resolution) via multi-choice interface. Wait for all answers before proceeding.

**Gate 2 (A1 Anchor Approval)**: Generate three-view product reference → display to user → ask "Does this match your expectation? ✅ Confirm / ❌ Revise". If ❌, collect revision instructions and regenerate. ONLY proceed after ✅.

**Gate 3 (Global Anchors Approval)**: Generate A2 style + A3 scene(s) + A4 composition anchors → display all images in grid → ask "Do these 4 anchors match the intended visual language? ✅ Confirm / ❌ Specify which to revise". ONLY proceed after ✅.

**Gate 4 (Shot Table Approval)**: Present the complete shot breakdown table (shot ID, description, duration, anchor references) → ask "Approve this shot structure? ✅ Confirm / ❌ Request changes". ONLY proceed after ✅.

**Gate 5 (First Batch Review)**: After generating shots S01-S05, display all 5 videos → ask "Do these shots meet quality standards? ✅ Continue to second batch / ❌ Regenerate specific shots". ONLY proceed after ✅.

**Gate 6 (Second Batch Review)**: After generating shots S06-S10, display all videos → ask "Approve second batch? ✅ Proceed to BGM / ❌ Regenerate specific shots". ONLY proceed after ✅.

**Gate 7 (BGM Approval)**: Generate background music → provide audio preview → ask "Approve BGM? ✅ Proceed to final assembly / ❌ Regenerate with different instructions". ONLY proceed after ✅.

Critical enforcement: If the agent skips any gate, the user MUST be able to halt the workflow and return to the missed checkpoint for retroactive approval.

## Workflow

### 1. Preparation Stage

**Input Checklist:**

- Product subject (specific model/variant if available, or generic category)
- Visual type selection: A (product-only), B (product + driver/character), C (pure scene/lifestyle)
- Lighting style: natural light, studio high-key, dramatic low-key, backlit silhouette
- Scene context(s): 1-3 environments from \[racetrack, desert/wilderness, mountain pass, urban street, coastal highway, industrial zone\]
- Target duration/resolution: 15s/30s/60s × 720p/1080p

**Pre-Production Decisions:**

- Determine five-act duration allocation based on total length (use percentage ratios above)
- Calculate shot count: 15s → 6 shots, 30s → 9-10 shots, 60s → 15-18 shots
- Identify required anchor types: A1 (always), A2 (always), A3 (1-3 variants), A4 (optional for extreme angles)

### 2. Initial Design Stage

**Anchor Generation Sequence:**

1. **A1 Three-View Reference**: Prompt structure = `[product name] + [key visual attributes from user input] + three-view layout (front, side, 45-degree angle) + high-resolution product photography style + [brand-specific details if known]`. Generate single image, present to user, await Gate 2 approval.

2. **Global Anchors (A2/A3/A4)**: Parallel generation of 3-4 images:

   - A2: `[lighting style from user input] + cinematic quality + [color temperature matching product] + no product visible, pure lighting reference`
   - A3: `[scene context 1] + [weather/time of day] + establishing shot + no product` (repeat for each selected scene)
   - A4: `[extreme camera angle if needed] + [composition rule] + visual drama + product silhouette`Present all anchors in grid, await Gate 3 approval.

**Shot Table Construction:**

- Map five-act structure percentages to shot durations
- Assign scene contexts to Act 4 shots (alternate between A3 variants for rhythm)
- Write detailed shot descriptions encoding: camera movement + product action + visual effect + anchor references
- Present table to user, await Gate 4 approval

### 3. Iteration Stage

**Batch Video Generation:**

- First batch (S01 - S05): Generate 5 shots in parallel, each prompt MUST include `{{node_key}}` placeholders referencing relevant anchors
- Display all 5 videos, await Gate 5 approval. If ❌, identify problematic shots, regenerate only those, re-present for approval
- Second batch (S06 - S10): Repeat parallel generation and Gate 6 approval cycle

**BGM Generation:**

- Prompt structure: `[total duration]s + three-part structure (suspenseful buildup 0-X%, explosive rhythm X-Y%, reverb decay Y-100%) + [genre matching product personality] + no vocals + cinematic trailer music`
- Generate audio node, provide preview link, await Gate 7 approval

**Pre-Assembly Checklist:**

- ✅ All shot nodes generated and approved
- ✅ No deprecated nodes in videoList
- ✅ Shot sequence matches five-act structure
- ✅ BGM timestamps written for three-part structure
- ✅ Audio mix ratio: original audio 30% + BGM 85%
- ✅ Resolution consistency confirmed (all shots match target resolution)

**Final Assembly:**

- Concatenate approved shots in narrative order
- Apply BGM with timestamp markers
- Execute final composite, generate master video node
- Present completion summary with five-act breakdown table

## Key Constraints & Standards

### Immutable Rules

- **Anchor inheritance**: Every shot generation prompt MUST reference at least one anchor via `{{node_key}}` placeholder. Shots without anchor references will have uncontrolled visual drift.
- **Confirmation gates**: The agent MUST halt at each of the 7 gates and wait for explicit ✅ approval. Skipping gates is a critical workflow violation.
- **Five-act structure**: The narrative arc is non-negotiable. Duration percentages can flex ±5%, but act sequence and objectives are fixed.

### Fidelity Rules

- **Product identity lock**: A1 anchor defines immutable attributes (brand emblem, signature color, body silhouette). These MUST remain pixel-consistent across all shots showing the product.
- **Lighting coherence**: All shots within the same scene context must reference the same A2 anchor. Cross-scene lighting shifts are allowed only at act transitions.
- **Scene spatial logic**: If A3 shows a racetrack with specific track markings, all racetrack shots must maintain that spatial signature (turn radius, barrier type, surface texture).

### Consistency Rules

- **Cut rhythm in Act 4**: Shot duration in the speed detonation phase must follow logarithmic decay pattern (3s → 2.5s → 2s → 2s → 3s for the hero beat). Never use uniform duration.
- **Visual glitch distribution**: RGB chromatic aberration, negative film, and white flash transitions must appear in Act 4 but NEVER in Acts 1-3 or 5. Maximum 3 glitch effects total.
- **BGM sync points**: The three-part BGM structure MUST align with act transitions (buildup = Acts 1-3, explosive = Act 4, decay = Act 5).

### Quality Thresholds

- **Anchor approval threshold**: If the user requests &gt;2 rounds of revision on any anchor, escalate to manual prompt refinement rather than continuing automated generation.
- **Shot regeneration limit**: If a single shot requires &gt;3 regeneration attempts, flag it as a potential prompt engineering issue and request user input on specific quality concerns.
- **Batch size**: Parallel generation is capped at 5 shots maximum to prevent GPU timeout. Larger projects must use multiple batches with intermediate approval gates.

## Recommended Tools & Models

Use \[@tool:video_generation_kuaishou_kling_v1_6_standard:Kling 1.6 Standard:\*\*\*\*s://a.lovart.ai/tool-icons/video_generation/kuaishou_kling_v1_6_standard.png\] for all video shot generation (anchor-referenced prompts, 5s/10s clip support, 720p/1080p output). Use \[@tool:generate_music:Music Generation:\*\*\*\*s://a.lovart.ai/tool-icons/audio/generate_music.png\] for three-part BGM creation with timestamp control.

## Advanced Techniques

### Anchor Blending for Transition Shots

For shots bridging two scene contexts (e.g., racetrack → desert transition), reference BOTH A3 anchors in the prompt with weighted notation: `70% {{A3a_racetrack}} + 30% {{A3b_desert}} + motion blur + speed lines`. This creates visual continuity across environmental shifts.

### Dynamic Anchor Override

If the user requests a specific shot that intentionally breaks anchor consistency (e.g., "make one shot black-and-white"), create a temporary one-time anchor (A5) for that shot only, then revert to global anchors for subsequent shots. Document the override in the shot table.

### Emergency Workflow Recovery

If the agent accidentally skips a confirmation gate, immediately halt all generation tasks, backtrack to the missed gate, present the relevant assets (anchors/shots/BGM) with a clear "Retroactive Approval Required" notice, and await user response before resuming. Never attempt to "fix forward" by continuing the workflow.