#!/usr/bin/env python3
"""Printable "review us on Google" QR code for the front desk.

    python3 tools/build_review_card.py

Writes _dev/print/review-qr/: review-qr.pdf (page 1 a letter-size sign, page 2
four quarter-page cards with cut lines), plus review-qr.svg and review-qr.png
for anything else (email, a frame, the exam rooms).

The code points at legacymedicalpalmbeach.com/review, which build.py redirects
to Google's write-a-review form for the practice (GOOGLE["review_url"] in
content.py). Printed copies keep working if that link ever has to change:
update content.py, not the paper. Needs reportlab, Pillow and fontTools
(with brotli for the woff2 fonts); build.py does not.
"""
import io
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image, ImageDraw
from reportlab.graphics.barcode import qr
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLFont
from reportlab.pdfgen import canvas

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
import build as B  # noqa: E402

FONTS = os.path.join(ROOT, "public", "assets", "fonts")
MARK = os.path.join(ROOT, "_dev", "source-images", "legacy-mark.png")
OUT = os.path.join(ROOT, "_dev", "print", "review-qr")
URL = B.BASE + "/review"
URL_SHOWN = URL.split("//", 1)[1]
P = B.PRACTICE

# Printed on white paper: black text, gold kept to the frame and small type. The site's
# --gold is too light for text on white, so text uses a deeper gold.
INK = HexColor("#0E0D0B")
MUTED = HexColor("#5C574F")
GOLD = HexColor("#C9A35B")
GOLD_TEXT = HexColor("#8A6A2C")


def register(name, file, wght):
    f = TTFont(os.path.join(FONTS, file))
    f = instancer.instantiateVariableFont(f, {"wght": wght})
    f.flavor = None
    buf = io.BytesIO()
    f.save(buf)
    buf.seek(0)
    pdfmetrics.registerFont(RLFont(name, buf))


register("Serif", "legacy-display-v1.woff2", 400)
register("Sans", "legacy-sans-v1.woff2", 400)
register("SansMed", "legacy-sans-v1.woff2", 550)
register("SansBold", "legacy-sans-v1.woff2", 700)


def matrix(data):
    q = qr.QrCodeWidget(data, barLevel="Q").qr
    q.make()
    n = q.getModuleCount()
    return [[q.isDark(r, c) for c in range(n)] for r in range(n)]


QR = matrix(URL)
N = len(QR)
QUIET = 4  # modules of white margin the QR spec asks for


def draw_qr(c, x, y, size):
    """QR with its quiet zone, `size` points square, lower-left at x, y."""
    m = size / (N + 2 * QUIET)
    c.setFillColor(white)
    c.rect(x, y, size, size, stroke=0, fill=1)
    c.setFillColor(INK)
    for r, row in enumerate(QR):
        run = None
        for col, dark in enumerate(row + [False]):
            if dark and run is None:
                run = col
            elif not dark and run is not None:
                c.rect(x + (QUIET + run) * m, y + size - (QUIET + r + 1) * m, (col - run) * m, m, stroke=0, fill=1)
                run = None


def spaced(c, text, x, y, font, size, track, color, anchor="centre"):
    c.saveState()  # character spacing would otherwise stick to every later string
    c.setFont(font, size)
    c.setFillColor(color)
    w = pdfmetrics.stringWidth(text, font, size) + track * (len(text) - 1)
    sx = x - w / 2 if anchor == "centre" else x
    t = c.beginText(sx, y)
    t.setFont(font, size)
    t.setCharSpace(track)
    t.textOut(text)
    c.drawText(t)
    c.restoreState()


def wrap(text, font, size, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if pdfmetrics.stringWidth(trial, font, size) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    return lines + [line]


def centred_lines(c, lines, cx, y, font, size, lead, color):
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in lines:
        c.drawCentredString(cx, y, ln)
        y -= lead
    return y


def lockup(c, cx, top, mark_w):
    """Gold mark over the LEGACY / MEDICAL wordmark, centred on cx. Returns the y under it."""
    img = ImageReader(MARK)
    iw, ih = img.getSize()
    mh = mark_w * ih / iw
    c.drawImage(img, cx - mark_w / 2, top - mh, mark_w, mh, mask="auto")
    y = top - mh - mark_w * 0.2
    spaced(c, "LEGACY", cx, y, "SansBold", mark_w * 0.17, mark_w * 0.03, INK)
    y -= mark_w * 0.13
    spaced(c, "MEDICAL", cx, y, "SansMed", mark_w * 0.075, mark_w * 0.045, MUTED)
    return y


def panel(c, x, y, w, h, s):
    """One complete sign in the box x, y, w, h; s scales type and spacing."""
    cx = x + w / 2
    pad = 0.42 * inch * s
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.4 * s)
    c.roundRect(x + pad, y + pad, w - 2 * pad, h - 2 * pad, 10 * s, stroke=1, fill=0)
    c.setLineWidth(0.5 * s)
    c.roundRect(x + pad + 5 * s, y + pad + 5 * s, w - 2 * pad - 10 * s, h - 2 * pad - 10 * s, 7 * s, stroke=1, fill=0)

    yy = lockup(c, cx, y + h - pad - 0.42 * inch * s, 1.5 * inch * s)
    yy -= 0.5 * inch * s
    spaced(c, "PATIENT REVIEWS", cx, yy, "SansBold", 10.5 * s, 2.4 * s, GOLD_TEXT)
    yy -= 44 * s
    c.setFont("Serif", 38 * s)
    c.setFillColor(INK)
    c.drawCentredString(cx, yy, "How was your visit?")
    yy -= 30 * s
    lede = "Scan with your phone's camera to leave a review of Legacy Medical on Google."
    yy = centred_lines(c, wrap(lede, "Sans", 15 * s, 4.6 * inch * s), cx, yy, "Sans", 15 * s, 21 * s, MUTED)

    q = 3.5 * inch * s
    qy = yy - 6 * s - q
    c.setStrokeColor(GOLD)
    c.setLineWidth(1 * s)
    c.roundRect(cx - q / 2 - 6 * s, qy - 6 * s, q + 12 * s, q + 12 * s, 9 * s, stroke=1, fill=0)
    draw_qr(c, cx - q / 2, qy, q)

    yy = qy - 34 * s
    c.setFont("Sans", 11 * s)
    c.setFillColor(MUTED)
    c.drawCentredString(cx, yy, "or visit")
    yy -= 17 * s
    c.setFont("SansMed", 14 * s)
    c.setFillColor(INK)
    c.drawCentredString(cx, yy, URL_SHOWN)

    fy = y + pad + 0.5 * inch * s
    c.setFont("Serif", 13 * s)
    c.setFillColor(INK)
    c.drawCentredString(cx, fy + 20 * s, "Thank you for choosing Legacy Medical.")
    c.setFont("Sans", 9.5 * s)
    c.setFillColor(MUTED)
    c.drawCentredString(cx, fy, "%s, %s, %s %s  ·  %s" % (P["street_short"], P["city"], P["region"], P["postal"], P["phone"]))


def card(c, x, y, w, h):
    """Quarter-page handout: lockup, one line of ask, the code, the short link."""
    cx = x + w / 2
    pad = 0.22 * inch
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.roundRect(x + pad, y + pad, w - 2 * pad, h - 2 * pad, 7, stroke=1, fill=0)
    yy = lockup(c, cx, y + h - pad - 0.26 * inch, 0.78 * inch)
    yy -= 0.36 * inch
    c.setFont("Serif", 21)
    c.setFillColor(INK)
    c.drawCentredString(cx, yy, "How was your visit?")
    yy -= 17
    yy = centred_lines(c, ["Scan to leave a review", "of Legacy Medical on Google."], cx, yy, "Sans", 10.5, 14, MUTED)
    q = 2.6 * inch
    qy = yy - 4 - q
    draw_qr(c, cx - q / 2, qy, q)
    c.setFont("SansMed", 10)
    c.setFillColor(INK)
    c.drawCentredString(cx, qy - 12, URL_SHOWN)


def pdf(path):
    W, H = letter
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle("Legacy Medical: review us on Google")
    c.setAuthor(P["name"])
    c.setSubject("QR code to " + URL)
    panel(c, 0, 0, W, H, 1)
    c.showPage()
    w, h = W / 2, H / 2
    for i in range(2):
        for j in range(2):
            card(c, i * w, j * h, w, h)
    c.setStrokeColor(HexColor("#B9B3A8"))
    c.setLineWidth(0.5)
    c.setDash(3, 3)
    c.line(w, 0, w, H)
    c.line(0, h, W, h)
    c.setDash()
    c.setFont("Sans", 7)
    c.setFillColor(HexColor("#9C968B"))
    c.drawString(8, h + 4, "cut")
    c.showPage()
    c.save()


def svg(path, px=10):
    full = N + 2 * QUIET
    rects = "".join('<rect x="%d" y="%d" width="1" height="1"/>' % (QUIET + col, QUIET + r)
                    for r, row in enumerate(QR) for col, dark in enumerate(row) if dark)
    with open(path, "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" shape-rendering="crispEdges">'
                '<title>Review Legacy Medical on Google: %s</title><rect width="100%%" height="100%%" fill="#fff"/>'
                '<g fill="#0E0D0B">%s</g></svg>\n' % (full, full, full * px, full * px, URL, rects))


def png(path, px=24):
    full = N + 2 * QUIET
    im = Image.new("RGB", (full * px, full * px), "white")
    d = ImageDraw.Draw(im)
    for r, row in enumerate(QR):
        for col, dark in enumerate(row):
            if dark:
                x, y = (QUIET + col) * px, (QUIET + r) * px
                d.rectangle([x, y, x + px - 1, y + px - 1], fill=(14, 13, 11))
    im.save(path, optimize=True)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    pdf(os.path.join(OUT, "review-qr.pdf"))
    svg(os.path.join(OUT, "review-qr.svg"))
    png(os.path.join(OUT, "review-qr.png"))
    print("QR -> %s (version %d, %dx%d modules)" % (URL, (N - 17) // 4, N, N))
    print("wrote", os.path.relpath(OUT, ROOT))
