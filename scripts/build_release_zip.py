#!/usr/bin/env python3
"""Build a release zip for product-factor-skills using only Python standard library."""
from __future__ import annotations

import argparse
from pathlib import Path
import zipfile

EXCLUDE_DIRS = {".git", "__pycache__", "tmp", ".pytest_cache", ".mypy_cache"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_dir():
            continue
        if any(part in EXCLUDE_DIRS for part in path.relative_to(root).parts):
            continue
        if path.suffix in EXCLUDE_SUFFIXES:
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build product-factor-skills release zip")
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    out = Path(args.out or root.parent / f"product-factor-skills-{version}.zip").resolve()

    if out.exists():
        out.unlink()

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        base = root.name
        for path in iter_files(root):
            zf.write(path, Path(base) / path.relative_to(root))

    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
