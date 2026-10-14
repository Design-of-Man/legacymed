# Local authority audit: listings, records and the map pack (2026-10-14)

Evidence for the owner actions in `docs/GROWTH-PLAN-2026-10.md` and the browser prompt in
`docs/COWORK-LOCAL-FIXES.md`. Everything below was read on 2026-10-14 from the public
page named in each row. Nothing here was changed by us: directories, NPPES and the
Google Business Profile are owner actions.

## 1. The short answer: it is the category and the records, not schema

- In Google Maps, Legacy Medical is **4th** for "concierge doctor Palm Beach Gardens" and
  "concierge doctor North Palm Beach", and **6th** for "concierge medicine Jupiter FL".
  With 45 reviews at 5.0 it has the **most reviews of any concierge listing in those top
  tens** (next: Adult Medicine Concierge 43, Coastal Concierge Internal Medicine 42,
  Yael Vidal, MD 40, Dr. Frank J. Contacessa, MD 36).
- For "internist Palm Beach Gardens" it is **not in the top 20**. Its primary category is
  "Medical Center"; every internist that ranks lists as Internist. For "nephrologist Palm
  Beach Gardens" it shows as Nephrologist (a secondary category) and is 11th.
- None of the top concierge competitors wins on markup: most have a single Physician or
  MedicalClinic node, or none (table in `docs/seo-kit/competitor-teardown-2026-10.md`).
  The new site already carries Physician, MedicalClinic, FAQPage and BreadcrumbList.

So the levers are: the primary category, a few wrong directory records that still put
Dr. Shtern in Jupiter or New York, and keeping review velocity up. Not more schema.

## 2. Name collision check: no live practice found

NPPES still lists two similarly named internal medicine entities about 3 miles away in
North Palm Beach (records last updated 2008 and 2009, still marked active in NPPES).
Checked 2026-10-14:

- **Florida Sunbiz:** both entities are INACTIVE, administratively dissolved for not
  filing annual reports (event dates 2009-09-25 and 2010-09-24).
- **Google Maps:** no listing under that name at that address, and none nearby.
- **Web search:** no site, directory profile or review page for it.

Conclusion: dormant records, not a competing practice. **No disambiguation line is needed
on the site now.** If one ever appears, the prepared line is:

> Legacy Medical is an independent concierge internal medicine practice with one office,
> at 11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens. It is not affiliated with
> other practices that use a similar name.

The brand plan stays simple: the exact name "Legacy Medical" with "Palm Beach Gardens"
everywhere, and the legal name Legacy Medical PLLC where a form asks for it. Never name,
contact or report the other entity; its NPPES records can only be changed by its own
authorized official. Re-check once a year.

Other "Legacy" names that show in searches are unrelated and far away (Legacy Health in
Portland, Oregon; Legacy Medical Group in Tamarac; Legacy Medical Center in Miami).

## 3. Wrong records (one row per error)

Canonical facts: Legacy Medical (legal name Legacy Medical PLLC), 11380 Prosperity Farms
Road, Suite 114, Palm Beach Gardens, FL 33410. Phone (561) 834-9280, fax (561) 834-9279.
Mon to Thu 9 AM to 5 PM, Fri 9 AM to 2 PM. Dr. Yana Shtern, MD, NPI 1497940852, FL
license ME114615.

| # | Where | What is wrong | Fix | Who |
|---|---|---|---|---|
| 1 | NPPES, Legacy Medical PLLC, org NPI 1609647866 (updated 2024-01-15) | Location and mailing phone 917-209-9990 (a New York number); no fax; primary taxonomy Nephrology | Phone (561) 834-9280, fax (561) 834-9279; consider Internal Medicine (207R00000X) as primary, Nephrology secondary | Dr. Shtern (authorized official), NPPES login |
| 2 | NPPES, Palm Beach Nephrology Care PLLC, org NPI 1679198162 (updated 2020-06-10) | Still active; location 1210 S Old Dixie Hwy, Jupiter (the hospital's address); phone 917-209-9990 | If that entity no longer bills, deactivate the NPI; if it does, correct phone and location | Dr. Shtern (authorized official) |
| 3 | WebMD (doctor.webmd.com, Shtern profile) | "Concierge Medicine of Jupiter, 2151 S Alternate A1A Ste 950, Jupiter", (561) 743-2239; languages "Chinese, Spanish"; affiliation Maimonides Midwood | Claim (WebMD Care for Providers), set the PBG office, phone, Legacy Medical; set languages once confirmed | Office or Nick, needs provider verification |
| 4 | Vitals (vitals.com/doctors/Dr_Yana_Shtern.html) | Same Jupiter address and (561) 743-2239 | Vitals is part of the WebMD network; the WebMD claim usually feeds it. Check after #3 | Office |
| 5 | EverydayHealth (everydayhealth.care, provider 570986) | Primary practice "2151 S Alt A1A Ste 950, Jupiter", phone (917) 209-9990; PBG listed as "Practice 2" | Most of these aggregators read NPPES: fixing #1 and #2 corrects them on their next refresh; request an edit if not | Office |
| 6 | Vitadox (vitadox.com, Jupiter 33477 profile) | Jupiter Ste 950 address, (561) 743-2239 | Same as #5 | Office |
| 7 | Google Maps, separate listing "Concierge Medicine of Jupiter" (2151 S FL A1A Alt Ste 950, 10 reviews, "Temporarily closed", 561-743-2239) | A former practice listing that many directories copied | Only if Dr. Shtern owns or manages it: mark it permanently closed. If she does not, leave it alone | Question for Nick |
| 8 | Birdeye (reviews.birdeye.com, unclaimed, 45 reviews) | Hours shifted by a day: Mon closed, Tue to Fri 9 to 5, Sat 9 to 2 | Claim free profile and correct hours, or ignore (Birdeye is not a ranking source); Google itself shows the right hours | Office, optional |
| 9 | findmydirectdoctor.com | Specialty "Concierge Nephrology"; languages "English" | Request an edit to "Concierge internal medicine and nephrology" once languages are confirmed | Office, optional |
| 10 | Languages, three sources disagree | WebMD: Chinese, Spanish. US News: Spanish, Russian, English. Jupiter Medical Center (per OPEN-ITEMS): English, Russian | Dr. Shtern confirms; then set the same list everywhere and on the site | Dr. Shtern |
| 11 | Google Business Profile | Primary category "Medical Center"; name "Legacy Medical Concierge - Dr. Yana Shtern" | Primary Internist (keep Nephrologist secondary); name = office signage; appointment link /meet-and-greet | Owner via Cowork (task list) |

Correct already (no action): Google Maps hours and phone; Healthgrades (PBG address,
28 reviews, last verified 2026-10-12); US News profile 650087 (PBG, accepting new patients);
Doximity (PBG, phone and fax right); Sharecare (Legacy Medical, PBG); Castle Connolly
(PBG office listed). Zocdoc, md.com and the Jupiter Medical Center physician page blocked
automated reads; check them by hand.

Social profiles linked from the old site: facebook.com/legacymedicalpalmbeach (the new
site links it) and a LinkedIn **personal-profile** URL, linkedin.com/in/legacy-medical-palm-beaches.
A business on a personal profile breaks LinkedIn's terms; if the practice wants LinkedIn,
it should be a company page.

## 4. Directories and associations worth having

These are the relevant ones for a concierge internist. Each needs the practice to claim or
apply; none is a paid link scheme.

- Healthgrades, US News, Doximity, WebMD/Vitals: the physician profiles above. They rank
  for "Dr. Yana Shtern" and feed AI answers.
- Castle Connolly: already lists her (Top Doctor since 2023 per the site). Keep the
  profile's office current.
- American Academy of Private Physicians (AAPP) member directory: the concierge
  association. Membership is a practice decision and has a fee; question for Nick.
- Jupiter Medical Center and Palm Beach Gardens Medical Center physician directories:
  hospital affiliations are the strongest local trust signal. Make sure both show the
  Legacy Medical office and phone.

## 5. Links worth earning

- Hospital directory pages (above): a contextual link to legacymedicalpalmbeach.com from
  each affiliated hospital's profile of Dr. Shtern.
- Local press: web search surfaces December 2022 issues of Seabreeze Publications'
  community papers (Lifestyles in Palm Beach Gardens, PGA Community News) for "Legacy
  Medical Palm Beach Gardens", but the pages now return 404, so the mention is
  unverified. Ask the office whether they ran an advertorial; a fresh piece at launch,
  linking the new site, is the earned-link opportunity.
- No sitewide footer links, no paid directory bundles, no link exchanges.

## 6. Google Business Profile changes (owner approval needed)

1. Primary category: **Internist**. Secondary: keep **Nephrologist**; "Medical Center" can
   go. This is the single change most likely to move "internist" searches.
2. Name: whatever is on the office sign. Google allows only the real-world name; adding
   "Dr. Yana Shtern" is fine only if the sign carries it.
3. Website stays https://legacymedicalpalmbeach.com/ (already set). Appointment link:
   https://legacymedicalpalmbeach.com/meet-and-greet.
4. Services list: concierge membership, annual physical, hypertension care, kidney care
   (nephrology), preventive care, telehealth visits, labs in the office. Wording from the
   site only.
5. Photos: a new set after the photo shoot in OPEN-ITEMS (exterior, suite entrance,
   exam room, Dr. Shtern). One new photo a month keeps the profile active.
6. Reviews: 45 is already the most among nearby concierge listings. Keep a steady pace by
   asking every member at the annual physical. No incentives, no gating, no review
   schema on the site.

## 7. Shipped in this PR from this audit

- Nothing in the directories (owner actions only).
- On the site: the area pages' Palm Beach drive time now matches the measured table
  (23 minutes, not 25) and the unsourced "many are full" and "island waitlist" lines are
  gone. Drive times were re-measured 2026-10-14 with the same OpenStreetMap routing the
  page cites; all eight towns match within a minute.
