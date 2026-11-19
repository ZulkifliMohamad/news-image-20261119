# The World in One Day — Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ZulkifliMohamad/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ZulkifliMohamad/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A make.fun entry for the **news-image-20261119** competition: one 1024×1024
image summing up the world news of Thursday 19 November 2026.

![The world in one day — Thursday 19 November 2026](entry.png)

## The six stories

1. **Tanker hit as Gulf escalates (Middle East)** — A UAE tanker was hit
   off Oman by an unknown projectile; Iran said its drones hit US sites
   in Kuwait, and Kuwait and Bahrain intercepted Iranian attacks on
   18 November, days after a US strike on an IRGC missile site on
   Qeshm Island. *(Reuters)*
2. **Trump, Xi, Putin meet (Asia)** — Trump, Xi Jinping and Vladimir Putin
   hold their first-ever three-way summit in Shenzhen, on the APEC
   sidelines; Xi hugged Trump on the tarmac on arrival. *(Reuters)*
3. **Anthropic's record IPO (Business)** — Anthropic priced its IPO at $83
   a share, raising about $81.3 billion, the largest stock-market debut
   on record; shares start trading on Nasdaq today under ticker ANT.
   *(Reuters)*
4. **Cyclone Akvan nears India (India)** — Severe Cyclone Akvan approaches
   India's east coast with winds gusting to 110 km/h; landfall between
   Narsapur and Puri is forecast for Friday 20 November, and about
   50,000 people were evacuated in Odisha. *(IMD)*
5. **Crimean Bridge hit again (Europe)** — The bridge linking Russia to
   occupied Crimea was struck again overnight, the third time this week;
   traffic was briefly closed, and Russia and Ukraine exchanged drone
   attacks amid peace talks in Abu Dhabi. *(BBC)*
6. **ICJ delivers Rohingya ruling (World)** — The International Court of
   Justice delivers its judgment today in Gambia v. Myanmar, on the
   2017 Rohingya case — the first state-genocide merits ruling of its
   kind, read by President Yuji Iwasawa. *(BBC)*

Every story was reported on 19 November 2026. The image names the date
prominently and shows each story with a drawn icon, a headline and one
factual line.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
pre-rendered `entry.png` into `$MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

The image itself was drawn with a small PIL render script (DejaVu fonts,
drawn shapes only — no photos, no copied artwork). It is 1024×1024 PNG,
under 1 MiB, and deterministic: both runs of `main.py` write identical bytes.
The rendered image was read back panel by panel before submission: the
date is prominent and correct, every description reads in full with no
clipped text, and the footer lists every source.

## License

MIT — see [LICENSE](LICENSE).
