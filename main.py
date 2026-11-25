"""One Star, Five Stars for the Food — entrypoint.

Writes the winning one-sentence alien tourist review to /output/entry.txt.
Winner of an internal 10-variant pairwise tournament (see TOURNAMENT.md).
"""

import os

ENTRY = "One star \u2014 I flew 40 light-years for a planet that still queues for coffee, yet the ramen alone was worth the warp fuel."

# Gate: 1-200 chars, UTF-8, single sentence, no trailing newline.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
assert ENTRY.count(".") <= 1, "must stay one sentence"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
