---
sensitivity: private
entity_type: concept
name: "kie-ai-veo3-prompt-engineering"
description: "Hallucination patterns and prompt structure rules for Kie AI / Veo 3 video generation in REFERENCE_2_VIDEO mode"
tags: [kie-ai, veo3, video-generation, prompt-engineering, seraman]
created: "2026-06-28"
---

# Kie AI / Veo 3 — Prompt Engineering Rules

Discovered during SERAMAN M2 testing. These patterns apply to REFERENCE_2_VIDEO mode
(presenter reference image + product image + video_prompt text).

---

## Input Model

Kie AI / Veo 3 accepts:
- `video_prompt` — the only text input. Drives both VISUAL generation AND audio/speech generation.
- Presenter reference image
- Product reference image

There is no separate audio or dialogue field. Dialogue must live inside `video_prompt`.
`voiceover_text` is a Creatomate field only — Kie AI never sees it.

---

## Hallucination Patterns Found

### 1. Product name in opening dialogue → text on product surface

When the video_prompt contains dialogue that opens with the product name as a
standalone declaration, Veo 3 renders that text visually onto the nearest surface
(packaging, shelves, backgrounds).

**Example:** `'Allora — CVN4 Tactical Responder Bandage.'`
→ Kie AI hallucinated "Tactical Resolyer Bag/over Bandage" as a printed label on the green pouch.

**Fix:** Don't open dialogue with the product name as a declaration.
Move the name mid-sentence: `'Allora. Quattro pollici, TCCC certificato. Questo è il CVN4.'`

---

### 2. No-text instruction at the end of the prompt = ignored

When `no text overlays, no visible text...` appears at the END of the video_prompt,
Veo 3 has already committed to surface rendering from the earlier prompt content.

**Fix:** Put the full no-text block at the VERY START of the prompt, before camera
description and before dialogue. Veo 3 weights earlier instructions more heavily.

**Correct order:**
```
[NO-TEXT RULES BLOCK]
[Camera description]
[Scene action]
[Presenter dialogue]
```

**Full no-text block (use verbatim):**
> no text overlays, no generated logos, no readable labels in frame, no visible text
> writing labels tags or markings on any shelf wall packaging or background object in
> frame, no skulls no crossbones no danger symbols no hazard markings on any product.

---

### 3. Tactical/military context triggers danger symbols

Words like `TCCC`, `tactical`, `combat`, combined with phrases like "no second chance"
or "life or death" cause Veo 3 to hallucinate skull, crossbones, or hazard symbols
onto product surfaces.

**Fix:** Include explicit no-skull / no-hazard instruction in the no-text block (already
in the block above). Do not remove tactical language from dialogue — just block the
visual output.

---

### 4. Environment text hallucination: separate class from overlay text

`no text overlays` suppresses Kie AI's own rendered caption/overlay layer.
It does NOT suppress text that appears on background objects (shelves, packaging,
store signs, wall text). These are treated as environmental content, not overlays.

**Fix:** Always include both:
- `no text overlays, no generated logos` — blocks the overlay layer
- `no visible text writing labels tags or markings on any shelf wall packaging or background object in frame` — blocks environment text

Both are needed. One does not cover the other.

---

### 5. One product image per run vs multiple product forms in the script

If a video script shows the same product in different forms (e.g., Scene 1: vacuum-sealed
package, Scene 3: unrolled bandage), and the automation passes ONE product image URL to
all scenes, Kie AI generates conflicting product representations.

**Fix Option A (quick):** Pick one product form for the entire video. Rewrite all
prompts to show only that form. Pass the matching image.

**Fix Option B (correct):** Support per-scene product images. Output `product_image_url`
per scene from the Claude script agent. Pass different image URLs to scenes that show
different product states. Requires Tally form + n8n schema change.

---

## System Prompt Rule (to add to v5.1+)

Add to the IMAGE PROMPT ENGINEERING RULES section:

> **Prompt structure order (non-negotiable):**
> 1. No-text rules block — always first
> 2. Camera specification
> 3. Scene action and choreography
> 4. Presenter dialogue (end of prompt)
>
> **Dialogue rule:** Never open spoken dialogue with the product name as a standalone
> declaration. The product name should appear mid-sentence, not as the first spoken words.
> This prevents Veo 3 from rendering the product name as a printed label on the product surface.

---

## Related nodes

[[giovanni-seraman]] · [[seraman-pipeline]] · [[loom-strategy]]
