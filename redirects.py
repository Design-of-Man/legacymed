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
    "/legacy-blog": "/journal",
    "/testimonials": "/#reviews",
    "/testimonials-lg": "/#reviews",
    "/privacy-policy": "/notice-of-privacy-practices",
    "/accessibility-statement": "/accessibility",
    "/home": "/",
    "/blog": "/journal",
}
# Patterns (Vercel path-to-regexp). Order matters: specific before general.
# Coverage is checked by _dev/redirect_coverage.py against every old URL in
# _dev/redirects/old-urls.txt (both WordPress sitemaps, every internal link on
# every old page, and the ?p= shortlinks, crawled 2026-10-14). Run it after any
# change here; preflight runs it too.
MAIN_PATTERNS = [
    # Theme demo items ("01" to "04", one line of placeholder text each). There
    # is no equivalent page, so these, and only these, go to the home page.
    ("/wws_portfolio/:path*", "/"),
    ("/wws_portfolio_category/:path*", "/"),
    ("/author/:path*", "/journal"),
    ("/category/:path*", "/journal"),
    ("/tag/:path*", "/journal"),
    ("/legacy-blog/:path*", "/journal"),
    ("/blog/:path*", "/journal"),
    ("/:file(wp-sitemap.*\\.xml)", "/sitemap.xml"),
    ("/feed", "/journal/feed.xml"),
    ("/comments/feed", "/journal/feed.xml"),
    ("/:y(\\d{4})/:m(\\d{2})/:d(\\d{2})/:slug/feed", "/journal"),
    ("/:y(\\d{4})/:m(\\d{2})/:d(\\d{2})/:slug", "/journal"),
    ("/:y(\\d{4})/:m(\\d{2})/:d(\\d{2})", "/journal"),
    ("/:y(\\d{4})/:m(\\d{2})", "/journal"),
    ("/:y(\\d{4})", "/journal"),
]

CMED = {
    "/": "/",
    "/dr-shtern": "/dr-yana-shtern",
    "/our-team": "/our-team",
    "/concierge-medicine": "/concierge-medicine",
    "/membership-benefits": "/membership",
    "/faq": "/faq",
    "/contact": "/contact",
    "/blog": "/journal",
    "/patient-testimonials": "/#reviews",
    "/privacy-policy": "/notice-of-privacy-practices",
    "/accessibility": "/accessibility",
    "/accessibility-statement": "/accessibility",
}
CMED_PATTERNS = MAIN_PATTERNS + [("/:path*", "/")]

# Old legacymedicalpalmbeach.com pages whose address did not change, so they
# need no redirect (only their trailing-slash form, which Vercel handles).
SAME_PATH = {"/concierge-medicine", "/faq", "/accessibility"}

# WordPress shortlinks (/?p=ID), resolved against the live sites on 2026-10-14.
# Each ID points at the OLD path; the new destination is looked up from the
# maps above, so a page is only ever mapped in one place.
SHORTLINKS = {
    "legacymedicalpalmbeach.com": {
        2: "/yana-shtern", 3: "/privacy-policy", 498: "/wws_portfolio/01", 499: "/wws_portfolio/02",
        500: "/wws_portfolio/03", 501: "/wws_portfolio/04", 1285: "/2024/05/01/lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-faucibus",
        1287: "/2024/05/01/lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-faucibus-2",
        1292: "/2024/10/01/lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-faucibus-3",
        1776: "/concierge-medicine", 1972: "/legacy-membership", 2391: "/contact-us", 2410: "/legacy-blog",
        2428: "/testimonials", 2460: "/meet-the-team", 2743: "/testimonials-lg", 2760: "/faq", 3898: "/accessibility",
        3971: "/2024/05/01/safety-of-over-the-counter-meds", 3978: "/2024/10/07/vitamins-that-can-be-taken-in-the-morning",
        4003: "/2024/12/11/bananas-are-an-amazing-source-of-nutrition",
    },
    "cmedjupiter.com": {
        2: "/dr-shtern", 3: "/privacy-policy", 498: "/wws_portfolio/01", 499: "/wws_portfolio/02", 500: "/wws_portfolio/03",
        501: "/wws_portfolio/04", 755: "/2020/08/20/everything-you-need-to-know-about-executive-level-physical-exams",
        762: "/2020/09/14/how-concierge-medicine-works-with-your-hospitalization",
        766: "/2020/09/14/top-10-foods-that-promote-a-healthy-heart", 1087: "/2020/12/16/pandemic-fatigue-tips",
        1244: "/2021/11/01/cdc-booster-update",
        1285: "/2024/05/01/lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-faucibus",
        1287: "/2024/05/01/lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-faucibus-2",
        1292: "/2024/05/01/lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-faucibus-3",
        1345: "/2022/06/28/what-is-low-dose-computed-tomography", 1776: "/concierge-medicine", 1972: "/membership-benefits",
        2391: "/contact", 2410: "/blog", 2460: "/our-team", 2743: "/patient-testimonials", 2760: "/faq",
        3851: "/accessibility-statement", 3857: "/2020/08/11/covid-19-5-tips-on-how-to-avoid-spreading-the-virus",
        3858: "/2020/08/20/how-to-know-if-a-concierge-doctor-is-right-for-me", 3859: "/2020/10/14/arthritis-common-helpful-tips",
        3860: "/2020/10/14/the-best-method-to-washing-your-hands", 3861: "/2020/10/14/5-quick-tips-to-reduce-your-stress",
        3863: "/2020/11/18/what-is-concierge-medicine", 3865: "/2020/12/02/concierge-medicine-pros-and-cons",
        3866: "/2020/12/30/hair-loss-in-men-and-women", 3868: "/2021/01/25/what-is-hyperhidrosis",
        3869: "/2021/02/26/are-you-getting-enough-sleep-are-you-sleeping-too-much", 3870: "/2021/03/24/why-is-obesity-a-disease",
        3871: "/2021/04/09/fully-vaccinated-now-what", 3877: "/2021/05/11/is-cancer-preventable",
        3878: "/2021/07/07/mediterranean-diet-approach", 3879: "/2021/07/26/vitamin-supplementation",
        3880: "/2021/08/27/lets-talk-about-antibiotics-the-good-the-bad-and-the-ugly", 3881: "/2021/09/23/everyone-is-going-bananas",
        3882: "/2021/12/13/safety-of-over-the-counter-oral-pain-medications", 3884: "/2022/02/01/what-is-a-pulse-oximeter",
        3885: "/2022/03/30/potty-like-a-rockstar", 3886: "/2022/05/03/the-benefits-of-exercising",
        3887: "/2022/08/17/how-often-should-someone-urinate", 3888: "/2022/10/31/benefits-of-yearly-influenza-vaccination",
        3889: "/2022/12/27/rsv-infection-in-adults", 4083: "/accessibility",
    },
}


def shortlink_map(host, exact):
    """{post id: new path} for one old host, resolved through `exact`."""
    out = {}
    for pid, old in SHORTLINKS[host].items():
        if old in exact:
            out[pid] = exact[old]
        elif old in SAME_PATH:
            out[pid] = old
        elif old.startswith("/wws_portfolio/"):
            out[pid] = "/"
        else:
            raise SystemExit("redirects.py: shortlink %s?p=%d points at %s, which has no mapping" % (host, pid, old))
    return out


def shortlink_rules(smap, absolute=False):
    """Vercel rules for /?p=ID. They must come before any rule on "/"."""
    # On the same host a shortlink to "/" would loop (Vercel carries the query
    # string through), so those few just serve the home page.
    return [{"source": "/", "has": [{"type": "query", "key": "p", "value": str(pid)}],
             "destination": (NEW + dst) if absolute else dst, "permanent": True}
            for pid, dst in sorted(smap.items()) if absolute or dst.split("#")[0] != "/"]


def post_map(host):
    out = {}
    for old, new in J.REDIRECTS:
        u = urlparse(old)
        if u.netloc.replace("www.", "") == host:
            out[u.path.rstrip("/") or "/"] = new
    return out


def vercel_rules(exact, patterns, absolute=False, host=None):
    rules = []
    def add(src, dst):
        r = {"source": src, "destination": (NEW + dst) if absolute else dst, "permanent": True}
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
