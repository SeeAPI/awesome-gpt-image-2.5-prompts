# Repository Structure

```text
README.md                         # Visual homepage and linked directories
catalog.json                      # IDs, categories, status, paths, attribution
CHANGELOG.md                      # Content changes
cases/
  01-pixel-art-gif.md              # C01: complete English case
  06-360-orbit.md                  # C06: complete English case
  p01-personalized-sticker-pack.md # P01: standalone prompt case
prompts/
  01-pixel-art-gif/
    image-prompt.txt
    gif-assembly-prompt.txt
  06-360-orbit/
    image-prompt.txt
    video-prompt.txt
    negative-prompt.txt
  p01-personalized-sticker-pack/
    image-prompt.txt
assets/
  01-pixel-art-gif/
    elephant-sprite-sheet.png
    elephant-roll.gif
  06-360-orbit/
    frosted-glass-mug-poster.png
docs/
  production/                     # Detailed Chinese production notes
  prompting-tips.md
  sources-and-rights.md
  repository-structure.md
  maintenance.md
  repository-design.zh-CN.md       # Rationale and roadmap
templates/
  case.md
scripts/
  build_elephant_gif.py
  build_penguin_gif.py
  prepare_video_references.py
  validate_catalog.py
```

## IDs and Names

Creative workflows have stable IDs **C01–C10**; C01, C02, C04, C05, and C06 are active; C03 remains archived with its original files. Their slugs retain the existing `01-pixel-art-gif` format to preserve image and script paths. Standalone prompts use **P01, P02, …** with slugs such as `p01-personalized-sticker-pack`.

Use the exact same slug for the case filename, prompt folder, and media folder. Use lowercase English words separated by hyphens. Never renumber a published case when adding a new one. If an unpublished draft collides with an upstream ID, allocate it a new ID and update its slug, files, catalog, cross-references, and internal handoff mapping together. The current standalone range is P01–P40. Keep the title in English; category membership can change without changing the ID.

Name files by their role: `character-prompt.txt`, `scene-prompt.txt`, `video-prompt.txt`, `negative-prompt.txt`, `mira-reference.png`, `greenhouse-opening.png`, `shot-01.png`, or `result.gif`. For corrections, retain a named draft and its correction prompt. Add a media directory when media exists; P01–P08 do not need empty asset folders.

## Where Content Lives

- **Homepage:** previews, linked indexes, short usage/model guidance. All complete prompts and existing example images are expanded inline in the README.
- **Cases:** concise copies of the README cases to preserve existing direct links. Use Preview, Workflow, and Full Prompt.
- **Prompts:** plain UTF-8 `.txt` copies for reuse, without Markdown fences. These are the canonical copyable prompt files; synchronize inline README and case blocks after an edit.
- **Assets:** references, approved results, relevant drafts, GIFs, and eventual videos. Do not put prompt text in the media tree.
- **Production notes:** longer Chinese shot planning and correction instructions.
- **Catalog:** machine-readable case metadata. The README is edited manually; it is not automatically generated from the catalog. Update both together and run the validator.

Record model provenance in the case, not in a guessed filename. Keep original supplied media unchanged; add a separately named optimized preview if needed later. Link large future videos from a stable hosted result or use Git LFS with a documented setup rather than repeatedly committing large binary versions.

[← Back to the collection](../README.md)

## Collected source metadata

Collected entries add `source` with a public `url`, `publisher`, stable `item_key`, `author_status` (`credited-by-source` or `unconfirmed`), and `relationship` (`collected` or `adapted`). `content_type` distinguishes `full-prompt` from `short-template`. `model_provenance` distinguishes source claims from source workflow configuration; neither means a repository test. `media` records each local path, role, proportional display dimensions, and SHA-256. Keep private review snapshots and record IDs outside the repository.

Follow [the Feishu update SOP](feishu-update-sop.zh-CN.md) for collection handoff and publication.

When a maintainer selects a collection page for display, set `source.credit_role` to `collection`, use its publisher and URL for the “Collected from” credit, and retain `source.original_source` and original `author` for provenance. This does not transfer original authorship.
