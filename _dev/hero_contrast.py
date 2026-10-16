#!/usr/bin/env python3
"""Measure text-over-video contrast in the home hero.

The copy sits low on the left over the film, with a gradient shade behind it.
Hides the text, photographs the box it occupied, and compares the text
colour with the 98th-percentile brightest pixel behind it (the poster is the
video's first frame, so this is what visitors see before and during play).
Fails under 4.5:1."""
import asyncio, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify as V
from PIL import Image
from playwright.async_api import async_playwright

SEL = [(".hero-kicker", 4.5), (".hero-title", 3.0), (".hero-lede", 4.5), (".hero-facts dd", 4.5), (".hero-facts dt", 4.5)]

def lum(rgb):
    def f(c):
        c /= 255
        return c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)

async def main():
    base = V.serve()
    bad = 0
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=V._chromium())
        for w, h in [(1440, 900), (1280, 720), (390, 844), (375, 667)]:
            ctx = await b.new_context(viewport={"width": w, "height": h}, reduced_motion="reduce")
            pg = await ctx.new_page()
            await pg.goto(base + "/", wait_until="networkidle")
            colors = {}
            for sel, _ in SEL:
                colors[sel] = await pg.evaluate("s => getComputedStyle(document.querySelector(s)).color", sel)
            await pg.add_style_tag(content=".hero *{color:transparent!important;text-shadow:none!important;border-color:transparent!important} .hero .btn{visibility:hidden} .hero-toggle svg{visibility:hidden}")
            for sel, need in SEL:
                els = await pg.query_selector_all(sel)
                worst = 99
                for el in els:
                    box = await el.bounding_box()
                    if not box or box["width"] < 2 or not await el.is_visible():
                        continue
                    png = await pg.screenshot(clip=box, full_page=True)
                    im = Image.open(io.BytesIO(png)).convert("RGB")
                    ls = sorted(lum(px) for px in im.get_flattened_data())
                    l98 = ls[int(len(ls) * .98) - 1]
                    rgb = [int(x) for x in colors[sel].replace("rgba(", "").replace("rgb(", "").replace(")", "").split(",")[:3]]
                    lt = lum(rgb)
                    hi, lo = max(lt, l98), min(lt, l98)
                    worst = min(worst, (hi + .05) / (lo + .05))
                ok = worst >= need
                bad += not ok
                print("%4dx%-4d %-16s %5.2f:1 (need %.1f) %s" % (w, h, sel, worst, need, "ok" if ok else "FAIL"))
            await ctx.close()
        await b.close()
    sys.exit(bad)

asyncio.run(main())
