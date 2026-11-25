---
name: script-structural-decomposer
description: "Script structural decomposer for comic drama: precisely break down scripts into shooting drafts ready for comic drama and short drama production."
---

# Function and Purpose

This Skill is designed to break down rough original scripts in a factory-style process, converting them into shooting drafts that can be directly used for animated and short drama production. Its core feature is thoroughly decoupling actor actions from dialogue, while automatically identifying episodes, scenes, characters, and emotions, greatly improving pre-production efficiency.

# Applicable Input

- Complete long scripts or already-episodized script fragments.
- Formats may include: txt, Word content, or directly pasted text.

# Operation Steps

1. **Episode Identification**: Automatically split according to script markers or plot closure (approximately 800-1200 characters). Each episode must distill its core hook and explosive moment.
2. **Scene Splitting**: Split scenes based on location and time changes, marking interior/exterior, day/night, and primary/secondary scene names.
3. **Element Extraction**: Identify all characters (main/supporting/extra), key props, and transition methods.
4. **Action and Dialogue Decoupling**: Extract independent actions from descriptions (starting with "△"), and list dialogue separately, tagged with the corresponding extreme emotion label (e.g., sweet, angsty, satisfying, hype, etc.).
5. **Shot Refinement**: Generate shot size, camera movement, and visual content descriptions for each scene.

# Output Requirements

The output consists of three core tables, ensuring all fields are complete:

### 1. Episode Outline

Includes episode number, core hook (≤15 characters), the episode's explosive moment, cliffhanger emotion, and key characters.

### 2. Scene Table

Includes episode-scene number, scene name, interior/exterior and day/night, characters, key props, transition method, and plot summary.

### 3. Shot Breakdown Draft

- **Fields**: Shot number, shot size, camera movement, visual content, actor action (must start with △), dialogue, emotion label, and remarks.
- **Action Standard**: If there is no explicit action, fill in "△Stand Still" or "△Gaze"; empty entries are forbidden.
- **Emotional Peak**: For conflict shots, mark "【Emotional Peak】Recommend slow motion/freeze frame".

# Notes

- Actions must be reverse-deconstructed from the dialogue context (e.g., "said with a sneer" split into "△Sneer" + dialogue).
- Missing interior/exterior or day/night information must be completed based on context and marked with "\*".
- Ensure the information density of each shot meets the fast-paced requirements of short dramas.