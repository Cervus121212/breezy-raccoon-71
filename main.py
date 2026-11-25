#!/usr/bin/env python3
"""One Line, One Laugh — writes the entry line to entry.txt.

The program writes a single funny line of text to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``)
and exits 0. No network, no randomness, no clock: the output is
identical on every run.
"""

import os
import sys

LINE = "My autocorrect changed 'meeting at 3' to 'eating a tree.' My boss now thinks I'm a koala."
MAX_CHARS = 140


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    line = LINE.strip()
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: line is {len(line)} chars, over the {MAX_CHARS}-char gate",
            file=sys.stderr,
        )
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            print("error: written entry does not match the line", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
