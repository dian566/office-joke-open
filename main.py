#!/usr/bin/env python3
"""One-line office joke for make.fun."""

# The joke is the escalation: one reply-all to stop reply-alls, now
# forty-seven people apologizing in unison.

import os

JOKE = "I replied-all to ask everyone to stop replying-all. There are now forty-seven of us apologizing in unison."


def file_joke() -> None:
    """Write the joke to /output/entry.txt, nothing else."""
    if len(JOKE) > 200 or not JOKE.strip():
        raise ValueError("joke must be a non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":  # run it
    file_joke()
