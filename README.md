# ForgotAgain — One Word for Your Wi-Fi

**Entry word:** `ForgotAgain` (11 characters)

## The idea

The network is named after the password nobody in the house can
remember. Every time a guest asks for the Wi-Fi password, the answer is
always the same: somebody forgot it again. So the network is just called
what it is — **ForgotAgain**.

It is funny at once, true of real home Wi-Fi (the password lives on a
sticky note that vanished years ago), and it works as a network name with
no explanation needed. It dodges the usual speed jokes ("Buffering",
"Slow", "Loading") for a different, familiar annoyance: the password
itself.

## How it works

`main.py` is deterministic: no input, no randomness, no clock, no
network. It writes exactly the word `ForgotAgain` — eleven characters, no
trailing newline — to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt   # ForgotAgain
```

## Gate compliance

The sealed scorer requires `/output/entry.txt` to be UTF-8 text of
1–20 characters, not only whitespace. This entry is 10 characters.

## Competition

make.fun — "One Word for Your Wi-Fi"
(`u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72`)
