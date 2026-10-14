# Search Console deep dive, October 2026 (pre-cutover)

Written 2026-10-14. Status: **blocked on access**. The new site is not live yet:
legacymedicalpalmbeach.com still serves the old WordPress site, and cmedjupiter.com
is an older copy of it. This file records what could and could not be measured, and
the exact baseline to pull the day access arrives, so the switch can be measured.

## 1. What could be read

| Source | legacymedicalpalmbeach.com | cmedjupiter.com |
|---|---|---|
| Search Console (`gsc.py sites`, our service-account key) | **Not readable** | **Not readable** |
| Windsor.ai `searchconsole` connector | not connected | not connected |
| Windsor.ai `googleanalytics4` | no Legacy property connected | none |
| Windsor.ai `google_my_business` | no Legacy location connected | n/a |
| Vercel Web Analytics | project `legacymedical` exists, domain not pointed at it | n/a |

`gsc.py sites` on 2026-10-14 lists exactly four properties: elitesportsmed.org,
www.firstrehabnpb.com, sc-domain:jupiterlaser.com and sc-domain:regenorthopb.com.

So these numbers are **unavailable**, not zero:

- Clicks, impressions, CTR and average position, last 28 days vs the previous 28
- Striking-distance queries (position 4 to 20, 10+ impressions, non-brand)
- Which old pages earn clicks, brand vs non-brand split, cannibalization

## 2. What Nick needs to do (owner action)

1. In Search Console, check whether these properties exist and who owns them:
   `sc-domain:legacymedicalpalmbeach.com` and `sc-domain:cmedjupiter.com`
   (Domain properties, verified by a DNS TXT record; Unkind Designs holds DNS).
   If DNS is not possible, URL-prefix properties for `https://legacymedicalpalmbeach.com/`,
   `https://cmedjupiter.com/` and `https://www.cmedjupiter.com/` verified by an HTML
   file on each WordPress site.
2. On each property: Settings, Users and permissions, Add user:
   `claude-gsc-reader@design-of-man-seo.iam.gserviceaccount.com`, permission
   **Restricted** (read-only is all we need).
3. The same Google account must be an **Owner** of both properties for the Change of
   Address tool later (`_dev/redirects/CHANGE-OF-ADDRESS.md`, step 4).

## 3. The baseline to pull the day access arrives

Run from any checkout (the key lives outside the repo):

```sh
GSC=/root/.claude/skills/search-console/scripts/gsc.py
for P in legacymedicalpalmbeach cmedjupiter; do
  python3 $GSC summary --property $P --days 28
  python3 $GSC compare --property $P --days 28
  python3 $GSC pages   --property $P --days 90 --limit 200
  python3 $GSC raw     --property $P --days 90 --dimensions query,page --limit 5000 --json > /tmp/$P-90d.json
done
```

Then, before DNS changes:

- Add every page with impressions to `_dev/redirects/old-urls.txt` (source `gsc`) and
  run `python3 _dev/redirect_coverage.py`. It must still print `N/N mapped`.
- Record the 28-day clicks, impressions, CTR and position for **both** domains here,
  with exact date ranges. The cutover is measured as the sum of the two properties
  before vs legacymedicalpalmbeach.com alone after (cmedjupiter.com should fall to
  near zero inside 180 days once the Change of Address runs).
- List the queries that land on old URLs. The new equivalent of each must keep that
  intent (the map in `_dev/redirects/redirect-map.csv` already sends every old post to
  its own new article, never to the journal index or the homepage).

## 4. What we measured instead (no Search Console needed)

**Old-site inventory.** Both WordPress sitemaps, every link on every old page, and every
`/?p=ID` shortlink, crawled 2026-10-14: 208 URLs (52 on legacymedicalpalmbeach.com,
156 on cmedjupiter.com). Redirect coverage before this PR: 149/208. After: **208/208**
(details in `docs/GROWTH-PLAN-2026-10.md`, section 5). The Wayback Machine could not be
reached from the build sandbox, so URLs that exist only in the archive are not in the
inventory; Search Console's page list will catch any that still get impressions.

**Google Maps positions** (logged-out desktop browser, map centred on the office,
2026-10-14). This is the closest thing to a ranking baseline we have today:

| Query | Legacy Medical's position | Reviews shown |
|---|---|---|
| concierge doctor Palm Beach Gardens | 4 | 45, 5.0 |
| concierge doctor North Palm Beach | 4 | 45, 5.0 |
| concierge medicine Jupiter FL | 6 | 45, 5.0 |
| nephrologist Palm Beach Gardens | 11 | 45, 5.0 |
| internist Palm Beach Gardens | not in the top 20 | |

The listing's primary category is "Medical Center". Every internist that ranks for
"internist Palm Beach Gardens" lists as Internist. See the local authority audit.

**Organic.** A `site:` search for either domain returned nothing usable from the search
tool available here, so no organic baseline exists. OPEN-ITEMS records that
cmedjupiter.com outranks the real domain; that is not verifiable until Search Console
access arrives.

## 5. Re-run checklist (next pull)

- [ ] `gsc.py sites` lists both Legacy properties
- [ ] 28-day summary and compare for both, date ranges written here
- [ ] striking-distance count (position 4 to 20, 10+ impressions, non-brand)
- [ ] old URLs with impressions added to `old-urls.txt`, coverage still N/N
- [ ] title/description CTR outliers listed (none changed blind in this PR except
      /insurance-and-fees, which gained a Medicare guide; changed 2026-10-14)
