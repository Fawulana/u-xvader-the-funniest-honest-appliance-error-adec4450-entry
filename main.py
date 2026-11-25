#!/usr/bin/env python3
"""Writes the funniest honest appliance error to /output/entry.txt.

Deterministic, stdlib-only, offline: the line is a fixed constant and the
output is byte-identical on every run.
"""

import os

LINE = "ERROR 04: I have stopped mid-cycle. One sock is missing. I know where it is. I am not telling you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the line, no trailing newline: the gate counts the
    # file's characters, so the file must be the line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
