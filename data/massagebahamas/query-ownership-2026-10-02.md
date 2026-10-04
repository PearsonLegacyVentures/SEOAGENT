# MassageBahamas.com — query ownership review

Date: 2026-10-02 settled GSC data

## High-priority intent leakage

### `massage nassau bahamas`

Total observed impressions across material URLs: **435**.

| Page | Impressions | Avg position |
|---|---:|---:|
| `/` | 221 | 55.04 |
| `/massage-in/nassau` | 45 | 50.76 |
| `/book` | 43 | 78.74 |
| `/gallery` | 30 | 62.20 |
| `/best-massage-nassau-bahamas` | 26 | 55.73 |
| `/in-spa-services` | 20 | 75.65 |

**Intended owner:** `/massage-in/nassau`

**Action:** IMPROVE owner + reduce competing commercial signals from utility/support pages. Do not create another Nassau massage page.

### `mobile massage nassau bahamas`

Total observed impressions across material URLs: **297**.

Top observed pages included the homepage, Exuma page, Nassau page, a mobile deep-tissue service page, gallery and Antigua page. The intended `/mobile-services` owner was not among the material top pages in this cut.

**Intended owner:** `/mobile-services`

**Action:** URL-inspect owner first; then strengthen ownership and internal linking if indexable.

### `nassau massage price`

Total observed impressions across material URLs: **258**.

The homepage, membership page, Nassau page and booking page all receive impressions. The site governance files are also inconsistent: the route registry targets `/in-spa-services` for price intent while the current SEO Control Center assigns `nassau massage price` to `/massage-in/nassau`.

**Proposed owner:** `/in-spa-services`

**Action:** resolve internal governance conflict before editing content.

### `deep tissue massage near me`

Total observed impressions across material URLs: **217**.

The homepage receives more impressions and a better average position than the dedicated `/deep-tissue-massage` page. A separate `/service-page/deep-tissue` URL also competes.

**Intended owner:** `/deep-tissue-massage`

**Action:** inspect indexation/canonical state, compare both deep-tissue pages, then consolidate signals.

### `couples massage nassau bahamas`

Total observed impressions across material URLs: **210**.

Homepage, Nassau, booking, gallery and contact pages all receive material impressions, while the dedicated `/couples-massage-nassau` page is not a leading URL in this data cut.

**Intended owner:** `/couples-massage-nassau`

**Action:** inspect owner, strengthen relevance/internal links, then reduce overlap.

## Technical observations

Search Console still reports some trailing-slash variants such as `/massage-in/nassau/` and `/spa-membership-nassau/` even though the current Cloudflare worker is designed to 301 non-root trailing slashes to the clean URL. Treat this as an inspection item before changing routing; it may reflect historical data or canonical processing rather than a current redirect failure.

The sitemap currently contains the legacy misspelled lymphatic URL `service-page/lympahtic-drainage-massage-nassau-bahamas` even though current site governance defines that URL as a redirect to the corrected canonical slug. The sitemap should ultimately contain the canonical destination, not the redirecting legacy URL.
