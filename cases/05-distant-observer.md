# Case 05：雨中机器人与远景旁观视角

## 项目理解与关键假设

采用用户指定的远景“偶然拍到”视角，先定义角色，再创建远处场景首帧，最后图生视频。原创故事为旧机器人把自己的伞让给路边小花。目标竖屏 9:16、约 8 秒、单镜头。静态素材由内置图像工具生成，视频尚未生成。

参考链接：[Pablo Prompt](https://x.com/pabloprompt/status/2097382752622436744)。原帖文字注明 GPT Image 2 + Seedance 2.5 in CapCut；本文不将其改称为 GPT Image 2.5。已读取帖文，视频截图未成功，下面按用户给定的远景玩法独立设计，不声称逐镜复现。

## 故事梗概

雨中，一个旧机器人发现路边的小花正在淋雨。它弯下身，把伞移过去，自己留在雨里。

## 完整故事

摄影机躲在街对面空门廊的遮雨处，越过模糊的门框望向对面人行道。一个锈红色机器人举着黄色伞停在青绿色卷帘门前。它低头注意到脚边陶盆里的一朵小白花，慢慢屈膝弯腰，把始终打开的雨伞降到花盆上方。伞沿不碰花，握柄的手不更换。雨继续打在它露出的头和肩上，它只是低头看着花。镜头始终不靠近，机器人也没有发现摄影机。

## 连续性设定

| 对象 | 固定设定 | 状态变化 |
|---|---|---|
| C05-R01 旧机器人定妆图 | 锈红钢身、米白头、双圆眼、无嘴、双臂双腿、三指手、左髋橄榄色小包 | 站立 → 低头 → 屈膝弯腰 |
| 黄色雨伞 | 仅一把，始终打开，伞杆连接完整，持续由同一只手握持 | 机器人上方 → 陶盆上方 |
| 陶盆小白花 | 一个陶盆、一株植物、一朵白花 | 位置不动，仅茎叶微晃 |
| 场景 | 街对面人行道、青绿卷帘门、湿路面、持续阴雨 | 水面波纹和雨线运动 |
| 观察点 | 对街门廊，本例主体直立时约占画面高 18% | 极轻手持漂移，不推近 |

弯腰时机器人投影高度自然变小；不能通过放大角色或推镜头来维持固定占比。

## Text to Image 资产与提示词

C05-R01 旧机器人定妆图：目标 2:3 竖幅全身，锁定外形和颜色。它是身份图，不是视频首帧。无需上传其他原始图片，本图可直接使用文字生成。

```text
Create one portrait 2:3 full-body character identity reference photograph of an original friendly obsolete street-maintenance robot. It is a physically built practical movie prop, about 2 meters tall, with a stocky weathered rust-red steel torso, off-white rounded rectangular head, exactly two small round dark glass eyes, no mouth, two thick articulated arms, exactly three blunt fingers on each hand, two short sturdy legs, and broad dark rubber feet. Its plates show chipped paint and light rain marks, never military armor. One small olive canvas pouch is strapped at its left hip. No writing, badges, logos, screens, weapons, or human face.
The robot stands upright in a relaxed front three-quarter pose on a plain mid-gray studio floor and seamless backdrop. Both empty hands, full head, and both feet are clearly visible with ample margins. No props in the hands, no umbrella in this identity reference. Keep one single robot, no collage, no turnaround grid, no other subject.
Photoreal practical-effects cinematography, tactile metal and canvas, soft overcast illumination, understated warmth. Design a unique humble municipal helper with rounded proportions, not an existing franchise robot.
```

负面提示词：existing franchise robot, extra limbs, mouth, human face, extra pouch, text, weapon, cropped feet。

实际素材：[机器人定妆图](../assets/05-distant-observer/robot-reference.png)。

## Image Edit / Image-to-Image 场景图

### 新图片编号与名称

C05-K00 雨街远景草稿。

### 本次任务

将同一个机器人置于街对面，加入伞和花盆，建立远景、遮挡及未开始让伞的动作状态。目标 9:16。

### 本次需要使用的原始图片

- C05-R01 旧机器人定妆图（T2I 资产）：锁定机器人头部、身形、装甲颜色、关节、手指和小包；不继承定妆图的近景构图。

### 编辑提示词

```text
Use the uploaded robot portrait as the strict identity reference C05-R01: preserve the rust-red stocky steel body, off-white rounded rectangular head, two round dark eyes, no mouth, two arms, three blunt fingers per hand, two legs, rubber feet, and single olive pouch at its left hip.

Create one photoreal 9:16 vertical first frame with the visual feeling of a candid distant observation of a fictional scene. The camera is sheltered inside an unoccupied cafe doorway across a narrow rain-soaked street, about 25 meters from the robot. Use a moderate telephoto perspective with compressed depth and natural lens softness, not a wide-angle close-up. A dark out-of-focus door jamb occupies only the left 8% of the image and a soft blurred ledge crosses the bottom 5%; neither covers the robot or the flowerpot. No people or camera equipment are visible.

On the far sidewalk, the robot stands just right of center beneath its one OPEN mustard-yellow umbrella. The robot's body from head to feet occupies only 24–28% of the entire image height; keep it visibly small in a much larger urban environment. Its lowered gaze is directed at one terracotta flowerpot on the ground immediately to its right, containing one short green plant with one small white flower. The pot is close enough for the robot to shelter it by lowering and moving the umbrella a short distance. The hand nearest the pot holds the umbrella shaft at chest height; the free hand hangs at its side. The umbrella is currently above the robot, NOT already above the pot. Show the shaft continuously attached to the canopy and gripped by one hand.

Quiet old tram-stop frontage with a closed teal shutter behind the robot, damp pale plaster walls, a curb, a wet road occupying much of the lower middle frame, soft rain and broad puddle reflections. No readable shop names, road text, logos, vehicles, pedestrians, or other plants. The setting and wet empty space should dominate. Overcast afternoon daylight, subdued colors except the rust-red robot, yellow umbrella, and terracotta pot. The umbrella and flowerpot remain separate and fully visible. Natural slightly imperfect observer framing, no surveillance overlays, timestamp, cinematic black bars, or exaggerated bokeh. This is an ordinary street seen from afar, with one unexpected quiet act about to happen; not a hero portrait.
```

### 负面提示词

hero portrait, close-up, cropped umbrella, extra flowerpot, blocked action, readable text, crowd, vehicle, sunny weather, CCTV overlay。

### 验收要点

- 机器人明显小于环境，双脚落在对街人行道上。
- 仅一把伞和一盆花，伞杆与手连续连接。
- 伞仍在机器人上方，小花尚未被遮住，后续动作才有变化。
- 门框只挡边缘，不挡机器人、伞或小花。
- 静态远景成功不代表视频镜头锁定已验证。

## 场景局部修正

### 新图片编号与名称

C05-K01 雨街远景首帧（从 C05-K00 修正）。

### 本次任务

首轮图片的花盆位于伞沿下，需将它移到伞右侧的雨中，让“给花让伞”有明确起点。保留实际较小的主体占比，不为了满足原始 24–28% 目标而放大它。

### 本次需要使用的原始图片

- C05-K00 雨街远景草稿（已生成场景图）：锁定机器人、雨伞、摄影机位置和所有环境，只改变一盆花的位置。该草稿位于 `assets/05-distant-observer/rainy-street-draft.png`。

### 编辑提示词

```text
Edit this distant rainy street frame with one local correction only. Move the existing terracotta pot and its single white flower to the RIGHT along the same sidewalk plane, so the ENTIRE pot and flower are visibly outside the yellow umbrella canopy's rightmost edge and receiving rain. Place the pot center at approximately 89% of image width, preserving its current size and its grounded contact with the sidewalk. Leave a visible horizontal rain-filled gap between the canopy's right edge and the flower. Remove the pot completely from its old position; there must still be exactly one pot and one flower.

Keep everything else unchanged: exact camera distance and framing, small robot size and pose, its two eyes and olive pouch, umbrella angle and connected shaft, hand grip, shutter, building, wet road, rain, bench, foreground doorway and blurred ledge, light, texture, and image dimensions. Do not move or enlarge the robot, change the umbrella, add characters, or crop the image. This frame is BEFORE the robot moves its umbrella over the pot.
```

### 负面提示词

duplicate flowerpot, moved robot, enlarged subject, changed umbrella, new camera angle, missing rain。

### 验收要点

- 花盆仅一只，原位置清空，新位置在伞外且落地。
- 机器人和摄影机不移动，伞仍罩着机器人。
- 视频使用修正后的 C05-K01，不再使用草稿 C05-K00。

## Image to Video 参考图上传方案

- 必需首帧：C05-K01 雨街远景首帧，锁定距离、构图、道具和动作起点。
- 可选身份图：C05-R01 旧机器人定妆图，仅在支持额外参考槽时追加。
- 环境由 C05-K01 控制，不需要额外场景图。
- 无独立尾帧，结束状态由动作提示词定义。
- 单图工具只上传 C05-K01，不使用近景定妆图做首帧。

### 主提示词与负面提示词

```text
Animate C05-K01 as the exact first frame of an 8-second photoreal 9:16 distant-observer video, one uninterrupted shot. C05-R01 is optional robot identity reference only if the tool supports an extra reference slot. If only one image is allowed, use C05-K01. Preserve its street layout, wet road, teal shutter, foreground doorway edge, robot size, umbrella, and flowerpot.

The camera remains inside the doorway across the street at the same approximately 25-meter distance. Match the robot's exact small standing scale in C05-K01 (about 18% of frame height in the supplied example), rather than enlarging it to meet a numerical target. As it bends, allow its projected height to decrease naturally; never enlarge it or move the camera to compensate. The viewer should feel they happened to notice a small event on the far sidewalk. Only very slight low-amplitude handheld drift, under 1% of frame width; no zoom, push-in, tracking toward the subject, close-up, camera cut, or dramatic rack focus. Foreground occlusion remains at the edges, never over the action.

0–2 seconds: the rust-red robot pauses under its open yellow umbrella and tilts its off-white head down toward the single terracotta pot and white flower beside it. Rain continues falling; the flower stem nods slightly. Keep exactly two eyes, no mouth, one olive hip pouch, and the same physical body proportions.
2–6 seconds: the robot bends at the knees and waist, using the hand already gripping the umbrella shaft to lower and move the still-open umbrella toward the pot. The umbrella moves as one rigid connected canopy-and-shaft assembly. Keep its grip continuous and do not swap hands. The free hand rests against its own thigh. The feet remain planted on the sidewalk. Finish with the canopy visibly centered above the pot while most of the robot's head and shoulders are outside its cover in the rain. The umbrella does not shrink, fold, detach, or touch the flower.
6–8 seconds: the robot holds the umbrella steady over the pot and quietly watches the flower. Rain remains visible around the canopy, and puddle rings continue on the road. End on this small act of care from the same distant viewpoint. The robot never notices or looks into the camera. No return to the starting pose and no loop.

Photoreal practical-effects character with believable joint motion, damp metal, soft daylight, and restrained movement. Optional audio: rain recorded from the sheltered camera position, with very faint mechanical movement at a distance; no close-miked dialogue, music cue, or dramatic sound effect. If audio is not supported, export silently.

Negative prompt: growing subject, automatic zoom, face close-up, moving across the street, camera orbit, film cuts, eye contact with camera, waving at viewer, extra robot or person, extra umbrella, second flowerpot, umbrella changing size, detached shaft, grip swap, additional fingers, floating feet, sunlight transition, dry pavement, disappearing rain, added text, watermark, timestamp, CCTV interface.
```

## 后期制作建议

保留完整的远景动作，不裁切成角色特写。按工具支持时长生成后剪取约 8 秒的连贯单镜头。声音采用观察点附近的雨声，远处关节声很轻；没有音频能力时导出静音。验收伞杆、握持和膝关节连续性，确认花盆不漂移、镜头不推近。本仓库目前没有该案例的视频成片。
