#!/usr/bin/env python3
"""Rank Google Search Console query opportunities from a CSV export.

Required columns:
    query, clicks, impressions, ctr, position

CTR may be provided as a decimal (0.02) or percent (2.0 / "2%").
The score is intentionally transparent and is only a sorting aid.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass


@dataclass
class Row:
    query: str
    clicks: float
    impressions: float
    ctr: float
    position: float


def number(value: str) -> float:
    raw = (value or "0").strip().replace(",", "")
    if raw.endswith("%"):
        return float(raw[:-1]) / 100
    return float(raw or 0)


def normalize_ctr(value: str) -> float:
    v = number(value)
    return v / 100 if v > 1 else v


def position_weight(position: float) -> float:
    if 4 <= position <= 10:
        return 1.00
    if 10 < position <= 20:
        return 0.90
    if 20 < position <= 30:
        return 0.70
    if 30 < position <= 40:
        return 0.45
    if 1 <= position < 4:
        return 0.35
    return 0.15


def score(row: Row) -> float:
    demand = math.log1p(max(row.impressions, 0))
    click_gap = max(0.15, 1 - min(max(row.ctr, 0), 1))
    return demand * position_weight(row.position) * click_gap


def bucket(position: float) -> str:
    if position <= 3:
        return "defend/CTR"
    if position <= 10:
        return "fast win"
    if position <= 20:
        return "page-one candidate"
    if position <= 30:
        return "medium"
    if position <= 40:
        return "longer-term"
    return "investigate"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--min-impressions", type=float, default=5)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    rows: list[Row] = []
    with open(args.csv_path, newline="", encoding="utf-8-sig") as f:
        for item in csv.DictReader(f):
            row = Row(
                query=(item.get("query") or item.get("Query") or "").strip(),
                clicks=number(item.get("clicks") or item.get("Clicks") or "0"),
                impressions=number(item.get("impressions") or item.get("Impressions") or "0"),
                ctr=normalize_ctr(item.get("ctr") or item.get("CTR") or "0"),
                position=number(item.get("position") or item.get("Position") or "0"),
            )
            if row.query and row.impressions >= args.min_impressions:
                rows.append(row)

    rows.sort(key=score, reverse=True)

    print("score\tbucket\tposition\timpressions\tclicks\tctr\tquery")
    for row in rows[: args.limit]:
        print(
            f"{score(row):.3f}\t{bucket(row.position)}\t{row.position:.2f}\t"
            f"{row.impressions:.0f}\t{row.clicks:.0f}\t{row.ctr:.2%}\t{row.query}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
