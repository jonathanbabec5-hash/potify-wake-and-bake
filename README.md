# Wake and Bake POTIFY Price Update

## Find your way in

| If you are… | Start here | Try this |
| --- | --- | --- |
| A viewer | [Read an episode worksheet](examples/issue.json) | Look for the observation time and chart source. |
| An editor | [Inspect the renderer](src/render.py) | Trace a price statement back to a dated source. |
| A contributor | [Explore the project tree](docs/DIRECTORY.md) | Suggest a missing evidence field using fictional data. |

[Complete repository directory tree](docs/DIRECTORY.md)

## A chart needs a clock

There is an honest sentence a market show should be willing to say on a quiet evening: the last trade is old. A fresh screenshot does not make it new. Wake and Bake POTIFY Price Update starts by giving each observation its own time, interval and source.

The [episode worksheet](examples/issue.json) opens with the observation time and verified mint. The [renderer](src/render.py) holds the editorial structure together; it does not fetch a fresh market price. Archived chart frames stay attached to their original dates.

Use the example to trace a single price statement back to its chart and time. If it cannot be traced, leave it unknown and suggest the missing source field. This review concerns editorial evidence; it makes no trading call or promise.

**Editorial production kit.** Make a short, time-stamped daily report readers can check for themselves.

### Setup and usage

Python 3.10 or newer. The project uses the standard library.

```sh
python3 src/render.py examples/issue.json
```

Review one episode worksheet. The worksheet supports the source-only 22:00 ET review. Draft a continuous 60–90 second script, or roughly two minutes for the supplied seven-chart format. Supply the pair, chart interval, time zone, observation date and reliable source. The renderer produces a local draft.

### Developer entry points

An episode worksheet separates market observation, chart time, source and founder commentary. Seven slots correspond to the existing chart-led format. Explore `examples/`, `src/`, `tests/` in the full tree.

### Verification

The commands below ran in a clean test context using local files and fixtures.

```sh
python3 -m unittest discover -s tests
```

### Release scope

No live quotes, trading signal, unapproved post copy or sponsor agreement is supplied. Original seven vertical chart frames and contact sheet from Wake_and_Bake_POTIFY_7_VERTICAL_CHARTS.zip. October 9 chart imagery, with an October 18 script in the original archive. The reusable worksheet now follows the seven archived headings. The screenshots are historical.

[Technical whitepaper](docs/WHITEPAPER.md) · [Marketing and sales plan](docs/MARKETING.md) · [Dated developer log](docs/BUILD-LOG.md)

Existing asset and code terms remain applicable. Public access to a recording, illustration, brand or manuscript does not itself grant commercial reuse rights.
