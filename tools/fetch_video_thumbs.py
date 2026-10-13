"""Fetch YouTube thumbnails for every video in content.PRACTICE_FILMS and
content.VIDEO_LIBRARY, crop the 4:3 letterbox to 16:9, register them in
tools/images.json as v-<id> and build them with build_images.py.

The site then serves its own copy, so a visitor's browser makes no request to
YouTube until they press play. Needs network access and Pillow."""
import io
import json
import os
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import content as C  # noqa: E402
from PIL import Image  # noqa: E402

SRC = os.path.join(ROOT, "_dev", "source-images", "videos")
SPEC = os.path.join(ROOT, "tools", "images.json")


def fetch(vid):
    for q in ("sddefault", "hqdefault"):
        try:
            with urllib.request.urlopen("https://i.ytimg.com/vi/%s/%s.jpg" % (vid, q), timeout=20) as r:
                return Image.open(io.BytesIO(r.read())).convert("RGB")
        except Exception:
            continue
    raise SystemExit("no thumbnail for %s" % vid)


def main():
    os.makedirs(SRC, exist_ok=True)
    spec = json.load(open(SPEC, encoding="utf-8"))
    new = []
    for v in C.PRACTICE_FILMS + C.VIDEO_LIBRARY:
        key = "v-" + v["id"]
        path = os.path.join(SRC, v["id"] + ".jpg")
        if not os.path.exists(path):
            im = fetch(v["id"])
            w, h = im.size
            ch = round(w * 9 / 16)
            top = (h - ch) // 2
            im.crop((0, top, w, top + ch)).save(path, quality=92)
        if key not in spec:
            spec[key] = {"file": "videos/%s.jpg" % v["id"], "alt": v["title"],
                         "source": "https://www.youtube.com/watch?v=%s (%s)" % (v["id"], v["channel"]),
                         "q": 80, "widths": [400, 640], "formats": ["webp", "avif"]}
            new.append(key)
    with open(SPEC, "w", encoding="utf-8") as f:
        f.write(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    if new:
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_images.py")] + new, check=True)
    print("thumbnails:", len(C.PRACTICE_FILMS + C.VIDEO_LIBRARY), "new:", len(new))


if __name__ == "__main__":
    main()
