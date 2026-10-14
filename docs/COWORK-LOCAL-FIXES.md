# Cowork prompt: fix Legacy Medical's listings and records

Paste everything inside the block below into a new Cowork task on the computer where Nick
(or the office) is signed in to Google. Evidence for every task:
`docs/LOCAL-AUTHORITY-AUDIT-2026-10.md`. Written 2026-10-14.

**Timing.** Tasks 1 to 3 can run now. Task 4 (Search Console) can run now. Leave the
website field on Google as it is until the new site is live on legacymedicalpalmbeach.com;
it already points at the right domain.

```text
You are fixing the online listings and records for Legacy Medical, Dr. Yana Shtern's
concierge internal medicine practice in Palm Beach Gardens, Florida. Use my Chrome browser,
where I am signed in. Work through the tasks in order. For each one, look first, change
only what is listed, and keep a running log of what you saw and what you changed.

THE CORRECT FACTS (use exactly these, everywhere)
- Name: Legacy Medical. Legal name (only where a form asks for it): Legacy Medical PLLC
- Address: 11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens, FL 33410
- Phone: (561) 834-9280   Fax: (561) 834-9279   Email: info@legacymedicalpalmbeach.com
- Hours: Monday to Thursday 9:00 AM to 5:00 PM, Friday 9:00 AM to 2:00 PM, Saturday and
  Sunday closed
- Website: https://legacymedicalpalmbeach.com/
- Appointment link: https://legacymedicalpalmbeach.com/meet-and-greet
- Physician: Yana Shtern, MD. Board-certified in internal medicine and nephrology
  (American Board of Internal Medicine). NPI 1497940852. Florida license ME114615.
  Hospital privileges: Jupiter Medical Center and Palm Beach Gardens Medical Center.
- Languages: DO NOT change languages anywhere until I give you the confirmed list.

RULES (non-negotiable)
1. Never type a password, one-time code or security answer for me, and never ask me to
   paste one into the chat. When a site needs a login or 2FA, stop, tell me which site,
   and wait.
2. Stop and ask me before anything that submits a legal attestation (NPPES "certify"),
   costs money, deletes or removes content, marks anything closed, or publicly posts under
   the practice's name.
3. No reviews of any kind: do not write, request, incentivize, flag, reply to or report
   reviews on any site, unless I approve a specific one.
4. Fix only our own records. Do not mention, contact, report or edit any other practice or
   any other business's listing, including any business with a similar name.
5. No patient information anywhere. Do not open patient portals, EMR systems or email
   inboxes.
6. If a page looks different from what I describe, take a screenshot, describe it, and ask
   rather than guessing.

TASKS

1. Google Business Profile for "Legacy Medical Concierge - Dr. Yana Shtern"
   (11380 Prosperity Farms Rd STE 114). Open it from business.google.com.
   a. Report the current primary and secondary categories, business name, website,
      appointment link, services list, number of reviews, the date of the newest review,
      and how many reviews arrived in the last 12 months.
   b. Propose, then wait for my yes: primary category "Internist"; keep "Nephrologist" as
      a secondary; remove "Medical Center" only if I say so.
   c. Ask me what the office sign says before touching the business name. Google only
      allows the name on the sign.
   d. Set the appointment link to the appointment link above. Leave the website as it is.
   e. Check hours match the facts above (Google showed them correctly on 2026-10-14).
   f. Do not post, do not reply to reviews, do not buy ads, decline every upsell.

2. Physician directory profiles. For each, open the page, write down the address, phone,
   practice name and languages shown, then start the free provider claim and go as far
   as it goes without payment or identity documents. Stop and tell me what is needed.
   a. WebMD: https://doctor.webmd.com/doctor/yana-shtern-fb2c5a64-a11e-468e-a541-a873646ac761-overview
      shows "Concierge Medicine of Jupiter, 2151 S Alternate A1A Ste 950, Jupiter",
      (561) 743-2239. It should show Legacy Medical at the address and phone above.
   b. Vitals: https://www.vitals.com/doctors/Dr_Yana_Shtern.html (same wrong Jupiter
      address; often fixed through the WebMD claim, so check after 2a).
   c. Zocdoc: https://www.zocdoc.com/doctor/yana-shtern-md-42511 (could not be read
      automatically; report what it shows).
   d. EverydayHealth: https://www.everydayhealth.care/providers/570986/dr-yana-y-shtern-md/
      shows a Jupiter primary practice and (917) 209-9990. Use its "suggest an edit" or
      contact form if there is one; otherwise log it.
   e. Vitadox: https://www.vitadox.com/doctor/jupiter-fl-33477/yana-shtern-md/N29nHkB2gFwzuGAAx7PAqR
      (Jupiter address, (561) 743-2239). Same as 2d.
   f. Healthgrades, US News, Doximity: these showed the right office on 2026-10-14. Just
      confirm and log.
   g. Jupiter Medical Center and Palm Beach Gardens Medical Center physician directories:
      find Dr. Shtern's profile on each and log the office, phone and website shown.

3. NPPES (nppes.cms.hhs.gov). This needs Dr. Shtern's own CMS login. Stop and ask me to
   have her sign in. Then show me each change before saving, and stop before "certify".
   a. Organization NPI 1609647866, Legacy Medical PLLC: change the practice location and
      mailing phone from 917-209-9990 to (561) 834-9280, add fax (561) 834-9279. Ask me
      whether to make Internal Medicine (207R00000X) the primary taxonomy, with Nephrology
      (207RN0300X) secondary.
   b. Organization NPI 1679198162, Palm Beach Nephrology Care PLLC (location Jupiter,
      phone 917-209-9990): ask me whether that entity still bills. If not, Dr. Shtern may
      choose to deactivate it; that is her decision and her attestation.
   c. Individual NPI 1497940852 is correct. Do not change it.

4. Google Search Console (search.google.com/search-console).
   a. Tell me whether properties exist for legacymedicalpalmbeach.com and cmedjupiter.com,
      their type (Domain or URL prefix), and which account owns them.
   b. On each one that exists, add the user
      claude-gsc-reader@design-of-man-seo.iam.gserviceaccount.com with "Restricted"
      permission. Show me the screen before confirming.
   c. If a property does not exist, stop. Verifying a domain needs a DNS record that
      Unkind Designs controls; tell me and I will arrange it.

5. Bing Places for Business (bingplaces.com). Search for Legacy Medical at the address
   above. Report whether a listing exists and what it shows. If it exists and is
   unclaimed, the easiest path is "import from Google Business Profile"; stop before
   submitting and show me.

6. Apple Business Connect (businessconnect.apple.com). Same as task 5: report what Apple
   Maps shows for Legacy Medical, stop before claiming.

When you finish, give me the log as a table: site, what it showed, what you changed, what
is waiting on me.
```

## What Cowork cannot do (owner)

- DNS for legacymedicalpalmbeach.com and cmedjupiter.com (Unkind Designs): point the domain
  at Vercel, add Search Console TXT records, put the cmedjupiter.com `.htaccess` live.
- NPPES certification (Dr. Shtern).
- Confirm languages spoken, office signage (for the GBP name), and whether Dr. Shtern
  controls the "Concierge Medicine of Jupiter" Google listing.
