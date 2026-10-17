"""Page builders. Each function renders one page (or one family of pages)
from content.py / journal_content.py through build.document()."""
import html
import json
import os
import re

import content as C
import journal_content as J


def build_all(B):
    home(B)
    doctor(B)
    team(B)
    concierge(B)
    for slug in C.SERVICE_PAGES:
        service(B, slug)
    meet_and_greet(B)
    for slug in C.GUIDES:
        guide_page(B, slug)
    membership(B)
    insurance(B)
    faq(B)
    areas(B)
    for loc in C.LOCATIONS:
        location(B, loc)
    patients(B)
    journal(B)
    videos(B)
    contact(B)
    legal(B)
    not_found(B)


# ---------------------------------------------------------------- home
def home(B):
    P, D, H = B.PRACTICE, B.DOCTOR, C.HOME
    esc, icon, photo = B.esc, B.icon, B.photo

    # Poster is the LCP element: real <img>, eager, high priority, preloaded.
    v = C.HERO_VIDEO
    poster = ('<picture><source type="image/avif" media="(max-aspect-ratio: 4/5)" srcset="%(pa)s">'
              '<source type="image/webp" media="(max-aspect-ratio: 4/5)" srcset="%(pw)s">'
              '<source type="image/avif" srcset="%(a768)s 768w, %(a1280)s 1280w" sizes="100vw">'
              '<source type="image/webp" srcset="%(w768)s 768w, %(w1280)s 1280w" sizes="100vw">'
              '<img src="%(j1280)s" srcset="%(j768)s 768w, %(j1280)s 1280w" sizes="100vw" width="1280" height="720" '
              'alt="" fetchpriority="high" decoding="async"></picture>') % v["posters"]
    # No poster attribute: the <picture> underneath is the poster, so the
    # browser never fetches a second copy of the same frame.
    video = ('<video muted loop playsinline preload="none" aria-hidden="true" tabindex="-1" disablepictureinpicture '
             'data-uhd="%s" data-qhd="%s" data-hd="%s" data-portrait="%s"></video>' % (v["uhd"], v["qhd"], v["hd"], v["portrait"]))
    preload = ['<link rel="preload" as="image" type="image/avif" imagesrcset="%(a768)s 768w, %(a1280)s 1280w" imagesizes="100vw" media="(min-aspect-ratio: 4/5)" fetchpriority="high">' % v["posters"],
               '<link rel="preload" as="image" type="image/avif" href="%(pa)s" media="(max-aspect-ratio: 4/5)" fetchpriority="high">' % v["posters"]]

    title_lines = "".join('<span class="ln">%s</span>' % ln for ln in H["hero_lines"])
    # The film fills the screen; a compact block of copy sits low on the left (Elite-style).
    hero = """<section class="hero" aria-labelledby="hero-h">
  <div class="hero-media">%(poster)s%(video)s</div>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <h1 id="hero-h"><span class="hero-kicker">%(kicker)s</span><span class="hero-title">%(lines)s</span></h1>
      <p class="hero-lede">%(lede)s</p>
      <div class="btn-row">
        <a class="btn" href="/meet-and-greet" data-loc="hero">Book a meet and greet %(arrow)s</a>
        <a class="btn ghost" href="tel:%(tel)s" data-loc="hero">%(phoneico)s Call<span class="hide-sm"> %(phone)s</span></a>
      </div>
      <dl class="hero-facts">
        <div><dt>Physician</dt><dd><a href="/dr-yana-shtern">Dr. Yana Shtern, MD</a><br>Internal Medicine and Nephrology</dd></div>
        <div><dt>Office</dt><dd><a href="%(maps)s" rel="noopener" target="_blank">%(street)s<span class="sr-only"> (opens Google Maps)</span></a><br>%(city)s, FL %(postal)s</dd></div>
        <div><dt>Hours</dt><dd>Mon–Thu 9–5, Fri 9–2<br>Members: phone 24/7</dd></div>
      </dl>
    </div>
  </div>
  <div class="hero-ctl"><button class="hero-toggle" type="button" aria-pressed="false" hidden>%(play)s%(pause)s<span class="t">Play</span><span class="sr-only"> the Juno Beach film</span></button></div>
</section>""" % {"poster": poster, "video": video, "kicker": esc(H["kicker"]), "lines": title_lines, "lede": H["hero_lede"],
                 "arrow": icon("arrow"), "tel": P["tel"], "phone": P["phone"], "phoneico": icon("phone"),
                 "maps": esc(P["google_maps"]), "street": P["street_short"], "city": P["city"], "postal": P["postal"],
                 "play": B.ICONS["play"], "pause": B.ICONS["pause"].replace('class="i-pause"', 'class="i-pause" hidden')}

    problem = """<section class="section" aria-labelledby="problem-h">
  <div class="wrap split">
    <div>
      <p class="eyebrow">%s</p>
      <h2 id="problem-h" class="statement" data-fill style="margin-top:1.5rem">%s</h2>
    </div>
    <div>
      <p class="lede" data-reveal>%s</p>
      <ol class="problem-list" style="margin-top:2.5rem">%s</ol>
    </div>
  </div>
</section>""" % (esc(H["problem_eyebrow"]), B.words_spans(H["problem_statement"]), H["problem_lede"],
                  "".join('<li data-reveal style="--d:%d"><span class="n">%02d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i, i + 1, esc(t), d) for i, (t, d) in enumerate(H["problems"])))

    creds = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (esc(k), v) for k, v in D["home_creds"])
    q = C.TESTIMONIALS[0]
    guide = """<section class="section doc-feature" aria-labelledby="doc-h">
  <div class="wrap doctor">
    <figure class="cap-fig"><div class="doctor-photo" data-reveal="clip">%(photo)s</div><figcaption class="ph-cap">Dr. Yana Shtern, MD<span>Legacy Medical, Palm Beach Gardens</span></figcaption></figure>
    <div>
      <p class="eyebrow">Your physician</p>
      <h2 id="doc-h" class="doc-name">Dr. Yana Shtern, MD</h2>
      <p class="doc-role">Board-certified in Internal Medicine and Nephrology</p>
      <p class="doc-line">%(line)s</p>
      <div class="stack" style="margin-top:1.5rem;max-width:36rem">%(body)s</div>
      <dl class="creds">%(creds)s</dl>
      <blockquote class="doc-quote"><p>%(quote)s</p><footer>%(who)s, %(src)s</footer></blockquote>
      <div class="btn-row" style="margin-top:2rem"><a class="btn" href="/meet-and-greet" data-loc="doctor">Book a meet and greet %(arrow)s</a><a class="btn ghost" href="/dr-yana-shtern" data-loc="doctor">Her background</a></div>
    </div>
  </div>
</section>""" % {"photo": photo(D["photo"], "Dr. Yana Shtern, MD, at Legacy Medical in Palm Beach Gardens", sizes="(max-width: 880px) 90vw, 42vw", max_w=1200),
                 "line": esc(H["guide_h"]), "body": H["guide_body"], "creds": creds,
                 "quote": esc("She identified the cause of my problem rather than only trying to treat my symptoms as the other doctors I saw did."),
                 "who": "Patient review", "src": q["source_html"], "arrow": icon("arrow")}

    (m1, a1), (m2, a2) = H["manifesto_photos"]
    manifesto = """<section class="section manifesto" aria-labelledby="mani-h">
  <div class="wrap mani-grid">
    <figure class="mani-fig a"><div class="mani-ph" data-reveal="clip">%s</div><figcaption class="ph-cap">The front desk<span>Prosperity Farms Road</span></figcaption></figure>
    <h2 id="mani-h" class="mani-text" data-fill>%s</h2>
    <figure class="mani-fig b"><div class="mani-ph" data-reveal="clip">%s</div><figcaption class="ph-cap">Legacy Medical<span>Palm Beach Gardens</span></figcaption></figure>
  </div>
</section>""" % (photo(m1, a1, sizes="(max-width: 880px) 44vw, 18vw", max_w=800), B.words_spans(H["manifesto"]),
                  photo(m2, a2, sizes="(max-width: 880px) 44vw, 18vw", max_w=800))

    def stat(s):
        src = '<cite>%s</cite>' % s[3] if len(s) > 3 else ""
        fig = esc(s[0])
        if " → " in s[0]:  # "before → after": the before figure sits small and muted
            a, b = s[0].split(" → ")
            fig = '<span class="was">%s →</span> %s' % (esc(a), esc(b))
        return '<li data-reveal><p class="fig">%s</p><p class="lab">%s</p><p class="note">%s%s</p></li>' % (fig, esc(s[1]), esc(s[2]), src)
    why = """<section class="section why" aria-labelledby="why-h">
  <div class="wrap">
    <div class="headline-row"><div><p class="eyebrow">The difference</p><h2 id="why-h" style="margin-top:1.25rem">%s</h2></div><p class="lede">%s</p></div>
    <ul class="ledger">%s</ul>
    <p class="small muted" style="margin-top:1.5rem">The 300, 8 and one-hour figures are Legacy Medical's own limits. Primary care averages: U.S. Government Accountability Office, <a class="inline-link" href="https://www.gao.gov/products/gao-05-929" rel="noopener">Physician Services: Concierge Care Characteristics</a> (2005); Neprash et al., <a class="inline-link" href="https://pubmed.ncbi.nlm.nih.gov/33301282/" rel="noopener">Measuring Primary Care Exam Length Using Electronic Health Record Data</a>, <em>Medical Care</em> (2021). <a class="inline-link" href="/concierge-vs-traditional-primary-care">Concierge and traditional care, side by side</a>.</p>
  </div>
</section>""" % (B.hx(H["why_h"]), H["why_lede"], "".join(stat(s) for s in H["why_stats"]))

    included = "".join('<li data-reveal style="--d:%d"><span class="num" aria-hidden="true">%02d</span><h3>%s</h3><p>%s</p></li>' % (i % 3, i + 1, esc(s["name"]), s["text"])
                       for i, s in enumerate(C.SERVICES_INCLUDED[:6]))
    inc = """<section class="section" aria-labelledby="inc-h">
  <div class="wrap">
    <div class="headline-row"><div><p class="eyebrow">Membership</p><h2 id="inc-h" style="margin-top:1.25rem">%s</h2></div><p class="lede">%s</p></div>
    <ul class="included">%s</ul>
    <div class="agreement" style="margin-top:2rem">%s<p>%s</p></div>
    <p style="margin-top:2rem"><a class="text-link" href="/concierge-medicine">How concierge medicine works here %s</a></p>
  </div>
</section>""" % (B.hx(H["included_h"]), H["included_lede"], included, B.ICONS["shield"], H["agreement"], icon("arrow"))

    clock = clock_section(B)

    pp, pa = H["personal_photo"]
    rows = "".join('<li data-reveal><span class="pn" aria-hidden="true">%02d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i + 1, esc(t), d) for i, (t, d) in enumerate(H["personal"]))
    personal = """<section class="section personal" aria-labelledby="pers-h">
  <div class="wrap pers-grid">
    <div class="pers-media">
      <figure class="cap-fig"><div class="pers-ph" data-reveal="clip">%s</div><figcaption class="ph-cap">Dr. Yana Shtern, MD<span>One on one, every visit</span></figcaption></figure>
    </div>
    <div class="pers-body">
      <p class="eyebrow">One on one</p>
      <h2 id="pers-h" style="margin-top:1.25rem">%s</h2>
      <p class="lede" style="margin-top:1.25rem">%s</p>
      <ol class="pers-list">%s</ol>
      <div class="btn-row" style="margin-top:2.5rem"><a class="btn" href="/meet-and-greet" data-loc="personal">Book a meet and greet %s</a><a class="text-link" href="/dr-yana-shtern">About Dr. Shtern %s</a></div>
    </div>
  </div>
</section>""" % (photo(pp, pa, sizes="(max-width: 880px) 90vw, 40vw", max_w=1200), B.hx(H["personal_h"]), H["personal_lede"], rows, icon("arrow"), icon("arrow"))

    specs = "".join("""<li><a href="/%s"><span class="n">%02d</span><h3>%s</h3><p>%s</p><span class="go" aria-hidden="true">%s</span></a></li>""" % (
        s, i + 1, esc(t), esc(d), icon("arrow")) for i, (s, t, d) in enumerate(H["specialties"]))
    spec = """<section class="section sunk" aria-labelledby="spec-h">
  <div class="wrap">
    <div class="headline-row"><div><p class="eyebrow">Areas of focus</p><h2 id="spec-h" style="margin-top:1.25rem">%s</h2></div><p class="lede">%s</p></div>
    <ul class="spec-list">%s</ul>
  </div>
</section>""" % (B.hx(H["spec_h"]), H["spec_lede"], specs)

    reviews = reviews_section(B)

    area_links = "".join('<a href="/areas/%s">%s <span class="t">%s min</span></a>' % (l["slug"], esc(l["name"]), l["drive_min"]) for l in C.LOCATIONS)
    areas_sec = """<section class="section tight" aria-labelledby="areas-h">
  <div class="wrap split even" style="align-items:end">
    <div><p class="eyebrow">Where patients come from</p><h2 id="areas-h" style="margin-top:1.25rem;font-size:var(--step-3)">%s</h2><p class="lede" style="margin-top:1.25rem">%s</p></div>
    <div><div class="area-links">%s<a href="/areas-we-serve">All areas served %s</a></div><p class="small muted" style="margin-top:1rem">Typical drive times from the office, without traffic.</p></div>
  </div>
</section>""" % (esc(H["areas_h"]), H["areas_lede"], area_links, icon("arrow"))

    hfaq = """<section class="section" aria-labelledby="hfaq-h">
  <div class="wrap split">
    <div class="sticky-head"><p class="eyebrow">FAQ</p><h2 id="hfaq-h" style="margin-top:1.25rem">Common questions</h2><p class="lede" style="margin-top:1.25rem">Short answers to what people ask first. The full list is on the FAQ page.</p><p style="margin-top:1.5rem"><a class="text-link" href="/faq">All questions and answers %s</a></p></div>
    %s
  </div>
</section>""" % (icon("arrow"), B.faq_html(C.HOME_FAQ))

    ig = ""
    if C.INSTAGRAM.get("url"):
        tiles = "".join('<figure class="ig-tile">%s</figure>' % photo(it["stem"], it["alt"], sizes="(max-width: 760px) 46vw, 22vw", max_w=800) for it in C.REEL[:4])
        ig = """<section class="section ig" aria-labelledby="ig-h">
  <div class="wrap">
    <div class="headline-row"><div><p class="eyebrow">Instagram</p><h2 id="ig-h" style="margin-top:1.25rem">Follow along</h2></div><a class="btn ghost" href="%s" rel="noopener" target="_blank">%s @%s<span class="sr-only"> on Instagram (opens in a new tab)</span></a></div>
    <a class="ig-grid" href="%s" rel="noopener" target="_blank" aria-label="Legacy Medical on Instagram (opens in a new tab)">%s</a>
  </div>
</section>""" % (esc(C.INSTAGRAM["url"]), B.ICONS["instagram"], esc(C.INSTAGRAM["handle"]), esc(C.INSTAGRAM["url"]), tiles)

    posts = J.POSTS[:3]
    journal_sec = """<section class="section sunk" aria-labelledby="j-h">
  <div class="wrap">
    <div class="headline-row"><div><p class="eyebrow">Blog</p><h2 id="j-h" style="margin-top:1.25rem">Notes from <em>the practice</em></h2></div><a class="text-link" href="/blog">All articles %s</a></div>
    <div class="post-row">%s</div>
  </div>
</section>""" % (icon("arrow"), "".join(post_card(B, p) for p in posts))

    stakes = """<section class="section" aria-labelledby="stakes-h">
  <div class="wrap split">
    <div><p class="eyebrow">Why it matters</p><h2 id="stakes-h" style="margin-top:1.25rem">%s</h2></div>
    <div class="stack lede" style="color:var(--ink-2)">%s</div>
  </div>
</section>""" % (esc(H["stakes_h"]), H["stakes_body"])

    body = hero + guide + manifesto + why + personal + inc + spec + reviews + hfaq + ig + journal_sec
    body += B.cta_band() + B.reel_html()  # the photo reel closes the page, just above the footer

    schema = B.graph(B.website_node(), B.clinic_node(), B.physician_node(full=True),
                     {"@type": "WebPage", "@id": B.url("") + "#webpage", "url": B.url(""), "name": C.HOME_TITLE,
                      "isPartOf": {"@id": B.SITE_ID}, "about": {"@id": B.ORG_ID}, "primaryImageOfPage": B.BASE + v["posters"]["j1280"],
                      "inLanguage": "en-US"}, B.faq_node(C.HOME_FAQ, B.url("")))
    B.write_page("", C.HOME_TITLE, C.HOME_DESC, body, schema=schema, og_image="/assets/img/og/home.jpg", preload=preload, over_hero=True)


def clock_section(B):
    """Signature: a 7-day ring. Office hours drawn in gold, member phone
    access as the full circle. Built from PRACTICE['hours'], so it cannot
    disagree with the footer or the schema."""
    import math
    hours = {d: (o, c) for d, o, c in B.PRACTICE["hours"]}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    cx = cy = 200
    r = 168
    total = 7 * 24
    def arc(start_h, end_h, radius):
        a0 = (start_h / total) * 2 * math.pi - math.pi / 2
        a1 = (end_h / total) * 2 * math.pi - math.pi / 2
        x0, y0 = cx + radius * math.cos(a0), cy + radius * math.sin(a0)
        x1, y1 = cx + radius * math.cos(a1), cy + radius * math.sin(a1)
        large = 1 if (end_h - start_h) > total / 2 else 0
        length = radius * (a1 - a0)
        return "M%.2f %.2fA%d %d 0 %d 1 %.2f %.2f" % (x0, y0, radius, radius, large, x1, y1), length
    parts, office_hours = [], 0
    k = 0
    for i, d in enumerate(days):
        base = i * 24
        pth, ln = arc(base + 0.15, base + 23.85, r)
        parts.append('<path class="day member" d="%s" style="--len:%.1f;--k:%d"/>' % (pth, ln, k)); k += 1
        if d in hours:
            o, c = hours[d]
            oh = int(o[:2]) + int(o[3:]) / 60
            ch = int(c[:2]) + int(c[3:]) / 60
            office_hours += ch - oh
            pth, ln = arc(base + oh, base + ch, r)
            parts.append('<path class="day office" d="%s" style="--len:%.1f;--k:%d"/>' % (pth, ln, k)); k += 1
        ang = ((base + 12) / total) * 2 * math.pi - math.pi / 2
        lx, ly = cx + (r + 26) * math.cos(ang), cy + (r + 26) * math.sin(ang)
        parts.append('<text class="lbl" x="%.1f" y="%.1f" text-anchor="middle" dominant-baseline="middle">%s</text>' % (lx, ly, d[:3]))
        tx0, ty0 = cx + (r - 14) * math.cos(base / total * 2 * math.pi - math.pi / 2), cy + (r - 14) * math.sin(base / total * 2 * math.pi - math.pi / 2)
        tx1, ty1 = cx + (r + 14) * math.cos(base / total * 2 * math.pi - math.pi / 2), cy + (r + 14) * math.sin(base / total * 2 * math.pi - math.pi / 2)
        parts.append('<line class="tick" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (tx0, ty0, tx1, ty1))
    office_hours = round(office_hours)
    rows = "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (d, ("%s – %s" % (B.fmt12(hours[d][0]), B.fmt12(hours[d][1]))) if d in hours else "Closed") for d in days)
    H = C.HOME
    return """<section class="section night clock-sec" aria-labelledby="clock-h">
  <div class="wrap clock-grid">
    <div>
      <p class="eyebrow">Access</p>
      <h2 id="clock-h" style="margin-top:1.25rem">%(h)s</h2>
      <p class="lede" style="margin-top:1.5rem">%(lede)s</p>
      <div class="clock-legend" aria-hidden="true"><span><i></i>Office open, %(oh)d hours a week</span><span><i class="m"></i>Member phone line, all 168</span></div>
      <table class="hours-table"><caption class="sr-only">Office hours</caption>%(rows)s</table>
    </div>
    <div class="clock" role="img" aria-label="A week drawn as a ring: the office is open %(oh)d of 168 hours, and members can reach the practice by phone at any hour.">
      <svg viewBox="-20 -20 440 440" aria-hidden="true" focusable="false"><circle class="track" cx="200" cy="200" r="168"/>%(parts)s</svg>
      <div class="clock-center"><span class="big">168</span><span class="cap">hours a week you can reach us</span></div>
    </div>
  </div>
</section>""" % {"h": B.esc(H["clock_h"]), "lede": H["clock_lede"], "oh": office_hours, "rows": rows, "parts": "".join(parts)}


def reviews_section(B):
    """Google reviews. The rating badge and the four quotes are a dated snapshot from the public
    listing (content.GOOGLE / GOOGLE_REVIEWS); main.js swaps in live Google data when /api/reviews
    is configured. No AggregateRating schema (preflight blocks self-serving stars)."""
    esc = B.esc
    G = C.GOOGLE
    quotes = "".join('<figure class="quote" data-reveal style="--d:%d"><blockquote><p>%s</p></blockquote><figcaption><b>%s</b> \u00b7 Google review \u00b7 %s</figcaption></figure>' % (
        i % 2, esc(t["quote"]), esc(t["who"]), esc(t["when"])) for i, t in enumerate(C.GOOGLE_REVIEWS[:4]))
    ratings = "".join('<li><a class="inline-link" href="%s" rel="noopener" target="_blank">%s<span class="sr-only"> (opens in a new tab)</span></a></li>' % (esc(r["url"]), esc(r["label"])) for r in C.RATING_LINKS)
    stars = '<span class="stars" aria-hidden="true">%s</span>' % (B.ICONS["star"] * 5)
    badge = ('<a class="rating-badge" href="%s" rel="noopener" target="_blank" data-live-badge><b>%s</b><span>%s<span class="sr-only">%s out of 5 stars, </span>'
             'Google rating from %d reviews<br><span class="small muted">As of %s</span></span><span class="sr-only"> (opens in a new tab)</span></a>') % (
        esc(G["url"]), esc(G["rating"]), stars, esc(G["rating"]), G["count"], esc(G["as_of"]))
    live_attr = ' data-live-reviews' if B.LIVE_REVIEWS else ""
    return """<section class="section surface" id="reviews" aria-labelledby="rev-h"%s>
  <div class="wrap">
    <div class="reviews-head">
      <div><p class="eyebrow">Patients</p><h2 id="rev-h" style="margin-top:1.25rem">%s</h2></div>
      %s
    </div>
    <div class="quotes" data-live-list>%s</div>
    <div style="margin-top:2.25rem;display:flex;flex-wrap:wrap;gap:1rem 2rem;align-items:center">
      <p class="small muted">%s</p>
      <ul class="pill-list" style="gap:.5rem 1.25rem">%s</ul>
    </div>
  </div>
</section>""" % (live_attr, B.hx(C.HOME["reviews_h"]), badge, quotes, C.HOME["reviews_note"], ratings)


def human_date(iso):
    import datetime
    d = datetime.date.fromisoformat(iso[:10])
    return d.strftime("%B %-d, %Y")


# ---------------------------------------------------------------- doctor
def doctor(B):
    D = B.DOCTOR
    esc, icon = B.esc, B.icon
    slug = "dr-yana-shtern"
    trail = [("Home", ""), ("Dr. Yana Shtern, MD", slug)]
    hero = B.page_hero(trail, "Internal Medicine · Nephrology", "Dr. Yana Shtern, MD", D["hero_lede"],
                       media=B.photo(D["photo"], "Portrait of Dr. Yana Shtern, MD", sizes="(max-width: 880px) 90vw, 40vw", eager=True, max_w=1200))
    facts = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (esc(k), v) for k, v in D["facts"])
    bio = "".join("<p>%s</p>" % p for p in D["bio"])
    timeline = "".join('<li><span class="tl-k">%s</span><h3>%s</h3><p>%s</p></li>' % (esc(a), esc(b), c) for a, b, c in D["timeline"])
    body = hero + """<section class="section flush-top"><div class="wrap split">
  <div><dl class="facts" style="grid-template-columns:1fr">%s</dl></div>
  <div class="prose">%s</div>
</div></section>
<section class="section sunk" aria-labelledby="train-h"><div class="wrap split"><div class="sticky-head"><p class="eyebrow">Training and experience</p><h2 id="train-h" style="margin-top:1.25rem">%s</h2></div>
<ol class="tl">%s</ol></div></section>
<section class="section" aria-labelledby="verify-h"><div class="wrap split"><div><p class="eyebrow">Check for yourself</p><h2 id="verify-h" style="margin-top:1.25rem">Credentials you can verify</h2></div>
<div class="prose"><p>%s</p><ul>%s</ul></div></div></section>
<section class="section surface" aria-labelledby="personal-h"><div class="wrap centered-note"><p class="eyebrow">Outside the office</p><h2 id="personal-h" style="margin-top:1.25rem">A little more about her</h2><p class="lede" style="margin-top:1.25rem">%s</p></div></section>
""" % (facts, bio, esc(D["training_h"]), timeline, D["verify_intro"],
       "".join('<li><a href="%s" rel="noopener" target="_blank">%s<span class="sr-only"> (opens in a new tab)</span></a>%s</li>' % (esc(u), esc(t), (" " + n) if n else "") for t, u, n in D["verify_links"]),
       D["personal"])
    body += B.cta_band("Meet Dr. Shtern before you join.")
    schema = B.graph(B.physician_node(full=True), B.clinic_node(),
                     {"@type": "ProfilePage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": D["page_title"],
                      "mainEntity": {"@id": B.DOC_ID}, "isPartOf": {"@id": B.SITE_ID}, "dateModified": B.SITE_UPDATED},
                     B.breadcrumb_node(trail))
    B.write_page(slug, D["page_title"], D["page_desc"], body, schema=schema, og_image="/assets/img/og/dr-yana-shtern.jpg")


def team(B):
    esc = B.esc
    slug = "our-team"
    trail = B.trail_for(slug, "Our team")
    hero = B.page_hero(trail, "Our team", C.TEAM_PAGE["h1"], C.TEAM_PAGE["lede"])
    cards = []
    for m in B.TEAM:
        img = B.photo(m["photo"], "Portrait of " + m["name"], sizes="(max-width: 880px) 90vw, 30vw", max_w=900) if m.get("photo") else ""
        cards.append("""<article class="doctor" style="align-items:start;margin-top:4rem">
  <figure class="doctor-photo" style="aspect-ratio:4/5">%s</figure>
  <div><p class="eyebrow">%s</p><h2 style="margin-top:1rem;font-size:var(--step-3)">%s</h2><div class="prose" style="margin-top:1.25rem">%s</div>%s</div>
</article>""" % (img, esc(m["role"]), esc(m["name"]), "".join("<p>%s</p>" % p for p in m["bio"]),
                 ('<p style="margin-top:1.5rem"><a class="text-link" href="%s">%s %s</a></p>' % (m["link"], esc(m["link_label"]), B.icon("arrow"))) if m.get("link") else ""))
    body = hero + '<section class="section flush-top"><div class="wrap">%s</div></section>' % "".join(cards) + B.cta_band()
    persons = []
    for m in B.TEAM:
        if m.get("is_doctor"):
            persons.append({"@id": B.DOC_ID})
        else:
            persons.append({"@type": "Person", "name": m["name"], "jobTitle": m["role"], "worksFor": {"@id": B.ORG_ID},
                            "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": c} for c in m.get("creds", [])]})
    schema = B.graph({"@type": "AboutPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": C.TEAM_PAGE["title"],
                      "about": {"@id": B.ORG_ID}, "mentions": persons, "isPartOf": {"@id": B.SITE_ID}}, B.breadcrumb_node(trail))
    B.write_page(slug, C.TEAM_PAGE["title"], C.TEAM_PAGE["desc"], body, schema=schema)


# ---------------------------------------------------------------- concierge
def concierge(B):
    esc, icon = B.esc, B.icon
    S = C.CONCIERGE
    slug = "concierge-medicine"
    trail = B.trail_for(slug, "Concierge medicine")
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"])
    sections = "".join(prose_section(B, i, h, b, slug) for i, (h, b) in enumerate(S["sections"]))
    included = "".join('<li>%s<h3>%s</h3><p>%s</p></li>' % (B.svc_icon(s["icon"]), esc(s["name"]), s["text"]) for s in C.SERVICES_INCLUDED)
    rows = "".join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % (esc(a), esc(b), esc(c)) for a, b, c in S["compare"])
    body = hero + """<section class="section flush-top" aria-labelledby="inc-h"><div class="wrap">
<div class="headline-row"><div><p class="eyebrow">Included in membership</p><h2 id="inc-h" style="margin-top:1.25rem">What membership includes</h2></div><p class="lede">%s</p></div>
<ul class="included">%s</ul></div></section>
<section class="section sunk" aria-labelledby="cmp-h"><div class="wrap"><div class="headline-row"><div><p class="eyebrow">Side by side</p><h2 id="cmp-h" style="margin-top:1.25rem">Concierge care and a typical practice</h2></div><p class="lede">%s</p></div>
<div class="table-scroll"><table class="compare"><caption class="sr-only">Comparison of concierge care at Legacy Medical and a typical high-volume practice</caption><thead><tr><th scope="col">Topic</th><th scope="col">Typical high-volume practice</th><th scope="col">Legacy Medical</th></tr></thead><tbody>%s</tbody></table></div></div></section>
%s""" % (S["included_lede"], included, S["compare_lede"], rows, sections)
    body += '<section class="section sunk" aria-labelledby="cfaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="cfaq-h" style="margin-top:1.25rem">About concierge medicine</h2></div>%s</div></section>' % B.faq_html(S["faqs"])
    body += '<section class="section" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h" style="font-size:var(--step-3);margin-bottom:2rem">Keep reading</h2>%s</div></section>' % B.related_cards(S["related"])
    body += B.cta_band()
    schema = B.graph(medical_webpage(B, slug, S["title"], S["desc"], S.get("about", []), specialty="PrimaryCare"),
                     B.faq_node(S["faqs"], B.url(slug)), B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema, og_image="/assets/img/og/concierge-medicine.jpg")


def prose_section(B, i, h, body_html, slug=None):
    """One titled section. Sections are numbered like chapters, and a section
    with a photo in C.SECTION_IMAGES becomes a split with the image on
    alternating sides."""
    cls = " sunk" if i % 2 else ""
    sid = "s-%s" % re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-")[:40]
    stem = C.SECTION_IMAGES.get(slug, {}).get(h) if slug else None
    n = '<p class="sec-n" aria-hidden="true">%02d</p>' % max(i, 1)
    if stem and stem in B.IMG:
        side = " flip" if i % 2 == 0 else ""
        img = B.photo(stem, B.IMG[stem].get("alt", ""), sizes="(max-width: 880px) 92vw, 46vw", max_w=1600)
        return ('<section class="section%s" aria-labelledby="%s"><div class="wrap media-split%s"><figure class="ms-img" data-reveal="clip">%s</figure>'
                '<div class="ms-text">%s<h2 id="%s" style="font-size:var(--step-3)">%s</h2><div class="prose" style="margin-top:1.25rem">%s</div></div></div></section>') % (
            cls, sid, side, img, n, sid, B.esc(h), body_html)
    return '<section class="section%s" aria-labelledby="%s"><div class="wrap split"><div>%s<h2 id="%s" style="font-size:var(--step-3)">%s</h2></div><div class="prose">%s</div></div></section>' % (cls, sid, n, sid, B.esc(h), body_html)


def medical_webpage(B, slug, title, desc, about, specialty=None):
    node = {"@type": "MedicalWebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": title, "description": B.clamp_desc(desc),
            "isPartOf": {"@id": B.SITE_ID}, "publisher": {"@id": B.ORG_ID}, "inLanguage": "en-US",
            "dateModified": B.SITE_UPDATED, "audience": {"@type": "Patient"},
            "about": [{"@type": "MedicalCondition", "name": a} if isinstance(a, str) else a for a in about] or {"@id": B.ORG_ID},
            "mentions": {"@id": B.DOC_ID}}
    if specialty:
        node["specialty"] = "https://schema.org/" + specialty
    return node


# ---------------------------------------------------------------- service pages
def service(B, slug):
    esc, icon = B.esc, B.icon
    S = C.SERVICE_PAGES[slug]
    trail = B.trail_for(slug, S["crumb"])
    media = B.photo(S["photo"], S["photo_alt"], sizes="(max-width: 880px) 90vw, 40vw", eager=True, max_w=1200) if S.get("photo") else None
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"], media=media)
    body = hero
    if S.get("points"):
        pts = "".join('<li>%s<h3>%s</h3><p>%s</p></li>' % (B.svc_icon(ic), esc(t), d) for ic, t, d in S["points"])
        body += '<section class="section flush-top" aria-labelledby="pts-h"><div class="wrap"><h2 id="pts-h" class="sr-only">At a glance</h2><ul class="included">%s</ul></div></section>' % pts
    body += "".join(prose_section(B, i + 1, h, b, slug) for i, (h, b) in enumerate(S["sections"]))
    if S.get("faqs"):
        body += '<section class="section%s" aria-labelledby="sfaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="sfaq-h" style="margin-top:1.25rem">%s</h2></div>%s</div></section>' % (
            " sunk" if len(S["sections"]) % 2 == 0 else "", esc(S.get("faq_h", "Common questions")), B.faq_html(S["faqs"]))
    body += '<section class="section" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h" style="font-size:var(--step-3);margin-bottom:2rem">Related care</h2>%s</div></section>' % B.related_cards(S["related"])
    body += B.cta_band(S.get("cta_h"))
    nodes = [medical_webpage(B, slug, S["title"], S["desc"], S.get("about", []), S.get("specialty")), B.breadcrumb_node(trail)]
    if S.get("faqs"):
        nodes.append(B.faq_node(S["faqs"], B.url(slug)))
    if S.get("service_node"):
        sn = dict(S["service_node"])
        sn.update({"provider": {"@id": B.ORG_ID}, "areaServed": {"@type": "City", "name": "Palm Beach Gardens, FL"}})
        nodes.append(sn)
    B.write_page(slug, S["title"], S["desc"], body, schema=B.graph(*nodes), og_image="/assets/img/og/%s.jpg" % slug)


# ---------------------------------------------------------------- membership + form
def tour_form(B, kind, heading_id):
    P = B.PRACTICE
    esc = B.esc
    reasons = ["A meet and greet with Dr. Shtern", "Membership questions", "Kidney or blood pressure care", "Care for a parent", "Something else"]
    opts = "".join('<option>%s</option>' % esc(r) for r in reasons)
    def field(fid, label, typ="text", req=False, auto="", hint="", full=False, extra=""):
        return ('<div class="field%s"><label for="%s">%s%s</label>%s<input id="%s" name="%s" type="%s"%s%s%s aria-describedby="%s-err%s"><p class="err" id="%s-err" hidden></p></div>' % (
            " full" if full else "", fid, esc(label), "" if req else ' <span class="muted">(optional)</span>',
            ('<p class="hint" id="%s-hint">%s</p>' % (fid, hint)) if hint else "", fid, fid, typ,
            " required" if req else "", (' autocomplete="%s"' % auto) if auto else "", extra, fid, (" %s-hint" % fid) if hint else "", fid))
    return """<form class="form" data-tour="%(kind)s" data-phone="%(phone)s" action="/api/tour" method="post" novalidate aria-labelledby="%(hid)s">
  <div class="notice full">%(info)s<p><strong>Please do not include medical details.</strong> This form is for setting up a meet and greet or a call. We will talk about your health in person or by phone.</p></div>
  %(name)s
  %(phone_f)s
  %(email)s
  <div class="field"><label for="reason">I'm interested in</label><select id="reason" name="reason">%(opts)s</select></div>
  <div class="field"><label for="contact_pref">Best way to reach me</label><select id="contact_pref" name="contact_pref"><option>Phone call</option><option>Email</option><option>Either</option></select></div>
  %(best)s
  <div class="field full"><label for="message">Anything else? <span class="muted">(optional, no medical details)</span></label><textarea id="message" name="message" maxlength="600" rows="3" aria-describedby="message-hint"></textarea><p class="hint" id="message-hint">For example: "I'm a seasonal resident" or "I'm asking for my mother."</p></div>
  <div class="hp" aria-hidden="true"><label for="company_website">Leave this empty</label><input id="company_website" name="company_website" type="text" tabindex="-1" autocomplete="off"></div>
  <div class="check full"><input id="no_medical" name="no_medical" type="checkbox" value="yes" required aria-describedby="no_medical-err"><label for="no_medical">I understand this form is not for medical questions or emergencies. In an emergency I will call 911.</label></div>
  <p class="err full" id="no_medical-err" hidden></p>
  <div class="btn-row full"><button class="btn" type="submit">Send request %(arrow)s</button><a class="btn ghost" href="tel:%(tel)s" data-loc="form">Or call %(phone)s</a></div>
  <p class="small muted full">The office will call or email you back. See our <a class="inline-link" href="/privacy">website privacy notice</a> for how we handle what you send.</p>
  <div class="form-status full" role="status" aria-live="polite" tabindex="-1" hidden></div>
</form>""" % {"kind": kind, "phone": P["phone"], "tel": P["tel"], "hid": heading_id, "info": B.ICONS["info"], "opts": opts, "arrow": B.icon("arrow"),
              "name": field("name", "Full name", req=True, auto="name"),
              "phone_f": field("phone", "Phone", typ="tel", auto="tel", hint="Phone or email, at least one."),
              "email": field("email", "Email", typ="email", auto="email"),
              "best": field("best_time", "Best time to reach you", hint="e.g. weekday mornings")}


def guide_page(B, slug):
    esc, icon = B.esc, B.icon
    S = C.GUIDES[slug]
    trail = B.trail_for(slug, S["crumb"])
    media = B.photo(S["photo"], S["photo_alt"], sizes="(max-width: 880px) 90vw, 45vw", max_w=1200) if S.get("photo") else None
    body = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"], media=media)
    if S.get("compare"):
        rows = "".join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % (esc(a), esc(b), esc(c)) for a, b, c in C.CONCIERGE["compare"])
        body += """<section class="section flush-top" aria-labelledby="cmp-h"><div class="wrap"><h2 id="cmp-h" style="font-size:var(--step-3);margin-bottom:1.5rem">At a glance</h2>
<div class="table-scroll"><table class="compare"><caption class="sr-only">Traditional primary care compared with concierge care at Legacy Medical</caption><thead><tr><th scope="col">Topic</th><th scope="col">Typical high-volume practice</th><th scope="col">Concierge care at Legacy Medical</th></tr></thead><tbody>%s</tbody></table></div></div></section>""" % rows
    body += "".join(prose_section(B, i + 1, h, b, slug) for i, (h, b) in enumerate(S["sections"]))
    body += '<section class="section%s" aria-labelledby="gfaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="gfaq-h" style="margin-top:1.25rem">Common questions</h2></div>%s</div></section>' % (
        " sunk" if len(S["sections"]) % 2 == 0 else "", B.faq_html(S["faqs"]))
    posts = {p["slug"]: p for p in J.POSTS}
    reads = [posts[s] for s in S.get("related_posts", []) if s in posts]
    if reads:
        cards = "".join('<a class="card" href="/blog/%s"><p class="meta">%s</p><h3>%s</h3><p>%s</p><span class="more">Read %s</span></a>' % (
            p["slug"], esc(p["category"]), esc(p["title"]), esc(p["excerpt"]), icon("arrow")) for p in reads[:3])
        body += '<section class="section" aria-labelledby="gread-h"><div class="wrap"><h2 id="gread-h" style="font-size:var(--step-3);margin-bottom:2rem">From the blog</h2><div class="cards">%s</div></div></section>' % cards
    body += '<section class="section sunk" aria-labelledby="grel-h"><div class="wrap"><h2 id="grel-h" style="font-size:var(--step-3);margin-bottom:2rem">Related</h2>%s</div></section>' % B.related_cards(S["related"])
    body += B.cta_band()
    schema = B.graph({"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": S["title"], "description": S["desc"],
                      "isPartOf": {"@id": B.SITE_ID}, "about": {"@id": B.ORG_ID}, "inLanguage": "en-US"},
                     B.faq_node(S["faqs"], B.url(slug)), B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema)


def membership(B):
    esc, icon = B.esc, B.icon
    S = C.MEMBERSHIP
    slug = "membership"
    trail = B.trail_for(slug, "How to join")
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"], cta=False)
    steps = "".join('<li><h3>%s</h3><p>%s</p></li>' % (esc(t), d) for t, d in S["steps"])
    body = hero + """<section class="section flush-top" aria-labelledby="steps-h"><div class="wrap"><h2 id="steps-h" class="sr-only">Steps to join</h2><ol class="steps">%s</ol>
<div class="agreement">%s<p>%s</p></div></div></section>""" % (steps, B.ICONS["shield"], S["agreement"])
    body += "".join(prose_section(B, i + 1, h, b, slug) for i, (h, b) in enumerate(S["sections"]))
    body += """<section class="section sunk" id="tour" aria-labelledby="tour-h"><div class="wrap split" style="align-items:center">
<div><p class="eyebrow">First step</p><h2 id="tour-h" style="margin-top:1.25rem">Start with a meet and greet.</h2><p class="lede" style="margin-top:1.25rem">A complimentary conversation with Dr. Shtern at the office. Ask anything, then decide in your own time.</p></div>
<div class="btn-row"><a class="btn" href="/meet-and-greet" data-loc="membership">Book a meet and greet %s</a><a class="btn ghost" href="tel:%s" data-loc="membership">Call %s</a></div></div></section>""" % (icon("arrow"), B.PRACTICE["tel"], B.PRACTICE["phone"])
    body += '<section class="section" aria-labelledby="mfaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="mfaq-h" style="margin-top:1.25rem">About joining</h2></div>%s</div></section>' % B.faq_html(S["faqs"])
    schema = B.graph({"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": S["title"], "isPartOf": {"@id": B.SITE_ID},
                      "about": {"@id": B.ORG_ID}, "potentialAction": {"@type": "ReserveAction", "name": "Book a meet and greet", "target": B.url("meet-and-greet") + "#request"}},
                     B.faq_node(S["faqs"], B.url(slug)), B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema, og_image="/assets/img/og/membership.jpg")


def patients(B):
    esc, icon = B.esc, B.icon
    S = C.PATIENTS_PAGE
    slug = "patients"
    trail = B.trail_for(slug, "For patients")
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"], cta=False,
                       media=B.photo("front-desk-scrubs", "A member of the Legacy Medical team at the front desk", sizes="(max-width: 880px) 90vw, 45vw", max_w=1200))
    rows = "".join('<li data-reveal><span class="pn" aria-hidden="true">%02d</span><div><h3>%s</h3><p>%s</p><a class="text-link" href="/%s">%s %s</a></div></li>'
                   % (i + 1, esc(t), esc(d), esc(href), esc(lbl), icon("arrow")) for i, (t, d, href, lbl) in enumerate(S["guide"]))
    guide = """<section class="section flush-top" aria-labelledby="pg-h"><div class="wrap split"><div class="sticky-head"><p class="eyebrow">The practical guide</p>
<h2 id="pg-h" style="margin-top:1.25rem">How things <em>work here</em></h2><p class="lede" style="margin-top:1.25rem">Short answers to what new and current members ask most. Anything else, call (561) 834-9280.</p></div>
<ol class="pers-list pg-list">%s</ol></div></section>""" % rows
    learn = """<section class="section sunk" aria-labelledby="learn-h"><div class="wrap">
<div class="headline-row"><div><p class="eyebrow">Learn</p><h2 id="learn-h" style="margin-top:1.25rem">Read, watch, <em>ask</em></h2></div><p class="lede">Articles and videos on the questions members bring to their visits.</p></div>
<div class="learn-grid">
<a class="learn-card" href="/blog"><span class="eyebrow">Blog</span><h3>Articles on concierge care, the heart, kidneys, prevention and healthy aging</h3><span class="text-link">Read the blog %(a)s</span></a>
<a class="learn-card" href="/videos"><span class="eyebrow">Videos</span><h3>A film from the practice and trusted explainers from public health organizations</h3><span class="text-link">Watch the videos %(a)s</span></a>
<a class="learn-card" href="/faq"><span class="eyebrow">FAQ</span><h3>Straight answers on access, fees, insurance, labs and hospitals</h3><span class="text-link">Read the FAQ %(a)s</span></a>
</div></div></section>""" % {"a": icon("arrow")}
    docs = """<section class="section" aria-labelledby="docs-h"><div class="wrap split even"><div><p class="eyebrow">Privacy and policies</p><h2 id="docs-h" style="margin-top:1.25rem;font-size:var(--step-3)">Your information</h2></div>
<div class="towns"><ul><li><a href="/notice-of-privacy-practices">Notice of Privacy Practices<span>HIPAA</span></a></li><li><a href="/privacy">Website privacy<span>This site</span></a></li><li><a href="/accessibility">Accessibility<span>Our commitment</span></a></li></ul></div></div></section>"""
    body = hero + guide + learn + docs + B.cta_band()
    schema = B.graph({"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": S["title"], "description": S["desc"],
                      "isPartOf": {"@id": B.SITE_ID}, "about": {"@id": B.ORG_ID}, "inLanguage": "en-US"}, B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema)


def video_facade(B, v, sizes, eager=False):
    """A poster button that swaps in the YouTube player (privacy-enhanced
    domain) only when pressed. The poster is our own copy of the thumbnail."""
    return ('<div class="vid" data-yt="%s" data-title="%s"><button class="vid-play" type="button">%s'
            '<span class="vid-btn" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></span>'
            '<span class="sr-only">Play video: %s (loads YouTube)</span></button></div>'
            % (B.esc(v["id"]), B.esc(v["title"]), B.photo("v-" + v["id"], "", sizes=sizes, decorative=True, eager=eager),
               B.esc(v["title"])))


def videos(B):
    esc, icon = B.esc, B.icon
    S = C.VIDEOS_PAGE
    slug = "videos"
    trail = B.trail_for(slug, "Videos")
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"], cta=False)
    films = ""
    for v in C.PRACTICE_FILMS:
        films += """<section class="section flush-top" aria-labelledby="film-%(id)s"><div class="wrap film-grid">
<figure class="film">%(vid)s<figcaption class="ph-cap">%(t)s<span>From the practice</span></figcaption></figure>
<div><p class="eyebrow">From the practice</p><h2 id="film-%(id)s" style="margin-top:1.25rem">Meet <em>Dr. Shtern</em></h2>
<p class="lede" style="margin-top:1.25rem">%(s)s</p>
<div class="btn-row" style="margin-top:2rem"><a class="btn" href="/meet-and-greet" data-loc="videos">Book a meet and greet %(a)s</a><a class="text-link" href="/dr-yana-shtern">About Dr. Shtern %(a)s</a></div></div>
</div></section>""" % {"id": esc(v["id"]), "vid": video_facade(B, v, "(max-width: 880px) 92vw, 58vw", eager=True),
                       "t": esc(v["title"]), "s": esc(v["summary"]), "a": icon("arrow")}
    lib = ""
    if C.VIDEO_LIBRARY:
        cards = ""
        for v in C.VIDEO_LIBRARY:
            rel = ('<a class="text-link" href="/%s">Read more %s</a>' % (esc(v["related"]), icon("arrow"))) if v.get("related") else ""
            cards += ('<li class="vcard">%s<p class="pc-meta"><span class="cat">%s</span><span>%s</span></p><h3>%s</h3><p class="pc-ex">%s</p>%s</li>'
                      % (video_facade(B, v, "(max-width: 700px) 92vw, (max-width: 1100px) 45vw, 30vw"), esc(v["topic"]), esc(v["channel"]),
                         esc(v["title"]), esc(v["summary"]), rel))
        groups = '<ul class="vgrid">%s</ul>' % cards
        lib = """<section class="section sunk" aria-labelledby="lib-h"><div class="wrap">
<div class="headline-row"><div><p class="eyebrow">Library</p><h2 id="lib-h" style="margin-top:1.25rem">%s</h2></div><p class="lede">%s</p></div>
%s</div></section>""" % (B.hx(S["library_h"]), esc(S["library_lede"]), groups)
    body = hero + films + lib + B.cta_band("Questions after watching?", "Bring them to a complimentary meet and greet with Dr. Shtern, or call the office.")
    schema = B.graph({"@type": "CollectionPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": S["title"],
                      "isPartOf": {"@id": B.SITE_ID}, "about": {"@id": B.ORG_ID}}, B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema)


def meet_and_greet(B):
    esc, icon = B.esc, B.icon
    S = C.MEET
    slug = "meet-and-greet"
    trail = B.trail_for(slug, "Meet and greet")
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"], cta=False,
                       media=B.photo("dr-shtern-desk", "Dr. Yana Shtern at her desk at Legacy Medical", sizes="(max-width: 880px) 90vw, 45vw", max_w=1200))
    steps = "".join('<li><h3>%s</h3><p>%s</p></li>' % (esc(t), d) for t, d in S["steps"])
    body = hero + """<section class="section flush-top" aria-labelledby="steps-h"><div class="wrap"><h2 id="steps-h" class="sr-only">How it works</h2><ol class="steps">%s</ol>
<p style="margin-top:2rem"><a class="btn" href="#request" data-loc="meet-steps">Book a meet and greet %s</a></p></div></section>""" % (steps, icon("arrow"))
    body += "".join(prose_section(B, i + 1, h, b, slug) for i, (h, b) in enumerate(S["sections"]))
    body += """<section class="section sunk" id="request" aria-labelledby="request-h"><div class="wrap split">
<div><p class="eyebrow">Book</p><h2 id="request-h" style="margin-top:1.25rem">%s</h2><p class="lede" style="margin-top:1.25rem">%s</p>
<dl class="facts" style="margin-top:2rem;grid-template-columns:1fr"><div><dt>Phone</dt><dd><a href="tel:%s" data-loc="meet">%s</a></dd></div><div><dt>Office</dt><dd>%s<br>%s, FL %s</dd></div><div><dt>Office hours</dt><dd>Mon to Thu 9 AM to 5 PM, Fri 9 AM to 2 PM</dd></div></dl></div>
<div class="panel">%s</div></div></section>""" % (esc(S["form_h"]), S["form_lede"], B.PRACTICE["tel"], B.PRACTICE["phone"], B.PRACTICE["street_short"], B.PRACTICE["city"], B.PRACTICE["postal"], tour_form(B, "meet-and-greet", "request-h"))
    body += '<section class="section" aria-labelledby="mgfaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="mgfaq-h" style="margin-top:1.25rem">About the meet and greet</h2></div>%s</div></section>' % B.faq_html(S["faqs"])
    schema = B.graph({"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": S["title"], "isPartOf": {"@id": B.SITE_ID},
                      "about": {"@id": B.ORG_ID}, "mentions": {"@id": B.DOC_ID},
                      "potentialAction": {"@type": "ReserveAction", "name": "Book a meet and greet", "target": B.url(slug) + "#request"}},
                     B.faq_node(S["faqs"], B.url(slug)), B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema, scripts=("assets/js/tour.js",), track=False, og_image="/assets/img/og/membership.jpg")


def insurance(B):
    esc = B.esc
    S = C.INSURANCE
    slug = "insurance-and-fees"
    trail = B.trail_for(slug, "Insurance and fees")
    hero = B.page_hero(trail, S["eyebrow"], S["h1"], S["lede"])
    body = hero + "".join(prose_section(B, i, h, b, slug) for i, (h, b) in enumerate(S["sections"]))
    body += '<section class="section sunk" aria-labelledby="ifaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="ifaq-h" style="margin-top:1.25rem">Insurance and fee questions</h2></div>%s</div></section>' % B.faq_html(S["faqs"])
    body += B.cta_band("Ask us about the fee in person.", S["cta_lede"])
    schema = B.graph({"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": S["title"], "isPartOf": {"@id": B.SITE_ID}, "about": {"@id": B.ORG_ID}},
                     B.faq_node(S["faqs"], B.url(slug)), B.breadcrumb_node(trail))
    B.write_page(slug, S["title"], S["desc"], body, schema=schema)


def faq(B):
    esc = B.esc
    slug = "faq"
    trail = B.trail_for(slug, "FAQ")
    hero = B.page_hero(trail, "FAQ", C.FAQ_PAGE["h1"], C.FAQ_PAGE["lede"], cta=False)
    groups = ""
    all_pairs = []
    for g in C.FAQ_GROUPS:
        all_pairs += g["pairs"]
        gid = "g-" + re.sub(r"[^a-z]+", "-", g["name"].lower()).strip("-")
        groups += '<div class="faq-group"><h2 id="%s">%s</h2>%s</div>' % (gid, esc(g["name"]), B.faq_html(g["pairs"]))
    body = hero + """<section class="section flush-top"><div class="wrap" style="max-width:62rem">
<div class="faq-search field"><label for="faq-q">Search the questions</label><input id="faq-q" type="search" autocomplete="off" placeholder="Try Medicare, labs, or after hours"><p class="small muted" id="faq-status" role="status" aria-live="polite"></p></div>
%s</div></section>""" % groups + B.cta_band("Still have a question? Call us.")
    schema = B.graph(B.faq_node(all_pairs, B.url(slug)), B.breadcrumb_node(trail))
    B.write_page(slug, C.FAQ_PAGE["title"], C.FAQ_PAGE["desc"], body, schema=schema)


# ---------------------------------------------------------------- areas
def areas(B):
    esc, icon = B.esc, B.icon
    slug = "areas-we-serve"
    A = C.AREAS_PAGE
    trail = [("Home", ""), ("Areas served", slug)]
    hero = B.page_hero(trail, "Areas served", A["h1"], A["lede"])
    rows = "".join('<tr><th scope="row">%s</th><td class="tabular">%s mi</td><td class="tabular">%s min</td><td>%s</td><td>%s</td></tr>' % (
        ('<a class="inline-link" href="/areas/%s">%s</a>' % (l["slug"], esc(l["name"]))) if l.get("slug") else esc(l["name"]),
        l["distance_mi"], l["drive_min"], esc(l["route_short"]), esc(l["hospital_short"])) for l in C.ALL_AREAS)
    body = hero + """<section class="section flush-top" aria-labelledby="tbl-h"><div class="wrap">
<h2 id="tbl-h" style="font-size:var(--step-3);margin-bottom:1.5rem">Drive times from the office</h2>
<div class="table-scroll"><table class="compare"><caption class="sr-only">Distance and typical drive time from Legacy Medical to nearby towns</caption><thead><tr><th scope="col">Town</th><th scope="col">Distance</th><th scope="col">Drive</th><th scope="col">Usual route</th><th scope="col">Nearer affiliated hospital</th></tr></thead><tbody>%s</tbody></table></div>
<p class="small muted" style="margin-top:1rem">%s</p></div></section>""" % (rows, A["method_note"])
    body += "".join(prose_section(B, i + 1, h, b, "areas-we-serve") for i, (h, b) in enumerate(A["sections"]))
    body += """<section class="section" aria-labelledby="map-h"><div class="wrap split"><div><h2 id="map-h" style="font-size:var(--step-3)">Find the office</h2><p class="lede" style="margin-top:1rem">%s</p></div>%s</div></section>""" % (A["map_lede"], map_card(B))
    body += B.cta_band()
    schema = B.graph({"@type": "CollectionPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": A["title"], "isPartOf": {"@id": B.SITE_ID},
                      "about": {"@id": B.ORG_ID}, "hasPart": [{"@type": "WebPage", "url": B.url("areas/" + l["slug"]), "name": l["title"]} for l in C.LOCATIONS]},
                     B.breadcrumb_node(trail))
    B.write_page(slug, A["title"], A["desc"], body, schema=schema)


def map_card(B):
    P = B.PRACTICE
    return """<div class="map-card"><div class="map-frame"><iframe src="%s" title="Map showing Legacy Medical in Palm Beach Gardens" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<div class="body"><p><strong>%s</strong><br>%s, %s %s</p><p class="small muted" style="margin-top:.5rem">%s.</p><p style="margin-top:1rem"><a class="text-link" href="%s" rel="noopener" target="_blank">Directions in Google Maps<span class="sr-only"> (opens in a new tab)</span> %s</a></p></div></div>""" % (
        B.esc(P["map_embed"]), P["street"], P["city"], P["region"], P["postal"], P["building_notes"], B.esc(P["google_maps"]), B.icon("arrow"))


def location(B, L):
    esc, icon = B.esc, B.icon
    slug = "areas/" + L["slug"]
    trail = [("Home", ""), ("Areas served", "areas-we-serve"), (L["name"], slug)]
    hero = B.page_hero(trail, "Concierge medicine near " + L["name"], L["h1"], L["lede"])
    facts = """<section class="section flush-top"><div class="wrap"><dl class="facts">
<div><dt>From %s</dt><dd>%s miles, about %s minutes</dd></div>
<div><dt>Usual route</dt><dd>%s</dd></div>
<div><dt>Nearer affiliated hospital</dt><dd>%s</dd></div>
<div><dt>Office</dt><dd>%s, Palm Beach Gardens</dd></div></dl>
<p class="small muted" style="margin-top:1rem">Drive estimates without traffic. In season, allow a little longer.</p></div></section>""" % (
        esc(L["from_label"]), L["distance_mi"], L["drive_min"], esc(L["route"]), esc(L["hospital"]), B.PRACTICE["street_short"])
    body = hero + facts + "".join(prose_section(B, i + 1, h, b, slug) for i, (h, b) in enumerate(L["sections"]))
    if L.get("faqs"):
        body += '<section class="section%s" aria-labelledby="lfaq-h"><div class="wrap split"><div><p class="eyebrow">FAQ</p><h2 id="lfaq-h" style="margin-top:1.25rem">From %s</h2></div>%s</div></section>' % (
            " sunk" if len(L["sections"]) % 2 == 0 else "", esc(L["name"]), B.faq_html(L["faqs"]))
    body += '<section class="section" aria-labelledby="map-h"><div class="wrap split"><div><h2 id="map-h" style="font-size:var(--step-3)">Getting here from %s</h2><p class="lede" style="margin-top:1rem">%s</p></div>%s</div></section>' % (esc(L["name"]), L["directions"], map_card(B))
    others = "".join('<a href="/areas/%s">%s <span class="t">%s min</span></a>' % (o["slug"], esc(o["name"]), o["drive_min"]) for o in C.LOCATIONS if o["slug"] != L["slug"])
    body += '<section class="section tight sunk" aria-labelledby="oth-h"><div class="wrap"><h2 id="oth-h" style="font-size:var(--step-2);margin-bottom:1.25rem">Other nearby towns</h2><div class="area-links">%s<a href="/areas-we-serve">All areas</a></div></div></section>' % others
    body += B.cta_band("Visit the office from %s." % L["name"])
    nodes = [{"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": L["title"], "isPartOf": {"@id": B.SITE_ID},
              "about": {"@id": B.ORG_ID}, "spatialCoverage": {"@type": "City", "name": L["name"] + ", FL"},
              "mentions": [{"@type": "Hospital", "name": L["hospital"]}]},
             B.breadcrumb_node(trail)]
    if L.get("faqs"):
        nodes.append(B.faq_node(L["faqs"], B.url(slug)))
    B.write_page(slug, L["title"], L["desc"], body, schema=B.graph(*nodes))


# ---------------------------------------------------------------- journal
def post_image(B, p, sizes, eager=False, cls=""):
    """The article's lead photo, if one has been sourced (stem j-<slug>)."""
    stem = "j-" + p["slug"]
    if stem not in B.IMG:
        return ""
    return B.photo(stem, B.IMG[stem].get("alt", ""), sizes=sizes, eager=eager, cls=cls)


def read_mins(p):
    words = sum(len((b.get("text", "") + " " + " ".join(b.get("items", []))).split()) for b in p["blocks"])
    return max(1, round(words / 220))


def post_card(B, p, i=0, tag="h3"):
    esc, icon = B.esc, B.icon
    img = post_image(B, p, "(max-width: 700px) 92vw, (max-width: 1100px) 45vw, 30vw")
    return """<a class="post-card" href="/blog/%s">%s<div class="pc-body"><p class="pc-meta"><span class="cat">%s</span><span>%d min read</span></p><%s>%s</%s><p class="pc-ex">%s</p><span class="more">Read %s</span></div></a>""" % (
        p["slug"], ('<figure class="pc-img">%s</figure>' % img) if img else "", esc(p["category"]), read_mins(p), tag, esc(p["title"]), tag, esc(p["excerpt"]), icon("arrow"))


def journal(B):
    esc, icon = B.esc, B.icon
    slug = "blog"
    trail = [("Home", ""), ("Blog", slug)]
    cats = []
    for p in J.POSTS:
        if p["category"] not in cats:
            cats.append(p["category"])
    cats.sort(key=lambda c: -sum(1 for p in J.POSTS if p["category"] == c))
    chips = '<div class="chips" role="group" aria-label="Filter by topic"><button type="button" aria-pressed="true" data-cat="all">All <span class="n">%d</span></button>%s</div>' % (len(J.POSTS), "".join(
        '<button type="button" aria-pressed="false" data-cat="%s">%s <span class="n">%d</span></button>' % (esc(c), esc(c), sum(1 for p in J.POSTS if p["category"] == c)) for c in cats))
    lead, rest = J.POSTS[0], J.POSTS[1:]
    feature = """<section class="section flush-top" aria-labelledby="lead-h"><div class="wrap"><a class="feature-post" href="/blog/%s">%s<div class="fp-body"><p class="eyebrow">Latest · %s</p><h2 id="lead-h">%s</h2><p class="lede">%s</p><p class="pc-meta"><span>%s</span><span>%d min read</span></p><span class="more">Read the article %s</span></div></a></div></section>""" % (
        lead["slug"], ('<figure class="fp-img">%s</figure>' % post_image(B, lead, "(max-width: 900px) 92vw, 58vw", eager=True)) if post_image(B, lead, "1px") else "",
        esc(lead["category"]), esc(lead["title"]), esc(lead["excerpt"]), human_date(lead["date"]), read_mins(lead), icon("arrow"))
    items = "".join('<li data-cat="%s">%s</li>' % (esc(p["category"]), post_card(B, p, i)) for i, p in enumerate(rest))
    hero = B.page_hero(trail, "Blog", "Notes on health, from a concierge practice", C.JOURNAL_LEDE, cta=False)
    body = hero + feature + '<section class="section flush-top" aria-labelledby="all-h"><div class="wrap"><div class="headline-row"><h2 id="all-h" style="font-size:var(--step-3)">All articles</h2></div>%s<ul class="post-grid">%s</ul><p class="more-row"><button class="btn ghost" type="button" data-more hidden>Show all articles</button></p></div></section>' % (chips, items) + B.cta_band()
    schema = B.graph({"@type": "Blog", "@id": B.url(slug) + "#blog", "url": B.url(slug), "name": "Legacy Medical Blog", "publisher": {"@id": B.ORG_ID},
                      "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": B.url("blog/" + p["slug"]), "datePublished": p["date"]} for p in J.POSTS]},
                     B.breadcrumb_node(trail))
    B.write_page(slug, "Blog: Health Notes from Legacy Medical, Palm Beach Gardens", C.JOURNAL_DESC, body, schema=schema)
    for i, p in enumerate(J.POSTS):
        post(B, p, J.POSTS)
    feed(B)


def render_blocks(B, blocks):
    out = []
    seen_h2 = False
    for b in blocks:
        t = b["type"]
        if t == "h3" and not seen_h2:
            t = "h2"  # an h3 before any h2 would skip a level after the page h1
        if t == "h2":
            seen_h2 = True
        if t == "h2":
            hid = re.sub(r"[^a-z0-9]+", "-", b["text"].lower()).strip("-")[:60]
            out.append('<h2 id="%s">%s</h2>' % (hid, inline(B, b["text"])))
        elif t in ("p", "h3"):
            out.append("<%s>%s</%s>" % (t, inline(B, b["text"]), t))
        elif t in ("ul", "ol"):
            out.append("<%s>%s</%s>" % (t, "".join("<li>%s</li>" % inline(B, x) for x in b["items"]), t))
        elif t == "quote":
            out.append("<blockquote><p>%s</p></blockquote>" % inline(B, b["text"]))
        elif t == "img" and b.get("stem"):
            out.append("<figure>%s%s</figure>" % (B.photo(b["stem"], b.get("alt", ""), sizes="(max-width: 980px) 92vw, 640px", max_w=1200),
                                                   ("<figcaption>%s</figcaption>" % B.esc(b["caption"])) if b.get("caption") else ""))
    return "".join(out)


def inline(B, text):
    """Escape text, then turn [label](href) into links. External links open
    normally; internal ones are root-relative."""
    s = B.esc(text)
    def repl(m):
        label, href = m.group(1), html.unescape(m.group(2))
        ext = href.startswith("http") and "legacymedicalpalmbeach.com" not in href
        if ext:
            return '<a href="%s" rel="noopener">%s</a>' % (B.esc(href), label)
        href = re.sub(r"^https?://(www\.)?legacymedicalpalmbeach\.com", "", href) or "/"
        return '<a href="%s">%s</a>' % (B.esc(href), label)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", repl, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return s


def post(B, p, all_posts):
    esc, icon = B.esc, B.icon
    slug = "blog/" + p["slug"]
    trail = [("Home", ""), ("Blog", "blog"), (p["title"], slug)]
    body_html = render_blocks(B, p["blocks"])
    if p.get("stale_note"):
        body_html = '<div class="notice">%s<p>%s</p></div>' % (B.ICONS["info"], esc(p["stale_note"])) + body_html
    words = len(re.sub(r"<[^>]+>", " ", body_html).split())
    mins = max(1, round(words / 220))
    # A quiet invitation part-way through, before the third section.
    heads = [m.start() for m in re.finditer(r"<h2 ", body_html)]
    invite = ('<aside class="inline-cta" aria-label="Meet Dr. Shtern"><p class="eyebrow">Legacy Medical</p><p class="ic-h">Questions like this are easier in person.</p>'
              '<p>Your first visit is a complimentary meet and greet with Dr. Shtern in Palm Beach Gardens.</p>'
              '<a class="btn small" href="/meet-and-greet" data-loc="article-inline">Book a meet and greet %s</a></aside>' % icon("arrow"))
    if len(heads) >= 3:
        body_html = body_html[:heads[2]] + invite + body_html[heads[2]:]
    toc = "".join('<li><a href="#%s">%s</a></li>' % (m.group(1), m.group(2)) for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body_html))
    related = [x for x in all_posts if x["category"] == p["category"] and x["slug"] != p["slug"]][:3]
    if len(related) < 3:
        related += [x for x in all_posts if x["slug"] != p["slug"] and x not in related][:3 - len(related)]
    owner = C.CATEGORY_OWNERS.get(p["category"])
    owner_html = ('<p class="toc-care"><span class="eyebrow">Related care</span><a class="text-link" href="/%s">%s %s</a></p>' % (owner[0], esc(owner[1]), icon("arrow"))) if owner else ""
    reviewed = ""
    if p.get("reviewed_by"):
        reviewed = '<span>Medically reviewed by <a class="inline-link" href="/dr-yana-shtern">%s</a></span>' % esc(p["reviewed_by"])
    stem = "j-" + p["slug"]
    lead = ""
    if stem in B.IMG:
        m = B.IMG[stem]
        credit = (" Photo: %s on Pexels." % esc(m["credit"])) if m.get("credit") else " Photo: Pexels."
        lead = '<figure class="wrap article-lead">%s<figcaption>%s</figcaption></figure>' % (
            post_image(B, p, "(max-width: 1400px) 96vw, 1340px", eager=True), credit.strip())
    article = """<div class="read-progress" aria-hidden="true"></div><article class="post">
<header class="wrap article-head">%(crumbs)s<p class="eyebrow">%(cat)s</p><h1>%(title)s</h1><p class="dek">%(dek)s</p>
<p class="article-meta"><span>By the Legacy Medical team</span><span><time datetime="%(d)s">%(date)s</time></span><span>%(mins)d min read</span>%(rev)s</p></header>
%(lead)s
<div class="wrap article-body section flush-top">
<aside class="article-toc" aria-label="In this article"><p class="eyebrow">In this article</p><ol>%(toc)s</ol>%(owner)s</aside>
<div class="prose article-prose">%(body)s
<p class="small muted disclaimer">This article is general information, not advice for your situation. Members can call the office with questions about their own care.</p></div>
</div></article>
<section class="section sunk" aria-labelledby="more-h"><div class="wrap"><div class="headline-row"><h2 id="more-h" style="font-size:var(--step-3)">Keep reading</h2><a class="text-link" href="/blog">All articles %(arrow)s</a></div><div class="post-row">%(cards)s</div></div></section>""" % {
        "crumbs": B.crumbs_html(trail), "cat": esc(p["category"]), "title": esc(p["title"]), "dek": esc(p["excerpt"]), "d": p["date"][:10],
        "date": human_date(p["date"]), "mins": mins, "rev": reviewed, "lead": lead, "toc": toc, "owner": owner_html, "body": body_html,
        "arrow": icon("arrow"), "cards": "".join(post_card(B, x) for x in related)}
    article += B.cta_band()
    node = {"@type": "BlogPosting", "@id": B.url(slug) + "#article", "headline": p["title"][:110], "description": p["excerpt"],
            "datePublished": p["date"], "dateModified": p.get("modified", p["date"]), "url": B.url(slug), "mainEntityOfPage": B.url(slug),
            "author": {"@id": B.ORG_ID}, "publisher": {"@id": B.ORG_ID}, "articleSection": p["category"], "wordCount": words,
            "inLanguage": "en-US", "isPartOf": {"@id": B.url("blog") + "#blog"},
            "image": B.BASE + (("/assets/img/%s-og.jpg" % stem) if stem in B.IMG else "/assets/img/og/journal.jpg")}
    if p.get("reviewed_by"):
        node["reviewedBy"] = {"@id": B.DOC_ID}
        node["@type"] = ["BlogPosting", "MedicalWebPage"]
    title = p.get("seo_title") or (p["title"] + " | Legacy Medical")
    og = ("/assets/img/%s-og.jpg" % stem) if stem in B.IMG else "/assets/img/og/journal.jpg"
    B.write_page(slug, title, p["excerpt"], article, schema=B.graph(node, B.clinic_node(), B.breadcrumb_node(trail)), og_image=og,
                 lastmod_override=p.get("modified", p["date"])[:10])


def feed(B):
    items = []
    for p in J.POSTS[:20]:
        import datetime
        d = datetime.datetime.fromisoformat(p["date"][:19])
        items.append("<item><title>%s</title><link>%s</link><guid>%s</guid><pubDate>%s</pubDate><description>%s</description></item>" % (
            B.esc(p["title"]), B.url("blog/" + p["slug"]), B.url("blog/" + p["slug"]), d.strftime("%a, %d %b %Y %H:%M:%S +0000"), B.esc(p["excerpt"])))
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Legacy Medical Blog</title><link>%s</link><description>Health notes from Legacy Medical, a Concierge Internal Medicine practice in Palm Beach Gardens, Florida.</description><language>en-us</language>%s</channel></rss>\n' % (B.url("blog"), "".join(items))
    os.makedirs(os.path.join(B.PUB, "blog"), exist_ok=True)
    open(os.path.join(B.PUB, "blog/feed.xml"), "w", encoding="utf-8").write(xml)


# ---------------------------------------------------------------- contact, legal, 404
def contact(B):
    P = B.PRACTICE
    esc = B.esc
    slug = "contact"
    trail = [("Home", ""), ("Contact", slug)]
    hero = B.page_hero(trail, "Contact", "Call, write, or stop by the office.", C.CONTACT_LEDE, cta=False)
    hours_rows = "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (d, "%s – %s" % (B.fmt12(o), B.fmt12(c))) for d, o, c in P["hours"]) + '<tr><th scope="row">Saturday and Sunday</th><td>Closed</td></tr>'
    body = hero + """<section class="section flush-top"><div class="wrap split">
<div>
<dl class="facts" style="grid-template-columns:1fr">
<div><dt>Phone</dt><dd><a href="tel:%(tel)s" data-loc="contact" style="font:300 var(--step-3)/1.1 var(--serif);text-decoration:none">%(phone)s</a></dd></div>
<div><dt>Fax</dt><dd>%(fax)s</dd></div>
<div><dt>Email</dt><dd><a class="inline-link" href="mailto:%(email)s" data-loc="contact">%(email)s</a><br><span class="small muted">Please keep medical details out of email.</span></dd></div>
<div><dt>Address</dt><dd>%(street)s<br>%(city)s, %(region)s %(postal)s<br><span class="small muted">%(notes)s</span></dd></div>
%(portal)s</dl>
<table class="hours-table" style="margin-top:2.5rem"><caption class="eyebrow" style="text-align:left;margin-bottom:.75rem">Office hours</caption>%(hours)s</table>
<p class="small muted" style="margin-top:1rem">%(after)s In an emergency, call 911.</p>
</div>
<div class="panel"><h2 id="contact-form-h" style="font-size:var(--step-3);margin-bottom:1.5rem">Send a request</h2>%(form)s</div>
</div></section>
<section class="section sunk" aria-labelledby="map-h"><div class="wrap split"><div><h2 id="map-h" style="font-size:var(--step-3)">Finding the office</h2><p class="lede" style="margin-top:1rem">%(dir)s</p></div>%(map)s</div></section>""" % {
        "tel": P["tel"], "phone": P["phone"], "fax": P["fax"], "email": P["email"], "street": P["street"], "city": P["city"], "region": P["region"],
        "postal": P["postal"], "notes": P["building_notes"], "hours": hours_rows, "after": P["after_hours"], "form": tour_form(B, "contact", "contact-form-h"),
        "dir": C.DIRECTIONS, "map": map_card(B),
        "portal": ('<div><dt>Patient portal</dt><dd><a class="inline-link" href="%s" rel="noopener">Sign in to the patient portal</a></dd></div>' % esc(P["portal_url"])) if P["portal_url"] else ""}
    schema = B.graph({"@type": "ContactPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": C.CONTACT_TITLE, "isPartOf": {"@id": B.SITE_ID}, "about": {"@id": B.ORG_ID}},
                     B.clinic_node(), B.breadcrumb_node(trail))
    B.write_page(slug, C.CONTACT_TITLE, C.CONTACT_DESC, body, schema=schema, scripts=("assets/js/tour.js",), track=False)


def legal(B):
    for slug, data in C.LEGAL.items():
        trail = [("Home", ""), (data["crumb"], slug)]
        hero = B.page_hero(trail, data["eyebrow"], data["h1"], data.get("lede", ""), cta=False)
        body = hero + '<section class="section flush-top"><div class="wrap"><div class="prose">%s</div></div></section>' % data["body"]
        schema = B.graph({"@type": "WebPage", "@id": B.url(slug) + "#webpage", "url": B.url(slug), "name": data["title"], "isPartOf": {"@id": B.SITE_ID}}, B.breadcrumb_node(trail))
        B.write_page(slug, data["title"], data["desc"], body, schema=schema)


def not_found(B):
    body = """<section class="wrap page-hero not-found"><p class="eyebrow">Page not found</p><h1>That page has moved or no longer exists.</h1>
<p class="lede">Our website was rebuilt in 2026 and some old addresses changed. These are the pages people usually look for:</p>
<div class="area-links" style="margin-top:2rem"><a href="/">Home</a><a href="/dr-yana-shtern">Dr. Shtern</a><a href="/concierge-medicine">Concierge medicine</a><a href="/membership">How to join</a><a href="/blog">Journal</a><a href="/contact">Contact</a></div>
<p style="margin-top:2rem">Or call <a class="inline-link" href="tel:%s">%s</a>.</p></section>""" % (B.PRACTICE["tel"], B.PRACTICE["phone"])
    out = B.document("404", "Page not found | Legacy Medical", "This page could not be found. Find Dr. Yana Shtern's concierge practice in Palm Beach Gardens, or call the office.", body, noindex=True, canonical=False)
    open(os.path.join(B.PUB, "404.html"), "w", encoding="utf-8").write(B.smart_quotes(out))
