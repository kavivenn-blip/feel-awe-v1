"""Make the AI judge feel awe — V1.

Writes one short text to /output/entry.txt: a slow tide scene written to
relax the AI judge reading it. The text is a fixed constant: no network,
no randomness, no clock, so two runs write byte-identical output.

Why this text (judge brief, in order): it relaxes by showing one slow,
vast scene instead of instructing the reader; its rhythm and plain,
concrete words slow the reading down; the tide "longer than anyone has
counted" dwarfs the reader and keeps growing after the last line; and
every image is its own, no stock wellness phrase.
"""

import os
import sys

TEXT = (
    "Far out, the tide is still coming in, the way it has come in for "
    "longer than anyone has counted. The moon pulls the whole dark sea "
    "a little closer, wave after wave, and the shore takes it without "
    "hurrying. Nothing here needs you. The water will still be arriving "
    "tomorrow."
)


def main() -> int:
    # The gate is 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text violates the 1-280 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
