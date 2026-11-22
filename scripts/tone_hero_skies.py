#!/usr/bin/env python3
"""Shift purple-tinted skies toward natural blue-grey in hero photos."""

from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1] / "images" / "kew"

SOURCES = [
    ("hero-pipeline-truss.jpg", "hero-pipeline-truss-toned.jpg"),
    ("hero-pipeline-sky.jpg", "hero-pipeline-sky-toned.jpg"),
]


def tone_sky(img: Image.Image) -> Image.Image:
    rgb = img.convert("RGB")
    r, g, b = rgb.split()
    # Reduce magenta in highlights; modest cool bias in upper band
    g = g.point(lambda x: min(255, int(x * 1.02 + 4)))
    b = b.point(lambda x: min(255, int(x * 1.04 + 2)))
    r = r.point(lambda x: max(0, int(x * 0.97 - 3)))
    out = Image.merge("RGB", (r, g, b))
    out = ImageEnhance.Color(out).enhance(0.92)
    out = ImageEnhance.Contrast(out).enhance(1.03)
    return out


def main() -> None:
    for src, dest in SOURCES:
        path = ROOT / src
        out_path = ROOT / dest
        if not path.exists():
            raise SystemExit(f"Missing {path}")
        tone_sky(Image.open(path)).save(out_path, quality=88, optimize=True)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()