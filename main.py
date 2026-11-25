"""Worst App Idea Ever Pitched — entry writer.

Writes a single-sentence pitch (<=240 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output when the variable is unset).
"""

import os

ENTRY = (
    "Meet Doorknob, the app that lets busy professionals rate, review, and "
    "follow their favorite doorknobs, so you'll never turn a handle again "
    "without knowing its grip, spin, and five-star potential."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
