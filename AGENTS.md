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
