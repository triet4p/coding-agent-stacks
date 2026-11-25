#!/usr/bin/env python3
"""Structure and geometry gate for a PPTX deck.

Usage:
    python check_deck.py deck.pptx
    python check_deck.py deck.pptx --expect 36 --json

Hard failures (exit 1): slide count mismatch, shapes outside the slide,
learner-facing text crossing the decision band or the footer rule.
Warnings (exit 0): text below the profile floor, slides over the character
budget, shapes whose estimated text height exceeds their box (rank, don't trust).
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

from pptx import Presentation

EMU = 914400.0
TOLERANCE = 9000
DECISION_TOP, DECISION_BOTTOM = 6.02, 6.58
FOOTER_RULE = 6.98
MIN_LEARNER_PT = 13.0
MAX_CHARS = 700
MONO = {"Consolas", "Cascadia Code", "Courier New"}
_TITLE_FONT = "C:/Windows/Fonts/arial.ttf"


def iter_shapes(container):
    for sh in container.shapes:
        yield sh
        if sh.shape_type == 6:  # GROUP
            yield from iter_shapes(sh)


def text_of(sh):
    if not getattr(sh, "has_text_frame", False) or not sh.has_text_frame:
        return ""
    return sh.text_frame.text.strip()


def is_code(sh):
    if not getattr(sh, "has_text_frame", False) or not sh.has_text_frame:
        return False
    names = {r.font.name for p in sh.text_frame.paragraphs for r in p.runs if r.font.name}
    return bool(names) and names <= MONO


def box(sh):
    if sh.left is None or sh.top is None or sh.width is None or sh.height is None:
        return None
    return (sh.left / EMU, sh.top / EMU, sh.width / EMU, sh.height / EMU)


_FONTS = {}


def _font(pt):
    key = round(pt * 4)
    if key not in _FONTS:
        try:
            from PIL import ImageFont
            _FONTS[key] = ImageFont.truetype(_TITLE_FONT, max(8, int(round(pt * 96 / 72))))
        except Exception:
            _FONTS[key] = None
    return _FONTS[key]


def _line_count(txt, pt, width_in):
    font = _font(pt)
    if font is None:
        approx = len(txt) * pt * 0.5 / 72.0
        return max(1, math.ceil(approx / max(width_in, 0.1)))
    words = txt.split(" ")
    lines, acc = 1, 0.0
    for word in words:
        w = font.getlength(word + " ") / 96.0
        if acc + w > width_in and acc > 0:
            lines += 1
            acc = w
        else:
            acc += w
    return lines


def estimated_height(sh, width_in):
    total = 0.0
    for p in sh.text_frame.paragraphs:
        runs = [r for r in p.runs if r.text]
        if not runs:
            continue
        txt = "".join(r.text for r in runs)
        pt = max([r.font.size.pt for r in runs if r.font.size] or [18.0])
        total += _line_count(txt, pt, width_in) * pt * 1.22 / 72.0
    return total


def has_decision_strip(sl) -> bool:
    """A decision strip is a full-width panel sitting at 6.02 in."""
    for sh in iter_shapes(sl):
        b = box(sh)
        if not b:
            continue
        _, y, w, h = b
        if 5.98 <= y <= 6.06 and w >= 11.0 and 0.50 <= h <= 0.70:
            return True
    return False


def audit(path: Path, expect=None, min_pt=MIN_LEARNER_PT):
    prs = Presentation(str(path))
    sw, sh_ = prs.slide_width, prs.slide_height
    failures, warnings, slides = [], [], []
    for idx, sl in enumerate(prs.slides, 1):
        info = {"slide": idx, "chars": 0, "issues": []}
        decision = has_decision_strip(sl)
        for sh in iter_shapes(sl):
            b = box(sh)
            if b is None:
                continue
            x, y, w, h = b
            if x < 0 or y < 0 or sh.left + sh.width > sw + TOLERANCE or sh.top + sh.height > sh_ + TOLERANCE:
                failures.append(f"s{idx:02d}: shape outside slide ({x:.2f},{y:.2f},{w:.2f},{h:.2f})")
            txt = text_of(sh)
            if not txt:
                continue
            info["chars"] += len(txt)
            is_footer = y >= 6.90
            # Judge the text, not the (often generous) text box.
            need = h if is_code(sh) else estimated_height(sh, max(w - 0.08, 0.2))
            bottom = y + min(h, max(need, 0.10))
            if decision and not is_footer and y < DECISION_TOP - 0.05 and bottom > DECISION_TOP + 0.02:
                failures.append(f"s{idx:02d}: text enters decision band: {txt[:40]!r}")
            if not is_footer and y < FOOTER_RULE - 0.05 and bottom > FOOTER_RULE + 0.02:
                failures.append(f"s{idx:02d}: text crosses footer rule: {txt[:40]!r}")
            if not is_footer:
                sizes = [r.font.size.pt for p in sh.text_frame.paragraphs for r in p.runs if r.font.size]
                # Labels, eyebrows, badges, and code titles are intentionally small.
                label_like = (txt.upper() == txt or sh.shape_type == 9
                              or (h <= 0.50 and len(txt) <= 40))
                if sizes and min(sizes) < min_pt and not label_like:
                    warnings.append(f"s{idx:02d}: {min(sizes):.1f} pt < {min_pt:g} pt: {txt[:40]!r}")
                if not is_code(sh) and h >= 0.30 and w >= 0.60 and len(txt) > 3:
                    need = estimated_height(sh, w - 0.08)
                    if need > h * 1.25:
                        info["issues"].append(f"text ~{need:.2f} in in {h:.2f} in box: {txt[:40]!r}")
        if info["chars"] > MAX_CHARS:
            warnings.append(f"s{idx:02d}: {info['chars']} displayed chars > {MAX_CHARS}")
        if info["issues"]:
            slides.append(info)
    if expect is not None and len(prs.slides) != expect:
        failures.append(f"slide count {len(prs.slides)} != expected {expect}")
    return {
        "file": str(path),
        "slides": len(prs.slides),
        "failures": failures,
        "warnings": warnings,
        "overflow_candidates": slides,
    }


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Structure and geometry gate for a PPTX deck.")
    ap.add_argument("deck", type=Path)
    ap.add_argument("--expect", type=int, default=None, help="expected slide count")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--min-pt", type=float, default=MIN_LEARNER_PT,
                    help="warn below this size (labels, badges, footers are exempt)")
    args = ap.parse_args()
    if not args.deck.exists():
        print(f"missing file: {args.deck}", file=sys.stderr)
        return 2
    r = audit(args.deck, args.expect, args.min_pt)
    try:
        _emit(r, args.json)
    except BrokenPipeError:
        return 0
    return 1 if r["failures"] else 0


def _emit(r, as_json):
    if as_json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"{r['file']}  slides={r['slides']}")
        for f in r["failures"]:
            print(f"  FAIL  {f}")
        for w in r["warnings"][:10]:
            print(f"  warn  {w}")
        if len(r["warnings"]) > 10:
            print(f"  warn  … {len(r['warnings']) - 10} more small-text warnings (use --min-pt to adjust)")
        if r["overflow_candidates"]:
            print("  overflow candidates (review by eye, do not trust):")
            for s in r["overflow_candidates"]:
                for issue in s["issues"]:
                    print(f"    s{s['slide']:02d}  {issue}")
        if not r["failures"]:
            print("  OK  structure and geometry")


if __name__ == "__main__":
    raise SystemExit(main())
