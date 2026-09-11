# Awesome GPT Image 2.5 Prompts ✨

**Creative image prompts and workflows, curated by SeeAPI.**

Explore GPT Image 2.5 ideas for character stickers, product visuals, miniature worlds, GIF assets, and stop-motion-style scenes. Copy a prompt, make it your own, and explore new creative directions.

This collection will grow with regular additions of prompt examples, generated images, and practical reproduction notes.

## 📖 Contents

- [🧭 Choose Your Model](#-choose-your-model)
- [🗂 Prompt Directory](#-prompt-directory)
- [💡 10 Creative Things to Try](#-10-creative-things-to-try)

## 🧭 Choose Your Model

OpenAI's GPT Image 2.5 family includes Sunburst and Flare. Both accept text and image inputs and produce still images.

### GPT Image 2.5 Sunburst

Sunburst is OpenAI's most capable image generation and editing model, with an emphasis on editing precision. It can create new images or revise existing ones from text instructions and image references.

**API model ID:** `gpt-image-2.5-sunburst` · [Official documentation](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)

### GPT Image 2.5 Flare

Flare is OpenAI's fastest model for high-quality everyday image generation. It supports text prompts and image references for creating new visuals.

**API model ID:** `gpt-image-2.5-flare` · [Official documentation](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)

## 🗂 Prompt Directory

A growing library of individual prompt examples, updated regularly. Each entry will include a copyable prompt, an example image, the model used, any required reference images, and source credits where applicable.

**Coming soon:** New entries will be listed here with links to their full prompts and images, with the latest additions first.

For starter prompts you can try now, explore the [10 creative ideas below](#-10-creative-things-to-try).

## 💡 10 Creative Things to Try

These are original starter prompts and workflow ideas, not a gallery of verified outputs. Example images and reproduction notes will be added after testing. Prompts describe the intended result; details such as text accuracy and character consistency should be checked after generation.

| # | Idea | Starting material | Output path |
|---|---|---|---|
| 01 | [Reaction GIF Character](#01-reaction-gif-character) | Text | Still → animation → GIF |
| 02 | [Clay Stop-Motion Scene](#02-clay-stop-motion-scene) | Text | Still → animation |
| 03 | [Personalized Sticker Pack](#03-personalized-sticker-pack) | Character reference | Image → individual stickers |
| 04 | [Collectible Figure Packaging](#04-collectible-figure-packaging) | Text or character reference | Image |
| 05 | [Miniature World in an Everyday Object](#05-miniature-world-in-an-everyday-object) | Text | Image |
| 06 | [Product Photo to Campaign Visual](#06-product-photo-to-campaign-visual) | Product photo | Image edit |
| 07 | [Editorial Poster with Exact Copy](#07-editorial-poster-with-exact-copy) | Text | Image |
| 08 | [One Character, Three Scenes](#08-one-character-three-scenes) | Character reference | Separate images |
| 09 | [Paper-Cut Storybook Scene](#09-paper-cut-storybook-scene) | Text | Image |
| 10 | [Glass Material Remix](#10-glass-material-remix) | Object reference | Image edit |

GPT Image 2.5 produces still images. The GIF and stop-motion ideas below require a separate animation step and, where needed, GIF export.

### 01. Reaction GIF Character

Create a recognizable character with a simple silhouette, ready for a short reaction loop.

**Input:** None. **Starting model:** Flare.

```text
Create a single animation-ready keyframe of a tiny round orange fox sitting at a desk, looking directly at the viewer with a delighted expression. Its ears are upright, paws rest beside a small cream mug, and its fluffy tail curls around its body.

Use a clean 3D cartoon style, soft matte materials, warm studio lighting, and a plain pale-blue background. Center the full character in a square composition with generous space above its ears. Keep the silhouette clear and the desk simple. No text, borders, or additional characters.
```

**Next step:** Animate one small action, such as an ear twitch and blink, with a fixed camera. Check the transition between the last and first frames before exporting a looping GIF.

### 02. Clay Stop-Motion Scene

Build a handmade miniature scene as the starting frame for a stop-motion-style clip.

**Input:** None. **Starting model:** Flare.

```text
A handmade clay squirrel in a tiny bakery, standing behind a wooden counter with one miniature croissant on a plate. The squirrel wears a simple moss-green apron and rests both paws on the counter.

Visible clay fingerprints, slightly uneven sculpted edges, felt curtains, and a warm paper backdrop give the set a practical handcrafted appearance. Frame the scene at the squirrel's eye level, with the entire counter and character visible. Soft light enters from the left. Keep every object physically supported. No text or motion blur. Landscape composition.
```

**Next step:** Use the approved still as a reference for a short animation in which the squirrel lifts the croissant. Request small, stepped movements and a locked camera. Review paws, props, and character shape between frames.

### 03. Personalized Sticker Pack

Turn an original character into a set of expressive stickers.

**Input:** One character image you can use. **Starting model:** Sunburst for reference-based work.

```text
Using the uploaded character as the identity reference, create a clean 2-by-2 sticker sheet with four expressions: delighted, sleepy, surprised, and quietly proud.

Keep the character's face shape, colors, outfit, and distinctive features consistent. Show the complete character in each cell, with a thick white sticker outline and ample separation between stickers. Use a flat pastel-pink background so the silhouettes are easy to isolate. No captions, letters, decorative objects, or overlap between cells.
```

**Next step:** Check each expression, then crop and isolate the stickers individually. A flat background is not a transparent export.

### 04. Collectible Figure Packaging

Design an original toy concept with a clear character and accessory layout.

**Input:** None; optionally add your own character reference. **Starting model:** Flare for a new concept.

```text
Create a studio product photograph of an original collectible toy called "MOON GARDENER" inside a clear blister package on a midnight-blue cardboard backing.

The figure is a cheerful astronaut wearing a cream spacesuit with sage-green gardening gloves. Arrange exactly three accessories in separate compartments to its right: a tiny watering can, a potted sprout, and a small shovel. Keep the figure fully visible. Place the title "MOON GARDENER" at the top in large, readable lettering. Use realistic molded plastic, controlled reflections, and soft studio shadows. No additional text or existing brand logos. Portrait composition.
```

**Next step:** Check the title, accessory count, and reflections. If using a character reference, explicitly ask to preserve its identifying features.

### 05. Miniature World in an Everyday Object

Give a familiar object a surprising second life.

**Input:** None. **Starting model:** Flare.

```text
A miniature hillside village built inside an open vintage suitcase resting on a real wooden table. The suitcase contains a winding stone path, five small cottages, moss-covered terraces, and a tiny pond. Its open lid forms the backdrop, lined with faded botanical fabric.

Show the whole suitcase from a three-quarter overhead angle. Make the scale relationship unmistakable through detailed stitching, brass clasps, and a life-size ceramic cup beside it. Warm afternoon light, realistic miniature materials, shallow depth of field that keeps the village readable. No floating buildings or text. Landscape composition.
```

### 06. Product Photo to Campaign Visual

Change the setting while keeping the product recognizable.

**Input:** One clear product photo. **Starting model:** Sunburst.

```text
Edit the uploaded product photograph. Preserve the product's silhouette, proportions, orientation, packaging, logo placement, and all visible label wording.

Replace the surrounding scene with a warm ivory studio background and a matte stone platform. Add soft window light from the upper left and a natural contact shadow beneath the product. Keep the product on the right half of the frame and leave the left half uncluttered for copy to be added later.

Do not add text, extra products, decorative ingredients, or a new label. Do not crop any part of the product. Landscape composition.
```

**Next step:** Compare the product and label against the source before using the image. Add campaign copy after approving the product rendering.

### 07. Editorial Poster with Exact Copy

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

### 08. One Character, Three Scenes

Build a small visual series around one approved character.

**Input:** One original character reference. **Starting model:** Sunburst for reference-based refinements.

```text
Use the uploaded image as the character identity reference. Preserve the character's facial features, hairstyle, outfit, colors, and body proportions.

Create one new image of this character browsing a quiet neighborhood bookshop. The character is holding a closed book in both hands, with a warm reading lamp and softly blurred shelves behind them. Eye-level medium shot, gentle natural lighting, and the same visual style as the reference. No additional foreground characters or readable text.
```

**Next step:** Generate separate versions by changing only the scene and action—for example, waiting at a train platform or tending a balcony plant. Reuse the original reference each time and compare identity details across all three images.

### 09. Paper-Cut Storybook Scene

Create depth from layered paper rather than photographic realism.

**Input:** None. **Starting model:** Flare.

```text
A storybook forest made entirely from layered cut paper. A small cream-colored rabbit stands on a curved ochre path beneath oversized fern leaves, looking toward a lantern hanging from a low branch.

Use visible paper fibers, crisp cut edges, gently bent leaves, and real shadows between the layers. Limit the palette to forest green, warm cream, ochre, and muted coral. Compose the scene like a shallow theatrical set viewed from the front, with a clear foreground, middle ground, and background. No text, glossy plastic, or photorealistic fur. Square composition.
```

### 10. Glass Material Remix

Reimagine an object's material while keeping its recognizable form.

**Input:** One clear object image. **Starting model:** Sunburst.

```text
Transform the main object in the uploaded image into translucent amber glass while preserving its overall silhouette, proportions, orientation, and defining structural details.

Place it on a pale stone surface against a warm gray studio background. Show believable glass thickness, subtle internal reflections, softened refraction through curved areas, and a grounded contact shadow. Use a large soft light from the left and a faint rim light from behind. Keep the full object visible. Do not add extra parts, labels, text, or unrelated props.
```

**Next step:** Inspect edges, supports, and transparent areas. Refine structural mistakes before exploring alternate colors or materials.

---

Curated by SeeAPI. Independent of OpenAI; product names belong to their respective owners.
