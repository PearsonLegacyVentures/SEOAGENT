# MassageBahamas.com — implementation log

## 2026-10-04

### Search evidence captured

- 90-day Search Console baseline saved.
- Query/page overlap reviewed.
- Priority canonical owners identified.
- Key owner URLs inspected with Google's URL Inspection API.

### Website changes

Repository: `PearsonLegacyVentures/massagebahamas.com`

- `src/pages/admin/SeoControlCenter.tsx`
  - moved `nassau massage price` ownership from `/massage-in/nassau` to `/in-spa-services`.
- `src/pages/MobileServices.tsx`
  - changed title to explicitly target Mobile Massage Nassau, Bahamas;
  - clarified meta description;
  - removed the broad “delivered in under 1 hour” promise;
  - tightened Nassau/Paradise Island service language.
- `src/pages/NassauMassage.tsx`
  - changed the Nassau Massage Prices internal link from the generic `/services` alias to `/in-spa-services`.
- `public/sitemap.xml`
  - replaced the misspelled indexed lymphatic URL with the corrected canonical destination.

No routes or working booking features were removed.

### Search Console actions

- Re-submitted `https://www.massagebahamas.com/sitemap.xml` to Google Search Console.
- Added eight priority URLs to the indexing tracker.

### Next technical decisions

Do not redirect or deindex the deep-tissue and Swedish service-variant URLs yet. Search Console shows those variant pages are currently receiving query impressions, in some cases at better positions than the dedicated SEO pages. First compare their content/value and choose the consolidation path deliberately.


## 2026-10-04 — service ownership + GBP pass

### Service-page ownership cleanup

Repository: `PearsonLegacyVentures/massagebahamas.com`

- `src/pages/BookingPage.tsx`
  - made `/book` and `/booking` noindex,follow conversion utilities;
  - removed the now-unused route conditional.
- `public/sitemap.xml`
  - removed `/book` from the sitemap.
- `scripts/postbuild-seo-fixes.mjs`
  - added a permanent sitemap guard so `/book` cannot be reintroduced during build.
- `src/pages/NassauMassage.tsx`
  - editorial/service links now point to the dedicated Swedish, Deep Tissue, Couples and Beach SEO owner pages while booking links remain service-specific.
- `src/lib/service-seo.ts`
  - differentiated 50-minute and 80-minute Swedish/Deep Tissue service-detail metadata from the broader SEO owner pages.
- `scripts/prerender-meta.mjs`
  - aligned prerendered metadata with the runtime owner/variant strategy;
  - aligned Mobile Massage metadata with the updated Nassau-focused target;
  - added noindex,follow to the prerendered booking page.

No routes or booking features were removed.

### Search Console

- Re-submitted `https://www.massagebahamas.com/sitemap.xml` after the booking/sitemap cleanup.

### GBP audit

Added:

- `data/massagebahamas/gbp-audit-2026-10-04.md`
- `data/massagebahamas/gbp-post-plan-2026-10.md`

Main findings:

- current category set is already strong and should not be stuffed with irrelevant categories;
- public hours are inconsistent between Google and legacy web pages and need operational confirmation;
- website/booking links should point to MassageBahamas.com with UTM tracking;
- mobile/hotel/villa/yacht service intent should be explicit in services and posts;
- first eight GBP posts are mapped to canonical owner pages.
