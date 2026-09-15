# P43. Foodie Cities in Sculptural Typography

## 👀 Preview

[<img src="../assets/p43-foodie-cities-in-sculptural-typography/source-example-01.jpg" width="400" height="225" alt="Foodie Cities in Sculptural Typography — source example">](../assets/p43-foodie-cities-in-sculptural-typography/source-example-01.jpg)

## 👇 Workflow

`Place or culture parameter → sculptural typography image`

## 🔖 Full Prompt

```text
WITH identity AS (     SELECT        derive_display_name([PLACE_OR_CULTURE])          AS display_name,         infer_signature_foods([PLACE_OR_CULTURE])        AS foods,         infer_signature_materials([PLACE_OR_CULTURE])    AS materials,         infer_landmarks([PLACE_OR_CULTURE])              AS landmarks,         infer_objects([PLACE_OR_CULTURE])                AS objects,         infer_palette([PLACE_OR_CULTURE])                AS palette,         infer_three_values([PLACE_OR_CULTURE])           AS values,         infer_keyword_stack([PLACE_OR_CULTURE], 4)       AS keywords ),  glyph_assignment AS (     SELECT        glyph,         argmax(             source_item,             shape_match(glyph, source_item)             * cultural_relevance(source_item)             * visual_uniqueness(source_item)         ) AS source_material     FROM letters(display_name)     CROSS JOIN cultural_pool(foods, materials, objects) )  SELECT render FROM editorial_travel_stilllife_archive WHERE hero_typography = build_3d_word(     display_name,     material_per_glyph = glyph_assignment.source_material ) AND foreground = infer_culinary_stilllife([PLACE_OR_CULTURE]) AND background = infer_soft_focus_architecture([PLACE_OR_CULTURE]) AND base = 'premium sculptural plinth' AND base_caption = join(values, ' • ') AND side_stack = keywords AND lighting = 'warm sunlit premium editorial' AND styling = 'travel magazine × culinary still life × crafted typography' ORDER BY    cultural_specificity DESC,     glyph_legibility DESC,     material_variety DESC,     tactile_realism DESC,     composition_balance DESC LIMIT 1;
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2099299591485354266)) · [Source: X](https://x.com/Gdgtify/status/2099299591485354266)</sub>
