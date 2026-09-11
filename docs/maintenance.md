# Maintainer Update Checklist

SeeAPI maintains this collection. External prompt submissions and contribution requests are not open at this stage.

## Add a Case

1. Assign the next stable ID and a descriptive English slug. C07–C10 remain reserved for the creative series; use P09 onward for new standalone prompts.
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
