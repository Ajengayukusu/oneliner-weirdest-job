# Weirdest Job Title — one title for make.fun's
# "Weirdest Job Title: Blind Judge Showdown" bounty.
#
# Judge brief: a weird job title of 60 characters or fewer, a few words
# and nothing else; stranger than ordinary work, with a twist that lands
# on the first read; it must sound like a real job rather than random
# word salad, specific enough to picture the person doing it.
#
# The title: a professional mourner is a real, centuries-old job — hired
# to grieve at funerals. The twist is the clientele: not people, but
# other people's houseplants, mourned with full ceremony by someone in a
# black suit holding a tiny watering can they no longer need.
#
# SPDX-License-Identifier: MIT
import os
import sys
from pathlib import Path

LINE = "Professional Mourner for Other People's Houseplants"

MAX_CHARS = 60


def entry_line() -> str:
    line = LINE.strip()
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if any(ord(c) < 32 or ord(c) == 127 for c in line):
        raise ValueError("entry must not contain control characters")
    # A title, not a sentence: no ending punctuation, and it must read
    # as a job someone could be hired for — at least three words.
    if line[-1] in ".!?":
        raise ValueError("a job title carries no ending punctuation")
    if len(line.split()) < 3:
        raise ValueError("a job title needs at least three words")
    return line


def output_path() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def run() -> int:
    line = entry_line()
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
