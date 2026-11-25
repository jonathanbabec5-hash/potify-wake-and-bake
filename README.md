# Wake & Bake POTIFY Price Update

[Complete repository directory tree](docs/DIRECTORY.md)

**Editorial production kit.** Make a short, time-stamped daily report readers can check for themselves.

### Setup and usage

Python 3.10 or newer. The project uses the standard library.

```sh
python3 src/render.py examples/issue.json
```

Review one episode worksheet. Use the worksheet for a 2–4 minute captioned episode. Supply the pair, chart interval, time zone, observation date and reliable source. The renderer produces a local draft.

### Developer entry points

An episode worksheet separates market observation, chart time, source and founder commentary. Seven slots correspond to the existing chart-led format. Explore `examples/`, `src/`, `tests/` in the full tree.

### Verification

The commands below ran in a clean test context using local files and fixtures.

```sh
python3 -m unittest discover -s tests
```

### Release scope

No live quotes, trading signal, unapproved post copy or sponsor agreement is supplied. Established Wake & Bake series and dated November 14 production brief. This is a new reusable, data-empty production worksheet. The seven view assignments are editorial choices for this version.

[Technical whitepaper](docs/WHITEPAPER.md) · [Marketing and sales plan](docs/MARKETING.md) · [Dated developer log](docs/BUILD-LOG.md)

Existing asset and code terms remain applicable. Public access to a recording, illustration, brand or manuscript does not itself grant commercial reuse rights.
