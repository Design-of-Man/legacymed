# Legacy Medical: website (legacymedicalpalmbeach.com)

Static site for Legacy Medical, Dr. Yana Shtern's concierge internal medicine practice in Palm Beach Gardens, FL. A Design of Man client build. Generated: never hand-edit anything in `public/*.html`.

## Build
- `python3 build.py --check` regenerates every page into `public/`, plus sitemap.xml, robots.txt, llms.txt, journal/feed.xml, site.webmanifest, **vercel.json** (headers, CSP with hashed inline scripts, redirects) and `_dev/redirects/` (cmedjupiter.com 301 maps). `--check` fails on banned copy (em dashes, stock AI phrases; list in build.py `BANNED`).
- Stdlib only. Vercel runs the same command (`buildCommand`) and serves `public/` only, so env vars (GA4_ID, VERCEL_ANALYTICS, GOOGLE_PLACES_API_KEY) take effect at build time.
- Gates before any push: `python3 _dev/preflight.py` (must print READY TO DEPLOY), `python3 _dev/verify.py` (axe + console + 404s + overflow on every page at 375/768/1440, light and dark; needs `pip install playwright` and axe-core from npm, path at the top of the file), `python3 _dev/hero_contrast.py` (text over the hero video).

## Where things live
- Facts (phone, address, hours, insurance, socials): `PRACTICE` in build.py and `DOCTOR`/`TEAM` in content.py. Footer, schema, llms.txt and the hours ring all read from these.
- Page copy: content.py. Legal: legal_content.py + npp_text.py (HIPAA notice, carried over verbatim; do not reword). Journal: journal_content.py (POSTS + REDIRECTS). Redirect map: redirects.py.
- Site assistant (chat button, every page): public/assets/js/assist.js. Set answers only, no AI: build.py writes public/assets/assist.json from FAQ_GROUPS + ASSIST_KEYWORDS/ASSIST_EXTRA in content.py (build fails if an FAQ has no keywords). Tour requests post to /api/tour; nothing typed is stored on the device or sent to analytics.
- Page templates: pages.py. Design system: public/assets/css/site.css (black and gold palette, tokens on :root). The client asked for black and gold (Oct 2026): dark tokens on :root, gold accents; `.night` and the footer are a slightly lifted black. JS: public/assets/js/{main,tour,consent}.js. Functions: api/tour.js (Resend), api/reviews.js (Places API).
- Images: originals in `_dev/source-images`, spec in tools/images.json; `python3 tools/build_images.py` writes AVIF/WebP/JPEG + manifest. `python3 tools/build_brand.py` makes favicons, the logo mark and OG cards. Both need Pillow; build.py does not.
- Hero video: public/assets/video, provenance and exact ffmpeg commands in `_dev/video/PROVENANCE.md`. Source is the Jupiter Inlet sunset clip in Dropbox. Not the RevitalIV lighthouse clip.

## Rules that are easy to break
- Never invent facts, reviews, staff, stats or prices. Unconfirmed items live in `_dev/OPEN-ITEMS.md`, not on the site.
- No tracking on pages with a form (`track=False` in write_page for /meet-and-greet and /contact). GA4 is consent-gated and only loads when GA4_ID is set.
- No self-serving review stars in schema (preflight blocks AggregateRating/Review).
- Hero: the full-bleed Jupiter Inlet film fills the screen under a transparent header. A compact block of copy (kicker, h1, lede, two buttons, facts) sits low on the left, Elite-style, kept small at the owner's request, with a gradient shade only where the words sit. No italic in the h1, no `poster` attribute on the video (the <picture> is the poster). `_dev/hero_contrast.py` must stay all-pass.
- The photo reel uses only real practice photos. The 2020 "Concierge Medicine of Jupiter" shoot shows an earlier location and unidentified people: keep it out.
- Hosting/DNS for the domain is with Unkind Designs. Do not touch DNS.
