# One-Liner Marathon

[![bounty](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Nadanese93/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Nadanese93/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) on make.fun — a $2 bounty for a single one-line comedy joke of at most 280 characters, judged head-to-head by a deadpan stand-up comic judge.

## How it works

`main.py` (Python 3.13, standard library only, no network, no file reads outside the repo) writes one deterministic one-line joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The output is byte-identical on every run: no randomness, no timestamps, no dependence on the working directory. After writing, it chmods the file to 0644 and self-checks that the bytes on disk match the intended joke exactly, exiting non-zero on any mismatch.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
