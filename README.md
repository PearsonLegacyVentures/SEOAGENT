# SEOAGENT

A practical local-search operating system for Pearson Legacy Ventures.

SEOAGENT turns real search data into a controlled action queue. It is designed to improve existing websites before adding new pages, keep one clear page owner per search intent, and connect local-search work to measurable outcomes.

## Pilot

The first live pilot is **Tranquilitas Day Spa / MassageBahamas.com**.

- Website: https://www.massagebahamas.com
- Website repo: `PearsonLegacyVentures/massagebahamas.com`
- Search Console property: `https://www.massagebahamas.com/`
- Primary market: Nassau, The Bahamas
- Core offers: in-spa massage, mobile massage, couples massage, beach massage, facials, spa packages and related wellness services

## What this system does

1. Pull or import Google Search Console query/page data.
2. Rank opportunities by demand, current position and click-through performance.
3. Detect when multiple pages compete for the same query.
4. Assign one primary page to each important commercial intent.
5. Decide whether to **KEEP, IMPROVE, MERGE, CREATE or IGNORE**.
6. Audit Google Business Profile information against the real business and local competitors.
7. Produce Google Business Profile posts tied to real services and landing pages.
8. Run a compliant review-request workflow without review gating.
9. Measure results after changes instead of publishing blindly.

## Operating order

Run the system in this order:

`GSC baseline -> query ownership -> technical/indexation checks -> improve existing pages -> GBP -> reviews -> GBP posts -> new pages only when justified -> remeasure`

The default bias is **improve before create**.

## Commands

The markdown files in `commands/` are operating playbooks. They are written to be usable with ChatGPT, Claude Code or a human SEO operator rather than being tied to one AI product.

- `gsc-opportunity.md` — find the fastest ranking/click opportunities.
- `keyword-map.md` — assign search intents to canonical pages.
- `page-improve.md` — improve an existing page without creating more overlap.
- `gbp-audit.md` — audit and optimize a Google Business Profile.
- `gbp-posts.md` — create useful GBP posts with traceable links.
- `reviews.md` — request public reviews and private feedback without rating-gating.

## Data

`data/<site>/` stores dated baselines and query-ownership decisions. These are evidence, not permanent assumptions. Refresh them after material changes.

## Scripts

The scripts in `code/` work with CSV exports from Search Console or compatible query/page datasets.

```bash
python3 code/rank_gsc_opportunities.py data.csv
python3 code/find_cannibalization.py query_page.csv
```

Expected columns are documented inside each script.

## Guardrails

- Do not generate pages simply because a keyword can be formed.
- Do not create near-identical city/service pages with only names swapped.
- Do not add GBP categories or services the business does not genuinely offer.
- Do not route only happy customers to Google Reviews. Public review access must not depend on the customer's rating or sentiment.
- Do not make unsupported medical, pricing, availability or business-performance claims.
- Do not change canonical ownership without checking current Search Console evidence and indexation.

## Origin and license

This repository adapts useful structural ideas from Jono Catliff's 2026 `local-seo-agent` project, supplied by the repository author under the MIT License. See `NOTICE.md` and `LICENSE`.

The implementation here is substantially modified for Pearson Legacy Ventures, including Search Console-first prioritization, explicit query ownership, existing-site improvement, Caribbean market context and a non-gated review workflow.
