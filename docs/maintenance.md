# Maintainer Update Checklist

SeeAPI maintains this collection. External prompt submissions and contribution requests are not open at this stage.

For Feishu imports and collection handoff, follow [the update SOP](feishu-update-sop.zh-CN.md).

## Add a Case

1. Assign the next stable ID and a descriptive English slug. C07–C10 remain reserved for the creative series; C03 is archived. Allocate standalone IDs above the highest published or local catalog ID (currently P42, so the next is P43). After pulling, resolve ID collisions by preserving published IDs and reassigning only unpublished drafts, including their paths and links.
2. Copy [the case template](../templates/case.md). Write the complete prompt, reference requirements, source credits, and known limitations.
3. Store copyable prompts under `prompts/{slug}/`. Store actual media under `assets/{slug}/` and label its role and provenance. Do not mark a prompt tested simply because its text is complete.
4. Add the case to `catalog.json`. Allowed statuses are `prompt-only`, `gif-included`, `stills-included-video-pending`, `image-included`, and `video-included`. A status describes available output, not perfection or a model benchmark.
5. Expand the case in the README using Preview, Workflow, and Full Prompt; point its directory entry to the README heading anchor. Set readme_anchor in the catalog. Keep creative workflows after the Prompt Directory; list new P entries first. Update categories, totals, dates, and the changelog.
6. Verify local links, prompt copies, and catalog paths with `python3 scripts/validate_catalog.py`. Preview the Markdown and inspect any new image, GIF, or video.

## Publish a Result for an Existing Prompt

Keep its ID and slug. Add media, actual model/settings when known, result checks, and any remaining defects. Update its status and preview in the catalog and case, then update homepage wording. When replacing C06's video, review the camera movement, single handle, geometry, and typography against the associated prompt. Its current prompt requests a 120° arc; the earlier 360° alternative remains untested.

## Review Rhythm

Review candidate prompts and source links weekly when material is available. Publish an entry when its text, attribution, and status are accurate; a finished visual can be added later with an explicit status change. Review categories and featured selections monthly as the collection grows. These are maintainer guidelines, not an automated update schedule.

Before a release, run the validator and `git diff --check`, review the diff, and confirm that only intended files are included. Push when publishing is authorized. Do not assign a blanket license or add product links as a routine content update.

## Bilingual Publishing

Every content update must ship in English and Simplified Chinese. See [the repository instructions](../AGENTS.md). Keep titles, source credits, images, workflows, all prompt steps, counts and dates aligned. Store Chinese prompts alongside English originals as `*.zh-CN.txt`; register them in `prompts_zh`. Preserve bracketed placeholder keys, literal output wording and code. Review the translation when the original changes before recording its SHA-256 in `translation_source_sha256`.

Update reviewed UI translations in `docs/i18n/zh-CN.json`, then run `python3 scripts/build_chinese_readme.py` to render `README_zh.md` and `cases/zh-CN/`. Run `python3 scripts/validate_catalog.py` and `python3 scripts/build_chinese_readme.py --check` before publishing. A translation is not a new generation test.

每次公开内容更新都必须同步英文与简体中文。标题、来源、图片、工作流、完整提示词、数量和日期保持一致。中文提示词作为 `*.zh-CN.txt` 存于原英文文件旁，并登记到 `prompts_zh`；保留占位符名称、要求输出的原样文字及代码。英文变化后须先复核翻译，再记录源文 SHA-256。

界面文案翻译放在 `docs/i18n/zh-CN.json`，运行上述生成命令更新中文 README 和案例页，然后执行双语校验。翻译不代表重新生成或验证模型效果。
