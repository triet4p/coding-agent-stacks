#!/usr/bin/env python3
"""Layout budget gate: measure template repetition in a build script.

Usage:
    python check_layout_budget.py build_module_07.py
    python check_layout_budget.py build_module_07.py --max-share 20 --json

Counts `T.<template>(` calls, reports share per template, the longest run of
consecutive identical templates, and table share. Exit 1 on any violation.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

CALL = re.compile(r"\bT\.([a-z][a-z0-9_]*)\(")
IGNORED = {"header", "footer", "notes", "set_profile"}


def analyse(path: Path):
    src = path.read_text(encoding="utf-8", errors="replace")
    seq = [m for m in CALL.findall(src) if m not in IGNORED]
    counts = Counter(seq)
    total = len(seq)
    runs = []
    if seq:
        cur, prev = 1, seq[0]
        for name in seq[1:]:
            if name == prev:
                cur += 1
            else:
                runs.append((cur, prev))
                cur, prev = 1, name
        runs.append((cur, prev))
    longest = max(runs, default=(0, ""))
    return counts, total, longest, runs


def main() -> int:
    ap = argparse.ArgumentParser(description="Measure template repetition in a build script.")
    ap.add_argument("build_script", type=Path)
    ap.add_argument("--max-share", type=float, default=25.0, help="max %% of slides per template")
    ap.add_argument("--max-run", type=int, default=2, help="max consecutive identical templates")
    ap.add_argument("--max-table-share", type=float, default=20.0)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not args.build_script.exists():
        print(f"missing file: {args.build_script}", file=sys.stderr)
        return 2

    counts, total, longest, runs = analyse(args.build_script)
    if not total:
        print("no T.<template>( calls found", file=sys.stderr)
        return 2

    rows = []
    violations = []
    for name, n in counts.most_common():
        share = 100.0 * n / total
        rows.append({"template": name, "count": n, "share": round(share, 1)})
        if share > args.max_share:
            violations.append(f"{name}: {share:.1f}% > {args.max_share:g}%")
    table_share = 100.0 * counts.get("data_table", 0) / total
    if table_share > args.max_table_share:
        violations.append(f"data_table: {table_share:.1f}% > {args.max_table_share:g}%")
    for length, name in runs:
        if length > args.max_run and not (name == "ui_evidence" and length <= 3):
            violations.append(f"run of {length} × {name} (max {args.max_run})")

    result = {
        "file": str(args.build_script),
        "calls": total,
        "templates": len(counts),
        "top": rows[:8],
        "longest_run": {"template": longest[1], "length": longest[0]},
        "table_share": round(table_share, 1),
        "violations": violations,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{result['file']}  calls={total}  templates={len(counts)}")
        for r in rows[:8]:
            print(f"  {r['template']:<24} {r['count']:>3}  {r['share']:>5.1f}%")
        print(f"  longest run: {longest[0]} × {longest[1] or '-'}")
        print(f"  table share: {table_share:.1f}%")
        for v in violations:
            print(f"  VIOLATION  {v}")
        if not violations:
            print("  OK  layout budget")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
