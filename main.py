#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. Standard library only, no network.
"""

from pathlib import Path

ENTRY = (
    "Every morning there is a second cup of tea on the old woman's "
    "windowsill, untouched, still warm. No one has ever seen her put "
    "it there, or seen anyone drink it. By noon, the cup is always empty."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise SystemExit("entry must be 1-280 non-blank characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {out}")


if __name__ == "__main__":
    main()
