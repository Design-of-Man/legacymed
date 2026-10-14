# Open items (need the practice or account access)

Nothing below was guessed on the site. Each item is either left out of the copy or shown as a neutral line until confirmed.

## Needs Dr. Shtern / the office
- **Membership fee.** Not published anywhere. The site says "call the office". If they want a number or range on /insurance-and-fees, add `PRICE_RANGE` in content.py and a sentence to INSURANCE.
- **Insurance plans.** Site lists Medicare, Aetna, Cigna and BlueCross BlueShield (the logos on the old site). CMS data shows NPI 1497940852 enrolled in Medicare, not opted out. Confirm the current plan list.
- **Patient portal URL.** The old FAQ says a portal exists but never links it. Set `PRACTICE["portal_url"]` in build.py and the contact page shows a sign-in link.
- **"Medically reviewed by Dr. Shtern" on journal posts.** Every post has `reviewed_by: None`. When she signs off a post, set it to "Dr. Yana Shtern, MD" and the byline plus `reviewedBy` schema appear. Posts with possible inaccuracies she should look at first: vitamin C "can boost sunscreen" (vitamins-to-take-in-the-morning).
- **Languages spoken.** WebMD says Chinese and Spanish, US News says Spanish, Russian, English, Jupiter Medical Center says English and Russian. Not on the site until confirmed.
- **The unnamed team member** (blonde, Legacy scrubs) appears in the photo reel as "a member of the team". Add her name and role to TEAM in content.py if she wants to be named.
- **New photography.** Every current photo of Dr. Shtern is 934×740 or smaller. They look acceptable at the sizes used but soft on large retina screens. A half-day shoot (Dr. Shtern portrait at 3000px+, the office, exam room, the team) would lift the whole site.
- **Privacy Officer phone (561) 316-7199** in the HIPAA notice (carried over unchanged). Confirm it is still current.
- **Directory listings** (re-checked 2026-10-14, table in docs/LOCAL-AUTHORITY-AUDIT-2026-10.md): WebMD, Vitals, Vitadox and EverydayHealth still show "Concierge Medicine of Jupiter", 2151 S Alternate A1A Ste 950, Jupiter, (561) 743-2239 or (917) 209-9990. Healthgrades, US News (profile 650087), Doximity and Sharecare now show the Palm Beach Gardens office correctly. Claim and correct the rest.
- **NPPES.** Legacy Medical PLLC (NPI 1609647866) lists 917-209-9990 and Nephrology as its primary taxonomy; Dr. Shtern's older Palm Beach Nephrology Care PLLC (NPI 1679198162) is still active in NPPES with a Jupiter location and the same 917 number. She updates or deactivates these herself in NPPES.
- **Medicare figures on /insurance-and-fees** ($283 Part B deductible, $202.90 premium) are 2026 values. CMS publishes the 2027 values in the autumn; update `INSURANCE["medicare"]` in content.py and its "checked" date each January.

## Needs account access
- **Domain + DNS** for legacymedicalpalmbeach.com sit with Unkind Designs. Point the domain at the Vercel project when the handover happens; the vercel.json redirect map and www→apex rules go live with it.
- **cmedjupiter.com.** Ready-made 301 maps in `_dev/redirects/` (Vercel JSON, Apache .htaccess, CSV). Apply whichever matches where that domain ends up, then follow `_dev/redirects/CHANGE-OF-ADDRESS.md` (Search Console Change of Address, in order). This is the single biggest SEO fix: that domain currently outranks the real one.
- **Google Business Profile.** Change primary category from "Medical center" to "Internist" (keep Nephrologist as a secondary), set the name to whatever the office signage says (Google's rule; "Legacy Medical" if that is the sign), and add an appointment link to https://legacymedicalpalmbeach.com/meet-and-greet (the form moved there; /membership#tour is stale). Website is already set. Full steps: docs/COWORK-LOCAL-FIXES.md.
- **Search Console access (2026-10-14).** Neither legacymedicalpalmbeach.com nor cmedjupiter.com is readable by our reporting key. Add claude-gsc-reader@design-of-man-seo.iam.gserviceaccount.com as a user on both properties (verify them first if they do not exist). Until then there is no pre-cutover baseline. See docs/GSC-DEEP-DIVE-2026-10.md.
- **Form delivery.** /api/tour needs `RESEND_API_KEY`, `TOUR_TO_EMAIL` (and optionally `TOUR_FROM_EMAIL` on a verified domain) in Vercel env. Until then the form tells visitors to call. A signed BAA is not required for contact details only, but keep the "no medical details" notice.
- **Live Google reviews.** Set `GOOGLE_PLACES_API_KEY` (+ `GOOGLE_PLACE_ID`) in Vercel env; the next build wires the live rating into the home page.
- **Analytics.** Set `GA4_ID` (consent-gated, never on form pages) and/or `VERCEL_ANALYTICS=1` after enabling Web Analytics + Speed Insights in the project. Add Search Console + Bing verification (DNS preferred) and submit /sitemap.xml.

## Design ideas that need the practice (from the luxury concierge review, Oct 2026)
- A short signed letter from Dr. Shtern (why she started Legacy Medical). The strongest honest signal on MD² and Private Medical; needs her own words.
- A stated panel size ("we care for about N members"). Only with a number she confirms.
- "Accepting new members" status line. Only if true and kept current.

## Journal: 40 articles added Oct 14, 2026 (need Dr. Shtern's review)
Batches in journal_batch_a..d.py. reviewed_by stays None until she signs off. Lines the writers flagged:
- Fast-moving guidance: 2026 ACC/AHA cholesterol guideline (statins post), pneumococcal age 50 (CDC 2024), USPSTF prostate and cervical (2018, updates in progress), hepatitis B and RSV vaccine ages.
- Inferred wording to confirm: "PPSV23 only, a conjugate vaccine is usually still recommended"; shingles post mentions the 2025 Zostavax/dementia study (remove if she prefers).
- General clinical advice without a single source: AAA ultrasound fasting, colonoscopy prep, gout "hot joint with fever needs same-day care".
- Fiber targets (28 g men / 22 g women over 50) vs National Academies 30/21; fiber intake stat is from a conference abstract.
- Advance directives post is general information only, with a pointer to a Florida attorney.
- PSA "drawn in the office" follows from in-office labs but is not stated in content.py literally.
