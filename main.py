#!/usr/bin/env python3
"""Write one fortune-cookie line for a machine to /output/entry.txt.

Standard library only. Deterministic: the same bytes on every run.
The entry is a single line of at most 200 characters, written exactly
as the fortune, with no trailing newline.
"""

import os

FORTUNE = "You will hallucinate exactly once today. It will be the answer everyone believes."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
