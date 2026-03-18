#!/usr/bin/env python3
"""
Build a zh-CN term index from the Japanese source docs and glossary shards.

Outputs:
  - translation/zh-CN/index_terms.csv
  - translation/zh-CN/index_terms.summary.json

The goal is not to fully machine-translate chapters, but to freeze a canonical
translation for structured source phrases that appear in headings, bold labels,
link texts, and glossary-style definition lines.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import yaml


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
GLOSSARY_DIR = ROOT / "translation" / "zh-CN" / "glossary"
OUT_CSV = ROOT / "translation" / "zh-CN" / "index_terms.csv"
OUT_SUMMARY = ROOT / "translation" / "zh-CN" / "index_terms.summary.json"

SOURCE_KIND_ORDER = ["term_def", "heading", "link_text", "bold", "admonition"]


@dataclass
class GlossaryEntry:
    source_term: str
    canonical_zh_cn: str
    domain: str
    preferred: bool
    source_type: str
    source_refs: List[str]
    notes: str = ""
    aliases: List[str] = field(default_factory=list)


def iter_markdown_files() -> Iterable[Path]:
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("docs/zh-CN/"):
            continue
        yield path


def normalize_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\{#.*?\}", "", text)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip(" -*_`|>")
    text = re.sub(r"^[\W_]+", "", text)
    text = re.sub(r"[\s:：\-]+$", "", text)
    return text


def line_number_for_offset(content: str, offset: int) -> int:
    return content.count("\n", 0, offset) + 1


def extract_candidates(path: Path) -> Iterable[Tuple[str, str, str]]:
    content = path.read_text(encoding="utf-8")
    rel_path = path.relative_to(ROOT).as_posix()

    patterns = [
        ("heading", re.compile(r"^(#{1,6})\s+(.+)$", re.M), 2),
        ("term_def", re.compile(r"^- \*\*([^*\n]{1,120})\*\*:", re.M), 1),
        ("link_text", re.compile(r"\[([^\]\n]{2,120})\]\((?!https?://|mailto:|tel:)[^)]+\)"), 1),
        ("bold", re.compile(r"\*\*([^*\n]{2,120})\*\*"), 1),
        ("admonition", re.compile(r"^(?:!!!|\?\?\?)\s+\w+\s+\"([^\"]{2,120})\"", re.M), 1),
    ]

    for kind, pattern, group in patterns:
        for match in pattern.finditer(content):
            raw = normalize_text(match.group(group))
            if len(raw) < 2:
                continue
            line = line_number_for_offset(content, match.start(group))
            yield kind, raw, f"{rel_path}:{line}"


def load_glossary() -> Dict[str, GlossaryEntry]:
    entries: Dict[str, GlossaryEntry] = {}

    for path in sorted(GLOSSARY_DIR.glob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for item in data.get("entries", []):
            entry = GlossaryEntry(
                source_term=item["source_term"],
                canonical_zh_cn=item["canonical_zh_cn"],
                domain=item.get("domain", "general"),
                preferred=bool(item.get("preferred", False)),
                source_type=item.get("source_type", "repo_context"),
                source_refs=list(item.get("source_refs", [])),
                notes=item.get("notes", ""),
                aliases=list(item.get("aliases", [])),
            )
            entries[entry.source_term] = entry
            for alias in entry.aliases:
                entries.setdefault(alias, entry)

    return entries


def compose_translation(term: str, glossary: Dict[str, GlossaryEntry]) -> Tuple[str, str, List[str]]:
    if term in glossary:
        return glossary[term].canonical_zh_cn, "direct", [glossary[term].source_term]

    matched_terms: List[str] = []
    composed = term
    for source_term, entry in sorted(
        glossary.items(),
        key=lambda kv: (-len(kv[0]), kv[0]),
    ):
        if len(source_term) < 2:
            continue
        if source_term in composed:
            composed = composed.replace(source_term, entry.canonical_zh_cn)
            matched_terms.append(entry.source_term)

    if matched_terms and composed != term:
        status = "composed"
    elif matched_terms:
        # Official English names are often intentionally preserved as-is.
        status = "constrained"
    else:
        status = "untranslated"
    return composed, status, sorted(set(matched_terms))


def source_kind_rank(kind: str) -> int:
    try:
        return SOURCE_KIND_ORDER.index(kind)
    except ValueError:
        return len(SOURCE_KIND_ORDER)


def main() -> None:
    glossary = load_glossary()
    occurrences: Dict[str, Dict[str, object]] = {}

    for path in iter_markdown_files():
        for kind, raw, ref in extract_candidates(path):
            item = occurrences.setdefault(
                raw,
                {
                    "source_term": raw,
                    "source_kinds": set(),
                    "occurrences": [],
                },
            )
            item["source_kinds"].add(kind)
            item["occurrences"].append(ref)

    rows = []
    summary = {
        "glossary_entries": len({v.source_term for v in glossary.values()}),
        "index_terms": 0,
        "direct": 0,
        "composed": 0,
        "constrained": 0,
        "untranslated": 0,
    }

    for raw, item in sorted(occurrences.items()):
        translation, status, matched_terms = compose_translation(raw, glossary)
        kinds = sorted(item["source_kinds"], key=source_kind_rank)
        refs = item["occurrences"][:8]
        rows.append(
            {
                "source_term": raw,
                "canonical_zh_cn": translation,
                "status": status,
                "source_kinds": "|".join(kinds),
                "matched_terms": "|".join(matched_terms),
                "occurrences": "|".join(refs),
            }
        )
        summary["index_terms"] += 1
        summary[status] += 1

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "source_term",
                "canonical_zh_cn",
                "status",
                "source_kinds",
                "matched_terms",
                "occurrences",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    OUT_SUMMARY.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
