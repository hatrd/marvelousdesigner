#!/usr/bin/env python3
"""
Run one Codex sub-agent to translate a single chapter into zh-CN.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def build_prompt(source_path: str, target_path: str) -> str:
    return (
        "Translate exactly one chapter from Japanese to Simplified Chinese. "
        "Read translation/zh-CN/chapter-worker.md, "
        "translation/zh-CN/translation-rules.md, "
        "translation/zh-CN/sources.md, and "
        "translation/zh-CN/glossary/*.yml before editing. "
        f"Source file: {source_path}. "
        f"Target file: {target_path}. "
        "Requirements: edit only the target file; preserve Markdown, HTML structure, "
        "and link targets; obey the glossary for fixed terms; do not modify any other file; "
        "and report terminology conflicts or risky links in the final message."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_path")
    parser.add_argument("target_path")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = args.output
    if output is None:
        stem = Path(args.target_path).as_posix().replace("/", "_")
        output = f"/tmp/{stem}.out"

    cmd = [
        "codex",
        "exec",
        "-C",
        str(root),
        "--full-auto",
        "--ephemeral",
        "--output-last-message",
        output,
        build_prompt(args.source_path, args.target_path),
    ]

    result = subprocess.run(cmd)
    if result.returncode != 0:
        return result.returncode

    try:
        print(Path(output).read_text(encoding="utf-8"))
    except FileNotFoundError:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
