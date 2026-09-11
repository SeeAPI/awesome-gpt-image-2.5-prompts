# Case 03：双人温室点灯

## 项目理解与关键假设

两张独立人物图 → 双人场景首帧 → 8 秒单镜头视频，横屏 16:9。采用手绘动画质感，重点是双人身份一致和一个可读的道具动作。本包已生成静态参考素材；视频尚未生成。

## 故事梗概

Mira 将一颗琥珀种子放入温室灯具，Ren 在旁守候；灯亮起后，两人相视微笑。

## 完整故事

傍晚温室里，两位照料者面对一盏尚未点亮的铜灯。Mira 靠近灯具的手掌托着唯一的种子，她看向空槽；Ren 可见的一只手停在灯座旁。Mira 用空闲手的拇指和食指从托举的掌心拿起种子，放进空槽。接触后，暖光照亮两人的脸。她收回手，种子留在槽内，两人确认成功并微笑。视频停在亮灯结果，不自动复位。

## 连续性设定

| 对象 | 固定设定 | 允许变化 |
|---|---|---|
| C03-R01 Mira 定妆图 | 约 30 岁，棕色皮肤，黑色短卷发，橘色外套，奶油色上衣，海军蓝裤子 | 手部动作、视线和表情 |
| C03-R02 Ren 定妆图 | 约 32 岁，浅橄榄肤色，黑色低发髻，绿色外套，深灰上衣和裤子 | 视线和微笑 |
| 琥珀种子 | 全片仅一颗 | 托举掌心 → 空闲手指间 → 灯槽 |
| 铜灯 | 固定在石台中央，开始未亮、空槽 | 种子入槽后逐渐亮起 |
| 温室 | Mira 画面左，Ren 右，蓝调黄昏、石台和玻璃顶 | 轻微叶片运动、暖光反射 |

## Text to Image 资产与提示词

C03-R01 Mira 定妆图与 C03-R02 Ren 定妆图：本例先生成双人设定图，再拆成两个独立文件供下游上传。源图目标比例为 3:2，拆分后为竖幅。用户已有两张人物图时可直接替换，跳过生成。

无需上传其他原始图片，本图可直接使用文字生成。

```text
Generate a widescreen 3:2 character reference diptych, exactly two equal vertical panels with a plain warm gray background, no border or text. The panels will be cropped into two separate identity reference images. Each panel contains exactly one full-body adult original human character, head to boots fully visible with ample margins, both at identical scale.
Left panel: MIRA, an adult woman aged about 30, medium-brown skin, short curly black bob, oval face, dark eyes, rust-orange utility jacket over cream shirt, navy work trousers, brown ankle boots. No jewelry, no hat, no props. Arms relaxed and hands fully visible.
Right panel: REN, an adult man aged about 32, light olive skin, straight dark hair tied in a small low bun, clean-shaven angular face, dark eyes, moss-green utility jacket over charcoal shirt, charcoal trousers, brown work boots. No jewelry, no hat, no props. Arms relaxed and hands fully visible.
Style: cinematic hand-painted animation concept art, softly textured gouache backgrounds, clear expressive faces, grounded anatomy, restrained warm colors, diffuse studio lighting. Neutral front three-quarter standing poses. These are original greenhouse caretakers, no celebrities, no existing film characters. Do not blend identities, duplicate people, invent props, add text or crop limbs.
```

负面提示词：extra person, mixed identities, cropped feet, text, prop, collage inside a character panel。

实际图片：[Mira](../../assets/03-two-character-video/mira-reference.png)、[Ren](../../assets/03-two-character-video/ren-reference.png)。

## Image Edit 关键帧

### 新图片编号与名称

C03-K01 温室点灯首帧。

### 本次任务

将两名已定义的人物放入同一个温室，保留身份，建立种子尚未入槽的动作起点。目标比例 16:9。

### 本次需要使用的原始图片

- C03-R01 Mira 定妆图（T2I 资产）：作为上传图片 1，锁定脸、发型、肤色和橘色服装。
- C03-R02 Ren 定妆图（T2I 资产）：作为上传图片 2，锁定脸、发型、肤色和绿色服装。

### 编辑提示词

```text
Use the two uploaded character portraits as separate strict identity references: image 1 is MIRA, the woman with a rust-orange jacket; image 2 is REN, the man with a moss-green jacket. Preserve each person's face, hairstyle, skin tone, age, body proportions, and entire outfit. Do not merge or swap their identities.

Create a single cinematic 16:9 opening frame in the same hand-painted animation style. A glass greenhouse at blue hour, quiet foliage at the edges, dark blue glass roof overhead, a waist-high stone workbench across the foreground. Mira stands on the LEFT, Ren on the RIGHT, facing slightly inward toward one small unlit brass lantern fixed at the center of the bench. Mira's open right palm holds exactly one small amber glass seed just left of the lantern. Ren's left hand rests beside the lantern base, leaving the empty circular socket clearly visible. All hands remain distinct. Both faces are clearly readable in a medium-wide shot.

The lantern is attached to the bench and cannot move; its socket is empty. The amber seed has not been inserted yet. Soft cool dusk light and a faint warm reflection from the seed. Calm anticipation, grounded anatomy, subtle gouache texture, no text, no labels, no montage, no extra people, no duplicate seed, no costume changes, no oversized hands. This is the first frame before the action, not the finished glowing result.
```

### 负面提示词

face swap, merged hands, duplicate seed, lit lantern before insertion, costume change, split screen, text。

### 验收要点

- Mira 左、Ren 右，两张脸可辨，衣服对应原图。
- 只有一颗种子，仍在 Mira 靠近灯具的掌心上。
- 灯槽为空，灯未点亮，手与灯具没有融合。

## Image to Video 参考图上传方案

- 首帧：C03-K01 温室点灯首帧；优先级最高。
- 人物身份：C03-R01、C03-R02；仅在工具有额外身份参考槽时追加。
- 环境由 C03-K01 控制；无需额外环境图。
- 无独立尾帧，不将未生成的结果图当作素材。
- 仅支持一张图时只上传 C03-K01，不上传双栏人物设定图。

### 主提示词与负面提示词

```text
Create an 8-second cinematic hand-painted animation, 16:9, one continuous medium-wide shot. C03-K01 is the exact first frame and controls composition, greenhouse, bench, lantern, and initial hand positions. C03-R01 locks Mira's identity and rust-orange outfit; C03-R02 locks Ren's identity and moss-green outfit. If only one image is supported, use C03-K01 alone. Mira stays on screen-left, Ren on screen-right. Preserve both faces, hairstyles, skin tones, ages, clothes, and body proportions throughout.

0–2 seconds: Mira looks from the single amber seed on her seed-bearing palm to the empty lantern socket. Ren watches the socket, his visible hand resting beside the fixed base. Gentle breathing; leaves shift slightly in the greenhouse draft. The camera stays locked.
2–5 seconds: Mira uses the thumb and index finger of her free hand to lift the seed from her open seed-bearing palm, then seats it in the lantern's circular socket. Show one continuous transfer and contact. Ren does not take the seed or move the lantern. Once the seed is seated, its amber light gradually illuminates the lantern and nearby faces.
5–8 seconds: Mira withdraws the hand that placed the seed; the seed remains visibly seated. Both look at the illuminated lantern and exchange a small satisfied smile. Warm reflections settle on the glass roof. End on the two distinct characters and the lit lantern. Do not reset the action or loop.

Keep movement restrained and expressive, with coherent hand anatomy and stable painted textures. No scene cuts. Optional audio: faint greenhouse wind, a soft glass click at contact, and a gentle electrical hum after illumination; no dialogue or lip-sync. If audio is unavailable, export silently.

Negative prompt: face swap, merged people, outfit morphing, duplicate seed, disappearing seed, extra fingers or arms, passing objects through solid glass, floating lantern, premature illumination, camera orbit, zoom, captions, text, logos, unrelated cuts, flickering identities.
```

## 后期制作建议

使用工具实际支持的时长，必要时剪成约 8 秒；保持一个完整镜头。视频生成后再验收身份、手部、种子数量及入槽后亮灯的因果顺序。本仓库尚无该视频成片。
