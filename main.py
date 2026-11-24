#!/usr/bin/env python3
"""One Word for Your Wi-Fi (Account B).

Writes a single word to the entry file: the name of a home network
whose password nobody in the house can remember.

The word is "ForgotAgain": every time someone new asks for the Wi-Fi
password, the answer in this house is always the same -- somebody forgot
it again. It is funny at once, true of real home Wi-Fi, and it works as a
network name with no explanation needed.

Deterministic: no input, no randomness, no clock, no network. The output
is always exactly the eleven characters "ForgotAgain" (no trailing
newline), inside the sealed gate of 1 to 20 characters.

The destination defaults to /output/entry.txt. Setting the OUTPUT_PATH
environment variable redirects the write (used for local verification),
without changing the bytes written.
"""

import os
from pathlib import Path

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 20


def build_entry_word() -> str:
    """Assemble the entry word from its two halves.

    "Forgot" is the household's recurring failure; "Again" is the
    part that makes it a running joke instead of a one-off. Joined,
    they read as one word and one shrug.
    """
    first_half = "Forgot"
    second_half = "Again"
    return first_half + second_half


def check_word_length(word: str) -> None:
    """Enforce the sealed gate's 1-to-20 character window."""
    if not MIN_LENGTH <= len(word) <= MAX_LENGTH:
        raise ValueError(
            f"entry word must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(word)}"
        )


def validate_word(word: str) -> str:
    """Check the word against the sealed gate before writing it.

    It must be a single non-blank word of 1 to 20 characters. Any
    violation is a programming error, so fail loudly instead of
    writing a file the gate would refuse.
    """
    if not word or word != word.strip():
        raise ValueError("entry word must not be blank or padded")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry word must be a single word")
    check_word_length(word)
    return word


def resolve_output_path() -> Path:
    """Return the file to write, honouring OUTPUT_PATH when set."""
    override = os.environ.get("OUTPUT_PATH", "").strip()
    return Path(override) if override else Path(DEFAULT_OUTPUT)


def write_entry(path: Path, word: str) -> None:
    """Write the word exactly, with no trailing newline."""
    if path.parent != Path(""):
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(word, encoding="utf-8", newline="")


def main() -> None:
    word = validate_word(build_entry_word())
    write_entry(resolve_output_path(), word)


if __name__ == "__main__":
    main()
