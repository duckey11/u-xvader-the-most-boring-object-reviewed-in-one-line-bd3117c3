#!/usr/bin/env python3
"""Write one funny, true one-line review of the most boring everyday
object: the doorstop.

The joke is the object's own dullness: it has exactly one job, performs
it lying on the floor all day, and its only reward is being kicked by
the very people it serves. Every detail is true and instantly
recognisable: doorstops sit on the floor, nobody notices them, and
everyone kicks them.
"""

import os

REVIEW = (
    "The doorstop: one job, all day, on the floor, "
    "and its only thanks is a kick."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
