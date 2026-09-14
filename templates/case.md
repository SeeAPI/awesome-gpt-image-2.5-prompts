# {ID}. {English Title}

**by {Prompt author}** · [Source]({Public original post or collection-page URL})

{Link a credited author as a clickable @handle. Use SeeAPI only for prompts developed by SeeAPI. For collected prompts, preserve source attribution; if authorship is unresolved, write **Author unconfirmed** and identify the collection-page publisher separately. For adaptations, name the adapter and add “inspired by” with the original author/post. Omit the Source link for originals without an external source; never invent a URL.}

{State source-image provenance, model evidence, and any unresolved original-source or reuse question briefly.}

## 👀 Preview

{Embed actual result and required reference images using an img tag with proportional width/height bounded by 400 × 400 pixels, without upscaling. Link the image to its original file (or original video for a video preview). Keep original media unchanged; state when an example or video is pending. Keep essential provenance or limitations to a short note.}

## 👇 Workflow

`{Text → image → video, or Reference image → edited image. Include intermediate stages and upload roles where needed.}`

## 🔖 Full Prompt

**Step 1 — {Match the first Workflow stage}**

{One short upload instruction, if needed.}

```text
{Complete prompt, identical to its canonical .txt file. For P entries, prefer reusable person/character wording without fixed species or gender; use [placeholders] for customizable subjects, scenes, and copy. Preserve explicitly supplied prompts verbatim.}
```

{Repeat in workflow order for additional prompts. Label alternatives and negative prompts clearly. Publish this content inline in README with an H3 case title and H4 Preview / Workflow / Full Prompt headings; link the directory entry to that title’s page anchor.}

For prompts containing bracketed placeholders, put an italic note directly below the prompt block listing the actual fields to replace. Omit the note when no placeholders exist.

Source credits belong in the Prompt Directory entry as Source: X / Reddit / TikTok / GitHub / the actual platform. Case bodies contain only Preview, Workflow, and Full Prompt; omit repeated source paragraphs, review commentary, and footer navigation. Preserve prompt text and italic placeholder guidance.


## Bilingual maintenance / 双语维护

Publish an English case and a matching Simplified Chinese case. Add the complete Chinese prompt beside its English source (`*.zh-CN.txt`), preserving placeholders and literal output text. Register `title_zh`, `prompts_zh`, and reviewed `translation_source_sha256` values in the catalog. Update `docs/i18n/zh-CN.json`, then regenerate the Chinese pages.

每个英文案例均需对应的中文案例与完整中文提示词。保留占位符与原样输出文字，同步目录、预览、工作流和全部提示词步骤。运行双语生成和校验脚本；生成的中文页面不要手工修改。
