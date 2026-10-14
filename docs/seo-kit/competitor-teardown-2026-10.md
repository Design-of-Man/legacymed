# Competitor teardown, 2026-10-14

Concierge and internal medicine practices around Palm Beach Gardens, Jupiter and North
Palm Beach. Pages were loaded in a headless browser on 2026-10-14 and parsed for title,
H1, JSON-LD types and visible word count; Maps data came from Google Maps results for
five money queries, map centred on the office. Raw HTML is third-party content and is
not committed. Internal research only: none of this goes on the site, and the site never
names or compares itself to another practice. Conclusions are in
`docs/LOCAL-AUTHORITY-AUDIT-2026-10.md`.

## Map pack: who shows, with what (Google Maps, 2026-10-14)

Position in brackets is per query: CD-PBG = "concierge doctor Palm Beach Gardens",
CD-NPB = "concierge doctor North Palm Beach", CM-J = "concierge medicine Jupiter FL",
IM-PBG = "internist Palm Beach Gardens".

| Practice | Model | Primary category | Reviews | Positions |
|---|---|---|---|---|
| **Legacy Medical Concierge - Dr. Yana Shtern** (us) | Independent concierge, internist + nephrologist | Medical Center | 45, 5.0 | CD-PBG 4, CD-NPB 4, CM-J 6, IM-PBG not in top 20 |
| Weisz Concierge Medical, 3375 Burns Rd | Independent concierge | Medical clinic | 15, 5.0 | CD-PBG 1, CD-NPB 2 |
| Campazzi Concierge Medicine, 11940 US-1 | Independent concierge (also Palm Beach office) | Family practice physician | 3, 5.0 | CD-PBG 2, CD-NPB 3 |
| UPLIN Health, 2925 PGA Blvd | House-call concierge | Home health care service | 32, 5.0 | CD-PBG 3 |
| Yael Vidal, MD (Vidal Medical Concierge), 11911 US-1 | Independent concierge | **Internist** | 40, 4.9 | CD-NPB 1, CD-PBG 7 |
| Adult Medicine Concierge, 601 University Blvd, Jupiter | Independent concierge, internists | Medical clinic | 43, 5.0 | CM-J 1, CD-PBG 8 |
| Concierge Internal Medicine Associates, 600 University Blvd, Jupiter | Independent concierge | Medical clinic | 1, 5.0 (doctor's own listing: 15, 3.4) | CM-J 3, CD-PBG 6 |
| Jupiter Concierge Family Practice, 2151 Alt A1A S Ste 950 | Independent concierge, family medicine | Family practice physician | 21, 5.0 | CM-J 4 |
| Dr. Frank J. Contacessa, MD, 3335 Burns Rd | MDVIP-affiliated | **Internist** | 36, 4.8 | IM-PBG 9, CD-PBG 14 |
| Dr. Evan R. Shapiro, MD, 11020 RCA Center Dr | MDVIP-affiliated | **Internist** | 11, 4.5 | IM-PBG 11 |
| Dr. Ronald Goldin, MD, FASN, 4215 Burns Rd | MDVIP-affiliated, internist and nephrologist | **Internist** | 23, 4.5 | IM-PBG 5 |
| Tampa General Hospital Concierge Health, 4620 PGA Blvd | Hospital-system concierge | Internist | 4, 4.0 | CD-PBG 10 |
| Jupiter Medical Center Concierge Medicine, 2055 Military Trail | Hospital-system concierge | Medical office | none | CM-J 5 |
| Coastal Concierge Internal Medicine, West Palm Beach | Independent concierge | Internist | 42, 4.9 | CD-PBG 19 |

The closest analogue to Dr. Shtern is the MDVIP internist and nephrologist on Burns Road:
same double specialty, half the reviews, but listed as Internist, so he ranks 5th for
"internist Palm Beach Gardens" where we do not appear at all.

## Membership positioning (from each practice's own pages)

- **MDVIP affiliates** publish their fee on the physician page: annual $3,750 (Contacessa),
  $4,500 (Shapiro), $2,800 (Goldin), payable quarterly or semi-annually. MDVIP frames the
  fee as covering its "Wellness Program"; insurance is billed for everything else.
- **Independents** (Adult Medicine Concierge, Concierge Internal Medicine Associates,
  Jupiter Concierge Family Practice, Weisz, Campazzi, Vidal): none published a fee on the
  pages read. They sell 24/7 access, same or next-day visits, a limited panel and an
  annual or executive physical. One accepts members without insurance.
- **Hospital-system concierge** (Tampa General, Jupiter Medical Center): institutional
  affiliation is the pitch; few reviews.
- **Legacy Medical**: independent, double board-certified (internal medicine and
  nephrology), privileges at both local hospitals, complimentary meet and greet, fee
  explained in person. The new /insurance-and-fees Medicare guide answers the question
  the MDVIP pages answer with a number, without publishing one.

## Per page

| Page | Title tag | H1 | JSON-LD types | Words |
|---|---|---|---|---|
| MDVIP, Contacessa profile | Dr. Frank J. Contacessa, MD - Internal Medicine Doctor - Beyond Concierge Medicine in Palm Beach Gardens FL - MDVIP | Frank J. Contacessa, MD | Organization, Physician, PostalAddress | ~1,280 |
| MDVIP, Shapiro profile | Dr. Evan R. Shapiro, MD - Internal Medicine Doctor - … - MDVIP | Evan R. Shapiro, MD | Organization, Physician, PostalAddress | ~850 |
| MDVIP, Goldin profile | Dr. Ronald Goldin, MD, FASN - Internal Medicine Doctor - … - MDVIP | Ronald Goldin, MD, FASN | Organization, Physician, PostalAddress | ~990 |
| MDVIP directory, Palm Beach Gardens | Find Personal Primary Care Doctors in Palm Beach Gardens, FL \| MDVIP | Find Personal Doctors Near Palm Beach Gardens, FL | ItemList, Organization, Physician, PostalAddress, WebPage | ~370 |
| Concierge Internal Medicine, PBG page | Palm Beach Gardens Conciege Doctor - Concierge Internal Medicine | Concierge Medical Doctor | Article, Person, WebPage, WebSite, BreadcrumbList (Yoast default) | ~1,510 |
| Adult Medicine Concierge, home | Adult Medicine Concierge \| Concierge Medicine Practice Jupiter, FL | Jupiter's Finest Concierge Medicine Practice | MedicalClinic, WebPage, WebSite, BreadcrumbList | n/a |
| Jupiter Concierge Family Practice, concierge page | Concierge Medicine - Jupiter Concierge Family Practice | CONCIERGE MEDICINE | MedicalClinic, Organization, Service, Offer, WebPage, WebSite | ~620 |
| VIP Primary Care, PBG page | Concierge Doctor in Palm Beach Gardens - Dr. Robert Briskin - VIP Primary Care - … | VIP Primary Care - The first and best Concierge Doctor in Palm Beach Gardens, Florida | none | ~480 |
| TGH Concierge Health | TGH Concierge Health: A Service of TGH Primary Care | Concierge Health | none | ~500 |
| legacymedicalpalmbeach.com today (old WordPress) | Legacy Medical Palm Beach – Concierge Medicine | none | none; no meta description | ~780 |
| New site (legacymedical.vercel.app) | Concierge Doctor in Palm Beach Gardens \| Legacy Medical | Concierge medicine with a doctor who knows you. | Physician, MedicalClinic + MedicalBusiness, Hospital, EducationalOccupationalCredential, FAQPage, BreadcrumbList, and more | long-form |

## Reading it

1. **Schema is not the gap.** The best-ranked competitors carry one Physician node or
   none. The new site already out-marks all of them; keep it accurate, add nothing for
   ranking's sake.
2. **The primary category is.** Every practice that ranks for "internist" lists as
   Internist. Legacy lists as Medical Center.
3. **Reviews are already a strength.** 45 at 5.0 is the most in the concierge pack. Keep
   the pace steady rather than chase a number.
4. **The old site is the weakest page in the set** (no H1, no description, no schema).
   The cutover itself is the biggest organic lever, provided every old URL lands on its
   real equivalent (208/208 in this PR) and the Change of Address runs for cmedjupiter.com.
