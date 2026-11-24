#!/usr/bin/env python3
"""Write one funny single-line developer excuse to /output/entry.txt.

The excuse is written fresh in this session, inside the write call below.
Gate: UTF-8 text, 1-200 characters, exactly one line, not only whitespace.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# The excuse itself: production didn't break anything -- it just took away
# the mock data that was quietly holding the whole thing together.
EXCUSE = "Production didn't break my code, it just removed the mock data holding it together."


def main() -> int:
    # Self-validation before writing.
    if not (1 <= len(EXCUSE) <= 200):
        print(f"FAIL: length {len(EXCUSE)} not in 1..200", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("FAIL: excuse contains a newline", file=sys.stderr)
        return 1
    if not EXCUSE.strip():
        print("FAIL: excuse is only whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)

    # Read-back verification: the file must contain exactly what we wrote.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")  # raises if the file is not valid UTF-8
    if written != EXCUSE:
        print("FAIL: read-back mismatch", file=sys.stderr)
        return 1
    if len(written.splitlines()) != 1:
        print("FAIL: output is not exactly one line", file=sys.stderr)
        return 1
    if raw != EXCUSE.encode("utf-8"):
        print("FAIL: byte-level read-back mismatch", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(written)} characters to {OUTPUT_PATH}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
