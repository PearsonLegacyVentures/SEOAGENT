# GSC Opportunity

## Goal

Turn Google Search Console evidence into a ranked action queue for an existing website.

## Inputs

- Search Console property
- preferred analysis window (default: trailing 90 settled days)
- business context file
- current route/canonical map if available

## Workflow

1. Pull site totals for clicks, impressions, CTR and average position.
2. Pull query-level data.
3. Pull page-level data.
4. Pull query + page data together.
5. Segment queries into:
   - positions 1–3: defend/CTR check;
   - positions 4–10: fastest ranking wins;
   - positions 11–20: page-one candidates;
   - positions 21–40: medium-term opportunities;
   - positions 40+: investigate relevance before investing.
6. Flag high-impression queries with unusually weak CTR.
7. For each important query, count how many URLs receive impressions.
8. Flag possible cannibalization or intent leakage when multiple material pages compete for the same query.
9. Map each important query to the page that should own it.
10. Return one action per cluster: KEEP, IMPROVE, MERGE, CREATE or IGNORE.

## Important interpretation rule

Multiple URLs receiving impressions for one query is not automatically harmful. Flag it for review when the pages have overlapping purpose or when Google's preferred page differs from the business's intended owner.

## Output

### Executive baseline

- date range
- clicks
- impressions
- CTR
- average position
- comparison to previous period where available

### Fastest opportunities

| Query | Impressions | Clicks | Position | Intended owner | Current issue | Action |
|---|---:|---:|---:|---|---|---|

### Cannibalization / intent leakage

| Query | Material ranking pages | Intended owner | Diagnosis | Action |
|---|---:|---|---|---|

### Page action queue

| Priority | URL | Action | Why | Measurement query |
|---:|---|---|---|---|

Do not recommend mass page creation before this pass is complete.
