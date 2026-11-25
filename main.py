#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one single-line text message (89 characters) to /output/entry.txt:
the phone battery's last text to the charger it waited for all day.

The line: the battery waited all day at 1%, and now it is dying
mid-text -- the message itself cuts off mid-word, performing the death
it describes. The turn pays off in the final characters, which is the
joke: "just know I hate--" never gets finished.

Standard library only. Deterministic: same bytes on every run. No network,
no randomness, no clock, no input files.
"""

import os

LINE = "I waited all day at 1% and now I'm dying mid-text, so if this cuts off, just know I hate\u2014"


def main() -> None:
    # Gate self-check, mirroring RULES: 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, one line, 89 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify: the artifact on disk must be exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
