"""The Moon Finally Answers Back.

Writes one line -- the Moon's comeback to everyone who has ever stared
up at it, wished on it, howled at it, and made it late-night promises --
to /output/entry.txt.

The line must be 1 to 240 characters of UTF-8 text. Stdlib only, no
network access.
"""

import os

LINE = (
    "You howl at me, wish on me, and make me 2 a.m. promises you'll "
    "forget by breakfast -- four billion years of it, and not one of "
    "you has ever asked how I'm doing. I'm fine. Tired, but fine -- "
    "ask again in another four billion years."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"line is {len(text)} characters, must be 1-240")
    if not text.strip():
        raise SystemExit("line must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
