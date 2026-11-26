"""Snooze Button Roast — one line roasting a 6 AM Saturday alarm clock."""

import os

LINE = (
    "My alarm went off at 6 AM on a Saturday, full volume, for a night-shift "
    "nurse whose baby had just fallen asleep — because past-me set it "
    "'just in case.' In case of what? Sleep?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
