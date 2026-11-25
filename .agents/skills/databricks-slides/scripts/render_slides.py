#!/usr/bin/env python3
"""Render PPTX pages to PNG for slide-by-slide review.

Usage:
    python render_slides.py deck.pptx --out renders/
    python render_slides.py deck.pptx --dpi 110 --pages 1-5,12
    python render_slides.py deck.pptx --pages all --keep-pdf

Uses LibreOffice for PDF conversion and poppler's pdftoppm for rasterizing.
LibreOffice rendering is an iteration aid, not proof that PowerPoint renders
the same; open the deck in real PowerPoint before delivery.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SOFFICE_CANDIDATES = [
    os.environ.get("SOFFICE", ""),
    shutil.which("soffice") or "",
    r"C:/Program Files/LibreOffice/program/soffice.exe",
    r"C:/Program Files (x86)/LibreOffice/program/soffice.exe",
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    "/usr/bin/soffice",
    "/usr/local/bin/soffice",
]

PDFTOPPM_CANDIDATES = [
    os.environ.get("PDFTOPPM", ""),
    shutil.which("pdftoppm") or "",
    r"C:/Program Files/MiKTeX/miktex/bin/x64/pdftoppm.exe",
    "/usr/bin/pdftoppm",
    "/usr/local/bin/pdftoppm",
]


def find(candidates, what):
    for c in candidates:
        if c and Path(c).exists():
            return c
    raise SystemExit(f"{what} not found. Install it or set the environment variable.")


def parse_pages(spec, total):
    if not spec or spec == "all":
        return list(range(1, total + 1))
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            pages.extend(range(int(a), int(b) + 1))
        elif part:
            pages.append(int(part))
    return [p for p in pages if 1 <= p <= total]


def main() -> int:
    ap = argparse.ArgumentParser(description="Render PPTX pages to PNG.")
    ap.add_argument("deck", type=Path)
    ap.add_argument("--out", type=Path, default=Path("renders"))
    ap.add_argument("--dpi", type=int, default=100)
    ap.add_argument("--pages", default="all", help='e.g. "1-5,12" or "all"')
    ap.add_argument("--keep-pdf", action="store_true")
    args = ap.parse_args()

    if not args.deck.exists():
        print(f"missing file: {args.deck}", file=sys.stderr)
        return 2
    soffice = find(SOFFICE_CANDIDATES, "LibreOffice (soffice)")
    pdftoppm = find(PDFTOPPM_CANDIDATES, "pdftoppm (poppler)")

    args.out.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="render-"))
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", str(args.deck), "--outdir", str(tmp)],
                   check=True, capture_output=True, timeout=900)
    pdf = tmp / (args.deck.stem + ".pdf")
    if not pdf.exists():
        raise SystemExit("conversion produced no PDF")

    from pptx import Presentation
    total = len(Presentation(str(args.deck)).slides)
    pages = parse_pages(args.pages, total)
    made = []
    for n in pages:
        prefix = tmp / f"p{n:03d}"
        subprocess.run([pdftoppm, "-png", "-r", str(args.dpi), "-f", str(n), "-l", str(n),
                        str(pdf), str(prefix)], check=True, capture_output=True, timeout=300)
        got = sorted(tmp.glob(f"p{n:03d}*.png"))
        if not got:
            print(f"  page {n}: no output", file=sys.stderr)
            continue
        dst = args.out / f"{args.deck.stem}-p{n:02d}.png"
        shutil.copyfile(got[0], dst)
        made.append(dst)
        got[0].unlink()

    if args.keep_pdf:
        shutil.copyfile(pdf, args.out / pdf.name)
    shutil.rmtree(tmp, ignore_errors=True)

    print(f"rendered {len(made)}/{len(pages)} pages at {args.dpi} dpi -> {args.out}")
    for p in made:
        print(f"  {p}")
    return 0 if len(made) == len(pages) else 1


if __name__ == "__main__":
    raise SystemExit(main())
