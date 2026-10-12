#!/usr/bin/env python3
"""Logo files, favicons and Open Graph share cards.

    python3 tools/build_brand.py

The mark is the practice's own (gold infinity + ECG line), cropped from the
transparent logo on the old site. Share cards are 1200x630, set in the
site's own fonts, one per main page.
"""
import io
import os

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "_dev", "source-images")
PUB = os.path.join(ROOT, "public")
OG = os.path.join(PUB, "assets", "img", "og")
NIGHT = (14, 13, 11)
INK = (238, 234, 226)
GOLD = (212, 176, 114)
MUTED = (179, 173, 162)


def font(name, size):
    path = os.path.join(PUB, "assets", "fonts", name)
    f = TTFont(path)
    f.flavor = None
    buf = io.BytesIO()
    f.save(buf)
    buf.seek(0)
    ft = ImageFont.truetype(buf, size)
    return ft


def bold(name, size, wght=650):
    ft = font(name, size)
    try:
        ft.set_variation_by_axes([wght])
    except Exception:
        pass
    return ft


def mark(height):
    m = Image.open(os.path.join(SRC, "legacy-mark.png")).convert("RGBA")
    w = round(m.width * height / m.height)
    return m.resize((w, height), Image.LANCZOS)


def save_icons():
    os.makedirs(OG, exist_ok=True)
    # Header mark: 2x and 3x of a 40px-tall display.
    for h in (80, 120):
        mark(h).save(os.path.join(PUB, "assets", "img", "legacy-mark-%d.png" % h), optimize=True)
        mark(h).save(os.path.join(PUB, "assets", "img", "legacy-mark-%d.webp" % h), "WEBP", quality=90, method=6)
    def square(size, pad=0.16, bg=NIGHT):
        c = Image.new("RGBA", (size, size), bg + (255,))
        m = Image.open(os.path.join(SRC, "legacy-mark.png")).convert("RGBA")
        inner = int(size * (1 - 2 * pad))
        r = inner / max(m.size)
        m = m.resize((round(m.width * r), round(m.height * r)), Image.LANCZOS)
        c.alpha_composite(m, ((size - m.width) // 2, (size - m.height) // 2))
        return c
    square(180).convert("RGB").save(os.path.join(PUB, "apple-touch-icon.png"), optimize=True)
    square(192).save(os.path.join(OG, "logo-192.png"), optimize=True)
    square(512).save(os.path.join(OG, "logo-512.png"), optimize=True)
    ico = square(64, pad=0.06)
    ico.save(os.path.join(PUB, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    # SVG favicon: the mark as an embedded PNG on a dark rounded tile.
    import base64
    b = io.BytesIO()
    square(96, pad=0.08).save(b, "PNG", optimize=True)
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" rx="20" fill="#0E0D0B"/>'
           '<image href="data:image/png;base64,%s" width="96" height="96"/></svg>' % base64.b64encode(b.getvalue()).decode())
    open(os.path.join(PUB, "favicon.svg"), "w").write(svg)


def cover(img, w, h, focal=(0.5, 0.5)):
    r = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * r), round(img.height * r)), Image.LANCZOS)
    x = int((img.width - w) * focal[0])
    y = int((img.height - h) * focal[1])
    return img.crop((x, y, x + w, y + h))


def card(slug, title, kicker, photo=None, focal=(0.5, 0.3), bg_video=False):
    W, H = 1200, 630
    c = Image.new("RGB", (W, H), NIGHT)
    if bg_video:
        bg = Image.open(os.path.join(PUB, "assets", "video", "inlet-poster-1920.jpg")).convert("RGB")
        bg = cover(bg, W, H, (0.5, 0.6))
        c.paste(bg)
        shade = Image.new("L", (W, H))
        d = ImageDraw.Draw(shade)
        for x in range(W):
            d.line([(x, 0), (x, H)], fill=int(215 * max(0, 1 - x / (W * 0.85)) + 40))
        c = Image.composite(Image.new("RGB", (W, H), NIGHT), c, shade)
    elif photo:
        ph = Image.open(os.path.join(SRC, photo)).convert("RGB")
        pw = 470
        ph = cover(ph, pw, H, focal)
        c.paste(ph, (W - pw, 0))
        grad = Image.new("L", (pw, H))
        d = ImageDraw.Draw(grad)
        for x in range(160):
            d.line([(x, 0), (x, H)], fill=int(255 * (1 - x / 160)))
        c.paste(Image.new("RGB", (pw, H), NIGHT), (W - pw, 0), grad)
    d = ImageDraw.Draw(c)
    m = mark(54)
    c.paste(m, (72, 64), m)
    d.text((72 + m.width + 18, 66), "LEGACY", font=bold("legacy-sans-v1.woff2", 27, 700), fill=INK)
    d.text((72 + m.width + 20, 99), "M E D I C A L", font=bold("legacy-sans-v1.woff2", 13, 500), fill=MUTED)
    d.text((72, 214), kicker.upper(), font=bold("legacy-sans-v1.woff2", 19, 600), fill=GOLD, spacing=4)
    tf = font("legacy-display-v1.woff2", 66)
    maxw = 640 if (photo and not bg_video) else 900
    lines, cur = [], ""
    for word in title.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=tf) > maxw and cur:
            lines.append(cur)
            cur = word
        else:
            cur = t
    lines.append(cur)
    y = 256
    for ln in lines[:4]:
        d.text((70, y), ln, font=tf, fill=INK)
        y += 74
    d.line([(72, 540), (72 + 56, 540)], fill=GOLD, width=2)
    d.text((72, 556), "Palm Beach Gardens, FL  ·  (561) 834-9280", font=font("legacy-sans-v1.woff2", 21), fill=MUTED)
    c.save(os.path.join(OG, slug + ".jpg"), quality=84, optimize=True, progressive=True)


CARDS = [
    ("home", "Your doctor, with time for you.", "Concierge internal medicine", None, (0.5, 0.3), True),
    ("default", "Concierge internal medicine in Palm Beach Gardens.", "Legacy Medical", "dr-shtern-front-desk-team.jpg", (0.5, 0.3), False),
    ("dr-yana-shtern", "Dr. Yana Shtern, MD", "Internal medicine · Nephrology", "dr-shtern-portrait.jpg", (0.5, 0.2), False),
    ("concierge-medicine", "Primary care with fewer patients and more time.", "Concierge medicine", "dr-shtern-desk.jpg", (0.62, 0.3), False),
    ("membership", "Meet us first. Then decide.", "How to join", "reception-wall.jpg", (0.55, 0.4), False),
    ("kidney-care", "Kidney care from your own internist.", "Nephrology", "dr-shtern-full.jpg", (0.5, 0.2), False),
    ("hypertension", "When blood pressure will not come down.", "Hypertension", "dr-shtern-desk.jpg", (0.62, 0.3), False),
    ("geriatric-memory-care", "Care for older adults, and the people who help them.", "Geriatric medicine", "dr-shtern-portrait.jpg", (0.5, 0.2), False),
    ("preventive-care", "A physical with the time to mean something.", "Preventive care", "dr-shtern-full.jpg", (0.5, 0.2), False),
    ("telehealth", "See your doctor without the drive.", "Telehealth", "dr-shtern-desk.jpg", (0.62, 0.3), False),
    ("journal", "Notes on health from a concierge practice.", "Journal", None, (0.5, 0.3), True),
]

if __name__ == "__main__":
    save_icons()
    for args in CARDS:
        card(*args)
    print("icons + %d share cards" % len(CARDS))
