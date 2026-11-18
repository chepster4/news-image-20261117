"""Entry program for news-image-20261117.

Writes the pre-rendered front-page image (entry.png, shipped beside
this file in the repository) to the output directory. No network, no
other input: the same bytes are written on every run.

Before copying, check the image is really there and really a PNG
(magic bytes 89 50 4E 47): a missing or corrupt file must fail loudly
instead of producing a broken entry.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG"


def main():
    if not SOURCE.is_file():
        raise SystemExit("entry.png is missing")
    if SOURCE.read_bytes()[:4] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG image")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")
    print(f"copied {SOURCE.stat().st_size} bytes to {out_dir / 'entry.png'}")


if __name__ == "__main__":
    main()
