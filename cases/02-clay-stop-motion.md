# C02. Clay Stop-Motion: Fishing for a Star

**by SeeAPI** · Inspired by [Charlie Guo](https://x.com/charlierguo/status/2097399137142772071)

## 👀 Preview

[<img src="../assets/02-clay-stop-motion/penguin-star-stop-motion.gif" width="313" height="313" alt="Clay Stop-Motion: Fishing for a Star — GIF result">](../assets/02-clay-stop-motion/penguin-star-stop-motion.gif)

**Penguin star contact sheet**

[<img src="../assets/02-clay-stop-motion/penguin-star-contact-sheet.png" width="400" height="400" alt="penguin star contact sheet">](../assets/02-clay-stop-motion/penguin-star-contact-sheet.png)

Illustrative stills generated with an unexposed model ID. Some rod, line, and set drift remains in the GIF.

## 👇 Workflow

`Text → contact sheet → GIF`

## 🔖 Full Prompt

**Step 1 — Text → contact sheet**

No reference required.

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

**Step 2 — Contact sheet → GIF**

Upload the complete 4 × 4 sheet to Codex; preserve the full set.

```text
Use Python and Pillow to turn the attached 4x4 stop-motion contact sheet into a looping GIF. Split it into 16 equal-sized frames, reading left to right and top to bottom. If the image dimensions are not divisible by four, round the cell boundaries and use a consistent crop size, trimming at most one edge pixel where necessary.

Keep the complete miniature scene in every frame. Preserve one shared crop and the original image scale. Do not crop to the penguin's silhouette or recenter it independently: the ice hole, horizon, and floor must remain in place. Do not add camera movement, interpolated poses, optical flow, or crossfades.

Use a shared 256-color palette with no dithering. Start with 140 ms per frame, hold the reveal briefly, and use a short pause at the loop boundary. Preserve the source order unless the poses clearly require a change. Export an infinitely looping GIF and provide a reproducible script with the exact frame order and durations.

Inspect the character, rod, line, star, ice hole, and first-to-last transition. Report visible drift or missing motion honestly; if source frames need correction, explain what should be regenerated rather than describing the GIF as perfectly seamless.
```

[← Back to this case in the README](../README.md#c02-clay-stop-motion-fishing-for-a-star)
