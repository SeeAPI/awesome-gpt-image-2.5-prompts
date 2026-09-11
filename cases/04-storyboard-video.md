# C04. Character to Storyboard to Film

**Prompt: by SeeAPI.** **Inspiration:** [el.cine](https://x.com/EHuanglu/status/2097519538632024103). Original concept and prompt adaptation by SeeAPI; no source footage is included.

**Category:** Characters & Stickers · Story & Video

**Updated:** 2026-09-11

## Preview

**Storyboard — video pending.**

![Character to Storyboard to Film: storyboard — video pending](../assets/04-storyboard-video/lighthouse-storyboard.png)

## Reference Images

Use Inez (C04-R01) to build the storyboard. Crop the four storyboard panels into separate shot images before animation. Use the matching shot image for each clip; do not animate the full 2 × 2 board as a single scene. Follow the upload roles below when using references.

## Full Prompt & Workflow

Define a protagonist, plan the story as distinct shots, then animate each shot. In this original miniature-film concept, lighthouse mechanic Inez winds a dormant brass seabird, watches it wake, and releases it through an open window.

**Inspiration:** [el.cine's cast-design and storyboard workflow](https://x.com/EHuanglu/status/2097519538632024103). The source describes character design and storyboards followed by video generation. The lighthouse setting, character, prop, and story below are newly designed for this repository.

**Workflow:** Character design → four-shot storyboard → individual shot-start images → image-to-video → edit.

**Input:** A character concept and short story.

**Status:** Character reference, storyboard, and extracted shot-start images are included. The 12-second film remains a production plan; no generated video is included. Stills were created with Codex's built-in image generation tool, whose model ID was not exposed.

### Step 1 — Define the character

Create one reusable identity reference. Lock Inez's age, face, glasses, hairstyle, and clothes before designing the shots.

```text
Generate one landscape 3:2 clean single-character full-body identity reference portrait. Original protagonist INEZ, a lighthouse mechanic aged about 60, warm tan skin, short silver-gray curly hair, round tortoiseshell glasses, kind lined face, navy wool chore coat over an ochre knitted sweater, charcoal trousers and weathered dark brown work boots. Her hands are empty and visible, arms relaxed, head and boots fully inside the frame with ample margins. She stands in a neutral three-quarter pose against a simple warm gray studio backdrop. No other characters or props, no collage or additional views, no text.
Visual style: tactile miniature stop-motion film design, felted wool costume, subtly sculpted expressive face, cinematic soft overcast coastal light, muted navy and ochre palette, believable anatomy. Preserve the subject as a clearly older adult woman, no glamour retouching.
```

**C04-R01 — Inez:**

![Inez, an older lighthouse mechanic in a navy coat and ochre sweater](../assets/04-storyboard-video/inez-reference.png)

### Step 2 — Design the storyboard

| Shot | Editing target | Story beat | Starting image |
|---|---|---|---|
| 1 | 0–3 s | Discover the inert bird; reach toward it | C04-K01 |
| 2 | 3–6 s | Turn its attached winding key | C04-K02 |
| 3 | 6–9 s | The wings unfold; Inez offers her palm | C04-K03 |
| 4 | 9–12 s | Release the bird through the open window | C04-K04 |

Upload **C04-R01 only** for the following storyboard generation. It locks the character and material style; the prompt defines the new workshop and brass bird.

```text
Use the uploaded full-body portrait of INEZ as the strict identity and visual-style reference. Preserve her older adult face, short silver-gray curls, round tortoiseshell glasses, navy wool coat, ochre sweater, charcoal trousers, and brown work boots. Create one 16:9 storyboard sheet divided into an EXACT 2x2 grid of four equal 16:9 cinematic panels, no gutters, panel labels, numbers, captions, text, or borders. Reading order is left to right, top to bottom. This is a four-shot narrative storyboard, NOT consecutive animation frames.

Original story: in a tiny coastal lighthouse workshop, Inez revives one palm-sized brass mechanical seabird with an attached winding key, then lets it fly out of an already-open window. Tactile miniature stop-motion film look, felted wool clothing, sculpted face, softly weathered brass, overcast coastal daylight. The same wooden workbench runs beneath one arched OPEN window on the RIGHT of the room; cool sea beyond. One brass mechanical bird only, two hinged wings, one small attached winding key on its left flank. No loose tools or unrelated objects.

Panel 1, establishing medium-wide shot: Inez is on the LEFT of the workbench looking down at the inert bird resting on the bench at center-right. Both bird wings are folded. Her hands rest on the bench on either side of the bird without touching the key. The open window is visible on the right. This is the first moment before repair.
Panel 2, close-up from the same side of the bench: one of Inez's hands gently braces the bird body; her other hand holds the small attached winding key on its left flank, ready to turn. Both wings remain folded. Show enough ochre sleeve and navy cuff to link her costume. Brass bird geometry must match panel 1, not a different bird. Key remains attached.
Panel 3, medium shot: Inez smiles at the same bird standing on the bench, both hinged wings now partly unfolded, head lifted. Her hands are withdrawn and clearly separate from its wings. Bird has not taken off. Same window on right, same lighting and clothes.
Panel 4, medium-wide shot toward the open window: Inez remains on the LEFT with an open supporting palm near the window sill. The same brass bird rests on the RIGHT sill with wings poised for takeoff toward the open sea, still physically supported. Maintain the single window and its already-open state. Inez's face is visible in three-quarter profile, quietly proud. This is the beginning of the release shot, before the bird flies away.

Keep causal continuity, a single recognizable protagonist, one bird, stable costume, stable room geography, plausible hands, and a clear visual link between the close-up and wide shots. No magic beams, glowing eyes, extra characters, flying tools, missing glasses, unreadable writing, duplicate birds, grid overlays, or photoreal human replacement.
```

**C04-B01 — Four-shot storyboard:**

![Four shots showing Inez discovering, winding, awakening, and preparing to release a mechanical seabird](../assets/04-storyboard-video/lighthouse-storyboard.png)

### Step 3 — Prepare individual shot-start images

Split the storyboard into four images in reading order. A storyboard panel defines a shot; it is not one frame of a four-frame animation. Avoid feeding the entire grid into a first-frame-only video tool.

| ID | File | What it controls |
|---|---|---|
| C04-K01 | [Discovery](../assets/04-storyboard-video/shot-01.png) | Establishing view and inert bird |
| C04-K02 | [Winding](../assets/04-storyboard-video/shot-02.png) | Hand contact and key location |
| C04-K03 | [Awakening](../assets/04-storyboard-video/shot-03.png) | Wing state and reaction |
| C04-K04 | [Release](../assets/04-storyboard-video/shot-04.png) | Open window and takeoff position |

The included crops can be reproduced with `python scripts/prepare_video_references.py` using Python 3 and Pillow. Check costume, hand anatomy, bird geometry, attached key, and window placement across the crops. The bird body, winding-key detail, and apparent scale vary somewhat between the generated panels. Treat these as draft shot references and refine those differences before final video production; the included stills do not establish video continuity.

### Step 4 — Animate and edit

For a video tool that supports multiple ordered shot references, map C04-K01–K04 to shots 1–4 and supply C04-R01 as an identity reference if a separate slot exists. Otherwise, generate each shot separately from its matching C04-K image, then join four selected three-second clips with straight cuts. Do not assume a particular tool accepts four reference images or an exact three-second duration.

```text
Create a 12-second, 16:9 miniature stop-motion-style short film called The Last Flight, with four shots and clear tactile stepped motion. Do not render the title as text. C04-R01 is the identity reference for Inez. C04-B01 is a storyboard for planning only, not a frame sheet to animate directly. C04-K01 through C04-K04 are individual shot-start references. Never show the grid or multiple panels in the video.

Continuity: Inez is the same older woman with silver curls, round tortoiseshell glasses, navy coat and ochre sweater. There is one palm-sized brass mechanical seabird, two hinged wings, and one attached winding key on its left flank. The wooden bench is below a single already-open arched window on room-right. Overcast sea light stays constant. The bird progresses from inert to wound to active to airborne; it never duplicates or changes species.

Shot 1, 0–3 seconds, start from C04-K01: locked medium-wide shot. Inez notices the folded, inert brass bird on the bench, leans slightly closer, and reaches toward its attached key. The open window remains visible on the right. Cut on her reaching hand to the matching close-up.
Shot 2, 3–6 seconds, start from C04-K02: locked close-up. One hand braces the bird; the other gives its attached key one slow half-turn. The key remains attached and her fingers keep contact. A small mechanical click prompts the bird's head to lift slightly. Cut on this first movement to the wider reaction.
Shot 3, 6–9 seconds, start from C04-K03: medium shot. The bird unfolds its two wings, takes two short steps toward the right, and Inez offers her open palm beside it. She smiles, keeping her glasses and outfit unchanged. Cut in the direction of the bird's movement to the open-window shot; the short move to the sill is an intentional edit, not a teleport within a shot.
Shot 4, 9–12 seconds, start from C04-K04: medium-wide shot. From the sill, the bird pushes off with both feet and makes two small mechanical wingbeats, flying out through the already-open window toward screen-right. Inez withdraws her supporting palm and follows it with her gaze. End with her quiet smile and the open sea. The bird stays the same small brass object as it recedes. No reset or loop.

No camera movement is required. Prioritize readable action over extra cuts. Optional audio: low coastal wind, a winding click, two soft metallic wing flutters; no dialogue, captions, or lip-sync. If audio generation is unavailable, export silent clips.

Negative prompt: visible storyboard grid, collage animation, extra bird, detached key, changing bird design, wardrobe morph, missing glasses, extra fingers, hand-wing fusion, closed window, flight through glass, unmotivated room change, continuous-shot teleport, photoreal skin, fast montage, crossfades, text or logos.

Limited-input fallback: generate four separate 3-second clips using only the matching C04-K image as that clip's first frame and the corresponding shot paragraph above plus the continuity and negative instructions. Trim to three seconds per clip and join with straight cuts. If the generator requires a longer minimum duration, generate that duration and select a coherent three-second segment; the 12-second timing is an editing target, not a claim about a particular model's supported settings.
```

**Video result:** Pending generation. Verify that the key stays attached, the bird count stays at one, and the bird exits through the opening rather than through glass. Keep the move from workbench to sill as an intentional cut.

**Production notes:** [Chinese story, continuity ledger, panel-edit instructions, and upload map](../docs/production/04-storyboard-video.md). The [storyboard prompt](../prompts/04-storyboard-video/storyboard-prompt.txt) and [video prompt](../prompts/04-storyboard-video/video-prompt.txt) are supplied as text files.

## Prompt Files

- [character-prompt.txt](../prompts/04-storyboard-video/character-prompt.txt)
- [storyboard-prompt.txt](../prompts/04-storyboard-video/storyboard-prompt.txt)
- [video-prompt.txt](../prompts/04-storyboard-video/video-prompt.txt)

## Sources & Attribution

**Prompt: by SeeAPI.** **Inspiration:** [el.cine](https://x.com/EHuanglu/status/2097519538632024103). Original concept and prompt adaptation by SeeAPI; no source footage is included.

Example stills were created with Codex’s built-in image generation tool. The underlying model ID was not exposed; they are workflow illustrations, not verified GPT Image 2.5 model samples.

See the [sources and reuse notes](../docs/sources-and-rights.md). Attribution alone is not a repository-wide reuse license.

[← Browse the collection](../README.md) · [Prompting tips](../docs/prompting-tips.md)
