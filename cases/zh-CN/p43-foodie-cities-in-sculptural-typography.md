# P43. 美食城市雕塑字形

[English](../p43-foodie-cities-in-sculptural-typography.md) | [简体中文](p43-foodie-cities-in-sculptural-typography.md)

## 👀 预览

[<img src="../../assets/p43-foodie-cities-in-sculptural-typography/source-example-01.jpg" width="400" height="225" alt="美食城市雕塑字形——来源示例">](../../assets/p43-foodie-cities-in-sculptural-typography/source-example-01.jpg)

## 👇 工作流

`地点或文化参数 → 雕塑字形图片`

使用前填写 [PLACE_OR_CULTURE]。来源预览组合了四座城市，但原提示词未包含这一分组指令。SQL 风格文本是视觉提示词，并非可执行的数据库代码；中英文均保留其标识符和字符串字面量。

## 🔖 完整提示词

```text
WITH identity AS (     SELECT        derive_display_name([PLACE_OR_CULTURE])          AS display_name,         infer_signature_foods([PLACE_OR_CULTURE])        AS foods,         infer_signature_materials([PLACE_OR_CULTURE])    AS materials,         infer_landmarks([PLACE_OR_CULTURE])              AS landmarks,         infer_objects([PLACE_OR_CULTURE])                AS objects,         infer_palette([PLACE_OR_CULTURE])                AS palette,         infer_three_values([PLACE_OR_CULTURE])           AS values,         infer_keyword_stack([PLACE_OR_CULTURE], 4)       AS keywords ),  glyph_assignment AS (     SELECT        glyph,         argmax(             source_item,             shape_match(glyph, source_item)             * cultural_relevance(source_item)             * visual_uniqueness(source_item)         ) AS source_material     FROM letters(display_name)     CROSS JOIN cultural_pool(foods, materials, objects) )  SELECT render FROM editorial_travel_stilllife_archive WHERE hero_typography = build_3d_word(     display_name,     material_per_glyph = glyph_assignment.source_material ) AND foreground = infer_culinary_stilllife([PLACE_OR_CULTURE]) AND background = infer_soft_focus_architecture([PLACE_OR_CULTURE]) AND base = 'premium sculptural plinth' AND base_caption = join(values, ' • ') AND side_stack = keywords AND lighting = 'warm sunlit premium editorial' AND styling = 'travel magazine × culinary still life × crafted typography' ORDER BY    cultural_specificity DESC,     glyph_legibility DESC,     material_variety DESC,     tactile_realism DESC,     composition_balance DESC LIMIT 1;
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2099299591485354266)) · [来源平台： X](https://x.com/Gdgtify/status/2099299591485354266) · 来源示例；模型声明未经独立验证。</sub>
