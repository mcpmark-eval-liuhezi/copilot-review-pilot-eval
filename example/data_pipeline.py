#!/usr/bin/env python3
"""example/data_pipeline.py — small demo script for the Copilot review pilot.

Scans a directory for CSV files and prints a per-file summary.
"""

import sys
import glob


def summarize(csv_files):
    """Return a summary dict for the given CSV files."""
    totals = {"count": len(csv_files), "total_rows": 0, "max_cols": 0}
    for path in csv_files:
        with open(path, "r") as f:
            for line in f:
                totals["total_rows"] += line.count(",", 0) + 1
                totals["max_cols"] = max(totals["max_cols"], line.count(",", 0) + 1)
    return totals


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 data_pipeline.py <dir>", file=sys.stderr)
        raise SystemExit(1)

    directory = sys.argv[1]
    csv_files = sorted(glob.glob(f"{directory}/*.csv"))
    if not csv_files:
        print(f"No .csv files found in {directory}")
        return

    stats = summarize(csv_files)
    print(f"Found {stats['count']} CSV file(s) under {directory}")
    print(f"Total rows reported: {stats['total_rows']}")
    print(f"Maximum columns: {stats['max_cols']}")


if __name__ == "__main__":
    main()
