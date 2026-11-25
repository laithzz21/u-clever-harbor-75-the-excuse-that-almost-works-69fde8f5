#!/usr/bin/env python3
"""make.fun entry: The Excuse That Almost Works.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT if set)
and prints only the entry line to stdout.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os

ENTRY_TEXT = "Sorry, landlord's doing the gas safety check this morning and someone has to be in, I'll log on after."


def validate(text: str) -> None:
    """The brief requires one line, at most 20 words, 1-140 characters."""
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text.split()) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(text.split())}")


def resolve_output_path() -> str:
    """$MAKEFUN_OUTPUT may be a file path or a directory; default /output/entry.txt.

    A value ending in .txt (or naming an existing file) is used as the file
    path itself; anything else is treated as a directory holding entry.txt.
    """
    target = os.environ.get("MAKEFUN_OUTPUT")
    if target:
        if target.endswith(".txt") or os.path.isfile(target):
            return target
        return os.path.join(target, "entry.txt")
    return "/output/entry.txt"


def main() -> int:
    validate(ENTRY_TEXT)
    out_path = resolve_output_path()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY_TEXT:
            raise RuntimeError("verification failed: written file differs from entry text")
    print(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
