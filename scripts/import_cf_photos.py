#!/usr/bin/env python3
"""Import allowed Crystal Flow photos into images/kew/, max long side 1600px JPEG."""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

from PIL import Image

ZIP_PATH = Path(
    "/home/ubuntu/.cursor/projects/workspace/uploads/crystalflow_photos_0800.zip"
)
OUT_DIR = Path("/workspace/images/kew")
MAX_LONG = 1600
QUALITY = 88

# source path in zip -> destination filename under images/kew/
IMPORT_MAP: dict[str, str] = {
    "hero-pipelines.jpg": "hero-pipeline-primary.jpg",
    "pipeline-erection.jpg": "hero-pipeline-erection.jpg",
    "lab-stations.jpg": "lab-stations-quality.jpg",
    "meltshop-station.jpg": "vertical-station-meltshop.jpg",
    "gallery/01.jpg": "gallery-station-01.jpg",
    "gallery/02.jpg": "gallery-pipework-02.jpg",
    "gallery/03.jpg": "gallery-ducting-03.jpg",
    "gallery/04.jpg": "gallery-site-04.jpg",
    "gallery/05.jpg": "gallery-fabrication-05.jpg",
    "gallery/06.jpg": "gallery-carriers-06.jpg",
    "gallery/07.jpg": "gallery-pipeline-07.jpg",
    "gallery/08.jpg": "gallery-install-08.jpg",
    "gallery/09.jpg": "gallery-equipment-09.jpg",
}


def optimize_jpeg(src: Path, dest: Path) -> None:
    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        long_side = max(w, h)
        if long_side > MAX_LONG:
            scale = MAX_LONG / long_side
            im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, "JPEG", quality=QUALITY, optimize=True)


def main() -> None:
    if not ZIP_PATH.is_file():
        raise SystemExit(f"zip not found: {ZIP_PATH}")
    with zipfile.ZipFile(ZIP_PATH) as zf:
        names = set(zf.namelist())
        for src_name, dest_name in IMPORT_MAP.items():
            if src_name not in names:
                raise SystemExit(f"missing in zip: {src_name}")
            tmp = Path("/tmp") / f"cf-import-{dest_name}"
            with zf.open(src_name) as zsrc, tmp.open("wb") as out:
                shutil.copyfileobj(zsrc, out)
            optimize_jpeg(tmp, OUT_DIR / dest_name)
            print(f"wrote {OUT_DIR / dest_name}")


if __name__ == "__main__":
    main()