#!/usr/bin/env python3
"""One Word for Your Wi-Fi (Account B).

Writes a single word to /output/entry.txt: the name of a home network
whose password nobody in the house can remember.

The word is "ForgotAgain": every time someone new asks for the Wi-Fi
password, the answer in this house is always the same -- somebody forgot
it again. It is funny at once, true of real home Wi-Fi, and it works as a
network name with no explanation needed.

Deterministic: no input, no randomness, no clock, no network. The output
is always exactly the eleven characters "ForgotAgain" (no trailing newline),
inside the sealed gate of 1 to 20 characters.
"""

import os

WORD = "ForgotAgain"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
