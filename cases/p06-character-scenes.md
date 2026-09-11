# P06. Portrait Reference to Multi-View Sheet

## 👀 Preview

[<img src="../assets/p06-character-scenes/portrait-views-result.png" width="400" height="225" alt="Portrait reference sheet with three full-body views and two face views">](../assets/p06-character-scenes/portrait-views-result.png)

## 👇 Workflow

`Portrait reference → reference sheet (left 2/3: front / side / back full body; right 1/3: front / side face)`

## 🔖 Full Prompt

```text
Use the uploaded portrait as the identity reference for one person. Create a single landscape character reference sheet with exactly five views of that same person. Preserve facial identity, age, gender presentation, skin tone, hairstyle, body proportions, and visible clothing details. If the portrait does not show the full outfit or body, use [outfit and footwear description] and infer unseen proportions conservatively; keep those choices consistent across every view.

Divide the canvas into two main regions. The LEFT TWO-THIRDS contains three equally sized, evenly spaced full-body views arranged horizontally: front view on the left, true side profile in the middle facing left, and back view on the right. Show the entire person from the top of the head to the soles of the shoes in each view, with aligned head and ground levels, identical scale, relaxed neutral standing poses, and a small safety margin. Keep arms slightly clear of the torso where anatomically appropriate so the silhouette and clothing remain readable.

The RIGHT ONE-THIRD contains two equally sized face close-ups stacked vertically: front-facing face at the top and a true side-profile face facing left at the bottom. Show the complete head, hair, ears where visible, and upper neck without clipping. Use a consistent close-up scale, neutral expression, and clear facial detail. These are the same person as the three full-body views, not additional characters.

Use a plain [background color] studio background, soft even lighting, and the same visual style as the uploaded reference. Keep camera perspective natural and proportions undistorted. Separate views with clean whitespace rather than drawn borders. Preserve outfit colors, hairstyle, and identity across all five views. No text, labels, grid lines, extra views, extra people, invented accessories, cropped feet, duplicated limbs, or three-quarter poses replacing the required front, side, and back views.
```

*Replace `[outfit and footwear description]` with the clothing to use for any details not visible in the reference, and `[background color]` with your preferred background color.*

[← Back to this case in the README](../README.md#p06-portrait-reference-to-multi-view-sheet)
