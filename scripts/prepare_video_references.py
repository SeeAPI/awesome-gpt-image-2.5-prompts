"""Extract case 03 identities and case 04 panels with Python 3 and Pillow.

This prepares still-image references only; it does not generate video.
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
pair_dir = ROOT / "assets" / "03-two-character-video"
pair = Image.open(pair_dir / "character-reference-sheet.png")
mid = pair.width // 2
# Omit the thin central seam without changing either person's proportions.
pair.crop((0, 0, mid - 4, pair.height)).save(pair_dir / "mira-reference.png")
pair.crop((mid + 4, 0, pair.width, pair.height)).save(pair_dir / "ren-reference.png")

board_dir = ROOT / "assets" / "04-storyboard-video"
board = Image.open(board_dir / "lighthouse-storyboard.png")
width, height = board.width // 2, board.height // 2
for row in range(2):
    for col in range(2):
        left, top = round(col * board.width / 2), round(row * board.height / 2)
        # Identical output sizes; trim at most one pixel for an odd source dimension.
        box = (left, top, left + width, top + height)
        panel = board.crop(box)
        output = board_dir / f"shot-{row * 2 + col + 1:02d}.png"
        panel.save(output)
        print(f"{output.name}: {panel.width} x {panel.height}")
