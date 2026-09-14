# Repository maintenance / 仓库维护

- Maintain English and Simplified Chinese together. Every public content change must update `README.md`, `README_zh.md`, the affected English/Chinese cases, and both prompt languages. Keep existing IDs, source credits, media, placeholders, and workflow steps consistent.
- 所有公开内容修改必须同步中英文。中文页面不能省略完整提示词或现有示例图；目录在当前语言的 README 内定位。标题翻译不改变既有 ID 或英文 slug。
- English prompts remain the canonical source; store reviewed Chinese translations as sibling `*.zh-CN.txt` files. Preserve literal output text, model IDs, code, and `[placeholder]` keys. Translation does not prove equivalent model output or transfer source authorship.
- 中文翻译保留要求生成的原样文字、模型 ID、代码与占位符名称。修改英文提示词后，复核对应中文，再更新 catalog 中的 `translation_source_sha256`；不得只重算哈希来绕过翻译审核。
- Translate new UI prose in `docs/i18n/zh-CN.json`, then run `python3 scripts/build_chinese_readme.py`. Generated Chinese case pages live in `cases/zh-CN/`; do not edit them directly.
- 新增界面文字先更新翻译表，再生成中文页面。中英文数量与真实内容更新日期必须和 `catalog.json` 一致。
- Before publishing, run `python3 scripts/validate_catalog.py`, `python3 scripts/build_chinese_readme.py --check`, and `git diff --check`. Pull before publishing and preserve unrelated work. Never force push.
- 发布前运行以上校验，先拉取远端再整合推送。不更改无关工作，不强制推送。
- Keep the existing three-part case format (Preview / Workflow / Full Prompt; 预览 / 工作流 / 完整提示词), source platforms in the directory, and five creative IDs C01/C02/C04/C05/C06. P41/P42 have supplied before/after previews; preserve both originals and do not claim independent generation tests.
- 保留案例三段式、目录中的来源平台及五个创意案例稳定 ID。P41/P42 已有用户提供的前后对比图，保留原图，不冒称独立实测。现阶段不开放外部投稿，不增加产品引流链接。

- Featured order: Pixel Art GIF → Minecraft Skin → Bedroom Redesign. Keep directory links free of emoji; put 📌 before P-series case numbers in the expanded README headings, preserving existing anchors.
- 精选顺序固定为 GIF → Minecraft → 卧室改造。目录列表不加 emoji；README 展开的 P 系列案例标题在编号前加 📌，保留既有锚点。

## Category-first layout / 按分类展示

Use one Contents list and seven category sections. Each case appears once under its primary category in catalog.json. Keep the five creative cases together in the final GIF & Video Workflows category. Do not restore the separate Browse by Category block, full P-number directory, or creative overview table. Preserve existing case anchors and IDs. Place source/author credit in the expanded case title, including the source platform.

使用一个目录与七个分类正文，每个案例只在 catalog.json 的主分类中展开一次。五个创意案例全部放在最后的 GIF 与视频工作流分类。不恢复独立分类索引、全部 P 编号列表或创意案例总表。保留既有锚点与编号，来源平台和作者署名放在案例标题后。此规则优先于较早的目录布局说明。

- Display README cases with category-local numbers (1.1, 1.2, …, 7.5) from catalog.display_number. Keep P/C IDs and slugs internal and preserve legacy anchors. Renumber display values when category order changes, in both languages.
- README 案例采用分类内连续编号（1.1、1.2……7.5），对应 catalog.display_number。P/C 编号与 slug 保留在内部，旧锚点保持有效。调整分类顺序时同步两种语言的展示编号。

## Contents and source placement / 目录与来源位置

Group Contents into Repository Guide and Prompt Categories. Show author/source credits only in a `<sub>` footer after the final full-prompt block of each case, with platform and source link preserved. Remove standalone italic placeholder-replacement notes; keep actual placeholders in prompts unchanged. This supersedes earlier source-in-title rules.

Contents 分为仓库信息与提示词分类。每条案例的作者和来源统一置于最后一段完整提示词后的 `<sub>` 小字中，保留平台与来源链接。去掉独立的斜体占位符替换说明，不改提示词内部占位符。本规则优先于之前的标题署名要求。
