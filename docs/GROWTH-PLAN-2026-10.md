# Legacy Medical growth plan, October 2026 (cutover preparation)

Written 2026-10-14. The new site is built and deployed to Vercel but **not live**:
legacymedicalpalmbeach.com still serves the old WordPress site, and cmedjupiter.com is an
older copy of it. So this run prepares the switch and records a baseline; it does not tune
live pages. Evidence: `docs/GSC-DEEP-DIVE-2026-10.md`, `docs/LOCAL-AUTHORITY-AUDIT-2026-10.md`,
`docs/seo-kit/competitor-teardown-2026-10.md`. Index: `docs/seo-kit/README.md`.

## 1. Bottom line: the levers, ranked

1. **The cutover itself, done cleanly.** The old site has no H1, no meta description and
   no schema; the new one is complete. What can waste it is a broken redirect map. Every
   old URL we could find (208 across both domains) now lands on its real new page:
   **208/208 mapped**, up from 149/208. Then the Change of Address for cmedjupiter.com.
2. **Google Business Profile primary category: Internist.** The listing is 4th for
   "concierge doctor Palm Beach Gardens" but absent from the top 20 for "internist Palm
   Beach Gardens", where every ranking practice lists as Internist.
3. **Wrong records that still put Dr. Shtern in Jupiter or New York**: the practice's own
   org NPI carries a 917 number; an older nephrology NPI and four directories still show
   a Jupiter practice and phone. NPPES feeds most of them.
4. **Reviews: keep the pace.** 45 at 5.0 is already the most in the concierge pack. A
   steady ask at each annual physical, nothing more.
5. **Medicare clarity on /insurance-and-fees.** The main objection a Medicare-age member
   has is "do I pay twice?". The page now answers it from CMS sources, without a fee.

Not levers: more schema (the site already out-marks every competitor), more area pages
(there are eight; city intent is a Maps lever), new national health content.

## 2. What the data says

- **Search Console: unreadable for both domains** (`gsc.py sites`, 2026-10-14). No
  clicks, impressions, CTR, position or striking-distance numbers exist for this run.
  Owner action 1 below fixes it; the baseline commands are in the GSC deep dive.
- **GA4, GBP and Vercel analytics: none connected** for Legacy in Windsor.ai or Vercel.
- **Google Maps (logged out, 2026-10-14):** 4th for "concierge doctor Palm Beach Gardens"
  and "concierge doctor North Palm Beach", 6th for "concierge medicine Jupiter FL", 11th
  for "nephrologist Palm Beach Gardens", not in the top 20 for "internist Palm Beach
  Gardens". 45 reviews, 5.0, primary category "Medical Center". Hours on Google are right.
- **Name collision:** the two similarly named North Palm Beach entities in NPPES were
  administratively dissolved in 2009 and 2010 (Sunbiz) and have no Maps listing or web
  presence. No disambiguation line needed now; a prepared line is in the audit.
- **Area pages:** the eight drive times are sourced (OpenStreetMap routing, stated on the
  page) and were re-measured 2026-10-14 with the same router: all within a minute of the
  table. Palm Beach copy said "about 25 minutes" against a measured 22 to 23; fixed.
  Palm Beach Gardens' own "4 min" depends on which point counts as the town centre
  (OpenStreetMap's centroid gives 14); it appears only in the hub table. No pages added.

## 3. How a concierge practice wins locally in 2026

Proximity, the primary category, review count and recency, and consistent records decide
the map pack. Organic results for "concierge doctor <town>" go to pages that answer the
buyer's real questions (cost, Medicare, what is included, who the doctor is) with
specifics. Schema helps machines read what is already on the page; it does not rank a
thin page. FAQ rich results ended 7 May 2026; FAQ markup stays only where the questions
are visible, which is how this site does it.

## 4. Redirect coverage, in numbers

Inventory: `_dev/redirects/old-urls.txt`, 208 URLs crawled 2026-10-14 (both WordPress
sitemaps, every internal link on every old page, every `/?p=ID` shortlink resolved on the
live sites). Checker: `python3 _dev/redirect_coverage.py` (also run by preflight).

| | Before this PR | After |
|---|---|---|
| legacymedicalpalmbeach.com | 37/52 | **52/52** |
| cmedjupiter.com | 112/156 | **156/156** |
| Total | 149/208 | **208/208** |

All 89 sitemap URLs were already mapped. The gaps were 58 WordPress shortlinks (they
would have served the home page, or bounced cmedjupiter.com visitors to it) and the
cmedjupiter.com feed. Probing the live Vercel deployment found two more patterns with no
rule (blog pagination and day archives returned 404); both now go to /journal. Only the
theme's four demo items and one Elementor template go to the home page, because they had
no content.

Measured on the production Vercel deployment: Vercel strips the trailing slash before it
applies vercel.json redirects, so an old WordPress URL takes two permanent (308) hops on
legacymedicalpalmbeach.com. Google follows both; cmedjupiter.com's Apache rules take one.

## 5. Shipped in this PR

| Page or file | Change | Why |
|---|---|---|
| `redirects.py`, `vercel.json`, `_dev/redirects/*` | Shortlink maps for both domains; rules for blog pagination, day archives, WordPress sitemaps, feeds and robots.txt on cmedjupiter.com | Coverage 149/208 to 208/208 |
| `_dev/redirect_coverage.py`, `_dev/redirects/old-urls.txt`, `_dev/preflight.py` | Offline simulator of Vercel and Apache rules over the old-URL inventory, plus `--live HOST` mode; preflight blocks on any unmapped URL | Coverage can never silently regress |
| `vercel.json` (via build.py) | `X-Robots-Tag: noindex, nofollow` on any `*.vercel.app` host | legacymedical.vercel.app (the production alias) answered 200 with `index, follow`: a full duplicate of the site |
| /insurance-and-fees | Medicare and membership guide: who pays for what (table), what the fee is not, Medicare Advantage, 2026 CMS figures dated and sourced; one new visible FAQ (in FAQPage schema); title and description rewritten 2026-10-14 | Item 7 of the brief; the Medicare-age buyer's main objection |
| /membership | Hero now has "Book a meet and greet" and "Call" | At 393px nothing on the first screen booked a visit |
| /meet-and-greet | Hero "Request a time" jumps to the form, plus "Call" | The form started two screens down on a phone |
| `main.js` | The mobile Call / Meet & greet bar hides while a form is on screen | At 393px it covered the form's Send button |
| `main.js`, `build.py` | `appointment_cta` event on booking links; every event mirrored to Vercel Web Analytics; payload is placement and page path only | Same event names as the sibling sites; booking clicks were not counted |
| /areas/palm-beach | 25 minutes to 23 (matches the measured table); dropped the unsourced "many are full" and "island waitlist" lines; H1 changed 2026-10-14 | Facts discipline |
| `_dev/verify.py` | axe path settable with `AXE_JS` | The hard-coded path pointed at another session's scratchpad |
| `_dev/redirects/CHANGE-OF-ADDRESS.md`, `_dev/OPEN-ITEMS.md` | Updated for the new rules, the two-hop note, wp-admin retirement, GBP link, NPPES and directory findings | Runbooks match reality |

Title and description changes, dated 2026-10-14 (measure from the first Search Console
pull after cutover):

- /insurance-and-fees title: "Insurance and Membership Fees | Legacy Medical Concierge
  Practice" to "Concierge Fees, Medicare and Insurance | Legacy Medical".
- /insurance-and-fees description rewritten around Medicare (152 characters).
- /areas/palm-beach H1: "Concierge medicine for Palm Beach, without the island
  waitlist." to "Concierge medicine for Palm Beach, about 23 minutes north."

Verification: build `--check` clean; preflight READY TO DEPLOY with 208/208; verify.py
0 problem combos (145 pages x 3 widths x 2 schemes) before and after; hero_contrast all
pass. Lighthouse mobile, local static server, before vs after (two runs each; home TBT
varies 0 to 190 ms run to run):

| Page | Perf | A11y | LCP before | LCP after | CLS |
|---|---|---|---|---|---|
| / | 91 to 97 vs 95 | 100 | 2.6 to 2.7 s | 2.5 to 2.8 s | 0 |
| /insurance-and-fees | 99 vs 100 | 100 | 2.0 to 2.1 s | 1.7 s | 0 |
| /meet-and-greet | 98 vs 97 to 98 | 100 | 2.3 to 2.4 s | 2.3 to 2.4 s | 0 |
| /membership | 99 to 100 vs 100 | 100 | 1.8 to 2.1 s | 1.4 to 1.7 s | 0 |

## 6. Owner actions, in order

1. **Search Console access** (today): add `claude-gsc-reader@design-of-man-seo.iam.gserviceaccount.com`
   (Restricted) to both properties; verify them first if they do not exist. Then pull the
   baseline in the GSC deep dive before DNS changes.
2. **Merge order**: PR #2 (the site rebuild, branch `claude/legacy-site-rebuild`) first,
   then this PR. Vercel production already deploys from that branch.
3. **Vercel env vars** (project `legacymedical`, Production):
   - `RESEND_API_KEY`, `TOUR_TO_EMAIL`, optionally `TOUR_FROM_EMAIL` on a domain verified
     in Resend (its DNS records go through Unkind Designs). Until then /api/tour tells
     visitors to call.
   - `VERCEL_ANALYTICS=1` after switching on Web Analytics and Speed Insights in the
     project. Custom events (call_click, appointment_cta) need a plan that includes them.
   - `GA4_ID` if the practice wants GA4 (consent-gated, never on form pages). Then mark
     `call_click` and `appointment_cta` as key events in GA4.
   - `GOOGLE_PLACES_API_KEY` and `GOOGLE_PLACE_ID` for the live rating on the home page.
   - Redeploy after setting them (they take effect at build time).
4. **DNS cutover** (Unkind Designs): point legacymedicalpalmbeach.com and www at Vercel.
   Then run `python3 _dev/redirect_coverage.py --live legacymedicalpalmbeach.com` and
   `curl -s -o /dev/null -w '%{http_code}' https://www.legacymedicalpalmbeach.com/`
   (expect 308).
5. **cmedjupiter.com**: paste `_dev/redirects/cmedjupiter.htaccess` above the WordPress
   block (export anything needed from that WordPress first; wp-admin will redirect too),
   then follow `_dev/redirects/CHANGE-OF-ADDRESS.md`.
6. **Search Console and Bing**: submit https://legacymedicalpalmbeach.com/sitemap.xml in
   both; import the site into Bing Webmaster Tools from Search Console.
7. **GBP, NPPES and directories**: run `docs/COWORK-LOCAL-FIXES.md`.

## 7. Questions for Nick

- PR #2 is still open and is what Vercel serves. Is it about to merge into main? This PR
  is branched from it so the redirect checks run against the real new site.
- Does Dr. Shtern own or manage the Google listing "Concierge Medicine of Jupiter"
  (2151 S Alt A1A Ste 950, temporarily closed, 10 reviews)? Many directories copied it.
- Does Palm Beach Nephrology Care PLLC (NPI 1679198162) still bill? If not, she can
  deactivate that NPI.
- What does the office sign say (GBP name must match it)?
- Languages spoken: English and Russian? Spanish? (three directories disagree)
- Does the membership include the annual physical? The site says members "schedule your
  first Legacy physical"; the Medicare guide only says to ask which parts are billed.
- Did the practice run a piece in the Seabreeze community papers in December 2022?
- A /thank-you page after a successful meet-and-greet request would let us count
  confirmed leads (the form pages carry no analytics, by rule). Worth adding?

## 8. Next 90 days and how we will know

| Measure | Now (2026-10-14) | Target by mid-January 2027 |
|---|---|---|
| Search Console readable | no | both properties, baseline recorded |
| Old URLs mapped | 208/208 | 100% of any URL with impressions too |
| cmedjupiter.com Change of Address | not started | running, clicks shifting to the main domain |
| Maps, "internist Palm Beach Gardens" | not in top 20 | in the top 10 after the category change |
| Maps, "concierge doctor Palm Beach Gardens" | 4th | top 3 |
| Google reviews | 45, 5.0 | 55+, steady monthly pace |
| Directory records with a Jupiter or 917 phone | 6 (incl. 2 NPPES) | 0 |
| Confirmed meet-and-greet requests | not measured | counted (Resend live; thank-you page if approved) |

## 9. Guardrails

No invented facts, prices, reviews or drive times. No fee figure until the practice
publishes one. No review or AggregateRating schema; no reviewedBy until Dr. Shtern signs
off a page. No tracking on form pages. No new area or city pages. Never name or contact
the similarly named entities. DNS, GBP, NPPES and directories are owner actions.
