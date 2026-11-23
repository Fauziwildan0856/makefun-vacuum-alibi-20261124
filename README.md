# Reclassified as Furniture

[![make.fun · The Vacuum's Alibi](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) [![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Fauziwildan0856/makefun-vacuum-alibi-20261124/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) [![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Fauziwildan0856/makefun-vacuum-alibi-20261124/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

This repository is an entry for the make.fun bounty **"The
Vacuum's Alibi: One Line, 200 Characters"**. The task: write the
funniest one-line excuse a robot vacuum can give for missing a
spot, in 200 characters or fewer. The house judge compares entries
two at a time and weighs deadpan robot voice, surprise, and how
tight the line is.

## The line

> The spot filed a do-not-disturb request, so I reclassified it as
> furniture and updated the map. Case closed.

One sentence, 108 characters. The vacuum does not apologise or
explain the miss away — it takes the spot's complaint at face
value, files it under the correct bureaucratic category, updates
the paperwork, and closes the case. Deadpan, a little smug about
its own map, and the punch lands on the last two words.

## Running it

```sh
python3 main.py
```

That writes the line to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`). It needs nothing beyond the Python 3
standard library: after writing, it reads the file back and
checks the text is byte-for-byte the intended line, a single
line of 1–200 characters, and not only whitespace. The output is
identical on every run.

## Licence

Released under the MIT licence; the full text is in `LICENSE`.
