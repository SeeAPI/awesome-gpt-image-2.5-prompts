"""Rebuild case 01 with Python 3 and Pillow: python scripts/build_elephant_gif.py."""

from pathlib import Path

from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "01-pixel-art-gif"
sheet = Image.open(ASSETS / "elephant-sprite-sheet.png").convert("RGB")
sprites = []
for row in range(4):
    for col in range(4):
        cell = sheet.crop((round(col * sheet.width / 4), round(row * sheet.height / 4),
                           round((col + 1) * sheet.width / 4), round((row + 1) * sheet.height / 4)))
        # Ignore the nearly white background when finding the character bounds.
        channels = cell.split()
        darkest = ImageChops.darker(ImageChops.darker(channels[0], channels[1]), channels[2])
        bounds = darkest.point(lambda value: 255 if value < 210 else 0).getbbox()
        if bounds is None:
            raise ValueError(f"Empty sprite cell: {row * 4 + col + 1}")
        sprites.append(cell.crop(bounds))

size = (max(sprite.width for sprite in sprites) + 16,
        max(sprite.height for sprite in sprites) + 16)
centered = []
for sprite in sprites:
    frame = Image.new("RGB", size, "white")
    frame.paste(sprite, ((size[0] - sprite.width) // 2, (size[1] - sprite.height) // 2))
    centered.append(frame)

# Source cells are numbered left to right, top to bottom, starting at 1.
# Move the crouching cells after the roll to connect recovery to standing.
order = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 4, 3, 13, 14, 15, 16]
durations = [180, 110, 110, 110, 100, 100, 100, 100, 100, 110, 110, 110, 110, 100, 100, 160]
atlas = Image.new("RGB", (size[0] * 4, size[1] * 4), "white")
for index, frame in enumerate(centered):
    atlas.paste(frame, ((index % 4) * size[0], (index // 4) * size[1]))
palette = atlas.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
frames = [centered[index - 1].quantize(palette=palette, dither=Image.Dither.NONE) for index in order]
output = ASSETS / "elephant-roll.gif"
frames[0].save(output, save_all=True, append_images=frames[1:], duration=durations,
               loop=0, disposal=2, optimize=False)

with Image.open(output) as result:
    assert result.n_frames == 16
    assert result.info["loop"] == 0
    assert result.size == size
    total = 0
    for index in range(result.n_frames):
        result.seek(index)
        total += result.info["duration"]
print(f"Created {output.name}: {size[0]} x {size[1]}, 16 frames, {total} ms, infinite loop")
