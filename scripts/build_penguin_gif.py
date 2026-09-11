"""Rebuild case 02 with Python 3 and Pillow: python scripts/build_penguin_gif.py."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "02-clay-stop-motion"
sheet = Image.open(ASSETS / "penguin-star-contact-sheet.png").convert("RGB")
if sheet.width != sheet.height:
    raise ValueError("Expected a square 4-by-4 contact sheet")
side = sheet.width // 4
# Rounding handles generated sheets whose dimensions are not divisible by four.
# Take the same floor-sized crop from each cell, trimming at most one edge pixel.
frames = []
for row in range(4):
    for col in range(4):
        left, top = round(col * sheet.width / 4), round(row * sheet.height / 4)
        frames.append(sheet.crop((left, top, left + side, top + side)))
# Keep a shared crop: independently centering the penguin would move the entire set.
palette = sheet.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
durations = [200, 140, 140, 140, 140, 140, 140, 200,
             220, 140, 140, 140, 140, 140, 140, 180]
output = ASSETS / "penguin-star-stop-motion.gif"
frames[0].save(output, save_all=True, append_images=frames[1:], duration=durations,
               loop=0, disposal=2, optimize=False)
with Image.open(output) as result:
    assert result.n_frames == 16
    assert result.info["loop"] == 0
    assert result.size == (side, side)
    total = 0
    for index in range(result.n_frames):
        result.seek(index)
        total += result.info["duration"]
print(f"Created {output.name}: {side} x {side}, 16 frames, {total} ms, infinite loop")
