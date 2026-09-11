# C03. Two Characters, One Scene

**Prompt: by SeeAPI.** **Inspiration:** [TechieSA](https://x.com/TechieBySA/status/2096196085198839832). Original concept and prompt adaptation by SeeAPI; no source footage is included.

**Category:** Characters & Stickers · Story & Video

**Updated:** 2026-09-11

## Preview

**Opening frame — video pending.**

![Two Characters, One Scene: opening frame — video pending](../assets/03-two-character-video/greenhouse-opening.png)

## Reference Images

Upload Mira (C03-R01) first and Ren (C03-R02) second to create the shared scene. For video, use the greenhouse opening frame (C03-K01) as the first frame; the portraits are optional additional identity references only. Follow the upload roles below when using references.

## Full Prompt & Workflow

Bring two separately defined characters into one scene, then animate their interaction. In this original example, greenhouse caretakers Mira and Ren place an amber seed into a lantern and watch it light up together.

**Inspiration:** [TechieSA's character-reference-to-video workflow](https://x.com/TechieBySA/status/2096196085198839832). The source post names GPT Image 2 and Seedance 2.5. This adaptation uses original characters and a new scene; it is not a reproduction of that post or a tested claim about those models.

**Workflow:** Two character images → shared opening frame → image-to-video.

**Input:** Two separate character reference images. Use your own, or create the original pair below.

**Status:** Character images and an opening frame are included. The video prompt is ready to use; no video has been generated or verified. Example stills were made with Codex's built-in image generation tool; its underlying model ID was not exposed.

### Step 1 — Prepare two character references

Keep each character in a separate image so the video workflow can distinguish them. For this example, generate the following two-panel reference sheet, then split it into the two supplied portrait files. If using your own images, skip this generation step and assign them the same reference roles.

```text
Generate a widescreen 3:2 character reference diptych, exactly two equal vertical panels with a plain warm gray background, no border or text. The panels will be cropped into two separate identity reference images. Each panel contains exactly one full-body adult original human character, head to boots fully visible with ample margins, both at identical scale.
Left panel: MIRA, an adult woman aged about 30, medium-brown skin, short curly black bob, oval face, dark eyes, rust-orange utility jacket over cream shirt, navy work trousers, brown ankle boots. No jewelry, no hat, no props. Arms relaxed and hands fully visible.
Right panel: REN, an adult man aged about 32, light olive skin, straight dark hair tied in a small low bun, clean-shaven angular face, dark eyes, moss-green utility jacket over charcoal shirt, charcoal trousers, brown work boots. No jewelry, no hat, no props. Arms relaxed and hands fully visible.
Style: cinematic hand-painted animation concept art, softly textured gouache backgrounds, clear expressive faces, grounded anatomy, restrained warm colors, diffuse studio lighting. Neutral front three-quarter standing poses. These are original greenhouse caretakers, no celebrities, no existing film characters. Do not blend identities, duplicate people, invent props, add text or crop limbs.
```

| C03-R01 — Mira | C03-R02 — Ren |
|---|---|
| ![Mira in a rust-orange utility jacket](../assets/03-two-character-video/mira-reference.png) | ![Ren in a moss-green utility jacket](../assets/03-two-character-video/ren-reference.png) |

### Step 2 — Create a shared opening frame

Upload **C03-R01 first and C03-R02 second**. Use the images to preserve the two identities while changing their poses and placing them together in the greenhouse.

```text
Use the two uploaded character portraits as separate strict identity references: image 1 is MIRA, the woman with a rust-orange jacket; image 2 is REN, the man with a moss-green jacket. Preserve each person's face, hairstyle, skin tone, age, body proportions, and entire outfit. Do not merge or swap their identities.

Create a single cinematic 16:9 opening frame in the same hand-painted animation style. A glass greenhouse at blue hour, quiet foliage at the edges, dark blue glass roof overhead, a waist-high stone workbench across the foreground. Mira stands on the LEFT, Ren on the RIGHT, facing slightly inward toward one small unlit brass lantern fixed at the center of the bench. Mira's open right palm holds exactly one small amber glass seed just left of the lantern. Ren's left hand rests beside the lantern base, leaving the empty circular socket clearly visible. All hands remain distinct. Both faces are clearly readable in a medium-wide shot.

The lantern is attached to the bench and cannot move; its socket is empty. The amber seed has not been inserted yet. Soft cool dusk light and a faint warm reflection from the seed. Calm anticipation, grounded anatomy, subtle gouache texture, no text, no labels, no montage, no extra people, no duplicate seed, no costume changes, no oversized hands. This is the first frame before the action, not the finished glowing result.
```

**C03-K01 — Opening-frame example:**

![Mira and Ren beside an unlit lantern in a greenhouse at dusk](../assets/03-two-character-video/greenhouse-opening.png)

Check both faces and outfits, the single seed, the empty socket, and the separation of the hands before animating. The generated example reverses the anatomical hand assignments in the image prompt; the video prompt therefore follows the visible seed-bearing palm and free hand instead of forcing a left/right swap.

### Step 3 — Animate the interaction

| Upload | Role |
|---|---|
| C03-K01 — greenhouse opening frame | First frame; scene layout and starting poses |
| C03-R01 — Mira portrait | Optional identity reference, if supported |
| C03-R02 — Ren portrait | Optional identity reference, if supported |

If the video tool accepts only one image, upload **C03-K01**. Do not upload the two-person reference sheet as the first frame: that would start the video from a split-screen portrait layout. The 8-second duration is a creative target; use supported settings and trim if needed.

```text
Create an 8-second cinematic hand-painted animation, 16:9, one continuous medium-wide shot. C03-K01 is the exact first frame and controls composition, greenhouse, bench, lantern, and initial hand positions. C03-R01 locks Mira's identity and rust-orange outfit; C03-R02 locks Ren's identity and moss-green outfit. If only one image is supported, use C03-K01 alone. Mira stays on screen-left, Ren on screen-right. Preserve both faces, hairstyles, skin tones, ages, clothes, and body proportions throughout.

0–2 seconds: Mira looks from the single amber seed on her seed-bearing palm to the empty lantern socket. Ren watches the socket, his visible hand resting beside the fixed base. Gentle breathing; leaves shift slightly in the greenhouse draft. The camera stays locked.
2–5 seconds: Mira uses the thumb and index finger of her free hand to lift the seed from her open seed-bearing palm, then seats it in the lantern's circular socket. Show one continuous transfer and contact. Ren does not take the seed or move the lantern. Once the seed is seated, its amber light gradually illuminates the lantern and nearby faces.
5–8 seconds: Mira withdraws the hand that placed the seed; the seed remains visibly seated. Both look at the illuminated lantern and exchange a small satisfied smile. Warm reflections settle on the glass roof. End on the two distinct characters and the lit lantern. Do not reset the action or loop.

Keep movement restrained and expressive, with coherent hand anatomy and stable painted textures. No scene cuts. Optional audio: faint greenhouse wind, a soft glass click at contact, and a gentle electrical hum after illumination; no dialogue or lip-sync. If audio is unavailable, export silently.

Negative prompt: face swap, merged people, outfit morphing, duplicate seed, disappearing seed, extra fingers or arms, passing objects through solid glass, floating lantern, premature illumination, camera orbit, zoom, captions, text, logos, unrelated cuts, flickering identities.
```

**Video result:** Pending generation. Check identity consistency, the seed's continuous transfer into the socket, and illumination only after contact. A still-image slideshow would not validate this workflow.

**Production notes:** [Chinese story, continuity rules, and exact upload instructions](../docs/production/03-two-character-video.md). The [image prompt](../prompts/03-two-character-video/keyframe-prompt.txt) and [video prompt](../prompts/03-two-character-video/video-prompt.txt) are also available as text files.

## Prompt Files

- [character-prompt.txt](../prompts/03-two-character-video/character-prompt.txt)
- [keyframe-prompt.txt](../prompts/03-two-character-video/keyframe-prompt.txt)
- [video-prompt.txt](../prompts/03-two-character-video/video-prompt.txt)

## Sources & Attribution

**Prompt: by SeeAPI.** **Inspiration:** [TechieSA](https://x.com/TechieBySA/status/2096196085198839832). Original concept and prompt adaptation by SeeAPI; no source footage is included.

Example stills were created with Codex’s built-in image generation tool. The underlying model ID was not exposed; they are workflow illustrations, not verified GPT Image 2.5 model samples.

See the [sources and reuse notes](../docs/sources-and-rights.md). Attribution alone is not a repository-wide reuse license.

[← Browse the collection](../README.md) · [Prompting tips](../docs/prompting-tips.md)
