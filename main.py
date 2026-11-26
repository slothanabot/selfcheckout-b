#!/usr/bin/env python3
"""The Self-Checkout Is Judging You (account B).

Writes one self-checkout remark to $MAKEFUN_OUTPUT_DIR/entry.txt,
or /output/entry.txt when the variable is unset.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.

The joke: the machine totals the shop in its smug flat voice, then
lands the sting -- it has noticed the ice cream is dinner, again,
and it is keeping count.
"""

import os

LINE = "That will be $47.83, and yes, I noticed the ice cream is for dinner. Again."


def build_line() -> str:
    """Return the remark, validated as a single in-range line."""
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise SystemExit("entry must be one non-empty line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    return line


def write_entry(line: str) -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs")
    return written


def main() -> None:
    written = write_entry(build_line())
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
