# GPT Image 2.5 精选提示词库 🎨

[English](README.md) | [简体中文](README_zh.md)

**由 SeeAPI 精选的创意图像提示词与工作流。**

探索 GPT Image 2.5 在角色贴纸、产品视觉、微缩世界、GIF 素材和定格动画场景中的创意玩法。复制提示词，替换为自己的内容，尝试新的创作方向。

本仓库将持续更新提示词示例、生成图片和实用复现说明。

**5 个创意工作流 · 73 条独立提示词 · 更新于 2026 年 9 月 18 日**

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

**仓库信息**

- [🖼️ 精选示例](#-featured-examples)
- [🧭 选择模型](#-choose-your-model)
- [📝 来源、使用与维护](#-sources-reuse--maintenance)
- [🙏 致谢](#-acknowledgments)

**提示词分类**

- [📷 人像与摄影](#-portraits--photography)
- [🧸 角色与趣味创作](#-characters--playful-creations)
- [🛍️ 产品与品牌视觉](#-products--branding)
- [🎨 海报与艺术风格](#-posters--artistic-styles)
- [🏡 家居与室内设计](#-home--interior-design)
- [📊 信息图与实用设计](#-infographics--practical-design)
- [🎬 GIF 与视频工作流](#-gif--video-workflows)

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

<a id="p54-cinematic-modern-mafia-boss-portrait"></a>

### 📌 1.1. 电影感现代黑帮首领肖像

#### 👀 预览

[<img src="assets/p54-cinematic-modern-mafia-boss-portrait/source-example-01.jpg" width="400" height="400" alt="电影感现代黑帮首领肖像——来源示例">](assets/p54-cinematic-modern-mafia-boss-portrait/source-example-01.jpg)

#### 👇 工作流

`人脸参考图 → 电影感肖像`

#### 🔖 完整提示词

```text
创建一张我的超写实电影感肖像（使用上传的人脸），将我塑造成一位现代黑帮首领。我坐在一辆豪华黑色汽车里，身穿黑色西装，戴着有色飞行员太阳镜，抽着一根粗雪茄。神情冷峻无畏。背景：阴郁天空 + 虚化城市/街道，营造黑色电影氛围。冷色调，高对比度。面部与烟雾细节锐利。风格：8K、电影海报品质、浅景深、1:1。
```

<sub>(by [@john_my07](https://x.com/john_my07/status/2099745210196738366)) · [来源平台： X](https://x.com/john_my07/status/2099745210196738366)</sub>

<a id="p49-soft-hijab-beauty-portrait"></a>

### 📌 1.2. 柔光头巾美妆人像

#### 👀 预览

[<img src="assets/p49-soft-hijab-beauty-portrait/source-example-01.jpg" width="225" height="400" alt="柔光头巾美妆人像——来源示例">](assets/p49-soft-hijab-beauty-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 美妆人像`

#### 🔖 完整提示词

```text
一位年轻东亚女性的面部特写肖像。她拥有白皙、光滑的瓷感肌肤，肤色柔和均匀。她的眼睛大而呈杏仁形，为浅灰蓝色；睫毛纤长、深色且根根分明，搭配细致眼线。眉毛纤细而修整整齐。妆容自然水润，双颊带有柔和粉色腮红，略显丰润的玫瑰粉色双唇带有光泽。她直视镜头，神情平静、温柔，略显含蓄。

她佩戴一条轻薄半透明的头巾，采用柔和的米色、灰褐色与香槟色调，并带有金色和棕色的精致佩斯利与花卉图案。面料宽松地垂坠并分层包裹头部与肩部，完全遮住头发。头巾左侧靠近太阳穴的位置有一枚小巧的金色球形别针或胸针。面料质地柔软、略微透光，具有自然温和的褶皱与纹理。

背景为室内空间，浅色墙面上方左侧可见一个木质搁板，放有几只瓶子（其中一只有橙色瓶盖）。柔和的室内自然光为面部带来温暖、修饰性良好的光泽，不产生生硬阴影。

照片级写实、高细节美妆肖像、浅景深、背景柔焦、优雅而端庄的造型。
```

<sub>(by [@woleswoosh](https://x.com/woleswoosh/status/2099774470374502450)) · [来源平台： X](https://x.com/woleswoosh/status/2099774470374502450)</sub>

<a id="p47-y2k-queen-of-the-women-s-kingdom"></a>

### 📌 1.3. 千禧年女儿国国王

#### 👀 预览

[<img src="assets/p47-y2k-queen-of-the-women-s-kingdom/source-example-01.jpg" width="225" height="400" alt="千禧年女儿国国王——来源示例">](assets/p47-y2k-queen-of-the-women-s-kingdom/source-example-01.jpg)

#### 👇 工作流

`文字 → 千禧年风格人像`

#### 🔖 完整提示词

```text
千禧年非主流 × 早期数码感 × 反差萌 × 女儿国国王
```

<sub>(by [@DeepBlueX0](https://x.com/DeepBlueX0/status/2099303054797606998)) · [来源平台： X](https://x.com/DeepBlueX0/status/2099303054797606998) · 英文由 SeeAPI 翻译</sub>

<a id="p46-atmospheric-dressing-room-fashion-portrait"></a>

### 📌 1.4. 更衣室氛围时尚人像

#### 👀 预览

[<img src="assets/p46-atmospheric-dressing-room-fashion-portrait/source-example-01.jpg" width="300" height="400" alt="更衣室氛围时尚人像——来源示例">](assets/p46-atmospheric-dressing-room-fashion-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 时尚人像`

#### 🔖 完整提示词

```text
一张抓拍感、富有氛围的背面时尚人像：一位成年东亚女性停在半开的更衣室门口，画幅比例为 3:4 竖版。画面像朋友随手拍下的私密生活日记照片：略有不完美、柔和朦胧、低调时尚，带有含蓄情绪，但不显得摆拍或经过商业化精修。

女性位于画面中线偏左，背对镜头。相机从她身后近距离拍摄，机位约在腰部高度，取景从头顶到大腿中部。门框的一条边进入前景，将构图部分围合起来，营造观察转瞬即逝的私人时刻的感觉。画面略微不对称，右侧保留大量浅色负空间。

她的身体朝向衣柜内部，双肩放松。左手轻轻搭在移门边缘，手指自然弯曲。重心落在一条腿上，让体态形成柔和、不刻意的曲线。她从左肩上方回头，只有部分脸庞从散落发丝间显露。神情安静、略显疏离，目光柔和地直视镜头，嘴唇自然闭合。

她有精致的鹅蛋脸、柔和收窄的下颌线、深色杏眼、自然平直的眉毛、纤细的鼻子和柔和的玫瑰粉色嘴唇。妆容简淡而有生活感：轻薄自然的底妆、柔和的棕色眼线、根根分明的睫毛、淡淡的面颊色彩和轻透的缎光唇色。

深浓咖啡棕色的长发以松散、不规则的波浪自然垂落背部。发量自然，略显凌乱，包含压扁的部分、相互叠压的发束、细小飞发和独立发丝。几缕柔软发丝掠过脸颊，部分遮住一只眼睛。头发应显得柔软可触、随意打理，而不是发廊造型般完美。

她穿着一条精致的黑色真丝雪纺短裙，设计属于晚间时装而非内衣。裙子采用细肩带、柔和定型的合身上身、低露背设计及两条纤细的横向丝带，轻盈裙摆从腰间以松散的半透明层次垂落。不透明的黑色真丝内衬在外层雪纺之下提供完整遮盖，只有飘动的裙边和侧面层次透光。面料呈柔和哑光，带有细密织纹、自然褶皱、轻微动态和精细的手工缝线。

更衣室简洁，背景柔和虚化：带白色饰边的浅粉蓝色移门、细窄的拉丝金色把手、暖灰米色衣柜内部、几根纤细的横向挂杆，以及一个简洁白色抽屉柜的边缘。环境保持安静整洁，让深色人物和浅色建筑形状构成画面主体。

室外的冷色窗光与衣柜内部昏暗的暖色环境光混合。微弱的便携相机直闪轻轻提亮她的面部、肩部、手部及黑色雪纺边缘，同时让背景略微欠曝。混合光线形成奶油般柔和的肤色、浅淡的薰衣草灰阴影、柔化的黑色、高光中隐约的粉色暖意，以及向四角逐渐减弱的光线。

使用小型高端便携相机与等效 35mm 镜头拍摄，近距离手持视角，取景略微倾斜，浅景深，柔和的焦点衰减，轻微高光晕散，克制的直闪特征，少数发丝带有轻微运动模糊，并呈现细腻可见的颗粒。照片随性却观察细致，像从私人社交媒体动态中保存下来的安静夜间时尚随拍。

超写实摄影。真实的人体皮肤，具有可见毛孔、细软绒毛、自然色调变化、指关节与肩部的轻微泛红、细微皮肤挤压和真实的小瑕疵。头发逐根呈现，具有真实重力、不规则分束、飞发和柔和反光。真丝雪纺呈现真实织纹、层叠透明度、不透明内衬、自然重量、柔软折痕、尚在延续的动态和精细的边缘缝线。低对比度模拟胶片色彩、柔和的传感器颗粒、轻微闪光晕散、淡淡的镜头暗角，以及柔和粉蓝、暖灰、奶油象牙白和深柔黑。私密、轻松、梦幻、得体、自然不完美，并具有可信的摄影质感。
```

<sub>(by [@johnAGI168](https://x.com/johnAGI168/status/2099160929418031152)) · [来源平台： X](https://x.com/johnAGI168/status/2099160929418031152)</sub>

<a id="p45-natural-4k-photo-restoration"></a>

### 📌 1.5. 自然质感 4K 照片修复

#### 👀 预览

[<img src="assets/p45-natural-4k-photo-restoration/source-example-01.jpg" width="400" height="200" alt="自然质感 4K 照片修复——来源示例">](assets/p45-natural-4k-photo-restoration/source-example-01.jpg)

#### 👇 工作流

`照片参考图 → 修复照片`

#### 🔖 完整提示词

```text
将这张图片放大至 4K。保留每一处细节。使其呈现自然、未经修饰的原始质感。去除编辑痕迹和伪影。
```

<sub>(by [@ViralOps_](https://x.com/ViralOps_/status/2098774775934198214)) · [来源平台： X](https://x.com/ViralOps_/status/2098774775934198214)</sub>

<a id="p38-candid-mont-saint-michel-travel-portrait"></a>

### 📌 1.6. 圣米歇尔山旅行抓拍

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

<sub>(by [@saniaspeaks_](https://x.com/saniaspeaks_/status/2097532595814940683)) · [来源平台： X](https://x.com/saniaspeaks_/status/2097532595814940683) · 参考图改编：SeeAPI</sub>

<a id="p37-realistic-iphone-cafe-portrait"></a>

### 📌 1.7. 真实 iPhone 咖啡馆人像

#### 👀 预览

[<img src="assets/p37-realistic-iphone-cafe-portrait/source-example-01.jpg" width="300" height="400" alt="真实 iPhone 咖啡馆人像——来源示例">](assets/p37-realistic-iphone-cafe-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人在 [cafe setting] 的真实 iPhone 风格抓拍照片，穿着 [outfit]，正在 [simple action]。自然现场光，真实皮肤纹理，随意的手机取景，可信的手部与家具接触，克制的景深和日常色彩。不使用美颜滤镜面容，不改变体型，不添加前景人物、文字或水印。
```

<sub>(by [@blueemi99](https://x.com/blueemi99/status/2097602273085931662)) · [来源平台： X](https://x.com/blueemi99/status/2097602273085931662) · 参考图改编：SeeAPI</sub>

<a id="p36-dreamy-high-angle-qipao-portrait"></a>

### 📌 1.8. 梦幻俯拍旗袍人像

#### 👀 预览

[<img src="assets/p36-dreamy-high-angle-qipao-portrait/source-example-01.jpg" width="225" height="400" alt="梦幻俯拍旗袍人像——来源示例">](assets/p36-dreamy-high-angle-qipao-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人穿着 [qipao color and design] 的 9:16 竖幅时装人像，服装自然适配其真实比例。使用俯拍高机位、柔和光晕、梦幻背景虚化、精致的 [makeup style] 和轻柔优雅的姿势。面部保持可辨识且足够清晰。不强行拉高或瘦身，不重塑眼睛，不改变性别呈现。不添加文字或水印。
```

<sub>(by [@BubbleBrain](https://x.com/BubbleBrain/status/2097513469172129825)) · [来源平台： X](https://x.com/BubbleBrain/status/2097513469172129825) · 参考图改编：SeeAPI</sub>

<a id="p35-monochrome-cybernetic-horror-portrait"></a>

### 📌 1.9. 黑白赛博机械恐怖人像

#### 👀 预览

[<img src="assets/p35-monochrome-cybernetic-horror-portrait/source-example-01.jpg" width="400" height="400" alt="黑白赛博机械恐怖人像——来源示例">](assets/p35-monochrome-cybernetic-horror-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

将人像转化为黑白赛博机械恐怖摄影。通过面部结构和表情保持人物可辨识；在眼部周围使用开裂的瓷白色义体表面与内嵌金属细节，不替换头部或改变面部比例。头部周围布置黑色线缆和工业线圈附件，穿破旧深色布料服装。戏剧性低调照明，深黑背景，高对比黑白画面，具有触感的实体特效细节，85mm 人像镜头，浅景深。不添加其他人物，不放大眼睛，不换成无关面容，不添加文字。
```

<sub>(by [@meng_dagg695](https://x.com/meng_dagg695/status/2097558679956664521)) · [来源平台： X](https://x.com/meng_dagg695/status/2097558679956664521) · 参考图改编：SeeAPI</sub>

<a id="p29-caramel-suit-studio-portrait"></a>

### 📌 1.10. 焦糖色西装影棚人像

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

<sub>(by [@abs_uiux](https://x.com/abs_uiux/status/2098216202870964315)) · [来源平台： X](https://x.com/abs_uiux/status/2098216202870964315) · 参考图改编：SeeAPI</sub>

<a id="p17-1969-outdoor-festival-crowd"></a>

### 📌 1.11. 1969 年户外音乐节人群

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="p13-candid-sailor-portrait"></a>

### 📌 1.12. 渔船人物抓拍

#### 👀 预览

[<img src="assets/p13-candid-sailor-portrait/source-example-01.webp" width="267" height="400" alt="渔船人物抓拍——来源示例">](assets/p13-candid-sailor-portrait/source-example-01.webp)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人在小渔船上的写实抓拍照片，人物平静地整理渔网，一只狗坐在附近甲板上。人物穿着 [practical sailing outfit]。保留原有皮肤纹理与年龄，不额外添加皱纹或纹身。采用平视中景人像、50mm 镜头、柔和海岸日光、浅景深、35mm 胶片颗粒、自然色彩和磨损材质，营造未摆拍的日常氛围。不进行重度修图。
```

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/) · 参考图改编：SeeAPI</sub>

<a id="p12-cinematic-subway-motion-portrait"></a>

### 📌 1.13. 电影感地铁动感人像

#### 👀 预览

[<img src="assets/p12-cinematic-subway-motion-portrait/source-example-01.webp" width="224" height="400" alt="电影感地铁动感人像——来源示例">](assets/p12-cinematic-subway-motion-portrait/source-example-01.webp)

#### 👇 工作流

`人像参考图 → 风格化人像`

#### 🔖 完整提示词

```text
使用上传的人像作为主体人物的身份参考。保留其可辨识的面容、年龄、肤色、性别呈现、发型和身体比例。不要将其替换为通用模特，也不要强行改变其族裔、性别或体型。

制作此人静站在地铁站台上的电影感人像，一列银黄色列车在其身后驶过，形成水平方向运动模糊。面部清晰，表情平静。人物穿着 [outfit]，手持 [bouquet or prop]。保留原有发型，允许少量发丝在列车带动的气流中自然飘动。融合车站顶部冷光与温暖的皮肤高光，采用浅景深、真实皮肤纹理和细微胶片颗粒。
```

<sub>[来源平台： SeeAPI](https://www.aiimage.net/prompts/) · 参考图改编：SeeAPI</sub>

<a id="p10-1980s-retro-film-portrait"></a>

### 📌 1.14. 1980 年代复古胶片人像

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

<sub>(by [@Goodmanprotocol](https://x.com/Goodmanprotocol/status/2097954772586557873)) · [来源平台： X](https://x.com/Goodmanprotocol/status/2097954772586557873)</sub>

<a id="p57-candid-camera-roll-grid"></a>

### 📌 1.15. 随手拍相册九宫格

#### 👀 预览

[<img src="assets/p57-candid-camera-roll-grid/source-example-01.jpg" width="225" height="400" alt="随手拍相册九宫格——来源示例">](assets/p57-candid-camera-roll-grid/source-example-01.jpg)

[<img src="assets/p57-candid-camera-roll-grid/source-example-02.jpg" width="225" height="400" alt="随手拍相册九宫格——来源示例">](assets/p57-candid-camera-roll-grid/source-example-02.jpg)

[<img src="assets/p57-candid-camera-roll-grid/source-example-03.jpg" width="225" height="400" alt="随手拍相册九宫格——来源示例">](assets/p57-candid-camera-roll-grid/source-example-03.jpg)

#### 👇 工作流

`主题 → 3×3 随手拍相册九宫格`

#### 🔖 完整提示词

```text
围绕 [XXX] 主题，生成一组手机拍摄的业余、失败感抓拍照片，呈现私人相册气质，排成 3×3 九宫格，9:16。
```

<sub>(by [@MrLarus](https://x.com/MrLarus/status/2099871480112652453)) · [来源平台： X](https://x.com/MrLarus/status/2099871480112652453)</sub>

<a id="p59-concert-stage-bunny-costume"></a>

### 📌 1.16. 兔耳舞台服演唱会抓拍

#### 👀 预览

[<img src="assets/p59-concert-stage-bunny-costume/source-example-01.jpg" width="225" height="400" alt="兔耳舞台服演唱会抓拍——来源示例">](assets/p59-concert-stage-bunny-costume/source-example-01.jpg)

#### 👇 工作流

`文字 → 电影感演唱会舞台人像`

#### 🔖 完整提示词

```text
一张在舞台现场拍摄的电影感变形宽银幕静态照片：一位东亚表演者身穿精致的戏剧舞台服，在充满活力的现场场馆中央起舞。以动态中景主角构图呈现，摄影机位于视线高度，采用居中的竖版画幅，捕捉她灿烂的笑容与富有感染力的舞台魅力，呈现 M4 演唱会表演质感。

表演者有温暖的栗棕色长发，柔和的侧分刘海勾勒明亮的面庞，发丝垂落背后。白皙肌肤在舞台灯光下散发健康光泽，保留细微的自然毛孔纹理、轻微的次表面散射，以及锁骨与肩膀上的淡淡演出汗光。她戴着高挑华丽的兔耳戏剧头饰，材质为带纹理的绿松石色与祖母绿色提花面料，搭配水蓝色缎面领饰和镶有水晶胸针的蝴蝶结。服装是一件耀眼的高级定制舞台紧身胸衣连体服：浓郁的蓝绿色、海沫绿色与祖母绿色斑驳水彩纹样，点缀闪烁的金属亮片；精细的银色水晶珠饰与水钻滚边勾勒心形领口及胸衣结构，臀部两侧系着精巧的薄荷色缎带蝴蝶结。腿部穿着半透明菱形花纹演出连裤袜。她正处于舞蹈动作中，双臂轻轻向外舒展；深色杏眼闪着喜悦的光，直视镜头，露出明亮而动人的笑容。

环境是令人兴奋的现场演唱会场馆及夜店舞台，充满戏剧氛围：上方有灯光桁架、蜂巢状 LED 灯阵，水平霓虹激光束穿过背景中浓密的紫色和洋红色舞台烟雾。远处隐约可见多彩霓虹场馆标牌与舞台结构，柔和地发光，并融入奶油般的氛围虚化，为中央舞台营造丰富的纵深与空间沉浸感。

照明遵循真实演唱会灯光的物理效果：正面明亮、干净的白色与青色追光塑造她的面庞、闪耀的服装水晶及绿松石色面料，带来明亮的镜面高光与闪烁；背后的鲜艳洋红、霓虹紫和紫外线舞台染色灯，在她的肩膀与发丝边缘投下生动发亮的轮廓光。悬浮在空气中的体积烟雾捕捉舞台激光，形成可见的彩色光柱，让表演者自然融入脉动的现场舞台气氛。

以高宽容度数字电影画质拍摄，使用大光圈 50mm 变形宽银幕定焦镜头、T2.0 光圈，并以轻度柔光滤镜柔化鲜艳的霓虹高光；保持 M4 演唱会表演质感。真实的演唱会调色：深紫色阴影、饱和霓虹轮廓光，正面追光下的自然肤色保持干净。带有轻微的摄影师动态跟拍能量，舞动的指尖有细微自然运动模糊；整个画面覆盖精细的戏剧感 35mm 胶片颗粒。真实电影摄影机拍下的摄影画面，真实变形宽银幕镜头、真实亮片锦缎面料、真实水钻珠饰、真实人物表演者、真实舞台桁架与演唱会烟雾；不要 CGI、渲染感、过于干净的数字质感、塑料表面、AI 式过度平滑、磨皮、泛光、显得人工的光晕辉光或油亮高光。
```

<sub>(by [@johnAGI168](https://x.com/johnAGI168/status/2100090276576407848)) · [来源平台： X](https://x.com/johnAGI168/status/2100090276576407848)</sub>

<a id="p60-intimate-hallway-pov-portrait"></a>

### 📌 1.17. 玄关整理衣领的亲密视角人像

#### 👀 预览

[<img src="assets/p60-intimate-hallway-pov-portrait/source-example-01.jpg" width="225" height="400" alt="玄关整理衣领的亲密视角人像——来源示例">](assets/p60-intimate-hallway-pov-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 玄关亲密视角人像`

#### 🔖 完整提示词

```text
风格方向： 出门前亲密整理情绪
场景方向： 玄关 / 全身镜旁
服装方向： 雾粉色修身短袖家居裙或约会裙
气质标签： 温柔、轻熟、亲近、认真、甜
身形方向： 丰腴自然曲线
线条强调： 强
镜头方向： 女生站在镜头前很近的位置，身体偏向镜头，双手抬到镜头前方，像正在帮男友整理衣领或拉平衣服，整理完后抬眼看向镜头
画幅比例： 9:16
互动重点： 镜头直接承担“男友身体位置”，会产生非常明显的恋爱 POV；近距离也更容易自然呈现肩颈、胸腰轮廓。
```

<sub>(by [@liyue_ai](https://x.com/liyue_ai/status/2100152524884058399)) · [来源平台： X](https://x.com/liyue_ai/status/2100152524884058399) · 英文由 SeeAPI 翻译</sub>

<a id="p61-mirror-sculpture-street-portrait"></a>

### 📌 1.18. 镜面雕塑旁的都市街拍

#### 👀 预览

[<img src="assets/p61-mirror-sculpture-street-portrait/source-example-01.jpg" width="225" height="400" alt="镜面雕塑旁的都市街拍——来源示例">](assets/p61-mirror-sculpture-street-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 镜面雕塑旁的日间街拍人像`

#### 🔖 完整提示词

```text
摄影风格：日间清亮高光CCD生活照风
写真方向：都市艺术时尚生活照
场景方向：现代公共艺术广场 / 大型不锈钢镜面雕塑 / 浅灰地面 / 极简开放空间
服装方向：青柚绿色修身Polo短上衣 + 奶油白低腰修身短裙
气质标签：清冷、俏皮、时尚、明亮、有设计感
五官方向：高级元气淡颜
身形方向：轻盈纤细
线条强调：强
镜头方向：半身到大腿
姿态动作：站在镜面雕塑边，一只手轻触金属表面，身体轻微侧身看向镜面中的自己
光线氛围：晴天明亮自然光 + 镜面金属形成清晰中性反射补光
滤镜效果：高亮清晰绿白CCD色彩 + 清楚高光 + 稳定黑位 + 轻颗粒 + 极轻锐度
画幅比例：9:16
补充要求：镜面雕塑只能作为几何背景，不出现复杂畸变人像；人物胸腰轮廓清楚，整体要像城市随手拍而不是艺术棚拍
```

<sub>(by [@liyue_ai](https://x.com/liyue_ai/status/2100123514745536819)) · [来源平台： X](https://x.com/liyue_ai/status/2100123514745536819) · 英文由 SeeAPI 翻译</sub>

<a id="p63-golden-hour-beach-selfie"></a>

### 📌 1.19. 黄金时段海滩自拍

#### 👀 预览

[<img src="assets/p63-golden-hour-beach-selfie/source-example-01.jpg" width="225" height="400" alt="黄金时段海滩自拍——来源示例">](assets/p63-golden-hour-beach-selfie/source-example-01.jpg)

#### 👇 工作流

`文字 → 黄金时段海滩自拍`

#### 🔖 完整提示词

```text
一位长发黑发的东亚美女在海边自拍，穿着黑色高开叉连体泳衣，金色硬币吊坠项链，夕阳黄金时段，海浪拍打礁石，暖色侧光，真实摄影质感，皮肤细腻，微微侧身看镜头
```

<sub>(by [@shitunote](https://x.com/shitunote/status/2099846900031852562)) · [来源平台： X](https://x.com/shitunote/status/2099846900031852562) · 英文由 SeeAPI 翻译</sub>

<a id="p64-lavender-bedroom-portrait"></a>

### 📌 1.20. 薰衣草色卧室人像

#### 👀 预览

[<img src="assets/p64-lavender-bedroom-portrait/source-example-01.jpg" width="225" height="400" alt="薰衣草色卧室人像——来源示例">](assets/p64-lavender-bedroom-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 薰衣草色卧室人像`

#### 🔖 完整提示词

```text
超写实、IMAX 级、Netflix 风格的电影感人像，9:16 竖版。以上传图片作为主要身份参考，准确保留她的面部身份、比例和辨识特征。塑造一位美丽女性，身穿宽松的薰衣草紫色露肩针织毛衣，坐在明亮舒适卧室里的白色床上。柔软的白色床品环绕她，左侧大窗户让暖阳洒满房间。她在床上略微侧坐，上身轻轻后仰。左臂举过头顶，手放在头发里；另一只手臂自然垂在身侧。双肩放松，宽松毛衣露出一侧肩膀。她的头向上并略向后仰，眼睛大部分被散落的发丝遮住，露出自然、灿烂且看得见牙齿的笑容。长而蓬松的凌乱波浪发，自然宽松的中分，发量丰盈，凌乱的脸侧发丝垂过额头和眼睛，柔软的波浪卷落在肩膀和背部。白皙透亮的瓷质肌肤，呈亮象牙色至浅米色，带中性偏冷的底调，在暖阳下自然发亮。来自窗户的强烈金色逆光让头发与肩膀周围泛起发光的高光，伴随柔和镜头光斑、明亮通透的高光与轻柔阴影。暖调粉彩调色，以柔薰衣草紫、奶油白和金色为主；梦幻高调光线、细微柔光、自然肤质、浅景深、柔和浪漫的时尚摄影。
负面提示词：身份改变、面部扭曲、手或手指畸形、人体结构错误、不自然姿势、文字或水印。
```

<sub>(by [@imGopalTiwari](https://x.com/imGopalTiwari/status/2100744113503052078)) · [来源平台： X](https://x.com/imGopalTiwari/status/2100744113503052078)</sub>

<a id="p65-snowy-mountain-plaid-scarf-portrait"></a>

### 📌 1.21. 雪山格纹围巾人像

#### 👀 预览

[<img src="assets/p65-snowy-mountain-plaid-scarf-portrait/source-example-01.jpg" width="225" height="400" alt="雪山格纹围巾人像——来源示例">](assets/p65-snowy-mountain-plaid-scarf-portrait/source-example-01.jpg)

#### 👇 工作流

`人像参考图 → 雪山人像`

#### 🔖 完整提示词

```text
超写实、IMAX 级、Netflix 风格的电影感人像，9:16 竖版。以上传图片作为主要身份参考，准确保留她的面部身份、比例和辨识特征。塑造一位美丽女性，身穿黑色修身上衣、灰色牛仔夹克、黑色长裤、黑色系带靴、圆形深色太阳镜，并在颈间松松围着黑灰格纹围巾。她自信地坐在一块崎岖、覆雪的巨大山石上，四周是辽阔的雪山和密集的覆雪松林。一侧膝盖高高抬在身前，另一条腿沿岩石向下弯曲，两只靴子都稳稳踩在岩石上。一只手自然放在抬起的膝盖上，另一只手搭在另一侧大腿。上身挺直，略微放松地倾斜，肩膀自然；头微微上扬并转向一侧，表情平静、自信。浓密的长波浪发蓬松地向后梳，带有有质感的波浪、抬高的发根、自然动感和几缕勾勒脸部的散发。白皙透亮的瓷质肌肤，亮象牙色至浅米色，带中性偏冷底调；自然肤质和柔和真实的高光。柔和的冷色日光照亮她的脸与衣服，在雪景上形成轻微高光和冷调阴影。冷蓝灰冬日调色、低饱和色彩、轻柔的大气薄雾、真实的雪与岩石纹理、浅景深、电影感山地摄影。
负面提示词：身份改变、面部扭曲、手或手指畸形、人体结构错误、不自然姿势、文字或水印。
```

<sub>(by [@imGopalTiwari](https://x.com/imGopalTiwari/status/2100698813539492223)) · [来源平台： X](https://x.com/imGopalTiwari/status/2100698813539492223)</sub>

<a id="p68-towel-wrapped-makeup-frame-reconstruction"></a>

### 📌 1.22. 包毛巾上妆视频画面重建

#### 👀 预览

[<img src="assets/p68-towel-wrapped-makeup-frame-reconstruction/source-example-01.jpg" width="238" height="400" alt="包毛巾上妆视频画面重建——来源示例">](assets/p68-towel-wrapped-makeup-frame-reconstruction/source-example-01.jpg)

#### 👇 工作流

`参考画面 → 上妆视频静帧重建`

#### 🔖 完整提示词

```text
{
  "prompt_type": "photorealistic_image_reconstruction",
  "objective": "尽可能忠实地重建所提供的参考图，同时完全删除并忽略所有屏幕文字、播放控件、进度条、图标、时间戳及其他视频界面元素。保留原有摄影场景、人物、姿势、表情、造型、光线、环境、取景、比例和材质纹理。",
  "reference_priority": {
    "overall_composition": "极高",
    "subject_placement": "极高",
    "facial_structure": "极高",
    "towel_shape_and_texture": "极高",
    "hand_position": "极高",
    "lip_pencil_position": "极高",
    "lighting": "极高",
    "background_geometry": "高",
    "color_palette": "高",
    "micro_texture": "高",
    "ui_elements": "完全忽略"
  },
  "canvas": {
    "orientation": "竖版",
    "aspect_ratio": "约 704:1130",
    "framing": "竖版智能手机相机构图",
    "crop": "从头顶毛巾包裹处到上胸和肩部的紧凑特写",
    "edge_behavior": {
      "left_edge": "主体人像区域外可见一道狭窄的黑色竖边",
      "right_edge": "主体人像区域外可见一道极窄的深色或黑色边缘",
      "top_edge": "毛巾上方留有少量浅色背景",
      "bottom_edge": "在上身和胸部位置裁切"
    },
    "important": "不要重现任何截图控件、文字、图标、时间戳、进度指示或播放按钮。"
  },
  "scene_description": {
    "setting": "明亮、极简、现代的浴室或整洁的梳妆间内部",
    "visual_mood": "柔和、亲密、随意的日常美妆自拍",
    "time_of_day": "白天，或采用明亮日光色的室内光线",
    "overall_style": "真实的现代智能手机美妆视频画面，高度照片级真实，略带美颜但仍自然",
    "environmental_complexity": "简洁且不杂乱",
    "background_focus": "背景比女性面部略柔和、稍稍失焦"
  },
  "subject": {
    "person": {
      "description": "成年女性",
      "pose": "以放松的坐姿或半躺姿势正对镜头",
      "orientation": "正面人像",
      "head_alignment": "头部居中，仅有轻微自然倾斜",
      "body_visibility": "头、颈、双肩、上胸及一只或两只手可见",
      "expression": "平静放松、略微噘嘴，呈现自然柔和的美妆教程表情",
      "gaze": "看向镜头"
    },
    "skin": {
      "base_tone": "带柔和金色底调的浅至中等暖米色",
      "texture": "肤色非常平滑均匀，符合轻微社交媒体美颜滤镜的效果",
      "finish": "柔和发光的肌肤，带自然轻微高光",
      "blemishes": "瑕疵很少",
      "pores": "毛孔细微且被柔化，不要过度凸显细节",
      "blush": "双颊苹果肌有明显但柔和晕开的玫瑰粉腮红",
      "undertone": "温暖健康",
      "contrast": "低至中等"
    },
    "face": {
      "shape": "柔和的椭圆形脸",
      "forehead": "平滑、宽度适中的额头",
      "cheeks": "饱满、柔和圆润的双颊",
      "jaw": "下颌线柔和收窄",
      "chin": "小巧圆润的下巴",
      "symmetry": "自然且较高的面部对称性",
      "proportions": "精致、显年轻的面部比例"
    },
    "eyes": {
      "shape": "大而呈杏仁形的眼睛",
      "color": "深棕色",
      "orientation": "正面朝向镜头",
      "upper_lashes": {
        "length": "很长",
        "density": "浓密",
        "curl": "明显向上卷翘",
        "appearance": "明显经过美妆加强的睫毛"
      },
      "lower_lashes": "下睫毛细微、不突出",
      "eyelids": "眼睑轮廓柔和",
      "eye_makeup": "沿睫毛根部仅有少量深色眼妆",
      "under_eye": "眼下平滑、略提亮，没有明显黑眼圈",
      "catchlights": "轻微、柔和的眼神光"
    },
    "eyebrows": {
      "shape": "浓密、略带柔和弧度的眉毛",
      "color": "深棕色",
      "density": "中等偏浓",
      "styling": "修整干净但自然",
      "texture": "可见柔和的单根眉毛细节"
    },
    "nose": {
      "shape": "小巧精致的鼻子",
      "bridge": "鼻梁平滑、轮廓柔和",
      "tip": "鼻尖圆润低调",
      "lighting": "鼻梁和鼻尖有轻柔高光",
      "contour": "极轻微的自然修容"
    },
    "lips": {
      "shape": "饱满柔软的双唇",
      "upper_lip": "清晰的唇峰",
      "lower_lip": "下唇更饱满圆润",
      "position": "双唇微张并轻轻抿起",
      "color": "低饱和的玫瑰豆沙裸色",
      "finish": "柔和缎光，带少许自然光泽",
      "makeup": "淡淡的唇线及柔和粉裸色",
      "action": "正用唇线笔直接描画双唇中央和下唇"
    }
  },
  "hair": {
    "visibility": "头发几乎完全被遮住",
    "style": "头发完全包在一条大毛巾形成的头巾里",
    "visible_hair": "额头或发际线附近最多露出极少量头发",
    "instruction": "不要让长发披散在肩膀周围。"
  },
  "head_towel": {
    "type": "用大浴巾包出的饱满头巾",
    "material": "厚实机织棉布，具有明显的华夫格纹理",
    "primary_color": "暖调浅灰米色",
    "texture": {
      "pattern": "细密重复的方格或华夫格织纹",
      "definition": "清晰可见，但经过手机相机处理后稍显柔和",
      "surface": "哑光、吸水的棉质表面"
    },
    "structure": {
      "top": "头顶堆叠着大而圆润的多层褶皱",
      "front": "厚厚的卷边勾勒额头",
      "left_side": "一大块向外折叠的毛巾从头部左侧向后伸出",
      "right_side": "较长的毛巾部分沿面部右侧和肩膀向下垂落",
      "rear": "头后方有厚实的多层毛巾体积",
      "folds": "多个相互重叠的自然褶皱和扭转层次",
      "silhouette": "宽大、圆润、夸张的毛巾轮廓包围头顶"
    },
    "color_variation": "重叠褶皱之间有细微色差，略带粉米色和冷灰色变化",
    "lighting_response": "凸起的华夫格纹理上有柔和高光，褶皱内部有轻柔阴影"
  },
  "secondary_towel_or_fabric": {
    "description": "头部两侧和后方及肩后可见额外的柔软灰色毛巾状布料",
    "material": "柔软吸水的毛圈布或带纹理的棉布",
    "color": "浅中性灰色",
    "purpose": "增加头部周围层叠的毛巾体积"
  },
  "hands": {
    "visibility": "双手明显出现在画面下方中央前景",
    "skin_tone": "与人物暖米金色肤色一致",
    "position": "一只或两只手在嘴前竖直握住化妆笔",
    "gesture": "精细、准确的美妆上妆动作",
    "fingers": {
      "shape": "纤细的女性手指",
      "pose": "握笔姿态放松但稳定",
      "anatomy": "自然的人类手指比例",
      "instruction": "不得有多余手指、粘连手指、扭曲关节或畸形手部。"
    },
    "nails": {
      "length": "中长",
      "shape": "柔和方形或方头",
      "color": "不透明的干净白色",
      "finish": "平滑有光泽的美甲",
      "detail": "指甲表面有轻微镜面反光"
    }
  },
  "cosmetic_pencil": {
    "type": "纤细的唇线笔",
    "position": "几乎完全竖直，从画面下方中央向上延伸到双唇",
    "tip_location": "笔尖触碰或几乎触碰双唇中央或下唇",
    "body_color": "灰玫瑰色、低饱和粉色、豆沙粉色",
    "finish": "哑光至缎光",
    "shape": "纤细的圆柱形化妆笔",
    "visible_length": "很长一段笔身向下延伸到手中",
    "branding": "笔身可以有模糊的浅色化妆品标记，但不得出现可读文字",
    "interaction": "正在描画下唇轮廓或给下唇上色"
  },
  "jewelry": {
    "necklace": {
      "type": "非常细的精致链条",
      "color": "银色或浅金属色",
      "placement": "环绕颈部，部分显露在上胸前",
      "pendant": {
        "description": "小巧精致的金属吊饰",
        "shape": "紧凑的圆形或类似字母的吊饰",
        "position": "位于可见颈部与胸口较低的中央位置",
        "appearance": "明亮的金属高光，略带闪光"
      }
    }
  },
  "upper_body": {
    "clothing": "露出肩膀和上胸",
    "pose": "双肩放松",
    "skin_rendering": "平滑但仍有自然立体感",
    "lighting": "柔和正面光，下巴和锁骨周围有轻微阴影",
    "composition": "双肩分别延伸至画面左下角和右下角"
  },
  "background": {
    "walls": {
      "color": "非常浅的冷白色，略带蓝灰色调",
      "finish": "平滑的涂漆墙面",
      "detail": "整洁的极简建筑细节"
    },
    "ceiling_fan": {
      "visibility": "画面左上方附近可见部分吊扇",
      "description": "白色或极浅色的吊扇机身，一片深灰或黑色扇叶垂入画面",
      "focus": "不在主要焦平面上，因此略微柔化"
    },
    "air_vent": {
      "position": "右上方背景",
      "description": "白色矩形暖通空调或回风口，带狭窄的水平百叶",
      "appearance": "低调、整洁、几何感",
      "focus": "略微柔化"
    },
    "door_or_architecture": {
      "position": "最右侧背景",
      "description": "简洁的白色建筑边线或门框",
      "visibility": "局部可见",
      "detail_level": "柔和且不抢眼"
    },
    "background_depth": "浅景深，背景柔和模糊但仍可辨认"
  },
  "camera": {
    "device_style": "现代智能手机前置摄像头",
    "lens": "全画幅等效约 24–28mm 的广角自拍镜头",
    "perspective": "近距离面部自拍视角，带轻微广角特征",
    "camera_height": "大约与眼睛齐平",
    "camera_distance": "距离约一臂远",
    "orientation": "竖版人像",
    "focus_point": "眼睛和面部中央",
    "sharpness": "面部清晰，背景适度柔化",
    "depth_of_field": "中等偏浅的景深",
    "stabilization": "画面稳定",
    "image_quality": "高分辨率的现代智能手机影像",
    "processing": "轻微的计算摄影处理与美颜柔化"
  },
  "lighting": {
    "primary_source": "正面大面积漫射窗光或柔和的人造日光",
    "direction": "从正面略高处照射",
    "quality": "非常柔和",
    "contrast": "低对比度",
    "shadows": "阴影轻柔、弥散，没有硬边",
    "skin_highlights": "额头、鼻子、双颊及双唇上有柔和高光",
    "towel_lighting": "毛巾凸起的织纹处高光略亮",
    "background_lighting": "背景有浅淡冷色环境光",
    "color_temperature": "冷中性日光，肤色仍呈温暖质感",
    "overall_effect": "讨喜、干净、柔和的美妆视频光线"
  },
  "color_palette": {
    "dominant_colors": [
      "浅冷白色",
      "暖浅灰色",
      "米色",
      "灰米色",
      "柔和玫瑰粉",
      "灰豆沙紫",
      "暖金色肌肤"
    ],
    "saturation": "中等偏低",
    "contrast": "低至中等",
    "highlights": "奶油般柔和",
    "shadows": "轻柔且略微抬升",
    "skin_color_priority": "自然暖肤色必须与冷色背景保持区分",
    "towel_color_priority": "中性暖灰米色"
  },
  "beauty_processing": {
    "style": "轻微的社交媒体美颜滤镜",
    "skin_smoothing": "中等至较高",
    "blemish_reduction": "高",
    "facial_shape_adjustment": "极轻微",
    "eye_enhancement": "细微",
    "lash_enhancement": "可见",
    "blush_enhancement": "中等",
    "lip_enhancement": "细微",
    "overall_result": "精致但可信的智能手机美妆视频画面",
    "avoid": "避免极端修脸、塑料肌肤、不真实的对称感或人工 CGI 肌肤"
  },
  "composition_geometry": {
    "subject_center": "水平方向大致居中",
    "face_position": "面部位于画面中央中部",
    "eyes": "眼睛位于上半部约三分之一处",
    "towel_top": "毛巾顶部伸入画面上四分之一部分",
    "mouth": "嘴部位于垂直方向中央附近",
    "hands": "双手占据下方中央前景",
    "pencil": "化妆笔构成近乎竖直的中央视觉线",
    "shoulders": "双肩填满左下和右下区域",
    "negative_space": "留白有限，营造亲密特写取景",
    "symmetry": "整体大致为对称的正面构图，毛巾褶皱和双手保留自然不对称"
  },
  "fine_details": {
    "skin": "柔和真实的肤质，带细微色调变化",
    "lashes": "可见单根成束的睫毛",
    "brows": "可见细密的眉毛纹理",
    "lips": "妆容下可见细微自然唇纹",
    "nails": "干净、光泽的白色表面",
    "towel": "可见单根凸起的织线和线圈",
    "necklace": "细小金属反光",
    "pencil": "化妆笔上有细小印刷标记，但不得有可辨识文字",
    "background": "微弱的建筑细节，不要有分散注意力的杂物"
  },
  "photographic_style": {
    "genre": "随性而精致的美容或自我护理手机人像",
    "realism": "极高的照片级真实感",
    "image_character": "真实美妆视频的暂停画面",
    "retouching": "柔和的计算摄影美颜处理",
    "texture": "干净但不呆板",
    "dynamic_range": "高",
    "sharpness": "面部和双手中等程度清晰",
    "compression": "轻微的智能手机或社交媒体压缩质感"
  },
  "negative_prompt": [
    "文字",
    "图注",
    "字幕",
    "水印",
    "标志",
    "播放按钮",
    "暂停按钮",
    "进度条",
    "时间轴",
    "时间戳",
    "视频控件",
    "界面叠层",
    "社交媒体图标",
    "界面元素",
    "不同的人物",
    "不同的面部比例",
    "不同的姿势",
    "不同的毛巾造型",
    "披散的长发",
    "深色毛巾",
    "鲜艳颜色的毛巾",
    "红色口红",
    "深色口红",
    "浓重修容",
    "夸张眼线",
    "普通眼镜",
    "太阳镜",
    "耳环",
    "额外首饰",
    "其他人物",
    "多余的手",
    "多余的手指",
    "缺失的手指",
    "畸形的手",
    "过长的手指",
    "错误的指甲颜色",
    "尖头指甲",
    "红色指甲",
    "用口红管代替唇线笔",
    "横向构图",
    "横幅摄影",
    "全身",
    "侧面视角",
    "四分之三侧面视角",
    "夸张姿势",
    "硬闪光",
    "强烈阴影",
    "暖橙色光线",
    "昏暗环境",
    "杂乱的浴室",
    "以镜子为主的构图",
    "影棚时尚大片",
    "电影感摄影",
    "CGI",
    "3D 渲染",
    "插画",
    "动漫",
    "塑料肌肤",
    "过度磨皮",
    "诡异的人脸",
    "过度 HDR",
    "过强的背景虚化",
    "过度锐化的毛孔"
  ],
  "final_instruction": "生成一张高度照片级真实的竖版图像，尽可能贴合参考图构图。保留居中的正面脸部取景、带层叠褶皱的夸张米灰色纹理毛巾头巾、温暖平滑的肤色、玫瑰粉双颊、细长深色睫毛、饱满的柔和粉裸色嘴唇、白色亮面美甲、竖直触碰下唇的灰粉色唇线笔、精致银色项链、裸露双肩、浅冷色浴室背景、顶部局部可见的吊扇，以及右上方背景的矩形通风口。删除并忽略所有文字元素、时间戳、播放按钮、进度线和其他界面图形。结果应像没有任何界面叠层的干净原始视频画面。"
}
```

<sub>(by [@neverfilmed](https://x.com/neverfilmed/status/2100670687489020274)) · [来源平台： X](https://x.com/neverfilmed/status/2100670687489020274)</sub>

<a id="p69-summer-ice-cream-selfie"></a>

### 📌 1.23. 夏日冰淇淋自拍

#### 👀 预览

[<img src="assets/p69-summer-ice-cream-selfie/source-example-01.png" width="320" height="400" alt="夏日冰淇淋自拍——来源示例">](assets/p69-summer-ice-cream-selfie/source-example-01.png)

#### 👇 工作流

`文字 → 夏日冰淇淋抓拍自拍`

#### 🔖 完整提示词

```text
一张近距离、自然抓拍的自拍照：一位年轻女性站在户外质朴的天然石墙前，俏皮地舔着正在融化的冰淇淋筒。她伸出舌头接住滴落的冰淇淋，张着嘴，呈现有趣的瞬间。她单手举着甜筒，甜筒外包着格纹纸；佩戴粗框、超大圆形黑色太阳镜，镜片为棕色。深棕色长发编成两条松散的辫子，用黑色小发圈扎住，几缕柔软发丝修饰脸部。妆容温暖自然，带红润气色和亮泽双唇；指甲涂成长款红色，佩戴粗金戒指和多条精细的金色链条项链。

她穿着精致的钩针或针织开衫，饰以花朵珠饰、米珠与小珍珠，下搭一件带图案的上衣。前景中冰淇淋筒清晰对焦：华夫筒上是白色香草和粉色草莓口味的软冰淇淋旋卷，正沿两侧融化滴落，外面套着橙白格纹纸筒。

温暖、明亮、自然的地中海日光处于柔和阴影中，形成均匀暖光与轻柔阴影。背景是一面蜂蜜色与灰色交织的质朴天然石砖墙，受光柔和，填满她身后的画面。

面部结构：年轻的椭圆脸、柔和双颊、饱满双唇、直鼻、浓眉，以及温暖、被阳光亲吻过的地中海肤色。

相机与真实感：以手机前置摄像头拍摄，自拍视角自然、距离略近。真实的手机照片画质：细微颗粒、逼真的暖色、自然动态范围，没有厚重滤镜。高度真实的皮肤保留可见的天然质地——毛孔、淡淡雀斑、柔软细汗毛、细微肤色不均和日光下的自然光泽——让它读作真实抓拍，而非修图或磨皮。自然的浅景深，让冰淇淋与面部最清晰，后方石墙略柔和。温暖、俏皮的欧洲夏日氛围。
```

<sub>(by [u/imagine_ai](https://www.reddit.com/r/ImagineAiArt/comments/1wi79wi/gpt_image_25_flare_is_this_actually_the_best_ai/)) · [来源平台： Reddit](https://www.reddit.com/r/ImagineAiArt/comments/1wi79wi/gpt_image_25_flare_is_this_actually_the_best_ai/)</sub>

<a id="p70-y2k-lounge-fashion-portrait"></a>

### 📌 1.24. Y2K 休息室时尚人像

#### 👀 预览

[<img src="assets/p70-y2k-lounge-fashion-portrait/source-example-01.png" width="320" height="400" alt="Y2K 休息室时尚人像——来源示例">](assets/p70-y2k-lounge-fashion-portrait/source-example-01.png)

#### 👇 工作流

`文字 → Y2K 休息室时尚人像`

#### 🔖 完整提示词

```text
一张由他人在自然视线高度拍摄的随手照片：一位年轻东亚女性坐在室内一间时尚、暖色调的休息室或酒吧里，从臀部以上取景。她抬起一只手轻碰帽檐，肘部向外，头向下并稍稍侧倾；表情冷艳、妩媚、微噘嘴，双眼半垂，双唇亮泽。她留着顺滑的乌黑齐下巴短发，平直刘海落在额头与眼睛上，戴一顶柔软的蛇纹或豹纹报童帽。

造型受 Y2K 风格启发：修身紫色短袖露脐 T 恤，胸前有醒目的大号黑色数字图案（通用数字，不要标志），露出腰腹和肚脐穿孔饰品，下搭低腰、镶水钻的银色腰带或短裙。她戴一条由灰白珠子组成、带大吊坠的粗项链，一只手腕叠戴粗款银色手镯，指甲修长、尖端浅色，并挎一只细肩带的金属银色单肩包。背景是暖色、灯光昏暗的复古室内空间：弯曲的亮红色沙发、玻璃桌、墙上的抽象装框艺术、发光的壁灯和温暖的桃粉色光晕，轻微失焦。暖色环境室内光线、柔和阴影，营造有情绪且时髦的休息室气氛。

相机与纹理：在室内用 iPhone 后置摄像头拍摄，呈现真实的手机随手拍；细腻的传感器颗粒与数码噪点、暖色室内偏色、自然的手机动态范围与柔和高光、轻微柔焦，不加滤镜。

皮肤真实感（关键）：极其细致、逼真的真人皮肤，绝不呈现蜡质、塑料、过度平滑或 CGI 质感。保留自然的不完美：鼻子、脸颊与额头上可见毛孔，细软汗毛，轻微不均匀的肤色，淡雀斑与小痣，几颗细小瑕疵和自然暖意；眼下有柔和纹理及真实细纹；颧骨、鼻子、腰腹及手臂呈现自然柔和光泽，同时保留哑光区域。
```

<sub>(by [u/imagine_ai](https://www.reddit.com/r/ImagineAiArt/comments/1wi79wi/gpt_image_25_flare_is_this_actually_the_best_ai/)) · [来源平台： Reddit](https://www.reddit.com/r/ImagineAiArt/comments/1wi79wi/gpt_image_25_flare_is_this_actually_the_best_ai/)</sub>

<a id="p71-candid-street-food-bite"></a>

### 📌 1.25. 街头大口吃烤肉卷抓拍

#### 👀 预览

[<img src="assets/p71-candid-street-food-bite/source-example-01.png" width="320" height="400" alt="街头大口吃烤肉卷抓拍——来源示例">](assets/p71-candid-street-food-bite/source-example-01.png)

#### 👇 工作流

`文字 → 街头美食抓拍人像`

#### 🔖 完整提示词

```text
一张由他人拍摄的自然抓拍照：一位年轻女性坐在城市街道上一张小圆形户外咖啡桌前，俯身向下、向前张大嘴，即将大咬一口双手捧着、以锡箔纸和白纸包裹的馅料丰富的烤肉卷。她的眼睛轻轻闭着，咬下前的表情快乐又期待——有趣、未经摆拍、真实的抓拍瞬间。她的深色头发紧贴头皮向后梳，扎成顺滑低发髻或低马尾，脸侧有少量碎发；佩戴金色耳骨夹和粗款金色圈形或垂坠耳环。妆容柔和自然，眉形清晰、双唇亮泽；自然的阳光感肤色，肩膀和胸口带浅色雀斑与小痣。

她穿着黄色罗纹细肩带背心和牛仔裤，指甲涂浅中性色，戴金色戒指。桌上有一只米色斑点陶瓷盘、叠好的黄绿色与蓝绿色餐巾纸，以及一副折叠的太阳镜。馅料鼓出的卷饼清晰对焦：皮塔饼或薄饼内装切片 döner 烤肉、香脆炸物、新鲜绿生菜、番茄和酱汁。

欧洲城市街道上温暖、明亮的自然日光，柔和自然的阴影。背景是模糊的街景：停着的汽车、带招牌的店面、门洞与人行道，均柔和失焦。

面部结构：年轻的椭圆脸、分明颧骨、丰满双唇、修整整齐的浓眉、直鼻，以及温暖的阳光感肤色。

相机与真实感：用手机后置摄像头拍摄，取景自然抓拍。真实的手机照片画质：轻微颗粒、逼真的暖色、自然动态范围，没有厚重滤镜。高度真实的肌肤保留可见的天然纹理——肩膀与面部的毛孔、雀斑、小痣、细软汗毛、轻微肤色不均和日光下的自然光泽——让它读作真实抓拍，而非修图或磨皮。自然的浅景深，让卷饼与面部最清晰，背景虚化。温暖、有趣、即兴的街头美食氛围。
```

<sub>(by [u/imagine_ai](https://www.reddit.com/r/ImagineAiArt/comments/1wi79wi/gpt_image_25_flare_is_this_actually_the_best_ai/)) · [来源平台： Reddit](https://www.reddit.com/r/ImagineAiArt/comments/1wi79wi/gpt_image_25_flare_is_this_actually_the_best_ai/)</sub>

<a id="-characters--playful-creations"></a>

## 🧸 角色与趣味创作

<a id="p52-iphone-photos-day-in-the-life-camera-roll"></a>

### 📌 2.1. iPhone 照片 App 一日相册

#### 👀 预览

[<img src="assets/p52-iphone-photos-day-in-the-life-camera-roll/source-example-01.jpg" width="185" height="400" alt="iPhone 照片 App 一日相册——来源示例">](assets/p52-iphone-photos-day-in-the-life-camera-roll/source-example-01.jpg)

#### 👇 工作流

`主体参考图 → iPhone 照片 App 相册图`

#### 🔖 完整提示词

```text
仅将上传的图片用作主体参考。

创建一张竖版图片，使其看起来完全像 iPhone“照片”App 的屏幕截图，展示由上传参考图中的同一主体出演的一整天随手相册照片。

主体一致性
首先识别上传图片中的主要主体。它可以是人物、动漫角色、宠物、动物、毛绒玩具、手办、吉祥物、物体或其他角色。

在每张照片中始终保持主体可辨识的外观、颜色、比例、面部特征、发型、服装、配饰、标记、材质和标志性细节。

如果参考图包含同一主体的多个视角，应理解为同一个主体的不同视图，而不是多个角色。

不要重新设计或替换主体。

一日生活相册
根据该主体的外观、个性、风格与视觉世界，设想真实可信的一整天。

生成从清晨到夜晚的许多不同随手照片，仿佛有人在一天中自然地持续拍摄该主体。

自动选择适合上传主体的日常情境，例如：
醒来、休息、进食、坐在窗边、出行、户外散步、逛咖啡馆或商店、玩耍、工作、居家放松、与日常物品互动、日落时刻、夜间外出以及入睡。

活动和环境应自然适配主体。当主体是动物、玩具、物体或非人类角色时，不要强行安排看起来不自然的人类活动。

每个缩略图都应呈现不同的时刻、构图、距离、姿势、拍摄角度、光线条件或地点。

混合使用：
特写、
中景、
远景、
俯拍照片、
背影视角、
细节照片、
略带模糊的运动照片、
不完美的手持快照、
主体被局部裁切的照片、
与主体一天生活相关的环境照片。

整体应像自然随性、私人的生活记录，而不是专业摄影棚拍摄。

IPHONE“照片”APP 布局
最终图片本身必须像一张真实的全屏 iPhone“照片”App 截图。

使用高挑的智能手机屏幕截图比例，约为 9:19.5。

采用四列等宽缩略图创建密集相册网格，紧密贴近标准 iPhone“照片”App 的网格布局。

屏幕中应显示约 24–32 张独立照片缩略图。

缩略图之间只留极细的白色间隙。

相册网格应占据屏幕纵向的大部分空间。

包含真实可信的 iPhone“照片”界面元素：
• 白色 iOS 界面背景
• 顶部 iPhone 风格状态栏
• 左上角显示时间
• 右上角显示蜂窝网络/Wi-Fi/电池图标
• 顶部附近带有简洁导航控件
• 四列照片网格
• 底部“照片”App 导航栏
• “照片”标签以蓝色选中
• 其他导航图标显示为灰色
• 最底部带黑色主屏幕指示条

界面必须像真实的“照片”App 截图，而不是装饰边框、情绪板、联系表、剪贴簿、海报或普通拼贴画。

照片风格
让每个缩略图都像真实随手拍摄的 iPhone 相册照片。

使用自然日常光线、不完美构图、真实的曝光变化、偶尔的运动模糊、轻微对焦瑕疵、随性的画面安排和可信环境细节。

让同一主体在整幅相册中始终可辨识，同时允许姿势、表情、拍摄距离和光线产生自然变化。

如果上传参考图是插画、动画、风格化作品或 3D 图像，除非明确要求写实摄影，否则保留其原始视觉身份与风格。

重要要求
最终只输出一张图片。
完整输出是一张 iPhone“照片”App 截图，其中包含许多不同照片。
严格使用四列缩略图。
不要制作缺少 iPhone 界面的独立拼贴画。
不要创建多个独立输出。
不要重复使用完全相同的照片。
不要引入无关角色或主体。
不要改变主要主体的设计。
照片缩略图内部不要出现说明、日期、标签、贴纸、水印或装饰性文字。
只允许出现正常且极简的 iOS 界面元素。

9:16
```

<sub>(by [@Mayz1169](https://x.com/Mayz1169/status/2099479873027031442)) · [来源平台： X](https://x.com/Mayz1169/status/2099479395283214473) · 灵感来自 [@ikaretamenonui](https://x.com/ikaretamenonui/status/2099139951820742839)</sub>

<a id="p41-minecraft-skin-from-a-reference"></a>

### 📌 2.2. 参考图 → Minecraft 皮肤

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

<sub>(作者：SeeAPI)</sub>

<a id="p33-expressive-meme-sticker-sheet"></a>

### 📌 2.3. 夸张表情包贴纸

#### 👀 预览

[<img src="assets/p33-expressive-meme-sticker-sheet/source-example-01.jpg" width="400" height="300" alt="夸张表情包贴纸——来源示例">](assets/p33-expressive-meme-sticker-sheet/source-example-01.jpg)

#### 👇 工作流

`角色参考图 → 贴纸图`

#### 🔖 完整提示词

```text
根据所附图片制作表情包贴纸，融入 😎😛💕🚀🥳。使用夸张的网络反应表情，包括哭泣、困惑、震惊、得意、侧目和面无表情的难以置信，搭配别扭姿势、低保真剪贴纹理和荒诞幽默。

制作一张正方形（1:1）透明贴纸图，九张不同贴纸排列为 3×3 网格，每张展示不同表情、姿势或反应。贴纸之间留宽阔、完全透明的间隔。无背景、阴影或重叠元素。
```

<sub>[来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p18-four-panel-pet-comic"></a>

### 📌 2.4. 四格宠物漫画

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="p11-character-dance-pose-grid"></a>

### 📌 2.5. 角色舞蹈姿势网格

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

<sub>(by [@renoiseai](https://x.com/renoiseai/status/2097959984265130436)) · [来源平台： X](https://x.com/renoiseai/status/2097959984265130436)</sub>

<a id="p06-portrait-reference-to-multi-view-sheet"></a>

### 📌 2.6. 人像参考 → 多视图设定图

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

<sub>(作者：SeeAPI)</sub>

<a id="p02-collectible-figure-packaging"></a>

### 📌 2.7. 收藏玩偶包装

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

<sub>(作者：SeeAPI)</sub>

<a id="p01-personalized-sticker-pack"></a>

### 📌 2.8. 个性化贴纸包

#### 👀 预览

[<img src="assets/p01-personalized-sticker-pack/character-stickers-result.png" width="400" height="400" alt="蓝色背景上的四张猫咪表情贴纸">](assets/p01-personalized-sticker-pack/character-stickers-result.png)

#### 👇 工作流

`角色参考图 → 贴纸图片`

#### 🔖 完整提示词

```text
以上传的人物或角色作为身份参考，制作干净的 2×2 贴纸图，包含四种表情：[expression 1]、[expression 2]、[expression 3] 和 [expression 4]。

保留主体的身份、身体结构、比例、颜色、服装（如有）以及独特特征。根据主体的身体结构调整每种表情和姿势，不改变物种或性别呈现。每个单元格都展示完整主体，使用粗白色贴纸描边，贴纸之间留出充足间隔。背景为纯色 [background color]，使轮廓便于分离。不添加说明文字、字母、装饰物，不让内容跨格重叠。
```

<sub>(作者：SeeAPI)</sub>

<a id="p56-raiden-shogun-in-a-film-scene"></a>

### 📌 2.9. 雷电将军闯入电影名场面

#### 👀 预览

[<img src="assets/p56-raiden-shogun-in-a-film-scene/source-example-01.jpg" width="225" height="400" alt="雷电将军闯入电影名场面——来源示例">](assets/p56-raiden-shogun-in-a-film-scene/source-example-01.jpg)

[<img src="assets/p56-raiden-shogun-in-a-film-scene/source-example-02.jpg" width="225" height="400" alt="雷电将军闯入电影名场面——来源示例">](assets/p56-raiden-shogun-in-a-film-scene/source-example-02.jpg)

#### 👇 工作流

`电影场景 + 雷电将军 → 荒诞竖版抓拍`

#### 🔖 完整提示词

```text
经典电影名场面 × 第三者雷电将军融入剧情 × 荒诞合理感 × 失败照片 × 9:16竖版。
```

<sub>(by [@DeepBlueX0](https://x.com/DeepBlueX0/status/2100156601600782528)) · [来源平台： X](https://x.com/DeepBlueX0/status/2100156601600782528) · 英文由 SeeAPI 翻译</sub>

<a id="p58-cat-expression-transfer"></a>

### 📌 2.10. 猫咪表情迁移

#### 👀 预览

[<img src="assets/p58-cat-expression-transfer/source-example-01.jpg" width="400" height="400" alt="猫咪表情迁移——来源对比拼图">](assets/p58-cat-expression-transfer/source-example-01.jpg)

[<img src="assets/p58-cat-expression-transfer/source-example-02.jpg" width="334" height="400" alt="猫咪表情迁移——来源对比拼图">](assets/p58-cat-expression-transfer/source-example-02.jpg)

#### 👇 工作流

`表情参考图 + 猫咪参考图 → 迁移表情的猫咪`

#### 🔖 完整提示词

```text
把图二猫咪变成图一那样的表情
```

<sub>(by [@ZHO_ZHO_ZHO](https://x.com/ZHO_ZHO_ZHO/status/2099832996216135874)) · [来源平台： X](https://x.com/ZHO_ZHO_ZHO/status/2099832996216135874) · 英文由 SeeAPI 翻译</sub>

<a id="p66-couch-potato-miniature-set"></a>

### 📌 2.11. 懒人土豆微缩客厅

#### 👀 预览

[<img src="assets/p66-couch-potato-miniature-set/source-example-01.jpg" width="400" height="225" alt="懒人土豆微缩客厅——来源示例">](assets/p66-couch-potato-miniature-set/source-example-01.jpg)

#### 👇 工作流

`文字 → 懒人土豆微缩场景`

#### 🔖 完整提示词

```text
一颗大号红褐色土豆斜躺在一张微缩软垫扶手椅里，它天然疙瘩状的下半部搁在脚凳上，旁边放着电视遥控器。微缩布景摄影、视线高度取景、温暖的傍晚台灯光线；保留真实的土豆皮和慵懒舒适的姿态，置于没有文字的客厅。16:9 横幅构图。
```

<sub>(by [@unrealpixels](https://x.com/unrealpixels/status/2100662656835420370)) · [来源平台： X](https://x.com/unrealpixels/status/2100662656835420370)</sub>

<a id="-products--branding"></a>

## 🛍️ 产品与品牌视觉

<a id="p31-virtual-outfit-replacement"></a>

### 📌 3.1. 虚拟换装

#### 👀 预览

[<img src="assets/p31-virtual-outfit-replacement/source-example-01.jpg" width="400" height="313" alt="虚拟换装——来源示例">](assets/p31-virtual-outfit-replacement/source-example-01.jpg)

#### 👇 工作流

`人物参考图 + 服装参考图 → 换装图片`

#### 🔖 完整提示词

```text
以图片 1 作为人物参考，其余上传图片作为服装参考。只编辑图片 1 中人物穿着的服装。保留其准确身份、面容、年龄、肤色、身体比例、性别呈现、表情、发型和姿势。将参考服装自然适配其体型和姿势，表现真实布料行为。匹配原始照明、阴影和色温。背景、相机角度、构图和画质保持不变。不添加配饰、文字、标志或水印。
```

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcj1ud/gpt_image_25_prompt_guide_2026_23_9_official_edit/) · 参考图改编：SeeAPI</sub>

<a id="p27-cereal-box-nutrition-panel"></a>

### 📌 3.2. 麦片盒营养成分表

#### 👀 预览

[<img src="assets/p27-cereal-box-nutrition-panel/source-example-01.webp" width="400" height="226" alt="麦片盒营养成分表——来源示例">](assets/p27-cereal-box-nutrition-panel/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
麦片盒背面，包含完整营养成分表，每个数值都清晰可读
```

<sub>(收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p22-wine-label-with-tasting-notes"></a>

### 📌 3.3. 附品鉴笔记的葡萄酒标签

#### 👀 预览

[<img src="assets/p22-wine-label-with-tasting-notes/source-example-01.webp" width="400" height="225" alt="附品鉴笔记的葡萄酒标签——来源示例">](assets/p22-wine-label-with-tasting-notes/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
葡萄酒瓶标签，包含酒庄名称、年份和四行品鉴笔记
```

<sub>(收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p21-vintage-toy-airplane-packaging"></a>

### 📌 3.4. 复古玩具飞机包装

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="p16-minimal-bakery-logo"></a>

### 📌 3.5. 极简面包店标志

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="p15-streetwear-campaign-with-exact-typography"></a>

### 📌 3.6. 准确文字的街头服饰广告

#### 👀 预览

[<img src="assets/p15-streetwear-campaign-with-exact-typography/source-example-01.webp" width="267" height="400" alt="准确文字的街头服饰广告——来源示例">](assets/p15-streetwear-campaign-with-exact-typography/source-example-01.webp)

#### 👇 工作流

`人物参考图 → 街头服饰广告`

#### 🔖 完整提示词

```text
使用上传的人物参考图定义画面中的朋友，每张参考图对应一个独立人物。保留每个人可辨识的面容、年龄、肤色、性别呈现、发型和身体比例；绝不融合或交换身份。如果只上传一张人像，就只展示该人物。

为“[brand name]”制作精致的街头服饰广告。参考人物穿着 [streetwear styling]，自然地在 [setting] 相聚。采用现代构图、有活力的色彩方向、自然姿势和高级时装摄影。准确且清晰地呈现一次“[tagline]”。不显示方括号。不添加其他人物、额外文字、水印或无关标志。
```

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/) · 参考图改编：SeeAPI</sub>

<a id="p08-glass-material-remix"></a>

### 📌 3.7. 玻璃材质重塑

#### 👀 预览

[<img src="assets/p08-glass-material-remix/seeapi-glass-result.png" width="400" height="400" alt="保留原有颜色、转化为半透明玻璃的 SeeAPI 标志">](assets/p08-glass-material-remix/seeapi-glass-result.png)

#### 👇 工作流

`物体参考图 → 玻璃材质图片`

#### 🔖 完整提示词

```text
将上传图片中的主要物体转化为半透明玻璃，同时保留其整体轮廓、比例、朝向、颜色和标志性结构细节。

将其放在浅色石材表面上，搭配暖灰色影棚背景。表现可信的玻璃厚度、细微内部反射、曲面区域柔化的折射，以及贴合台面的接触阴影。使用左侧大型柔光源，后方添加微弱轮廓光。完整展示物体。不添加额外部件、标签、文字或无关道具。
```

<sub>(作者：SeeAPI)</sub>

<a id="p04-product-photo-to-campaign-visual"></a>

### 📌 3.8. 产品照片 → 广告视觉

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

<sub>(作者：SeeAPI)</sub>

<a id="p55-miniature-country-chocolate-bar"></a>

### 📌 3.9. 微缩国家巧克力

#### 👀 预览

[<img src="assets/p55-miniature-country-chocolate-bar/source-example-01.jpg" width="320" height="400" alt="微缩国家巧克力 — 法国来源示例">](assets/p55-miniature-country-chocolate-bar/source-example-01.jpg)

[<img src="assets/p55-miniature-country-chocolate-bar/source-example-02.jpg" width="320" height="400" alt="微缩国家巧克力 — 意大利来源示例">](assets/p55-miniature-country-chocolate-bar/source-example-02.jpg)

#### 👇 工作流

`国家与地标信息 → 微缩巧克力产品图`

#### 🔖 完整提示词

```text
创作一张令人惊叹、照片级真实的奢华食品艺术图像，将 [COUNTRY] 化作一块巨大的高级巧克力。

巧克力斜放在优雅的深色石材表面，从略微俯视的电影感角度拍摄。包装纸借鉴 [COUNTRY] 的视觉形象、色彩、纹样与文化美学，同时保持精致、高级的气质。

巧克力从中央戏剧性地裂开。

裂开的巧克力内部浮现一个极其精细的 [COUNTRY] 3D 微缩景观，仿佛整个国家都被雕刻在巧克力之中。

包含：

以 [FAMOUS LANDMARK] 为中心视觉焦点

周围环绕 [FAMOUS NATURAL LANDSCAPE]

微小而可辨认的当地建筑

微缩街道与交通工具

将 [FAMOUS LOCAL FOOD] 作为微小装饰元素

当地的花卉、树木、山峦或海岸线

该国独有的细微文化元素

巧克力本身必须极为真实：有光泽的可可表面、清脆的断口、柔滑的分层内馅、细小的巧克力碎屑、轻微融化的巧克力，以及真实的高光与阴影。

营造一种奇妙的过渡：巧克力碎块逐渐变成山脉、建筑与景观，看起来仿佛整个国家一直藏在巧克力之中。

高级商业食品摄影、电影感灯光、极度精细的微缩世界、真实材质、微距摄影、浅景深、空气透视、精致构图、丰富纹理、8K 照片级真实感；视觉上令人无法抗拒，超现实却可信。

构图：4:5 竖版、主体居中、戏剧性透视、干净奢华的背景、强烈视觉对比；无人、无字幕、无水印、无多余文字。
```

<sub>(by [@Naiknelofar788](https://x.com/Naiknelofar788/status/2100164588721651910)) · [来源平台： X](https://x.com/Naiknelofar788/status/2100164588721651910)</sub>

<a id="p67-cola-and-mentos-highway-dashcam"></a>

### 📌 3.10. 可乐与曼妥思高速公路行车记录仪画面

#### 👀 预览

[<img src="assets/p67-cola-and-mentos-highway-dashcam/source-example-01.jpg" width="400" height="227" alt="可乐与曼妥思高速公路行车记录仪画面——来源示例">](assets/p67-cola-and-mentos-highway-dashcam/source-example-01.jpg)

#### 👇 工作流

`文字 → 品牌卡车高速公路行车记录仪静帧`

#### 🔖 完整提示词

```text
指令：
制作一张静态画面，看起来像从一辆在高速公路行驶的汽车的行车记录仪中截取的真实帧。采用光学行车记录仪拍摄、宽阔的挡风玻璃视角，并看见挡风玻璃、A 柱及一小部分仪表台或引擎盖；画面要像真实日常的行车记录仪 JPEG，而不是电影画面，也不要 HDR。

事件／构图：
透过挡风玻璃向前看。在道路左侧（左车道或左侧路肩，清楚出现在画面里），有两辆靠得很近、带品牌标识的卡车。

可口可乐卡车（左侧，关键）：
一辆全尺寸可口可乐罐车或配送卡车，采用官方可口可乐红色涂装，标志清晰可读。它出了故障：罐壁上有一个撕裂的不规则破洞。一股粗重的深棕色可口可乐从洞中猛烈喷到沥青路面，大量液体形成不断扩散的积液和泡沫，空中有飞溅，湿路面反光。卡车已停下或缓慢挪动，处于道路险情中。

曼妥思卡车（在旁边，关键）：
紧贴可口可乐卡车（同处左侧车辆群，略微在前或并行）的是一辆封闭式厢式或配送卡车，车侧带大幅、明确可辨的 MENTOS 品牌标识（曼妥思标志和糖卷图案）。车后门和侧门均关闭。没有糖果洒出。必须清楚看出这是一辆曼妥思卡车。

摄像设备：
固定在挡风玻璃后方的行车记录仪，轻微桶形广角；画面底部可见仪表台或引擎盖，挡风玻璃带有污渍或反射，可选时间戳叠层；白天道路，远处还有其他车流。真实的消费级行车记录仪静帧。

光线：
白天，可阴天或晴天；道路颜色真实，可乐看起来像深色汽水而非黑色石油。

照片特征：
未经摆拍的行车记录仪截图；卡车在物理上可信，品牌可读，泄漏是事件焦点。
```

<sub>(by [@ECLIPSEINTEL001](https://x.com/ECLIPSEINTEL001/status/2100730298543550674)) · [来源平台： X](https://x.com/ECLIPSEINTEL001/status/2100730298543550674)</sub>

<a id="-posters--artistic-styles"></a>

## 🎨 海报与艺术风格

<a id="p53-adaptive-vintage-city-travel-poster"></a>

### 📌 4.1. 自适应复古城市旅行海报

#### 👀 预览

[<img src="assets/p53-adaptive-vintage-city-travel-poster/source-example-01.jpg" width="283" height="400" alt="自适应复古城市旅行海报——来源示例">](assets/p53-adaptive-vintage-city-travel-poster/source-example-01.jpg)

[<img src="assets/p53-adaptive-vintage-city-travel-poster/source-example-02.jpg" width="283" height="400" alt="自适应复古城市旅行海报——来源示例">](assets/p53-adaptive-vintage-city-travel-poster/source-example-02.jpg)

[<img src="assets/p53-adaptive-vintage-city-travel-poster/source-example-03.jpg" width="283" height="400" alt="自适应复古城市旅行海报——来源示例">](assets/p53-adaptive-vintage-city-travel-poster/source-example-03.jpg)

[<img src="assets/p53-adaptive-vintage-city-travel-poster/source-example-04.jpg" width="302" height="400" alt="自适应复古城市旅行海报——来源示例">](assets/p53-adaptive-vintage-city-travel-poster/source-example-04.jpg)

#### 👇 工作流

`城市名 + 风格参考图 → 复古旅行海报`

#### 🔖 完整提示词

```text
{
  "input": {
    "city_name": "{{USER_INPUT_CITY}}"
  },

  "reference_style": {
    "use_uploaded_reference_images": true,
    "reference_images_define": [
      "整体构图",
      "手工剪刻丝网印刷美学",
      "大胆的黑色图形剪影",
      "有限色板",
      "复古旅行海报气质",
      "粗粝油墨纹理",
      "略不完美的手工边缘",
      "超大城市字体",
      "分层地标布局",
      "底部交通元素",
      "奶油色/米白色纸张背景",
      "极简编辑构图"
    ],
    "do_not_copy": [
      "具体地标",
      "具体城市名",
      "具体交通工具",
      "具体配色组合",
      "完全相同的字体布局",
      "完全相同的地标位置"
    ]
  },

  "generation": {
    "type": "vintage_city_travel_poster",
    "aspect_ratio": "3:4",
    "resolution": "high",
    "orientation": "portrait",

    "city_adaptation": {
      "primary_rule": "所有内容都必须围绕用户输入的 city_name 重新设计。",
      "identify_city": true,
      "research_visual_identity": true,

      "landmarks": {
        "count": "4-7",
        "selection": "自动选择指定城市中最具辨识度且视觉特征鲜明的地标。",
        "prioritize": [
          "主要地标",
          "历史建筑",
          "现代建筑标志",
          "宗教或文化地标",
          "桥梁或纪念碑",
          "可辨识的天际线元素"
        ],
        "rendering": "将每个地标转化为简洁大胆的黑色丝网印刷剪影，同时保留其可辨识的建筑特征。"
      },

      "transportation": {
        "automatically_select": true,
        "instruction": "选择一种与指定城市高度相关的交通工具，例如出租车、有轨电车、公交车、地铁列车、嘟嘟车、缆车、人力车、经典汽车、渡轮或其他标志性本地交通工具。",
        "placement": "沿底部边缘放置一个大型前景元素",
        "style": "简化的复古丝网印刷插画"
      },

      "colors": {
        "automatically_adapt": true,
        "instruction": "根据城市的视觉形象、本地交通、旗帜、建筑或文化色彩，选择克制的 2–4 色配色。",
        "black": "占主导地位的图形油墨色",
        "background": "暖调做旧奶油色纸张",
        "accent_colors": "符合城市特色、色调柔和，绝不过度饱和"
      },

      "typography": {
        "text": "{{USER_INPUT_CITY}}",
        "case": "uppercase",
        "style": "大型、粗体、不规则的窄体展示字",
        "placement": "醒目地融入地标之间或地标后方",
        "texture": "粗糙印刷油墨",
        "alignment": "略不完美且富有有机感",
        "rule": "城市名称必须拼写完全正确且清晰可读。"
      },

      "secondary_text": {
        "enabled": false,
        "instruction": "不要添加随意的标语、日期、旅游宣传语、说明或额外可读文字。"
      },

      "local_details": {
        "automatically_adapt": true,
        "instruction": "加入能立即强化指定城市身份的细微视觉细节，同时避免使构图过于拥挤。"
      }
    },

    "composition": {
      "layout": "编辑设计风格的复古旅行海报",
      "landmarks": "围绕字体进行动态排列",
      "typography": "大型中央视觉锚点",
      "foreground": "一种标志性的城市交通工具",
      "depth": "带少量重叠的平面图形分层",
      "negative_space": "充足的奶油色负空间",
      "balance": "不对称但视觉均衡",
      "cropping": "允许选定地标或交通工具自然延伸至画面边缘"
    },

    "art_direction": {
      "medium": "手工丝网印刷/油毡版画风格的旅行海报",
      "visual_language": [
        "大胆剪影",
        "平面色块",
        "粗糙油墨边缘",
        "可见印刷颗粒",
        "细微油墨做旧",
        "轻微套色偏差",
        "手工瑕疵",
        "图形化编辑设计",
        "世纪中期旅行海报影响"
      ],
      "linework": "强劲、厚重、简化",
      "texture": "真实纸张颗粒与不均匀油墨覆盖",
      "finish": "呈现实体印刷作品质感，而不是数字化完美的矢量图"
    },

    "background": {
      "color": "暖象牙色/做旧奶油色",
      "texture": "细微天然纸张纤维",
      "pattern": "none",
      "gradient": false
    },

    "quality": {
      "photorealism": false,
      "vector_perfection": false,
      "digital_gloss": false,
      "clean_modern_ui": false,
      "high_detail": true,
      "print_ready_appearance": true
    }
  },

  "constraints": {
    "user_controls_only": [
      "city_name"
    ],
    "model_controls": [
      "地标选择",
      "地标布局",
      "交通工具",
      "配色",
      "本地视觉细节",
      "字体构图",
      "图形层级"
    ],
    "must_have": [
      "正确的城市名称",
      "该城市可辨识的地标",
      "具有城市特色的交通或出行元素",
      "暖奶油色纸张背景",
      "大胆的黑色丝网印刷形体",
      "大型城市字体",
      "复古手工印刷纹理",
      "统一的旅行海报构图"
    ],
    "avoid": [
      "来自其他城市的地标",
      "泛化建筑",
      "泛化旅游图像",
      "照片级写实渲染",
      "3D 渲染",
      "光滑渐变",
      "霓虹色",
      "现代企业海报设计",
      "随机文字",
      "拼错的城市名",
      "额外标语",
      "水印",
      "标志",
      "AI 瑕疵",
      "过于干净的矢量边缘"
    ]
  },

  "output_instruction": "创建一张代表 {{USER_INPUT_CITY}} 的完整复古丝网印刷旅行海报。保留所提供参考图的艺术语言与视觉克制感，但彻底重新设计地标、交通工具、强调色和本地细节，使其真实属于指定城市。"
}
```

<sub>(by [@Maercihh](https://x.com/Maercihh/status/2099757585264251102)) · [来源平台： X](https://x.com/Maercihh/status/2099757585264251102)</sub>

<a id="p51-rebel-streetwear-editorial-poster"></a>

### 📌 4.2. 叛逆街头时尚编辑海报

#### 👀 预览

[<img src="assets/p51-rebel-streetwear-editorial-poster/source-example-01.jpg" width="267" height="400" alt="叛逆街头时尚编辑海报——来源示例">](assets/p51-rebel-streetwear-editorial-poster/source-example-01.jpg)

#### 👇 工作流

`文字 → 时尚编辑海报`

#### 🔖 完整提示词

```text
创作一张超写实、高端编辑风格的时尚海报，主体是一位留着凌乱深棕色长发的年轻女性。她戴着窄框黑色太阳镜，身穿褪色蓝色牛仔夹克、白色修身短款上衣和宽松蓝色牛仔裤。

采用戏剧性的低机位视角捕捉她向前倾身、单手伸向镜头的瞬间。她的手靠近镜头，形成强烈透视与轻微运动模糊。她仰起头，神情自信而叛逆，头发随风自然飘动。

背景为复古混合媒介拼贴：带纹理的奶油色纸张底面，大面积做旧红色与橙色几何圆形和矩形，手绘黑白飞鸟、纤细植物枝条，以及克制的粗粝痕迹。

字体与平面设计：在左下区域加入原样的大号粗体白字“FEEL”，其下方加入原样的大号黑字“IT”。加入原样的小型编辑文字：“CHASE WHAT SETS YOUR SOUL ON FIRE”、“LIVE IN THE MOMENT. BE YOU. NO FILTER”和“KEEP GOING, KEEP GROWING.”。右侧加入竖排日文文字，以及纤细装饰线、抽象符号、条码图形、手写笔刷字和极简编辑细节。

配色：暖奶油色、做旧红色、橙色、黑色、白色与柔和牛仔蓝。加入复古纸张颗粒、丝网印刷纹理、褪色油墨、细微划痕和真实拼贴瑕疵。

构图：竖版时尚杂志封面，戏剧性低机位拍摄，主体位置富有动势，图形元素层层叠加，专业艺术指导，真实皮肤纹理，电影感照明，高级街头服饰编辑美学。

宽高比：2:3 竖版，超高细节，4K 照片级写实。
```

<sub>(by [@harboriis](https://x.com/harboriis/status/2099734295539790133)) · [来源平台： X](https://x.com/harboriis/status/2099734295539790133)</sub>

<a id="p50-minimal-watercolor-paper-cover"></a>

### 📌 4.3. 极简水彩纸面封面

#### 👀 预览

[<img src="assets/p50-minimal-watercolor-paper-cover/source-example-01.jpg" width="400" height="400" alt="极简水彩纸面封面——来源示例">](assets/p50-minimal-watercolor-paper-cover/source-example-01.jpg)

#### 👇 工作流

`参考图 → 水彩纸面封面插画`

#### 🔖 完整提示词

```text
## 指令
生成一幅单张水彩纸面封面插画。仅将所附参考图用于提取主体、轮廓、姿势、物体、颜色与画布比例。不要在画面中放置、拼贴、叠加、分割或附带原始照片。整幅画布都必须是插画。

## 画幅
准确匹配所附参考图的宽高比与方向。
参考图为横向时，插画也为横向。
参考图为竖向时，插画也为竖向。
参考图为正方形时，插画也为正方形。
一幅满版的手工纸张插画。
不采用上下分割。
不插入照片。
不采用双联画。
不添加黑边、白边或其他补边。

## 宽高比适配
输出画布必须继承参考图的尺寸关系。
重新构图，使提取出的元素有意识地占据同一比例的画布。
不要通过拉伸、压扁或填充画面来伪造其他格式。
不要把原照片中的空白边缘原样保留为无效空间。
把参考图的完整比例当作编辑页面使用：根据其特定宽度与高度来安排主体、少量辅助形状和纸张底色。

## 主体提取
研究所附参考图。
只保留：
- 最具辨识度的主体
- 必要的轮廓与比例
- 关键姿势或动作
- 重要物体
- 人物与物体之间的核心叙事关系

进行高度简化。
去除不必要的细节。
仅保留能够让人立即识别的视觉信息。

绝不把照片纹理、毛孔、镜头虚化或相机颗粒复制进插画。
绝不将照片重绘成一幅上色照片。
绝不让原始照片出现在画面中。

## 媒介
纸张上的极简手绘水彩。

使用：
- 细腻、略带不完美的手绘线条
- 透明水彩晕染
- 少量大胆、轮廓清晰的平涂色块
- 粗糙纸张纹理
- 可见的手工笔触
- 略不规则、富有有机感的边缘
- 轻微积色、水痕绽放与颜料颗粒
- 能体现真实手工感的细小瑕疵

主要插画主体应小巧且构图精心，约占画布的 20–35%。
在插画周围保留大量负空间，并依据参考图比例进行分配。

## 纸张底色
背景应主要呈现为：
- 粗糙白纸
- 暖调米白纸
- 淡色天然纸张
- 极简编辑类书籍封面纸

仅用少量线条或小型水彩色块暗示周围环境。
不要让完整场景铺满页面。
不要绘制照片式背景。

## 色彩
直接从所附参考图中提取主色。
将色板压缩为不超过 4 种主要颜色。
色彩保持克制、高雅、和谐。
使用大胆但可控的平涂水彩色块。
避免过多色彩变化。
保留细腻纸纹与手工笔触质感。
插画应像是对参考图的简化水彩诠释，而不是复制品。

## 字体
在自然适合时，可以加入少量简单文字。
可选元素包括：短标题、关键词、物体名称、地点、年份、数字或短语。
文字应极少、低调，并具有编辑设计感。
将文字放置在由参考图比例形成的负空间中。
若文字与主体并不自然契合，不要强行加入。
无标志。无水印。无描述图片内容的说明文字。

## 视觉语言
安静。诗意。精致。极简。纯真。松弛。艺术化。富有思考。高辨识度。高级。
艺术书封面。独立出版。当代编辑设计。富有思考的绘本。

## 负面提示词
画面中不得出现原始照片，不采用分割布局，不采用上方照片/下方绘画，不采用拼贴，不采用照片蒙太奇，不附带参考图，不使用照片级写实，不呈现相机观感，不使用镜头虚化，不采用电影感肖像，不进行美颜修饰，不添加额外人物，不追求强身份写实，不使用拥挤构图，不采用满版绘制场景，不强制 3:4，不强制正方形，不加上下黑边，不加黑条，不拉伸或压扁图画，不照搬照片中的无效边缘，不堆砌过多细节，主要颜色不超过四种，不使用喧闹字体，不添加标志，不添加水印，不添加 HUD。
```

<sub>(by [@impaulxyz](https://x.com/impaulxyz/status/2099770445595545766)) · [来源平台： X](https://x.com/impaulxyz/status/2099770443808821443) · 灵感来自 [@icreatelife](https://x.com/icreatelife/status/2099343607492702258)</sub>

<a id="p48-misty-autumn-lakeside-at-sunrise"></a>

### 📌 4.4. 晨曦薄雾中的秋日湖畔

#### 👀 预览

[<img src="assets/p48-misty-autumn-lakeside-at-sunrise/source-example-01.jpg" width="400" height="224" alt="晨曦薄雾中的秋日湖畔——来源示例">](assets/p48-misty-autumn-lakeside-at-sunrise/source-example-01.jpg)

#### 👇 工作流

`文字 → 风景图`

#### 🔖 完整提示词

```text
一幅宁静的粉彩色调风景：日出时分，静谧湖畔上方浮着柔和薄雾。前景是一片鲜艳草甸，雏菊、羽扇豆等野花一路延伸至一簇秋叶斑斓的白桦树。薄雾笼罩的湖面彼岸，温馨的木屋坐落在更多彩色树木之间，沐浴于朝阳温柔而温暖的光芒中。整体风格梦幻细腻，唤起平和而怀旧的情绪。
```

<sub>(by [@churvikv](https://x.com/churvikv/status/2099793774700376379)) · [来源平台： X](https://x.com/churvikv/status/2099793774700376379)</sub>

<a id="p44-halftone-travel-collage-poster"></a>

### 📌 4.5. 半色调旅行拼贴海报

#### 👀 预览

[<img src="assets/p44-halftone-travel-collage-poster/source-example-01.jpg" width="319" height="400" alt="半色调旅行拼贴海报——来源示例">](assets/p44-halftone-travel-collage-poster/source-example-01.jpg)

[<img src="assets/p44-halftone-travel-collage-poster/source-example-02.jpg" width="319" height="400" alt="半色调旅行拼贴海报——来源示例">](assets/p44-halftone-travel-collage-poster/source-example-02.jpg)

[<img src="assets/p44-halftone-travel-collage-poster/source-example-03.jpg" width="319" height="400" alt="半色调旅行拼贴海报——来源示例">](assets/p44-halftone-travel-collage-poster/source-example-03.jpg)

#### 👇 工作流

`人像参考图 → 半色调拼贴海报`

#### 🔖 完整提示词

```text
将这张人像照片转换为一张高品质的半色调旅行拼贴海报。每张上传照片输出一张海报——绝不将多张照片合并到同一画面中。
画幅

3:4 竖版画布。划分为两个大致等高的区域——上方是真实照片，下方是印刷拼贴——中间用一条干净、锐利的水平线分隔。不要为强行符合比例而拉伸、扭曲或移动人物。
上半部分——真实照片

忠实保留原照片：相同的身份、面容、表情、姿势、双手、服装、随身物品、背景结构、自然光影和原有色彩情绪。只添加轻微的高级调色与极淡的胶片颗粒。不要重绘或重新演绎人物。
下半部分——印刷重构

使用统一的暖灰色旧纸背景。将同一个人物重构为印刷拼贴：撕裂的照片切片 + 等宽 ASCII 字符区域 + 复印半色调网点。

保持面容、双手、发型、服装和一件标志性物品可辨识——即使画面被拆解，人物身份仍须保留。
带撕边的照片碎片承载面部与关键结构线；织物、阴影和背景向外消散成 ASCII 字符、黑色半色调网点及破碎的印刷颗粒。
纹理：粗糙的白色纸纤维边缘、轻微印刷套色偏移、旧纸污渍、少量裁切标记，以及一条克制的红色校准条。
颜色：暖灰纸色 + 黑色油墨 + 照片自身柔和的原有色彩 + 唯一的红色点缀。不要完全去色。
人物约占画面宽度的 60–88%——始终保留 22–38% 的纸面为空白、不作处理，使其呈现档案印刷品的感觉，而非塞满内容的终端屏幕。
根据照片主题添加一个清晰可读的等宽字体标题，再加入原样文字 "REC. STUDY 01" 和一句简短的观察性说明。少量散落的 ASCII 字符可以沿人物边缘形成纹理，但仅作纹理使用——绝不用来伪造身体细节或编造参数。

氛围

早期数字系统、模拟复印、地下独立杂志与现代旅行编辑视觉相结合。人物应像正从画面中浮现——半是照片、半是字符、半是印刷——克制、富有档案感，略带实验气质。
避免

纯黑终端背景、密集代码墙、赛博朋克霓虹、完全遮蔽的面孔、毫无意义的随机符号、编造的技术读数、乱码假文字、作者署名、品牌标志、二维码、水印。
```

<sub>(by [@ShamiWeb3](https://x.com/ShamiWeb3/status/2099316312426381491)) · [来源平台： X](https://x.com/ShamiWeb3/status/2099316312426381491)</sub>

<a id="p43-foodie-cities-in-sculptural-typography"></a>

### 📌 4.6. 美食城市雕塑字形

#### 👀 预览

[<img src="assets/p43-foodie-cities-in-sculptural-typography/source-example-01.jpg" width="400" height="225" alt="美食城市雕塑字形——来源示例">](assets/p43-foodie-cities-in-sculptural-typography/source-example-01.jpg)

#### 👇 工作流

`地点或文化参数 → 雕塑字形图片`

#### 🔖 完整提示词

```text
WITH identity AS (     SELECT        derive_display_name([PLACE_OR_CULTURE])          AS display_name,         infer_signature_foods([PLACE_OR_CULTURE])        AS foods,         infer_signature_materials([PLACE_OR_CULTURE])    AS materials,         infer_landmarks([PLACE_OR_CULTURE])              AS landmarks,         infer_objects([PLACE_OR_CULTURE])                AS objects,         infer_palette([PLACE_OR_CULTURE])                AS palette,         infer_three_values([PLACE_OR_CULTURE])           AS values,         infer_keyword_stack([PLACE_OR_CULTURE], 4)       AS keywords ),  glyph_assignment AS (     SELECT        glyph,         argmax(             source_item,             shape_match(glyph, source_item)             * cultural_relevance(source_item)             * visual_uniqueness(source_item)         ) AS source_material     FROM letters(display_name)     CROSS JOIN cultural_pool(foods, materials, objects) )  SELECT render FROM editorial_travel_stilllife_archive WHERE hero_typography = build_3d_word(     display_name,     material_per_glyph = glyph_assignment.source_material ) AND foreground = infer_culinary_stilllife([PLACE_OR_CULTURE]) AND background = infer_soft_focus_architecture([PLACE_OR_CULTURE]) AND base = 'premium sculptural plinth' AND base_caption = join(values, ' • ') AND side_stack = keywords AND lighting = 'warm sunlit premium editorial' AND styling = 'travel magazine × culinary still life × crafted typography' ORDER BY    cultural_specificity DESC,     glyph_legibility DESC,     material_variety DESC,     tactile_realism DESC,     composition_balance DESC LIMIT 1;
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2099299591485354266)) · [来源平台： X](https://x.com/Gdgtify/status/2099299591485354266)</sub>

<a id="p40-desert-motorcycle-editorial-poster"></a>

### 📌 4.7. 沙漠摩托车杂志海报

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

<sub>(by [Comfy-Org](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_sunburst_t2i.json)) · [来源平台： GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_sunburst_t2i.json) · 参考图改编：SeeAPI</sub>

<a id="p39-neon-motorsport-poster"></a>

### 📌 4.8. 霓虹赛车海报

#### 👀 预览

[<img src="assets/p39-neon-motorsport-poster/source-example-01.webp" width="400" height="400" alt="霓虹赛车海报——来源示例">](assets/p39-neon-motorsport-poster/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
1:1 正方形海报，极近距离、高对比拍摄赛车前鼻、空气动力学翼片与轮辋，在鲜红运动模糊和明亮橙光中冲破黑暗。“GPT IMAGE 2.5”以明亮霓虹橙色直接投影在车身上，与前翼和轮辋重叠。强烈红黑配色、电影感低调照明、锐利反射、戏剧性低机位、浅景深和高速赛车美学。不出现侧栏、额外 UI 面板、技术符号、条形码，除“GPT IMAGE 2.5”外不出现其他文字。
```

<sub>(by [Comfy-Org](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_flare_t2i.json)) · [来源平台： GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_25_flare_t2i.json)</sub>

<a id="p34-woodland-clearing"></a>

### 📌 4.9. 林间空地

#### 👀 预览

[<img src="assets/p34-woodland-clearing/source-example-01.jpg" width="400" height="300" alt="林间空地——来源示例">](assets/p34-woodland-clearing/source-example-01.jpg)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
林间空地照片，有大量绿色枝叶，高度细致
```

<sub>(by [@mark_k](https://x.com/mark_k/status/2097411028510179759)) · [来源平台： X](https://x.com/mark_k/status/2097411028510179759)</sub>

<a id="p32-dog-compositing-into-a-street-scene"></a>

### 📌 4.10. 将狗合成至街道场景

#### 👀 预览

[<img src="assets/p32-dog-compositing-into-a-street-scene/source-example-01.jpg" width="400" height="313" alt="将狗合成至街道场景——来源示例">](assets/p32-dog-compositing-into-a-street-scene/source-example-01.jpg)

#### 👇 工作流

`街道场景 + 狗的参考图 → 合成图片`

#### 🔖 完整提示词

```text
将第二张图中的狗放入图片 1 的场景中，紧挨着那位女性，使用相同的照明风格、构图与背景。其他一切保持不变。
```

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcj1ud/gpt_image_25_prompt_guide_2026_23_9_official_edit/)</sub>

<a id="p28-fashion-movements-across-four-decades"></a>

### 📌 4.11. 四个年代的时尚潮流

#### 👀 预览

[<img src="assets/p28-fashion-movements-across-four-decades/source-example-01.jpg" width="400" height="225" alt="四个年代的时尚潮流——来源示例">](assets/p28-fashion-movements-across-four-decades/source-example-01.jpg)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
2×2 网格，分别展示四个不同年代的时尚潮流，16:9 class EditorialPoster:     def __init__(self, topic):         self.topic = topic         self.resolution = self.resolve_auto_fields(topic)              def resolve_auto_fields(self, topic):         # Module 2: Copy & Facts         self.title = generate_title(topic, max_words=5)         self.tagline = generate_tagline(topic, min_words=3, max_words=8)         self.labels = extract_key_points(topic, count=6-12, relationship="components") # principles/stages/types                  # Module 3: The Surreal Character Engine         self.mechanism = infer_verb(topic) # e.g., "filtering", "branching", "accumulating"         self.base_form = select_organism(self.mechanism) # human, animal, or object         # CRITICAL: Transformation must be structural, not just accessories         self.transformation = invent_structural_alteration(self.base_form, self.mechanism)         self.pose = select_pose(topic, attitude="intriguing_uncanny")                  # Module 5: Geometry & Palette         self.geometry = select_geometric_family(topic) # rays, arcs, ribbons, grids         self.palette = derive_accent_colors(topic, count=2-6, mood="flat_matte_weathered")      def verify_character_logic(self):         # The "Thumbnail & Concept" Check         assert is_structural(self.transformation), "Module 3: Must be anatomy/proportion, not accessories."         assert fits_sentence(self.transformation, self.mechanism), "Module 3: Logic check failed."         assert visible_at_thumbnail(self.transformation), "Module 3: Must read at small scale."         assert not is_generic_cute_scary(self.pose), "Module 3: Avoid default emotional tropes."      def render(self):         self.verify_character_logic()                  # Module 1 & 6: Style Kernel         canvas = Canvas(aspect="1:1", bg="warm_ivory", texture="subtle_analog_grain")                  # Hero: Grayscale, sculptural shading, stippling/halftone         hero = render_grayscale_sculptural(self.base_form, self.transformation, self.pose,                                             shading="fine_stippling", texture="tactile_print")                  # Module 4: Adaptive Layout         layout = adaptive_composition(             hero=hero,              title=self.title, # Oversized, black, condensed, uppercase             labels=self.labels, # Compact, high contrast             geometry=self.geometry, # Connects hero to info             palette=self.palette # Flat, matte accents         )                  return canvas.compose(layout, typography="extreme_contrast_hierarchy")  EditorialPoster($ TOPIC).render()
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2098228786156196084)) · [来源平台： X](https://x.com/Gdgtify/status/2098228786156196084)</sub>

<a id="p25-three-panel-dialogue-comic"></a>

### 📌 4.12. 三格对话漫画

#### 👀 预览

[<img src="assets/p25-three-panel-dialogue-comic/source-example-01.webp" width="400" height="226" alt="三格对话漫画——来源示例">](assets/p25-three-panel-dialogue-comic/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
三格条漫，手写对话气泡，墨线与平涂色彩
```

<sub>(收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p09-paper-folk-story"></a>

### 📌 4.13. 剪纸民间故事

#### 👀 预览

[<img src="assets/p09-paper-folk-story/azed-ai-paper-folk-story.webp" width="400" height="267" alt="来自 azed_ai 原帖的提灯剪纸角色">](https://x.com/azed_ai/status/2096191635348705726)

#### 👇 工作流

`文字 → 剪纸角色图片`

#### 🔖 完整提示词

```text
剪纸动画风格的 [subject] 正在 [simple action]，全身角色，多层纸片形状，手工纸纹理，可见裁切边缘，层间柔和阴影，平涂的彩色纸张色调，略带不完美的手作细节，极简纸张拼贴场景，迷人的民间故事美学，轻柔的定格动画感，诗意的儿童绘本氛围，干净的白色背景
```

<sub>(作者：@azed_ai) · [来源平台： X](https://x.com/azed_ai/status/2096191635348705726) · [来源平台： X](https://x.com/azed_ai/status/2096191635348705726)</sub>

<a id="p07-paper-cut-storybook-scene"></a>

### 📌 4.14. 剪纸绘本场景

#### 👀 预览

[<img src="assets/p07-paper-cut-storybook/paper-cut-character-result.png" width="400" height="400" alt="温馨房间中的多层剪纸猫">](assets/p07-paper-cut-storybook/paper-cut-character-result.png)

#### 👇 工作流

`文字／可选角色参考图 → 剪纸图片`

#### 🔖 完整提示词

```text
制作完全由多层剪纸构成的绘本场景，地点为 [environment]。由 [character description] 定义的角色在 [focal object] 附近做出 [anatomy-appropriate action]。如果上传了角色参考图，在将外观转化为剪纸时保留其身份、身体结构、比例、颜色和独特特征。

表现可见纸纤维、利落的裁切边缘、轻微弯折的纸片，以及层与层之间的真实阴影。配色限定为 [color palette]。像从正面观看的浅景深舞台布景一样构图，前景、中景和背景明确。不出现文字、亮面塑料或照片般写实的表面纹理。正方形构图。
```

<sub>(作者：SeeAPI)</sub>

<a id="p05-editorial-poster-with-exact-copy"></a>

### 📌 4.15. 准确文案的杂志风海报

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

<sub>(作者：SeeAPI)</sub>

<a id="p03-miniature-world-in-an-everyday-object"></a>

### 📌 4.16. 日常物品中的微缩世界

#### 👀 预览

[<img src="assets/p03-miniature-world/miniature-world-result.png" width="400" height="400" alt="树皮容器内的微缩林间村庄">](assets/p03-miniature-world/miniature-world-result.png)

#### 👇 工作流

`文字 → 微缩场景图片`

#### 🔖 完整提示词

```text
在打开的 [everyday container] 内构建微缩 [world or scene theme]，容器放在真实的 [supporting surface] 上。包含 [main structures]、[landscape details] 和 [focal feature]，所有内容在物理上都位于容器内部。容器内壁构成背景，材质符合其真实结构。

从斜上方四分之三视角展示整个容器。通过真实接缝、边缘、五金配件，以及旁边实际尺寸的 [scale reference object]，明确微缩比例关系。采用 [lighting mood]、真实微缩材质和浅景深，同时保持场景清晰可读。不出现悬浮建筑或文字。横幅构图。
```

<sub>(作者：SeeAPI)</sub>

<a id="p62-minimal-chinese-roof-poster"></a>

### 📌 4.17. 新中式屋檐与雀鸟极简海报

#### 👀 预览

[<img src="assets/p62-minimal-chinese-roof-poster/source-example-01.jpg" width="225" height="400" alt="新中式屋檐与雀鸟极简海报——来源示例">](assets/p62-minimal-chinese-roof-poster/source-example-01.jpg)

#### 👇 工作流

`文字 → 留有标题区的新中式极简海报`

#### 🔖 完整提示词

```text
主题方向：东方禅意极简封面海报
风格分支：女性审美新中式型
主体内容：一位古风女子站在浅色屋脊下方，抬眼看一只停在檐角的小雀
情绪母题：灵动、安静、东方趣味感
场景与意象：月牙白屋墙、海棠红檐角点缀、松针绿植物、小雀、女子
构图与空间：9:16 竖版构图，屋檐斜向切入上方，人物位于下方偏一侧，上方大片浅色墙面形成标题区
色彩控制：月牙白作为背景和墙面基底，海棠红用于檐角和局部点睛，松针绿用于少量植物，小雀保持自然浅棕色；避免整图偏红或偏绿
光线与质感：明亮自然光，画面干净，边缘清楚，轻平面新中式海报感
画幅比例：9:16
补充要求：整体要有趣味但仍极简，小雀只作为灵动点，不要把背景做复杂，画面留白处配上合适的艺术文字
```

<sub>(by [@liyue_ai](https://x.com/liyue_ai/status/2100097638326780122)) · [来源平台： X](https://x.com/liyue_ai/status/2100097638326780122) · 英文由 SeeAPI 翻译</sub>

<a id="p72-spring-ridge-leaf-collage-slice"></a>

### 📌 4.18. 春日山脊叶片拼贴切片

#### 👀 预览

[<img src="assets/p72-spring-ridge-leaf-collage-slice/source-example-01.webp" width="225" height="400" alt="春日山脊叶片拼贴切片——来源示例">](assets/p72-spring-ridge-leaf-collage-slice/source-example-01.webp)

#### 👇 工作流

`文字 → 透明背景叶片拼贴切片`

#### 🔖 完整提示词

```text
一幅东方极简插画，形成一块形状不规则、悬浮且没有任何背景的场景切片：切片周围的区域完全透明（alpha = 0），既不是白色或彩色，也没有表面或棋盘格图案。切片内部是一幅完整的小型春日场景：层叠山脊由成千上万片鲜绿色的小叶片密集拼贴而成；切片内部的奶油色纸张底面留出宁静的负空间；两个用墨线勾勒的微小人物沿着山脊行走，旁边只有一棵小树；较高处放置一轮扁平的珊瑚色太阳圆盘，柔和雾带在山脊之间飘过。边界呈现拼贴逐渐散尽的样子：叶片碎屑逐渐稀疏并散落，纸边变得参差不齐，几簇叶片延伸到透明区域，使作品中心看起来已经完成、边缘仍未完成。

切片本体完整呈现，四周都有清晰的透明边距；透明区域均匀延伸到画布的四条边。柔和均匀的光线，细微的叶片浮雕感仅存在于切片内部。任何地方都没有文字；所有可能写字的表面都保持空白。9:16 竖版人像构图。
```

<sub>(by [@rafael_nascimento](https://alosem.com/i/spring-ridge-walk-leaf-collage-slice-1d5e0d44)) · [来源平台： Alosem](https://alosem.com/i/spring-ridge-walk-leaf-collage-slice-1d5e0d44)</sub>

<a id="p73-pressed-flower-wren-cutout"></a>

### 📌 4.19. 压花鹪鹩透明剪影

#### 👀 预览

[<img src="assets/p73-pressed-flower-wren-cutout/source-example-01.webp" width="400" height="225" alt="压花鹪鹩透明剪影——来源示例">](assets/p73-pressed-flower-wren-cutout/source-example-01.webp)

#### 👇 工作流

`文字 → 透明背景压花鹪鹩剪影`

#### 🔖 完整提示词

```text
一件压花拼贴艺术作品（押花，oshibana），形成一块形状不规则、悬浮且没有任何背景的场景切片：切片周围的区域完全透明（alpha = 0），既不是白色或彩色，也没有表面或棋盘格图案。切片内部是一幅完全由真实压花、花瓣、叶片与茎秆构成的完整小场景：一只小鹪鹩停在一根纤细的真实压制树枝上；它的身体由层叠的锈红色、赭色和灰玫瑰色花瓣构成，胸部是奶油色花瓣，翅膀和尾巴由苔绿色叶片制成，眼线是一根细小的干草；树枝保留天然不规则的树皮纹理。每个元素都保持压制植物材料的真实特征：不规则的天然花瓣边缘、纤细叶脉和轻巧的层叠翘起。切片边缘像压花摆设自然收尾那样：几片散落花瓣、微小叶片碎屑和一朵小小的干花散到透明区域，让作品中心显得完整，边缘仍带未完的感觉。

切片本体完整呈现，四周都有清晰的透明边距；透明区域均匀延伸到画布的四条边。柔和均匀的光线，细腻且有立体感的花瓣阴影仅存在于切片内部。任何地方都不要出现文字。16:9 横幅构图。
```

<sub>(by [@rafael_nascimento](https://alosem.com/i/pressed-flower-wren-on-twig-slice-4712aff7)) · [来源平台： Alosem](https://alosem.com/i/pressed-flower-wren-on-twig-slice-4712aff7)</sub>

<a id="-home--interior-design"></a>

## 🏡 家居与室内设计

<a id="p42-bedroom-redesign-from-your-photo"></a>

### 📌 5.1. 照片 → 卧室改造

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

<sub>(作者：SeeAPI)</sub>

<a id="-infographics--practical-design"></a>

## 📊 信息图与实用设计

<a id="p30-spanish-infographic-translation"></a>

### 📌 6.1. 信息图翻译为西班牙语

#### 👀 预览

[<img src="assets/p30-spanish-infographic-translation/source-example-01.jpg" width="400" height="313" alt="信息图翻译为西班牙语——来源示例">](assets/p30-spanish-infographic-translation/source-example-01.jpg)

#### 👇 工作流

`信息图参考 → 西班牙语信息图`

#### 🔖 完整提示词

```text
将信息图中的文字翻译为西班牙语。不改变图像的任何其他部分。
```

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcj1ud/gpt_image_25_prompt_guide_2026_23_9_official_edit/)</sub>

<a id="p26-ornate-award-certificate"></a>

### 📌 6.2. 华丽获奖证书

#### 👀 预览

[<img src="assets/p26-ornate-award-certificate/source-example-01.webp" width="400" height="226" alt="华丽获奖证书——来源示例">](assets/p26-ornate-award-certificate/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
获奖证书，华丽边框，以书法字体书写姓名和日期
```

<sub>(收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p24-boarding-pass-layout"></a>

### 📌 6.3. 登机牌版式

#### 👀 预览

[<img src="assets/p24-boarding-pass-layout/source-example-01.webp" width="400" height="225" alt="登机牌版式——来源示例">](assets/p24-boarding-pass-layout/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
登机牌效果图，乘客、登机口、座位和时间在干净的网格中清晰可读
```

<sub>(收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p23-national-park-trail-map"></a>

### 📌 6.4. 国家公园步道地图

#### 👀 预览

[<img src="assets/p23-national-park-trail-map/source-example-01.webp" width="400" height="225" alt="国家公园步道地图——来源示例">](assets/p23-national-park-trail-map/source-example-01.webp)

#### 👇 工作流

`文字 → 图片`

#### 🔖 完整提示词

```text
国家公园步道地图海报，六条路线标注名称与距离
```

<sub>(收录自 [SeeAPI](https://www.aiimage.net/prompts/)) · [来源平台： SeeAPI](https://www.aiimage.net/prompts/)</sub>

<a id="p20-cellular-respiration-classroom-diagram"></a>

### 📌 6.5. 课堂细胞呼吸示意图

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="p19-farmers-market-mobile-app-mockup"></a>

### 📌 6.6. 农夫市集手机应用效果图

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="p14-automatic-coffee-machine-infographic"></a>

### 📌 6.7. 全自动咖啡机信息图

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

<sub>[来源平台： Reddit](https://www.reddit.com/r/ChatGPT/comments/1wcatvx/gpt_image_25_prompt_guide_2026_13_8_rules_and_8/)</sub>

<a id="-5-creative-cases"></a>

<a id="-gif--video-workflows"></a>

## 🎬 GIF 与视频工作流

<a id="c01-pixel-art-character-gif-by-seeapi"></a>

### 📌 7.1. 像素角色 GIF

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


**步骤 2 — 精灵图 → GIF**

```text
将所附 4×4 角色精灵图制作成动画 GIF。使用 Python 和 Pillow 按从左到右、从上到下的顺序提取全部 16 格。检查姿势，从预备动作、标志性动作到恢复，选择连贯的动作序列；只有在能改善连续性时才调整帧顺序。

去掉每个角色周围多余的空白，不裁切耳朵、肢体、尾巴或道具。各帧保留角色原有大小和比例。使用同一画布，将每帧角色居中；画布大小以最大姿势为准，并保留少量一致的安全边距。不单独缩放某帧来填满画布。

保留像素画风和白色背景。使用共享调色板，不抖色、不平滑、不虚构中间姿势。调整帧时长，使动作清楚，最后一帧自然回到第一帧。导出无限循环 GIF。逐帧检查裁切与对齐，检查循环衔接，提供 GIF 和可复现的 Python 脚本。报告使用的帧顺序、尺寸和时长，并指出需要修改精灵图才能弥补的动作缺口。
```

<sub>(作者：SeeAPI)</sub>

<a id="c02-clay-stop-motion-fishing-for-a-star-by-seeapi-inspired-by-charlie-guo"></a>

### 📌 7.2. 陶土定格动画：钓起一颗星星

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


**步骤 2 — 陶土风格图 → 帧表**

```text
使用上传的陶土风格图片作为严格的身份、材质、布景、照明和机位参考。制作一张正方形 4×4 帧表，恰好包含十六个等大的正方形帧，按阅读顺序排列，无格间空隙、网格线、标签或文字。

表现动作：[simple action]。第 1–4 帧建立起始姿势与预备动作；第 5–8 帧开始主要运动；第 9–12 帧展示动作高潮；第 13–16 帧恢复并趋向起始姿势，形成循环。采用不同、递进且符合身体结构的姿势，轮廓发生变化。参考角色的物种、比例、服装、颜色和道具保持不变。不虚构额外肢体、角色或道具。

每格保留同一固定机位、一致主体大小、固定布景位置、背景、照明与场景几何。运动元素位于每格内部，并留少量安全边距。保持物理接触和对道具的连续握持。保留陶土触感、手作表面瑕疵和轻微阶跃式定格感。第 16 帧应自然衔接第 1 帧。不出现相机运动、运动模糊、重复待机帧或变化的场景。
```


**步骤 3 — 帧表 → GIF**

```text
使用 Python 和 Pillow 将所附 4×4 定格动画帧表制作成循环 GIF。按从左到右、从上到下的顺序分割成 16 个等大帧。如果图片尺寸不能被四整除，对单元格边界取整，并保持统一裁切尺寸，必要时最多裁去一个边缘像素。

每帧保留完整微缩场景。使用同一裁切区域，保持原图比例。不按企鹅轮廓裁切，也不将其单独重新居中：冰洞、地平线和地面必须固定。不添加相机运动、插值姿势、光流或交叉淡化。

使用共享的 256 色调色板，不抖色。以每帧 140 毫秒为起点，在揭示动作时稍作停留，并在循环边界短暂停顿。除非姿势明显需要调整，否则保留原顺序。导出无限循环 GIF，并提供可复现脚本，包含准确帧顺序与时长。

检查角色、钓竿、鱼线、星星、冰洞和首尾衔接。如实报告可见漂移或缺失动作；若源帧需修正，说明应重新生成哪些内容，不将 GIF 描述为完美无缝。
```

<sub>(作者：SeeAPI；灵感来源：[Charlie Guo](https://x.com/charlierguo/status/2097399137142772071)) · [来源平台： X](https://x.com/charlierguo/status/2097399137142772071)</sub>

<a id="c04-character-to-storyboard-to-film-by-seeapi-inspired-by-elcine"></a>

### 📌 7.3. 角色设定 → 分镜 → 短片

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

<sub>(作者：SeeAPI；灵感来源：[el.cine](https://x.com/EHuanglu/status/2097519538632024103)) · [来源平台： X](https://x.com/EHuanglu/status/2097519538632024103)</sub>

<a id="c05-distant-observer-a-robot-in-the-rain-by-seeapi-inspired-by-pablo-prompt"></a>

### 📌 7.4. 远景旁观：雨中的机器人

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

<sub>(作者：SeeAPI；灵感来源：[Pablo Prompt](https://x.com/pabloprompt/status/2097382752622436744)) · [来源平台： X](https://x.com/pabloprompt/status/2097382752622436744)</sub>

<a id="c06-frosted-glass-poster-to-360-orbit-by-seeapi"></a>

### 📌 7.5. 磨砂玻璃海报 → 360° 环绕视频

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

<sub>(作者：SeeAPI)</sub>

<a id="-sources-reuse--maintenance"></a>

## 📝 来源、使用与维护

本仓库包含 SeeAPI 原创、外部收录及改编提示词。每条案例在完整提示词下方标明作者和来源，并按实际情况注明翻译或改编署名。

各案例的使用条款与示例图片来源，详见 [来源与权利说明](docs/sources-and-rights.md)。

由 SeeAPI 持续维护，同步更新中英文提示词与示例。**现阶段暂不开放外部投稿。**

<a id="-acknowledgments"></a>

## 🙏 致谢

- [YouMind — Awesome Seedance 2.0 Prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts): 为本仓库的内容组织和精选示例提供灵感。

- [ZeroLu — Awesome Nano Banana Pro](https://github.com/ZeroLu/awesome-nanobanana-pro): 为本仓库按类别组织和展示案例的方式提供参考。
