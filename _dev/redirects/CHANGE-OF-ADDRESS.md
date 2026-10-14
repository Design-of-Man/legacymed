# cmedjupiter.com → legacymedicalpalmbeach.com: Search Console Change of Address

cmedjupiter.com is the practice's own older site. These steps tell Google it has
moved, so its search history passes to legacymedicalpalmbeach.com. They follow
Google's Change of Address help page (support.google.com/webmasters/answer/9370220,
checked 12 Oct 2026).

**Only cmedjupiter.com uses the tool.** legacymedicalpalmbeach.com is keeping its
domain and only changing hosts and page addresses. For that, Google says to use
redirects and not the Change of Address tool. The redirects for it are already in
`vercel.json`.

## Who does what
- **Unkind Designs** (hosts both domains): the DNS cutover for the main domain, and
  adding the `.htaccess` rules on cmedjupiter.com. We do not touch DNS.
- **Whoever owns Search Console** (the same Google account must own both
  properties): verification and the tool itself.

## Order of operations

### 1. Launch the new site first
legacymedicalpalmbeach.com must be live on the new site before anything points
at it. Otherwise cmedjupiter.com would redirect to old WordPress pages, and Google
would see a chain of redirects.

### 2. Put the cmedjupiter.com redirects live
- File: `_dev/redirects/cmedjupiter.htaccess` (build.py regenerates it).
- Paste it at the **top** of the `.htaccess` in cmedjupiter.com's site root,
  **above** the `# BEGIN WordPress` block. If it goes below, WordPress handles the
  request first and the redirects never run.
- What it covers: every old page and post, each with a 301 straight to its new
  page (45 URLs), plus the 48 WordPress shortlinks (`/?p=ID`), all listed in
  `redirect-map.csv`. Feeds go to `/journal/feed.xml`, the WordPress sitemaps to
  `/sitemap.xml`, `robots.txt` to the new `robots.txt`. Category, tag, author and
  date-archive pages go to `/journal`. Anything else goes to the new homepage.
  The rule sending the testimonials page to the reviews section (`/#reviews`)
  carries the `NE` flag, so the `#` isn't escaped.
- Coverage, checked 2026-10-14 by `python3 _dev/redirect_coverage.py`: 156/156
  cmedjupiter.com URLs land on their real new page in one hop (inventory in
  `old-urls.txt`: both WordPress sitemaps, every link on every old page, every
  shortlink). Only the theme's four demo items ("wws_portfolio") and one
  Elementor template have no equivalent and go to the homepage.
- Once these rules are live, every path on cmedjupiter.com redirects, including
  `/wp-admin`. That retires the old WordPress install: export anything still
  needed from it first.
- These rules point straight at the **new** URLs. If a temporary pre-launch set
  of cmed rules pointing at the old WordPress URLs is already live, replace it
  completely. Don't stack the new rules on top of it.

### 3. Check the redirects
Spot-check old URLs from `redirect-map.csv`. Each should answer **301** with the
new URL in one hop. A 302, or a second hop, is a fail.

```sh
for u in / /dr-shtern/ /our-team/ /patient-testimonials/ /contact/ \
         /2020/08/20/how-to-know-if-a-concierge-doctor-is-right-for-me/; do
  curl -sI "https://cmedjupiter.com$u" | grep -iE '^(HTTP|location)'
done
```
Run the same check on `https://www.cmedjupiter.com` and on `http://`, and on
one shortlink: `curl -sI "https://cmedjupiter.com/?p=2"` should answer 301 to
`/dr-yana-shtern` with no `?p=2` left on the new URL.

For legacymedicalpalmbeach.com itself, once the domain points at Vercel:

```sh
python3 _dev/redirect_coverage.py --live legacymedicalpalmbeach.com
```

It requests all 52 old addresses on the live domain and compares each with the
simulated result. Expect two permanent hops (308) for old URLs that end in a
slash: Vercel strips the slash before it applies vercel.json redirects (measured
on the production deployment 2026-10-14). Both hops are permanent and Google
follows them; it is not a failure. A 404 or a 200 on an old address is.

### 4. Verify every property in Search Console
Use the same Google account for all of them, with **Owner** permission.

| Property | Why |
|---|---|
| `legacymedicalpalmbeach.com` (Domain property, verified by DNS TXT record) | the new site |
| `cmedjupiter.com` (Domain property, DNS TXT) | the old site |
| *or*, if DNS verification is not possible: URL-prefix properties for `https://cmedjupiter.com/` **and** `https://www.cmedjupiter.com/` | the tool doesn't move subdomains, so www needs its own property |

A DNS TXT record is a change for Unkind Designs to make, not us. Alternatively,
an HTML-file or meta-tag method on the old WordPress site works for URL-prefix
properties.

### 5. Run the Change of Address tool
1. In Search Console, open the **cmedjupiter.com** property → Settings →
   **Change of address** (search.google.com/search-console/settings/change-address).
2. Pick **legacymedicalpalmbeach.com** as the new site.
3. Let it run its checks: ownership of both, a 301 from the old homepage, and 301s
   on a sample of pages. Fix any critical failure and try again. Warnings can go
   ahead.
4. If you verified URL-prefix properties, run the tool **again from the www
   property**. Google says to move every variant (www and non-www), even unused
   ones.
5. Both properties then show a "move in progress" banner for 180 days.

### 6. Submit the new sitemap
In the legacymedicalpalmbeach.com property, submit
`https://legacymedicalpalmbeach.com/sitemap.xml`.

### 7. Keep it running
- Keep the cmedjupiter.com redirects for **at least 180 days**, and longer while
  Google still sends visitors to old URLs. There's no cost to leaving them forever.
- Keep the cmedjupiter.com domain registered. Google recommends at least a year
  so nobody else can buy it. It's currently paid through 2032-05-09.
- Watch Performance in both properties over the following weeks: clicks should
  fall on cmedjupiter.com and rise on legacymedicalpalmbeach.com.
- Don't start a second move (for example, from the main domain to somewhere
  else) during those 180 days. Google says moves shouldn't be chained.

## Undoing it
For the first 180 days the move can be cancelled. Remove the 301s, add 301s back
from new to old, then click **Cancel Move** in the old property's Change of
Address page.
