#!/usr/bin/env python3
"""
Export a chapter inventory for zh-CN translation work.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
OUT_CSV = ROOT / "translation" / "zh-CN" / "chapters.csv"


def main() -> None:
    rows = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("docs/zh-CN/"):
            continue
        text = path.read_text(encoding="utf-8")
        title = ""
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        target = Path("docs/zh-CN") / path.relative_to(DOCS_DIR)
        rows.append(
            {
                "source_path": rel,
                "target_path": target.as_posix(),
                "title": title,
                "section": path.relative_to(DOCS_DIR).parts[0],
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["source_path", "target_path", "title", "section"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {OUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
