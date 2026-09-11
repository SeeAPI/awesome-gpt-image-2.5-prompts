# Case 04：灯塔修理员与机械海鸟

## 项目理解与关键假设

角色设定 → 四镜头分镜 → 四张镜头首帧 → 图生视频 → 剪辑。目标 12 秒、四镜头、横屏 16:9，微缩定格电影质感。已提供静态参考素材，视频尚未生成。

## 故事梗概

老修理员 Inez 为机械海鸟上发条，让它从灯塔窗台重新飞向海面。

## 完整故事

海边灯塔的工作台上，一只黄铜海鸟垂着翅膀。Inez 看见它，伸手握住鸟身旁的固定发条钥匙。一个半圈后，齿轮响起，鸟抬头。她松开手，鸟展开翅膀向窗边迈步，她伸出掌心护送它。剪到已经打开的窗台，鸟蹬离窗沿，拍翼飞向海面；Inez 收回手，安静地微笑。

## 连续性设定

| 对象 | 固定设定 | 状态顺序 |
|---|---|---|
| C04-R01 Inez 定妆图 | 约 60 岁，银灰短卷发，圆形玳瑁眼镜，海军蓝外套，赭色毛衣 | 发现 → 专注 → 欣喜 → 目送 |
| 黄铜海鸟 | 掌心大小、仅一只、两个铰接翅膀、左侧附着发条钥匙 | 静止 → 上弦 → 苏醒 → 飞走 |
| 工作室 | 木台在拱形窗下，窗在房间右侧且一直打开，阴天海光 | 无场景结构变化 |
| 手部动作 | 一手扶鸟、一手转钥匙；之后双手离开鸟翼 | 不能与鸟翼融合或凭空增加手指 |

## Text to Image 资产与提示词

C04-R01 Inez 定妆图：单人全身图，目标比例 3:2，锁定脸、年龄和材质风格。无需上传其他原始图片，本图可直接使用文字生成。

```text
Generate one landscape 3:2 clean single-character full-body identity reference portrait. Original protagonist INEZ, a lighthouse mechanic aged about 60, warm tan skin, short silver-gray curly hair, round tortoiseshell glasses, kind lined face, navy wool chore coat over an ochre knitted sweater, charcoal trousers and weathered dark brown work boots. Her hands are empty and visible, arms relaxed, head and boots fully inside the frame with ample margins. She stands in a neutral three-quarter pose against a simple warm gray studio backdrop. No other characters or props, no collage or additional views, no text.
Visual style: tactile miniature stop-motion film design, felted wool costume, subtly sculpted expressive face, cinematic soft overcast coastal light, muted navy and ochre palette, believable anatomy. Preserve the subject as a clearly older adult woman, no glamour retouching.
```

负面提示词：younger face, missing glasses, costume variation, extra person, props, text, cropped boots。

实际素材：[Inez 定妆图](../../assets/04-storyboard-video/inez-reference.png)。

## Image Edit / Image-to-Image

### 新图片编号与名称

C04-B01 灯塔四镜头分镜。

### 本次任务

以 Inez 为唯一主角生成 2×2 分镜，将发现、上弦、苏醒、放飞起点组织成四个不同镜头。目标整图 16:9，每格也为 16:9。

### 本次需要使用的原始图片

- C04-R01 Inez 定妆图（T2I 资产）：锁定年龄、面孔、眼镜、发型、衣服和微缩材质。

### 编辑提示词

```text
Use the uploaded full-body portrait of INEZ as the strict identity and visual-style reference. Preserve her older adult face, short silver-gray curls, round tortoiseshell glasses, navy wool coat, ochre sweater, charcoal trousers, and brown work boots. Create one 16:9 storyboard sheet divided into an EXACT 2x2 grid of four equal 16:9 cinematic panels, no gutters, panel labels, numbers, captions, text, or borders. Reading order is left to right, top to bottom. This is a four-shot narrative storyboard, NOT consecutive animation frames.

Original story: in a tiny coastal lighthouse workshop, Inez revives one palm-sized brass mechanical seabird with an attached winding key, then lets it fly out of an already-open window. Tactile miniature stop-motion film look, felted wool clothing, sculpted face, softly weathered brass, overcast coastal daylight. The same wooden workbench runs beneath one arched OPEN window on the RIGHT of the room; cool sea beyond. One brass mechanical bird only, two hinged wings, one small attached winding key on its left flank. No loose tools or unrelated objects.

Panel 1, establishing medium-wide shot: Inez is on the LEFT of the workbench looking down at the inert bird resting on the bench at center-right. Both bird wings are folded. Her hands rest on the bench on either side of the bird without touching the key. The open window is visible on the right. This is the first moment before repair.
Panel 2, close-up from the same side of the bench: one of Inez's hands gently braces the bird body; her other hand holds the small attached winding key on its left flank, ready to turn. Both wings remain folded. Show enough ochre sleeve and navy cuff to link her costume. Brass bird geometry must match panel 1, not a different bird. Key remains attached.
Panel 3, medium shot: Inez smiles at the same bird standing on the bench, both hinged wings now partly unfolded, head lifted. Her hands are withdrawn and clearly separate from its wings. Bird has not taken off. Same window on right, same lighting and clothes.
Panel 4, medium-wide shot toward the open window: Inez remains on the LEFT with an open supporting palm near the window sill. The same brass bird rests on the RIGHT sill with wings poised for takeoff toward the open sea, still physically supported. Maintain the single window and its already-open state. Inez's face is visible in three-quarter profile, quietly proud. This is the beginning of the release shot, before the bird flies away.

Keep causal continuity, a single recognizable protagonist, one bird, stable costume, stable room geography, plausible hands, and a clear visual link between the close-up and wide shots. No magic beams, glowing eyes, extra characters, flying tools, missing glasses, unreadable writing, duplicate birds, grid overlays, or photoreal human replacement.
```

### 负面提示词

duplicate bird, detached winding key, changing glasses, closed window, fused hands, text, labels, unrelated props。

### 验收要点

- 同一位 Inez、同一只鸟，鸟翼数量正确。
- 发现 → 接触钥匙 → 展翼 → 窗台待飞，动作状态可区分。
- 窗口一直打开，工作台与窗的位置连贯。
- 特写中的鸟体与全景一致，手指没有融合。

### 镜头首帧拆分

C04-K01 发现、C04-K02 上弦、C04-K03 苏醒、C04-K04 放飞，均由 C04-B01 从左到右、从上到下裁切，属于已有分镜的裁片，不是新生成图。运行 `python scripts/prepare_video_references.py` 可复现。四格图不能直接作为四帧动画。

### 单个镜头需要修正时

只重新生成有问题的一格；下面的四个任务各自产生一张新图，其他镜头保持原样。修正图通过验收后才替换视频输入。

#### 新图片编号与名称

C04-K01R 发现修正版。

#### 本次任务

修正该镜头的身份、道具或动作起点，输出单张 16:9 画面。

#### 本次需要使用的原始图片

- C04-R01 Inez 定妆图（T2I 资产）：锁定面孔、眼镜和衣服。
- C04-K01 发现（已生成分镜裁片）：锁定对应镜头的构图、场景和动作状态。

#### 编辑提示词

```text
Create one corrected single shot, preserving Inez from C04-R01 and the composition from C04-K01. Inez stands on the left of the bench, both hands resting beside the inert brass bird with folded wings. The arched window is already open at right. Keep the navy coat, ochre sweater, silver curls, round glasses, one brass bird, two wings, attached key, open-window geography, and miniature-film material style unchanged. Fix only continuity errors. No collage, text, extra characters, duplicate bird, or new props.
```

#### 负面提示词

face drift, bird redesign, extra fingers, detached key, closed window, collage, text。

#### 验收要点

- 身份、服装和鸟体与来源图对应。
- 动作起点正确，鸟数为一，窗口打开。

#### 新图片编号与名称

C04-K02R 上弦修正版。

#### 本次任务

修正该镜头的身份、道具或动作起点，输出单张 16:9 画面。

#### 本次需要使用的原始图片

- C04-R01 Inez 定妆图（T2I 资产）：锁定面孔、眼镜和衣服。
- C04-K02 上弦（已生成分镜裁片）：锁定对应镜头的构图、场景和动作状态。
- C04-K01 发现（已生成分镜裁片）：锁定鸟体结构和原始房间布局。

#### 编辑提示词

```text
Create one corrected single shot, preserving Inez from C04-R01 and the composition from C04-K02. Close-up of one hand bracing the same bird and the other holding its attached left-flank winding key. Keep wings folded and match the bird geometry to C04-K01. Keep the navy coat, ochre sweater, silver curls, round glasses, one brass bird, two wings, attached key, open-window geography, and miniature-film material style unchanged. Fix only continuity errors. No collage, text, extra characters, duplicate bird, or new props.
```

#### 负面提示词

face drift, bird redesign, extra fingers, detached key, closed window, collage, text。

#### 验收要点

- 身份、服装和鸟体与来源图对应。
- 动作起点正确，鸟数为一，窗口打开。

#### 新图片编号与名称

C04-K03R 苏醒修正版。

#### 本次任务

修正该镜头的身份、道具或动作起点，输出单张 16:9 画面。

#### 本次需要使用的原始图片

- C04-R01 Inez 定妆图（T2I 资产）：锁定面孔、眼镜和衣服。
- C04-K03 苏醒（已生成分镜裁片）：锁定对应镜头的构图、场景和动作状态。
- C04-K01 发现（已生成分镜裁片）：锁定鸟体结构和原始房间布局。

#### 编辑提示词

```text
Create one corrected single shot, preserving Inez from C04-R01 and the composition from C04-K03. Medium shot of the same bird with two partly unfolded wings on the bench. Inez smiles with her hands withdrawn; keep the window on the right. Keep the navy coat, ochre sweater, silver curls, round glasses, one brass bird, two wings, attached key, open-window geography, and miniature-film material style unchanged. Fix only continuity errors. No collage, text, extra characters, duplicate bird, or new props.
```

#### 负面提示词

face drift, bird redesign, extra fingers, detached key, closed window, collage, text。

#### 验收要点

- 身份、服装和鸟体与来源图对应。
- 动作起点正确，鸟数为一，窗口打开。

#### 新图片编号与名称

C04-K04R 放飞修正版。

#### 本次任务

修正该镜头的身份、道具或动作起点，输出单张 16:9 画面。

#### 本次需要使用的原始图片

- C04-R01 Inez 定妆图（T2I 资产）：锁定面孔、眼镜和衣服。
- C04-K04 放飞（已生成分镜裁片）：锁定对应镜头的构图、场景和动作状态。
- C04-K01 发现（已生成分镜裁片）：锁定鸟体结构和原始房间布局。

#### 编辑提示词

```text
Create one corrected single shot, preserving Inez from C04-R01 and the composition from C04-K04. The bird is physically supported on the already-open window sill, wings ready for takeoff. Inez remains left with an open palm nearby. Do not show flight yet. Keep the navy coat, ochre sweater, silver curls, round glasses, one brass bird, two wings, attached key, open-window geography, and miniature-film material style unchanged. Fix only continuity errors. No collage, text, extra characters, duplicate bird, or new props.
```

#### 负面提示词

face drift, bird redesign, extra fingers, detached key, closed window, collage, text。

#### 验收要点

- 身份、服装和鸟体与来源图对应。
- 动作起点正确，鸟数为一，窗口打开。

## Image to Video 参考图上传方案

- 人物身份：C04-R01 Inez 定妆图，仅在支持身份参考槽时追加。
- 分镜策划：C04-B01，用于理解镜头顺序，不能作为单镜头首帧。
- 镜头 1–4 首帧：依次使用 C04-K01–K04；如已验收修正版则使用对应 R 版本。
- 环境、鸟体和动作起点由每张镜头首帧控制，无需上传额外环境图。
- 没有独立尾帧。最后一格是放飞镜头的起点，不是假称已经飞走的尾帧。
- 只有一个输入槽时，每次只上传该镜头的 C04-K 图，使用完整连续性约束及对应镜头段落。

### 主提示词与负面提示词

```text
Create a 12-second, 16:9 miniature stop-motion-style short film called The Last Flight, with four shots and clear tactile stepped motion. Do not render the title as text. C04-R01 is the identity reference for Inez. C04-B01 is a storyboard for planning only, not a frame sheet to animate directly. C04-K01 through C04-K04 are individual shot-start references. Never show the grid or multiple panels in the video.

Continuity: Inez is the same older woman with silver curls, round tortoiseshell glasses, navy coat and ochre sweater. There is one palm-sized brass mechanical seabird, two hinged wings, and one attached winding key on its left flank. The wooden bench is below a single already-open arched window on room-right. Overcast sea light stays constant. The bird progresses from inert to wound to active to airborne; it never duplicates or changes species.

Shot 1, 0–3 seconds, start from C04-K01: locked medium-wide shot. Inez notices the folded, inert brass bird on the bench, leans slightly closer, and reaches toward its attached key. The open window remains visible on the right. Cut on her reaching hand to the matching close-up.
Shot 2, 3–6 seconds, start from C04-K02: locked close-up. One hand braces the bird; the other gives its attached key one slow half-turn. The key remains attached and her fingers keep contact. A small mechanical click prompts the bird's head to lift slightly. Cut on this first movement to the wider reaction.
Shot 3, 6–9 seconds, start from C04-K03: medium shot. The bird unfolds its two wings, takes two short steps toward the right, and Inez offers her open palm beside it. She smiles, keeping her glasses and outfit unchanged. Cut in the direction of the bird's movement to the open-window shot; the short move to the sill is an intentional edit, not a teleport within a shot.
Shot 4, 9–12 seconds, start from C04-K04: medium-wide shot. From the sill, the bird pushes off with both feet and makes two small mechanical wingbeats, flying out through the already-open window toward screen-right. Inez withdraws her supporting palm and follows it with her gaze. End with her quiet smile and the open sea. The bird stays the same small brass object as it recedes. No reset or loop.

No camera movement is required. Prioritize readable action over extra cuts. Optional audio: low coastal wind, a winding click, two soft metallic wing flutters; no dialogue, captions, or lip-sync. If audio generation is unavailable, export silent clips.

Negative prompt: visible storyboard grid, collage animation, extra bird, detached key, changing bird design, wardrobe morph, missing glasses, extra fingers, hand-wing fusion, closed window, flight through glass, unmotivated room change, continuous-shot teleport, photoreal skin, fast montage, crossfades, text or logos.

Limited-input fallback: generate four separate 3-second clips using only the matching C04-K image as that clip's first frame and the corresponding shot paragraph above plus the continuity and negative instructions. Trim to three seconds per clip and join with straight cuts. If the generator requires a longer minimum duration, generate that duration and select a coherent three-second segment; the 12-second timing is an editing target, not a claim about a particular model's supported settings.
```

## 后期制作建议

按 1→2→3→4 顺序选取四段约 3 秒的连贯片段并直切，总长约 12 秒。若工具最短时长更长，在生成后剪取合适片段。工作台到窗台是明确剪辑省略，不能要求单镜头内瞬移。成片生成后再检查鸟体连续性、钥匙是否附着、手部与窗口穿越。
