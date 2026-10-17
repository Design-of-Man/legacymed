#!/usr/bin/env python3
"""Legacy Medical: site generator. The single source of truth.

    python3 build.py            regenerate every page, sitemap, robots, llms.txt
    python3 build.py --check    regenerate, then fail if any copy rule is broken

Standard library only, so a clean checkout (or Vercel's build image) can build
with no installs. Facts live in PRACTICE / DOCTOR / TEAM below; page copy lives
in content.py; journal posts in journal_content.py. Edit those, rebuild, commit.

Environment (all optional, read at build time on Vercel):
    GA4_ID                  e.g. G-XXXXXXX. Adds consent-gated GA4 to pages
                            that carry no form. Off when unset.
    VERCEL_ANALYTICS=1      Adds Vercel Web Analytics + Speed Insights.
                            Only set it once both are enabled in the project.
    GOOGLE_PLACES_API_KEY   Present at build time => the homepage asks
                            /api/reviews for the live Google rating.
"""
import datetime
import hashlib
import html
import json
import os
import re
import sys
from urllib.parse import quote

import content as C
import journal_content as J

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")  # Vercel serves only this directory
BASE = "https://legacymedicalpalmbeach.com"
SITE_UPDATED = "2026-10-10"

GA4_ID = os.environ.get("GA4_ID", "").strip()
VERCEL_ANALYTICS = os.environ.get("VERCEL_ANALYTICS", "") == "1"
LIVE_REVIEWS = bool(os.environ.get("GOOGLE_PLACES_API_KEY", "").strip())

# --------------------------------------------------------------------------
# Facts. One place. Copy, schema, footer, llms.txt all read from here.
# --------------------------------------------------------------------------
PRACTICE = {
    "name": "Legacy Medical",
    "descriptor": "Concierge Medicine · Palm Beach Gardens",
    "legal_name": "Legacy Medical PLLC",
    "alt_names": ["Legacy Medical Palm Beach", "Legacy Medical Concierge"],
    "phone": "(561) 834-9280",
    "tel": "+15618349280",
    "fax": "(561) 834-9279",
    "email": "info@legacymedicalpalmbeach.com",
    "street": "11380 Prosperity Farms Road, Suite 114",
    "street_short": "11380 Prosperity Farms Rd, Suite 114",
    "city": "Palm Beach Gardens",
    "region": "FL",
    "postal": "33410",
    "country": "US",
    "geo": C.GEO,
    "building_notes": "First-floor suite, ADA accessible, free Wi-Fi",
    # day, open, close (24h). Days absent from this list are closed.
    "hours": [("Monday", "09:00", "17:00"), ("Tuesday", "09:00", "17:00"),
              ("Wednesday", "09:00", "17:00"), ("Thursday", "09:00", "17:00"),
              ("Friday", "09:00", "14:00")],
    "after_hours": "Members reach the practice by phone 24 hours a day, 7 days a week.",
    "service_area": ["Palm Beach Gardens", "Jupiter", "Juno Beach", "Tequesta", "Hobe Sound",
                     "Stuart", "North Palm Beach", "Palm Beach", "West Palm Beach"],
    "insurance_shown": ["Medicare", "Aetna", "Cigna", "BlueCross BlueShield"],
    "google_maps": "https://www.google.com/maps/search/?api=1&query=" + quote("Legacy Medical, 11380 Prosperity Farms Rd Suite 114, Palm Beach Gardens, FL 33410"),
    "map_embed": "https://www.google.com/maps?q=" + quote("11380 Prosperity Farms Rd Suite 114, Palm Beach Gardens, FL 33410") + "&output=embed",
    "socials": C.SOCIALS,
    # TODO(practice): portal URL. The old FAQ mentions a portal but never links it.
    "portal_url": None,
}

DOCTOR = C.DOCTOR
TEAM = C.TEAM

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def esc(s):
    return html.escape(str(s), quote=True)


def asset_v(rel):
    try:
        with open(os.path.join(PUB, rel), "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:10]
    except FileNotFoundError:
        return "missing"


def a(rel):
    """Root-relative asset URL with a content-hash cache-buster."""
    return "/" + rel + "?v=" + asset_v(rel)


def url(path):
    """Canonical absolute URL for a site path ('' = home)."""
    path = path.strip("/")
    return BASE + ("/" + path if path else "/")


def clamp_desc(s, n=158):
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= n:
        return s
    cut = s[: n - 1].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "…"


def hours_compact():
    return "Mon–Thu 9 AM–5 PM · Fri 9 AM–2 PM"


def fmt12(t):
    h, m = map(int, t.split(":"))
    suffix = "AM" if h < 12 else "PM"
    h = h % 12 or 12
    return ("%d:%02d %s" % (h, m, suffix)).replace(":00 ", " ")


def hx(text):
    """Escape a heading but keep its <em> accent phrase."""
    return esc(text).replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")


def words_spans(text):
    """Split a statement into word spans for the scroll-fill effect."""
    out = []
    for i, w in enumerate(text.split(" ")):
        out.append('<span class="w" style="--wi:%d">%s</span>' % (i, w))
    return " ".join(out)


ICONS = {
    "arrow": '<svg class="arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M1 8h13M9 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>',
    "phone": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3.6 1.5 5.9 1l1.3 3.1-1.6 1.2a8.4 8.4 0 0 0 5.1 5.1l1.2-1.6 3.1 1.3-.5 2.3c-.1.6-.7 1.1-1.3 1.1C6.6 13.5 2.5 9.4 2.5 2.8c0-.6.5-1.2 1.1-1.3Z" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>',
    "chev": '<svg viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="m2 4 4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>',
    "play": '<svg class="i-play" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M3 1.5v9l7-4.5z" fill="currentColor"/></svg>',
    "pause": '<svg class="i-pause" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M3 1.5h2v9H3zM7 1.5h2v9H7z" fill="currentColor"/></svg>',
    "info": '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8.5" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M10 9v5M10 6.2v.1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "shield": '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 1.8 3.5 4.3v5c0 4 2.8 7.5 6.5 8.9 3.7-1.4 6.5-4.9 6.5-8.9v-5z" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/><path d="m7 10 2 2 4-4.5" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>',
    "star": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="m8 1.2 2 4.3 4.7.5-3.5 3.2 1 4.6L8 11.4l-4.2 2.4 1-4.6L1.3 6l4.7-.5z" fill="currentColor"/></svg>',
    "instagram": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="1.5" width="13" height="13" rx="3.5" fill="none" stroke="currentColor" stroke-width="1.3"/><circle cx="8" cy="8" r="3" fill="none" stroke="currentColor" stroke-width="1.3"/><circle cx="11.8" cy="4.2" r=".8" fill="currentColor"/></svg>',
    "facebook": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M9.2 15V8.7h2.1l.3-2.5H9.2V4.7c0-.7.2-1.2 1.2-1.2h1.3V1.3a17 17 0 0 0-1.9-.1c-1.9 0-3.2 1.2-3.2 3.3v1.8H4.5v2.5h2.1V15z" fill="currentColor"/></svg>',
    "linkedin": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3.6 5.5H1.2V15h2.4zM2.4 1A1.4 1.4 0 1 0 2.4 3.8 1.4 1.4 0 0 0 2.4 1zM15 9.7c0-2.6-1.4-4.3-3.6-4.3-1.2 0-2 .6-2.4 1.2v-1H6.6V15H9v-4.9c0-1.2.4-2.1 1.6-2.1 1.1 0 1.6.8 1.6 2.1V15H15z" fill="currentColor"/></svg>',
}


def icon(name):
    return ICONS[name]


def svc_icon(kind):
    """Line icons for the 'included' grid. Drawn, 1.3px strokes, 32px box."""
    p = {
        "time": '<circle cx="16" cy="16" r="12"/><path d="M16 9v7l5 3"/>',
        "phone": '<path d="M9 4.5 12.6 4l2 4.8-2.4 1.8a13 13 0 0 0 7.8 7.8l1.8-2.4 4.8 2-.5 3.6c-.1.9-1 1.7-2 1.7C13.6 23.3 6.7 16.4 6.7 6.5c0-1 .8-1.9 1.7-2z"/>',
        "calendar": '<rect x="5" y="7" width="22" height="20" rx="2"/><path d="M5 13h22M11 4v6M21 4v6M11 18h3v3h-3z"/>',
        "lab": '<path d="M12 4h8M13 4v8L6.5 24a2 2 0 0 0 1.8 3h15.4a2 2 0 0 0 1.8-3L19 12V4"/><path d="M9 19h14"/>',
        "heart": '<path d="M4 16h5l2-5 4 10 3-7 2 2h8"/>',
        "screen": '<rect x="4" y="6" width="24" height="16" rx="2"/><path d="M12 27h8M16 22v5"/>',
        "people": '<circle cx="11" cy="11" r="4"/><circle cx="22" cy="12" r="3"/><path d="M4 26c0-4 3-7 7-7s7 3 7 7M19 19.5c3.6-.6 7 1.6 7 5.5"/>',
        "pill": '<rect x="5" y="12" width="22" height="8" rx="4" transform="rotate(-35 16 16)"/><path d="m13 11 6 10"/>',
        "shield": '<path d="M16 4 7 7.5v7c0 5.6 3.9 10.5 9 12.5 5.1-2 9-6.9 9-12.5v-7z"/><path d="m12 16 3 3 5-6"/>',
        "home": '<path d="M5 15 16 6l11 9M8 13v13h16V13"/><path d="M13 26v-7h6v7"/>',
        "brain": '<path d="M13 6a4 4 0 0 0-4 4 4 4 0 0 0-3 6 4 4 0 0 0 3 6 4 4 0 0 0 4 4h1V6zM19 6a4 4 0 0 1 4 4 4 4 0 0 1 3 6 4 4 0 0 1-3 6 4 4 0 0 1-4 4h-1V6z"/>',
        "kidney": '<path d="M12 5c-4 0-7 4-7 10s3 12 8 12c3 0 4-2 4-5s-2-3-2-7 2-4 2-6-2-4-5-4zM22 9c3 1 5 4 5 8 0 5-2 9-5 9"/>',
        "gauge": '<path d="M5 22a11 11 0 1 1 22 0"/><path d="m16 22 5-7"/><circle cx="16" cy="22" r="1.5"/>',
        "ecg": '<rect x="4" y="7" width="24" height="18" rx="2"/><path d="M7 17h4l2-5 3 9 2-6 1 2h6"/>',
    }[kind]
    return ('<svg class="ico" viewBox="0 0 32 32" aria-hidden="true" focusable="false" fill="none" '
            'stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % p)


# --------------------------------------------------------------------------
# Images. tools/build_images.py writes assets/img/manifest.json from the
# originals in _dev/source-images; build.py only reads that manifest, so it
# stays stdlib-only.
# --------------------------------------------------------------------------
def load_manifest():
    p = os.path.join(PUB, "assets/img/manifest.json")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)


IMG = load_manifest()


def photo(stem, alt, sizes="100vw", cls="", eager=False, focal=None, max_w=None, decorative=False):
    """<picture> with AVIF + WebP + JPEG and width descriptors."""
    m = IMG.get(stem)
    if not m:
        raise SystemExit("photo(): no manifest entry for %r. Run tools/build_images.py." % stem)
    widths = [w for w in m["widths"] if not max_w or w <= max_w] or m["widths"][:1]
    def srcset(ext):
        return ", ".join("/assets/img/%s-%d.%s %dw" % (stem, w, ext, w) for w in widths)
    w0 = widths[-1]
    h0 = round(w0 * m["h"] / m["w"])
    fp = focal or m.get("focal") or "50% 50%"
    alt_attr = "" if decorative else esc(alt)
    attrs = 'width="%d" height="%d" alt="%s" style="object-position:%s"' % (w0, h0, alt_attr, fp)
    if eager:
        attrs += ' fetchpriority="high" decoding="async"'
    else:
        attrs += ' loading="lazy" decoding="async"'
    if cls:
        attrs += ' class="%s"' % cls
    fb = "jpg" if "jpg" in m.get("formats", ["jpg"]) else "webp"
    return ('<picture><source type="image/avif" srcset="%s" sizes="%s">'
            '<source type="image/webp" srcset="%s" sizes="%s">'
            '<img src="/assets/img/%s-%d.%s" srcset="%s" sizes="%s" %s></picture>'
            % (srcset("avif"), sizes, srcset("webp"), sizes, stem, widths[min(1, len(widths) - 1)], fb,
               srcset(fb), sizes, attrs))


# --------------------------------------------------------------------------
# Navigation. Labels here are also the breadcrumb section names.
# --------------------------------------------------------------------------
NAV = [
    ("About", None, [
        ("dr-yana-shtern", "Dr. Yana Shtern, MD", "Internist and nephrologist"),
        ("our-team", "Our team", "Who answers when you call"),
        ("for-families", "For families", "Caring for a parent"),
        ("seasonal-residents", "Seasonal residents", "Care between seasons"),
    ]),
    ("Services", None, [
        ("concierge-medicine", "Concierge medicine", "How the practice works"),
        ("kidney-care", "Kidney care and Nephrology", "CKD, stones, electrolytes"),
        ("hypertension", "Hypertension", "Hard-to-control blood pressure"),
        ("geriatric-memory-care", "Geriatric and memory care", "Healthy aging, cognition"),
        ("preventive-care", "Preventive care and physicals", "The annual executive physical"),
        ("telehealth", "Telehealth", "Visits by video"),
    ]),
    ("Membership", None, [
        ("meet-and-greet", "Meet and greet", "Your first visit"),
        ("membership", "How to join", "Three unhurried steps"),
        ("insurance-and-fees", "Insurance and fees", "What insurance still covers"),
        ("concierge-vs-traditional-primary-care", "Concierge vs. traditional", "A side-by-side look"),
        ("faq", "FAQ", "Straight answers"),
    ]),
    ("Patients", None, [
        ("patients", "For patients", "Visits, calls, labs, records"),
        ("same-or-next-day-visits", "Same or next day visits", "Seen when you need it"),
        ("chronic-care", "Chronic care support", "Ongoing conditions"),
        ("specialists-and-hospital-care", "Specialists and hospitals", "Care that stays in one place"),
        ("labs-and-tests", "Labs and tests", "Done in the office"),
        ("blog", "Blog", "Articles on health"),
        ("videos", "Videos", "Watch and learn"),
    ]),
    ("Areas Served", "areas-we-serve", None),
    ("FAQ", "faq", None),
    ("Contact", "contact", None),
]


def section_of(slug):
    for label, href, kids in NAV:
        if href and (slug == href or slug.startswith(href.split("-")[0] + "/") and href == "areas-we-serve"):
            return label, href
        if kids and any(k[0] == slug for k in kids):
            return label, None
    if slug.startswith("areas/"):
        return "Areas Served", "areas-we-serve"
    if slug.startswith("blog/"):
        return "Blog", "blog"
    return None, None


def nav_html(current):
    items = []
    for i, (label, href, kids) in enumerate(NAV):
        if kids:
            mid = "menu-%d" % i
            is_cur = any(k[0] == current for k in kids) or (current.startswith("blog/") and any(k[0] == "blog" for k in kids))
            links = "".join(
                '<li><a href="/%s"%s>%s<small>%s</small></a></li>' % (
                    k[0], ' aria-current="page"' if k[0] == current else "", esc(k[1]), esc(k[2]))
                for k in kids)
            items.append(
                '<li><button class="nav-trigger%s" type="button" aria-expanded="false" aria-controls="%s">%s %s</button>'
                '<ul class="menu" id="%s">%s</ul></li>' % (" current" if is_cur else "", mid, esc(label), icon("chev"), mid, links))
        else:
            cur = current == href or (href == "areas-we-serve" and current.startswith("areas/")) or (href == "blog" and current.startswith("blog/"))
            items.append('<li><a class="nav-link" href="/%s"%s>%s</a></li>' % (href, ' aria-current="page"' if cur else "", esc(label)))
    return items


def header(current):
    p = PRACTICE
    items = nav_html(current)
    return """<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">%(mark)s<span class="brand-name"><b>Legacy</b> <span>Medical</span><span class="sr-only">, home</span></span></a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav-list">%(items)s</ul>
      <div class="mobile-cta">
        <a class="btn" href="/meet-and-greet" data-loc="mobile-menu">Book a meet and greet %(arrow)s</a>
        <a class="btn ghost" href="tel:%(tel)s" data-loc="mobile-menu">Call %(phone)s</a>
        <p class="menu-foot">%(street)s, %(city)s<br>Mon–Thu 9–5 · Fri 9–2 · Members: phone 24/7</p>
      </div>
    </nav>
    <div class="header-actions">
      <a class="header-phone" href="tel:%(tel)s" data-loc="header">%(ico)s<span class="label">%(phone)s</span><span class="sr-only"> (call the office)</span></a>
      <a class="btn small" href="/meet-and-greet" data-loc="header">Book a meet &amp; greet</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span></button>
    </div>
  </div>
</header>""" % {"mark": brand_mark(), "items": "".join(items), "tel": p["tel"], "phone": p["phone"],
                 "ico": icon("phone"), "arrow": icon("arrow"),
                 "street": p["street_short"], "city": p["city"]}


def brand_mark():
    """The practice's own mark: a gold infinity loop crossed by an ECG line,
    cropped from the transparent logo on the old site (tools/build_brand.py)."""
    return ('<img class="brand-mark" src="/assets/img/legacy-mark-80.png" srcset="/assets/img/legacy-mark-80.png 1x, '
            '/assets/img/legacy-mark-120.png 1.5x" width="69" height="40" alt="">')


def footer():
    p = PRACTICE
    col = lambda title, links: '<div class="footer-col"><h3>%s</h3><ul>%s</ul></div>' % (
        title, "".join('<li><a href="/%s">%s</a></li>' % (h, esc(t)) for h, t in links))
    care = [(k[0], k[1]) for k in NAV[1][2]]
    practice = [("dr-yana-shtern", "Dr. Yana Shtern"), ("our-team", "Our team"), ("membership", "How to join"),
                ("insurance-and-fees", "Insurance and fees"), ("faq", "FAQ"), ("blog", "Blog"),
                ("contact", "Contact")]
    areas = [("areas/" + l["slug"], l["name"]) for l in C.LOCATIONS] + [("areas-we-serve", "All areas served")]
    socials = "".join('<a href="%s" rel="noopener" target="_blank">%s<span class="sr-only">%s (opens in a new tab)</span></a>' % (
        esc(s["url"]), icon(s["icon"]), esc(s["label"])) for s in p["socials"])
    hours = "<br>".join(["Mon–Thu 9:00 AM – 5:00 PM", "Fri 9:00 AM – 2:00 PM", "Sat–Sun closed"])
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <h2>One patient at a time. A <em>very</em> small practice on purpose.</h2>
        <address class="footer-contact">
          <span>%(street)s<br>%(city)s, %(region)s %(postal)s</span>
          <a href="tel:%(tel)s" data-loc="footer">%(phone)s</a>
          <span>Fax %(fax)s</span>
          <a href="mailto:%(email)s" data-loc="footer">%(email)s</a>
          <span class="small" style="margin-top:.6rem">%(hours)s</span>
        </address>
        %(socials)s
      </div>
      %(care)s%(practice)s%(areas)s
    </div>
    <div class="footer-word" aria-hidden="true" data-word="Legacy Medical"></div>
    <div class="footer-bottom">
      <p>© %(year)s %(legal)s. Concierge Internal Medicine in Palm Beach Gardens, Florida.</p>
      <ul>
        <li><a href="/privacy">Website privacy</a></li>
        <li><a href="/notice-of-privacy-practices">Notice of Privacy Practices</a></li>
        <li><a href="/accessibility">Accessibility</a></li>
      </ul>
    </div>
    <p class="small muted" style="margin-top:1rem;max-width:48rem">This website is general information, not medical advice. In an emergency, call 911.</p>
  </div>
</footer>""" % {
        "street": p["street"], "city": p["city"], "region": p["region"], "postal": p["postal"],
        "tel": p["tel"], "phone": p["phone"], "fax": p["fax"], "email": p["email"], "hours": hours,
        "socials": ('<div class="socials">%s</div>' % socials) if socials else "",
        "care": col("Services", care), "practice": col("Practice", practice), "areas": col("Areas served", areas),
        "year": SITE_UPDATED[:4], "legal": p["legal_name"]}


def callbar():
    p = PRACTICE
    return ('<div class="callbar" aria-label="Quick contact" role="region">'
            '<a class="btn ghost small" href="tel:%s" data-loc="callbar">%s Call</a>'
            '<a class="btn small" href="/meet-and-greet" data-loc="callbar">Meet &amp; greet</a></div>' % (p["tel"], icon("phone")))


# --------------------------------------------------------------------------
# Schema. Every node is built from the facts above; pages reference the
# clinic and physician by @id so there is one entity, never a copy.
# --------------------------------------------------------------------------
ORG_ID = BASE + "/#clinic"
SITE_ID = BASE + "/#website"
DOC_ID = BASE + "/dr-yana-shtern#physician"


def opening_hours_spec():
    return [{"@type": "OpeningHoursSpecification", "dayOfWeek": "https://schema.org/" + d,
             "opens": o, "closes": c} for d, o, c in PRACTICE["hours"]]


def postal_address():
    p = PRACTICE
    return {"@type": "PostalAddress", "streetAddress": p["street"], "addressLocality": p["city"],
            "addressRegion": p["region"], "postalCode": p["postal"], "addressCountry": p["country"]}


def clinic_node():
    p = PRACTICE
    node = {
        "@type": ["MedicalClinic", "MedicalBusiness"],
        "@id": ORG_ID,
        "name": p["name"],
        "legalName": p["legal_name"],
        "alternateName": p["alt_names"],
        "description": C.ONE_LINER,
        "url": BASE + "/",
        "telephone": p["tel"],
        "faxNumber": "+15618349279",
        "email": p["email"],
        "address": postal_address(),
        "geo": {"@type": "GeoCoordinates", "latitude": p["geo"]["lat"], "longitude": p["geo"]["lng"]},
        "hasMap": p["google_maps"],
        "openingHoursSpecification": opening_hours_spec(),
        "medicalSpecialty": ["https://schema.org/PrimaryCare", "https://schema.org/Renal", "https://schema.org/Geriatric"],
        "areaServed": [{"@type": "City", "name": c + ", FL"} for c in p["service_area"]] + [{"@type": "AdministrativeArea", "name": "Martin County, FL"}],
        "availableService": [{"@type": "MedicalProcedure" if s.get("procedure") else "MedicalTherapy", "name": s["name"]} for s in C.SERVICES_INCLUDED if s.get("schema")],
        "employee": {"@id": DOC_ID},
        "founder": {"@id": DOC_ID},
        "isAcceptedPaymentMethod": None,
        "logo": BASE + "/assets/img/og/logo-512.png",
        "image": BASE + "/assets/img/og/home.jpg",
        "sameAs": [s["url"] for s in p["socials"]] + C.CLINIC_SAME_AS,
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": "Wheelchair accessible first-floor suite", "value": True},
                           {"@type": "LocationFeatureSpecification", "name": "Free Wi-Fi", "value": True}],
    }
    node.pop("isAcceptedPaymentMethod")
    if C.PRICE_RANGE:
        node["priceRange"] = C.PRICE_RANGE
    if C.HEALTH_PLANS:
        node["healthPlanNetworkId"] = None
        node.pop("healthPlanNetworkId")
    return node


def physician_node(full=False):
    d = DOCTOR
    node = {
        "@type": ["Physician", "Person"],
        "@id": DOC_ID,
        "name": d["name"],
        "honorificSuffix": "MD",
        "jobTitle": d["title"],
        "url": url("dr-yana-shtern"),
        "image": BASE + "/assets/img/og/dr-yana-shtern.jpg",
        "worksFor": {"@id": ORG_ID},
        "medicalSpecialty": ["https://schema.org/PrimaryCare", "https://schema.org/Renal"],
        "usNPI": d["npi"],
        "identifier": [{"@type": "PropertyValue", "propertyID": "NPI", "value": d["npi"]},
                       {"@type": "PropertyValue", "propertyID": "Florida medical license", "value": d["license"]}],
        "hospitalAffiliation": [{"@type": "Hospital", "name": h["name"], "url": h["url"],
                                 "address": h["address"]} for h in d["hospitals"]],
        "memberOf": [{"@type": "Organization", "name": m} for m in d["member_of"]],
        "alumniOf": [{"@type": "CollegeOrUniversity" if e.get("college") else "Hospital", "name": e["name"]} for e in d["education"]],
        "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Board certification",
                           "name": c, "recognizedBy": {"@type": "Organization", "name": "American Board of Internal Medicine", "url": "https://www.abim.org/"}}
                          for c in d["board_certs"]],
        "knowsAbout": d["knows_about"],
        "address": postal_address(),
        "telephone": PRACTICE["tel"],
        "sameAs": d["same_as"],
    }
    if not full:
        return {"@id": DOC_ID}
    return node


def website_node():
    return {"@type": "WebSite", "@id": SITE_ID, "url": BASE + "/", "name": PRACTICE["name"],
            "alternateName": PRACTICE["alt_names"], "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"}


def breadcrumb_node(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": url(path)} for i, (name, path) in enumerate(trail)]}


def faq_node(pairs, page_url):
    return {"@type": "FAQPage", "@id": page_url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)}} for q, ans in pairs]}


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def graph(*nodes):
    return {"@context": "https://schema.org", "@graph": [n for n in nodes if n]}


# --------------------------------------------------------------------------
# document(): every page passes through here. Cross-cutting rules live here.
# --------------------------------------------------------------------------
PAGES = []  # (slug, title, description, html) — filled by write_page()
SEEN_TITLES = {}


JS_FLAG = "document.documentElement.classList.add('js')"
GA_INLINE = ("window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
             "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'});"
             "gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',false);")
INLINE_SCRIPTS_INIT = [JS_FLAG]


def analytics_tags(allow):
    if not allow:
        return ""
    out = []
    if GA4_ID:
        # Consent Mode v2: everything denied until the visitor accepts.
        INLINE_SCRIPTS.add(GA_INLINE)
        out.append('<script>%s</script>\n<script defer src="%s" data-ga="%s"></script>' % (GA_INLINE, a("assets/js/consent.js"), esc(GA4_ID)))
    if VERCEL_ANALYTICS:
        out.append('<script defer src="/_vercel/insights/script.js"></script>')
        out.append('<script defer src="/_vercel/speed-insights/script.js"></script>')
    return "\n".join(out)


_CSS = None


def inline_css():
    """The stylesheet, minified and inlined. One render-blocking request fewer
    on every first visit; ~9 KB gzipped. Font URLs become root-relative."""
    global _CSS
    if _CSS is None:
        css = open(os.path.join(PUB, "assets/css/site.css"), encoding="utf-8").read()
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        css = re.sub(r"\s+", " ", css)
        css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
        css = css.replace(";}", "}").replace("../fonts/", "/assets/fonts/")
        _CSS = css.strip()
    return _CSS


def document(slug, title, desc, body, *, schema=None, og_image=None, over_hero=False,
             extra_head="", scripts=(), track=True, noindex=False, canonical=True, preload=()):
    title = title.strip()
    if title in SEEN_TITLES:
        raise SystemExit("Duplicate <title> %r on %s and %s" % (title, SEEN_TITLES[title], slug))
    SEEN_TITLES[title] = slug
    desc = clamp_desc(desc)
    page_url = url(slug)
    og = og_image or "/assets/img/og/default-oct-2026.jpg"
    og_abs = og if og.startswith("http") else BASE + og.split("?")[0]
    css = inline_css()
    js = a("assets/js/main.js")
    preload_html = "".join(preload)
    ld = ""
    if schema:
        ld = '<script type="application/ld+json">%s</script>' % json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    script_tags = "".join('<script defer src="%s"></script>' % a(s) for s in scripts)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">'
    canon = '<link rel="canonical" href="%s">' % page_url if canonical else ""
    body_cls = "over-hero" if over_hero else ""
    return """<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
%(robots)s
%(canon)s
<meta name="theme-color" content="#0E0D0B">
<meta name="color-scheme" content="light">
<meta name="format-detection" content="telephone=no, address=no, email=no, date=no">
<link rel="preload" href="/assets/fonts/legacy-display-v1.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/legacy-sans-v1.woff2" as="font" type="font/woff2" crossorigin>
%(preload)s
<style>%(css)s</style>
<script>%(jsflag)s</script>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="Legacy Medical Blog" href="/blog/feed.xml">
<meta property="og:type" content="%(ogtype)s">
<meta property="og:site_name" content="Legacy Medical">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(og)s">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="%(ogalt)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(og)s">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="Palm Beach Gardens">
<meta name="geo.position" content="%(lat)s;%(lng)s">
<meta name="ICBM" content="%(lat)s, %(lng)s">
%(ld)s
%(extra)s
%(analytics)s
<script defer src="%(js)s"></script>
<script defer src="%(assist)s" data-faq="%(faq)s"></script>
%(scripts)s
</head>
<body class="%(bodycls)s">
%(header)s
<main id="main" tabindex="-1">
%(body)s
</main>
%(footer)s
%(callbar)s
</body>
</html>
""" % {"title": esc(title), "desc": esc(desc), "robots": robots, "canon": canon, "css": css, "js": js,
       "url": page_url, "og": esc(og_abs), "ogalt": esc(title), "ogtype": "article" if slug.startswith("blog/") and slug != "blog" else "website",
       "lat": PRACTICE["geo"]["lat"], "lng": PRACTICE["geo"]["lng"], "ld": ld, "extra": extra_head,
       "analytics": analytics_tags(track), "scripts": script_tags, "bodycls": body_cls,
       "header": header(slug), "body": body, "jsflag": JS_FLAG, "footer": footer(), "callbar": callbar(), "preload": preload_html,
       "assist": a("assets/js/assist.js"), "faq": a("assets/assist.json")}


def write_page(slug, title, desc, body, sitemap=True, **kw):
    out = "index.html" if slug == "" else (slug + "/index.html" if slug in ("blog",) else slug + ".html")
    path = os.path.join(PUB, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lastmod = kw.pop("lastmod_override", None)
    doc = document(slug, title, desc, body, **kw)
    doc = smart_quotes(doc)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    if sitemap and not kw.get("noindex"):
        PAGES.append({"slug": slug, "title": title, "desc": clamp_desc(desc), "lastmod": lastmod or SITE_UPDATED})
    return out


def smart_quotes(doc):
    """Curl straight quotes in visible text only (never inside tags, scripts or JSON)."""
    parts = re.split(r"(<script.*?</script>|<style.*?</style>|<[^>]+>)", doc, flags=re.S)
    for i, p in enumerate(parts):
        if i % 2 == 1 or not p.strip():
            continue
        p = p.replace("&#x27;", "'").replace("&quot;", '"')
        p = re.sub(r"(^|[\s(\[{>—–-])'", "\\1\u2018", p)
        p = p.replace("'", "\u2019")
        p = re.sub(r'(^|[\s(\[{>—–-])"', "\\1\u201c", p)
        p = p.replace('"', "\u201d")
        parts[i] = p
    return "".join(parts)


# --------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------
def crumbs_html(trail):
    items = []
    for i, (name, path) in enumerate(trail):
        if i == len(trail) - 1:
            items.append('<li aria-current="page">%s</li>' % esc(name))
        else:
            items.append('<li><a href="/%s">%s</a></li>' % (path, esc(name)))
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">%s</ol></nav>' % "".join(items)


def trail_for(slug, name):
    sec, href = section_of(slug)
    t = [("Home", "")]
    if sec and href and href != slug:
        t.append((sec, href))
    elif sec == "Patients" and slug != "patients":
        t.append(("For patients", "patients"))
    t.append((name, slug))
    return t


def page_hero(trail, eyebrow, h1, lede, media=None, cta=True, h1_html=None):
    btns = ""
    if cta:
        btns = ('<div class="btn-row"><a class="btn" href="/meet-and-greet" data-loc="page-hero">Book a meet and greet %s</a>'
                '<a class="btn ghost" href="tel:%s" data-loc="page-hero">Call %s</a></div>' % (icon("arrow"), PRACTICE["tel"], PRACTICE["phone"]))
    text = """<div>%s<p class="eyebrow">%s</p><h1>%s</h1>%s%s</div>""" % (
        crumbs_html(trail), esc(eyebrow), h1_html or esc(h1), ('<p class="lede">%s</p>' % lede) if lede else "", btns)
    if media:
        return '<section class="wrap page-hero with-media">%s<figure class="media" data-reveal="clip">%s</figure></section>' % (text, media)
    return '<section class="wrap page-hero">%s</section>' % text


def cta_band(heading=None, lede=None, night=True):
    p = PRACTICE
    heading = heading or "Meet Dr. Shtern <em>before you decide.</em>"
    lede = lede or ("Every membership starts with a complimentary meet and greet. Sit down with Dr. Shtern, see the office, "
                    "and ask whatever you like.")
    return """<section class="section cta-band%s" aria-labelledby="cta-h">
  <div class="wrap cta-grid">
    <div>
      <p class="eyebrow">Next step</p>
      <h2 id="cta-h" style="margin-top:1.25rem">%s</h2>
      <p class="lede">%s</p>
      <div class="btn-row"><a class="btn" href="/meet-and-greet" data-loc="cta-band">Book a meet and greet %s</a><a class="btn ghost" href="tel:%s" data-loc="cta-band">Call %s</a></div>
    </div>
    <nav class="towns" aria-label="Drive times to the office">
      <p class="towns-h">Drive times to the office</p>
      <ul>%s</ul>
      <a class="text-link" href="/areas-we-serve">All areas served %s</a>
    </nav>
  </div>
</section>""" % (" night" if night else " sunk", hx(heading), lede, icon("arrow"), p["tel"], p["phone"],
                  "".join('<li><a href="/areas/%s">%s<span>%d min</span></a></li>' % (l["slug"], esc(l["name"]), l["drive_min"])
                          for l in C.LOCATIONS[:6]), icon("arrow"))


def faq_html(pairs, heading_id=None):
    out = []
    for q, ans in pairs:
        out.append('<details><summary><span>%s</span><span class="pm" aria-hidden="true"></span></summary><div class="a">%s</div></details>' % (esc(q), ans))
    return '<div class="faq">%s</div>' % "".join(out)


def related_cards(slugs):
    cards = []
    lookup = {k[0]: k for _, _, kids in NAV if kids for k in kids}
    for s in slugs:
        k = lookup[s]
        cards.append('<div class="card"><p class="meta">%s</p><h3><a class="stretch" href="/%s" style="text-decoration:none;color:inherit">%s</a></h3><p>%s</p><span class="more">Read more %s</span></div>'
                     % ("Services" if s in [x[0] for x in NAV[1][2]] else ("For patients" if s in [x[0] for x in NAV[3][2]] else "Practice"), s, esc(k[1]), esc(C.CARD_BLURBS.get(s, k[2])), icon("arrow")))
    return '<div class="cards">%s</div>' % "".join(cards)


def reel_html():
    items = C.REEL
    if not items:
        return ""
    def group(hidden):
        imgs = "".join('<figure class="reel-item">%s</figure>' % photo(it["stem"], "" if hidden else it["alt"], sizes="(max-width: 760px) 70vw, 30vw", max_w=1200, decorative=hidden) for it in items)
        return '<div class="reel-group"%s>%s</div>' % (' aria-hidden="true"' if hidden else "", imgs)
    return """<section class="reel" aria-labelledby="reel-h">
  <div class="wrap reel-head">
    <div><p class="eyebrow">The practice</p><h2 id="reel-h" style="font-size:var(--step-3);margin-top:1rem">Inside Legacy Medical</h2></div>
    <button class="reel-pause" type="button" aria-pressed="false" aria-label="Pause photo reel">%s%s</button>
  </div>
  <div class="reel-track" tabindex="0" role="group" aria-label="Photos of the practice. Focus or hover to pause.">%s%s</div>
</section>""" % (ICONS["pause"], ICONS["play"].replace('class="i-play"', 'class="i-play" hidden'), group(False), group(True))


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
from pages import build_all  # noqa: E402  (page builders live beside this file)


def build_meta():
    # sitemap.xml
    rows = []
    for pg in PAGES:
        rows.append("  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (url(pg["slug"]), pg["lastmod"]))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % "\n".join(rows)
    open(os.path.join(PUB, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    # robots.txt
    robots = ("User-agent: *\nAllow: /\nDisallow: /api/\n\n"
              "# AI assistants may read the site to answer questions about the practice.\n"
              "User-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\n"
              "User-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
              "Sitemap: %s/sitemap.xml\n" % BASE)
    open(os.path.join(PUB, "robots.txt"), "w", encoding="utf-8").write(robots)
    # llms.txt
    open(os.path.join(PUB, "llms.txt"), "w", encoding="utf-8").write(C.llms_txt(PRACTICE, DOCTOR, PAGES, url))
    # manifest
    manifest = {"name": "Legacy Medical", "short_name": "Legacy Medical", "start_url": "/", "display": "browser",
                "background_color": "#0E0D0B", "theme_color": "#0E0D0B",
                "icons": [{"src": "/assets/img/og/logo-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "/assets/img/og/logo-512.png", "sizes": "512x512", "type": "image/png"}]}
    open(os.path.join(PUB, "site.webmanifest"), "w", encoding="utf-8").write(json.dumps(manifest, indent=2))


# --------------------------------------------------------------------------
# Copy rules, enforced. `--check` fails the build on any of these in visible
# text, so the house style cannot drift one page at a time.
# --------------------------------------------------------------------------
BANNED = [r"—", r"\bdelve", r"\belevate", r"\bjourney\b", r"\bseamless", r"\brobust\b", r"\bholistic",
          r"\bcutting-edge", r"\bstate-of-the-art", r"\bworld-class", r"\bnestled", r"\btestament to",
          r"\bunparalleled", r"\bcomprehensive\b", r"\bleverag", r"\btailored\b", r"\bempower",
          r"\bin today's\b", r"\bwhether you're\b", r"\bpeace of mind\b", r"\bnavigat", r"\bembark",
          r"\blorem\b", r"\bipsum\b", r"\bunlock", r"\bpivotal", r"\bmeticulous", r"\bbespoke\b", r"\bwellness journey"]


def visible_text(doc):
    doc = re.sub(r"<(script|style)\b.*?</\1>", " ", doc, flags=re.S)
    doc = re.sub(r"<[^>]+>", " ", doc)
    return html.unescape(doc)


def check_copy():
    problems = []
    for root, _, files in os.walk(PUB):
        if "/assets" in root:
            continue
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(root, fn)
            txt = visible_text(open(path, encoding="utf-8").read())
            # Migrated journal posts are checked for banned words but the
            # original authors' em dashes in quoted material are allowed.
            for pat in BANNED:
                for m in re.finditer(pat, txt, flags=re.I):
                    ctx = txt[max(0, m.start() - 40): m.end() + 40].replace("\n", " ")
                    problems.append("%s: %r in …%s…" % (os.path.relpath(path, PUB), m.group(0), ctx.strip()))
    return problems


INLINE_SCRIPTS = {JS_FLAG}  # every inline <script> body, hashed into the CSP


def csp():
    hashes = " ".join("'sha256-%s'" % __import__("base64").b64encode(hashlib.sha256(s.encode()).digest()).decode() for s in sorted(INLINE_SCRIPTS))
    return "; ".join([
        "default-src 'self'",
        "script-src 'self' %s https://www.googletagmanager.com" % hashes,
        "style-src 'self' 'unsafe-inline'",
        "img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com",
        "font-src 'self'",
        "media-src 'self'",
        "connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com",
        "frame-src https://www.google.com https://maps.google.com https://www.youtube-nocookie.com",
        "object-src 'none'",
        "base-uri 'self'",
        "form-action 'self'",
        "frame-ancestors 'self'",
        "upgrade-insecure-requests",
    ])


def build_vercel():
    import redirects as R
    rules = R.vercel_rules({**R.MAIN, **R.post_map("legacymedicalpalmbeach.com")}, R.MAIN_PATTERNS)
    # www -> apex. Two rules because "/:path*" does not match the bare root on Vercel.
    www = [{"source": "/", "has": [{"type": "host", "value": "www.legacymedicalpalmbeach.com"}], "destination": BASE + "/", "permanent": True},
           {"source": "/:path*", "has": [{"type": "host", "value": "www.legacymedicalpalmbeach.com"}], "destination": BASE + "/:path*", "permanent": True}]
    sec = [
        {"key": "X-Content-Type-Options", "value": "nosniff"},
        {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
        {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
        {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()"},
        {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains"},
        {"key": "Cross-Origin-Opener-Policy", "value": "same-origin"},
        {"key": "Content-Security-Policy", "value": csp()},
    ]
    cfg = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "buildCommand": "python3 build.py --check",
        "outputDirectory": "public",
        "installCommand": "",
        "framework": None,
        "cleanUrls": True,
        "trailingSlash": False,
        "headers": [
            {"source": "/(.*)", "headers": sec},
            {"source": "/assets/(css|js)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/assets/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/assets/(img|video)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800, stale-while-revalidate=86400"}]},
            {"source": "/(meet-and-greet|contact)", "headers": [{"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"}]},
            {"source": "/(llms.txt|robots.txt)", "headers": [{"key": "Content-Type", "value": "text/plain; charset=utf-8"}, {"key": "Cache-Control", "value": "public, max-age=3600"}]},
            {"source": "/api/(.*)", "headers": [{"key": "Cache-Control", "value": "no-store"}]},
            # The vercel.app aliases serve the same pages as the real domain: keep them out of search.
            {"source": "/(.*)", "has": [{"type": "host", "value": ".*\\.vercel\\.app"}],
             "headers": [{"key": "X-Robots-Tag", "value": "noindex"}]},
        ],
        "redirects": www + rules,
    }
    with open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")
    # cmedjupiter.com: the domain is not ours yet. Three ready-to-use forms.
    cm = {**R.CMED, **R.post_map("cmedjupiter.com")}
    d = os.path.join(ROOT, "_dev", "redirects")
    os.makedirs(d, exist_ok=True)
    vr = R.vercel_rules(cm, R.CMED_PATTERNS, absolute=True)
    json.dump({"redirects": vr}, open(os.path.join(d, "cmedjupiter.vercel.json"), "w"), indent=2)
    ht = ["# cmedjupiter.com -> legacymedicalpalmbeach.com (301).", "# Place at the top of the site root .htaccess, ABOVE the \"# BEGIN WordPress\" block.", "# NE keeps \"#reviews\" from being escaped to %23.", "RewriteEngine On"]
    for src, dst in sorted(cm.items(), key=lambda kv: -len(kv[0])):
        pat = "^" + re.escape(src.strip("/")) + "/?$" if src != "/" else "^$"
        ht.append("RewriteRule %s %s%s [R=301,L,NE]" % (pat, R.NEW, dst))
    ht.append("RewriteRule ^(category|tag|author)/ %s/blog [R=301,L]" % R.NEW)
    ht.append("RewriteRule ^\\d{4}/ %s/blog [R=301,L]" % R.NEW)
    ht.append("RewriteRule ^ %s/ [R=301,L]" % R.NEW)
    open(os.path.join(d, "cmedjupiter.htaccess"), "w").write("\n".join(ht) + "\n")
    rows = ["old_url,new_url"] + ["https://cmedjupiter.com%s,%s%s" % (k, R.NEW, v) for k, v in sorted(cm.items())]
    rows += ["https://legacymedicalpalmbeach.com%s,%s%s" % (k, R.NEW, v) for k, v in sorted({**R.MAIN, **R.post_map("legacymedicalpalmbeach.com")}.items())]
    open(os.path.join(d, "redirect-map.csv"), "w").write("\n".join(rows) + "\n")


def build_assist():
    """Everything the site assistant knows, written to assets/assist.json.

    faq: every question answered anywhere on the site (FAQ page, home, every
    service, town, guide and membership page) plus assistant-only answers.
    pages: every page and article with a one-line description, so a question
    with no set answer still gets pointed at the right page."""
    def plain(h):
        h = re.sub(r"</p>\s*<p>", " ", h)
        return re.sub(r"</?p>", "", h).strip()
    items, seen = [], set()
    def add(q, a, k=None, url_=None):
        key = re.sub(r"[^a-z0-9 ]", "", (q or a).lower()).strip()
        if key in seen:
            return
        seen.add(key)
        it = {"a": plain(a), "k": k or []}
        if q:
            it["q"] = q
        if url_ is not None:
            it["u"] = "/" + url_
        items.append(it)
    for g in C.FAQ_GROUPS:
        for q, a in g["pairs"]:
            if q not in C.ASSIST_KEYWORDS:
                raise SystemExit("assistant: no keywords for FAQ %r (add them to ASSIST_KEYWORDS)" % q)
            add(q, a, C.ASSIST_KEYWORDS[q], "faq")
    for l in C.LOCATIONS:
        add("How far is the office from %s?" % l["name"],
            "About %s miles from %s, roughly %s minutes without traffic. Usual route: %s. <a href=\"/areas/%s\">Concierge care near %s</a>." % (
                l["distance_mi"], l["from_label"], l["drive_min"], l["route"], l["slug"], l["name"]),
            [l["name"].lower(), "from " + l["name"].lower()])
    for x in C.ASSIST_EXTRA:
        add(None, x["a"], x["k"])
    sources = [("", C.HOME_FAQ), ("meet-and-greet", C.MEET["faqs"]), ("membership", C.MEMBERSHIP["faqs"]),
               ("insurance-and-fees", C.INSURANCE["faqs"]), ("concierge-medicine", C.CONCIERGE["faqs"])]
    sources += [(slug, s["faqs"]) for slug, s in C.SERVICE_PAGES.items()]
    sources += [(slug, s["faqs"]) for slug, s in C.GUIDES.items()]
    sources += [("areas/" + l["slug"], l.get("faqs", [])) for l in C.LOCATIONS]
    for slug, pairs in sources:
        for q, a in pairs:
            add(q, a, None, slug)
    pages = []
    for label, href, kids in NAV:
        for slug, name, sub in (kids or []):
            pages.append({"t": name, "u": "/" + slug, "d": C.CARD_BLURBS.get(slug, sub)})
    pages += [{"t": "Areas served", "u": "/areas-we-serve", "d": "Towns members come from, with drive times to the office."},
              {"t": "Contact and directions", "u": "/contact", "d": "Phone, address, hours and directions to the office."},
              {"t": "Blog", "u": "/blog", "d": "Articles on concierge medicine and health."}]
    pages += [{"t": "Concierge doctor near " + l["name"], "u": "/areas/" + l["slug"], "d": l["desc"]} for l in C.LOCATIONS]
    pages += [{"t": p["title"], "u": "/blog/" + p["slug"], "d": p["excerpt"]} for p in J.POSTS]
    p = PRACTICE
    data = {"phone": p["phone"], "tel": p["tel"], "email": p["email"],
            "hours": "Mon to Thu 9 to 5, Fri 9 to 2", "faq": items, "pages": pages}
    for it in items + pages:
        txt = visible_text(it.get("a", "") + " " + it.get("q", "") + " " + it.get("t", "") + " " + it.get("d", ""))
        for pat in BANNED:
            if re.search(pat, txt, flags=re.I):
                raise SystemExit("assistant text breaks copy rule %r: %s" % (pat, txt[:80]))
    with open(os.path.join(PUB, "assets", "assist.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

def main():
    build_assist()  # first, so pages can hash it
    build_all(sys.modules[__name__])
    build_meta()
    build_vercel()
    print("built %d pages" % len(PAGES))
    if "--check" in sys.argv:
        probs = check_copy()
        if probs:
            print("COPY RULES BROKEN (%d):" % len(probs))
            for p in probs[:80]:
                print("  " + p)
            sys.exit(1)
        print("copy rules: clean")


if __name__ == "__main__":
    main()
