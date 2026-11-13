#!/usr/bin/env python3
"""
Generate pond background variants for git-koi.
Produces:
  - koi/koi-zen-pond.gif    (Deep Zen Water Pond with ripples & lily pads)
  - koi/koi-tokyonight.gif   (TokyoNight themed dark card with subtle borders)
"""

import os
import math
from PIL import Image, ImageDraw, ImageSequence

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOI_DIR = os.path.join(BASE_DIR, "koi")
INPUT_GIF = os.path.join(KOI_DIR, "koi.gif")

def create_zen_pond(size=(512, 512)):
    bg = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)
    cx, cy, r = size[0] // 2, size[1] // 2, 246

    # Outer pond border / stone rim
    draw.ellipse([cx - r - 6, cy - r - 6, cx + r + 6, cy + r + 6], fill=(16, 28, 48, 255))
    draw.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=(24, 42, 70, 255))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(12, 25, 45, 255))

    # Deep water gradient rings
    for radius in range(r - 1, 0, -2):
        factor = radius / r
        r_col = int(6 * factor + 16 * (1 - factor))
        g_col = int(20 * factor + 52 * (1 - factor))
        b_col = int(40 * factor + 92 * (1 - factor))
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(r_col, g_col, b_col, 255))

    # Water ripples
    for rip_r in [55, 105, 155, 205]:
        draw.ellipse([cx - rip_r, cy - rip_r, cx + rip_r, cy + rip_r], outline=(255, 255, 255, 18), width=2)

    # Lily pads & blossoms
    def draw_lily(lx, ly, l_r, notch_deg):
        draw.ellipse([lx - l_r, ly - l_r, lx + l_r, ly + l_r], fill=(30, 115, 75, 245), outline=(55, 160, 105, 255), width=2)
        rad = math.radians(notch_deg)
        nx = lx + math.cos(rad) * l_r
        ny = ly + math.sin(rad) * l_r
        draw.polygon([(lx, ly), (nx, ny), (lx + math.cos(rad + 0.35) * l_r, ly + math.sin(rad + 0.35) * l_r)], fill=(10, 28, 52, 255))
        # Pink lotus blossom
        draw.ellipse([lx - 5, ly - 5, lx + 5, ly + 5], fill=(255, 150, 185, 240))
        draw.ellipse([lx - 2, ly - 2, lx + 2, ly + 2], fill=(255, 230, 240, 255))

    draw_lily(100, 115, 34, 40)
    draw_lily(130, 90, 24, 120)
    draw_lily(415, 395, 36, 210)
    draw_lily(380, 430, 26, 300)

    return bg

def create_tokyonight_card(size=(512, 512)):
    bg = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)

    pad = 12
    box = [pad, pad, size[0] - pad, size[1] - pad]
    # Card border glow
    draw.rounded_rectangle([pad - 3, pad - 3, size[0] - pad + 3, size[1] - pad + 3], radius=36, fill=(26, 37, 64, 255))
    draw.rounded_rectangle(box, radius=32, fill=(13, 20, 37, 255), outline=(36, 123, 255, 180), width=3)

    # Subtle inner aquatic gradient ring
    cx, cy = size[0] // 2, size[1] // 2
    for radius in range(210, 0, -3):
        factor = radius / 210
        r_col = int(13 * factor + 18 * (1 - factor))
        g_col = int(20 * factor + 35 * (1 - factor))
        b_col = int(37 * factor + 65 * (1 - factor))
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(r_col, g_col, b_col, 255))

    for rip_r in [70, 140]:
        draw.ellipse([cx - rip_r, cy - rip_r, cx + rip_r, cy + rip_r], outline=(114, 135, 253, 25), width=2)

    return bg

def create_ripple_pond(size=(512, 512)):
    bg = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)
    cx, cy = size[0] // 2, size[1] // 2

    for radius in range(230, 0, -2):
        factor = radius / 230
        alpha = int(140 * (1 - factor**2))
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(15, 25, 45, alpha))

    for rip_r in [50, 100, 150, 200]:
        draw.ellipse([cx - rip_r, cy - rip_r, cx + rip_r, cy + rip_r], outline=(56, 189, 248, 35), width=2)

    return bg

def composite_gif(bg_img, in_path, out_path):
    if not os.path.exists(in_path):
        print(f"Skipping {out_path}: {in_path} does not exist.")
        return

    koi = Image.open(in_path)
    frames = []
    for frame in ImageSequence.Iterator(koi):
        f_rgba = frame.convert("RGBA")
        comp = Image.alpha_composite(bg_img, f_rgba)
        frames.append(comp.convert("P", palette=Image.ADAPTIVE))

    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=koi.info.get("duration", 70),
        loop=0,
        optimize=True
    )
    print(f"Generated: {out_path}")

def main():
    if not os.path.exists(INPUT_GIF):
        print(f"Error: {INPUT_GIF} not found.")
        return

    print("Compositing Zen Pond...")
    zen_bg = create_zen_pond()
    composite_gif(zen_bg, INPUT_GIF, os.path.join(KOI_DIR, "koi-zen-pond.gif"))

    print("Compositing TokyoNight Card...")
    tn_bg = create_tokyonight_card()
    composite_gif(tn_bg, INPUT_GIF, os.path.join(KOI_DIR, "koi-tokyonight.gif"))

    print("Compositing Minimal Ripple Pond...")
    rip_bg = create_ripple_pond()
    composite_gif(rip_bg, INPUT_GIF, os.path.join(KOI_DIR, "koi-ripple.gif"))
    print("All pond variants generated successfully!")

if __name__ == "__main__":
    main()
