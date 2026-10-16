#!/usr/bin/env python3
"""Pre-deploy gate for legacymedicalpalmbeach.com. Exits non-zero on any blocker.

    python3 _dev/preflight.py

Ported from the Design of Man preflight. Checks every generated page in
public/: unconfigured placeholders, form endpoints, broken internal links
(including srcset and preloads), missing assets, duplicate or missing
titles/descriptions, canonicals off the production domain, invalid JSON-LD,
images without alt, one <h1>, landmarks, sitemap coverage, redirect targets,
page weight budgets, and the copy rules from build.py.
"""
import glob
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PUB = os.path.join(ROOT, "public")
DOMAIN = "https://legacymedicalpalmbeach.com"
HOME_BUDGET_KB = 1500          # initial homepage weight, excluding the lazily attached video
ASSET_BUDGET_KB = {".avif": 400, ".webp": 450, ".jpg": 600, ".woff2": 80, ".css": 80, ".js": 40}

blockers, notes = [], []
seen_titles, seen_descs = {}, {}


class Doc(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self._in_title = False
        self.metas, self.canonical = {}, None
        self.links, self.imgs, self.scripts, self.srcs = [], [], [], []
        self.h1 = 0
        self.landmarks = set()
        self.ld, self._in_ld, self._buf = [], False, ""
        self.lang = None
        self.forms = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.metas[k] = a.get("content", "")
        elif tag == "link":
            if a.get("rel") == "canonical":
                self.canonical = a.get("href")
            if a.get("href"):
                self.srcs.append(a["href"])
            if a.get("imagesrcset"):
                self.srcs += [p.strip().split(" ")[0] for p in a["imagesrcset"].split(",")]
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.imgs.append(a)
            if a.get("src"):
                self.srcs.append(a["src"])
        elif tag == "source" and a.get("srcset"):
            self.srcs += [p.strip().split(" ")[0] for p in a["srcset"].split(",")]
        elif tag == "video":
            for k in ("poster",):
                if a.get(k):
                    self.srcs.append(a[k])
            for k in ("data-hd", "data-sd", "data-portrait"):
                if a.get(k):
                    self.srcs += a[k].split("|")
        elif tag == "script":
            if a.get("src"):
                self.scripts.append(a["src"])
            if a.get("type") == "application/ld+json":
                self._in_ld, self._buf = True, ""
        elif tag == "h1":
            self.h1 += 1
        elif tag in ("header", "nav", "main", "footer"):
            self.landmarks.add(tag)
        elif tag == "form":
            self.forms.append(a)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_ld:
            self._in_ld = False
            try:
                self.ld.append(json.loads(self._buf))
            except Exception as e:
                blockers.append(("SCHEMA", "invalid JSON-LD: %s" % e))

    def handle_data(self, d):
        if self._in_title:
            self.title = (self.title or "") + d
        if self._in_ld:
            self._buf += d


def target(href):
    clean = href.split("#")[0].split("?")[0]
    if not clean:
        return None
    if clean.startswith(DOMAIN):
        clean = clean[len(DOMAIN):] or "/"
    t = os.path.normpath(os.path.join(PUB, clean.lstrip("/")))
    if os.path.exists(t + ".html"):
        t += ".html"
    elif os.path.isdir(t):
        t = os.path.join(t, "index.html")
    return t


def is_internal(href):
    return href.startswith("/") or href.startswith(DOMAIN)


def walk_ld(node, found):
    if isinstance(node, dict):
        t = node.get("@type")
        if t:
            for x in (t if isinstance(t, list) else [t]):
                found.add(x)
        for v in node.values():
            walk_ld(v, found)
    elif isinstance(node, list):
        for v in node:
            walk_ld(v, found)


pages = sorted(os.path.relpath(p, PUB) for p in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True))
all_types = {}
for rel in pages:
    html = open(os.path.join(PUB, rel), encoding="utf-8").read()
    d = Doc()
    d.feed(html)

    def bad(c, m, rel=rel):
        blockers.append((c, "%s: %s" % (rel, m)))

    def note(c, m, rel=rel):
        notes.append((c, "%s: %s" % (rel, m)))

    for ph in set(re.findall(r"REPLACE_[A-Z_]+|TODO|FIXME|lorem ipsum", html, flags=re.I)):
        bad("CONFIG", "placeholder in output: %s" % ph)
    for f in d.forms:
        act = f.get("action", "")
        if not act or act == "#":
            bad("CONFIG", "form posts nowhere")
        elif act.startswith("/api/") and not os.path.exists(os.path.join(ROOT, "api", act[5:] + ".js")):
            bad("CONFIG", "form endpoint missing: %s" % act)

    if not d.lang:
        bad("A11Y", "missing lang")
    title = (d.title or "").strip()
    if not title:
        bad("SEO", "missing <title>")
    elif len(title) > 70:
        note("SEO", "title %d chars: %s" % (len(title), title))
    desc = d.metas.get("description", "")
    if not desc:
        bad("SEO", "missing meta description")
    elif not (100 <= len(desc) <= 165):
        note("SEO", "meta description %d chars" % len(desc))
    if rel != "404.html":
        if not d.canonical:
            bad("SEO", "missing canonical")
        elif not d.canonical.startswith(DOMAIN):
            bad("SEO", "canonical not on production domain: %s" % d.canonical)
        for t in ["og:title", "og:description", "og:image", "og:url", "twitter:card"]:
            if t not in d.metas:
                bad("SEO", "missing %s" % t)
        og = d.metas.get("og:image", "")
        if og.startswith(DOMAIN) and not os.path.exists(target(og) or ""):
            bad("LINK", "og:image file missing: %s" % og)
        if title in seen_titles:
            bad("SEO", "duplicate title with %s" % seen_titles[title])
        seen_titles[title] = rel
        if desc and desc in seen_descs:
            bad("SEO", "duplicate meta description with %s" % seen_descs[desc])
        seen_descs[desc] = rel
        if not d.ld:
            bad("SCHEMA", "no JSON-LD")
    found = set()
    for block in d.ld:
        walk_ld(block, found)
        if isinstance(block, dict) and block.get("@context") != "https://schema.org":
            bad("SCHEMA", "JSON-LD without schema.org context")
    for t in found:
        all_types.setdefault(t, 0)
        all_types[t] += 1
    if "AggregateRating" in found or "Review" in found:
        bad("SCHEMA", "self-served review markup (Google ignores or penalises it)")

    if d.h1 != 1:
        bad("A11Y", "%d <h1> elements" % d.h1)
    for lm in ("header", "nav", "main", "footer"):
        if lm not in d.landmarks:
            bad("A11Y", "missing <%s>" % lm)
    dup_ids = {i for i in d.ids if d.ids.count(i) > 1}
    if dup_ids:
        bad("A11Y", "duplicate ids: %s" % ", ".join(sorted(dup_ids)))

    for img in d.imgs:
        if "alt" not in img:
            bad("A11Y", "img missing alt: %s" % img.get("src", "?"))
        if not (img.get("width") and img.get("height")):
            bad("CLS", "img without width/height: %s" % img.get("src", "?"))
    for src in d.srcs + d.scripts:
        if src.startswith(("http", "data:", "mailto:")) and not src.startswith(DOMAIN):
            continue
        if src.startswith("/_vercel/"):
            continue
        t = target(src)
        if t and not os.path.exists(t):
            bad("LINK", "missing asset: %s" % src)
    for href in d.links:
        if href.startswith("tel:"):
            if not re.match(r"^tel:\+1\d{10}$", href):
                bad("LINK", "tel: not in +1########## form: %s" % href)
            continue
        if href == "#" or href == "":
            bad("LINK", 'dead link href="%s"' % href)
            continue
        if href.startswith("#"):
            if href[1:] not in d.ids:
                bad("LINK", "in-page anchor with no target: %s" % href)
            continue
        if is_internal(href):
            t = target(href)
            if t and not os.path.exists(t):
                bad("LINK", "broken internal link: %s" % href)
            frag = href.split("#", 1)[1] if "#" in href else None
            if frag and t and os.path.exists(t) and ('id="%s"' % frag) not in open(t, encoding="utf-8").read():
                bad("LINK", "anchor #%s not found on %s" % (frag, href))
        elif "cmedjupiter.com" in href:
            bad("LINK", "link to the old duplicate domain: %s" % href)

# ------------------------------------------------------------------ site-wide
for f in ["robots.txt", "sitemap.xml", "llms.txt", "site.webmanifest", "favicon.svg", "favicon.ico", "apple-touch-icon.png", "404.html"]:
    if not os.path.exists(os.path.join(PUB, f)):
        blockers.append(("BUILD", "missing public/%s" % f))
for f in ["vercel.json", "api/tour.js", "api/reviews.js"]:
    if not os.path.exists(os.path.join(ROOT, f)):
        blockers.append(("BUILD", "missing %s" % f))

sm = open(os.path.join(PUB, "sitemap.xml"), encoding="utf-8").read()
locs = set(re.findall(r"<loc>(.*?)</loc>", sm))
for rel in pages:
    if rel == "404.html":
        continue
    html = open(os.path.join(PUB, rel), encoding="utf-8").read()
    if re.search(r'<meta[^>]+name="robots"[^>]+noindex', html):
        continue
    slug = "" if rel == "index.html" else (rel[:-11] if rel.endswith("/index.html") else rel[:-5])
    if DOMAIN + ("/" + slug if slug else "/") not in locs:
        blockers.append(("SEO", "not in sitemap: %s" % rel))
for loc in locs:
    if not os.path.exists(target(loc) or ""):
        blockers.append(("SEO", "sitemap URL has no page: %s" % loc))

vj = json.load(open(os.path.join(ROOT, "vercel.json")))
for r in vj.get("redirects", []):
    dst = r["destination"]
    if dst.startswith(DOMAIN):
        dst = dst[len(DOMAIN):] or "/"
    if ":" in dst:
        continue
    t = target(dst)
    if not t or not os.path.exists(t):
        blockers.append(("REDIRECT", "%s -> %s has no target page" % (r["source"], r["destination"])))
cm = os.path.join(ROOT, "_dev", "redirects", "cmedjupiter.vercel.json")
if os.path.exists(cm):
    for r in json.load(open(cm))["redirects"]:
        dst = r["destination"][len(DOMAIN):] or "/"
        if ":" not in dst and not os.path.exists(target(dst) or ""):
            blockers.append(("REDIRECT", "cmedjupiter %s -> %s has no target page" % (r["source"], r["destination"])))

for path in glob.glob(os.path.join(PUB, "assets", "**", "*"), recursive=True):
    ext = os.path.splitext(path)[1]
    if ext in ASSET_BUDGET_KB and os.path.getsize(path) > ASSET_BUDGET_KB[ext] * 1024:
        blockers.append(("WEIGHT", "%s is %d KB (budget %d KB)" % (os.path.relpath(path, PUB), os.path.getsize(path) // 1024, ASSET_BUDGET_KB[ext])))
for path in glob.glob(os.path.join(PUB, "assets", "video", "*.mp4")) + glob.glob(os.path.join(PUB, "assets", "video", "*.webm")):
    # Owner asked for the 4K-sourced film (Oct 2026). It never loads before the page does
    # (preload="none", attached after load, tap-to-play on phones), so the cap is generous.
    if os.path.getsize(path) > 22 * 1024 * 1024:
        blockers.append(("WEIGHT", "%s over 22 MB" % os.path.relpath(path, PUB)))

for need in ["MedicalClinic", "Physician", "WebSite", "FAQPage", "BreadcrumbList", "BlogPosting", "MedicalWebPage", "OpeningHoursSpecification", "GeoCoordinates"]:
    if need not in all_types:
        blockers.append(("SCHEMA", "no %s anywhere on the site" % need))

r = subprocess.run([sys.executable, os.path.join(ROOT, "build.py"), "--check"], cwd=ROOT, capture_output=True, text=True)
if r.returncode != 0:
    blockers.append(("COPY", "build.py --check failed:\n" + r.stdout[-3000:] + r.stderr[-2000:]))

print("=" * 66)
print("LEGACY MEDICAL: PRE-DEPLOY CHECK")
print("=" * 66)
print("Pages checked: %d   Schema types: %s\n" % (len(pages), ", ".join("%s×%d" % kv for kv in sorted(all_types.items()))))
if blockers:
    print("BLOCKERS (%d)\n%s" % (len(blockers), "-" * 66))
    for c, m in blockers:
        print("  [%s] %s" % (c, m))
    print()
else:
    print("BLOCKERS: none\n")
if notes:
    grouped = {}
    for c, m in notes:
        grouped.setdefault(c, []).append(m)
    print("NOTES (%d)\n%s" % (len(notes), "-" * 66))
    for c in sorted(grouped):
        print("  [%s] %d" % (c, len(grouped[c])))
        for m in grouped[c][:8]:
            print("      · %s" % m)
        if len(grouped[c]) > 8:
            print("      · and %d more" % (len(grouped[c]) - 8))
print("=" * 66)
print("RESULT: %s" % ("FAIL: do not deploy" if blockers else "READY TO DEPLOY"))
print("=" * 66)
sys.exit(1 if blockers else 0)
