# C02. Clay Stop-Motion: Fishing for a Star (by SeeAPI; inspired by [Charlie Guo](https://x.com/charlierguo/status/2097399137142772071))

## 👀 Preview

[<img src="../assets/02-clay-stop-motion/penguin-star-stop-motion.gif" width="313" height="313" alt="Clay Stop-Motion: Fishing for a Star — GIF result">](../assets/02-clay-stop-motion/penguin-star-stop-motion.gif)

**Penguin star contact sheet**

[<img src="../assets/02-clay-stop-motion/penguin-star-contact-sheet.png" width="400" height="400" alt="penguin star contact sheet">](../assets/02-clay-stop-motion/penguin-star-contact-sheet.png)

## 👇 Workflow

`Reference image / Text → clay-style image → contact sheet → GIF`

## 🔖 Full Prompt

**Step 1A — Reference image → clay-style image**

```text
Edit the uploaded image into a handcrafted clay stop-motion still. Preserve the character’s identity, species, anatomy, proportions, clothing, colors, signature props, pose, and scene composition. Translate surfaces into tactile modeling clay with subtle fingerprints, slightly imperfect sculpted edges, soft miniature-set shadows, and fabric texture where appropriate. Keep a single coherent scene with all important elements visible. No added characters, props, text, contact sheet, or animation frames. This is one clay-style starting image.
```

**Step 1B — Text → clay-style image (without a reference)**

```text
Create one handcrafted clay stop-motion starting image of [character description] in [setting], preparing to [simple action]. Use anatomy-appropriate poses and only [required props]. Place the character and props so the intended action can occur clearly in one locked-camera shot. Tactile modeling clay, subtle fingerprints, slightly imperfect sculpted shapes, soft miniature-set lighting, and a clean readable composition. Keep all subjects and props fully inside the frame with space for movement. No text, montage, contact sheet, or multiple frames.
```

*Replace `[character description]`, `[setting]`, `[simple action]`, and `[required props]` with your own content. Choose either Step 1A or Step 1B.*

**Step 2 — Clay-style image → contact sheet**

```text
Use the uploaded clay-style image as the strict identity, material, set, lighting, and camera reference. Create one square 4-by-4 contact sheet containing exactly sixteen equally sized square frames in reading order, with no gutters, grid lines, labels, or text.

Animate this action: [simple action]. Frames 1–4 establish the starting pose and anticipation; frames 5–8 begin the main movement; frames 9–12 show the action’s peak; frames 13–16 recover toward the starting pose for a loop. Use distinct, incremental, anatomy-appropriate poses with changing silhouettes. Keep the reference character’s species, proportions, outfit, colors, and props unchanged. Do not invent additional limbs, characters, or props.

Preserve one locked camera, consistent subject scale, fixed set placement, background, lighting, and scene geometry across every cell. Keep moving elements inside each cell with a small safety margin. Maintain physical contact and continuous grips on props. Retain tactile clay, handmade surface imperfections, and a gently stepped stop-motion feel. Frame 16 should flow naturally into frame 1. No camera movement, motion blur, duplicated idle frames, or changing scenery.
```

*Replace `[simple action]` with the movement you want to animate.*

**Step 3 — Contact sheet → GIF**

```text
Use Python and Pillow to turn the attached 4x4 stop-motion contact sheet into a looping GIF. Split it into 16 equal-sized frames, reading left to right and top to bottom. If the image dimensions are not divisible by four, round the cell boundaries and use a consistent crop size, trimming at most one edge pixel where necessary.

Keep the complete miniature scene in every frame. Preserve one shared crop and the original image scale. Do not crop to the penguin's silhouette or recenter it independently: the ice hole, horizon, and floor must remain in place. Do not add camera movement, interpolated poses, optical flow, or crossfades.

Use a shared 256-color palette with no dithering. Start with 140 ms per frame, hold the reveal briefly, and use a short pause at the loop boundary. Preserve the source order unless the poses clearly require a change. Export an infinitely looping GIF and provide a reproducible script with the exact frame order and durations.

Inspect the character, rod, line, star, ice hole, and first-to-last transition. Report visible drift or missing motion honestly; if source frames need correction, explain what should be regenerated rather than describing the GIF as perfectly seamless.
```
