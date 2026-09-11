# Awesome GPT Image 2.5 Prompts ✨

**Creative image prompts and workflows, curated by SeeAPI.**

Explore GPT Image 2.5 ideas for character stickers, product visuals, miniature worlds, GIF assets, and stop-motion-style scenes. Copy a prompt, make it your own, and explore new creative directions.

This collection will grow with regular additions of prompt examples, generated images, and practical reproduction notes.

## 📖 Contents

- [🧭 Choose Your Model](#-choose-your-model)
- [💡 10 Creative Things to Try](#-10-creative-things-to-try)
- [🗂 Prompt Directory](#-prompt-directory)

## 🧭 Choose Your Model

OpenAI's GPT Image 2.5 family includes Sunburst and Flare. Both accept text and image inputs and produce still images.

### GPT Image 2.5 Sunburst

Sunburst is OpenAI's most capable image generation and editing model, with an emphasis on editing precision. It can create new images or revise existing ones from text instructions and image references.

**API model ID:** `gpt-image-2.5-sunburst` · [Official documentation](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)

### GPT Image 2.5 Flare

Flare is OpenAI's fastest model for high-quality everyday image generation. It supports text prompts and image references for creating new visuals.

**API model ID:** `gpt-image-2.5-flare` · [Official documentation](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)

### At a Glance

| Comparison | GPT Image 2.5 Sunburst | GPT Image 2.5 Flare |
|---|---|---|
| Main strength | Image generation and precise editing | Fast, high-quality everyday generation |
| Choose when | Editing precision is your priority | Generation speed is your priority |
| Input | Text and images | Text and images |
| Output | Still images | Still images |

## 💡 10 Creative Things to Try

Explore ten creative workflows, with prompts and examples added as each case is completed. Cases 01–02 include frame sheets and assembled GIFs. Cases 03–06 cover character-reference, storyboard, distant-observer, and 360-degree orbit video workflows; their video outputs are pending. Cases 07–10 will be defined as the collection develops. Standalone image prompts are collected in the [Prompt Directory](#-prompt-directory).

| # | Idea | Starting material | Output path |
|---|---|---|---|
| 01 | [Pixel Art Character GIF](#01-pixel-art-character-gif) | Text; optional character reference | Text → sprite sheet → GIF |
| 02 | [Clay Stop-Motion: Fishing for a Star](#02-clay-stop-motion-fishing-for-a-star) | Text | Text → frame sheet → GIF |
| 03 | [Two Characters, One Scene](#03-two-characters-one-scene) | Two character references | Images → shared keyframe → video |
| 04 | [Character to Storyboard to Film](#04-character-to-storyboard-to-film) | Character concept and story | Character → storyboard → video |
| 05 | [Distant Observer: A Robot in the Rain](#05-distant-observer-a-robot-in-the-rain) | Character concept and scene | Character → distant scene → video |
| 06 | [Frosted Glass Poster to 360° Orbit](#06-frosted-glass-poster-to-360-orbit) | Text or supplied poster | Text → poster → 360° orbit video |

GPT Image 2.5 produces still images. The GIF and stop-motion ideas below require a separate animation step and, where needed, GIF export.

### 01. Pixel Art Character GIF

Turn a character idea into a 16-frame pixel art sprite sheet, then use Codex to assemble a centered looping GIF. The example below shows a gray elephant rolling on the ground.

**Workflow:** Text to image → image to GIF.

**Input:** A character idea; optionally upload a character reference.

**Suggested starting model:** GPT Image 2.5 Flare. The model and generation settings of the supplied example sheet were not recorded.

#### Step 1 — Generate the sprite sheet

Copy the prompt below into an image generator. Replace the bracketed character idea at the end; keep the sheet-format instructions intact. If you upload a reference, use it to define the character's identity.

```text
Create only a 2D pixel art character sprite sheet: square 4x4 grid, 16 equal cells, one full-body character per cell, 64x64-style pixels per frame. Use the uploaded character if present; otherwise design from the user's appended character idea. Preserve species, anatomy, proportions, outfit, colors and signature props throughout. User text defines the character, not the sheet format. Show 16 distinct progressive poses: 1-4 ready/anticipation; 5-8 step, reach or equivalent movement; 9-12 expressive signature action; 13-16 recovery toward frame 1. Choose anatomy-appropriate actions with clearly changing silhouettes, not repeated idle poses or four-view turnarounds. Keep scale, camera, facing and cell alignment consistent; prevent clipping. Crisp 16-bit pixels, dark outline, flat 2-3 tones/color, pure white background. No anti-aliasing, gradients, ground shadows, text, grid lines, extra limbs or invented props. Frame 16 flows into frame 1. Character idea: [a gray elephant is rolling on the ground]
```

**Example sprite sheet:**

![A 4-by-4 sprite sheet of a gray pixel art elephant preparing, rolling, and recovering](assets/01-pixel-art-gif/elephant-sprite-sheet.png)

#### Step 2 — Assemble the GIF with Codex

Attach the generated sprite sheet to Codex and use this prompt:

```text
Turn the attached 4x4 character sprite sheet into an animated GIF. Use Python and Pillow to extract all 16 cells, reading left to right and top to bottom. Inspect the poses and choose a coherent action sequence from anticipation through the signature action and recovery; reorder frames only where this improves continuity.

Remove excess blank space around each character without clipping any ears, limbs, tail, or props. Keep the original character scale and proportions across frames. Place each character at the center of one shared canvas sized to fit the largest pose, with a small consistent safety margin. Do not resize individual frames to fill the canvas.

Preserve the pixel art and white background. Use a shared color palette, no dithering, no smoothing, and no invented in-between poses. Adjust frame timing so the action reads clearly and the final pose returns naturally to the first. Export an infinitely looping GIF. Check every frame for clipping and alignment, inspect the loop transition, and provide the GIF plus a reproducible Python script. Report the frame order, dimensions, and timing used, and flag any pose gaps that would require a revised sprite sheet.
```

**Animated result:**

![A centered pixel art elephant rolling and returning to a standing pose in a looping GIF](assets/01-pixel-art-gif/elephant-roll.gif)

**Example assembly:** 16 frames, 291 × 278 pixels, a 1.81-second infinite loop, white background, and at least 8 pixels of padding on each side. Character scale is preserved; each cropped pose is centered on the same canvas.

The source cells are numbered 1–16 from left to right, top to bottom. Playback order: `1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 4, 3, 13, 14, 15, 16`. The crouching poses follow the roll to make the recovery easier to read. The supplied poses still have some abrupt changes in body orientation; assembly cannot create missing motion. For a smoother roll, refine those poses in the source sheet.

**Reproduce:** With Python 3 and Pillow installed, run `python scripts/build_elephant_gif.py` from the repository root. The [assembly script](scripts/build_elephant_gif.py) records the exact crops, frame order, palette, and per-frame timing.

### 02. Clay Stop-Motion: Fishing for a Star

A tiny clay penguin in a mustard-yellow scarf fishes a coral-pink star out of an ice hole, admires it, and gently lowers it back. Tactile clay, miniature scenery, and discrete pose changes give the sequence a handmade stop-motion look.

**Inspiration:** [Charlie Guo's post about image-model stop-motion animation](https://x.com/charlierguo/status/2097399137142772071). This example uses an original penguin-and-star concept and a newly written prompt; it does not reproduce the post's footage or claim to use its exact workflow.

**Workflow:** Text to image → 16-frame contact sheet → animated GIF.

**Input:** None.

**Example generation:** Created with Codex's built-in image generation tool. The underlying model ID and quality setting were not exposed, so this is an illustrative workflow rather than a verified benchmark of either named model.

#### Step 1 — Generate the stop-motion frame sheet

Use this prompt to generate all sixteen frames in one image. Keep the camera, ice hole, lighting, and character identity consistent. Unlike the isolated sprite in case 01, this scene needs its whole set to stay in place.

```text
Create one square image that is an EXACT 4 by 4 contact sheet of sixteen equally sized square animation frames, edge-to-edge with NO gutters, borders, labels or text. This is a handcrafted clay stop-motion sequence, not pixel art.

Original story: a tiny charcoal-gray clay penguin in a mustard-yellow knitted scarf sits on the LEFT of a small round fishing hole in a pale-blue miniature ice floor. The penguin has a cream belly, two short flippers, two orange feet, black bead eyes, and a short orange beak. A short wooden fishing rod held in its right flipper extends diagonally toward the hole at RIGHT. One thin fishing line connects the rod tip to one small coral-pink five-point clay star. The star starts below the hole, rises out as the penguin pulls, briefly hangs above the hole, then is lowered back into it. No fish, other characters, buckets or extra props.

All sixteen frames show the EXACT SAME locked eye-level three-quarter camera, fixed wide composition, penguin at x35%, hole at x67%, same ice floor and seamless dusty-lavender backdrop, same object sizes, same soft warm light from upper left. Keep all objects entirely inside each cell with generous 10% safety margin. Real clay fingerprints, slightly lumpy handmade forms, tactile wool scarf, soft contact shadows. Every frame looks like a photographed tabletop miniature. Use modest, clearly distinct stepped pose changes and consistent anatomy.

Frame progression in strict reading order, left to right then top to bottom:
1: penguin holds rod low, looks at hole, star hidden.
2: penguin leans forward slightly, rod low.
3: penguin starts raising rod, fishing line taut.
4: penguin leans back, rod rises, pink star tip appears inside hole.
5: star half emerges, line visibly attached.
6: full star just clears hole, penguin looks at it.
7: star rises a little more, rod higher.
8: star hangs one star-height above hole, penguin eyes wide.
9: hold the same star height, penguin tilts its head in delight.
10: penguin begins lowering rod, star slightly lower.
11: star descends toward hole.
12: star touches hole rim level.
13: star half submerged.
14: only star tip visible, penguin straightens.
15: star hidden, rod returning to initial low angle.
16: same composition and near-identical pose as frame 1, ready to loop.

Prioritize exact 4x4 equal cell geometry, unchanging set placement, stable identity, line continuity and readable incremental motion. No motion blur, camera movement, frame numbers, captions, changing background, extra limbs, floating penguin or disconnected fishing line.
```

**Generated frame sheet:**

![Sixteen clay-style frames of a penguin lifting a pink star out of an ice fishing hole and lowering it back](assets/02-clay-stop-motion/penguin-star-contact-sheet.png)

#### Step 2 — Assemble the stop-motion GIF with Codex

Attach the frame sheet to Codex and use this prompt:

```text
Use Python and Pillow to turn the attached 4x4 stop-motion contact sheet into a looping GIF. Split it into 16 equal-sized frames, reading left to right and top to bottom. If the image dimensions are not divisible by four, round the cell boundaries and use a consistent crop size, trimming at most one edge pixel where necessary.

Keep the complete miniature scene in every frame. Preserve one shared crop and the original image scale. Do not crop to the penguin's silhouette or recenter it independently: the ice hole, horizon, and floor must remain in place. Do not add camera movement, interpolated poses, optical flow, or crossfades.

Use a shared 256-color palette with no dithering. Start with 140 ms per frame, hold the reveal briefly, and use a short pause at the loop boundary. Preserve the source order unless the poses clearly require a change. Export an infinitely looping GIF and provide a reproducible script with the exact frame order and durations.

Inspect the character, rod, line, star, ice hole, and first-to-last transition. Report visible drift or missing motion honestly; if source frames need correction, explain what should be regenerated rather than describing the GIF as perfectly seamless.
```

**Animated result:**

![Clay-style penguin fishing a pink star from an ice hole in a looping stop-motion GIF](assets/02-clay-stop-motion/penguin-star-stop-motion.gif)

**Example assembly:** 16 frames in source order, 313 × 313 pixels, a 2.48-second infinite loop. Each frame keeps the full miniature set. Frame durations in milliseconds: `200, 140, 140, 140, 140, 140, 140, 200, 220, 140, 140, 140, 140, 140, 140, 180`.

**What to check:** The generated sheet communicates the lift-and-lower action, but the rod angle, penguin pose, and ice-hole placement vary slightly between frames. Some line-length changes also remain. These are source-image continuity limits, so the result is a stylized frame animation with visible stepping, not a perfectly registered physical stop-motion shoot.

**Reproduce:** With Python 3 and Pillow installed, run `python scripts/build_penguin_gif.py` from the repository root. The [assembly script](scripts/build_penguin_gif.py) and [exact generation prompt](assets/02-clay-stop-motion/generation-prompt.txt) are included.

### 03. Two Characters, One Scene

Bring two separately defined characters into one scene, then animate their interaction. In this original example, greenhouse caretakers Mira and Ren place an amber seed into a lantern and watch it light up together.

**Inspiration:** [TechieSA's character-reference-to-video workflow](https://x.com/TechieBySA/status/2096196085198839832). The source post names GPT Image 2 and Seedance 2.5. This adaptation uses original characters and a new scene; it is not a reproduction of that post or a tested claim about those models.

**Workflow:** Two character images → shared opening frame → image-to-video.

**Input:** Two separate character reference images. Use your own, or create the original pair below.

**Status:** Character images and an opening frame are included. The video prompt is ready to use; no video has been generated or verified. Example stills were made with Codex's built-in image generation tool; its underlying model ID was not exposed.

#### Step 1 — Prepare two character references

Keep each character in a separate image so the video workflow can distinguish them. For this example, generate the following two-panel reference sheet, then split it into the two supplied portrait files. If using your own images, skip this generation step and assign them the same reference roles.

```text
Generate a widescreen 3:2 character reference diptych, exactly two equal vertical panels with a plain warm gray background, no border or text. The panels will be cropped into two separate identity reference images. Each panel contains exactly one full-body adult original human character, head to boots fully visible with ample margins, both at identical scale.
Left panel: MIRA, an adult woman aged about 30, medium-brown skin, short curly black bob, oval face, dark eyes, rust-orange utility jacket over cream shirt, navy work trousers, brown ankle boots. No jewelry, no hat, no props. Arms relaxed and hands fully visible.
Right panel: REN, an adult man aged about 32, light olive skin, straight dark hair tied in a small low bun, clean-shaven angular face, dark eyes, moss-green utility jacket over charcoal shirt, charcoal trousers, brown work boots. No jewelry, no hat, no props. Arms relaxed and hands fully visible.
Style: cinematic hand-painted animation concept art, softly textured gouache backgrounds, clear expressive faces, grounded anatomy, restrained warm colors, diffuse studio lighting. Neutral front three-quarter standing poses. These are original greenhouse caretakers, no celebrities, no existing film characters. Do not blend identities, duplicate people, invent props, add text or crop limbs.
```

| C03-R01 — Mira | C03-R02 — Ren |
|---|---|
| ![Mira in a rust-orange utility jacket](assets/03-two-character-video/mira-reference.png) | ![Ren in a moss-green utility jacket](assets/03-two-character-video/ren-reference.png) |

#### Step 2 — Create a shared opening frame

Upload **C03-R01 first and C03-R02 second**. Use the images to preserve the two identities while changing their poses and placing them together in the greenhouse.

```text
Use the two uploaded character portraits as separate strict identity references: image 1 is MIRA, the woman with a rust-orange jacket; image 2 is REN, the man with a moss-green jacket. Preserve each person's face, hairstyle, skin tone, age, body proportions, and entire outfit. Do not merge or swap their identities.

Create a single cinematic 16:9 opening frame in the same hand-painted animation style. A glass greenhouse at blue hour, quiet foliage at the edges, dark blue glass roof overhead, a waist-high stone workbench across the foreground. Mira stands on the LEFT, Ren on the RIGHT, facing slightly inward toward one small unlit brass lantern fixed at the center of the bench. Mira's open right palm holds exactly one small amber glass seed just left of the lantern. Ren's left hand rests beside the lantern base, leaving the empty circular socket clearly visible. All hands remain distinct. Both faces are clearly readable in a medium-wide shot.

The lantern is attached to the bench and cannot move; its socket is empty. The amber seed has not been inserted yet. Soft cool dusk light and a faint warm reflection from the seed. Calm anticipation, grounded anatomy, subtle gouache texture, no text, no labels, no montage, no extra people, no duplicate seed, no costume changes, no oversized hands. This is the first frame before the action, not the finished glowing result.
```

**C03-K01 — Opening-frame example:**

![Mira and Ren beside an unlit lantern in a greenhouse at dusk](assets/03-two-character-video/greenhouse-opening.png)

Check both faces and outfits, the single seed, the empty socket, and the separation of the hands before animating. The generated example reverses the anatomical hand assignments in the image prompt; the video prompt therefore follows the visible seed-bearing palm and free hand instead of forcing a left/right swap.

#### Step 3 — Animate the interaction

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

**Production notes:** [Chinese story, continuity rules, and exact upload instructions](cases/03-two-character-video.md). The [image prompt](assets/03-two-character-video/keyframe-prompt.txt) and [video prompt](assets/03-two-character-video/video-prompt.txt) are also available as text files.

### 04. Character to Storyboard to Film

Define a protagonist, plan the story as distinct shots, then animate each shot. In this original miniature-film concept, lighthouse mechanic Inez winds a dormant brass seabird, watches it wake, and releases it through an open window.

**Inspiration:** [el.cine's cast-design and storyboard workflow](https://x.com/EHuanglu/status/2097519538632024103). The source describes character design and storyboards followed by video generation. The lighthouse setting, character, prop, and story below are newly designed for this repository.

**Workflow:** Character design → four-shot storyboard → individual shot-start images → image-to-video → edit.

**Input:** A character concept and short story.

**Status:** Character reference, storyboard, and extracted shot-start images are included. The 12-second film remains a production plan; no generated video is included. Stills were created with Codex's built-in image generation tool, whose model ID was not exposed.

#### Step 1 — Define the character

Create one reusable identity reference. Lock Inez's age, face, glasses, hairstyle, and clothes before designing the shots.

```text
Generate one landscape 3:2 clean single-character full-body identity reference portrait. Original protagonist INEZ, a lighthouse mechanic aged about 60, warm tan skin, short silver-gray curly hair, round tortoiseshell glasses, kind lined face, navy wool chore coat over an ochre knitted sweater, charcoal trousers and weathered dark brown work boots. Her hands are empty and visible, arms relaxed, head and boots fully inside the frame with ample margins. She stands in a neutral three-quarter pose against a simple warm gray studio backdrop. No other characters or props, no collage or additional views, no text.
Visual style: tactile miniature stop-motion film design, felted wool costume, subtly sculpted expressive face, cinematic soft overcast coastal light, muted navy and ochre palette, believable anatomy. Preserve the subject as a clearly older adult woman, no glamour retouching.
```

**C04-R01 — Inez:**

![Inez, an older lighthouse mechanic in a navy coat and ochre sweater](assets/04-storyboard-video/inez-reference.png)

#### Step 2 — Design the storyboard

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

![Four shots showing Inez discovering, winding, awakening, and preparing to release a mechanical seabird](assets/04-storyboard-video/lighthouse-storyboard.png)

#### Step 3 — Prepare individual shot-start images

Split the storyboard into four images in reading order. A storyboard panel defines a shot; it is not one frame of a four-frame animation. Avoid feeding the entire grid into a first-frame-only video tool.

| ID | File | What it controls |
|---|---|---|
| C04-K01 | [Discovery](assets/04-storyboard-video/shot-01.png) | Establishing view and inert bird |
| C04-K02 | [Winding](assets/04-storyboard-video/shot-02.png) | Hand contact and key location |
| C04-K03 | [Awakening](assets/04-storyboard-video/shot-03.png) | Wing state and reaction |
| C04-K04 | [Release](assets/04-storyboard-video/shot-04.png) | Open window and takeoff position |

The included crops can be reproduced with `python scripts/prepare_video_references.py` using Python 3 and Pillow. Check costume, hand anatomy, bird geometry, attached key, and window placement across the crops. The bird body, winding-key detail, and apparent scale vary somewhat between the generated panels. Treat these as draft shot references and refine those differences before final video production; the included stills do not establish video continuity.

#### Step 4 — Animate and edit

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

**Production notes:** [Chinese story, continuity ledger, panel-edit instructions, and upload map](cases/04-storyboard-video.md). The [storyboard prompt](assets/04-storyboard-video/storyboard-prompt.txt) and [video prompt](assets/04-storyboard-video/video-prompt.txt) are supplied as text files.

### 05. Distant Observer: A Robot in the Rain

Create the feeling of noticing a small, unexpected moment from across the street. In this original scene, an old maintenance robot lowers its own umbrella over a tiny flowerpot, leaving itself in the rain. The emotional beat comes from the action and the distant framing, rather than a face close-up.

**Inspiration:** [Pablo Prompt's post](https://x.com/pabloprompt/status/2097382752622436744). Its caption credits GPT Image 2 and Seedance 2.5 in CapCut. This example develops the distant-observer approach identified in the reference brief with a newly designed robot and story; it does not reproduce the post's footage or claim that the source used GPT Image 2.5.

**Workflow:** Text-defined character → distant scene image → image-to-video.

**Input:** A character idea; optionally replace the supplied original robot with your own character reference.

**Status:** A generated robot reference and scene image are included. The 8-second video prompt is ready; video generation and motion validation remain pending. Stills were made with Codex's built-in image generation tool; its model ID was not exposed.

#### Step 1 — Define the character

Use a clean character reference to establish the robot's silhouette, colors, joints, and pouch. This close reference is for identity only; it should not become the video's opening composition.

```text
Create one portrait 2:3 full-body character identity reference photograph of an original friendly obsolete street-maintenance robot. It is a physically built practical movie prop, about 2 meters tall, with a stocky weathered rust-red steel torso, off-white rounded rectangular head, exactly two small round dark glass eyes, no mouth, two thick articulated arms, exactly three blunt fingers on each hand, two short sturdy legs, and broad dark rubber feet. Its plates show chipped paint and light rain marks, never military armor. One small olive canvas pouch is strapped at its left hip. No writing, badges, logos, screens, weapons, or human face.
The robot stands upright in a relaxed front three-quarter pose on a plain mid-gray studio floor and seamless backdrop. Both empty hands, full head, and both feet are clearly visible with ample margins. No props in the hands, no umbrella in this identity reference. Keep one single robot, no collage, no turnaround grid, no other subject.
Photoreal practical-effects cinematography, tactile metal and canvas, soft overcast illumination, understated warmth. Design a unique humble municipal helper with rounded proportions, not an existing franchise robot.
```

**C05-R01 — Robot identity reference:**

![Weathered rust-red maintenance robot with an off-white head and olive hip pouch](assets/05-distant-observer/robot-reference.png)

#### Step 2 — Build the distant scene

Upload **C05-R01 only**. Change the setting, scale within the composition, and arm pose while retaining the robot design. Establish the umbrella above the robot and the flowerpot beside it, before the act of sheltering the flower.

| Visual choice | Direction |
|---|---|
| Framing | Vertical 9:16, distant view across the street |
| Subject scale | Small in frame; the generated example is about one-fifth of frame height |
| Foreground | Soft doorway edge and ledge, away from the action |
| Camera | Compressed perspective; fixed observer position |
| Motion to preserve later | Small handheld drift; no push-in or close-up |
| Story anchor | One yellow umbrella moves from robot to flowerpot |

```text
Use the uploaded robot portrait as the strict identity reference C05-R01: preserve the rust-red stocky steel body, off-white rounded rectangular head, two round dark eyes, no mouth, two arms, three blunt fingers per hand, two legs, rubber feet, and single olive pouch at its left hip.

Create one photoreal 9:16 vertical first frame with the visual feeling of a candid distant observation of a fictional scene. The camera is sheltered inside an unoccupied cafe doorway across a narrow rain-soaked street, about 25 meters from the robot. Use a moderate telephoto perspective with compressed depth and natural lens softness, not a wide-angle close-up. A dark out-of-focus door jamb occupies only the left 8% of the image and a soft blurred ledge crosses the bottom 5%; neither covers the robot or the flowerpot. No people or camera equipment are visible.

On the far sidewalk, the robot stands just right of center beneath its one OPEN mustard-yellow umbrella. The robot's body from head to feet occupies only 24–28% of the entire image height; keep it visibly small in a much larger urban environment. Its lowered gaze is directed at one terracotta flowerpot on the ground immediately to its right, containing one short green plant with one small white flower. The pot is close enough for the robot to shelter it by lowering and moving the umbrella a short distance. The hand nearest the pot holds the umbrella shaft at chest height; the free hand hangs at its side. The umbrella is currently above the robot, NOT already above the pot. Show the shaft continuously attached to the canopy and gripped by one hand.

Quiet old tram-stop frontage with a closed teal shutter behind the robot, damp pale plaster walls, a curb, a wet road occupying much of the lower middle frame, soft rain and broad puddle reflections. No readable shop names, road text, logos, vehicles, pedestrians, or other plants. The setting and wet empty space should dominate. Overcast afternoon daylight, subdued colors except the rust-red robot, yellow umbrella, and terracotta pot. The umbrella and flowerpot remain separate and fully visible. Natural slightly imperfect observer framing, no surveillance overlays, timestamp, cinematic black bars, or exaggerated bokeh. This is an ordinary street seen from afar, with one unexpected quiet act about to happen; not a hero portrait.
```

The first generation placed the pot beneath the umbrella edge. A [local correction prompt](assets/05-distant-observer/scene-correction-prompt.txt) moves that one pot outside the canopy before animation. Upload the [draft scene C05-K00](assets/05-distant-observer/rainy-street-draft.png) alone for that correction, keeping the robot and camera fixed. The final example also places the robot slightly smaller than the original size target; the video prompt follows the actual frame.

**C05-K01 — Distant opening-frame example:**

![A small robot with a yellow umbrella on the far sidewalk, seen from a sheltered doorway across a wet street](assets/05-distant-observer/rainy-street-opening.png)

Before animation, check that the robot remains small, both feet are grounded, the umbrella shaft reaches its hand, and the pot is within reach. Rain, the road, and the shutter must remain consistent through the action.

#### Step 3 — Animate without losing the distant viewpoint

| Upload | Role |
|---|---|
| C05-K01 — rainy street scene | Required first frame; distance, environment, props, and starting pose |
| C05-R01 — robot portrait | Optional identity reference only, if an extra slot is supported |

If only one image is supported, upload **C05-K01**. Keep the distant composition even when the robot bends down. A close-up of its face would change the central idea of this case. Eight seconds is a creative target, not a claim about any particular video model's duration settings.

```text
Animate C05-K01 as the exact first frame of an 8-second photoreal 9:16 distant-observer video, one uninterrupted shot. C05-R01 is optional robot identity reference only if the tool supports an extra reference slot. If only one image is allowed, use C05-K01. Preserve its street layout, wet road, teal shutter, foreground doorway edge, robot size, umbrella, and flowerpot.

The camera remains inside the doorway across the street at the same approximately 25-meter distance. Match the robot's exact small standing scale in C05-K01 (about 18% of frame height in the supplied example), rather than enlarging it to meet a numerical target. As it bends, allow its projected height to decrease naturally; never enlarge it or move the camera to compensate. The viewer should feel they happened to notice a small event on the far sidewalk. Only very slight low-amplitude handheld drift, under 1% of frame width; no zoom, push-in, tracking toward the subject, close-up, camera cut, or dramatic rack focus. Foreground occlusion remains at the edges, never over the action.

0–2 seconds: the rust-red robot pauses under its open yellow umbrella and tilts its off-white head down toward the single terracotta pot and white flower beside it. Rain continues falling; the flower stem nods slightly. Keep exactly two eyes, no mouth, one olive hip pouch, and the same physical body proportions.
2–6 seconds: the robot bends at the knees and waist, using the hand already gripping the umbrella shaft to lower and move the still-open umbrella toward the pot. The umbrella moves as one rigid connected canopy-and-shaft assembly. Keep its grip continuous and do not swap hands. The free hand rests against its own thigh. The feet remain planted on the sidewalk. Finish with the canopy visibly centered above the pot while most of the robot's head and shoulders are outside its cover in the rain. The umbrella does not shrink, fold, detach, or touch the flower.
6–8 seconds: the robot holds the umbrella steady over the pot and quietly watches the flower. Rain remains visible around the canopy, and puddle rings continue on the road. End on this small act of care from the same distant viewpoint. The robot never notices or looks into the camera. No return to the starting pose and no loop.

Photoreal practical-effects character with believable joint motion, damp metal, soft daylight, and restrained movement. Optional audio: rain recorded from the sheltered camera position, with very faint mechanical movement at a distance; no close-miked dialogue, music cue, or dramatic sound effect. If audio is not supported, export silently.

Negative prompt: growing subject, automatic zoom, face close-up, moving across the street, camera orbit, film cuts, eye contact with camera, waving at viewer, extra robot or person, extra umbrella, second flowerpot, umbrella changing size, detached shaft, grip swap, additional fingers, floating feet, sunlight transition, dry pavement, disappearing rain, added text, watermark, timestamp, CCTV interface.
```

**Video result:** Pending generation. Validate the umbrella's rigid shape and continuous grip, the pot's fixed location, natural joints, and the absence of an automatic zoom. The body occupies less vertical space when bending; preserve camera distance rather than enlarging the crouched robot to compensate.

**Production notes:** [Chinese story, continuity rules, and per-image upload instructions](cases/05-distant-observer.md). Download the [scene prompt](assets/05-distant-observer/scene-prompt.txt) and [video prompt](assets/05-distant-observer/video-prompt.txt) for reuse.

### 06. Frosted Glass Poster to 360° Orbit

**by SeeAPI**

Turn a minimalist exhibition poster into a six-second product film: the camera makes one full orbit around a sculptural frosted-glass mug, then returns to the original poster composition. Changing refraction and the handle's silhouette make the motion readable.

**Workflow:** Text to image → image to 360° orbit video.

**Input:** The image prompt below, or the supplied finished poster.

**Status:** The supplied poster and ready-to-use video prompts are included. The video will be generated separately by the contributor; no orbit video has been generated or validated here. The source image's generation model and settings were not recorded.

#### Step 1 — Generate the exhibition poster

The prompt below preserves the supplied wording, with formatting escapes removed. The supplied render uses an uppercase subtitle, so the video prompt follows its visible lettering.

```text
A minimalist futurist exhibition poster with an ultra-light cool yellow background (#e7ff48).

At the center of the poster is a fluid 3D metaball shaped mug in full form, rendered in frosted glass with delicate grainy noise.
The fluid gradient transitions from light yellow (#E7FF48) to Pearl White (#FFFFFF), giving it a silky glass-like appearance.

High-position softbox lighting casts long, soft colored shadows and a subtle halo.

The fluid overlaps with the text: letters obscured by the frosted glass appear with a gentle Gaussian blur.
- The main title, the light yellow “SeeAPI” logo, is centered and partially obscured by the fluid. The covered letters are slightly blurred through the frosted glass.
- The subtitle, in bold all-caps modern sans-serif pure black font, reads: “Images, videos and models API”, placed below the main title. It is also partially overlapped by the fluid and blurred in those areas, while the rest remains sharp.

The overall layout is clean with generous whitespace, balanced composition, sharp focus, and HDR high dynamic range.
```

**C06-R01 — Supplied frosted-glass poster:**

![SeeAPI exhibition poster with a frosted fluid-shaped mug on a cool-yellow background](assets/06-360-orbit/frosted-glass-mug-poster.png)

#### Step 2 — Generate a complete six-second orbit

Upload **C06-R01 as the first frame**. If the video tool has a last-frame slot, use the same image there to guide the return composition. Keep the output square, matching the source.

The camera travels around a stationary mug. The typography is treated as a fixed graphic layer behind the mug's projected image, with changing glass occlusion. This keeps the brand layout readable without turning the entire poster into a rotating plane.

```text
Create a 6-second, square 1:1 product film in ONE continuous shot, using C06-R01 as the exact opening composition. The hook is one complete 360-degree camera orbit around the same sculptural frosted-glass mug, revealing its fluid silhouette, hollow rim, single attached handle, and changing transmitted light. Preserve the minimalist futurist exhibition-poster aesthetic and cool yellow #E7FF48 to pearl-white palette.

Keep exactly one mug with the source image's proportions, asymmetric metaball contours, glass thickness, open top, and one continuous handle. The mug remains stationary in world space at its original height relative to the surface; its position, shape, and orientation do not animate. Infer unseen surfaces conservatively as a continuation of that same mug, without adding decoration or a second handle.

SHOT 1: Starting at the supplied three-quarter view, move the camera clockwise as seen from above through one uninterrupted circular orbit: front three-quarter to side, rear, opposite side, and back to the exact starting view. Complete the full 360 degrees within the six seconds. Keep the camera radius, elevation, focal length, and aim at the mug's center fixed, with no camera roll. Let the motion begin promptly and run at a smooth near-constant pace so every side is shown; settle briefly only after returning to the starting angle. Keep the whole mug and handle within the frame at a stable scale. Let the single handle naturally become hidden by the body and reappear according to perspective; it must never split or jump between sides.

The high softbox and seamless cool-yellow studio environment remain fixed in world space. Highlights, visible glass thickness, refraction, and the projected soft shadow change coherently as the camera travels. Preserve the fine frosted grain as surface texture, not flickering noise. The glass stays frosted and translucent throughout, with a restrained halo and no melting or opacity transformation.

Typography is a screen-aligned exhibition graphic behind the rendered mug, not lettering printed on the mug and not a physical sign that the camera orbits. Keep the source layout, font, spacing, colors, and exact visible text fixed: "SeeAPI" and "IMAGES, VIDEOS AND MODELS API". As the mug's projection changes, only the regions seen through its frosted glass receive gentle refraction and soft blur; unobscured text stays sharp. Never rotate, mirror, rewrite, or move the letters with the mug. At the final angle, restore the original overlap and blur pattern.

End at the source camera angle, scale, lighting, and composition with zero residual camera motion. If a last-frame slot is available, use C06-R01 there as well while retaining the full-orbit instruction. The result should reveal actual changing viewpoints of a volumetric object, not rotate the flat poster, spin the mug on a turntable, or substitute a zoom or layered 2D drift. No scene cuts. Silent output is suitable.
```

**Negative prompt:**

```text
Partial orbit, camera reversing before completing the circle, stationary-camera turntable spin, flat poster rotation, simple zoom or 2D parallax, jump cut hiding the back, extra mug, extra handle, detached handle, sealed mug opening, changing rim shape, melting glass, changing product scale, camera roll, tilt drift, sudden opacity changes, random sparkling particles, unstable grain, moving or misspelled lettering, mirrored text, text printed onto the mug, extra captions, watermarks, background color change, mismatched final viewpoint.
```

**Before publishing:** Confirm that the camera actually shows the side and back before returning, rather than stopping halfway or spinning the object. Check the single handle, hollow rim, frosted material, exact lettering, and final alignment. A single source image does not establish the mug's hidden geometry, so the generated rear view must be reviewed. Matching first and last images alone does not prove that a full orbit occurred.

**Typography note:** If the video tool cannot hold the lettering or reproduce the glass blur reliably, composite the typography in post-production. A basic overlay can preserve spelling and placement; the through-glass effect additionally needs a matching mask and blur/refraction treatment.

**Video result:** Pending contributor generation. [Chinese upload and camera instructions](cases/06-360-orbit.md) · [Video prompt](assets/06-360-orbit/video-prompt.txt) · [Negative prompt](assets/06-360-orbit/negative-prompt.txt).

**Attribution:** Reproduction of this example is permitted with proper attribution to SeeAPI.

## 🗂 Prompt Directory

Browse standalone prompts for image generation and editing. New examples will be added regularly and listed first. The current entries are starter prompts; example images and reproduction notes will be added after testing.

Original prompts are credited to SeeAPI. Entries adapted from a source or inspired by a shared reference will name and link to that source.

- [P08: Glass Material Remix (by SeeAPI)](#p08-glass-material-remix)
- [P07: Paper-Cut Storybook Scene (by SeeAPI)](#p07-paper-cut-storybook-scene)
- [P06: One Character, Three Scenes (by SeeAPI)](#p06-one-character-three-scenes)
- [P05: Editorial Poster with Exact Copy (by SeeAPI)](#p05-editorial-poster-with-exact-copy)
- [P04: Product Photo to Campaign Visual (by SeeAPI)](#p04-product-photo-to-campaign-visual)
- [P03: Miniature World in an Everyday Object (by SeeAPI)](#p03-miniature-world-in-an-everyday-object)
- [P02: Collectible Figure Packaging (by SeeAPI)](#p02-collectible-figure-packaging)
- [P01: Personalized Sticker Pack (by SeeAPI)](#p01-personalized-sticker-pack)

### P01. Personalized Sticker Pack

**by SeeAPI**

Turn an original character into a set of expressive stickers.

**Input:** One character image you can use. **Starting model:** Sunburst for reference-based work.

```text
Using the uploaded character as the identity reference, create a clean 2-by-2 sticker sheet with four expressions: delighted, sleepy, surprised, and quietly proud.

Keep the character's face shape, colors, outfit, and distinctive features consistent. Show the complete character in each cell, with a thick white sticker outline and ample separation between stickers. Use a flat pastel-pink background so the silhouettes are easy to isolate. No captions, letters, decorative objects, or overlap between cells.
```

**Next step:** Check each expression, then crop and isolate the stickers individually. A flat background is not a transparent export.

### P02. Collectible Figure Packaging

**by SeeAPI**

Design an original toy concept with a clear character and accessory layout.

**Input:** None; optionally add your own character reference. **Starting model:** Flare for a new concept.

```text
Create a studio product photograph of an original collectible toy called "MOON GARDENER" inside a clear blister package on a midnight-blue cardboard backing.

The figure is a cheerful astronaut wearing a cream spacesuit with sage-green gardening gloves. Arrange exactly three accessories in separate compartments to its right: a tiny watering can, a potted sprout, and a small shovel. Keep the figure fully visible. Place the title "MOON GARDENER" at the top in large, readable lettering. Use realistic molded plastic, controlled reflections, and soft studio shadows. No additional text or existing brand logos. Portrait composition.
```

**Next step:** Check the title, accessory count, and reflections. If using a character reference, explicitly ask to preserve its identifying features.

### P03. Miniature World in an Everyday Object

**by SeeAPI**

Give a familiar object a surprising second life.

**Input:** None. **Starting model:** Flare.

```text
A miniature hillside village built inside an open vintage suitcase resting on a real wooden table. The suitcase contains a winding stone path, five small cottages, moss-covered terraces, and a tiny pond. Its open lid forms the backdrop, lined with faded botanical fabric.

Show the whole suitcase from a three-quarter overhead angle. Make the scale relationship unmistakable through detailed stitching, brass clasps, and a life-size ceramic cup beside it. Warm afternoon light, realistic miniature materials, shallow depth of field that keeps the village readable. No floating buildings or text. Landscape composition.
```

### P04. Product Photo to Campaign Visual

**by SeeAPI**

Change the setting while keeping the product recognizable.

**Input:** One clear product photo. **Starting model:** Sunburst.

```text
Edit the uploaded product photograph. Preserve the product's silhouette, proportions, orientation, packaging, logo placement, and all visible label wording.

Replace the surrounding scene with a warm ivory studio background and a matte stone platform. Add soft window light from the upper left and a natural contact shadow beneath the product. Keep the product on the right half of the frame and leave the left half uncluttered for copy to be added later.

Do not add text, extra products, decorative ingredients, or a new label. Do not crop any part of the product. Landscape composition.
```

**Next step:** Compare the product and label against the source before using the image. Add campaign copy after approving the product rendering.

### P05. Editorial Poster with Exact Copy

**by SeeAPI**

Start with a short headline and a clear layout hierarchy.

**Input:** None. **Starting model:** Flare; use Sunburst for focused revisions.

```text
Design a portrait exhibition poster on warm off-white paper. A large sculptural cobalt-blue ribbon occupies the middle third of the composition, lit from the upper left with a soft shadow.

Include only this exact text:
Top, large bold sans-serif: "FORM & FLOW"
Below the sculpture, smaller: "A Study in Motion"
Bottom, small: "October 18–24"

Use generous margins, a strict left-aligned text grid, and strong separation between the title, sculpture, and supporting copy. Keep every word fully visible. No extra lettering, logos, frames, or watermarks.
```

**Next step:** Proofread every word and inspect readability at the intended display size.

### P06. One Character, Three Scenes

**by SeeAPI**

Build a small visual series around one approved character.

**Input:** One original character reference. **Starting model:** Sunburst for reference-based refinements.

```text
Use the uploaded image as the character identity reference. Preserve the character's facial features, hairstyle, outfit, colors, and body proportions.

Create one new image of this character browsing a quiet neighborhood bookshop. The character is holding a closed book in both hands, with a warm reading lamp and softly blurred shelves behind them. Eye-level medium shot, gentle natural lighting, and the same visual style as the reference. No additional foreground characters or readable text.
```

**Next step:** Generate separate versions by changing only the scene and action—for example, waiting at a train platform or tending a balcony plant. Reuse the original reference each time and compare identity details across all three images.

### P07. Paper-Cut Storybook Scene

**by SeeAPI**

Create depth from layered paper rather than photographic realism.

**Input:** None. **Starting model:** Flare.

```text
A storybook forest made entirely from layered cut paper. A small cream-colored rabbit stands on a curved ochre path beneath oversized fern leaves, looking toward a lantern hanging from a low branch.

Use visible paper fibers, crisp cut edges, gently bent leaves, and real shadows between the layers. Limit the palette to forest green, warm cream, ochre, and muted coral. Compose the scene like a shallow theatrical set viewed from the front, with a clear foreground, middle ground, and background. No text, glossy plastic, or photorealistic fur. Square composition.
```

### P08. Glass Material Remix

**by SeeAPI**

Reimagine an object's material while keeping its recognizable form.

**Input:** One clear object image. **Starting model:** Sunburst.

```text
Transform the main object in the uploaded image into translucent amber glass while preserving its overall silhouette, proportions, orientation, and defining structural details.

Place it on a pale stone surface against a warm gray studio background. Show believable glass thickness, subtle internal reflections, softened refraction through curved areas, and a grounded contact shadow. Use a large soft light from the left and a faint rim light from behind. Keep the full object visible. Do not add extra parts, labels, text, or unrelated props.
```

**Next step:** Inspect edges, supports, and transparent areas. Refine structural mistakes before exploring alternate colors or materials.

---

Curated by SeeAPI. Independent of OpenAI; product names belong to their respective owners.
