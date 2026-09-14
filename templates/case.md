# {ID}. {English Title}

## 👀 Preview

{Embed each actual image with an img tag bounded by 400 × 400, preserving aspect ratio. Link to the original file. Distinguish reference, output, and comparison roles.}

## 👇 Workflow

`{Input → output}`

{Concise required-input or reproduction notes. Do not invent missing references or imply independent generation tests.}

## 🔖 Full Prompt

```text
{Complete prompt matching the canonical English .txt file. Preserve source evidence, literal output text, code, model IDs, and [placeholder] keys.}
```

{Repeat additional steps and full prompt blocks in workflow order. Do not add standalone italic placeholder-replacement notes.}

<sub>{Author credit} · {Platform-labelled public source link} · {Translation/adaptation credit when applicable}</sub>

## Bilingual maintenance / 双语维护

Register title_zh, prompts_zh and reviewed translation_source_sha256 in catalog.json. Store each complete reviewed Chinese prompt as a sibling *.zh-CN.txt; preserve code, literal output text and placeholder keys. Keep a Chinese source original when the English canonical prompt is a translation, and label the translation.

Update docs/i18n/zh-CN.json, then run scripts/build_chinese_readme.py. Do not edit generated cases/zh-CN pages directly. In both READMEs, place each case once in its primary category using catalog.display_number and an explicit legacy anchor. Keep the Preview / Workflow / Full Prompt structure, 📌 before P-series display numbers, and source credits only in the final sub footer. Follow AGENTS.md for category order and Contents layout.

先审核中英文提示词，再更新源文件哈希并生成中文页面；不得只更新哈希绕过翻译审核。按主分类展开一次，展示编号分类内连续，内部 ID 与英文 slug 不变，来源位于最后的 sub 小字中。
