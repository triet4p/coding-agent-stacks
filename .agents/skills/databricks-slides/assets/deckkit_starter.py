# -*- coding: utf-8 -*-
"""Databricks-style slide primitives — dependency-light starter.

Copy this file into a project as `deckkit.py` and import from every build script.
It encodes the tokens and geometry from `references/layout-spec.md` so a deck
cannot drift into deck-local colors or type sizes.

Requires: python-pptx. Pillow is optional (title measurement, image aspect).

    from deckkit import *
    set_profile("training-dense")
    prs = new_deck()
    sl = blank(prs)
    header(sl, "Title", "One line of scope", eyebrow="MODULE 03 · DELTA LAKE")
    ...
    footer(sl, "MODULE 03 · DELTA LAKE & UNITY CATALOG", 7, 32)
"""
from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# ---------------------------------------------------------------- palette
INK = RGBColor(0x0B, 0x1F, 0x24)
RED = RGBColor(0xFF, 0x36, 0x21)
BG = RGBColor(0xF7, 0xF8, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BORDER = RGBColor(0xD7, 0xDD, 0xE3)
MUTED = RGBColor(0x5B, 0x66, 0x70)
INFO = RGBColor(0x2F, 0x6B, 0xFF)
SUCCESS = RGBColor(0x1A, 0x9B, 0x62)
CAUTION = RGBColor(0xF3, 0xB3, 0x3D)
AI = RGBColor(0x7B, 0x61, 0xFF)
DANGER_SOFT = RGBColor(0xE0, 0x56, 0x38)

TINTS = {
    "red": RGBColor(0xFD, 0xE9, 0xE6),
    "info": RGBColor(0xE8, 0xEF, 0xFF),
    "success": RGBColor(0xE6, 0xF5, 0xEE),
    "caution": RGBColor(0xFD, 0xF3, 0xDF),
    "ai": RGBColor(0xEE, 0xEA, 0xFF),
    "ink": RGBColor(0xEC, 0xEF, 0xF1),
    "muted": RGBColor(0xEE, 0xF1, 0xF3),
}
COLOR_NAME = {INK: "ink", MUTED: "muted", RED: "red", WHITE: "white",
              SUCCESS: "success", CAUTION: "caution", AI: "ai", INFO: "info"}

# ---------------------------------------------------------------- profiles
_PROFILES = {
    "training-dense": dict(title=30, title_min=25, subtitle=17, body=18,
                           card_title=16.5, card_body=16, caption=13, label=11,
                           footer=10, code=13.5),
    "lecture-sparse": dict(title=32, title_min=28, subtitle=20, body=24,
                           card_title=20, card_body=20, caption=16, label=12,
                           footer=10, code=15),
}
_active = "training-dense"


def set_profile(name: str) -> None:
    """Select one density profile for the whole deck. Call once, at the top."""
    global _active, TITLE, TITLE_MIN, SUBTITLE, BODY, CARD_TITLE, CARD_BODY, CAPTION, LABEL, FOOTER_PT, CODE
    if name not in _PROFILES:
        raise ValueError(f"unknown profile {name!r}; use one of {sorted(_PROFILES)}")
    p = _PROFILES[name]
    _active = name
    TITLE, TITLE_MIN, SUBTITLE, BODY = p["title"], p["title_min"], p["subtitle"], p["body"]
    CARD_TITLE, CARD_BODY, CAPTION, LABEL = p["card_title"], p["card_body"], p["caption"], p["label"]
    FOOTER_PT, CODE = p["footer"], p["code"]


def profile() -> str:
    return _active


set_profile(_active)

FONT = "Arial"
MONO = "Consolas"

# ---------------------------------------------------------------- geometry
SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN = 0.70
CONTENT_W = SLIDE_W - 2 * MARGIN
BODY_TOP, BODY_BOTTOM = 2.02, 6.72
DECISION_TOP, DECISION_BOTTOM = 6.02, 6.58
FOOTER_Y = 6.98
R_CARD, R_NODE, R_FRAME = 0.10, 0.05, 0.03
CALLOUT_CAP = 1.60


def new_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    return prs


def blank(prs: Presentation):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    fill = sl.background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    return sl


def content_area(decision: bool = False):
    """(y, h) available for content, accounting for the decision strip."""
    return BODY_TOP, BODY_BOTTOM - BODY_TOP - (0.70 if decision else 0.0)


# ---------------------------------------------------------------- primitives
def _tf(shape):
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def _flat(shp):
    """Remove theme style so PowerPoint does not add an inherited shadow."""
    from pptx.oxml.ns import qn
    el = shp._element
    style = el.find(qn("p:style"))
    if style is not None:
        el.remove(style)
    shp.shadow.inherit = False
    return shp


def text(sl, x, y, w, h, value, size=None, color=INK, bold=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=FONT, line=1.05):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = _tf(tb)
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line
    r = p.add_run()
    r.text = value
    r.font.name = font
    r.font.size = Pt(size if size is not None else BODY)
    r.font.bold = bold
    r.font.color.rgb = color
    return tb


def panel(sl, x, y, w, h, fill=WHITE, border=BORDER, radius=R_CARD, line_w=0.75):
    shp = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.adjustments[0] = min(0.5, radius / max(0.01, min(w, h)))
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if border is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = border
        shp.line.width = Pt(line_w)
    return _flat(shp)


def rect(sl, x, y, w, h, fill, line=None):
    shp = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    return _flat(shp)


def bullets(tf, items, size=None, color=INK, marker=RED, space=6):
    size = size if size is not None else CARD_BODY
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.03
        p.space_after = Pt(space)
        m = p.add_run()
        m.text = "•  "
        m.font.name = FONT
        m.font.size = Pt(size)
        m.font.bold = True
        m.font.color.rgb = marker
        r = p.add_run()
        r.text = item
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.color.rgb = color


def chip(sl, x, y, w, h, label, accent=INK, size=None):
    fill = TINTS.get(COLOR_NAME.get(accent, "ink"), TINTS["ink"])
    panel(sl, x, y, w, h, fill=fill, border=fill, radius=h / 2)
    text(sl, x + 0.14, y + (h - 0.24) / 2, w - 0.24, 0.24, label,
         size=size if size is not None else LABEL + 1, color=INK, bold=True)


def badge(sl, x, y, n, d=0.30, color=RED):
    shp = sl.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    _flat(shp)
    tf = _tf(shp)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(n)
    r.font.name = FONT
    r.font.size = Pt(max(10, d * 34))
    r.font.bold = True
    r.font.color.rgb = WHITE
    return shp


def arrow(sl, x, y, length, color=BORDER, direction="right", thickness=0.055):
    shape = {"right": MSO_SHAPE.RIGHT_ARROW, "down": MSO_SHAPE.DOWN_ARROW,
             "left": MSO_SHAPE.LEFT_ARROW, "up": MSO_SHAPE.UP_ARROW}[direction]
    if direction in ("down", "up"):
        shp = sl.shapes.add_shape(shape, Inches(x), Inches(y), Inches(thickness * 3.2), Inches(length))
    else:
        shp = sl.shapes.add_shape(shape, Inches(x), Inches(y), Inches(length), Inches(thickness * 3.2))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    return _flat(shp)


def connector(sl, x1, y1, x2, y2, color=BORDER, width=1.25, dashed=False):
    from pptx.enum.shapes import MSO_CONNECTOR
    cn = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    cn.line.color.rgb = color
    cn.line.width = Pt(width)
    if dashed:
        from pptx.enum.dml import MSO_LINE_DASH_STYLE
        cn.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    return _flat(cn)


# ---------------------------------------------------------------- header / footer
_TITLE_FONT = "C:/Windows/Fonts/arialbd.ttf"


def _text_width(value: str, pt: float) -> float:
    try:
        from PIL import ImageFont
        f = ImageFont.truetype(_TITLE_FONT, int(round(pt * 96 / 72)))
        return f.getlength(value) / 96.0
    except Exception:
        return len(value) * pt * 0.55 / 72.0


def header(sl, title, subtitle=None, eyebrow=None):
    """Eyebrow + red rule + title (+ subtitle). Returns the body top.

    Long titles shrink to TITLE_MIN before wrapping; a wrapped title pushes the
    subtitle down so the two never share a band.
    """
    y = 0.30
    if eyebrow:
        rect(sl, MARGIN - 0.02, y + 0.05, 0.055, 0.20, RED)
        text(sl, MARGIN + 0.12, y, 9.6, 0.28, eyebrow.upper(),
             size=FOOTER_PT + 0.5, color=MUTED, bold=True)

    ty = 0.66
    size, lines = TITLE, 1
    if _text_width(title, size) > CONTENT_W - 0.10:
        for s in range(TITLE - 1, TITLE_MIN - 1, -1):
            if _text_width(title, s) <= CONTENT_W - 0.10:
                size = s
                break
        else:
            size, lines = TITLE_MIN, 2

    title_h = 0.90 if lines == 1 else 0.86
    rect(sl, MARGIN - 0.20, ty + 0.06, 0.075, 0.52 if lines == 1 else 0.78, RED)
    text(sl, MARGIN, ty, CONTENT_W, title_h, title, size=size, color=INK, bold=True, line=0.98)

    if subtitle:
        text(sl, MARGIN, 1.52 if lines == 1 else 1.56, CONTENT_W, 0.42, subtitle,
             size=SUBTITLE, color=MUTED, line=1.0)
        return BODY_TOP
    return 1.78


def footer(sl, module_label, page, total):
    rect(sl, MARGIN, FOOTER_Y, CONTENT_W, 0.012, BORDER)
    text(sl, MARGIN, FOOTER_Y + 0.10, 8.6, 0.24, module_label.upper(), size=FOOTER_PT, color=MUTED)
    text(sl, SLIDE_W - MARGIN - 1.2, FOOTER_Y + 0.10, 1.2, 0.24, f"{page:02d} / {total:02d}",
         size=FOOTER_PT, color=MUTED, align=PP_ALIGN.RIGHT)


def key_decision(sl, value, label="Key decision", y=DECISION_TOP):
    """Decision strip. Prefixes PRODUCT STATUS / LIMITATION / CAUTION change the accent."""
    accent = RED
    for pfx in ("PRODUCT STATUS:", "LIMITATION:", "CAUTION:", "KEY DECISION:"):
        if value.upper().startswith(pfx):
            label = pfx[:-1].strip()
            value = value[len(pfx):].strip()
            accent = {"PRODUCT STATUS:": INFO, "CAUTION:": CAUTION, "LIMITATION:": DANGER_SOFT}.get(pfx, RED)
            break
    panel(sl, MARGIN, y, CONTENT_W, 0.56, fill=RGBColor(0xF2, 0xF4, 0xF6), border=BORDER, radius=0.06)
    rect(sl, MARGIN, y + 0.08, 0.05, 0.40, accent)
    lbl_w = 1.95 if len(label) > 12 else 1.65
    text(sl, MARGIN + 0.18, y + 0.16, lbl_w, 0.24, label.upper(), size=LABEL - 0.5, color=accent, bold=True)
    text(sl, MARGIN + lbl_w + 0.20, y + 0.13, CONTENT_W - (lbl_w + 0.35), 0.32, value,
         size=CAPTION + 1, color=INK)


# ---------------------------------------------------------------- media
def image_fit(sl, path, x, y, w, h, border=BORDER, frame=True, align="center"):
    """Place an image inside a box, preserving aspect. Returns (pic, (fx, fy, fw, fh)).

    Badge coordinates must be computed from this fitted rect, never from the box.
    """
    path = Path(path)
    try:
        from PIL import Image
        im = Image.open(path)
        aspect = im.width / im.height
    except Exception:
        aspect = w / h
    if aspect > w / h:
        fw = w
        fh = fw / aspect
    else:
        fh = h
        fw = fh * aspect
    fx = x + (w - fw) / 2
    fy = y + (h - fh) / 2 if align == "center" else y
    if frame:
        panel(sl, x - 0.04, y - 0.04, w + 0.08, h + 0.08, fill=WHITE, border=border, radius=R_FRAME)
    pic = sl.shapes.add_picture(str(path), Inches(fx), Inches(fy), Inches(fw), Inches(fh))
    return pic, (fx, fy, fw, fh)


def code_block(sl, x, y, w, h, lines, title=None, numbered=True, size=None):
    size = size if size is not None else CODE
    panel(sl, x, y, w, h, fill=INK, border=INK, radius=0.06)
    ty = y + 0.16
    if title:
        text(sl, x + 0.22, ty, w - 0.44, 0.24, title.upper(), size=LABEL - 1,
             color=RGBColor(0x9A, 0xA8, 0xB2), bold=True)
        ty += 0.30
    tb = sl.shapes.add_textbox(Inches(x + 0.22), Inches(ty), Inches(w - 0.44), Inches(h - (ty - y) - 0.12))
    tf = _tf(tb)
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.0
        p.space_after = Pt(2)
        if numbered:
            n = p.add_run()
            n.text = f"{i + 1:>2}  "
            n.font.name = MONO
            n.font.size = Pt(size)
            n.font.color.rgb = RGBColor(0x5F, 0x70, 0x7A)
        r = p.add_run()
        r.text = line
        r.font.name = MONO
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0x8F, 0xA3, 0xAD) if line.strip().startswith("#") else RGBColor(0xE9, 0xEE, 0xF1)


# ---------------------------------------------------------------- notes
def notes(sl, body, sources=None, extra=None):
    """Speaker notes contract: detail + sources with status and check date."""
    tf = sl.notes_slide.notes_text_frame
    tf.clear()
    tf.paragraphs[0].text = body
    if extra:
        h = tf.add_paragraph()
        h.text = "\n[ADDITIONAL DETAIL]"
        h.font.bold = True
        for line in extra:
            tf.add_paragraph().text = f"• {line}"
    if sources:
        h = tf.add_paragraph()
        h.text = "\n[SOURCES]"
        h.font.bold = True
        for title, status, date, url in sources:
            tf.add_paragraph().text = f"• {title} ({status}, checked {date}): {url}"
