# GPT Image 2.5 精选提示词库 🎨

[English](README.md) | [简体中文](README_zh.md)

**由 SeeAPI 精选的创意图像提示词与工作流。**

探索 GPT Image 2.5 在角色贴纸、产品视觉、微缩世界、GIF 素材和定格动画场景中的创意玩法。复制提示词，替换为自己的内容，尝试新的创作方向。

本仓库将持续更新提示词示例、生成图片和实用复现说明。

**5 个创意工作流 · 97 条独立提示词 · 更新于 2026 年 9 月 23 日**

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

<a id="p77-natural-bedroom-ugc-selfie"></a>

### 📌 1.26. 自然卧室 UGC 自拍

#### 👀 预览

[<img src="assets/p77-natural-bedroom-ugc-selfie/source-example-01.jpg" width="300" height="400" alt="自然卧室 UGC 自拍——来源示例 1">](assets/p77-natural-bedroom-ugc-selfie/source-example-01.jpg)

#### 👇 工作流

`文字 → 自然卧室 UGC 自拍`

#### 🔖 完整提示词

```text
{
  "prompt_type": "photorealistic_female_ugc",
  "subject": {
    "person": "20 多岁的白人成年女性",
    "appearance": "天生有吸引力、有亲和力且平易近人",
    "expression": "真实、自发、自然",
    "body_language": "放松且不摆姿势",
    "skin": "真实的白皙至浅色皮肤，毛孔可见，纹理自然，有细微的瑕疵"
  },
  "scene": {
    "environment": "现实的日常场景",
    "background": "具有自然细节和微妙缺陷的居住环境",
    "atmosphere": "休闲、个性、不做作"
  },
  "clothing": {
    "style": "休闲日常服装",
    "appearance": "现代、舒适、有亲和力",
    "texture": "逼真的织物褶皱和皱纹",
    "branding": "没有可见的徽标或可识别的品牌"
  },
  "hair": {
    "style": "自然现代的发型",
    "texture": "真实的单根发丝",
    "appearance": "稍有不完美，排列自然"
  },
  "camera": {
    "device": "现代智能手机",
    "perspective": "自然智能手机视角",
    "framing": "中景特写或中景",
    "composition": "手持取景略有缺陷",
    "focus": "自然智能手机自动对焦",
    "image_quality": "高分辨率智能手机摄影",
    "lens": "自然智能手机广角镜头"
  },
  "lighting": {
    "source": "自然可用光",
    "quality": "柔软而真实",
    "shadows": "自然定向阴影",
    "avoid": [
      "演播室灯光",
      "专业美容灯光",
      "戏剧性的电影灯光"
    ]
  },
  "ugc_characteristics": {
    "authenticity": "极高",
    "style": "原始、随意、自发且相关",
    "camera_feel": "手持智能手机捕捉",
    "commercial_feel": "最小的",
    "social_media_feel": "原生于 TikTok 和 Instagram",
    "imperfections": "取景、灯光和环境中微妙的自然缺陷"
  },
  "realism": {
    "skin": "逼真的",
    "anatomy": "准确的人体解剖学",
    "hands": "现实的手和手指"
  },
  "negative_prompt": [
    "产品",
    "产品包装",
    "标志",
    "品牌名称",
    "广告",
    "商业摄影",
    "工作室摄影",
    "时尚社论",
    "CGI",
    "3D渲染",
    "卡通片",
    "日本动画片",
    "塑料皮",
    "蜡质皮肤",
    "不切实际的解剖学",
    "额外的手指",
    "变形的手",
    "文本",
    "字幕",
    "水印",
    "图形",
    "人工摆姿势"
  ],
  "final_generation_instruction": "生成一张逼真的 UGC 风格的白人成年女性图像，看起来就像 TikTok 或 Instagram 上真实的智能手机截图。让她感觉自己是一个真正的创造者，而不是一个模特。优先考虑自然的面部表情、真实的皮肤纹理、可信的解剖结构、休闲服装、自然光线、不完美的手持取景和居住环境。最终的图像应该感觉自然、亲切，像真实的社交媒体内容。请勿包含任何产品、品牌、徽标、广告图形或商业元素。"
}
```

<sub>(by [@Daniloecom](https://x.com/Daniloecom/status/2101403775164674440)) · [来源平台： X](https://x.com/Daniloecom/status/2101403775164674440)</sub>

<a id="p78-candid-gym-deadlift-photo"></a>

### 📌 1.27. 健身房硬拉抓拍

#### 👀 预览

[<img src="assets/p78-candid-gym-deadlift-photo/source-example-01.jpg" width="267" height="400" alt="健身房硬拉抓拍——来源示例 1">](assets/p78-candid-gym-deadlift-photo/source-example-01.jpg)

#### 👇 工作流

`文字 → 健身房训练抓拍`

#### 🔖 完整提示词

```text
{
  "prompt": {
    "type": "ultra_photorealistic_lifestyle_fitness_photography",
    "objective": "生成一张极其逼真的高分辨率健身照片，展示一位虚构的年轻成年女性在真实的当代健身房内锻炼的情况。图像应该给人自然性感、自信和女性化的感觉，而不是做作的、露骨的或做作的。它必须看起来像一张真正的智能手机在锻炼期间随意拍摄的照片，而不是人工智能生成的艺术品、CGI、商业健身广告或过度修饰的照片。优先考虑可信的解剖结构、不完美的自然皮肤、真实的织物行为、真实的健身房照明、微妙的不对称、物理正确的设备和普通的摄影缺陷。",
    "image_format": {
      "orientation": "肖像",
      "aspect_ratio": "大约2:3",
      "framing": "全身至四分之三的垂直健身照片",
      "resolution": "非常高分辨率",
      "composition_priority": "极高",
      "photographic_authenticity_priority": "最大限度"
    },
    "subject": {
      "count": 1,
      "presentation": "年轻的成年女性",
      "age_appearance": "显然是成年人，大约二十五岁左右",
      "appearance": {
        "physique": "女性运动体格，臀部和腿部自然发达，腹部健美，肩膀和手臂轮廓适中，腰臀比例真实，定期力量训练的明显证据，但没有夸张的健美比例",
        "body_realism": [
          "左右两侧微妙的自然不对称",
          "运动中的真实肌肉张力",
          "运动引起的小自然皮肤褶皱",
          "没有不可能的沙漏比例",
          "无人工极度减腰",
          "没有夸张的胸部或臀部比例"
        ],
        "skin": {
          "tone": "温暖的浅晒黑自然皮肤",
          "texture": "可见真实的毛孔和微妙的皮肤纹理",
          "details": [
            "肤色的微小变化",
            "身体活动引起的非常轻微的发红",
            "轻微的自然缺陷",
            "适当区域有微弱可见的静脉",
            "锻炼出汗后产生的轻微自然光泽",
            "衣服与皮肤接触处的细微压缩痕迹"
          ],
          "avoid": "完美的蜡质皮肤、塑料质感、过度平滑或人工美容滤镜外观"
        },
        "hair": {
          "color": "浓郁的深棕色",
          "length": "长的",
          "style": "松散扎成高马尾",
          "condition": "运动时有点凌乱",
          "details": [
            "可见独立发丝",
            "额头和太阳穴周围有松散的细丝",
            "自然翘起的碎发",
            "轻微的不均匀而不是完美的沙龙造型"
          ]
        },
        "face": {
          "expression": "轻松、自信、巧妙地调情，没有夸张的姿势",
          "gaze": "带着自然而略显紧张的表情看向镜头",
          "mouth": "嘴唇自然放松并微微张开",
          "makeup": "简约逼真的健身房妆容、精致的睫毛膏、自然的眉毛和柔和的裸粉色嘴唇",
          "facial_structure": "有吸引力但可信的成人脸，比例自然",
          "realism": [
            "面部轻微不对称",
            "自然的眼底纹理",
            "真实的鼻唇沟轮廓",
            "额头和脸颊上的微妙皮肤纹理",
            "没有完美镜像的特征"
          ]
        }
      },
      "exercise": {
        "type": "罗马尼亚杠铃硬拉",
        "moment": "当拍摄对象扭动臀部时在重复的中下部分附近捕捉到的",
        "execution": {
          "feet": "距离大约与臀部同宽，牢固地固定在橡胶地板上",
          "knees": "以逼真的罗马尼亚硬拉姿势稍微弯曲",
          "hips": "自然地向后推",
          "spine": "中性且解剖学上合理",
          "torso": "由于髋关节铰链而向前倾斜，同时保持真实的姿势",
          "barbell": "靠近腿部中部胫骨至膝盖以下的位置",
          "shoulders": "稍微向后拉并稳定",
          "hands": "自然地握住杠铃，大约与肩同宽",
          "head": "稍微抬起并转动足以让拍摄对象看向相机"
        },
        "pose_character": "运动和功能第一，自然的臀部铰链位置创造出迷人的轮廓，而不会变成不切实际的海报姿势"
      }
    },
    "clothing": {
      "top": {
        "type": "极简合身运动文胸",
        "color": "深酒红色/酒红色",
        "cut": "低至中等运动汤匙领口",
        "fit": "紧密支撑压缩贴合",
        "straps": "薄到中的运动肩带",
        "back": "受工字背启发的简约运动结构",
        "fabric": "哑光科技弹力材质",
        "details": [
          "逼真的拼接",
          "小接缝",
          "轻微的自然织物张力",
          "非常小的同色系徽标或没有明显的品牌"
        ]
      },
      "bottom": {
        "type": "非常合身的高腰无缝健身短裤",
        "color": "深炭灰色",
        "length": "短至大腿上部的运动长度",
        "waist": "高腰罗纹压缩腰带",
        "fit": "贴身轮廓风格，具有真实的压缩效果",
        "fabric": "哑光无缝弹力针织",
        "details": [
          "微妙的罗纹纹理",
          "天然织物张力",
          "髋关节周围的真实折痕",
          "大腿周围轻微受压",
          "微妙的中心接缝和轮廓接缝",
          "没有不可能的绘画纹理"
        ]
      },
      "socks": {
        "type": "白色运动袜",
        "height": "小腿中部",
        "condition": "有点破旧但很干净",
        "texture": "可见的棉罗纹和轻微的自然皱纹"
      },
      "shoes": {
        "type": "平底女式健身训练鞋",
        "color": "白色和灰白色，带有柔和的灰色细节",
        "design": "实用的力量训练剪影",
        "condition": "干净但明显被使用过",
        "details": [
          "鞋底轻微磨损",
          "蕾丝张力略有不均匀",
          "真正的纺织网",
          "缝合",
          "地板上的小灰尘痕迹"
        ]
      },
      "accessories": {
        "headphones": {
          "type": "紧凑型无线入耳式耳机",
          "color": "白色的",
          "details": "小而低调"
        },
        "watch": {
          "type": "健身智能手表",
          "position": "左手腕",
          "color": "黑色的",
          "details": "屏幕轻微反光，没有可读的界面文本"
        },
        "jewelry": {
          "type": "小号细圈耳环",
          "appearance": "微妙而可信"
        }
      }
    },
    "barbell": {
      "type": "标准奥林匹克杠铃",
      "position": "罗马尼亚硬拉时紧贴腿部",
      "plates": {
        "quantity": "每面一个中等大小的盘子",
        "style": "黑色商用橡胶保险杠板",
        "weight_markings": "微妙且不一定可读"
      },
      "details": [
        "逼真的滚花",
        "金属套",
        "正常健身房使用造成的轻微划痕",
        "物理上正确的板厚度",
        "正确的杆直线度和角度"
      ]
    },
    "gym_environment": {
      "location": "真正的高档城市商业健身房",
      "overall_style": "现代工业简约力量训练区",
      "atmosphere": "活跃但不拥挤，可信且略显不完美，而不是像原始的陈列室一样",
      "floor": {
        "material": "深色木炭橡胶地板",
        "texture": "精细斑点橡胶纹理",
        "condition": "轻微的鞋痕和正常的健身穿着",
        "details": "地板部分之间的可见接缝"
      },
      "walls": {
        "materials": [
          "温暖的灰白色油漆混凝土",
          "深色金属",
          "大镜面板"
        ],
        "condition": "干净但实用",
        "decoration": "最小的"
      },
      "windows": {
        "type": "大型工业落地窗",
        "frames": "黑金属",
        "lighting": "柔和的自然光从侧面进入",
        "glass": "真实的轻微反射和微妙的污迹",
        "view": "现代城市建筑外"
      },
      "ceiling": {
        "style": "裸露的工业天花板",
        "color": "黑炭",
        "details": [
          "暖通空调管道",
          "电气导管",
          "支撑梁",
          "线性 LED 灯具",
          "小嵌入式灯"
        ]
      }
    },
    "gym_equipment": {
      "power_racks": {
        "position": "背面和侧面背景",
        "type": "重型黑钢商用货架",
        "details": [
          "立柱",
          "洞",
          "J型钩",
          "安全臂",
          "储存的盘子"
        ]
      },
      "dumbbells": {
        "position": "背景",
        "type": "商用黑色橡胶哑铃",
        "arrangement": "沿多层机架不完美对齐",
        "realism": "轻微磨损和可信的金属反射"
      },
      "benches": {
        "position": "背景边缘",
        "type": "黑色可​​调节健身凳",
        "details": "微妙的内饰折痕和金属支撑框架"
      },
      "weight_plates": {
        "position": "存储钉和板树",
        "appearance": "轻微使用过的黑色板材，表面有轻微磨损"
      },
      "additional_details": [
        "水瓶在背景中部分可见",
        "远处长凳上的小健身毛巾",
        "电缆手柄自然悬挂",
        "没有不自然的完美装备安排"
      ]
    },
    "mirrors": {
      "presence": true,
      "position": "大镜子面板位于拍摄对象后面并稍微偏向一侧",
      "reflection_behavior": "物理上与实际相机和拍摄对象位置一致",
      "reflection_quality": "比直视稍微暗一些并且稍微柔和一些",
      "details": [
        "正确反映的健身器材",
        "正确的反射照明",
        "没有重复的肢体",
        "没有不可能的替代姿势",
        "没有不可能的相机反射"
      ]
    },
    "composition": {
      "subject_position": "稍微偏右",
      "body_coverage": "几乎全身可见",
      "exercise_visibility": "杠铃和完整的髋铰链位置清晰可读",
      "visual_emphasis": "面部、腰部到臀部的轮廓、腿部张力和运动",
      "foreground": "橡胶地板的微妙部分，脚和杠铃周围有足够的空间",
      "background": "可识别的健身房内部，具有真实的深度，但不会分散注意力",
      "visual_hierarchy": [
        "拍摄对象的脸部和目光",
        "自然的运动剪影",
        "罗马尼亚硬拉动作",
        "酒红色运动文胸和炭灰色短裤",
        "杠铃",
        "健身器材和窗户"
      ],
      "camera_angle": "相对于站立主体的臀部到腰部高度",
      "camera_position": "大约四分之三的正面角度而不是完美的正面角度",
      "camera_distance": "距拍摄对象约 2.5 至 3.5 米",
      "framing_character": "有点随意，就好像另一个人快速拍摄了锻炼照片，而不是精确地撰写时尚广告"
    },
    "camera_characteristics": {
      "device": "现代旗舰智能手机主摄像头",
      "lens": "约28mm全画幅等效",
      "aperture_behavior": "类似智能手机的自然景深，而不是人工 DSLR 人像模糊",
      "focus": "拍摄对象的躯​​干和面部清晰聚焦",
      "background_focus": "由于距离的原因稍微柔和一些，但仍然清晰可辨",
      "depth_of_field": "中等深度",
      "dynamic_range": "逼真的智能手机 HDR",
      "exposure": "稍微不完美但平衡的自然曝光",
      "white_balance": "大部分是中性的，略带暖色的皮肤渲染",
      "sharpness": "自然细节丰富，但数字化程度不高",
      "noise": "较暗区域中非常细微的传感器噪声",
      "lens_distortion": "靠近帧边缘的真实广角畸变较小",
      "chromatic_aberration": "极其微妙且仅在物理上合理的情况下",
      "motion": "松散发丝的微小自然运动柔软度，而面部和躯干保持锐利",
      "processing": "最小的计算摄影外观",
      "avoid": [
        "电影分级",
        "商业演播室照明",
        "不切实际的边缘锐化",
        "假深度图模糊",
        "完美均匀的皮肤暴露"
      ]
    },
    "lighting": {
      "primary_source": "来自大侧窗的自然光",
      "secondary_source": "现有的中性白色健身房顶部照明",
      "direction": "侧前方日光塑造柔和的身体轮廓",
      "quality": "柔软但不平坦",
      "contrast": "适度且现实",
      "face": "自然光照，阴影略有变化",
      "body": "由真实的头顶和窗户光造成的肩膀、腹部和腿部的柔和亮点",
      "skin_specularity": "非常微妙、逼真的锻炼后光泽",
      "shadows": [
        "鞋底接触阴影",
        "杠铃下方的柔和阴影",
        "四肢之间的自然阴影",
        "微妙的面部阴影",
        "设备阴影与顶灯一致"
      ],
      "avoid": [
        "美容盘照明",
        "强边缘照明",
        "霓虹灯 RGB 灯光",
        "橙色和青色的电影分级",
        "完美对称的光线",
        "不切实际的发光皮肤",
        "窗户曝光过度"
      ]
    },
    "photographic_realism": {
      "goal": "观看者最初应该假设这是健身创作者上传的普通真实照片，而不是生成的图像。",
      "required_imperfections": [
        "稍微不对称的框架",
        "织物轻微皱纹",
        "微妙的皮肤纹理",
        "自然飞扬的头发",
        "微小的照明不一致",
        "设备轻微磨损",
        "橡胶地板小磨损",
        "鞋子放置不完美",
        "肌张力略有变化",
        "自然面部不对称",
        "真实的手部压力"
      ],
      "avoid_ai_signatures": [
        "超完美的脸",
        "相同的重复哑铃",
        "完美间隔的设备",
        "不可能的反射",
        "融化背景物体",
        "随机不可读的墙壁字体",
        "假标志",
        "表面过于光滑",
        "均匀的毛孔纹理",
        "腿过于光滑",
        "过于戏剧化的身体比例"
      ]
    },
    "anatomical_requirements": {
      "hands": [
        "每只手恰好有五个手指",
        "自然的手指间距",
        "拇指正确放置在杆周围",
        "正确的手腕对齐",
        "没有融合的手指"
      ],
      "legs": [
        "真实的膝盖结构",
        "正确的小腿和大腿比例",
        "双脚自然地与地板连接",
        "没有重复或扭曲的关节"
      ],
      "torso": [
        "自然胸腔尺寸",
        "现实腰部",
        "物理上合理的脊柱姿势",
        "无扭曲的躯干几何形状"
      ],
      "face": [
        "两只对称但自然不相同的眼睛",
        "正常牙齿（如果可见）",
        "现实的耳朵",
        "正确的发际线"
      ]
    },
    "fine_details": [
      "太阳穴附近的个别发丝",
      "发际线处有微小的水滴或细微的汗水",
      "自然眉毛",
      "嘴唇上有轻微的纹理",
      "手上的静脉非常细",
      "逼真的指甲",
      "杠铃滚花",
      "轻微的金属划痕",
      "短裤中可见针织面料",
      "运动文胸拼接",
      "袜子罗纹",
      "鞋网",
      "鞋带纤维",
      "橡胶地板粒度",
      "设备附近有少量灰尘",
      "镜面边缘接缝",
      "远处镜子上的细微指纹或污迹",
      "窗户反射",
      "健身房硬件上的小亮点"
    ],
    "color_palette": {
      "dominant": [
        "勃艮第",
        "黑炭",
        "黑色的",
        "白色的",
        "温暖自然的肤色",
        "柔和的中性灰色"
      ],
      "secondary": [
        "凉爽的日光蓝",
        "拉丝钢",
        "柔和的城市色彩"
      ],
      "saturation": "自然又内敛",
      "contrast": "缓和",
      "grading": "最小的现实智能手机色彩处理"
    },
    "negative_prompt": [
      "AI生成的外观",
      "CGI",
      "3D渲染",
      "插图",
      "日本动画片",
      "卡通片",
      "数字绘画",
      "塑料皮",
      "瓷皮",
      "喷枪皮肤",
      "美颜滤镜",
      "皮肤完美光滑",
      "皮肤过于有光泽",
      "夸张的沙漏身材",
      "腰细得不可思议",
      "超大的乳房",
      "夸张的臀部",
      "不自然的臀宽",
      "拉长腿",
      "四肢缩短",
      "额外的武器",
      "额外的腿",
      "额外的手",
      "额外的手指",
      "缺少手指",
      "融合的手指",
      "扭曲的手",
      "手腕骨折",
      "膝盖变形",
      "脚翘",
      "浮鞋",
      "浮动杠铃",
      "弯曲的杠铃",
      "不对称配重板",
      "重复的健身器材",
      "重复哑铃模式",
      "扭曲的机架",
      "扭曲的镜子",
      "不正确的反映",
      "镜子里的复制人",
      "鱼眼畸变",
      "极低角度",
      "极广角",
      "人像严重模糊",
      "假散景",
      "电影灯光",
      "演播室灯光",
      "RGB霓虹灯",
      "青橙分级",
      "过度的 HDR",
      "过度锐化",
      "对比度过度",
      "脸部运动模糊",
      "颗粒状的低质量图像",
      "水印",
      "随机文本",
      "墙上的文字难以辨认",
      "假品牌标志",
      "完美的展厅健身房",
      "不自然的运动形式",
      "模特姿势僵硬",
      "明显的裸体",
      "透明衣服",
      "衣柜故障",
      "色情框架"
    ],
    "identity_handling": {
      "instruction": "创建一个完全虚构的成年女性。请勿复制或模仿任何真人的可识别身份。"
    },
    "priority_order": [
      "1. 结果必须看起来像真实世界中智能手机健身房的照片",
      "2. 保留可信的成人解剖学和运动生物力学",
      "3. 无需露骨的呈现，打造自然诱人、性感的健身美学",
      "4. 保留真实的不完美皮肤、头发、织物和设备细节",
      "5. 使罗马尼亚硬拉姿势在解剖学和力学上合理",
      "6.保留逼真的酒红色运动胸罩和木炭合身短裤",
      "7. 使用普通的自然健身房照明代替电影或演播室照明",
      "8. 保留物理上正确的镜子、阴影和反射",
      "9. 包含细微的现实世界缺陷，减少人工智能生成的外观",
      "10. 避免手、设备、背景几何和纹理中所有常见的 AI 伪影"
    ]
  },
  "output": {
    "style": "极其逼真的真实健身摄影",
    "quality": "最大限度",
    "detail": "最大限度",
    "human_realism": "最大限度",
    "skin_realism": "最大限度",
    "anatomical_accuracy": "最大限度",
    "exercise_accuracy": "非常高",
    "environment_realism": "最大限度",
    "photographic_authenticity": "最大限度",
    "ai_artifact_suppression": "最大限度",
    "retouching_level": "最小的"
  }
}
```

<sub>(by [@cartelfather](https://x.com/cartelfather/status/2101400765772542021)) · [来源平台： X](https://x.com/cartelfather/status/2101400765772542021)</sub>

<a id="p79-two-woman-fitness-selfie-reconstruction"></a>

### 📌 1.28. 双人健身自拍重建

#### 👀 预览

[<img src="assets/p79-two-woman-fitness-selfie-reconstruction/source-example-01.jpg" width="225" height="400" alt="双人健身自拍重建——来源示例 1">](assets/p79-two-woman-fitness-selfie-reconstruction/source-example-01.jpg)

#### 👇 工作流

`参考照片 → 双人健身自拍重建`

#### 🔖 完整提示词

```text
{
  "prompt_type": "photorealistic_reference_image_reconstruction",
  "goal": "尽可能地重新创建提供的参考照片，匹配构图、两人布置、面部表情、身体姿势、服装、配饰、背景树叶、相机视角、自然光、颜色、比例和智能手机照片美学。完全忽略并删除所有文本、界面元素、按钮、图标、时间戳、水印、标题、边框和任何其他屏幕图形。",
  "reference_fidelity": {
    "target": "极高的视觉相似度",
    "priority_order": [
      "整体构图与裁切",
      "两位人物的位置与画面占比",
      "面部表情和头部角度",
      "头发的形状和颜色",
      "眼镜",
      "服装廓形和颜色",
      "手的放置和修指甲",
      "绿色饮料和吸管",
      "背景绿化和建筑",
      "照明和颜色分级",
      "优质材质和皮肤细节"
    ]
  },
  "canvas": {
    "orientation": "肖像",
    "aspect_ratio": "约 736:1307",
    "framing": "紧密垂直智能手机自拍照片",
    "crop_style": "上半身到大腿中部/全身局部框架",
    "camera_distance": "非常近，大约一臂长度",
    "camera_height": "略高于胸部水平并向下倾斜一点",
    "composition": "两个成年女性站得很近，几乎占据了整个画面",
    "edge_behavior": {
      "top": "两个头顶上方可见少量背景",
      "left": "左边女人的头发和身体延伸到接近框架边缘",
      "right": "右侧女性的肩膀和躯干延伸到靠近框架边缘",
      "bottom": "右边女人的裤子和左边女人的腿向底部边界延伸"
    }
  },
  "scene": {
    "setting": "阳光明媚的户外露台、花园或住宅庭院",
    "atmosphere": "温暖的高档休闲夏季生活方式环境",
    "visual_style": "正宗的高端智能手机社交媒体照片，而不是工作室摄影",
    "background": {
      "dominant_element": "茂密的深绿色绿叶树篱或攀缘植被",
      "architecture": {
        "visible": true,
        "description": "奶油色/浅米色灰泥或混凝土垂直结构，部分被树叶遮盖",
        "details": [
          "垂直苍白结构柱",
          "浅色墙面",
          "右上角附近微妙的屋顶或凉棚结构",
          "深色水平/木质建筑元素"
        ]
      },
      "vegetation": {
        "type": "茂密的阔叶绿化",
        "color": "深天然绿色，阳光照射下的叶子颜色较浅",
        "density": "非常高",
        "focus": "比拍摄对象稍微柔和一些"
      },
      "ground": {
        "appearance": "浅灰色或浅色石头/混凝土露台",
        "visibility": "大部分被拍摄对象遮挡，在较低背景中可见"
      }
    }
  },
  "subjects": {
    "count": 2,
    "both_are": "成年女性",
    "interaction": "紧密站在一起拍摄休闲自拍/时尚生活照",
    "mood": "俏皮、自信、放松、夏日气息"
  },
  "right_subject": {
    "position": "前景右侧，更大且更靠近相机",
    "scale": "主要主体占据可见图像宽度的大约 55-60%",
    "body_visibility": "头部、肩膀、躯干、腹部、臀部和高腰裤的上半部分可见",
    "pose": {
      "orientation": "几乎直接面对相机",
      "head": "稍微向观看者左侧倾斜",
      "shoulders": "轻松开放",
      "torso": "朝前，轻微自然旋转",
      "right_arm": "大部分位于框架外部或沿框架边缘",
      "left_arm": "靠近中左区域，手放在另一个女人的肩膀上",
      "posture": "挺直、放松"
    },
    "face": {
      "shape": "柔和的椭圆形，颧骨轮廓分明，下脸呈锥形",
      "skin": {
        "tone": "暖中棕褐色/金米色",
        "finish": "光滑、明亮、轻微的阳光亲吻",
        "texture": "通过智能手机加工软化自然细腻的质感",
        "highlights": "额头、脸颊、鼻子和上胸部有温暖的亮点"
      },
      "expression": "微微噘嘴，嘴唇轻轻抿起，表情平静自信",
      "gaze": "直接朝向相机",
      "eyes": {
        "visibility": "大部分被太阳镜遮挡",
        "makeup": "裸露区域周围精致的抛光眼妆"
      },
      "brows": "黑暗、整洁、明确",
      "nose": "直线，柔和定义",
      "lips": {
        "shape": "完整且明确",
        "color": "柔和的裸粉色 / 柔和的紫红色",
        "finish": "缎面至微光泽",
        "expression": "轻微的吻状撅嘴"
      },
      "cheeks": "柔和的古铜色，带有淡淡的温暖腮红"
    },
    "hair": {
      "color": "深棕色至近黑色",
      "style": "时尚、紧紧向后拉的发型",
      "length": "长但大部分聚集在远离脸部的地方",
      "part": "清洁中心或稍微偏离中心的部分",
      "finish": "光滑有光泽",
      "texture": "细腻光滑的股线，具有微妙的个人细节",
      "silhouette": "靠近头顶附近的头皮并向后拉"
    },
    "eyewear": {
      "type": "窄型未来派环绕式太阳镜",
      "frame": "深色金属色或亮黑色",
      "lens": "深烟熏棕黑色反光镜片",
      "shape": "细长角猫眼/盾形混合体",
      "size": "中等宽度，垂直高度相对较窄",
      "position": "足够低，可以清晰地勾勒出上脸的轮廓，但完全遮盖眼睛",
      "reflection": "镜片上可见微妙的明亮户外反射",
      "style": "2000 年代初期时尚前卫的矩形太阳镜"
    },
    "clothing": {
      "top": {
        "type": "合身短款运动背心 / 运动文胸式上衣",
        "color": "非常淡的冰蓝白色/凉爽的薰衣草白色",
        "neckline": "宽圆汤匙领",
        "straps": "中宽运动肩带",
        "fit": "舒适且塑形",
        "length": "剪裁在胸围下方",
        "material": "细罗纹弹力运动面料",
        "finish": "哑光，带有微妙的织物亮点"
      },
      "bottom": {
        "type": "高腰合身打底裤或瑜伽裤",
        "color": "搭配非常淡的蓝白色/冷淡的薰衣草白色",
        "rise": "非常高腰",
        "fit": "腰部和臀部贴身",
        "surface": "光滑的弹力面料，带有精致的罗纹结构",
        "waistband": "广泛和支持",
        "silhouette": "干净合身的运动线条"
      }
    },
    "jewelry": {
      "earrings": {
        "type": "大金圈耳环",
        "shape": "圆形粗箍",
        "finish": "温暖的抛光金",
        "visibility": "最靠近相机的一侧清晰可见"
      },
      "necklace": {
        "type": "非常精致的短金链",
        "pendant": "极简主义小吊坠",
        "placement": "上胸部低"
      }
    },
    "manicure": {
      "hand": "手搭在另一个女人的肩膀上",
      "nails": {
        "length": "长的",
        "shape": "长杏仁形/锥形细高杏仁形",
        "color": "浅中性粉色或柔和的裸色",
        "finish": "高光泽",
        "appearance": "精心修剪、优雅"
      },
      "rings": {
        "quantity": "一枚或几枚精致的戒指",
        "material": "银或金",
        "style": "最小的"
      }
    }
  },
  "left_subject": {
    "position": "前景女性的后方和左侧",
    "scale": "由于离相机较远，因此略小",
    "body_visibility": "头部、肩膀、躯干、腰部、短裤和大腿上中部可见",
    "pose": {
      "orientation": "面对相机",
      "head": "稍微倾斜",
      "shoulders": "轻松",
      "left_arm": "较低且部分裁剪",
      "right_arm": "靠近中心/右侧，手与前景女性进行视觉交互",
      "posture": "随意且略带棱角"
    },
    "face": {
      "shape": "柔软青春的椭圆形",
      "skin": {
        "tone": "暖中棕褐色/金米色",
        "finish": "光滑且柔和发光",
        "texture": "自然但经过微妙的美感过滤"
      },
      "expression": "俏皮夸张的吻唇/鸭嘴撅嘴",
      "gaze": "朝向相机",
      "eyes": {
        "visibility": "透过有色太阳镜可见",
        "appearance": "黑眼睛和微妙的眼妆"
      },
      "brows": "黑暗而明确",
      "nose": "小且轮廓柔和",
      "lips": {
        "shape": "饱满而突出",
        "color": "柔和的玫瑰粉色",
        "finish": "软缎",
        "expression": "强烈的皱起嘴的吻表情"
      }
    },
    "hair": {
      "color": "深棕色",
      "style": "长、浓密、松散的头发",
      "length": "越过肩膀，向下延伸至腰部/臀部",
      "texture": "柔和的波浪与自然的身体",
      "part": "稍微偏离中心",
      "appearance": "饱满，略显凌乱，有光泽",
      "face_framing": "多根松散的线和厚的部分构成脸颊和下巴",
      "volume": "头部两侧高"
    },
    "eyewear": {
      "type": "小窄矩形太阳镜",
      "frame": "深棕色/黑色",
      "lens": "暖棕色烟熏半透明镜片",
      "shape": "略呈猫眼状/矩形",
      "position": "以眼睛为中心",
      "style": "复古未来窄时尚太阳镜"
    },
    "clothing": {
      "top": {
        "type": "合身短款背心 / 运动文胸式上衣",
        "color": "柔和的淡粉色腮红",
        "trim": "领口和肩带周围有对比鲜明的浅冷灰色滚边或饰边",
        "neckline": "圆勺",
        "fit": "紧密和支持",
        "length": "剪裁至腰部以上",
        "material": "弹力运动面料",
        "finish": "哑光，带有微妙的罗纹纹理"
      },
      "bottom": {
        "type": "高腰合身机车短裤",
        "color": "搭配浅粉色腮红",
        "length": "大腿中部",
        "fit": "紧致的身体轮廓",
        "material": "光滑弹力运动面料",
        "waistband": "高又宽",
        "wrinkles": "臀部和大腿周围微妙的自然面料张力"
      }
    },
    "accessories": {
      "watch_or_bracelet": {
        "position": "左手腕",
        "type": "厚实的金表或叠戴手镯",
        "finish": "抛光金",
        "appearance": "明亮的金属亮点"
      },
      "rings": {
        "style": "最小精致的戒指",
        "finish": "金子"
      }
    },
    "drink": {
      "type": "透明塑料杯绿色饮料",
      "position": "保持在下躯干前面",
      "beverage": "明亮的天然绿色冰沙、抹茶或压制绿色饮料",
      "cup": {
        "material": "透明塑料",
        "shape": "中大型圆柱形外卖杯",
        "lid": "透明的圆顶或扁平塑料盖",
        "condensation": "外部有轻微的湿气",
        "color_detail": "绿色饮料主导室内装饰"
      },
      "straw": {
        "color": "白色的",
        "type": "直塑料吸管",
        "position": "从杯子向右上角斜向上升起",
        "visibility": "清晰可见"
      },
      "grip": {
        "hand": "左侧受试者的手自然地握住杯子",
        "fingers": "细长的",
        "nails": "浅粉色/裸色光泽长指甲"
      }
    }
  },
  "interaction_between_subjects": {
    "distance": "非常接近，肩膀和上臂几乎接触",
    "foreground_hand": "右主体的手随意地放在左主体的肩膀上或附近",
    "body_overlap": "右侧主体与左侧主体躯干的一部分重叠",
    "social_context": "亲密的朋友一起摆出休闲时尚/生活方式的自拍照",
    "pose_relationship": "协调但自发"
  },
  "background": {
    "vegetation": {
      "description": "茂密的绿叶树篱覆盖了大部分上部和中部背景",
      "colors": [
        "深林绿",
        "中自然绿色",
        "橄榄绿",
        "柔和的鼠尾草绿"
      ],
      "lighting": "混合阴影与小片温暖的阳光",
      "texture": "许多重叠的小叶和中叶",
      "depth": "缓和"
    },
    "architecture": {
      "wall": "暖色米白色或米色",
      "vertical_pillar": "左上角/中心的浅米色结构柱",
      "roof_structure": "右上方可见部分板条凉棚/遮阳篷",
      "background_detail": "微妙且不分散注意力"
    },
    "ground": {
      "material": "浅灰色石材/混凝土",
      "texture": "稍微粗糙",
      "lighting": "柔和地照亮"
    }
  },
  "lighting": {
    "source": "室外自然光",
    "style": "明亮但柔和的阳光透过附近的树叶",
    "direction": "右前且稍高于摄像头",
    "quality": "柔和的定向日光，带有一些斑驳的亮点",
    "skin_rendering": "温暖、明亮、讨人喜欢",
    "hair_highlights": "松散的发丝上有微妙的温暖亮点",
    "clothing_highlights": "白色/浅色织物上柔和明亮的亮点",
    "background": "稍深的树叶在脸部周围形成分离",
    "shadows": "柔和逼真，没有刺眼的闪光阴影",
    "color_temperature": "暖中性日光"
  },
  "camera": {
    "device": "现代智能手机前置摄像头",
    "lens": "微广角自拍镜头",
    "focal_length_equivalent": "约24-28毫米",
    "perspective": "具有轻微自然边缘拉伸的近距离广角肖像",
    "orientation": "垂直的",
    "camera_position": "保持在眼睛/胸部上方或周围",
    "distance": "一臂长度或稍长的自拍距离",
    "focus": "两个女人的脸都相当锐利，前景主体稍微锐利一些",
    "depth_of_field": "适中，背景柔和但仍可辨认",
    "image_quality": "高分辨率智能手机照片",
    "processing": "微妙的HDR，平滑的皮肤处理，清晰度适中，色彩自然",
    "stabilization": "非常稳定的手持图像",
    "motion_blur": "最小的"
  },
  "composition": {
    "foreground_subject": "框架右半部分较大",
    "background_subject": "框架左半部分稍小",
    "faces": {
      "right_subject": "右上象限",
      "left_subject": "左上象限",
      "vertical_level": "脸部大致对齐，但前景女性的头部略高"
    },
    "bodies": {
      "right_subject": "躯干占据右下角",
      "left_subject": "躯干和短裤占据左下角"
    },
    "drink": "绿色杯锚定左下中区域",
    "hands": "一只手靠近受试者左肩的中心/顶部，一只手握住绿色饮料",
    "negative_space": "由于自拍取景紧凑，负空间很小",
    "visual_balance": "两张脸和两套对比鲜明的柔和服装构成了主要视觉焦点"
  },
  "clothing_materials": {
    "right_outfit": {
      "texture": "细罗纹运动针织",
      "stretch": "平滑的身体轮廓拉伸",
      "surface": "哑光缎面"
    },
    "left_outfit": {
      "texture": "细运动针织",
      "stretch": "柔软合身",
      "surface": "哑光，带有微妙的光泽"
    }
  },
  "color_grading": {
    "overall": "温暖、淡雅、自然的社交媒体美学",
    "skin": "温暖的金米色",
    "whites": "有点凉",
    "pink": "柔和的腮红粉色",
    "green": "丰富的天然绿叶",
    "contrast": "缓和",
    "saturation": "缓和",
    "highlights": "稍微温暖",
    "shadows": "凉爽柔和的绿色和灰色",
    "black_levels": "自然，未压碎"
  },
  "beauty_processing": {
    "strength": "缓和",
    "skin_smoothing": "中到高",
    "blemish_reduction": "缓和",
    "eye_enhancement": "微妙的",
    "facial_shape_changes": "无或最少",
    "lip_definition": "微妙的",
    "overall": "抛光智能手机/社交媒体的美丽外观，同时保持照片般的真实感"
  },
  "micro_details": {
    "skin": "细微的自然毛孔和色调变化仍然可见",
    "hair": "面部和肩部周围可见细小的单丝",
    "sunglasses": "天空/建筑的真实反射",
    "gold_jewelry": "微小锐利的镜面高光",
    "nails": "光泽反射和真实曲率",
    "athletic_fabric": "精细的罗纹纹理和逼真的张力褶皱",
    "drink": "透明反射，绿色液体深度，轻微凝结",
    "leaves": "单独的叶子形状和重叠的阴影",
    "background_structure": "微妙的建筑边缘和纹理"
  },
  "photographic_character": {
    "genre": "奢华休闲生活方式/时尚影响者自拍",
    "realism": "极端照片写实主义",
    "camera_feel": "真实的智能手机捕捉",
    "retouching": "轻度至中度",
    "avoid": "工作室编辑外观",
    "desired_result": "看起来像是其中一个拍摄对象在户外拍摄的真实即兴照片"
  },
  "negative_prompt": [
    "文本",
    "字幕",
    "字幕",
    "水印",
    "标志",
    "社交媒体用户界面",
    "按钮",
    "播放图标",
    "暂停图标",
    "进度条",
    "时间戳",
    "界面元素",
    "屏幕覆盖",
    "额外的人",
    "第三人称",
    "人物数量不同",
    "孩子",
    "青少年",
    "不同的姿势",
    "不同的拍摄角度",
    "广阔的风景构图",
    "短头",
    "裁剪过的脸",
    "失踪的手",
    "额外的手",
    "额外的手指",
    "手指变形",
    "解剖扭曲",
    "重复肢体",
    "不自然的身体比例",
    "不同的发型",
    "左侧主体的短发",
    "右侧主体的头发松散",
    "缺少太阳镜",
    "超大太阳镜",
    "圆形太阳镜",
    "透明太阳镜",
    "不同的衣服颜色",
    "深色衣服",
    "长袖",
    "夹克",
    "外套",
    "牛仔裤",
    "裙子",
    "不同的饮料",
    "不喝酒",
    "不带吸管的杯子",
    "金属杯",
    "玻璃酒杯",
    "繁忙的城市背景",
    "室内环境",
    "夜景",
    "工作室背景",
    "闪光摄影",
    "戏剧性的电影灯光",
    "极端散景",
    "鱼眼畸变",
    "卡通片",
    "日本动画片",
    "插图",
    "3D渲染",
    "CGI",
    "塑料皮",
    "怪异的面孔",
    "皮肤过度光滑",
    "过度的 HDR",
    "过饱和的颜色",
    "不真实的反射"
  ],
  "final_generation_instruction": "生成一张高度真实的垂直智能手机自拍照，与参考构图尽可能匹配。两名成年女性在户外靠得很近，靠着茂密的绿树篱和苍白的建筑背景。右边的前景女子离镜头较近，身穿淡色冰蓝白色合身短款运动上衣，搭配高腰紧身裤、窄窄的深色环绕式太阳镜、大金圈耳环和精致的金首饰。她的头发光滑，向后梳，嘴唇轻轻地撅起，她的右侧占据了画面的主导地位。她修剪整齐的手随意地搭在另一个女人的肩膀上。左边的女士站在稍微靠后的位置，穿着浅粉色短款运动背心，搭配冷灰色饰边，搭配配套的高腰机车短裤，戴着窄窄的棕色矩形太阳镜，留着宽松的深色长卷发。她拿着一个透明的杯子，里面装着鲜绿色的饮料，还有一根白色的吸管。两人都有光滑的杏仁形长指甲和温暖的自然古铜色皮肤。保留亲密的自拍视角、自然光、逼真的皮肤、微妙的美感处理、绿叶背景、苍白的运动面料、珠宝反射和休闲的社交媒体生活方式美学。删除并忽略所有文本、按钮、UI 元素、时间戳、水印和界面图形。"
}
```

<sub>(by [@jasonugc](https://x.com/jasonugc/status/2101372937353965940)) · [来源平台： X](https://x.com/jasonugc/status/2101372937353965940)</sub>

<a id="p80-sepia-reference-portraits"></a>

### 📌 1.29. 参考人物棕褐色人像

#### 👀 预览

[<img src="assets/p80-sepia-reference-portraits/source-example-01.jpg" width="400" height="400" alt="参考人物棕褐色人像——来源示例 1">](assets/p80-sepia-reference-portraits/source-example-01.jpg)

[<img src="assets/p80-sepia-reference-portraits/source-example-02.jpg" width="400" height="400" alt="参考人物棕褐色人像——来源示例 2">](assets/p80-sepia-reference-portraits/source-example-02.jpg)

[<img src="assets/p80-sepia-reference-portraits/source-example-03.jpg" width="400" height="400" alt="参考人物棕褐色人像——来源示例 3">](assets/p80-sepia-reference-portraits/source-example-03.jpg)

[<img src="assets/p80-sepia-reference-portraits/source-example-04.jpg" width="400" height="400" alt="参考人物棕褐色人像——来源示例 4">](assets/p80-sepia-reference-portraits/source-example-04.jpg)

#### 👇 工作流

`人物参考图 → 棕褐色人像`

#### 🔖 完整提示词

```text
以所附参考图中的人物为主体创作棕褐色调人像，保留其五官、身份特征、发型、肤色和比例。采用经典暖棕色调、柔和的定向光、细腻胶片颗粒、浓郁阴影和经久耐看的复古摄影风格；保留自然皮肤纹理，构图优雅，浅景深，细节丰富，照片级写实，具有电影感且对焦清晰。
```

<sub>(by [@shushant_l](https://x.com/shushant_l/status/2101567556268310657)) · [来源平台： X](https://x.com/shushant_l/status/2101567556268310657)</sub>

<a id="p81-playful-plaza-finger-point-portrait"></a>

### 📌 1.30. 广场俏皮指向镜头人像

#### 👀 预览

[<img src="assets/p81-playful-plaza-finger-point-portrait/source-example-01.jpg" width="225" height="400" alt="广场俏皮指向镜头人像——来源示例 1">](assets/p81-playful-plaza-finger-point-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 广场俏皮街拍人像`

#### 🔖 完整提示词

```text
一张在外景拍摄的电影般的 35 毫米街头照片 — 一幅引人入胜的突出主体的中景构图，描绘的是一位在阳光明媚的城市广场上异常迷人的 20 岁东亚女大学生，相机直接置于胸部水平，捕捉到她以 M1 电影叙事方式将右手食指直接指向相机镜头时，捕捉到她令人惊叹的青春美丽和俏皮魅力。

这名女子是一位20岁左右的年轻女子，有着精致、甜美的东亚五官，柔软而容光焕发的脸颊上泛着精致的桃红，一双迷人的黑杏仁大眼睛直视着镜头。她柔软、丰满的玫瑰色嘴唇被压成一个可爱、微妙的微撅，上唇微微皱起，露出一种可爱、可爱的表情，一副俏皮的假装烦恼的表情。她有一头柔滑的及肩深色浓缩咖啡色头发，整齐、通风的直刘海勾勒出她可爱的脸庞，左耳上方饰有一个微型白色发夹，柔软的发丝捕捉着温暖的午后阳光。她拥有非常优美的曲线、沙漏般的女性身材、突出、丰满的胸部和纤细纤细的腰围。她穿着一件舒适合身的紧身白色弹力棉婴儿 T 恤，整齐地包裹着她性感的胸围和细腰，胸部中央有独特的卡通黑色车把胡须印花。棕褐色皮革斜挎包带斜跨过她的躯干，自然地凸显了她引人注目的女性轮廓。她的衬衫整齐地塞进高腰合身的水洗灰色牛仔吊带短裤中，短裤紧贴在腰间，肩膀上有细长的牛仔吊带。她的右臂直接伸向镜头，食指以戏剧性的光学透视方式指向镜头，而她的左手自信地放在臀部，手腕上戴着细长的银色三叶草手镯。

场景是一个明亮的下午的现代户外建筑入口——一根巨大的圆形米色花岗岩柱子直接在她旁边升起，脚下是光滑的石头路面，户外台阶通向柔和模糊的背景中的景观绿色灌木，提供了一个真实的城市校园/城市环境。

照明由干净、温暖的自然午后阳光控制——来自上方和相机右侧的明亮定向光源在她的黑发顶部和肩膀上投射出明亮的金色边缘光和明亮的高光，而清晰的环境日光以平衡、讨人喜欢的照明平滑地充满她的脸和白衬衫，美丽地突出了她的女性曲线和迷人的面部表情。

使用大光圈 T2.0 的快速 35 毫米广角定焦镜头拍摄宽宽容度数字电影效果，在她的眼睛、流苏刘海、微妙的撅嘴和合身 T 恤上呈现清晰的焦点，同时自然地柔化伸出的前景食指，并将背景建筑模糊为平滑的圆形散景。日光胶片模拟，具有温暖、明亮的肤色、清晰干净的白色以及胡须印花和牛仔布中深邃浓郁的黑色，并在整个画面上采用精细、有机的 35 毫米戏剧胶片颗粒。真实的电影摄影机拍摄的真实摄影画面，真实的广角镜头，真实的修身棉质 T 恤，真实的牛仔面料，真实的皮革肩带，真实华丽的20岁东亚女性，真实的阳光照射的城市广场——没有CGI，没有渲染外观，没有数字清洁度，没有塑料表面，没有AI平滑度，没有皮肤平滑，没有儿童特征，没有夸张扭曲的噘嘴，没有发光，没有看起来像人造的光晕绽放，没有光泽高光。
```

<sub>(by [@johnAGI168](https://x.com/johnAGI168/status/2101552625669833159)) · [来源平台： X](https://x.com/johnAGI168/status/2101552625669833159)</sub>

<a id="p85-y2k-street-fashion-portrait"></a>

### 📌 1.31. Y2K 街头时尚人像

#### 👀 预览

[<img src="assets/p85-y2k-street-fashion-portrait/source-example-01.jpg" width="300" height="400" alt="Y2K 街头时尚人像——来源示例">](assets/p85-y2k-street-fashion-portrait/source-example-01.jpg)

#### 👇 工作流

`先前人像参考图 → Y2K 街头抓拍姿势`

#### 🔖 完整提示词

```text
超写实的自然手机照片，竖幅 3:4，抓拍一位年轻漂亮的日本女性的 Y2K 街头时尚人像。<<<d1ec9c33a3e14a5dbbef4f3088b4ad5f>>>，她站在有纹理的灰白色灰泥墙前。

以下特征须保持完全一致：她自然垂落肩头的深棕色长直发，以及轻柔地修饰脸庞的发丝；有型的黑色报童帽／面包师帽；合身、纯白、短款短袖 baby tee，胸前有一颗醒目的豹纹五角星图案；低腰、宽大的深蓝色阔腿牛仔裤，带有真实的水洗褪色效果；腰间的豹纹腰带／裤腰；饰有大号圆形金属环和垂坠带饰的长金属链；以及黑色大号单肩包。

全新的姿势——与先前所有版本明显不同：抓拍她自然走动时迈步的瞬间，身体约以四分之三角度朝向镜头，头部从左肩向后转过来看向镜头，神情冷酷而漫不经心——嘴唇微张，目光放松且直视镜头。重心正向前转移到右脚，左腿向后迈步，使宽松牛仔裤呈现自然的行走动态。右臂随步态自然向前摆动，肘部放松地弯曲；左臂略向后摆，黑色单肩包随着动作自然移动。头发松散垂落，并有暗示步行的细微动态。整体姿态应像街头时尚抓拍，随意、不摆拍；其身体朝向、重心分布和头部方向都与之前两个参考姿势完全不同。

使用直接的机顶闪光灯拍摄，在身后的纹理墙上投下她身体与帽子的清晰、真实阴影。呈现真实的 2000 年代早期傻瓜相机或便携数码相机质感。RAW 手机照片美学、真实皮肤纹理、清晰可辨的发丝、准确的手和手指、自然的人体比例、细致的牛仔布纹理、真实的皮革包、真实的金属反光、可见的墙面肌理、直接闪光、轻微颗粒感、略不完美的曝光，以及怀旧的 Y2K 时尚摄影感。不要美颜滤镜、塑料皮肤、CGI 外观或过度修饰。竖幅 3:4 构图。
```

<sub>(by [@saniaspeaks_](https://x.com/saniaspeaks_/status/2101878359282036998)) · [来源平台： X](https://x.com/saniaspeaks_/status/2101878359282036998)</sub>

<a id="p88-bangkok-night-market-street-photograph"></a>

### 📌 1.32. 曼谷夜市街头摄影

#### 👀 预览

[<img src="assets/p88-bangkok-night-market-street-photograph/source-example-01.png" width="400" height="224" alt="曼谷夜市街头摄影——来源示例">](assets/p88-bangkok-night-market-street-photograph/source-example-01.png)

#### 👇 工作流

`文字 → 曼谷夜市摄影`

#### 🔖 完整提示词

```text
一张曼谷繁忙夜市的广角照片，从视平线高度使用 35mm 镜头拍摄。前景面摊升起蒸汽，头顶悬挂着串灯，大约十五个人分布在画面的不同距离处走动，湿润的路面倒映着泰文霓虹招牌。让前景摊贩处于浅景深焦点之内，其后的所有景物逐渐虚化。
```

<sub>(by [Jim Clyde Monge](https://generativeai.pub/i-tested-gpt-image-2-5-and-compared-it-against-gpt-image-2-5-on-pollo-ai-87a8bb375ce2)) · [来源平台： Generative AI](https://generativeai.pub/i-tested-gpt-image-2-5-and-compared-it-against-gpt-image-2-5-on-pollo-ai-87a8bb375ce2)</sub>

<a id="p92-night-train-window-portrait"></a>

### 📌 1.33. 夜间列车窗边人像

#### 👀 预览

[<img src="assets/p92-night-train-window-portrait/source-example-01.jpg" width="225" height="400" alt="夜间列车窗边人像——来源示例">](assets/p92-night-train-window-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 电影感列车窗边人像`

#### 🔖 完整提示词

```text
制作一张照片级写实、具有电影感的人像照片：一名年轻成年女性独自坐在现代城际列车的窗边。

构图：
竖版 9:16 人像画幅。相机位于过道一侧、她前方座椅的稍后方，斜向看向窗边座位。一个大幅虚化的列车座椅占据左下前景，形成强烈景深并框住主体。女性位于画面中间偏右，被前景座椅遮住一部分。她的倒影清晰可见于右侧列车窗户中。

主体：
年轻成年女性，肤色白皙，有自然雀斑和柔和面部特征；中等长度的铜红色头发，凌乱自然的刘海垂在额前。头发略显蓬乱且不完美，能看到独立发丝。她有浅蓝灰色眼睛、自然眉毛、细微睫毛、柔粉色自然嘴唇，面部完全自然，没有浓妆。

她穿宽松的米色／灰褐色连帽衫，帽子搭在后脑和肩部周围。连帽衫具有写实的柔软面料纹理和自然褶皱。

姿势与表情：
她坐在窗边，身体略微朝过道倾斜，直视相机，神情安静、疲惫且内省。头部略微低垂并朝前景座椅倾斜。姿势放松，嘴唇轻轻闭合，带有细微忧郁情绪。这是自然抓拍瞬间，不是在为镜头摆姿势。

列车内部：
写实的现代欧洲风格列车车厢。深炭灰色布艺座椅上散布细小红色几何图案。多排座椅向背景延伸。前景座椅离相机很近并严重失焦。远处背景中勉强可见另一名乘客，同样高度虚化。

窗户：
女性紧邻一扇大列车窗。玻璃上有轻微反光和淡淡污迹。她的脸和上半身以柔和但可辨识的倒影出现在窗中。窗外是不清晰、低饱和的城乡景观，因为列车移动而完全模糊。

光线：
柔和自然日光从右侧列车窗射入。温暖、略带金色的日光照亮她的脸和铜红色头发，车厢内部则保持较暗和克制。使用柔和的电影感对比、柔软阴影、真实皮肤高光，以及来自窗户的细微反射光。

相机：
专业电影感摄影，50mm 镜头，约 f/1.8，浅景深。焦点精确落在女性的眼睛和脸部。前景座椅和背景乘客强烈虚化。自然透视、真实光学景深和轻微镜头压缩感。

色彩与氛围：
低饱和电影调色，以头发中的温暖铜色／橙色和米色连帽衫，对比冷调深蓝灰色列车座椅与窗户色调。柔和胶片对比、略微降低饱和度、自然肤色、细微颗粒，营造有空气感且亲密的氛围。

真实感：
超写实、真实抓拍摄影，呈现真实皮肤毛孔和雀斑、独立发丝、写实面料纹理、物理准确的玻璃倒影、自然瑕疵、真实列车材质和真正的摄影景深；不要人工美颜修饰。

负面提示词：
卡通、动漫、插画、CGI、3D 渲染、塑料皮肤、浓妆、完美皮肤、美颜滤镜、过度锐化、不真实的眼睛、扭曲面部、多余手指、畸形手部、重复人物、重复倒影、错误倒影、人造头发、油亮皮肤、影棚灯光、奇幻列车、文字、水印、标志、低分辨率、过度 HDR、过饱和色彩
```

<sub>(by [@harboriis](https://x.com/harboriis/status/2102635863893307394)) · [来源平台： X](https://x.com/harboriis/status/2102635863893307394)</sub>

<a id="p94-luxury-suv-night-selfie-reconstruction"></a>

### 📌 1.34. 豪华 SUV 夜间自拍重建

#### 👀 预览

[<img src="assets/p94-luxury-suv-night-selfie-reconstruction/source-example-01.jpg" width="312" height="400" alt="豪华 SUV 夜间自拍重建——来源示例">](assets/p94-luxury-suv-night-selfie-reconstruction/source-example-01.jpg)

#### 👇 工作流

`照片参考图 → 豪华 SUV 夜间自拍重建`

#### 🔖 完整提示词

```text
将上传的图片作为唯一视觉依据。把它重建为一张高度照片级写实的竖版夜间手机自拍，拍摄于白色豪华 SUV 后排乘客座。保留女性的身份、面部比例、表情、肤色、超长中分金发、自然柔和妆容、黑色连衣裙、银色金属链节腕表、坐姿、伸出的持机手臂、抬到太阳穴旁的手、被布料覆盖并弯曲的膝盖、手袋、车厢布局、闪光灯光线、反射、透视、裁切和取景。

构图
使用竖版、广角、手臂长度的自拍透视，比例约为 1108:1420。保留主体上方充足的车顶空间。脸部位于中心略偏左，躯干处于下方中央，抬起的膝盖位于右下前景。让伸出的手臂从左边缘进入画面，并因靠近镜头而自然放大。保留底部穿过手袋、腿部和被连衣裙覆盖腿部的裁切；不要收紧成大头照。

主体与造型
表现一名成年女性：暖调浅至中等金棕肤色、柔和细长椭圆脸、低饱和棕榛色杏眼、柔和拱形灰棕眉、纤细笔直的鼻子、饱满的桃粉裸色嘴唇、可见的自然毛孔和克制的闪光高光。她的超长米金色头发带香槟色高光，接近中分，发根较深，大部分发丝笔直、末端有轻柔弯曲，并具有自然发束分离。她穿合身、不透明、哑光的黑色短袖高领连衣裙，腰部和腿部带真实褶皱。保留太阳穴旁的银色不锈钢链节腕表，以及靠近髋部、带金色链条的黑色绗缝皮革单肩包。不要添加醒目耳环或其他配饰。

姿势与表情
她随意后靠，一条膝盖抬起，直视镜头，表情平静而自信。嘴唇微张，眉毛放松，抬起的手轻靠太阳穴，手指结构和腕部旋转符合解剖。保持真实的肩部连接、肢体长度、坐姿几何和广角透视。

车辆内饰
重现带窄黑滚边的白色打孔皮革座椅和头枕、散布暖白光纤星点的象牙色打孔顶棚、斜向软包把手、仅有轻微头发与手臂倒影的深色侧窗、浅色软包立柱、亮面碳纤维饰板、抛光铬金属细节、内嵌矩形车门把手和宽大的白色皮革扶手。车外保持近乎全黑。不要添加第二个人、倒映的人脸、可见手机或明亮户外景象。

光线与相机
使用来自镜头旁的夜间手机直闪，并由白色车厢柔化。清晰照亮脸部、头发、手臂、连衣裙和附近内饰，同时保留窗户和车厢凹处的深阴影。使用中性闪光色，配合暖肤色和星光顶棚；高光受控，低光传感器纹理真实，手机锐化适中，景深较广，并具有 24–28mm 广角自拍镜头的视觉特征。最终效果必须像真实的高分辨率手机照片，而不是影棚人像。

移除所有文字、按钮、图标、时间戳、水印和界面图形。避免美颜滤镜、蜡质皮肤、过度修饰、解剖扭曲、多余手指、重复肢体、错误倒影、亮面缎料、低领、蕾丝、肩带、额外标志、人造光晕、CGI、3D 渲染、过饱和色彩、极端 HDR 或臆造的车厢元素。
```

<sub>(by [@noneugc](https://x.com/noneugc/status/2102655295335936032)) · [来源平台： X](https://x.com/noneugc/status/2102655295335936032) · 参考图改编：SeeAPI</sub>

<a id="p95-minimalist-kitchen-iphone-ugc-portrait"></a>

### 📌 1.35. 极简厨房 iPhone UGC 人像

#### 👀 预览

[<img src="assets/p95-minimalist-kitchen-iphone-ugc-portrait/source-example-01.jpg" width="224" height="400" alt="极简厨房 iPhone UGC 人像——来源示例">](assets/p95-minimalist-kitchen-iphone-ugc-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → iPhone 厨房随手拍人像`

#### 🔖 完整提示词

```text
制作一张照片级写实的竖版 iPhone 生活方式照片：一名有吸引力的成年金发女性夜间站在现代极简公寓厨房里。画面应像真实的手持深夜随拍，而不是专业时尚广告。

主体
表现一名二十多岁的成年女性，皮肤白皙并带轻微日晒感，脸型为柔和清晰的椭圆形，嘴唇自然饱满粉润，眉形精致，眼睛为蓝绿色。金发保留较深的自然发根，松散扎成略显凌乱的高发髻，并留有几缕细碎发丝。保留真实毛孔、细小面部绒毛、轻微色调变化和细小自然瑕疵。她穿一件带精致蕾丝滚边的黑色短款缎面睡袍，腰间松松系起。缎面反光应克制且符合物理规律，并呈现自然褶皱。

姿势与构图
采用自然手持手机视角，从腰部至胸部高度取景，距离主体约 2–3 米，形成竖版全身人像。将她置于左侧操作台与右侧嵌入式电器之间的中央过道附近。她以放松的对立式站姿站立，身体略微背向相机，同时回头看向镜头。保留头顶充足留白，展示高柜和嵌入式顶灯。使用中等广角的 24mm 等效透视和较深的手机景深，让人物和厨房都保持可辨识。

厨房
使用当代欧洲极简室内风格：通高哑光灰米色柜体、暖白和奶油色表面、带细腻灰色纹理的白色大理石挡板、黑色电磁炉、黑色平底锅、哑黑弧形水龙头、嵌入式黑色微波炉与烤箱、大块浅色瓷砖地面，以及干净的建筑线条。加入可信的日常细节：左下前景白色陶瓷烤盘中的新鲜咸味派或乳蛋饼、放有烤面包或糕点的木砧板、深绿色橄榄油瓶、小调味罐和透明皂液瓶。空间应有生活痕迹但不过度杂乱。

光线与相机
使用 3000–3500K 暖色嵌入式顶灯和橱柜下方 LED 灯照明。让脸部、头发、睡袍、柜体、挡板和台面获得柔和但有方向性的照明，同时在柜体下方和电器周围保留真实暗部。模拟 iPhone 17 Pro Max 主摄：24mm 等效镜头、f/1.8、ISO 400、1/60 秒、自然自动曝光、受控的顶灯高光、轻微计算锐化、真实室内降噪和暖中性白平衡。使用适中的自然对比、低饱和色彩、深黑色和最少量后期处理。

避免影棚或编辑式灯光、磨皮或塑料皮肤、夸张解剖、扭曲手部、多余手指、变形柜体、弯曲建筑线条、悬浮物件、不真实的织物反光、过度散景、镜头光斑、重胶片颗粒、极端 HDR、顶灯过曝、过度锐化、压缩伪影、文字、水印和标志。
```

<sub>(by [@cvcvta](https://x.com/cvcvta/status/2102600005693391324)) · [来源平台： X](https://x.com/cvcvta/status/2102600005693391324) · 参考图改编：SeeAPI</sub>

<a id="p96-ducati-night-motorcycle-hero-portrait"></a>

### 📌 1.36. 杜卡迪夜间机车主角人像

#### 👀 预览

[<img src="assets/p96-ducati-night-motorcycle-hero-portrait/source-example-01.jpg" width="300" height="400" alt="杜卡迪夜间机车主角人像——来源示例">](assets/p96-ducati-night-motorcycle-hero-portrait/source-example-01.jpg)

#### 👇 工作流

`文字 → 电影感夜间机车人像`

#### 🔖 完整提示词

```text
一张令人屏息的电影感 35mm 夜间照片——在夜晚的开阔柏油场地中，以亲密、迷人、低机位主角构图，拍摄一名格外漂亮的 20 岁东亚女性跨坐在哑光战舰灰超级运动摩托车上；机位与视线齐平，呈现真实的 M1 电影叙事质感。

女性拥有极其漂亮、洋娃娃般的东亚面孔，双颊柔和年轻，下巴精致收尖，瓷白肌肤明亮，并能看到细微毛孔纹理和淡淡桃色红晕。深棕色头发紧束成光滑高马尾，顺背部垂下；太阳穴和额前有柔软自然的碎发与细小胎毛。她的大号深色杏眼略微看向镜头外，神情冷静、迷人并带一点疏离，搭配自然有光泽的玫瑰色嘴唇。她身形纤细但曲线鲜明。她穿复古时髦的短款摩托赛车皮夹克，醒目的深红与黑色搭配清晰白色滚边；领口敞开，露出合身白色圆领吊带背心。下身搭配高腰黑色短裤和黑色漆皮厚底骑士靴，修长裸露的瓷白双腿与深色机械摩托形成鲜明而迷人的对比。她上身前倾伏在油箱上，胸部靠近画面，左臂支撑，右手握住黑色分离式车把；一条纤细的腿弯曲并高抬至后座整流罩旁，形成毫不费力、冷酷而迷人的骑行姿势。

摩托车是一辆线条锐利、富有攻击性的现代超级摩托，采用平滑哑光战舰水泥灰涂装，配有锐利空气动力学双前灯、亮黑色染色风挡，以及深色柏油路面上可见的机械发动机组件。深邃夜景背景融化为柔和的暗色工业纹理，远处少量琥珀色跑道标记灯被柔焦成细腻散景。

光线遵循干净的高端时尚夜间闪光物理：来自左前方、清晰且讨喜的冷色日光平衡主光，以明亮水润的清晰度照亮她瓷白的脸、锁骨和裸露双腿，同时在下颌和夹克曲线处投下自然细微阴影。她明亮的身形由此从暗色柏油和哑灰色摩托车架中漂亮地分离出来，没有人造光晕。

使用高宽容度数字电影质感，以高速 50mm 复古定焦镜头和 T1.8 大光圈拍摄；她的眼睛、睫毛、独立发丝、皮夹克缝线和金属摩托部件都具有极高光学清晰度，深色背景则优雅融化为平滑自然的虚化。使用 Kodak 日光胶片模拟，呈现浓郁饱和的深红、干净瓷白、柔滑且未压死的黑色和真实温暖肤色，并以细腻自然的 35mm 院线胶片颗粒覆盖全画面。真实电影机拍摄的真实照片画面、真实定焦镜头、真实皮夹克、真实高性能超级摩托、真实的漂亮 20 岁东亚成年女性、真实夜间柏油环境——不要 CGI、不要渲染感、不要过分数字洁净、不要塑料表面、不要 AI 平滑感、不要磨皮、不要虚假 3D 蜡质感、不要发光，也不要显得人造的光晕泛光。
```

<sub>(by [@johnAGI168](https://x.com/johnAGI168/status/2102595053021483400)) · [来源平台： X](https://x.com/johnAGI168/status/2102595053021483400)</sub>

<a id="p97-rainy-bus-stop-multi-model-benchmark"></a>

### 📌 1.37. 雨夜公交站多模型对比

#### 👀 预览

[<img src="assets/p97-rainy-bus-stop-multi-model-benchmark/source-example-01.png" width="400" height="400" alt="雨夜公交站多模型对比——来源示例 1 — GPT Image 2.5 Sunburst">](assets/p97-rainy-bus-stop-multi-model-benchmark/source-example-01.png)

[<img src="assets/p97-rainy-bus-stop-multi-model-benchmark/source-example-02.png" width="400" height="400" alt="雨夜公交站多模型对比——来源示例 2 — GPT Image 2.5 Flare">](assets/p97-rainy-bus-stop-multi-model-benchmark/source-example-02.png)

#### 👇 工作流

`同一提示词 → Sunburst 与 Flare 对比`

#### 🔖 完整提示词

```text
一名三十多岁女性在雨夜公交站的照片级写实人像，药房招牌投下柔和霓虹光，带轻微胶片颗粒，不要文字，不要水印
```

<sub>(by [u/kaboom-o](https://www.reddit.com/r/generativeAI/comments/1wmq8pj/same_prompt_five_image_models_rainy_busstop)) · [来源平台： Reddit](https://www.reddit.com/r/generativeAI/comments/1wmq8pj/same_prompt_five_image_models_rainy_busstop)</sub>

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

<a id="p83-cinema-pets-with-3d-glasses"></a>

### 📌 2.12. 戴 3D 眼镜的影院宠物

#### 👀 预览

[<img src="assets/p83-cinema-pets-with-3d-glasses/source-example-01.webp" width="400" height="400" alt="戴 3D 眼镜的影院宠物——来源示例 1">](assets/p83-cinema-pets-with-3d-glasses/source-example-01.webp)

#### 👇 工作流

`文字 → 怀旧影院宠物照片`

#### 🔖 完整提示词

```text
一只西高地白梗和一只黑白相间的猫并排坐在昏暗的电影院里，均戴着复古蓝色纸板 3D 眼镜，各自抱着一桶装满黄油爆米花的桶：狗的桶是暖橙色，猫的桶是青绿色。深蓝色天鹅绒影院座椅铺满前景和后排，来自左前方的低调银幕光照亮它们的脸。采用浅景深、1970 年代胶片照片质感、褪色的柯达色彩、明显的颗粒与灰尘斑点、轻微柔焦；正方形 1:1 裁切，画面居中对称。两只动物都望向画外的银幕，氛围怀旧，带有含蓄的幽默感。排除：现代数码锐度、HDR、卡通风格、人类的手、文字、水印、扭曲的眼睛。
```

<sub>[来源平台： Clico](https://tryclico.com/gallery/double-feature)</sub>

<a id="p84-orochi-fashion-character-concept-sheet"></a>

### 📌 2.13. OROCHI 时尚角色设定表

#### 👀 预览

[<img src="assets/p84-orochi-fashion-character-concept-sheet/source-example-01.jpg" width="400" height="225" alt="OROCHI 时尚角色设定表——来源示例">](assets/p84-orochi-fashion-character-concept-sheet/source-example-01.jpg)

#### 👇 工作流

`角色风格参考图＋设定说明 → 角色设定表`

#### 🔖 完整提示词

```text
在纯白背景上制作一张高端、现代的高定时尚角色概念设定表，采用 16:9 宽屏布局。所附参考图定义了画面风格——将它视为严格的风格准则，在设定表的每个人物上精确复现其渲染技法。

[STYLE — MIRROR THE REFERENCE EXACTLY]：忠实复现参考图的渲染方式：超写实 3D CGI 收藏级人偶渲染、基于物理的渲染、Octane Render 水准的布光，以及真实的材质表现（织物的纹理与垂坠、金属的磨损与氧化、石化木细至毛孔尺度的微观细节）。整体灯光布置和材质色板须与参考图一致（明亮、干净、白底的摄影棚拍摄效果——不要将其扁平化或处理成赛璐璐上色），使用柔和的棚拍光，以及与参考图相符的轻微轮廓光。每个人物都必须看起来像使用同一个 3D 文件、在同一套摄影棚灯光下渲染而成。

[STYLE PROHIBITIONS — ABSOLUTE]：不得使用扁平的 2D 赛璐璐上色、卡通描边、线稿、动漫风格、绘画笔触、海报化的纯色块、低多边形或游戏资产外观、塑料玩具光泽，也不得出现融合或畸形的手指。如果参考图采用写实材质，本设定表也必须如此——绝不能将其扁平化。

[PROPORTIONS]：每个人物的身体比例都要与参考图精确一致——修长的时装插画式体态（身高约 9–10 个头长、头部较小、四肢纤长、腰部窄），并延续到照片级写实渲染中。较小的姿态研究图也不能把比例改回普通人体比例。

[SUBJECT_DESCRIPTION]：角色名为 OROCHI。一个由浅色石化梣木构成的高大类人形实体，头生树枝状的角，佩戴金色圆环耳环，面部是一道虚空般的裂缝。身穿宽大垂坠的橄榄绿机能风和服外套、战术尼龙胸前绑带、深靛蓝宽腿机能袴式牛仔裤，脚穿厚重的战术凉鞋。

可见的超能力：空中漂浮着发出幽光的深红色幽灵樱花瓣；幻影般的绿色灵火环绕其木质利爪和武士刀刀身。

版面构图（严格按以下分区组织）：
1. 左侧面板：元数据与转面图——使用干净、厚重、窄体的无衬线字体，竖排突出角色名“OROCHI”。元数据块以清晰的无衬线字体写出“ROLE: PHANTOM RONIN”、“CORE MOOD: ANCIENT DREAD”和“VISUAL SIGNATURE: SPECTRAL WOOD MAGIC”。迷你转面图：3 个较小的竖向全身人物，分别标为“neutral”、“back view”、“profile”；即使尺寸较小，也要保持与参考图完全一致的风格和完整的材质细节。剪影研究：在转面图下方放置 3 个与这些姿势对应的纯黑剪影。表情研究（左下角）：恰好 4 个小幅头部特写，展现其虚空裂缝面部所发出灵火的细微变化。

2. 中央面板：主视觉——一个占据画面主导地位的巨大、完整全身人物，摆出冷静放松的标志性姿势，细节达到最高程度，并与参考图风格完美一致；拔出的武士刀周围缠绕着发光的深红色幽灵叶片和绿色灵火。

3. 右侧面板：多姿势与主题研究——姿势研究：恰好 4 到 5 个中小尺寸人物，摆出动态战斗姿势（拔刀、施放灵火、向前突刺）。每个人物下方都有一个手写风格的小标签；所有人物都使用与参考图完全一致的风格。

4. 右下面板：细节研究——恰好 5 个方形小幅局部特写，分别突出：(1) 石化木纹与金色圆环耳环；(2) 橄榄色帆布外套的织纹与战术绑带；(3) 武士刀刀刃上的幻影绿色灵火；(4) 牛仔机能袴的褶裥；(5) 握着悬浮深红花瓣的木质利爪。每个局部特写下方都加上干净的手写风格标签。
```

<sub>(by [@itsPixieVerse](https://x.com/itsPixieVerse/status/2101905822888677714)) · [来源平台： X](https://x.com/itsPixieVerse/status/2101905822888677714)</sub>

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

<a id="p75-loreva-coastal-fragrance-ad"></a>

### 📌 3.11. LORÉVA 海岸香水广告

#### 👀 预览

[<img src="assets/p75-loreva-coastal-fragrance-ad/source-example-01.jpg" width="400" height="300" alt="LORÉVA 海岸香水广告——来源示例 1">](assets/p75-loreva-coastal-fragrance-ad/source-example-01.jpg)

#### 👇 工作流

`构图参考图 + 文字 → 海岸香水广告`

#### 🔖 完整提示词

```text
为名为 LORÉVA 的虚构的高级定制香水品牌创建博物馆级香水广告主视觉，设计为单一的高级杂志风格构图，其中写实的香水瓶及其包装成为诗意景观装置的中心。将参考的构图逻辑保留为纯粹的设计逻辑：前景是一个居中的矩形玻璃香水瓶，后面是一个稍高的包装盒，下面是一个雕塑矿物基座，以及一个柔和融入画面的目的地意境，在产品后面并部分在产品表面延展。最终的形象必须比传统的香水广告更具艺术感、更内敛、更奢华，同时读起来就像一张具有收藏价值的画廊海报和一个高级时尚网站的主视觉。

产品是绝对的画面主角。瓶子必须逼真且精美渲染：厚实的透明玻璃壁、优雅的比例、淡色微光香液、微妙的折射和反射、清晰的肩部边缘、带有可见纹理的温暖天然木瓶盖，以及带有精致排版的干净标签。它后面的包装盒必须感觉像一个优质的纸制品，具有触感哑光纹理和略带风化质感的印刷图案，延伸出相同的大气景观语言，就好像香气描绘的世界仿佛藏在包装内部一样。瓶身应以清晰轮廓、静谧气质和精准材质细节占据视觉主导，而盒子则充当安静的建筑支撑。

这个概念是气味包含一个地方，但这个地方被呈现为记忆而不是插图。在产品背后和周围营造出苍白、有文化、如绘画般真实的地中海景观：褪色的沿海山脉、遥远的海岸线、柏树的轮廓、软化的石头村庄、矿物质空气和内敛的植物痕迹。这个世界应该感觉被时间冲刷过，几乎就像修复的壁画或手工着色的风景记忆，而不是真正的旅行明信片。环境意象应该轻轻地融入苍白的背景中，并部分融入盒子表面，给人一种香水是氛围、距离和沉默的容器的印象。

在底部，使用浅色岩石、苔藓、风化的石头、柔和的干茎、一两朵柔和色调的花朵和精致的半透明花瓣建造一个雕刻的静物基座。这些元素必须让人感觉是经过精心策划的、最小化的，而不是拥挤的。静物画应该像香坛一样支撑瓶子，而不是装饰造型。减少任何不必要的道具丰富，让空虚在构图中发挥积极作用。

颜色层次：60% 羊皮纸象牙色、石灰石米色、粉笔白和浅矿纸色调； 20% 苔藓绿、柏树绿、干橄榄色和柔和的植物灰绿色； 15% 柔和的葡萄酒、尘土飞扬的李子、褪色的赭色和花香勃艮第的口音； 5% 透明玻璃高光和清晰的深色字体。灯光柔和而智能：来自左前方的漫射日光、玻璃下精致的阴影池、沿着瓶子边缘的微妙高光线、穿过液体的安静光芒以及景观领域的大气深度。保持低对比度但精致，通过材料响应而不是刺眼的戏剧性照明来实现体积和分离。

排版应更冷静、更精简、更高级。将品牌名称 "LORÉVA" 置于顶部中心，采用精致的高对比度衬线，具有宽敞的呼吸空间。在左侧的空白处，只用优雅的衬线大写字母放置一条声明线："WE DISTILL DISTANCE." 在其下方添加一条非常小的支撑线，简短而智能，关于气味、记忆和地点。尽量减少或几乎不存在所有其他界面文本。版式应该感觉像是豪华展览布局的一部分，而不是商业网页横幅，并且绝不能与瓶子竞争。

材质语义必须明确而精致：厚实的玻璃折射、哑光的纸盒纤维、天然的木纹、柔和的石粉、半透明的花瓣纹理、内敛的花香深度、如水彩般柔和的山水氛围。物体与世界之间的融合必须感觉天衣无缝，就好像香水将整个地理浓缩到一个容器中。每个元素都应经过有意取舍，显得克制而宁静。

渲染目标：照片般真实的奢华香水广告、美术静物的精确性、编辑的精致性、高端的印刷效果、产品主导的层次结构、内敛的视觉诗意、优雅的负空间和国际画廊级别的审美。

结构化排除约束：没有真正的香水品牌名称，没有复制的文字，没有杂乱的花卉，没有过多的装饰水晶，没有扭曲的瓶子几何形状，没有扭曲的标签，没有难以阅读的排版，没有随机字母，没有浑浊的颜色，没有肮脏的雾霾，没有繁忙的道具造型，没有风格漂移，没有廉价的美容商业外观，没有人工智能工件。
```

<sub>(by [@ou_zhen599](https://x.com/ou_zhen599/status/2101557541318910089)) · [来源平台： X](https://x.com/ou_zhen599/status/2101557541318910089)</sub>

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

<a id="p74-colossal-squid-harbor-poster"></a>

### 📌 4.20. 巨型鱿鱼港湾海报

#### 👀 预览

[<img src="assets/p74-colossal-squid-harbor-poster/source-example-01.jpg" width="400" height="400" alt="巨型鱿鱼港湾海报——来源示例 1">](assets/p74-colossal-squid-harbor-poster/source-example-01.jpg)

#### 👇 工作流

`构图参考图 + 文字 → 鱿鱼港湾插画海报`

#### 🔖 完整提示词

```text
为名为 TIDEKRAKEN 的虚构沿海美食品牌制作优质插图海鲜广告海报，将其提炼为更高级、更豪华的Orbit-plus-Transit 风格方向。将其设计为单一垂直组合的商业海报，其中巨大的新鲜鱿鱼是绝对的核心食材，以雕塑般的优雅主宰着框架，而精心策划的港口生活微观世界则在其身体、触手、码头和周围的水域中展开。仅将参考的核心构图要点保留为视觉逻辑：巨大的中央鱿鱼，顶部坐着的成年女性吉祥物，左上角的大胆标题区域，以及以严格的节奏分布在产品周围的层次丰富的微型场景。结果一定不像一部可爱的节日卡通片，而更像是一场全球获奖的美食插画活动：精致、具有收藏价值、诙谐且高度艺术化。

鱿鱼是产品的核心图标，一定会让人感到难以抗拒的优质感。以精致的编辑插图风格渲染，具有精致的海洋纹理：温暖的珊瑚桃肉、微妙的辣椒粉斑点、湿润的表面亮点、肉质触手的重量、优雅的吸盘结构、干净的自然解剖结构，以及从远处即可立即读取的宏伟雕塑轮廓。它不是怪诞的，不是喜剧恐怖的，也不是混乱的。它是一种宏伟的食材，转变为不朽的美食风景。鱿鱼身上和周围的每一个微观场景都必须强化其作为明星食材的吸引力。

围绕鱿鱼构建的世界应该比以前更加精心策划和选择性。微型港口场景仍然存在，但层次感更强，呼吸空间更大：一些精致的码头平台，优雅的海鲜烧烤台，品酒桌，小渔船，悬挂的渔线，以及故意间隔排列的小型市场人物。减少低值噪声。让最精彩的场景感觉像是社论的小插曲，而不是随机的人群混乱。下部触手应形成优雅的弧线，像书法笔画一样引导视线穿过海报，支持优质的流程和图形节奏。

鱿鱼的顶部坐着一位成年女性，以精致的沿海社论风格描绘，平静而诱人，而不是过于顽皮。她穿着一套精致的工作服风格的服装：头巾、卷袖、围裙元素、宽松的裤子和暖色调的鞋子，所有这些都简化为优雅的造型语言。她拿着鱿鱼串作为象征性的产品线索。她的身材必须明显是成人的，比例正确的插图，平衡的肩膀，自然的坐姿重量，可读的手，五个手指（可见）和泰然自若的姿势。她充当品牌大使，但她必须保持对鱿鱼的次要地位。

环境应该感觉像是一个高端港口美食世界，而不是一个喧闹的游乐场。在上场使用浅色开放背景空间来保持海报的精致度。在下半部分，整合了选择性海域、饱经风霜的渔船、安静的海鸥、绳索纹理、浮动平台和烤架上的一些烟羽。保持微风景丰富而优雅，与密集的儿童插画相比，具有更好的视觉编辑和更多的负空间。想想美食季节海报，而不是漫画混乱。

颜色层次：50%暖色调鱿鱼珊瑚色、贝壳粉色、海盐桃色、烤辣椒色调； 20% 海洋蓝、港青色和柔和的风化海军蓝； 20% 羊皮纸白、矿物奶油色和日晒褪色的中性空间； 10% 木炭墨水线条、柔和的铁锈细节和版式。使用清晰的线条、微妙的水粉水彩填充行为、内敛的纹理和优质的打印清晰度。渲染应该给人一种手工制作和智能的感觉，具有清晰的轮廓规则和精致的色彩分离。让调色板稍微灰一点、更优雅、更国际化。

版式必须在权威上更加大胆，但在完成上更加复杂。在左上角，创建一个大型定制黑色毛笔标题块，具有更强的豪华海报节奏，例如 "SQUID SOCIETY" 或 "THE SQUID TABLE" ，堆叠着动态但受控的形状能量。在其下方，仅放置一条短支撑线，最小且尖锐，例如 "Season arrives in salt and fire." 减少所有其他标语文本。在微型市场世界中只使用一些微小的设计标志，并保持它们稀疏、干净和有意。版式必须感觉像是海报图形构成的一部分，而不是分散的新奇标牌。

材料和食物线索必须奢华而令人胃口大开：光滑的烤釉、烤串上烧焦的边缘、风化的码头木材、潮湿的海水倒影、绳索纤维、彩绘船、海鲜烧烤的烟带、干净的市场板条箱和优雅的电镀细节。每种规格的鱿鱼都必须保持新鲜、优质且令人向往。整张海报应该感觉像是一场荣获戛纳电影节大奖的美食宣传片，将一种标志性食材变成了一个完整的季节性宇宙。

输出目标：一张完成的插图海报，优质的商业品质，产品主导的层次结构，精致的微观故事讲述，受控的负空间，优雅的海岸能量，强大的轮廓可读性，大胆的收藏标题设计，以及世界一流的海报完成。

排除和质量限制：没有恐怖鱿鱼，没有血腥，没有腐烂的海鲜，没有泥泞的纹理，没有低端卡通外观，没有混乱的人群杂乱，没有变形的触手，没有破碎的吸盘，没有解剖学崩溃，没有童趣的吉祥物比例，没有畸形的手，没有多余的手指，没有缺失的手指，没有融合的手指，没有难以阅读的文字，没有随机字母，没有廉价的节日传单审美，没有风格漂移，没有AI 套路感，没有真实品牌名称，没有真实的人名。
```

<sub>(by [@ou_zhen599](https://x.com/ou_zhen599/status/2101586769250783463)) · [来源平台： X](https://x.com/ou_zhen599/status/2101586769250783463)</sub>

<a id="p76-avelora-coastal-bridge-car-poster"></a>

### 📌 4.21. AVELORA 海岸大桥汽车海报

#### 👀 预览

[<img src="assets/p76-avelora-coastal-bridge-car-poster/source-example-01.jpg" width="300" height="400" alt="AVELORA 海岸大桥汽车海报——来源示例 1">](assets/p76-avelora-coastal-bridge-car-poster/source-example-01.jpg)

#### 👇 工作流

`构图参考图 + 文字 → 俯瞰汽车海报`

#### 🔖 完整提示词

```text
为名为 AVELORA 的虚构豪华豪华 GT 旅行车品牌制作优质汽车艺术海报活动，设计为具有巨大自上而下视角的单一垂直空中构图。保留参考图的构图逻辑作为纯粹的视觉建筑：左边是一片广阔的发光的沿海水域，右边是被太阳烤焦的土块，以及一座在框架右侧附近垂直延伸的严格的线性桥梁。真正的核心产品是一辆沿着桥行驶的石墨金属豪华旅行轿车，视觉上很小，但通过布局、对比度和周围有规律的空虚，在构图上占据主导地位。最终的图像必须感觉更艺术、更高级，并且比传统的汽车广告更像博物馆级的国际广告海报。

这个概念是运动在景观中写下一段无声的乐谱。海洋、海岸线、农业几何形状、海岸线曲率、尾流线和陆地痕迹必须暗示节奏、共鸣和管弦乐顺序，而不能成为说明性或字面意义。图像应该感觉像是由地理形态谱写的音乐。这座桥读起来就像是大地画布上的一条决定性的线，而汽车读起来就像是唯一重要的音符。

左边的大海一定是深邃的、矿物质的、如照片般真实的绘画：饱和但优雅的地中海蓝色、青色的深度变化、苍白的波浪边缘，以及从远处的几艘船留下的细长的白色尾迹，感觉就像是手势划过海面。右边的土地必须是干燥的、有质感的、有雕塑感的：赤土土地、氧化赭土、尘土飞扬的棕土、苍白的沙坑，以及嵌入地形中的微妙螺旋或书法土地痕迹，仿佛地球本身记得运动。海岸线应该感觉自然切割、不规则且美丽，有白色的海岸泡沫和可信的侵蚀线。每个宏观形状都必须让人感觉是经过精心设计的，但绝不是做作的。

该车是一款真正的高级轿车，高度真实，设计精密：低矮而优雅的车身线条，深色全景车顶玻璃，微妙的金属反射，清晰的车窗装饰，精致的车轮设计，逼真的轮胎接触，以及平静的速度感而不是激进的运动模糊。尽管车辆规模较大，但必须通过受控的道路对比度、精确的阴影以及在桥上的精确定位来保持清晰易读。桥梁表面是完美无瑕的深色沥青，带有薄薄的浅色车道标记、工程边缘和最小的结构中断，呈现出一条纯粹的现代主义线条穿过海洋和陆地。

颜色层次：55% 发光的深蓝色和青色水色，25% 暖铜色、铁锈色、陶土色和矿土色，10% 木炭桥和石墨车，10% 柔和的白色尾流线和版式。照明是高空日光，但精致成美术色调：清爽的海岸阳光、水和土壤中的雕刻纹理、精确的白色泡沫边缘、非常微妙的大气扩散以及强烈的微对比度，而没有严重的过度锐化。图像必须给人干净、昂贵、透气和全球优质的感觉。

排版必须比以前更少、更冷、更精致。总共仅使用两个文本元素。在左上角的开放水域，放置一个优雅的标题："Composed for Distance." 采用现代精致的无衬线字体或内敛的高级时尚衬线无衬线字体混合，亮白色，精心调整字距，显得克制而有力量。在右上角，仅使用极简品牌区块： "AVELORA" 。没有额外的描述符，没有网站，没有说明性文案，没有混乱的信息。排版应该感觉像是画廊级的杂志式设计，悬浮在负空间中，永远不会与景观或汽车竞争。

材质语义必须明确且提升：富含矿物质的水深、白垩海岸线、干燥的农业土壤、工程沥青、金属汽车油漆、反光玻璃、微妙的车底阴影和精细的航空摄影纹理。整个构图必须被解读为一场以产品为主导的奢华活动，其中汽车将景观转变为一种情感运动工具。

渲染目标：照片般真实的豪华汽车广告、航空美术写实主义、概念智能构图、优质社论海报完成、干净的负空间、克制的排版、世界一流的印刷质量以及工程、地形和视觉诗意之间的无缝和谐。

结构化的排除约束：没有真正的汽车品牌，没有复制的标语，没有乱码的排版，没有难以阅读的文字，没有多余的车辆凌乱在桥上，没有低分辨率的汽车，没有扭曲的海岸线，没有卡通音乐符号，没有扭曲的桥梁几何形状，没有泥水，没有肮脏的雾霾，没有廉价的旅游海报外观，没有过饱和的旅游审美，没有风格漂移，没有人工智能伪影，没有重复的船，没有视觉混乱。
```

<sub>(by [@ou_zhen599](https://x.com/ou_zhen599/status/2101556753762586720)) · [来源平台： X](https://x.com/ou_zhen599/status/2101556753762586720)</sub>

<a id="p82-culinary-vapor-monument-poster"></a>

### 📌 4.22. 蒸汽纪念碑式美食海报

#### 👀 预览

[<img src="assets/p82-culinary-vapor-monument-poster/source-example-01.jpg" width="268" height="400" alt="蒸汽纪念碑式美食海报——来源示例 1">](assets/p82-culinary-vapor-monument-poster/source-example-01.jpg)

[<img src="assets/p82-culinary-vapor-monument-poster/source-example-02.jpg" width="268" height="400" alt="蒸汽纪念碑式美食海报——来源示例 2">](assets/p82-culinary-vapor-monument-poster/source-example-02.jpg)

#### 👇 工作流

`菜品变量 → 蒸汽美食海报`

#### 🔖 完整提示词

```text
竖版美食纪念碑式海报。将一道 [DISH] 摆放在 [SURFACE] 上，居中置于高耸的 [VAPOR] 气柱下方；气柱成为画面的主要图形结构。蒸汽应具有建筑感：层叠的半透明平面，而非蓬松的卡通蒸汽。[HUMAN] 只以手和前臂的形式从 [ENTRY] 伸入画面，穿着 [SLEEVES]，正在进行 [ACTION]。背景是平面化的 [KITCHEN PLANE]，只保留一件有用的物品：[UTENSIL]。配色：[PALETTE]。在蒸汽后方放置放大的数字“[NUMBER]”。底部以紧凑的窄体字体写出菜名“[DISH NAME]”。呈现热度、度量感与静谧感。画幅比例 4:5。
```

<sub>(by [@miratechtool](https://x.com/miratechtool/status/2101560392589758614)) · [来源平台： X](https://x.com/miratechtool/status/2101560392589758614)</sub>

<a id="p90-photo-to-illustration-editorial-poster"></a>

### 📌 4.23. 照片转手绘插画编辑海报

#### 👀 预览

[<img src="assets/p90-photo-to-illustration-editorial-poster/source-example-01.jpg" width="300" height="400" alt="照片转手绘插画编辑海报——来源示例 1">](assets/p90-photo-to-illustration-editorial-poster/source-example-01.jpg)

[<img src="assets/p90-photo-to-illustration-editorial-poster/source-example-02.jpg" width="300" height="400" alt="照片转手绘插画编辑海报——来源示例 2">](assets/p90-photo-to-illustration-editorial-poster/source-example-02.jpg)

#### 👇 工作流

`照片参考图 → 照片与插画结合的编辑海报`

#### 🔖 完整提示词

```text
将上传的图片作为精确参考。保留原始主体、身份、姿势、构图、色彩、光线、背景和关键细节。不要添加、删除或重新排列主要元素。

制作一张竖版 3:4 编辑海报，分为上下两个部分：

- 上半部分：保持原始照片自然、清晰，基本不作改动。
- 下半部分：以柔和水彩、彩色铅笔和细腻墨线速写风格，将完全相同的场景重新绘制成精致的手绘插画。

保持相同的主体、位置、透视和可辨识细节。使用柔和的粉彩色调、暖白色纸张背景、细微纸张纹理，以及高级编辑设计／艺术画册／明信片的质感。在照片与插画之间加入柔和、无缝的过渡。

加入极简而优雅的排版：一个手写风格标题和一行简洁的小副标题。根据情境使用合适的原样文字，例如 “A Brighter Day” 和 “A Slower Life”；宠物或家庭场景可使用 “Good Friends”、“Brighter Days” 或 “Happier Tails ♡”。

可选：仅在自然契合画面时，加入少量细腻的手绘装饰，例如小花瓣、叶片、爱心或速写笔触。

不要改变人物身份或场景，也不要让下半部分呈现照片写实、3D、动漫或卡通效果。
```

<sub>(by [@miratechtool](https://x.com/miratechtool/status/2102656456478589340)) · [来源平台： X](https://x.com/miratechtool/status/2102656456478589340)</sub>

<a id="p91-cinematic-paper-memory-poster"></a>

### 📌 4.24. 电影感纸艺记忆海报

#### 👀 预览

[<img src="assets/p91-cinematic-paper-memory-poster/source-example-01.jpg" width="288" height="360" alt="电影感纸艺记忆海报——来源示例 1">](assets/p91-cinematic-paper-memory-poster/source-example-01.jpg)

[<img src="assets/p91-cinematic-paper-memory-poster/source-example-02.jpg" width="288" height="360" alt="电影感纸艺记忆海报——来源示例 2">](assets/p91-cinematic-paper-memory-poster/source-example-02.jpg)

#### 👇 工作流

`文字 → 电影感人像与分层纸艺记忆海报`

#### 🔖 完整提示词

```text
制作一张高级 4:5 编辑艺术海报，呈现一个原创角色和一段视觉丰富的个人故事。

上半部分应是在与角色故事相关的自然环境中拍摄的高度写实电影感人像。赋予角色鲜明的外貌、真实的表情、写实的皮肤纹理、可信的服装，以及经过精心构成的环境细节。场景应像高端旅行或生活方式杂志中的电影画面。

让同一构图的下半部分逐渐转化为精细的手工分层剪纸艺术。完全通过裁切和塑形纸张重新诠释角色、周围环境、地标、物件和细小叙事元素。使用堆叠纸层、精细裁切的轮廓、轻微压纹、折叠和撕裂边缘、可触摸的纤维、微缩细节，以及细腻阴影形成的真实景深。

让纸艺在视觉上延续上方照片中的元素，仿佛现实世界正在展开为一个微缩的手工世界。加入与角色所在城市、职业、热爱、旅行或个人经历相关的视觉母题，而不是简单复制照片场景。

使用温暖象牙白、羊皮纸色、低饱和大地色、灰调中性色和克制强调色组成的精致色板，并呈现可见纸张颗粒和手工瑕疵。加入优雅的编辑排版，使用精致衬线字体、简短的虚构姓名或标题，以及最少量的辅助文字。

构图：高级杂志封面美学、清晰的视觉层级、充足留白、平衡对称、高端艺术指导、细微电影感光线、可触摸的真实质感和博物馆级纸艺工艺。

核心视觉概念：一个真实的电影瞬间逐渐演变为手工纸艺记忆。

不要使用参考图，不使用现有名人肖像，也不要复制既有构图。从零开始创作角色、环境和叙事，同时让整个画面保持精致且可辨识的统一视觉身份。
```

<sub>(by [@j_smeaton99](https://x.com/j_smeaton99/status/2102653995919487110)) · [来源平台： X](https://x.com/j_smeaton99/status/2102653995919487110)</sub>

<a id="p93-collectible-souvenir-box-travel-posters"></a>

### 📌 4.25. 收藏式旅行纪念盒海报

#### 👀 预览

[<img src="assets/p93-collectible-souvenir-box-travel-posters/source-example-01.jpg" width="320" height="400" alt="收藏式旅行纪念盒海报——来源示例 1">](assets/p93-collectible-souvenir-box-travel-posters/source-example-01.jpg)

[<img src="assets/p93-collectible-souvenir-box-travel-posters/source-example-02.jpg" width="320" height="400" alt="收藏式旅行纪念盒海报——来源示例 2">](assets/p93-collectible-souvenir-box-travel-posters/source-example-02.jpg)

[<img src="assets/p93-collectible-souvenir-box-travel-posters/source-example-03.jpg" width="320" height="400" alt="收藏式旅行纪念盒海报——来源示例 3">](assets/p93-collectible-souvenir-box-travel-posters/source-example-03.jpg)

[<img src="assets/p93-collectible-souvenir-box-travel-posters/source-example-04.jpg" width="320" height="400" alt="收藏式旅行纪念盒海报——来源示例 4">](assets/p93-collectible-souvenir-box-travel-posters/source-example-04.jpg)

#### 👇 工作流

`国家变量 → 收藏式旅行纪念盒海报`

#### 🔖 完整提示词

```text
为 [COUNTRY] 制作一张高级 4:5 竖版 Instagram 旅行海报，作为统一的收藏式 “Souvenir Box” 系列之一。

展示一个打开的复古纸板旅行盒，内含恰好 10 件来自 [COUNTRY]、具有真实文化特征的纪念品：1 件主角物件、2–3 件辅助物件，以及若干更小的纪念物。选择材质、尺寸、形状和文化意义各不相同的物件。

加入恰好 4 个纸质元素：

- 一张折叠插画地图，展示 4 个不同目的地
- 一张带齿孔的复古旅行票
- 一张模切 [COUNTRY] 目的地贴纸
- 一件符合当地文化的纸艺元素

使用带细微纤维和瑕疵的温暖纹理纸背景。在盒子后方放置巨大的做旧窄体 “[COUNTRY]” 字样。

从该国的风景、建筑、传统工艺和文化中汲取灵感，设计独特配色，包括主色、辅助色、暖中性色、强调色和深色文字色。

风格

高级可触摸的 3D 收藏插画＋复古国际旅行海报＋编辑杂志封面＋怀旧包装设计。使用柔和影棚灯光、真实接触阴影、细微环境光遮蔽、材质颗粒、纸张纹理和手工瑕疵。保持精致和可触摸的质感，避免光亮 CGI 效果。

加入克制的旅行票据元素：4–7 个邮戳／徽章／标签、一个抵达印记、邮资细节、路线箭头、坐标、小型旅行元数据、一句符合文化语境的当地语言短语，以及：

“COLLECT MEMORIES NOT THINGS.”

保持清晰层级：

COUNTRY 标题 → 主角纪念品 → 辅助物件 → 其余纪念物 → 图形细节。

使用强留白、平衡构图、丰富但受控的细节，以及出色的缩略图可读性。

每个国家都必须依据自身文化身份获得全新原创构图。绝不要复制其他参考图的版式、物件、字体排列或视觉构图。
```

<sub>(by [@Goodmanprotocol](https://x.com/Goodmanprotocol/status/2102630540293837041)) · [来源平台： X](https://x.com/Goodmanprotocol/status/2102630540293837041)</sub>

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

<a id="p86-global-dish-ingredient-provenance-map"></a>

### 📌 6.8. 全球菜肴食材溯源图

#### 👀 预览

[<img src="assets/p86-global-dish-ingredient-provenance-map/source-example-01.jpg" width="400" height="225" alt="全球菜肴食材溯源图——来源示例">](assets/p86-global-dish-ingredient-provenance-map/source-example-01.jpg)

#### 👇 工作流

`四种菜肴变量 → 食材溯源图`

#### 🔖 完整提示词

```text
16:9，$ DISH: [A, B, C, D, each a lesser known under rated dishes from various countries around the world]；$ VIEW: "ingredient provenance network converging on final plating"；$ MEDIUM: "gastronomic manuscript with supply-chain cartography"。为 [$DISH] 制作一本美食手稿，以汇聚图的形式展示每种食材从产地到最终摆盘的旅程。画面中央悬浮着成品菜肴，以精美的照片级写实细节呈现——蒸汽升腾、质地闪亮，并盛放在符合其时代背景的餐具中——成为发光的视觉焦点。每种食材的溯源路线像车轮辐条一样从菜肴向外辐射，沿线追踪其来源。一颗番茄的路线经过市场摊位、配送仓库、农田，最终抵达安第斯山脉中该具体栽培品种的遗传起源。一种香料的路线则在一幅微型大航海时代地图上跨越海洋贸易航线。每条路线都采用相应食材的代表色——藏红花金、罗勒绿、辣椒红——并依据该食材在菜谱中的重要程度改变线条粗细。
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2101941248022249841)) · [来源平台： X](https://x.com/Gdgtify/status/2101941248022249841)</sub>

<a id="p87-voxel-brain-teaser-posters"></a>

### 📌 6.9. 体素风烧脑题海报

#### 👀 预览

[<img src="assets/p87-voxel-brain-teaser-posters/source-example-01.jpg" width="320" height="400" alt="体素风烧脑题海报——来源示例 1">](assets/p87-voxel-brain-teaser-posters/source-example-01.jpg)

[<img src="assets/p87-voxel-brain-teaser-posters/source-example-02.jpg" width="320" height="400" alt="体素风烧脑题海报——来源示例 2">](assets/p87-voxel-brain-teaser-posters/source-example-02.jpg)

[<img src="assets/p87-voxel-brain-teaser-posters/source-example-03.jpg" width="320" height="400" alt="体素风烧脑题海报——来源示例 3">](assets/p87-voxel-brain-teaser-posters/source-example-03.jpg)

#### 👇 工作流

`主题变量 → 体素风谜题海报`

#### 🔖 完整提示词

```text
4 张图，4:5，围绕数学、科学、逻辑和谜语生成难到连智商 150 的人都会抓狂的烧脑题。输入：$ TOPIC。# 在该主题上建立难度场 D。D = infer_conceptual_depth($ TOPIC) # 按 D 的递增阈值抽取 4 道题。Q1 = generate_question($ TOPIC, difficulty='easy') Q2 = generate_question($ TOPIC, difficulty='medium') Q3 = generate_question($ TOPIC, difficulty='hard') Q4 = generate_question($ TOPIC, difficulty='brutal') # 将 Q1–Q4 渲染为体素风海报。
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2101753259325063485)) · [来源平台： X](https://x.com/Gdgtify/status/2101753259325063485)</sub>

<a id="p89-endangered-animal-infographic"></a>

### 📌 6.10. 濒危动物信息图

#### 👀 预览

[<img src="assets/p89-endangered-animal-infographic/source-example-01.webp" width="267" height="400" alt="濒危动物信息图——来源示例">](assets/p89-endangered-animal-infographic/source-example-01.webp)

#### 👇 工作流

`动物资料研究 → 图解信息图`

#### 🔖 完整提示词

```text
制作一张视觉丰富的濒危动物信息图。先在线寻找一种濒危动物，研究其栖息地、食性和独特特征。通过带标注的视觉元素和结构化说明框呈现信息，而不要使用泛泛的章节。风格如大胆的平面插画：以细节丰富、照片级写实的动物作为画面中心，辅以图解、标注和简洁的文字元素。使用干净的背景，将照片写实效果与有力的图形元素（形状、图标、色块）结合，形成有层次的构图。让画面信息密集、富有触感，并呈现专业作者的制作水准。
```

<sub>[来源平台： Vanikya](https://vanikya.ai/gpt-image-2-5#education-poster)</sub>

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
