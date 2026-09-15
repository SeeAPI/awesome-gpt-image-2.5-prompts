# P53. 自适应复古城市旅行海报

[English](../p53-adaptive-vintage-city-travel-poster.md) | [简体中文](p53-adaptive-vintage-city-travel-poster.md)

## 👀 预览

[<img src="../../assets/p53-adaptive-vintage-city-travel-poster/source-example-01.jpg" width="283" height="400" alt="自适应复古城市旅行海报——来源示例">](../../assets/p53-adaptive-vintage-city-travel-poster/source-example-01.jpg)

[<img src="../../assets/p53-adaptive-vintage-city-travel-poster/source-example-02.jpg" width="283" height="400" alt="自适应复古城市旅行海报——来源示例">](../../assets/p53-adaptive-vintage-city-travel-poster/source-example-02.jpg)

[<img src="../../assets/p53-adaptive-vintage-city-travel-poster/source-example-03.jpg" width="283" height="400" alt="自适应复古城市旅行海报——来源示例">](../../assets/p53-adaptive-vintage-city-travel-poster/source-example-03.jpg)

[<img src="../../assets/p53-adaptive-vintage-city-travel-poster/source-example-04.jpg" width="302" height="400" alt="自适应复古城市旅行海报——来源示例">](../../assets/p53-adaptive-vintage-city-travel-poster/source-example-04.jpg)

## 👇 工作流

`城市名 + 风格参考图 → 复古旅行海报`

## 🔖 完整提示词

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
