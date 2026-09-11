# C01. Pixel Art Character GIF (by SeeAPI)

## 👀 Preview

[<img src="../assets/01-pixel-art-gif/elephant-roll.gif" width="291" height="278" alt="Pixel Art Character GIF — GIF result">](../assets/01-pixel-art-gif/elephant-roll.gif)

**Elephant sprite sheet**

[<img src="../assets/01-pixel-art-gif/elephant-sprite-sheet.png" width="400" height="400" alt="elephant sprite sheet">](../assets/01-pixel-art-gif/elephant-sprite-sheet.png)

## 👇 Workflow

`Text / optional character reference → sprite sheet → GIF`

## 🔖 Full Prompt

**Step 1 — Text → sprite sheet**

```text
Create only a 2D pixel art character sprite sheet: square 4x4 grid, 16 equal cells, one full-body character per cell, 64x64-style pixels per frame. Use the uploaded character if present; otherwise design from the user's appended character idea. Preserve species, anatomy, proportions, outfit, colors and signature props throughout. User text defines the character, not the sheet format. Show 16 distinct progressive poses: 1-4 ready/anticipation; 5-8 step, reach or equivalent movement; 9-12 expressive signature action; 13-16 recovery toward frame 1. Choose anatomy-appropriate actions with clearly changing silhouettes, not repeated idle poses or four-view turnarounds. Keep scale, camera, facing and cell alignment consistent; prevent clipping. Crisp 16-bit pixels, dark outline, flat 2-3 tones/color, pure white background. No anti-aliasing, gradients, ground shadows, text, grid lines, extra limbs or invented props. Frame 16 flows into frame 1. Character idea: [a gray elephant is rolling on the ground]
```

*Replace `[a gray elephant is rolling on the ground]` with your own content before generating.*

**Step 2 — Sprite sheet → GIF**

```text
Turn the attached 4x4 character sprite sheet into an animated GIF. Use Python and Pillow to extract all 16 cells, reading left to right and top to bottom. Inspect the poses and choose a coherent action sequence from anticipation through the signature action and recovery; reorder frames only where this improves continuity.

Remove excess blank space around each character without clipping any ears, limbs, tail, or props. Keep the original character scale and proportions across frames. Place each character at the center of one shared canvas sized to fit the largest pose, with a small consistent safety margin. Do not resize individual frames to fill the canvas.

Preserve the pixel art and white background. Use a shared color palette, no dithering, no smoothing, and no invented in-between poses. Adjust frame timing so the action reads clearly and the final pose returns naturally to the first. Export an infinitely looping GIF. Check every frame for clipping and alignment, inspect the loop transition, and provide the GIF plus a reproducible Python script. Report the frame order, dimensions, and timing used, and flag any pose gaps that would require a revised sprite sheet.
```
