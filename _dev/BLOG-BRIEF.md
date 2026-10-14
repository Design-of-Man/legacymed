# Brief: journal articles for Legacy Medical

You are writing patient-education articles for the journal of Legacy Medical, Dr. Yana Shtern's concierge
internal medicine practice in Palm Beach Gardens, FL. Dr. Shtern is board-certified in internal medicine
and nephrology. Read `CLAUDE.md`, then study 2 or 3 posts in `journal_concierge.py` to match the exact data
shape, length, tone and linking style. The posts there are the model; copy their structure exactly.

## What to deliver

1. One new Python module at the path your task names (for example `journal_batch_a.py`), with a single
   list `POSTS = [...]` of post dicts, same keys as in `journal_concierge.py`:
   `slug, title, seo_title, date, modified, category, excerpt, blocks, sources, stale_note, reviewed_by`.
   - `reviewed_by` is always `None`. `stale_note` is `None`. `sources` is `[]` (sources go inline as links).
   - `date` and `modified`: use the dates your task gives, `YYYY-MM-DDTHH:MM:SS`, each post a different time.
   - `category` must be one of: Concierge medicine, Everyday health, Prevention and screening,
     Infections and vaccines, Heart and blood pressure, Healthy aging, Medications, Nutrition,
     Aging and family, Seasonal residents, Kidney health.
   - `seo_title` ends with ` | Legacy Medical` and stays at or under 65 characters in total.
   - `excerpt`: 1 to 2 sentences, under 200 characters.
   - Block types used in the model: `p` (text), `h2` (text), `ul`/`ol` (items). Inline markdown links
     `[text](url)` and `**bold**` work inside text.
2. One lead photo per post saved to `_dev/source-images/journal/<slug>.jpg`, plus a JSON file
   at the path your task names (for example `_dev/blog-photos-a.json`) mapping `"j-<slug>"` to
   `{"file": "journal/<slug>.jpg", "alt": "...", "credit": "<photographer>", "source": "<pexels page url>",
   "q": 76, "widths": [800, 1600], "formats": ["webp", "avif"], "og": true}`.
   **Do not edit `tools/images.json`, `journal_content.py`, `build.py` or anything else.** The lead merges.

## Rules (the build fails or the client objects otherwise)

- **Accuracy first.** Every medical fact, number and recommendation must come from an official or primary
  source (CDC, NIH/NIDDK/NIA/NHLBI/NCI, USPSTF, AHA, ADA, ACC, National Kidney Foundation, KDIGO, FDA,
  Mayo Clinic, Cleveland Clinic, peer-reviewed papers on PubMed) and be linked inline where it is used.
  Use WebSearch/WebFetch to check what the source says *now*; do not quote from memory. If guidance changed
  recently (for example USPSTF updates), use the current version and say what year it is from.
- Never invent anything about the practice: no fees, prices, staff, stats, reviews, services or promises
  beyond what `content.py` already states (`PRACTICE` in build.py, `DOCTOR`/`TEAM`/`HOME` in content.py).
  Safe to mention: complimentary meet and greet with Dr. Shtern (`/meet-and-greet`), same or next business
  day visits, members reach the practice by phone at any hour, video visits (`/telehealth`), she is
  board-certified in internal medicine and nephrology, Palm Beach Gardens office.
- Not medical advice in tone: explain, give the official guidance, say when to call a doctor or 911,
  and end each post with a short, low-key paragraph linking to a relevant site page and the meet and greet.
- Internal links only to pages that exist: /concierge-medicine /membership /meet-and-greet /telehealth
  /hypertension /kidney-care /preventive-care /chronic-care /labs-and-tests /same-or-next-day-visits
  /specialists-and-hospital-care /geriatric-memory-care /for-families /seasonal-residents /patients
  /faq /insurance-and-fees /dr-yana-shtern /videos, and existing journal posts `/journal/<slug>` (list them
  with `python3 -c "import journal_content as J; print([p['slug'] for p in J.POSTS])"`).
- Copy style: plain, warm, specific American English. Short paragraphs. No em dashes (use commas,
  colons or periods). None of these words: delve, elevate, journey, seamless, robust, holistic,
  cutting-edge, state-of-the-art, world-class, nestled, testament to, unparalleled, comprehensive,
  leverage, tailored, empower, "in today's", "whether you're", peace of mind, navigate/navigating,
  embark, unlock, pivotal, meticulous, bespoke. Avoid stock AI patterns ("it's not X, it's Y",
  "In conclusion", triplet lists of adjectives).
- Length: 700 to 1,100 words per post, 3 to 5 `h2` sections.
- Slugs must not collide with existing journal slugs.

## Photos

- Pexels only (free licence). Find one on pexels.com via search, then download with
  `curl -sL -o _dev/source-images/journal/<slug>.jpg "https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=2000"`.
  Check it is a real JPEG at least 1600 px wide (`python3 -c "from PIL import Image; print(Image.open(p).size)"`)
  and look at it (Read the file) before keeping it.
- Landscape. Warm, calm, editorial still lifes or scenes that fit a cream, boutique site: objects, food,
  hands, nature, Florida light. Avoid clinical stock clichés (stethoscope-on-keyboard, doctor pointing at
  a tablet), avoid faces that look like they could be "our patients", and avoid anything cold, dark or garish.
- `alt` describes what is literally in the photo. `credit` is the photographer's name from the Pexels page.

## Check before you finish

Run `python3 -c "import <yourmodule> as m; print(len(m.POSTS))"` and a quick scan of your module text for
the banned words and em dashes. Report: the slugs, titles, categories, and anything you were unsure of.
