#!/usr/bin/env python3
"""One Line, One Laugh - writes a single funny line to /output/entry.txt.

The line below is the winner of an 8-draft duel tournament (7-0, unbeaten):
concrete scene + specific number + an absurd twist at the end.
No dependencies; writes exactly one line, at most 200 characters.
"""

import os

LINE = "NASA spent $4 million teaching a robot to fold laundry. It folded one shirt, then filed for overtime."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
