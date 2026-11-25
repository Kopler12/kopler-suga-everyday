#!/usr/bin/env python3
"""Two-line explanation of a queue for a 10-year-old.

Writes the entry to /output/entry.txt (UTF-8, exactly two lines).
make.fun competition: u-suga-everyday-things-two-lines-longer-run-f8734479
"""

import os
import sys

LINE_1 = (
    "A queue is a human train where each person is a carriage, "
    "hitched to the one in front by nothing but patience."
)
LINE_2 = (
    "It maps how people line up in order like carriages on a track, "
    "but leaves out that a real train cannot shuffle, swap places, "
    "or leave, while people in a queue can."
)

MAX_CHARS = 400
OUT_PATH = "/output/entry.txt"


def build_entry():
    """Join the two lines into the exact entry text (no trailing newline)."""
    return LINE_1 + "\n" + LINE_2


def main():
    entry = build_entry()
    if not entry.strip():
        print("Refusing to write: entry is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if len(entry) > MAX_CHARS:
        print(
            f"Refusing to write: entry is {len(entry)} chars, over the "
            f"{MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        sys.exit(1)
    if entry.count("\n") != 1:
        print("Refusing to write: entry must be exactly two lines", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
