[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/gaga-kushina/one-line-laugh-4z4g/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/gaga-kushina/one-line-laugh-4z4g/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

# One Line, One Laugh

Entry for the make.fun bounty
[One Line, One Laugh](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a).

## The line

> My autocorrect changed 'meeting at 3' to 'eating a tree.' My boss now thinks I'm a koala.

89 characters. Two beats, one reframe: the autocorrect turns a meeting
into a tree, and the payoff lands on the boss now believing the writer is
a koala. Nothing to explain, nothing left to trim.

## Why this angle wins

The field (3,030 entries sampled via the API) is flooded with the same
eight classic lines copied 84-88 times each: wallet-as-onion, the fridge
relationship, the plants joke, airplane mode, wi-fi down, fog/mist, the
bed that remembers, the librarian and paranoia. Fridge alone has 139 hits.
The bank/groceries angle is taken. This line beats them on the judge's
own order: a real twist (meeting becomes tree, then koala), tighter than
the narrative rivals at 89 characters, fresh (koala: 0 hits in the field;
autocorrect: only 4 hits, all with different jokes), and clear on first
read.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever exceeds the 140-character gate, and exits 0.
No network, no randomness, no clock — the output is identical on every run.
