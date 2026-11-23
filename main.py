"""Entry for make.fun bounty "The Vacuum's Alibi: One Line, 200 Characters".

Writes the vacuum's one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt,
then reads it back and verifies it is exactly the intended text and
within the 1-200 character gate. Standard library only.
"""

import os
import sys

ENTRY = (
    "The spot filed a do-not-disturb request, so I reclassified it "
    "as furniture and updated the map. Case closed."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200:
        print("entry is %d characters, outside the 1-200 range" % len(written),
              file=sys.stderr)
        return 1
    if not written.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("entry must be a single line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
