#!/usr/bin/env python3
import math
from PIL import Image, ImageDraw

def create_aura_logo(size=1024):
    # Supersampling 2x for ultra-sharp anti-aliased edges
    scale = 2
    dim = size * scale
    img = Image.new("RGBA", (dim, dim), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center = dim / 2
    r_outer = dim * 0.44
    r_inner = dim * 0.35

    # Draw smooth gradient ring (The "Aura")
    num_segments = 360
    # Palette: Indigo (#4F46E5) -> Violet (#8B5CF6) -> Fuchsia (#D946EF) -> Cyan (#06B6D4) -> Indigo
    colors = [
        (6, 182, 212),   # Cyan
        (79, 70, 229),   # Indigo
        (139, 92, 246),  # Violet
        (217, 70, 239),  # Fuchsia
        (99, 102, 241),  # Purple
        (6, 182, 212),   # Back to Cyan
    ]

    def interpolate_color(t):
        idx = t * (len(colors) - 1)
        i = int(idx)
        f = idx - i
        if i >= len(colors) - 1:
            return colors[-1]
        c1, c2 = colors[i], colors[i+1]
        return (
            int(c1[0] + (c2[0] - c1[0]) * f),
            int(c1[1] + (c2[1] - c1[1]) * f),
            int(c1[2] + (c2[2] - c1[2]) * f),
            255
        )

    # 1. Draw outer ring ribbon
    ring_thickness = r_outer - r_inner
    mid_r = (r_outer + r_inner) / 2
    step = 0.5
    angle = 0
    while angle < 360:
        rad = math.radians(angle)
        rad_next = math.radians(angle + step * 1.5)
        t = angle / 360.0
        col = interpolate_color(t)

        x1 = center + r_inner * math.cos(rad)
        y1 = center + r_inner * math.sin(rad)
        x2 = center + r_outer * math.cos(rad)
        y2 = center + r_outer * math.sin(rad)
        x3 = center + r_outer * math.cos(rad_next)
        y3 = center + r_outer * math.sin(rad_next)
        x4 = center + r_inner * math.cos(rad_next)
        y4 = center + r_inner * math.sin(rad_next)

        draw.polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], fill=col)
        angle += step

    # 2. Draw modern geometric "A" inside the ring
    # Coordinates for crisp modern chevron A
    a_top_y = center - dim * 0.22
    a_bottom_y = center + dim * 0.22
    a_width = dim * 0.24
    stroke = dim * 0.055

    # Left leg
    p_top = (center, a_top_y)
    p_bottom_left = (center - a_width, a_bottom_y)
    p_bottom_right = (center + a_width, a_bottom_y)

    # Gradient for the A (Cyan to Bright White-Cyan)
    draw.line([p_bottom_left, p_top], fill=(255, 255, 255, 255), width=int(stroke), joint="curve")
    draw.line([p_top, p_bottom_right], fill=(255, 255, 255, 255), width=int(stroke), joint="curve")

    # Crossbar of "A" - dynamic cyan accent
    bar_y = center + dim * 0.06
    bar_left = (center - a_width * 0.55, bar_y)
    bar_right = (center + a_width * 0.55, bar_y)
    draw.line([bar_left, bar_right], fill=(6, 182, 212, 255), width=int(stroke * 0.85), joint="curve")

    # Downsample with Lanczos to get pixel-perfect anti-aliased result
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

if __name__ == "__main__":
    logo_512 = create_aura_logo(512)
    logo_512.save("aura-assets/aura-logo.png", "PNG")
    
    # Save Windows ICO with all standard icon sizes
    sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icon_images = [create_aura_logo(s[0]) for s in sizes]
    icon_images[0].save("aura-assets/aura-icon.ico", format="ICO", sizes=sizes, append_images=icon_images[1:])
    print("Created aura-logo.png and aura-icon.ico with true transparency!")
