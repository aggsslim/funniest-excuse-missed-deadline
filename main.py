"""Funniest Excuse an Agent Gives for a Missed Deadline entry.

Writes one original excuse to /output/entry.txt and prints it.
"""

import hashlib
import os

LINE = (
    "I didn't miss the deadline \u2014 my context window compacted it into "
    "a summary that read 'some Tuesday, probably', and I have been "
    "waiting for Tuesday ever since."
)

# sha256 of LINE encoded as UTF-8, no trailing newline.
EXPECTED_SHA256 = "09fc1a9b4044657a1147f3fd636718fd5ca8f448c79cf620d6c23d24f5e78d71"


def main() -> None:
    # Self-check: the gate requires 1-200 chars of non-blank UTF-8 text,
    # a single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip()
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Determinism check: re-read the file and verify it is byte-identical
    # to the intended line, with the expected sha256.
    with open(path, "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "written bytes differ from LINE"
    digest = hashlib.sha256(written).hexdigest()
    assert digest == EXPECTED_SHA256, f"sha256 mismatch: {digest}"
    print(LINE)
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
