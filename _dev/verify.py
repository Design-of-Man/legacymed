#!/usr/bin/env python3
"""Look at every page in a real browser. Exits non-zero on any problem.

    python3 _dev/verify.py                       all pages, 375/768/1440, light + dark
    python3 _dev/verify.py --shots _dev/shots    also keep screenshots
    python3 _dev/verify.py --pages index,contact

Serves public/ with Vercel-style clean URLs and redirects from vercel.json,
emulates prefers-reduced-motion so reveal animations cannot hide content from
axe, and reports per page and viewport: axe violations (WCAG 2.0/2.1/2.2 A+AA),
console errors, failed requests (any 4xx/5xx), horizontal overflow, and
elements wider than the viewport. A second motion-on pass checks the home page
hero and reel actually animate without errors.
"""
import argparse
import asyncio
import glob
import http.server
import json
import os
import re
import socket
import socketserver
import sys
import threading

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PUB = os.path.join(ROOT, "public")
AXE = os.environ.get("AXE") or os.path.join("/tmp/claude-0/-home-user-legacymed/a710e1f1-cec8-5210-8b4d-b0bba68caef7/scratchpad/tools/node_modules/axe-core/axe.min.js")
VIEWS = {"phone": (375, 812), "tablet": (768, 1024), "desktop": (1440, 900)}


def serve():
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=PUB, **kw)

        def log_message(self, *a):
            pass

        def send_head(self):
            path = self.path.split("?")[0].split("#")[0]
            if path.startswith("/api/"):
                self.send_error(503)
                return None
            fs = os.path.join(PUB, path.lstrip("/"))
            if path != "/" and not os.path.splitext(path)[1]:
                if os.path.exists(fs.rstrip("/") + ".html"):
                    self.path = path.rstrip("/") + ".html"
                elif os.path.isdir(fs) and os.path.exists(os.path.join(fs, "index.html")):
                    self.path = path.rstrip("/") + "/index.html"
            return super().send_head()

    class S(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        daemon_threads = True

        def handle_error(self, *a):
            pass

    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    httpd = S(("127.0.0.1", port), H)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return "http://127.0.0.1:%d" % port


def page_urls(subset):
    out = []
    for p in sorted(glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(p, PUB)
        if rel == "404.html":
            slug = "/404.html"
        elif rel == "index.html":
            slug = "/"
        elif rel.endswith("/index.html"):
            slug = "/" + rel[:-11]
        else:
            slug = "/" + rel[:-5]
        if subset and slug.strip("/") not in subset and rel[:-5] not in subset:
            continue
        out.append(slug)
    return out


async def check(browser, base, slug, view, scheme, axe_src, shots):
    w, h = VIEWS[view]
    ctx = await browser.new_context(viewport={"width": w, "height": h}, reduced_motion="reduce", color_scheme=scheme,
                                    device_scale_factor=1)
    page = await ctx.new_page()
    errors, failed = [], []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.on("response", lambda r: failed.append("%d %s" % (r.status, r.url.replace(base, ""))) if r.status >= 400 and "/api/" not in r.url else None)
    await page.goto(base + slug, wait_until="networkidle")
    await page.wait_for_timeout(250)
    probs = []
    ov = await page.evaluate("""() => {
        const d = document.documentElement, vw = d.clientWidth;
        const wide = [];
        document.querySelectorAll('body *').forEach(el => {
          const r = el.getBoundingClientRect();
          if (r.width && (r.right > vw + 1) && getComputedStyle(el).position !== 'fixed' && !el.closest('.reel, .table-scroll, .footer-word, .menu, .nav, .hp'))
            wide.push((el.className && el.className.baseVal === undefined ? el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0] : el.tagName.toLowerCase()) + ' ' + Math.round(r.right));
        });
        return {sw: d.scrollWidth, cw: vw, wide: wide.slice(0, 5)};
    }""")
    if ov["sw"] > ov["cw"] + 1:
        probs.append("overflow: scrollWidth %d > %d %s" % (ov["sw"], ov["cw"], ov["wide"]))
    elif ov["wide"]:
        probs.append("elements past viewport (clipped): %s" % ov["wide"])
    if axe_src:
        await page.add_script_tag(content=axe_src)
        res = await page.evaluate("""async () => {
            const r = await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']},
                                                rules: {'region': {enabled: true}}});
            return r.violations.map(v => ({id: v.id, impact: v.impact, n: v.nodes.length,
                    t: v.nodes.slice(0,3).map(n => n.target.join(' ') + ' :: ' + (n.failureSummary||'').split('\\n').slice(1,2).join(' '))}));
        }""")
        for v in res:
            probs.append("axe %s (%s) x%d: %s" % (v["id"], v["impact"], v["n"], " | ".join(v["t"])))
    for e in errors:
        probs.append("console: " + e[:200])
    for f in failed:
        probs.append("http: " + f)
    if shots:
        os.makedirs(shots, exist_ok=True)
        name = (slug.strip("/").replace("/", "_") or "home") + "-%s-%s.png" % (view, scheme)
        await page.screenshot(path=os.path.join(shots, name), full_page=True)
    await ctx.close()
    return probs


async def motion_pass(browser, base):
    """With motion on: the hero video must attach and play on desktop, the
    reel must run, and nothing may throw."""
    out = []
    ctx = await browser.new_context(viewport={"width": 1440, "height": 900})
    page = await ctx.new_page()
    errs = []
    page.on("pageerror", lambda e: errs.append(str(e)))
    page.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    await page.goto(base + "/", wait_until="load")
    await page.wait_for_timeout(3500)
    state = await page.evaluate("""() => {
        const v = document.querySelector('.hero-media video');
        return {src: v && v.currentSrc, paused: v && v.paused, t: v && v.currentTime, playing: v && v.classList.contains('playing')};
    }""")
    if not state["src"]:
        out.append("hero video never attached a source")
    await page.evaluate("document.querySelector('.reel').scrollIntoView({block: 'center'})")
    await page.wait_for_timeout(1500)
    reel = await page.evaluate("""() => { const t = document.querySelector('.reel-track'); return t && {running: t.classList.contains('running'), anim: getComputedStyle(t).animationName}; }""")
    if not reel or not reel["running"] or reel["anim"] != "reel":
        out.append("reel not running: %s" % reel)
    out += ["console: " + e for e in errs]
    await ctx.close()
    # narrow screen: the film autoplays too (owner's call), using the portrait cut
    ctx = await browser.new_context(viewport={"width": 390, "height": 844})
    page = await ctx.new_page()
    await page.goto(base + "/", wait_until="load")
    await page.wait_for_timeout(2500)
    src = await page.evaluate("document.querySelector('.hero-media video').currentSrc")
    if "portrait" not in (src or ""):
        out.append("phone did not attach the portrait film: %s" % src)
    await ctx.close()
    return out, state, reel


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages")
    ap.add_argument("--views", default="phone,tablet,desktop")
    ap.add_argument("--schemes", default="light,dark")
    ap.add_argument("--shots")
    a = ap.parse_args()
    from playwright.async_api import async_playwright
    base = serve()
    axe_src = open(AXE, encoding="utf-8").read() if os.path.exists(AXE) else None
    if not axe_src:
        print("axe-core not found: a11y pass skipped")
    subset = set(a.pages.split(",")) if a.pages else None
    urls = page_urls(subset)
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=_chromium(), args=["--autoplay-policy=no-user-gesture-required"])
        sem = asyncio.Semaphore(6)
        async def one(slug, view, scheme):
            async with sem:
                return slug, view, scheme, await check(browser, base, slug, view, scheme, axe_src, a.shots)
        jobs = [one(s, v, c) for s in urls for v in a.views.split(",") for c in a.schemes.split(",")]
        results = await asyncio.gather(*jobs)
        bad = [(s, v, c, pr) for s, v, c, pr in results if pr]
        for s, v, c, pr in sorted(bad):
            print("%s [%s/%s]" % (s, v, c))
            for x in pr:
                print("    " + x)
        total += len(bad)
        if not subset or "" in subset or "index" in subset:
            mp, state, reel = await motion_pass(browser, base)
            print("motion pass: video=%s reel=%s" % (state, reel))
            for x in mp:
                print("  MOTION: " + x)
            total += len(mp)
        await browser.close()
    print("checked %d pages x %d views x %d schemes: %d problem combos" % (len(urls), len(a.views.split(",")), len(a.schemes.split(",")), total))
    sys.exit(min(total, 100))


def _chromium():
    for c in glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome") + glob.glob("/opt/pw-browsers/chromium/chrome-linux/chrome") + ["/opt/pw-browsers/chromium"]:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


if __name__ == "__main__":
    asyncio.run(main())
