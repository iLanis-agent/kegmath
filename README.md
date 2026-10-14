# Keg math

The keg names the pints, the tank names the kegs, and the fridge names the day.

A keg is bought on a vibe and regretted on a schedule. Keg math does the counting: gallons and pour size become honest servings, tank pounds become the kegs the gas will push, and the temperature gap becomes the day the chilling has to start.

## The three tools

- **Pour plan** - keg gallons and pour ounces become servings: `round0(gal * 128 / pourOz)`, banded from a small gathering to a serious crowd.
- **Gas plan** - CO2 tank pounds become half-barrels pushed at a labeled 1.5 per pound: `round1(lb * 1.5)`, banded from a season of weekends to a cellar's worth.
- **Chill plan** - the temperature gap at a labeled 45 fridge-minutes per degree F becomes the hours: `round1((startF - targetF) * 0.75)`, banded from chill this morning to a two-day promise. A target at or above the start is refused.

## Honesty notes

Illustrative planning arithmetic only. Every figure is a labeled default - your regulator, your fridge and your crowd will amend them. Foam usually means warm lines or too much pressure, not a bad keg. Know your local rules on keg deposits and serving before the party.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
