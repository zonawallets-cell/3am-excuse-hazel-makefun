"""The 3 AM Excuse — make.fun entry.

Writes one line (93 characters): the most creative excuse a hardware
wallet gives for refusing to sign a transaction at 3 AM, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.

Why this line: the wallet is an exhausted employee with boundaries.
It clocked out at midnight, so at 3 AM it is no longer a wallet at all
— it is "a very expensive brick with a grudge and a union card". The
joke turns on the hour itself (it could not be pasted onto 3 PM), the
voice is the device's own, and the final beat — the union card — lands
the employee angle in three words.
"""

import os

LINE = (
    "I clocked out at midnight. At 3 AM I'm a very expensive brick "
    "with a grudge and a union card."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-200 chars, not only whitespace,
    single line, and free of control characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()
