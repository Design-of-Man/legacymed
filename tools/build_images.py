#!/usr/bin/env python3
"""Turn the practice's original photos into web renditions.

    python3 tools/build_images.py

Reads tools/images.json (stem -> source file, focal point, alt, credit) and
the originals in _dev/source-images/. Writes assets/img/<stem>-<w>.{avif,webp,jpg}
for each width that does not upscale, plus assets/img/manifest.json, which
build.py reads. Every rendition is re-encoded from pixels, so EXIF, XMP,
Photoshop and IPTC metadata never reach the site (the old site shipped a
472x666 photo as 3.8 MB of Photoshop data).

Needs Pillow with AVIF support. build.py itself never imports Pillow.
"""
import json
import os
import sys

from PIL import Image, ImageOps

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "_dev", "source-images")
OUT = os.path.join(ROOT, "public", "assets", "img")
WIDTHS = [480, 768, 1200, 1600]


def main():
    spec = json.load(open(os.path.join(ROOT, "tools", "images.json"), encoding="utf-8"))
    os.makedirs(OUT, exist_ok=True)
    manifest = {}
    only = set(sys.argv[1:])  # optional: build just these stems
    old = {}
    mpath = os.path.join(OUT, "manifest.json")
    if only and os.path.exists(mpath):
        old = json.load(open(mpath))
    for stem, s in spec.items():
        if only and stem not in only:
            if stem in old:
                manifest[stem] = old[stem]
            continue
        path = os.path.join(SRC, s["file"])
        im = Image.open(path)
        im = ImageOps.exif_transpose(im)
        if s.get("crop"):
            l, t, r, b = s["crop"]
            im = im.crop((l, t, r, b))
        im = im.convert("RGB")
        w, h = im.size
        want = s.get("widths", WIDTHS)
        fmts = s.get("formats", ["jpg", "webp", "avif"])
        widths = [x for x in want if x <= w] or [w]
        if w not in widths and w < want[-1] and w > widths[-1]:
            widths.append(w)  # small originals: keep full resolution as the top rendition
        made = []
        for tw in widths:
            th = round(h * tw / w)
            r = im if tw == w else im.resize((tw, th), Image.LANCZOS)
            base = os.path.join(OUT, "%s-%d" % (stem, tw))
            if "jpg" in fmts:
                r.save(base + ".jpg", "JPEG", quality=s.get("q", 80), optimize=True, progressive=True)
            r.save(base + ".webp", "WEBP", quality=s.get("q", 80) - 2, method=6)
            r.save(base + ".avif", "AVIF", quality=s.get("q", 80) - 22, speed=4)
            made.append(tw)
        if s.get("og"):  # a 1200-wide JPEG for social share cards
            ow = min(1200, w)
            im.resize((ow, round(h * ow / w)), Image.LANCZOS).save(os.path.join(OUT, "%s-og.jpg" % stem), "JPEG", quality=78, optimize=True, progressive=True)
        manifest[stem] = {"w": w, "h": h, "widths": made, "focal": s.get("focal", "50% 50%"),
                          "alt": s.get("alt", ""), "source": s.get("source", ""), "credit": s.get("credit", ""), "formats": fmts}
        sizes = sum(os.path.getsize(os.path.join(OUT, "%s-%d.avif" % (stem, x))) for x in made)
        print("%-28s %4dx%-4d -> %s  (avif total %d KB)" % (stem, w, h, made, sizes // 1024))
    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w"), indent=1, sort_keys=True)
    print("manifest: %d images" % len(manifest))


if __name__ == "__main__":
    sys.exit(main())
