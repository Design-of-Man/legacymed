# SEO and growth kit: START HERE

Legacy Medical (legacymedicalpalmbeach.com). Last updated 2026-10-14. The new site is
not live yet; everything here is cutover preparation plus a baseline.

## The plan and the evidence

| File | What it is | Status |
|---|---|---|
| `docs/GROWTH-PLAN-2026-10.md` | Levers ranked, what shipped, owner actions, questions, 90-day targets | Current |
| `docs/GSC-DEEP-DIVE-2026-10.md` | Search Console status and the baseline to pull before DNS changes | **Blocked**: neither domain readable yet |
| `docs/LOCAL-AUTHORITY-AUDIT-2026-10.md` | Maps positions, name-collision check, citation error table, GBP changes | Current; owner actions pending |
| `docs/COWORK-LOCAL-FIXES.md` | Paste-ready browser prompt for GBP, directories, NPPES, Search Console, Bing, Apple | Ready to run |
| `docs/seo-kit/competitor-teardown-2026-10.md` | Map pack and page-level teardown of nearby concierge and internal medicine practices | Current |
| `_dev/redirects/CHANGE-OF-ADDRESS.md` | cmedjupiter.com move, step by step | Ready; runs after cutover |
| `_dev/redirects/old-urls.txt` | Every old URL found on both domains (208) | Add Search Console pages when readable |
| `_dev/redirect_coverage.py` | Checks every old URL lands on its real new page; `--live HOST` tests a deployment | 208/208 mapped; preflight runs it |
| `_dev/OPEN-ITEMS.md` | Facts and decisions that need the practice | Updated 2026-10-14 |

## Questions that keep coming up

- **Why not more area pages?** Eight exist. City searches are answered by the map pack;
  the category, records and reviews move that, not pages.
- **Why no fee on the site?** The practice has not published one. MDVIP affiliates nearby
  do; the Medicare guide answers the cost question without a number.
- **Why does an old URL take two hops on the main domain?** Vercel strips the trailing
  slash before applying redirects. Both hops are permanent; Google follows them.
- **Is the similarly named practice a problem?** No: dissolved in 2009 and 2010, no
  listing. Do not name it anywhere.

## Facts every file must use

Legacy Medical (legal name Legacy Medical PLLC), 11380 Prosperity Farms Road, Suite 114,
Palm Beach Gardens, FL 33410. (561) 834-9280, fax (561) 834-9279,
info@legacymedicalpalmbeach.com. Monday to Thursday 9 AM to 5 PM, Friday 9 AM to 2 PM.
Dr. Yana Shtern, MD, board-certified in internal medicine and nephrology (ABIM),
NPI 1497940852, FL license ME114615, privileges at Jupiter Medical Center and Palm Beach
Gardens Medical Center. Team: Yan Konevsky, RN. Membership fee not published.
