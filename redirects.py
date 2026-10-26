"""301 map from the two old WordPress sites to the new URLs.

MAIN applies to legacymedicalpalmbeach.com and is written into vercel.json.
CMED applies to cmedjupiter.com, the practice's older duplicate site; build.py
writes it to _dev/redirects/ in three forms (Vercel, Apache .htaccess, CSV)
because that domain is not yet under our control. Journal post mappings come
from journal_content.REDIRECTS so a slug can only be defined once.
"""
from urllib.parse import urlparse

import journal_content as J

NEW = "https://legacymedicalpalmbeach.com"

# old path (no trailing slash) -> new path
MAIN = {
    "/yana-shtern": "/dr-yana-shtern",
    "/meet-the-team": "/our-team",
    "/legacy-membership": "/membership",
    "/contact-us": "/contact",
    "/legacy-blog": "/blog",
    "/testimonials": "/#reviews",
    "/testimonials-lg": "/#reviews",
    "/privacy-policy": "/notice-of-privacy-practices",
    "/accessibility-statement": "/accessibility",
    "/home": "/",
    "/journal": "/blog",
}
# Patterns (Vercel path-to-regexp). Order matters: specific before general.
MAIN_PATTERNS = [
    ("/journal/feed.xml", "/blog/feed.xml"),
    ("/journal/:slug", "/blog/:slug"),
    ("/wws_portfolio/:path*", "/"),
    ("/wws_portfolio_category/:path*", "/"),
    ("/author/:path*", "/blog"),
    ("/category/:path*", "/blog"),
    ("/tag/:path*", "/blog"),
    ("/feed", "/blog/feed.xml"),
    ("/comments/feed", "/blog/feed.xml"),
    ("/:y(\\d{4})/:m(\\d{2})/:d(\\d{2})/:slug/feed", "/blog"),
    ("/:y(\\d{4})/:m(\\d{2})/:d(\\d{2})/:slug", "/blog"),
    ("/:y(\\d{4})/:m(\\d{2})", "/blog"),
    ("/:y(\\d{4})", "/blog"),
]

CMED = {
    "/": "/",
    "/dr-shtern": "/dr-yana-shtern",
    "/our-team": "/our-team",
    "/concierge-medicine": "/concierge-medicine",
    "/membership-benefits": "/membership",
    "/faq": "/faq",
    "/contact": "/contact",
    "/blog": "/blog",
    "/patient-testimonials": "/#reviews",
    "/privacy-policy": "/notice-of-privacy-practices",
    "/accessibility": "/accessibility",
    "/accessibility-statement": "/accessibility",
}
CMED_PATTERNS = MAIN_PATTERNS + [("/:path*", "/")]


def post_map(host):
    out = {}
    for old, new in J.REDIRECTS:
        u = urlparse(old)
        if u.netloc.replace("www.", "") == host:
            out[u.path.rstrip("/") or "/"] = new
    return out


def vercel_rules(exact, patterns, absolute=False, host=None, status=None):
    """status=None gives Vercel's permanent 308; pass 301 where a tool insists on it."""
    rules = []
    def add(src, dst):
        r = {"source": src, "destination": (NEW + dst) if absolute else dst}
        if status:
            r["statusCode"] = status
        else:
            r["permanent"] = True
        if host:
            r["has"] = [{"type": "host", "value": host}]
        rules.append(r)
    for src, dst in exact.items():
        add(src, dst)
        if src != "/":
            add(src + "/", dst)
    for src, dst in patterns:
        add(src, dst)
    return rules
