# GPT Image 2.5 精选提示词库 🎨

[English](README.md) | [简体中文](README_zh.md)

**由 SeeAPI 精选的创意图像提示词与工作流。**

探索 GPT Image 2.5 在角色贴纸、产品视觉、微缩世界、GIF 素材和定格动画场景中的创意玩法。复制提示词，替换为自己的内容，尝试新的创作方向。

本仓库将持续更新提示词示例、生成图片和实用复现说明。

**5 个创意工作流 · 42 条独立提示词 · 更新于 2026 年 9 月 14 日**

⭐ 点击 Star 收藏本仓库，为下一次创作留存灵感。

<a id="-featured-examples"></a>

## 🖼️ 精选示例

| 像素 GIF | Minecraft 皮肤 | 卧室改造 |
| :---: | :---: | :---: |
| 动画效果 | 原图 → 效果图 | 原图 → 效果图 |
| [<img src="assets/featured/pixel-art.gif" width="130" height="130" alt="像素大象 GIF">](#c01-pixel-art-character-gif-by-seeapi) | [<img src="assets/p41-minecraft-skin-from-reference/reference.png" width="130" height="130" alt="参考图 → Minecraft 皮肤——原图">](assets/p41-minecraft-skin-from-reference/reference.png) [<img src="assets/p41-minecraft-skin-from-reference/result.png" width="130" height="130" alt="参考图 → Minecraft 皮肤——效果图">](assets/p41-minecraft-skin-from-reference/result.png) | [<img src="assets/p42-bedroom-redesign/reference.png" width="130" height="130" alt="照片 → 卧室改造——原图">](assets/p42-bedroom-redesign/reference.png) [<img src="assets/p42-bedroom-redesign/result.png" width="130" height="130" alt="照片 → 卧室改造——效果图">](assets/p42-bedroom-redesign/result.png) |
| 文字 → 图片 → GIF | 图片 → 图片 | 图片 → 图片 |
| [提示词与步骤](#c01-pixel-art-character-gif-by-seeapi) | [完整提示词](#p41-minecraft-skin-from-a-reference) | [完整提示词](#p42-bedroom-redesign-from-your-photo) |


<a id="-contents"></a>

## 📖 目录

- [🖼️ 精选示例](#-featured-examples)
- [🧭 选择模型](#-choose-your-model)
- [📷 人像与摄影](#-portraits--photography)
- [🧸 角色与趣味创作](#-characters--playful-creations)
- [🛍️ 产品与品牌视觉](#-products--branding)
- [🎨 海报与艺术风格](#-posters--artistic-styles)
- [🏡 家居与室内设计](#-home--interior-design)
- [📊 信息图与实用设计](#-infographics--practical-design)
- [🎬 GIF 与视频工作流](#-gif--video-workflows)
- [📝 来源、使用与维护](#-sources-reuse--maintenance)
- [🙏 致谢](#-acknowledgments)

<a id="-choose-your-model"></a>

## 🧭 选择模型

OpenAI 的 GPT Image 2.5 系列包括 **GPT Image 2.5 Sunburst** 和 **GPT Image 2.5 Flare**。两者均支持文字和图片输入，输出静态图片。以下选型建议与示例素材的实际生成来源分别记录。

| 对比项 | GPT Image 2.5 Sunburst | GPT Image 2.5 Flare |
|---|---|---|
| 主要优势 | 图像生成与精细编辑 | 快速、高质量的日常生成 |
| 适用需求 | 优先考虑编辑精度 | 优先考虑生成速度 |
| 输入 | 文字和图片 | 文字和图片 |
| 输出 | 静态图片 | 静态图片 |
| API 模型 ID | `gpt-image-2.5-sunburst` | `gpt-image-2.5-flare` |
| 官方资料 | [OpenAI 文档](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) | [OpenAI 文档](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) |

<a id="-browse-by-category"></a>
<a id="-prompt-directory"></a>

<a id="-portraits--photography"></a>

## 📷 人像与摄影

<a id="p38-candid-mont-saint-michel-travel-portrait"></a>

### 📌 1.1. 圣米歇尔山旅行抓拍 (作者：[@saniaspeaks_](https://x.com/saniaspeaks_/status/2097532595814940683)) · [来源平台： X](https://x.com/saniaspeaks_/status/2097532595814940683) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p38-candid-mont-saint-michel-travel-portrait/source-example-01.jpg" width="300" height="400" alt="圣米歇尔山旅行抓拍——来源示例">](assets/p38-candid-mont-saint-michel-travel-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人在长满苔藓的岩石旁、沙质海岸上的写实旅行抓拍，身后可见圣米歇尔山历史悠久的修道院、石墙和潮汐滩涂。保留参考发型与面部特征，向镜头露出自然温暖的微笑。

人物身穿宽松黑色长外套，内搭浅色服装，围无标志的柔软奶白围巾，背低调肩包。双手随意插在大衣口袋里。人物位于前景，修道院在背景中清晰可见。柔和傍晚光线、浅蓝天空、真实衣料与皮肤纹理、轻微手机摄影美感、柔和调色、自然比例，3:4 竖幅构图。不虚构品牌徽标或添加文字。
```

<a id="p37-realistic-iphone-cafe-portrait"></a>

### 📌 1.2. 真实 iPhone 咖啡馆人像 (作者：[@blueemi99](https://x.com/blueemi99/status/2097602273085931662)) · [来源平台： X](https://x.com/blueemi99/status/2097602273085931662) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p37-realistic-iphone-cafe-portrait/source-example-01.jpg" width="300" height="400" alt="真实 iPhone 咖啡馆人像——来源示例">](assets/p37-realistic-iphone-cafe-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人在 [cafe setting] 的真实 iPhone 风格抓拍照片，穿着 [outfit]，正在 [simple action]。自然现场光，真实皮肤纹理，随意的手机取景，可信的手部与家具接触，克制的景深和日常色彩。不使用美颜滤镜面容，不改变体型，不添加前景人物、文字或水印。
```

*生成前，请替换 `[cafe setting]`, `[outfit]`, `[simple action]`为自定义内容后再生成。*

<a id="p36-dreamy-high-angle-qipao-portrait"></a>

### 📌 1.3. 梦幻俯拍旗袍人像 (作者：[@BubbleBrain](https://x.com/BubbleBrain/status/2097513469172129825)) · [来源平台： X](https://x.com/BubbleBrain/status/2097513469172129825) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p36-dreamy-high-angle-qipao-portrait/source-example-01.jpg" width="225" height="400" alt="梦幻俯拍旗袍人像——来源示例">](assets/p36-dreamy-high-angle-qipao-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人穿着 [qipao color and design] 的 9:16 竖幅时装人像，服装自然适配其真实比例。使用俯拍高机位、柔和光晕、梦幻背景虚化、精致的 [makeup style] 和轻柔优雅的姿势。面部保持可辨识且足够清晰。不强行拉高或瘦身，不重塑眼睛，不改变性别呈现。不添加文字或水印。
```

*生成前，请替换 `[qipao color and design]`, `[makeup style]`为自定义内容后再生成。*

<a id="p35-monochrome-cybernetic-horror-portrait"></a>

### 📌 1.4. 黑白赛博机械恐怖人像 (作者：[@meng_dagg695](https://x.com/meng_dagg695/status/2097558679956664521)) · [来源平台： X](https://x.com/meng_dagg695/status/2097558679956664521) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p35-monochrome-cybernetic-horror-portrait/source-example-01.jpg" width="400" height="400" alt="黑白赛博机械恐怖人像——来源示例">](assets/p35-monochrome-cybernetic-horror-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

将人像转化为黑白赛博机械恐怖摄影。通过面部结构和表情保持人物可辨识；在眼部周围使用开裂的瓷白色义体表面与内嵌金属细节，不替换头部或改变面部比例。头部周围布置黑色线缆和工业线圈附件，穿破旧深色布料服装。戏剧性低调照明，深黑背景，高对比黑白画面，具有触感的实体特效细节，85mm 人像镜头，浅景深。不添加其他人物，不放大眼睛，不换成无关面容，不添加文字。
```

<a id="p29-caramel-suit-studio-portrait"></a>

### 📌 1.5. 焦糖色西装影棚人像 (作者：[@abs_uiux](https://x.com/abs_uiux/status/2098216202870964315)) · [来源平台： X](https://x.com/abs_uiux/status/2098216202870964315) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p29-caramel-suit-studio-portrait/source-example-01.jpg" width="267" height="400" alt="焦糖色西装影棚人像——来源示例">](assets/p29-caramel-suit-studio-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作一张写实全身影棚人像。参考人物穿温暖焦糖棕色剪裁合身的单排扣西装外套、同色直筒长裤、纯白圆领 T 恤以及擦亮的深棕色系带皮鞋。服装适配其现有身体比例。保留头发与面部毛发，不强行更换发型或变成无胡须面容。

双手自然插入裤袋，肩膀放松，站姿挺直，双脚舒适分开，视线略偏离镜头。纯浅灰影棚背景与无缝地面，柔和漫射光，真实皮肤与衣料褶皱，清晰面部细节和细微接触阴影。构图从头到鞋完整展示全身，平视机位，杂志时装摄影，2:3 竖幅。不添加新配饰或文字。
```

<a id="p17-1969-outdoor-festival-crowd"></a>

### 📌 1.6. 1969 年户外音乐节人群 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

[<img src="assets/p17-1969-outdoor-festival-crowd/source-example-01.webp" width="267" height="400" alt="1969 年户外音乐节人群——来源示例">](assets/p17-1969-outdoor-festival-crowd/source-example-01.webp)

[<img src="assets/p17-1969-outdoor-festival-crowd/source-example-02.webp" width="267" height="400" alt="1969 年户外音乐节人群——来源示例">](assets/p17-1969-outdoor-festival-crowd/source-example-02.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
制作 1969 年 8 月 16 日纽约州贝瑟尔的真实户外人群场景。
写实照片风格，服装、舞台布置和环境符合该年代。
```

<a id="p13-candid-sailor-portrait"></a>

### 📌 1.7. 渔船人物抓拍 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p13-candid-sailor-portrait/source-example-01.webp" width="267" height="400" alt="渔船人物抓拍——来源示例">](assets/p13-candid-sailor-portrait/source-example-01.webp)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人在小渔船上的写实抓拍照片，人物平静地整理渔网，一只狗坐在附近甲板上。人物穿着 [practical sailing outfit]。保留原有皮肤纹理与年龄，不额外添加皱纹或纹身。采用平视中景人像、50mm 镜头、柔和海岸日光、浅景深、35mm 胶片颗粒、自然色彩和磨损材质，营造未摆拍的日常氛围。不进行重度修图。
```

*生成前，请替换 `[practical sailing outfit]`为自定义内容后再生成。*

<a id="p12-cinematic-subway-motion-portrait"></a>

### 📌 1.8. 电影感地铁动感人像 (作者待确认) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p12-cinematic-subway-motion-portrait/source-example-01.webp" width="224" height="400" alt="电影感地铁动感人像——来源示例">](assets/p12-cinematic-subway-motion-portrait/source-example-01.webp)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人静站在地铁站台上的电影感人像，一列银黄色列车在其身后驶过，形成水平方向运动模糊。面部清晰，表情平静。人物穿着 [outfit]，手持 [bouquet or prop]。保留原有发型，允许少量发丝在列车带动的气流中自然飘动。融合车站顶部冷光与温暖的皮肤高光，采用浅景深、真实皮肤纹理和细微胶片颗粒。
```

*生成前，请替换 `[outfit]`, `[bouquet or prop]`为自定义内容后再生成。*

<a id="p10-1980s-retro-film-portrait"></a>

### 📌 1.9. 1980 年代复古胶片人像 (作者：[@Goodmanprotocol](https://x.com/Goodmanprotocol/status/2097954772586557873)) · [来源平台： X](https://x.com/Goodmanprotocol/status/2097954772586557873)
#### 👀 预览

[<img src="assets/p10-1980s-retro-film-portrait/source-example-01.webp" width="320" height="400" alt="1980 年代复古胶片人像——来源示例">](assets/p10-1980s-retro-film-portrait/source-example-01.webp)

[<img src="assets/p10-1980s-retro-film-portrait/source-example-02.webp" width="320" height="400" alt="1980 年代复古胶片人像——来源示例">](assets/p10-1980s-retro-film-portrait/source-example-02.webp)

[<img src="assets/p10-1980s-retro-film-portrait/source-example-03.webp" width="320" height="400" alt="1980 年代复古胶片人像——来源示例">](assets/p10-1980s-retro-film-portrait/source-example-03.webp)

[<img src="assets/p10-1980s-retro-film-portrait/source-example-04.webp" width="320" height="400" alt="1980 年代复古胶片人像——来源示例">](assets/p10-1980s-retro-film-portrait/source-example-04.webp)

#### 👇 工作流

`人物参考图 → 复古人像`

#### 🔖 完整提示词

```text
使用提供的人物作为精确面部参考，制作一张真实的 1980 年代复古人像，采用 4:5 竖幅比例。高度准确地保留其身份、面部结构、可辨识特征、肤色和自然表情，不改变或美化面容。

为主体设计经典的 1980 年代发型以及符合年代的时装，具有大胆轮廓、真实纹理和自然的复古气质。人像构图自然，具有鲜明的杂志摄影感，主体是明确焦点。

画面如同用 35mm 胶片相机拍摄，具有真实胶片颗粒、细微尘点和纹理、轻柔画质、自然皮肤细节、轻微褪色和真实胶片瑕疵。采用温暖怀旧的调色、柔和霓虹高光、细微环境光晕和机顶直闪，形成标志性的 1980 年代照片观感。

照明具有电影感且可信，阴影柔和，高光真实，对比自然，曝光略带胶片的不完美。最终图像应像真正拍摄于 1980 年代，而非数字重制，具有经典、怀旧、时尚且自然洒脱的氛围。
```

<a id="-characters--playful-creations"></a>

## 🧸 角色与趣味创作

<a id="p41-minecraft-skin-from-a-reference"></a>

### 📌 2.1. 参考图 → Minecraft 皮肤 (作者：SeeAPI)
#### 👀 预览

| 原图 | 效果图 |
|---|---|
| [<img src="assets/p41-minecraft-skin-from-reference/reference.png" width="300" height="300" alt="参考图 → Minecraft 皮肤——原图">](assets/p41-minecraft-skin-from-reference/reference.png) | [<img src="assets/p41-minecraft-skin-from-reference/result.png" width="300" height="300" alt="参考图 → Minecraft 皮肤——效果图">](assets/p41-minecraft-skin-from-reference/result.png) |

#### 👇 工作流

`人物照片 → Minecraft 风格图片`

#### 🔖 完整提示词

```text
将上传照片中的人物转化为 Minecraft 风格角色，同时保留可辨识的发型、服装颜色、配饰和关键视觉特征。将整个身体转化为干净的方块体素结构，采用方形几何、像素化纹理和经典 Minecraft 比例。保留原有姿势和整体构图。让角色呈现真实的自定义 Minecraft 皮肤观感，而不是写实的三维人物。使用清晰像素细节、简单明暗和干净的方块造型。
```

<a id="p33-expressive-meme-sticker-sheet"></a>

### 📌 2.2. 夸张表情包贴纸 (作者待确认) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p33-expressive-meme-sticker-sheet/source-example-01.jpg" width="400" height="300" alt="夸张表情包贴纸——来源示例">](assets/p33-expressive-meme-sticker-sheet/source-example-01.jpg)

#### 👇 工作流

`角色参考图 → 贴纸图`

#### 🔖 完整提示词

```text
根据所附图片制作表情包贴纸，融入 😎😛💕🚀🥳。使用夸张的网络反应表情，包括哭泣、困惑、震惊、得意、侧目和面无表情的难以置信，搭配别扭姿势、低保真剪贴纹理和荒诞幽默。

制作一张正方形（1:1）透明贴纸图，九张不同贴纸排列为 3×3 网格，每张展示不同表情、姿势或反应。贴纸之间留宽阔、完全透明的间隔。无背景、阴影或重叠元素。
```

<a id="p18-four-panel-pet-comic"></a>

### 📌 2.3. 四格宠物漫画 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

[<img src="assets/p18-four-panel-pet-comic/source-example-01.webp" width="267" height="400" alt="四格宠物漫画——来源示例">](assets/p18-four-panel-pet-comic/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
制作一张竖向四格短篇漫画。
第 1 格：主人从前门离开。身后窗户中的宠物显得很小，睁大眼睛，爪子高高按在玻璃上，房子突然安静下来。
第 2 格：门咔哒关上，打破寂静。宠物慢慢转向空荡的房子，姿态发生变化，眼神敏锐，仿佛充满可能。
第 3 格：家中景象变了。宠物像主人一样摊在沙发上，旁边有碎屑，阳光像聚光灯般斜穿房间。
第 4 格：门打开。宠物端正地坐在入口处，警觉又镇定，仿佛什么都没发生。
```

<a id="p11-character-dance-pose-grid"></a>

### 📌 2.4. 角色舞蹈姿势网格 (作者：[@renoiseai](https://x.com/renoiseai/status/2097959984265130436)) · [来源平台： X](https://x.com/renoiseai/status/2097959984265130436)
#### 👀 预览

[<img src="assets/p11-character-dance-pose-grid/source-example-01.webp" width="400" height="400" alt="角色舞蹈姿势网格——来源示例">](assets/p11-character-dance-pose-grid/source-example-01.webp)

#### 👇 工作流

`角色参考图 → 16 格舞蹈姿势图`

#### 🔖 完整提示词

```text
@[Image 1] = 角色参考。使用上传图片确定角色的外观、服装、比例、画风和个性，再设计合适的原创舞蹈动作。

制作一张正方形舞蹈参考图，严格按 4×4 网格排列，恰好包含 16 个等大单元格。用纤细清晰的线分隔，每格左上角标注 1–16，按从左到右、从上到下的顺序阅读。每格恰好展示同一角色的一个不同舞姿，且必须为全身。

角色一致性
十六格中保留参考角色的面容、发型、发色、眼睛、肤色、身体比例、服装、鞋子、配饰和标志性细节。匹配参考插画的画风和渲染方式。除非原图就是 Q 版，否则不要改成 Q 版。如果参考图包含多个视图，将其视为同一角色的不同视角。去除手持道具、武器及相关装备，使双手可以用于舞蹈。

适配舞蹈
根据角色的视觉个性、服装和活动能力推断适合的舞蹈风格。例如，活泼偶像适合轻快流行舞；街头服饰角色适合嘻哈与震感舞；神秘角色适合流畅的仪式感动作；穿长礼服的优雅角色适合精巧舞步和优美手臂动作。这些仅为指导，选择最适合上传角色的风格。

设计十六个不同且富有表现力的姿势，构成连贯舞蹈序列。根据实际服装和鞋子调整动作：长裙或高跟鞋采用受控舞步，服装允许时可使用更有活力的脚步。通过姿态、表情和手势保留角色个性。

动作顺序
建立清晰进程：
1：有角色特色的开场姿势。
2–4：通过起始舞步和手势建立节奏。
5–8：通过不同手臂形状和重心变化展开舞蹈。
9–12：加入受控转身、方向变化或适合的亮点动作。
13–15：回到接近正面的方向，为结尾蓄势。
16：符合角色个性的、令人印象深刻的结束姿势。

相邻姿势应能通过自然运动连接。变化手臂高度、轮廓、脚步位置、躯干朝向和重心分配。以正面和四分之三视角为主，适当加入侧面或背面转身。避免重复姿势或将同一站姿稍作变化十六次。

构图
每格完整展示角色，包括发梢、举起的手、配饰、飘动衣料和鞋子，四周保留舒适边距。所有格子的角色比例与相机高度一致。任何身体部位或服装都不得越过单元格边界。

使用纯白或轻微米白背景，搭配柔和且不抢眼的地面阴影，使角色和舞蹈易于辨认。线条与明暗处理精致，并与上传参考图一致。

质量约束
保持合理的身体结构与可信的平衡。转身时面部、服装与配饰位置一致。头发和衣料随动作自然运动，不遮挡姿势。保留服装原有覆盖范围。避免不切实际的动作、意外走光、额外肢体、重复角色、裁切的末端、服装变化或新增道具。

只包含 1–16 的格子编号。不出现标题、说明文字、标签、对话气泡、装饰场景或水印。

最终输出：一张完整、清晰的 4×4 参考图，包含为上传角色量身设计的十六个原创舞姿。
```

*将 `@[Image 1]` 替换为上传的角色参考图。*

<a id="p06-portrait-reference-to-multi-view-sheet"></a>

### 📌 2.5. 人像参考 → 多视图设定图 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p06-character-scenes/portrait-views-result.png" width="400" height="225" alt="包含三个全身视图与两个面部视图的人像设定图">](assets/p06-character-scenes/portrait-views-result.png)

#### 👇 工作流

`人像参考图 → 多视图设定图 (left 2/3: front / side / back full body; right 1/3: front / side face)`

#### 🔖 完整提示词

```text
使用上传的人像作为同一个人的身份参考。制作一张横幅角色参考图，恰好包含此人的五个视图。保留面部身份、年龄、性别呈现、肤色、发型、身体比例以及可见服装细节。如果人像没有展示完整服装或身体，使用 [outfit and footwear description]，并保守推断不可见的比例；所有视图保持这些选择一致。

将画布分为两个主要区域。左侧三分之二横向排列三个等大、等间距的全身视图：左边为正面，中间为面向左方的标准侧面，右边为背面。每个视图都从头顶完整展示到鞋底，头顶与地面高度对齐，比例一致，采用放松的自然站姿并留少量安全边距。在符合身体结构的情况下，双臂与躯干稍微分开，使轮廓与服装清晰可辨。

右侧三分之一上下排列两张等大面部特写：上方为正脸，下方为面向左方的标准侧脸。完整展示头部、头发、可见耳朵和上颈部，不裁切。特写比例一致，表情自然中性，面部细节清楚。这些特写与三个全身视图为同一人，不是额外角色。

使用纯色 [background color] 影棚背景、柔和均匀的照明，以及与上传参考图一致的视觉风格。透视自然，比例不变形。用干净留白区分视图，不画边框。五个视图中的服装颜色、发型和身份保持一致。不出现文字、标签、网格线、额外视图、额外人物、虚构配饰、裁切的脚部或重复肢体；不得用四分之三视角代替所要求的正面、侧面和背面。
```

*将 `[outfit and footwear description]` 替换为参考图未展示部分的服装与鞋履说明，将 `[background color]` 替换为背景颜色。*

<a id="p02-collectible-figure-packaging"></a>

### 📌 2.6. 收藏玩偶包装 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p02-collectible-figure-packaging/collectible-packaging-result.png" width="400" height="400" alt="粉色吸塑包装中的收藏角色">](assets/p02-collectible-figure-packaging/collectible-packaging-result.png)

#### 👇 工作流

`文字／可选角色参考图 → 包装图片`

#### 🔖 完整提示词

```text
制作一张原创收藏角色玩具的影棚产品照片。玩具名为“[toy name]”，装在透明吸塑包装中，背板为 [backing color] 纸板。

如果上传了人物或角色图片，以其作为身份参考；否则根据 [character description] 设计角色。保留参考图的辨识特征、身体结构、比例和颜色。采用 [outfit or surface details]，除非明确要求更改，否则保留参考外观。

在玩偶右侧的独立隔间里恰好放置三件配件：[accessory 1]、[accessory 2] 和 [accessory 3]。完整展示玩偶。顶部用大而清晰的字呈现准确标题“[toy name]”。采用真实的模塑塑料、受控反射和柔和影棚阴影。不添加其他文字或无关品牌标志。竖幅构图。
```

*生成前，请替换 `[toy name]`, `[backing color]`, `[character description]`, `[outfit or surface details]`, `[accessory 1]`, `[accessory 2]`, `[accessory 3]`为自定义内容后再生成。*

<a id="p01-personalized-sticker-pack"></a>

### 📌 2.7. 个性化贴纸包 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p01-personalized-sticker-pack/character-stickers-result.png" width="400" height="400" alt="蓝色背景上的四张猫咪表情贴纸">](assets/p01-personalized-sticker-pack/character-stickers-result.png)

#### 👇 工作流

`角色参考图 → 贴纸图片`

#### 🔖 完整提示词

```text
以上传的人物或角色作为身份参考，制作干净的 2×2 贴纸图，包含四种表情：[expression 1]、[expression 2]、[expression 3] 和 [expression 4]。

保留主体的身份、身体结构、比例、颜色、服装（如有）以及独特特征。根据主体的身体结构调整每种表情和姿势，不改变物种或性别呈现。每个单元格都展示完整主体，使用粗白色贴纸描边，贴纸之间留出充足间隔。背景为纯色 [background color]，使轮廓便于分离。不添加说明文字、字母、装饰物，不让内容跨格重叠。
```

*生成前，请替换 `[expression 1]`, `[expression 2]`, `[expression 3]`, `[expression 4]`, `[background color]`为自定义内容后再生成。*

<a id="-products--branding"></a>

## 🛍️ 产品与品牌视觉

<a id="p31-virtual-outfit-replacement"></a>

### 📌 3.1. 虚拟换装 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcj1ud/gpt_image_25_prompt_guide_2026_23_9_official_edit/) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p31-virtual-outfit-replacement/source-example-01.jpg" width="400" height="313" alt="虚拟换装——来源示例">](assets/p31-virtual-outfit-replacement/source-example-01.jpg)

#### 👇 工作流

`人物参考图 + 服装参考图 → 换装图片`

#### 🔖 完整提示词

```text
以图片 1 作为人物参考，其余上传图片作为服装参考。只编辑图片 1 中人物穿着的服装。保留其准确身份、面容、年龄、肤色、身体比例、性别呈现、表情、发型和姿势。将参考服装自然适配其体型和姿势，表现真实布料行为。匹配原始照明、阴影和色温。背景、相机角度、构图和画质保持不变。不添加配饰、文字、标志或水印。
```

<a id="p27-cereal-box-nutrition-panel"></a>

### 📌 3.2. 麦片盒营养成分表 (收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p27-cereal-box-nutrition-panel/source-example-01.webp" width="400" height="226" alt="麦片盒营养成分表——来源示例">](assets/p27-cereal-box-nutrition-panel/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
麦片盒背面，包含完整营养成分表，每个数值都清晰可读
```

<a id="p22-wine-label-with-tasting-notes"></a>

### 📌 3.3. 附品鉴笔记的葡萄酒标签 (收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p22-wine-label-with-tasting-notes/source-example-01.webp" width="400" height="225" alt="附品鉴笔记的葡萄酒标签——来源示例">](assets/p22-wine-label-with-tasting-notes/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
葡萄酒瓶标签，包含酒庄名称、年份和四行品鉴笔记
```

<a id="p21-vintage-toy-airplane-packaging"></a>

### 📌 3.4. 复古玩具飞机包装 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

[<img src="assets/p21-vintage-toy-airplane-packaging/source-example-01.webp" width="267" height="400" alt="复古玩具飞机包装——来源示例">](assets/p21-vintage-toy-airplane-packaging/source-example-01.webp)

[<img src="assets/p21-vintage-toy-airplane-packaging/source-example-02.webp" width="267" height="400" alt="复古玩具飞机包装——来源示例">](assets/p21-vintage-toy-airplane-packaging/source-example-02.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
制作一款收藏级复古螺旋桨玩具飞机，具有圆润机翼、前置旋转螺旋桨、略有掉漆的边缘和经典童年玩具比例，作为怀旧节日收藏品装入吸塑包装。

概念：灵感来自孩子们寒假时玩的简单玩具飞机，唤起温暖、想象力和童年惊喜。

风格：高级玩具摄影，真实塑料和涂漆金属纹理，影棚照明，浅景深，清晰标签印刷和高端零售展示。

约束：
仅原创设计。
无商标。
无水印。
无标志。
包装仅包含以下原样文字：“Christmas Memories Edition”。
```

<a id="p16-minimal-bakery-logo"></a>

### 📌 3.5. 极简面包店标志 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
为名为 Field & Flour 的本地面包店设计一个原创、不侵权的标志。
标志应温暖、简洁、经典。使用干净的矢量感形状、鲜明轮廓和均衡负空间。
优先简洁而非细节，保证大小尺寸下都清晰可辨。扁平设计，精简笔画，除非必要，否则不使用渐变。
背景完全透明。交付单个居中标志，四周留充足空间，透明边缘干净，不出现实色底板、场景、棋盘格或水印。
```

<a id="p15-streetwear-campaign-with-exact-typography"></a>

### 📌 3.6. 准确文字的街头服饰广告 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p15-streetwear-campaign-with-exact-typography/source-example-01.webp" width="267" height="400" alt="准确文字的街头服饰广告——来源示例">](assets/p15-streetwear-campaign-with-exact-typography/source-example-01.webp)

#### 👇 工作流

`人物参考图 → 街头服饰广告`

#### 🔖 完整提示词

```text
使用上传的人物参考图定义画面中的朋友，每张参考图对应一个独立人物。保留每个人可辨识的面容、年龄、肤色、性别呈现、发型和身体比例；绝不融合或交换身份。如果只上传一张人像，就只展示该人物。

为“[brand name]”制作精致的街头服饰广告。参考人物穿着 [streetwear styling]，自然地在 [setting] 相聚。采用现代构图、有活力的色彩方向、自然姿势和高级时装摄影。准确且清晰地呈现一次“[tagline]”。不显示方括号。不添加其他人物、额外文字、水印或无关标志。
```

*生成前，请替换 `[brand name]`, `[setting]`, `[streetwear styling]`, `[tagline]`为自定义内容后再生成。*

<a id="p08-glass-material-remix"></a>

### 📌 3.7. 玻璃材质重塑 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p08-glass-material-remix/seeapi-glass-result.png" width="400" height="400" alt="保留原有颜色、转化为半透明玻璃的 SeeAPI 标志">](assets/p08-glass-material-remix/seeapi-glass-result.png)

#### 👇 工作流

`物体参考图 → 玻璃材质图片`

#### 🔖 完整提示词

```text
将上传图片中的主要物体转化为半透明玻璃，同时保留其整体轮廓、比例、朝向、颜色和标志性结构细节。

将其放在浅色石材表面上，搭配暖灰色影棚背景。表现可信的玻璃厚度、细微内部反射、曲面区域柔化的折射，以及贴合台面的接触阴影。使用左侧大型柔光源，后方添加微弱轮廓光。完整展示物体。不添加额外部件、标签、文字或无关道具。
```

<a id="p04-product-photo-to-campaign-visual"></a>

### 📌 3.8. 产品照片 → 广告视觉 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p04-product-campaign/product-campaign-result.png" width="400" height="400" alt="浅色石材展台上的产品广告图">](assets/p04-product-campaign/product-campaign-result.png)

#### 👇 工作流

`产品参考图 → 广告图片`

#### 🔖 完整提示词

```text
编辑上传的产品照片。保留产品轮廓、比例、朝向、包装、标志位置和所有可见标签文字。

将周围场景替换为 [background color and material] 影棚背景和 [platform material] 展台。添加来自左上方的柔和窗光，以及产品下方自然的接触阴影。产品位于画面右半部，左半部保持整洁，留待之后添加文案。

不添加文字、额外产品、装饰食材或新标签。不裁切产品的任何部分。横幅构图。
```

*生成前，请替换 `[background color and material]`, `[platform material]`为自定义内容后再生成。*

<a id="-posters--artistic-styles"></a>

## 🎨 海报与艺术风格

<a id="p40-desert-motorcycle-editorial-poster"></a>

### 📌 4.1. 沙漠摩托车杂志海报 (作者：[Comfy-Org](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_sunburst_t2i.json)) · [来源平台： GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_sunburst_t2i.json) · 参考图改编：SeeAPI
#### 👀 预览

[<img src="assets/p40-desert-motorcycle-editorial-poster/source-example-01.webp" width="400" height="400" alt="沙漠摩托车杂志海报——来源示例">](assets/p40-desert-motorcycle-editorial-poster/source-example-01.webp)

#### 👇 工作流

`人像参考图 → 杂志海报`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人穿着 [motorcycle outfit] 的 1:1 正方形杂志时装海报。人物双臂交叉，站在未来沙漠拉力赛场景中的大型黑色装甲摩托车旁，站姿自然放松、符合身体结构。锈蚀机械塔、发光能量门、飘扬沙尘、电影感纵深、真实材质和细腻胶片颗粒。

用超大号焦橙色工业无衬线字体呈现准确标题“[poster title]”，文字穿插于场景元素前后，但不遮挡面容。添加不含字母的抽象图形点缀。使用不对称布局，配色为焦橙、黑色、沙漠米色和电光蓝。标题是唯一文字：不添加说明文字、额外标签或水印。
```

*生成前，请替换 `[motorcycle outfit]`, `[poster title]`为自定义内容后再生成。*

<a id="p39-neon-motorsport-poster"></a>

### 📌 4.2. 霓虹赛车海报 (作者：[Comfy-Org](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_flare_t2i.json)) · [来源平台： GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_flare_t2i.json)
#### 👀 预览

[<img src="assets/p39-neon-motorsport-poster/source-example-01.webp" width="400" height="400" alt="霓虹赛车海报——来源示例">](assets/p39-neon-motorsport-poster/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
1:1 正方形海报，极近距离、高对比拍摄赛车前鼻、空气动力学翼片与轮辋，在鲜红运动模糊和明亮橙光中冲破黑暗。“GPT IMAGE 2.5”以明亮霓虹橙色直接投影在车身上，与前翼和轮辋重叠。强烈红黑配色、电影感低调照明、锐利反射、戏剧性低机位、浅景深和高速赛车美学。不出现侧栏、额外 UI 面板、技术符号、条形码，除“GPT IMAGE 2.5”外不出现其他文字。
```

<a id="p34-woodland-clearing"></a>

### 📌 4.3. 林间空地 (作者：[@mark_k](https://x.com/mark_k/status/2097411028510179759)) · [来源平台： X](https://x.com/mark_k/status/2097411028510179759)
#### 👀 预览

[<img src="assets/p34-woodland-clearing/source-example-01.jpg" width="400" height="300" alt="林间空地——来源示例">](assets/p34-woodland-clearing/source-example-01.jpg)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
林间空地照片，有大量绿色枝叶，高度细致
```

<a id="p32-dog-compositing-into-a-street-scene"></a>

### 📌 4.4. 将狗合成至街道场景 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcj1ud/gpt_image_25_prompt_guide_2026_23_9_official_edit/)
#### 👀 预览

[<img src="assets/p32-dog-compositing-into-a-street-scene/source-example-01.jpg" width="400" height="313" alt="将狗合成至街道场景——来源示例">](assets/p32-dog-compositing-into-a-street-scene/source-example-01.jpg)

#### 👇 工作流

`街道场景 + 狗的参考图 → 合成图片`

#### 🔖 完整提示词

```text
将第二张图中的狗放入图片 1 的场景中，紧挨着那位女性，使用相同的照明风格、构图与背景。其他一切保持不变。
```

<a id="p28-fashion-movements-across-four-decades"></a>

### 📌 4.5. 四个年代的时尚潮流 (作者：[@Gdgtify](https://x.com/Gdgtify/status/2098228786156196084)) · [来源平台： X](https://x.com/Gdgtify/status/2098228786156196084)
#### 👀 预览

[<img src="assets/p28-fashion-movements-across-four-decades/source-example-01.jpg" width="400" height="225" alt="四个年代的时尚潮流——来源示例">](assets/p28-fashion-movements-across-four-decades/source-example-01.jpg)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
2×2 网格，分别展示四个不同年代的时尚潮流，16:9 class EditorialPoster:     def __init__(self, topic):         self.topic = topic         self.resolution = self.resolve_auto_fields(topic)              def resolve_auto_fields(self, topic):         # Module 2: Copy & Facts         self.title = generate_title(topic, max_words=5)         self.tagline = generate_tagline(topic, min_words=3, max_words=8)         self.labels = extract_key_points(topic, count=6-12, relationship="components") # principles/stages/types                  # Module 3: The Surreal Character Engine         self.mechanism = infer_verb(topic) # e.g., "filtering", "branching", "accumulating"         self.base_form = select_organism(self.mechanism) # human, animal, or object         # CRITICAL: Transformation must be structural, not just accessories         self.transformation = invent_structural_alteration(self.base_form, self.mechanism)         self.pose = select_pose(topic, attitude="intriguing_uncanny")                  # Module 5: Geometry & Palette         self.geometry = select_geometric_family(topic) # rays, arcs, ribbons, grids         self.palette = derive_accent_colors(topic, count=2-6, mood="flat_matte_weathered")      def verify_character_logic(self):         # The "Thumbnail & Concept" Check         assert is_structural(self.transformation), "Module 3: Must be anatomy/proportion, not accessories."         assert fits_sentence(self.transformation, self.mechanism), "Module 3: Logic check failed."         assert visible_at_thumbnail(self.transformation), "Module 3: Must read at small scale."         assert not is_generic_cute_scary(self.pose), "Module 3: Avoid default emotional tropes."      def render(self):         self.verify_character_logic()                  # Module 1 & 6: Style Kernel         canvas = Canvas(aspect="1:1", bg="warm_ivory", texture="subtle_analog_grain")                  # Hero: Grayscale, sculptural shading, stippling/halftone         hero = render_grayscale_sculptural(self.base_form, self.transformation, self.pose,                                             shading="fine_stippling", texture="tactile_print")                  # Module 4: Adaptive Layout         layout = adaptive_composition(             hero=hero,              title=self.title, # Oversized, black, condensed, uppercase             labels=self.labels, # Compact, high contrast             geometry=self.geometry, # Connects hero to info             palette=self.palette # Flat, matte accents         )                  return canvas.compose(layout, typography="extreme_contrast_hierarchy")  EditorialPoster($ TOPIC).render()
```

<a id="p25-three-panel-dialogue-comic"></a>

### 📌 4.6. 三格对话漫画 (收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p25-three-panel-dialogue-comic/source-example-01.webp" width="400" height="226" alt="三格对话漫画——来源示例">](assets/p25-three-panel-dialogue-comic/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
三格条漫，手写对话气泡，墨线与平涂色彩
```

<a id="p09-paper-folk-story"></a>

### 📌 4.7. 剪纸民间故事 (作者：@azed_ai) · [来源平台： X](https://x.com/azed_ai/status/2096191635348705726)
#### 👀 预览

[<img src="assets/p09-paper-folk-story/azed-ai-paper-folk-story.webp" width="400" height="267" alt="来自 azed_ai 原帖的提灯剪纸角色">](https://x.com/azed_ai/status/2096191635348705726)

#### 👇 工作流

`文字 → 剪纸角色图片`

#### 🔖 完整提示词

```text
剪纸动画风格的 [subject] 正在 [simple action]，全身角色，多层纸片形状，手工纸纹理，可见裁切边缘，层间柔和阴影，平涂的彩色纸张色调，略带不完美的手作细节，极简纸张拼贴场景，迷人的民间故事美学，轻柔的定格动画感，诗意的儿童绘本氛围，干净的白色背景
```

*将 `[subject]` 替换为人物或角色，将 `[simple action]` 替换为希望表现的动作。*

<a id="p07-paper-cut-storybook-scene"></a>

### 📌 4.8. 剪纸绘本场景 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p07-paper-cut-storybook/paper-cut-character-result.png" width="400" height="400" alt="温馨房间中的多层剪纸猫">](assets/p07-paper-cut-storybook/paper-cut-character-result.png)

#### 👇 工作流

`文字／可选角色参考图 → 剪纸图片`

#### 🔖 完整提示词

```text
制作完全由多层剪纸构成的绘本场景，地点为 [environment]。由 [character description] 定义的角色在 [focal object] 附近做出 [anatomy-appropriate action]。如果上传了角色参考图，在将外观转化为剪纸时保留其身份、身体结构、比例、颜色和独特特征。

表现可见纸纤维、利落的裁切边缘、轻微弯折的纸片，以及层与层之间的真实阴影。配色限定为 [color palette]。像从正面观看的浅景深舞台布景一样构图，前景、中景和背景明确。不出现文字、亮面塑料或照片般写实的表面纹理。正方形构图。
```

*生成前，请替换 `[environment]`, `[character description]`, `[anatomy-appropriate action]`, `[focal object]`, `[color palette]`为自定义内容后再生成。*

<a id="p05-editorial-poster-with-exact-copy"></a>

### 📌 4.9. 准确文案的杂志风海报 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p05-editorial-poster/summer-poster-result.png" width="225" height="400" alt="以冲浪板为主体的蓝色夏日海报">](assets/p05-editorial-poster/summer-poster-result.png)

#### 👇 工作流

`文字 → 海报图片`

#### 🔖 完整提示词

```text
在 [paper color and texture] 上设计一张竖幅展览海报。画面中间三分之一区域放置大型雕塑感 [central object]，颜色为 [object color]，从左上方照明并形成柔和阴影。

只包含以下准确文字，使用填写的值，不显示方括号：
顶部，大号粗体无衬线字：“[main title]”
雕塑下方，较小字号：“[subtitle]”
底部，小字号：“[date or supporting line]”

保留宽裕页边距，采用严格左对齐的文字网格，清晰区分标题、雕塑和辅助文案。每个词都完整可见。不添加其他文字、标志、边框或水印。
```

*生成前，请替换 `[paper color and texture]`, `[central object]`, `[object color]`, `[main title]`, `[subtitle]`, `[date or supporting line]`为自定义内容后再生成。*

<a id="p03-miniature-world-in-an-everyday-object"></a>

### 📌 4.10. 日常物品中的微缩世界 (作者：SeeAPI)
#### 👀 预览

[<img src="assets/p03-miniature-world/miniature-world-result.png" width="400" height="400" alt="树皮容器内的微缩林间村庄">](assets/p03-miniature-world/miniature-world-result.png)

#### 👇 工作流

`文字 → 微缩场景图片`

#### 🔖 完整提示词

```text
在打开的 [everyday container] 内构建微缩 [world or scene theme]，容器放在真实的 [supporting surface] 上。包含 [main structures]、[landscape details] 和 [focal feature]，所有内容在物理上都位于容器内部。容器内壁构成背景，材质符合其真实结构。

从斜上方四分之三视角展示整个容器。通过真实接缝、边缘、五金配件，以及旁边实际尺寸的 [scale reference object]，明确微缩比例关系。采用 [lighting mood]、真实微缩材质和浅景深，同时保持场景清晰可读。不出现悬浮建筑或文字。横幅构图。
```

*生成前，请替换 `[world or scene theme]`, `[everyday container]`, `[supporting surface]`, `[main structures]`, `[landscape details]`, `[focal feature]`, `[scale reference object]`, `[lighting mood]`为自定义内容后再生成。*

<a id="-home--interior-design"></a>

## 🏡 家居与室内设计

<a id="p42-bedroom-redesign-from-your-photo"></a>

### 📌 5.1. 照片 → 卧室改造 (作者：SeeAPI)
#### 👀 预览

| 原图 | 效果图 |
|---|---|
| [<img src="assets/p42-bedroom-redesign/reference.png" width="300" height="300" alt="照片 → 卧室改造——原图">](assets/p42-bedroom-redesign/reference.png) | [<img src="assets/p42-bedroom-redesign/result.png" width="300" height="300" alt="照片 → 卧室改造——效果图">](assets/p42-bedroom-redesign/result.png) |

#### 👇 工作流

`卧室照片 → 改造后的卧室`

#### 🔖 完整提示词

```text
将这间普通卧室重新设计为更时尚、协调、具有专业装饰感的室内空间，同时保留原有房间结构、布局、窗户位置、床的位置和整体透视。通过改进家具风格、层次丰富的床品、精致配色、有品位的挂画、柔软织物、细腻装饰点缀以及更好的视觉平衡，将其转化为温暖、现代、令人向往的卧室。使用真实材质、整洁收纳、优雅照明和舒适的生活气息，营造更成熟的室内设计感。效果真实可信，像真实家居改造照片，而不是 CGI。保持自然比例和真实照明，让房间明显升级，同时仍能清楚看出它基于原图。
```

<a id="-infographics--practical-design"></a>

## 📊 信息图与实用设计

<a id="p30-spanish-infographic-translation"></a>

### 📌 6.1. 信息图翻译为西班牙语 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcj1ud/gpt_image_25_prompt_guide_2026_23_9_official_edit/)
#### 👀 预览

[<img src="assets/p30-spanish-infographic-translation/source-example-01.jpg" width="400" height="313" alt="信息图翻译为西班牙语——来源示例">](assets/p30-spanish-infographic-translation/source-example-01.jpg)

#### 👇 工作流

`信息图参考 → 西班牙语信息图`

#### 🔖 完整提示词

```text
将信息图中的文字翻译为西班牙语。不改变图像的任何其他部分。
```

<a id="p26-ornate-award-certificate"></a>

### 📌 6.2. 华丽获奖证书 (收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p26-ornate-award-certificate/source-example-01.webp" width="400" height="226" alt="华丽获奖证书——来源示例">](assets/p26-ornate-award-certificate/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
获奖证书，华丽边框，以书法字体书写姓名和日期
```

<a id="p24-boarding-pass-layout"></a>

### 📌 6.3. 登机牌版式 (收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p24-boarding-pass-layout/source-example-01.webp" width="400" height="225" alt="登机牌版式——来源示例">](assets/p24-boarding-pass-layout/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
登机牌效果图，乘客、登机口、座位和时间在干净的网格中清晰可读
```

<a id="p23-national-park-trail-map"></a>

### 📌 6.4. 国家公园步道地图 (收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)
#### 👀 预览

[<img src="assets/p23-national-park-trail-map/source-example-01.webp" width="400" height="225" alt="国家公园步道地图——来源示例">](assets/p23-national-park-trail-map/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
国家公园步道地图海报，六条路线标注名称与距离
```

<a id="p20-cellular-respiration-classroom-diagram"></a>

### 📌 6.5. 课堂细胞呼吸示意图 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

[<img src="assets/p20-cellular-respiration-classroom-diagram/source-example-01.webp" width="400" height="267" alt="课堂细胞呼吸示意图——来源示例">](assets/p20-cellular-respiration-classroom-diagram/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
为高中生制作一张简单生物学示意图，标题为“Cellular Respiration at a Glance”。

展示葡萄糖如何在细胞内转化为能量，包含糖酵解、克雷布斯循环和电子传递链。用箭头连接各步骤，并标注主要分子：glucose、pyruvate、ATP、NADH、FADH2、CO2、O2 和 H2O。整体像干净的课堂讲义或幻灯片，白色背景、简单图标、清晰标签和易读文字。

避免过小文字、额外装饰或任何使图示难以理解的内容。
```

<a id="p19-farmers-market-mobile-app-mockup"></a>

### 📌 6.6. 农夫市集手机应用效果图 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

[<img src="assets/p19-farmers-market-mobile-app-mockup/source-example-01.webp" width="267" height="400" alt="农夫市集手机应用效果图——来源示例">](assets/p19-farmers-market-mobile-app-mockup/source-example-01.webp)

[<img src="assets/p19-farmers-market-mobile-app-mockup/source-example-02.webp" width="267" height="400" alt="农夫市集手机应用效果图——来源示例">](assets/p19-farmers-market-mobile-app-mockup/source-example-02.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
为本地农夫市集制作真实的手机应用 UI 效果图。
展示今日市集，包括简单页眉、附小照片和类别的简短摊贩列表、小型“Today’s specials”区域，以及地点和营业时间等基本信息。
设计实用、易用。白色背景，柔和自然的点缀色，清晰字体，装饰精简。
整体应像一个真正为小型本地市集设计的精美应用。
将 UI 效果图放在 iPhone 机框中。
```

<a id="p14-automatic-coffee-machine-infographic"></a>

### 📌 6.7. 全自动咖啡机信息图 (作者待确认) · [来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)
#### 👀 预览

[<img src="assets/p14-automatic-coffee-machine-infographic/source-example-01.webp" width="267" height="400" alt="全自动咖啡机信息图——来源示例">](assets/p14-automatic-coffee-machine-infographic/source-example-01.webp)

[<img src="assets/p14-automatic-coffee-machine-infographic/source-example-02.webp" width="267" height="400" alt="全自动咖啡机信息图——来源示例">](assets/p14-automatic-coffee-machine-infographic/source-example-02.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
制作一张详细信息图，解释 Jura 这类全自动咖啡机的工作原理与流程。
从豆仓到研磨、称重、水箱、锅炉等环节。
希望从技术和视觉层面理解整个流程。
```

<a id="-5-creative-cases"></a>

<a id="-gif--video-workflows"></a>

## 🎬 GIF 与视频工作流

<a id="c01-pixel-art-character-gif-by-seeapi"></a>

### 📌 7.1. 像素角色 GIF (作者：SeeAPI)

#### 👀 预览

[<img src="assets/01-pixel-art-gif/elephant-roll.gif" width="291" height="278" alt="像素角色 GIF——GIF 结果">](assets/01-pixel-art-gif/elephant-roll.gif)

**大象精灵图**

[<img src="assets/01-pixel-art-gif/elephant-sprite-sheet.png" width="400" height="400" alt="大象精灵图">](assets/01-pixel-art-gif/elephant-sprite-sheet.png)

#### 👇 工作流

`文字／可选角色参考图 → 精灵图 → GIF`

#### 🔖 完整提示词

**步骤 1 — 文字 → 精灵图**

```text
只制作一张二维像素角色精灵图：正方形 4×4 网格，16 个等大单元格，每格一个全身角色，每帧呈现 64×64 风格像素。如有上传角色则使用该角色，否则根据用户附加的角色创意设计。全程保持物种、身体结构、比例、服装、颜色和标志性道具一致。用户文字定义角色，不改变精灵图格式。展示 16 个不同且递进的姿势：1–4 准备／预备；5–8 迈步、伸手或相应动作；9–12 富有表现力的标志性动作；13–16 恢复并趋近第 1 帧。选择符合身体结构、轮廓明显变化的动作，不重复待机姿势，不制作四视图转身。保持大小、机位、朝向和单元格对齐一致，避免裁切。清晰 16 位像素风，深色描边，每种颜色使用 2–3 个平涂色阶，纯白背景。不使用抗锯齿、渐变、地面阴影、文字、网格线、额外肢体或虚构道具。第 16 帧自然衔接第 1 帧。角色创意：[a gray elephant is rolling on the ground]
```

*生成前，请替换 `[a gray elephant is rolling on the ground]`为自定义内容后再生成。*

**步骤 2 — 精灵图 → GIF**

```text
将所附 4×4 角色精灵图制作成动画 GIF。使用 Python 和 Pillow 按从左到右、从上到下的顺序提取全部 16 格。检查姿势，从预备动作、标志性动作到恢复，选择连贯的动作序列；只有在能改善连续性时才调整帧顺序。

去掉每个角色周围多余的空白，不裁切耳朵、肢体、尾巴或道具。各帧保留角色原有大小和比例。使用同一画布，将每帧角色居中；画布大小以最大姿势为准，并保留少量一致的安全边距。不单独缩放某帧来填满画布。

保留像素画风和白色背景。使用共享调色板，不抖色、不平滑、不虚构中间姿势。调整帧时长，使动作清楚，最后一帧自然回到第一帧。导出无限循环 GIF。逐帧检查裁切与对齐，检查循环衔接，提供 GIF 和可复现的 Python 脚本。报告使用的帧顺序、尺寸和时长，并指出需要修改精灵图才能弥补的动作缺口。
```

<a id="c02-clay-stop-motion-fishing-for-a-star-by-seeapi-inspired-by-charlie-guo"></a>

### 📌 7.2. 陶土定格动画：钓起一颗星星 (作者：SeeAPI；灵感来源：[Charlie Guo](https://x.com/charlierguo/status/2097399137142772071))

#### 👀 预览

[<img src="assets/02-clay-stop-motion/penguin-star-stop-motion.gif" width="313" height="313" alt="陶土定格动画：钓起一颗星星——GIF 结果">](assets/02-clay-stop-motion/penguin-star-stop-motion.gif)

**企鹅钓星星帧表**

[<img src="assets/02-clay-stop-motion/penguin-star-contact-sheet.png" width="400" height="400" alt="企鹅钓星星帧表">](assets/02-clay-stop-motion/penguin-star-contact-sheet.png)

#### 👇 工作流

`参考图片／文字 → 陶土风格图 → 帧表 → GIF`

#### 🔖 完整提示词

**步骤 1A — 参考图 → 陶土风格图**

```text
将上传图片编辑为手工陶土定格动画静帧。保留角色身份、物种、身体结构、比例、服装、颜色、标志性道具、姿势和场景构图。将表面转化为有触感的塑形陶土，带细微指纹、略不规整的雕塑边缘、柔和微缩布景阴影，并在合适处表现织物纹理。保持为一个连贯场景，所有重要元素可见。不新增角色、道具、文字，不制作帧表或动画分帧。这是一张陶土风格起始图。
```

**步骤 1B — 文字 → 陶土风格图（无参考图时）**

```text
制作一张手工陶土定格动画起始图：[character description] 位于 [setting]，准备进行 [simple action]。姿势符合身体结构，只使用 [required props]。安排角色和道具，使目标动作能在固定机位的单镜头中清楚发生。陶土材质富有触感，带细微指纹和略不规则的雕塑形状，微缩布景照明柔和，构图清晰整洁。所有主体和道具完整位于画面内，并留出运动空间。不出现文字、蒙太奇、帧表或多个画格。
```

*将 `[character description]`（角色说明）、`[setting]`（场景）、`[simple action]`（动作）和 `[required props]`（所需道具）替换为自定义内容。步骤 1A 与 1B 任选其一。*

**步骤 2 — 陶土风格图 → 帧表**

```text
使用上传的陶土风格图片作为严格的身份、材质、布景、照明和机位参考。制作一张正方形 4×4 帧表，恰好包含十六个等大的正方形帧，按阅读顺序排列，无格间空隙、网格线、标签或文字。

表现动作：[simple action]。第 1–4 帧建立起始姿势与预备动作；第 5–8 帧开始主要运动；第 9–12 帧展示动作高潮；第 13–16 帧恢复并趋向起始姿势，形成循环。采用不同、递进且符合身体结构的姿势，轮廓发生变化。参考角色的物种、比例、服装、颜色和道具保持不变。不虚构额外肢体、角色或道具。

每格保留同一固定机位、一致主体大小、固定布景位置、背景、照明与场景几何。运动元素位于每格内部，并留少量安全边距。保持物理接触和对道具的连续握持。保留陶土触感、手作表面瑕疵和轻微阶跃式定格感。第 16 帧应自然衔接第 1 帧。不出现相机运动、运动模糊、重复待机帧或变化的场景。
```

*将 `[simple action]` 替换为希望制作成动画的动作。*

**步骤 3 — 帧表 → GIF**

```text
使用 Python 和 Pillow 将所附 4×4 定格动画帧表制作成循环 GIF。按从左到右、从上到下的顺序分割成 16 个等大帧。如果图片尺寸不能被四整除，对单元格边界取整，并保持统一裁切尺寸，必要时最多裁去一个边缘像素。

每帧保留完整微缩场景。使用同一裁切区域，保持原图比例。不按企鹅轮廓裁切，也不将其单独重新居中：冰洞、地平线和地面必须固定。不添加相机运动、插值姿势、光流或交叉淡化。

使用共享的 256 色调色板，不抖色。以每帧 140 毫秒为起点，在揭示动作时稍作停留，并在循环边界短暂停顿。除非姿势明显需要调整，否则保留原顺序。导出无限循环 GIF，并提供可复现脚本，包含准确帧顺序与时长。

检查角色、钓竿、鱼线、星星、冰洞和首尾衔接。如实报告可见漂移或缺失动作；若源帧需修正，说明应重新生成哪些内容，不将 GIF 描述为完美无缝。
```

<a id="c04-character-to-storyboard-to-film-by-seeapi-inspired-by-elcine"></a>

### 📌 7.3. 角色设定 → 分镜 → 短片 (作者：SeeAPI；灵感来源：[el.cine](https://x.com/EHuanglu/status/2097519538632024103))

#### 👀 预览

**Inez 角色参考**

[<img src="assets/04-storyboard-video/inez-reference.png" width="400" height="267" alt="Inez 角色参考">](assets/04-storyboard-video/inez-reference.png)

**灯塔分镜**

[<img src="assets/04-storyboard-video/lighthouse-storyboard.png" width="400" height="225" alt="灯塔分镜">](assets/04-storyboard-video/lighthouse-storyboard.png)

**镜头 01**

[<img src="assets/04-storyboard-video/shot-01.png" width="400" height="225" alt="镜头 01">](assets/04-storyboard-video/shot-01.png)

**镜头 02**

[<img src="assets/04-storyboard-video/shot-02.png" width="400" height="225" alt="镜头 02">](assets/04-storyboard-video/shot-02.png)

**镜头 03**

[<img src="assets/04-storyboard-video/shot-03.png" width="400" height="225" alt="镜头 03">](assets/04-storyboard-video/shot-03.png)

**镜头 04**

[<img src="assets/04-storyboard-video/shot-04.png" width="400" height="225" alt="镜头 04">](assets/04-storyboard-video/shot-04.png)

#### 👇 工作流

`文字 → 角色参考图 → 分镜 → 单镜头图片 → 视频片段 → 剪辑成片`

#### 🔖 完整提示词

**步骤 1 — 文字 → 角色参考图**

```text
生成一张干净的横幅 3:2 单角色全身身份参考图。原创主角 INEZ，约 60 岁的灯塔机械师，温暖棕褐肤色，短银灰卷发，圆形玳瑁眼镜，面容慈祥且有岁月纹理。穿海军蓝羊毛工装外套、赭黄色针织衫、炭灰长裤和做旧深棕工作靴。双手空着且可见，双臂放松，头部和靴子完整位于画面内，四周留充足边距。她以自然的四分之三站姿站在简单暖灰影棚背景前。不出现其他角色或道具，不拼贴，不增加视图，不添加文字。
视觉风格：有触感的微缩定格电影设计，毡化羊毛服装，细腻雕塑感且有表现力的面容，电影感的柔和阴天海岸光，低饱和海军蓝与赭黄配色，身体结构可信。主体明确为年长成年女性，不做时尚美颜修饰。
```

**步骤 2 — 角色参考图 → 分镜**

```text
使用上传的 INEZ 全身像作为严格身份和视觉风格参考。保留其年长面容、短银灰卷发、圆形玳瑁眼镜、海军蓝羊毛外套、赭黄针织衫、炭灰长裤和棕色工作靴。制作一张 16:9 分镜图，严格分成 2×2 网格，含四个等大的 16:9 电影画格，无格间空隙、画格标签、编号、说明文字、文字或边框。按从左到右、从上到下阅读。这是四镜头叙事分镜，不是连续动画帧。

原创故事：在小型海岸灯塔工作室中，Inez 让一只带固定上弦钥匙、掌心大小的黄铜机械海鸟恢复运转，然后让它从已打开的窗户飞走。采用有触感的微缩定格电影风格、毡化羊毛服装、雕塑面容、轻微做旧黄铜以及阴天海岸日光。同一张木工作台位于房间右侧的一扇已打开的拱窗下，窗外是冷色海面。只有一只黄铜机械鸟，有两只铰接翅膀，左侧腹部连接一把小上弦钥匙。没有散落工具或无关物体。

第 1 格，建立场景的中远景：Inez 在工作台左侧，低头看着台面中右侧静止的机械鸟。两只翅膀折叠。她双手放在鸟两侧的台面上，不碰钥匙。右侧可见打开的窗户。这是修理前的最初一刻。
第 2 格，从工作台同一侧拍摄的特写：Inez 一只手轻扶鸟身，另一只手握住鸟左侧腹部连接的小钥匙，准备转动。两翼仍折叠。展示足够的赭黄色袖子和海军蓝袖口，使服装连续。黄铜鸟的几何结构必须与第 1 格一致，不能换成另一只鸟。钥匙保持连接。
第 3 格，中景：Inez 微笑地看着台面上的同一只鸟，两只铰接翅膀部分展开，头抬起。她双手已收回，与鸟翼明显分开。鸟尚未起飞。右侧仍是同一窗户，照明和服装一致。
第 4 格，朝向开窗的中远景：Inez 留在左侧，摊开的支撑手掌靠近窗台。同一只黄铜鸟停在右侧窗台，翅膀准备向开阔海面起飞，仍有物理支撑。保留唯一窗户及其已打开状态。Inez 的四分之三侧脸可见，流露安静的自豪。这是放飞镜头的起点，鸟尚未飞走。

保持因果连续、唯一且可辨识的主角、单只鸟、稳定服装、稳定房间方位、合理手部，并在特写与全景之间建立明确视觉联系。不出现魔法光束、发光眼睛、额外角色、飞行工具、丢失眼镜、不可读文字、重复鸟、网格覆盖或写实真人替换。
```

**步骤 3 — 单镜头图片 → 视频片段 → 剪辑成片**

```text
制作一支 12 秒、16:9 的微缩定格风格短片，名为 The Last Flight，含四个镜头，运动具有清楚的手作阶跃感。不要将片名显示为文字。C04-R01 是 Inez 的身份参考。C04-B01 仅用于分镜规划，不是直接驱动动画的帧表。C04-K01 至 C04-K04 是各镜头的起始画面参考。视频中绝不展示网格或多个画格。

连续性：Inez 始终是同一位年长女性，银色卷发、圆形玳瑁眼镜、海军蓝外套和赭黄色针织衫。只有一只掌心大小的黄铜机械海鸟，有两只铰接翅膀和一把固定在左侧腹部的上弦钥匙。木工作台位于房间右侧唯一、已打开的拱窗下。阴天海光保持不变。鸟从静止到上弦、活动、起飞，绝不复制或改变物种。

镜头 1，0–3 秒，以 C04-K01 开始：固定中远景。Inez 注意到台面上翅膀折叠、静止的黄铜鸟，略微靠近，伸手触向其连接的钥匙。右侧始终可见打开的窗户。在伸手动作上切到匹配的特写。
镜头 2，3–6 秒，以 C04-K02 开始：固定特写。一只手稳住鸟，另一只手将连接的钥匙缓慢转动半圈。钥匙保持连接，手指保持接触。一声轻微机械咔哒后，鸟头稍微抬起。在这一初始运动上切到更宽的反应镜头。
镜头 3，6–9 秒，以 C04-K03 开始：中景。鸟展开双翼，向右走两小步，Inez 在旁边摊开手掌。她微笑，眼镜和服装保持不变。顺着鸟的移动方向切到开窗镜头；到窗台的短距离移动通过有意剪辑省略，而不是镜头内瞬移。
镜头 4，9–12 秒，以 C04-K04 开始：中远景。鸟从窗台用双脚蹬起，机械翅膀轻拍两次，从已打开的窗户向画面右侧飞出。Inez 收回支撑手掌，目光跟随它。以她安静的微笑和开阔海面结束。鸟远去时仍为同一只小型黄铜物体。不重置，不循环。

无需移动相机。优先保证动作易读，不额外增加切镜。可选声音：低沉海风、上弦咔哒声、两次轻柔金属振翅声；无对白、字幕或口型同步。不支持音频生成时导出无声片段。

负面提示词：可见分镜网格、拼贴动画、额外鸟、脱落钥匙、鸟设计变化、服装变形、眼镜缺失、额外手指、手与翅膀融合、关闭的窗户、穿玻璃飞行、无原因的房间变化、长镜头内瞬移、写实皮肤、快速蒙太奇、交叉淡化、文字或标志。

输入受限时：分别生成四段 3 秒片段，每段只使用对应的 C04-K 图片作为首帧，并使用上述对应镜头段落，加上连续性与负面约束。每段裁为 3 秒，以直接切镜连接。如果生成器要求更长的最短时长，先生成该时长，再选取连贯的 3 秒；12 秒是剪辑目标，不代表某个具体模型支持的设置。
```

<a id="c05-distant-observer-a-robot-in-the-rain-by-seeapi-inspired-by-pablo-prompt"></a>

### 📌 7.4. 远景旁观：雨中的机器人 (作者：SeeAPI；灵感来源：[Pablo Prompt](https://x.com/pabloprompt/status/2097382752622436744))

#### 👀 预览

**雨街初稿**

[<img src="assets/05-distant-observer/rainy-street-draft.png" width="225" height="400" alt="雨街初稿">](assets/05-distant-observer/rainy-street-draft.png)

**雨街首帧**

[<img src="assets/05-distant-observer/rainy-street-opening.png" width="225" height="400" alt="雨街首帧">](assets/05-distant-observer/rainy-street-opening.png)

**机器人参考**

[<img src="assets/05-distant-observer/robot-reference.png" width="267" height="400" alt="机器人参考">](assets/05-distant-observer/robot-reference.png)

#### 👇 工作流

`文字 → 角色参考图 → 场景图 → 修正场景图 → 视频`

#### 🔖 完整提示词

**步骤 1 — 文字 → 角色参考图**

```text
制作一张 2:3 竖幅原创友善老式街道维护机器人的全身身份参考照片。它是实体搭建的电影道具，约 2 米高，躯干为敦实、风化的锈红色钢铁，头部为米白色圆角长方体，恰好两只小型圆形深色玻璃眼睛，没有嘴。两条粗壮关节手臂，每只手恰好三根圆钝手指，两条短而结实的腿和宽阔深色橡胶脚。外壳有掉漆和轻微雨痕，不是军事装甲。左胯绑着一个小橄榄绿帆布袋。没有文字、徽章、标志、屏幕、武器或人脸。
机器人以放松的正面四分之三姿态直立，站在纯中灰色影棚地面与无缝背景前。空着的双手、完整头部与双脚清楚可见，四周留充足边距。手中没有道具，身份参考图中不放雨伞。只有一个机器人，无拼贴、转身网格或其他主体。
采用写实实体特效电影摄影，有触感的金属和帆布，柔和阴天照明，气质温暖克制。设计独特、谦逊、比例圆润的市政助手，不使用已有系列中的机器人。
```

**步骤 2 — 角色参考图 → 场景图**

```text
使用上传的机器人照片作为严格身份参考 C05-R01：保留敦实的锈红钢铁身体、米白圆角长方体头部、两只圆形深色眼睛、无嘴、两条手臂、每手三根圆钝手指、两条腿、橡胶脚以及左胯唯一橄榄绿袋子。

制作一张写实 9:16 竖幅首帧，呈现偶然从远处观察虚构场景的感觉。相机躲在窄小雨街对面、无人咖啡馆的门口内，距机器人约 25 米。使用适度长焦透视、压缩的纵深和自然镜头柔化，不拍广角近景。深色失焦门框只占画面左侧 8%，柔软虚化的台沿横跨底部 5%；两者都不遮挡机器人或花盆。画面无人物或摄影器材。

远处人行道上，机器人位于中线略右，站在唯一一把打开的芥末黄色雨伞下。机器人从头到脚仅占整幅高度的 24–28%，在更大的城市环境中明显较小。它低头看向右侧紧邻地面上的一个陶土花盆，里面只有一株矮绿植和一朵小白花。花盆足够近，使机器人只需降低并稍微移动雨伞就能为其遮雨。靠近花盆的手在胸口高度握着伞杆，另一只手垂在身侧。雨伞当前位于机器人上方，还没有位于花盆上方。伞杆与伞面连续连接，由一只手握持。

安静的老电车站沿街建筑，机器人身后是关闭的青绿色卷帘门、潮湿浅色灰泥墙、路缘，湿路面占据画面中下部较大区域，细雨与宽阔水洼反光。没有可读店名、道路文字、标志、车辆、行人或其他植物。环境与湿润空旷空间占主导。阴天下午日光，除锈红机器人、黄伞和陶土花盆外，颜色低调。雨伞和花盆分开且完整可见。自然、略不完美的旁观者取景，无监控叠层、时间戳、电影黑边或夸张散景。这是远处看到的普通街道，一件意外的小小善举即将发生，而非英雄肖像。
```

**步骤 3 — 场景图 → 修正场景图**

```text
只对这张远景雨街画面进行一处局部修正。将现有陶土花盆及其唯一白花沿同一人行道平面向右移动，使整个花盆和花朵明显位于黄色伞面最右边缘之外，正在淋雨。花盆中心位于约画面宽度 89% 处，保留其当前大小以及与人行道的接触。在伞面右边缘与花朵之间留出可见、正在下雨的水平空隙。彻底移除旧位置的花盆；仍然只能有一个花盆和一朵花。

其他所有内容保持不变：准确机位距离与构图、小型机器人大小及姿势、两只眼睛与橄榄绿袋子、雨伞角度及连接的伞杆、握持、卷帘门、建筑、湿路面、雨、长凳、前景门框和虚化台沿、光线、纹理及图像尺寸。不移动或放大机器人，不改变雨伞，不添加人物，不裁切图片。这是机器人把雨伞移到花盆上方之前的画面。
```

**步骤 4 — 修正场景图 → 视频**

```text
以 C05-K01 为准确首帧，制作 8 秒写实 9:16 远景旁观视频，单个连续镜头。只有工具支持额外参考槽位时，才可将 C05-R01 作为可选机器人身份参考。若只允许一张图片，则使用 C05-K01。保留其街道布局、湿路面、青绿卷帘门、前景门框边缘、机器人大小、雨伞与花盆。

相机留在街对面的门内，保持约 25 米距离。匹配 C05-K01 中机器人站立时的准确小比例（提供的示例中约占画面高度 18%），不要为了满足数值目标放大它。弯腰时允许投影高度自然减小，不放大机器人或移动相机补偿。观众应感觉偶然注意到远处人行道上的小事。只允许极轻微、低幅度手持漂移，低于画面宽度 1%；不变焦、不推进、不朝主体跟踪、不拍特写、不切镜、不做戏剧性焦点转换。前景遮挡只在边缘，不能覆盖动作。

0–2 秒：锈红机器人停在打开的黄伞下，米白头部向下倾斜，看向旁边唯一的陶土花盆和白花。雨持续落下，花茎轻微点动。保持恰好两只眼睛、无嘴、一个橄榄绿胯包以及相同身体比例。
2–6 秒：机器人屈膝弯腰，用已经握住伞杆的手降低并移动仍然打开的伞，使其靠近花盆。伞面与伞杆作为一个刚性连接整体运动。持续握持，不换手。空闲手搭在自己的大腿上。双脚始终落在人行道上。结束时伞面明显位于花盆正上方，而机器人头肩的大部分在伞外淋雨。雨伞不缩小、不折叠、不脱落，也不碰到花朵。
6–8 秒：机器人稳稳地将伞撑在花盆上方，安静看着花。伞周仍可见雨，路面水洼持续出现涟漪。从同一远景视角结束这一小小关怀举动。机器人不察觉或看向镜头。不回到起始姿势，不循环。

写实实体特效角色，关节运动可信，金属潮湿，日光柔和，动作克制。可选音频：从相机遮雨位置录到的雨声，远处极轻微机械运动声；不出现近距离对白、音乐提示或戏剧性音效。不支持音频时导出无声。

负面提示词：主体变大、自动变焦、面部特写、横穿街道移动、相机环绕、切镜、与镜头对视、向观众挥手、额外机器人或人物、额外雨伞、第二个花盆、雨伞变大小、伞杆脱落、换手握持、额外手指、悬浮脚、变成阳光、干燥路面、雨消失、额外文字、水印、时间戳、监控界面。
```

<a id="c06-frosted-glass-poster-to-360-orbit-by-seeapi"></a>

### 📌 7.5. 磨砂玻璃海报 → 360° 环绕视频 (作者：SeeAPI)

#### 👀 预览

[<img src="assets/featured/glass-orbit.gif" width="320" height="320" alt="已提供的环绕视频预览">](assets/06-360-orbit/frosted-glass-mug-orbit.mp4)

**磨砂玻璃杯海报**

[<img src="assets/06-360-orbit/frosted-glass-mug-poster.png" width="400" height="400" alt="磨砂玻璃杯海报">](assets/06-360-orbit/frosted-glass-mug-poster.png)

#### 👇 工作流

`文字 → 海报图 → 360° 环绕视频`

#### 🔖 完整提示词

**步骤 1 — 文字 → 海报图**

```text
极简未来主义展览海报，背景为极浅冷黄色（#e7ff48）。

海报中心是一只完整的流体 3D 融球造型马克杯，以磨砂玻璃呈现，带细腻颗粒噪点。
流体渐变从浅黄色（#E7FF48）过渡至珍珠白（#FFFFFF），形成丝滑的玻璃质感。

高位柔光箱投下长而柔和的彩色阴影和细微光晕。

流体与文字重叠：被磨砂玻璃遮挡的字母呈现轻柔高斯模糊。
- 主标题为浅黄色“SeeAPI”标志，居中且被流体部分遮挡。覆盖的字母透过磨砂玻璃略微模糊。
- 副标题位于主标题下方，使用纯黑、粗体全大写现代无衬线字体，内容为“Images, videos and models API”。副标题也被流体部分覆盖，覆盖区域模糊，其余区域保持清晰。

整体布局干净，留白充足，构图均衡，对焦清晰，HDR 高动态范围。
```

**步骤 2 — 海报图 → 360° 环绕视频**

```text
制作一支 6 秒、1:1 正方形产品短片，只有一个连续镜头，以 C06-R01 为准确开场构图。核心是相机围绕同一只雕塑感磨砂玻璃杯完整环绕 360 度，展示流体轮廓、中空杯沿、唯一连接的把手以及变化的透射光。保留极简未来主义展览海报美感，以及冷黄色 #E7FF48 至珍珠白配色。

只保留一只杯子，比例、不对称融球轮廓、玻璃厚度、开放杯口和一个连续把手均与源图一致。杯子在世界空间静止，相对表面的高度不变；位置、形状和朝向不产生动画。对未见表面作保守推断，延续同一杯体，不添加装饰或第二个把手。

镜头 1：从所给四分之三视角开始，从上方看相机顺时针完成一次不中断的圆周环绕：正面四分之三、侧面、背面、另一侧，再回到准确起点。六秒内完成完整 360 度。保持环绕半径、高度、焦距和对准杯心的方向固定，无相机滚转。迅速开始移动，以平滑且接近匀速的节奏展示各面，仅在回到起始角度后短暂稳定。整只杯子和把手始终在画面内，大小稳定。唯一把手随透视自然被杯身遮挡并重新出现，不分裂或跳到另一侧。

高位柔光箱与无缝冷黄色影棚环境在世界空间固定。相机移动时，高光、可见玻璃厚度、折射及柔和投影连贯变化。保留细腻磨砂颗粒作为表面纹理，不变成闪烁噪点。玻璃始终磨砂且半透明，光晕克制，无融化或不透明度转变。

文字是渲染杯子后方、与屏幕对齐的展览图形，不是印在杯身上的字，也不是相机绕行的实体招牌。源图的布局、字体、间距、颜色及准确可见文字保持固定：“SeeAPI”和“IMAGES, VIDEOS AND MODELS API”。杯子投影变化时，仅透过磨砂玻璃看到的区域产生轻微折射和柔化；未遮挡文字保持锐利。字母不得随杯子旋转、镜像、改写或移动。最终角度恢复原来的重叠与模糊模式。

以源图相机角度、比例、照明和构图结束，相机无残余运动。如支持尾帧槽位，也使用 C06-R01，同时保留完整环绕指令。结果应展示真实立体物体的视点变化，不旋转平面海报、不让杯子在转台自转，也不用变焦或分层二维漂移替代。不切镜。可输出无声视频。
```

**步骤 3 — 360° 环绕视频：负面提示词**

```text
不完整环绕、完成一圈前相机反向、固定机位转台自转、平面海报旋转、简单变焦或二维视差、用跳切隐藏背面、额外杯子、额外把手、把手脱落、杯口封闭、杯沿形状变化、玻璃融化、产品大小变化、相机滚转、倾斜漂移、透明度突变、随机闪光粒子、不稳定颗粒、移动或拼错文字、镜像文字、文字印在杯子上、额外说明文字、水印、背景变色、结尾视角不匹配。
```

**步骤 4 — 备选：海报图 → 已提供的视频**

```text
制作单个连续镜头的图生视频。以上传图片作为首帧。保留原主体身份、外观、比例、服装或表面细节、视觉风格、照明与环境。

镜头 1 — 相机主导环绕：从源图准确视角出发，让相机沿平滑圆弧向右移动，围绕主要主体约 120 度。主体是环绕的固定空间中心。保持相机与主体距离、相机高度和焦距近乎不变，并轻轻向内转向，使主体始终稳定取景。立即开始移动，维持明确而流畅的运动，并平滑减速至最终视角。

让相机位置变化清楚可见：逐渐展示主体新的侧面，透视变化连贯，遮挡和显露自然。附近前景元素在画面中的移动快于远处背景。背景结构固定在相同物理位置，表观位置和角度随视点移动自然变化。保持地平线稳定、场景几何一致。

主体留在同一位置，在环境中的整体朝向保持原样。人物或动物可有细微呼吸、自然眨眼、轻微表情变化和小幅放松姿态调整。允许短暂、有限地看一眼经过的镜头，随后头部和躯干稳定，不持续追踪镜头。让相机自然显露四分之三或侧面视图。无生命物体保持静止。

保留与地板、座椅、栏杆或其他支撑表面的接触。环境运动轻微，并由原场景合理驱动。保持世界空间光照一致，高光和反射随视角变化自然响应。

主要可见运动来自相机绕主体行进。在新显露的角度结束，同一主体和环境保持完整。运动平滑且有电影感，空间纵深清晰，主体动画克制，无切镜。
```

<a id="-sources-reuse--maintenance"></a>

## 📝 来源、使用与维护

原创提示词标注为 **作者：SeeAPI**。有灵感来源的案例还会注明原作者并链接原帖。提示词作者、灵感来源和示例图片来源分别记录。

使用条款见 [来源与权利说明](docs/sources-and-rights.md)。本仓库目前没有覆盖所有提示词和素材的统一许可；C06 有单独的署名使用许可。署名不代表来源作品的所有权转移。

SeeAPI 维护本仓库，并将持续补充提示词、实测示例与制作说明。**现阶段暂不开放外部投稿。**

维护资料： [仓库结构](docs/repository-structure.md) · [案例模板](templates/case.md) · [更新清单](docs/maintenance.md) · [更新记录](CHANGELOG.md).

<a id="-acknowledgments"></a>

## 🙏 致谢

- [YouMind — Awesome Seedance 2.0 Prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts): 为本仓库的内容组织和精选示例提供灵感。
