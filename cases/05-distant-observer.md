# C05. Distant Observer: A Robot in the Rain (by SeeAPI; inspired by [Pablo Prompt](https://x.com/pabloprompt/status/2097382752622436744))

## 👀 Preview

**Rainy street draft**

[<img src="../assets/05-distant-observer/rainy-street-draft.png" width="225" height="400" alt="rainy street draft">](../assets/05-distant-observer/rainy-street-draft.png)

**Rainy street opening**

[<img src="../assets/05-distant-observer/rainy-street-opening.png" width="225" height="400" alt="rainy street opening">](../assets/05-distant-observer/rainy-street-opening.png)

**Robot reference**

[<img src="../assets/05-distant-observer/robot-reference.png" width="267" height="400" alt="robot reference">](../assets/05-distant-observer/robot-reference.png)



## 👇 Workflow

`Text → character reference → scene image → corrected scene image → video`

## 🔖 Full Prompt

**Step 1 — Text → character reference**

Generate the robot identity image.

```text
Create one portrait 2:3 full-body character identity reference photograph of an original friendly obsolete street-maintenance robot. It is a physically built practical movie prop, about 2 meters tall, with a stocky weathered rust-red steel torso, off-white rounded rectangular head, exactly two small round dark glass eyes, no mouth, two thick articulated arms, exactly three blunt fingers on each hand, two short sturdy legs, and broad dark rubber feet. Its plates show chipped paint and light rain marks, never military armor. One small olive canvas pouch is strapped at its left hip. No writing, badges, logos, screens, weapons, or human face.
The robot stands upright in a relaxed front three-quarter pose on a plain mid-gray studio floor and seamless backdrop. Both empty hands, full head, and both feet are clearly visible with ample margins. No props in the hands, no umbrella in this identity reference. Keep one single robot, no collage, no turnaround grid, no other subject.
Photoreal practical-effects cinematography, tactile metal and canvas, soft overcast illumination, understated warmth. Design a unique humble municipal helper with rounded proportions, not an existing franchise robot.
```

**Step 2 — Character reference → scene image**

Upload the robot portrait.

```text
Use the uploaded robot portrait as the strict identity reference C05-R01: preserve the rust-red stocky steel body, off-white rounded rectangular head, two round dark eyes, no mouth, two arms, three blunt fingers per hand, two legs, rubber feet, and single olive pouch at its left hip.

Create one photoreal 9:16 vertical first frame with the visual feeling of a candid distant observation of a fictional scene. The camera is sheltered inside an unoccupied cafe doorway across a narrow rain-soaked street, about 25 meters from the robot. Use a moderate telephoto perspective with compressed depth and natural lens softness, not a wide-angle close-up. A dark out-of-focus door jamb occupies only the left 8% of the image and a soft blurred ledge crosses the bottom 5%; neither covers the robot or the flowerpot. No people or camera equipment are visible.

On the far sidewalk, the robot stands just right of center beneath its one OPEN mustard-yellow umbrella. The robot's body from head to feet occupies only 24–28% of the entire image height; keep it visibly small in a much larger urban environment. Its lowered gaze is directed at one terracotta flowerpot on the ground immediately to its right, containing one short green plant with one small white flower. The pot is close enough for the robot to shelter it by lowering and moving the umbrella a short distance. The hand nearest the pot holds the umbrella shaft at chest height; the free hand hangs at its side. The umbrella is currently above the robot, NOT already above the pot. Show the shaft continuously attached to the canopy and gripped by one hand.

Quiet old tram-stop frontage with a closed teal shutter behind the robot, damp pale plaster walls, a curb, a wet road occupying much of the lower middle frame, soft rain and broad puddle reflections. No readable shop names, road text, logos, vehicles, pedestrians, or other plants. The setting and wet empty space should dominate. Overcast afternoon daylight, subdued colors except the rust-red robot, yellow umbrella, and terracotta pot. The umbrella and flowerpot remain separate and fully visible. Natural slightly imperfect observer framing, no surveillance overlays, timestamp, cinematic black bars, or exaggerated bokeh. This is an ordinary street seen from afar, with one unexpected quiet act about to happen; not a hero portrait.
```

**Step 3 — Scene image → corrected scene image**

Upload the draft scene alone to reposition the flowerpot.

```text
Edit this distant rainy street frame with one local correction only. Move the existing terracotta pot and its single white flower to the RIGHT along the same sidewalk plane, so the ENTIRE pot and flower are visibly outside the yellow umbrella canopy's rightmost edge and receiving rain. Place the pot center at approximately 89% of image width, preserving its current size and its grounded contact with the sidewalk. Leave a visible horizontal rain-filled gap between the canopy's right edge and the flower. Remove the pot completely from its old position; there must still be exactly one pot and one flower.

Keep everything else unchanged: exact camera distance and framing, small robot size and pose, its two eyes and olive pouch, umbrella angle and connected shaft, hand grip, shutter, building, wet road, rain, bench, foreground doorway and blurred ledge, light, texture, and image dimensions. Do not move or enlarge the robot, change the umbrella, add characters, or crop the image. This frame is BEFORE the robot moves its umbrella over the pot.
```

**Step 4 — Corrected scene image → video**

Upload the corrected rainy-street image as the first frame; the robot portrait is optional.

```text
Animate C05-K01 as the exact first frame of an 8-second photoreal 9:16 distant-observer video, one uninterrupted shot. C05-R01 is optional robot identity reference only if the tool supports an extra reference slot. If only one image is allowed, use C05-K01. Preserve its street layout, wet road, teal shutter, foreground doorway edge, robot size, umbrella, and flowerpot.

The camera remains inside the doorway across the street at the same approximately 25-meter distance. Match the robot's exact small standing scale in C05-K01 (about 18% of frame height in the supplied example), rather than enlarging it to meet a numerical target. As it bends, allow its projected height to decrease naturally; never enlarge it or move the camera to compensate. The viewer should feel they happened to notice a small event on the far sidewalk. Only very slight low-amplitude handheld drift, under 1% of frame width; no zoom, push-in, tracking toward the subject, close-up, camera cut, or dramatic rack focus. Foreground occlusion remains at the edges, never over the action.

0–2 seconds: the rust-red robot pauses under its open yellow umbrella and tilts its off-white head down toward the single terracotta pot and white flower beside it. Rain continues falling; the flower stem nods slightly. Keep exactly two eyes, no mouth, one olive hip pouch, and the same physical body proportions.
2–6 seconds: the robot bends at the knees and waist, using the hand already gripping the umbrella shaft to lower and move the still-open umbrella toward the pot. The umbrella moves as one rigid connected canopy-and-shaft assembly. Keep its grip continuous and do not swap hands. The free hand rests against its own thigh. The feet remain planted on the sidewalk. Finish with the canopy visibly centered above the pot while most of the robot's head and shoulders are outside its cover in the rain. The umbrella does not shrink, fold, detach, or touch the flower.
6–8 seconds: the robot holds the umbrella steady over the pot and quietly watches the flower. Rain remains visible around the canopy, and puddle rings continue on the road. End on this small act of care from the same distant viewpoint. The robot never notices or looks into the camera. No return to the starting pose and no loop.

Photoreal practical-effects character with believable joint motion, damp metal, soft daylight, and restrained movement. Optional audio: rain recorded from the sheltered camera position, with very faint mechanical movement at a distance; no close-miked dialogue, music cue, or dramatic sound effect. If audio is not supported, export silently.

Negative prompt: growing subject, automatic zoom, face close-up, moving across the street, camera orbit, film cuts, eye contact with camera, waving at viewer, extra robot or person, extra umbrella, second flowerpot, umbrella changing size, detached shaft, grip swap, additional fingers, floating feet, sunlight transition, dry pavement, disappearing rain, added text, watermark, timestamp, CCTV interface.
```

[← Back to this case in the README](../README.md#c05-distant-observer-a-robot-in-the-rain-by-seeapi-inspired-by-pablo-prompt)
