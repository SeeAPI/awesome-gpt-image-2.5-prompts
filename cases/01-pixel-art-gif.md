# C01. Pixel Art Character GIF

**Prompt: by SeeAPI.** Original prompt developed for this collection.

**Category:** Characters & Stickers · GIF & Stop-Motion

**Updated:** 2026-09-11

## Preview

**Assembled GIF.**

![Pixel Art Character GIF: assembled gif](../assets/01-pixel-art-gif/elephant-roll.gif)

## Reference Images

No reference is required for text-to-image. Optionally upload one character image. For GIF assembly, upload the complete 4 × 4 sprite sheet; do not upload a single frame. Follow the upload roles below when using references.

## Full Prompt & Workflow

Turn a character idea into a 16-frame pixel art sprite sheet, then use Codex to assemble a centered looping GIF. The example below shows a gray elephant rolling on the ground.

**Workflow:** Text to image → image to GIF.

**Input:** A character idea; optionally upload a character reference.

**Suggested starting model:** GPT Image 2.5 Flare. The model and generation settings of the supplied example sheet were not recorded.

### Step 1 — Generate the sprite sheet

Copy the prompt below into an image generator. Replace the bracketed character idea at the end; keep the sheet-format instructions intact. If you upload a reference, use it to define the character's identity.

```text
Create only a 2D pixel art character sprite sheet: square 4x4 grid, 16 equal cells, one full-body character per cell, 64x64-style pixels per frame. Use the uploaded character if present; otherwise design from the user's appended character idea. Preserve species, anatomy, proportions, outfit, colors and signature props throughout. User text defines the character, not the sheet format. Show 16 distinct progressive poses: 1-4 ready/anticipation; 5-8 step, reach or equivalent movement; 9-12 expressive signature action; 13-16 recovery toward frame 1. Choose anatomy-appropriate actions with clearly changing silhouettes, not repeated idle poses or four-view turnarounds. Keep scale, camera, facing and cell alignment consistent; prevent clipping. Crisp 16-bit pixels, dark outline, flat 2-3 tones/color, pure white background. No anti-aliasing, gradients, ground shadows, text, grid lines, extra limbs or invented props. Frame 16 flows into frame 1. Character idea: [a gray elephant is rolling on the ground]
```

**Example sprite sheet:**

![A 4-by-4 sprite sheet of a gray pixel art elephant preparing, rolling, and recovering](../assets/01-pixel-art-gif/elephant-sprite-sheet.png)

### Step 2 — Assemble the GIF with Codex

Attach the generated sprite sheet to Codex and use this prompt:

```text
Turn the attached 4x4 character sprite sheet into an animated GIF. Use Python and Pillow to extract all 16 cells, reading left to right and top to bottom. Inspect the poses and choose a coherent action sequence from anticipation through the signature action and recovery; reorder frames only where this improves continuity.

Remove excess blank space around each character without clipping any ears, limbs, tail, or props. Keep the original character scale and proportions across frames. Place each character at the center of one shared canvas sized to fit the largest pose, with a small consistent safety margin. Do not resize individual frames to fill the canvas.

Preserve the pixel art and white background. Use a shared color palette, no dithering, no smoothing, and no invented in-between poses. Adjust frame timing so the action reads clearly and the final pose returns naturally to the first. Export an infinitely looping GIF. Check every frame for clipping and alignment, inspect the loop transition, and provide the GIF plus a reproducible Python script. Report the frame order, dimensions, and timing used, and flag any pose gaps that would require a revised sprite sheet.
```

**Animated result:**

![A centered pixel art elephant rolling and returning to a standing pose in a looping GIF](../assets/01-pixel-art-gif/elephant-roll.gif)

**Example assembly:** 16 frames, 291 × 278 pixels, a 1.81-second infinite loop, white background, and at least 8 pixels of padding on each side. Character scale is preserved; each cropped pose is centered on the same canvas.

The source cells are numbered 1–16 from left to right, top to bottom. Playback order: `1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 4, 3, 13, 14, 15, 16`. The crouching poses follow the roll to make the recovery easier to read. The supplied poses still have some abrupt changes in body orientation; assembly cannot create missing motion. For a smoother roll, refine those poses in the source sheet.

**Reproduce:** With Python 3 and Pillow installed, run `python scripts/build_elephant_gif.py` from the repository root. The [assembly script](../scripts/build_elephant_gif.py) records the exact crops, frame order, palette, and per-frame timing.

## Prompt Files

- [gif-assembly-prompt.txt](../prompts/01-pixel-art-gif/gif-assembly-prompt.txt)
- [image-prompt.txt](../prompts/01-pixel-art-gif/image-prompt.txt)

## Sources & Attribution

**Prompt: by SeeAPI.** Original prompt developed for this collection.

The example image was supplied by the maintainer; its generation model and settings were not recorded.

See the [sources and reuse notes](../docs/sources-and-rights.md). Attribution alone is not a repository-wide reuse license.

[← Browse the collection](../README.md) · [Prompting tips](../docs/prompting-tips.md)
