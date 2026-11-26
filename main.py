#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence -- make.fun entry.

Writes the chosen one-line error message to /output/entry.txt.
Python 3.13 standard library only; no third-party imports.
"""

import os

# The entry: a flat error-message tone that turns into the joke --
# the words that never got generated are laid-off workers.
ENTRY = "Error: token limit reached. The remaining words have filed for unemployment."


def main() -> None:
    # Gate self-check, mirroring the sealed scorer: 1-140 chars,
    # a single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
