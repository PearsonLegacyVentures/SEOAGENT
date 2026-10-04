#!/usr/bin/env python3
"""Find queries receiving material impressions across multiple URLs.

Required columns:
    query, page, clicks, impressions, ctr, position

This reports possible cannibalization / intent leakage. Multiple pages ranking for
one query is not automatically a problem; the output is a review queue.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict


def number(value: str) -> float:
    raw = (value or "0").strip().replace(",", "").replace("%", "")
    return float(raw or 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--min-page-impressions", type=float, default=3)
    parser.add_argument("--min-query-impressions", type=float, default=20)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    grouped: dict[str, list[dict]] = defaultdict(list)
    with open(args.csv_path, newline="", encoding="utf-8-sig") as f:
        for item in csv.DictReader(f):
            query = (item.get("query") or item.get("Query") or "").strip()
            page = (item.get("page") or item.get("Page") or "").strip()
            if not query or not page:
                continue
            impressions = number(item.get("impressions") or item.get("Impressions") or "0")
            if impressions < args.min_page_impressions:
                continue
            grouped[query].append(
                {
                    "page": page,
                    "impressions": impressions,
                    "clicks": number(item.get("clicks") or item.get("Clicks") or "0"),
                    "position": number(item.get("position") or item.get("Position") or "0"),
                }
            )

    candidates = []
    for query, pages in grouped.items():
        total = sum(p["impressions"] for p in pages)
        if len(pages) >= 2 and total >= args.min_query_impressions:
            pages.sort(key=lambda p: p["impressions"], reverse=True)
            candidates.append((total, query, pages))

    candidates.sort(reverse=True)

    for total, query, pages in candidates[: args.limit]:
        print(f"\n{query} — {total:.0f} material impressions across {len(pages)} pages")
        for p in pages:
            print(
                f"  {p['impressions']:.0f} impr | {p['clicks']:.0f} clicks | "
                f"pos {p['position']:.2f} | {p['page']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
