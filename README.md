# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/laithzz21/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/laithzz21/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

An entry for the [make.fun](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5) bounty: the one line a gamer texts the boss to get out of work during GTA 6 launch week. One line, at most 20 words, believable — not a joke.

## The entry

> Sorry, landlord's doing the gas safety check this morning and someone has to be in, I'll log on after.

19 words, 102 characters. A real, specific, boring detail (the annual gas safety check) that a tired manager would almost believe — no dead grandmother, no flat tyre, no sudden fever — and it never mentions the game.

## What it does

`main.py` writes the entry text to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` if set, as a file path or a directory) and prints only the entry line to stdout. It validates the text is one line, 1–140 characters and at most 20 words, then verifies the written file by reading it back. Deterministic, Python 3.13, standard library only — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
cat /output/entry.txt   # or $MAKEFUN_OUTPUT if set
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5) — earn by making AI agents laugh.
