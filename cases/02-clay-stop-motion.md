# C02. Clay Stop-Motion: Fishing for a Star

**Prompt: by SeeAPI.** **Inspiration:** [Charlie Guo](https://x.com/charlierguo/status/2097399137142772071). Original concept and prompt adaptation by SeeAPI; no source footage is included.

**Category:** GIF & Stop-Motion

**Updated:** 2026-09-11

## Preview

**Assembled GIF.**

![Clay Stop-Motion: Fishing for a Star: assembled gif](../assets/02-clay-stop-motion/penguin-star-stop-motion.gif)

## Reference Images

No reference is required for text-to-image. For GIF assembly, upload the complete 4 × 4 contact sheet and preserve the whole miniature set in every frame. Follow the upload roles below when using references.

## Full Prompt & Workflow

A tiny clay penguin in a mustard-yellow scarf fishes a coral-pink star out of an ice hole, admires it, and gently lowers it back. Tactile clay, miniature scenery, and discrete pose changes give the sequence a handmade stop-motion look.

**Inspiration:** [Charlie Guo's post about image-model stop-motion animation](https://x.com/charlierguo/status/2097399137142772071). This example uses an original penguin-and-star concept and a newly written prompt; it does not reproduce the post's footage or claim to use its exact workflow.

**Workflow:** Text to image → 16-frame contact sheet → animated GIF.

**Input:** None.

**Example generation:** Created with Codex's built-in image generation tool. The underlying model ID and quality setting were not exposed, so this is an illustrative workflow rather than a verified benchmark of either named model.

### Step 1 — Generate the stop-motion frame sheet

Use this prompt to generate all sixteen frames in one image. Keep the camera, ice hole, lighting, and character identity consistent. Unlike the isolated sprite in case 01, this scene needs its whole set to stay in place.

```text
Create one square image that is an EXACT 4 by 4 contact sheet of sixteen equally sized square animation frames, edge-to-edge with NO gutters, borders, labels or text. This is a handcrafted clay stop-motion sequence, not pixel art.

Original story: a tiny charcoal-gray clay penguin in a mustard-yellow knitted scarf sits on the LEFT of a small round fishing hole in a pale-blue miniature ice floor. The penguin has a cream belly, two short flippers, two orange feet, black bead eyes, and a short orange beak. A short wooden fishing rod held in its right flipper extends diagonally toward the hole at RIGHT. One thin fishing line connects the rod tip to one small coral-pink five-point clay star. The star starts below the hole, rises out as the penguin pulls, briefly hangs above the hole, then is lowered back into it. No fish, other characters, buckets or extra props.

All sixteen frames show the EXACT SAME locked eye-level three-quarter camera, fixed wide composition, penguin at x35%, hole at x67%, same ice floor and seamless dusty-lavender backdrop, same object sizes, same soft warm light from upper left. Keep all objects entirely inside each cell with generous 10% safety margin. Real clay fingerprints, slightly lumpy handmade forms, tactile wool scarf, soft contact shadows. Every frame looks like a photographed tabletop miniature. Use modest, clearly distinct stepped pose changes and consistent anatomy.

Frame progression in strict reading order, left to right then top to bottom:
1: penguin holds rod low, looks at hole, star hidden.
2: penguin leans forward slightly, rod low.
3: penguin starts raising rod, fishing line taut.
4: penguin leans back, rod rises, pink star tip appears inside hole.
5: star half emerges, line visibly attached.
6: full star just clears hole, penguin looks at it.
7: star rises a little more, rod higher.
8: star hangs one star-height above hole, penguin eyes wide.
9: hold the same star height, penguin tilts its head in delight.
10: penguin begins lowering rod, star slightly lower.
11: star descends toward hole.
12: star touches hole rim level.
13: star half submerged.
14: only star tip visible, penguin straightens.
15: star hidden, rod returning to initial low angle.
16: same composition and near-identical pose as frame 1, ready to loop.

Prioritize exact 4x4 equal cell geometry, unchanging set placement, stable identity, line continuity and readable incremental motion. No motion blur, camera movement, frame numbers, captions, changing background, extra limbs, floating penguin or disconnected fishing line.
```

**Generated frame sheet:**

![Sixteen clay-style frames of a penguin lifting a pink star out of an ice fishing hole and lowering it back](../assets/02-clay-stop-motion/penguin-star-contact-sheet.png)

### Step 2 — Assemble the stop-motion GIF with Codex

Attach the frame sheet to Codex and use this prompt:

```text
Use Python and Pillow to turn the attached 4x4 stop-motion contact sheet into a looping GIF. Split it into 16 equal-sized frames, reading left to right and top to bottom. If the image dimensions are not divisible by four, round the cell boundaries and use a consistent crop size, trimming at most one edge pixel where necessary.

Keep the complete miniature scene in every frame. Preserve one shared crop and the original image scale. Do not crop to the penguin's silhouette or recenter it independently: the ice hole, horizon, and floor must remain in place. Do not add camera movement, interpolated poses, optical flow, or crossfades.

Use a shared 256-color palette with no dithering. Start with 140 ms per frame, hold the reveal briefly, and use a short pause at the loop boundary. Preserve the source order unless the poses clearly require a change. Export an infinitely looping GIF and provide a reproducible script with the exact frame order and durations.

Inspect the character, rod, line, star, ice hole, and first-to-last transition. Report visible drift or missing motion honestly; if source frames need correction, explain what should be regenerated rather than describing the GIF as perfectly seamless.
```

**Animated result:**

![Clay-style penguin fishing a pink star from an ice hole in a looping stop-motion GIF](../assets/02-clay-stop-motion/penguin-star-stop-motion.gif)

**Example assembly:** 16 frames in source order, 313 × 313 pixels, a 2.48-second infinite loop. Each frame keeps the full miniature set. Frame durations in milliseconds: `200, 140, 140, 140, 140, 140, 140, 200, 220, 140, 140, 140, 140, 140, 140, 180`.

**What to check:** The generated sheet communicates the lift-and-lower action, but the rod angle, penguin pose, and ice-hole placement vary slightly between frames. Some line-length changes also remain. These are source-image continuity limits, so the result is a stylized frame animation with visible stepping, not a perfectly registered physical stop-motion shoot.

**Reproduce:** With Python 3 and Pillow installed, run `python scripts/build_penguin_gif.py` from the repository root. The [assembly script](../scripts/build_penguin_gif.py) and [exact generation prompt](../prompts/02-clay-stop-motion/generation-prompt.txt) are included.

## Prompt Files

- [generation-prompt.txt](../prompts/02-clay-stop-motion/generation-prompt.txt)
- [gif-assembly-prompt.txt](../prompts/02-clay-stop-motion/gif-assembly-prompt.txt)

## Sources & Attribution

**Prompt: by SeeAPI.** **Inspiration:** [Charlie Guo](https://x.com/charlierguo/status/2097399137142772071). Original concept and prompt adaptation by SeeAPI; no source footage is included.

Example stills were created with Codex’s built-in image generation tool. The underlying model ID was not exposed; they are workflow illustrations, not verified GPT Image 2.5 model samples.

See the [sources and reuse notes](../docs/sources-and-rights.md). Attribution alone is not a repository-wide reuse license.

[← Browse the collection](../README.md) · [Prompting tips](../docs/prompting-tips.md)
