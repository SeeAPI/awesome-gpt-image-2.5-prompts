# P79. 双人健身自拍重建

[English](../p79-two-woman-fitness-selfie-reconstruction.md) | [简体中文](p79-two-woman-fitness-selfie-reconstruction.md)

## 👀 预览

[<img src="../../assets/p79-two-woman-fitness-selfie-reconstruction/source-example-01.jpg" width="225" height="400" alt="双人健身自拍重建——来源示例 1">](../../assets/p79-two-woman-fitness-selfie-reconstruction/source-example-01.jpg)

## 👇 工作流

`参考照片 → 双人健身自拍重建`

## 🔖 完整提示词

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
