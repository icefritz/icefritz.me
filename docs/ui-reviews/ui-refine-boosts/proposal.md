# Proposal

## Why

The boosts page is the calendar people come for, and it reads like a generic dashboard:

- The live cards take about 320px on a phone, so the first upcoming row starts near the bottom of the screen. Each card repeats the name and the date, and the time left is smaller than its label.
- Each row has a coloured rounded badge that repeats the name in short form. At this size "CP" reads as "OP".
- On a phone each row is about 85px because the length of the boost ("2 days") sits on its own line.
- On desktop the week blocks fill two columns, so the order zigzags and a gap opens under "This week".
- The heading uses the shared `.glow` class, so it has a text glow. This breaks the rule that glow is for the crystal only. The back arrow, rune and item images also carry drop-shadows.
- Section rules fade out with a gradient. The clock line breaks between the day and the month on a phone.

## What Changes

- Live now: one row per live boost, name on the left and the time left on the right as the largest figure. The "Next" line is removed because the list shows it.
- List rows: the kind is shown by a 2px coloured rule on the left edge, not a badge. Resource images are removed.
- List length: days move to the right end of the name line, so each row is about 60px on a phone.
- Week order: weeks flow top to bottom in date order on desktop, with no gaps.
- Glow: the text glow on the heading and the drop-shadows on the back arrow, rune and item images are removed.
- Section rules: solid 1px in the edge colour, not a fading gradient.
- Clock: date and time stay on one line.
- Data and behaviour (what boosts appear, the countdowns, filters, the 15-second refresh) do not change.

## Impact

- Files: `boosts/index.html` (styles and the row, card and week rendering), `assets/ice.css` (`.glow`, `.rune`, `.back .dash`, the `h2::after` rule).
- Affected other screens: `.glow`, `.rune`, the `h2` rule and `.back` are shared. The checklist title and headings, the home rune and the checklist back arrow change too. Check boosts, checklist and home.
- Tests: none in this project.
- Verify: `/ui-review --verify ui-refine-boosts` (Before/After screenshots and a check on a real phone).
- Before screenshots: `screenshots/before-*.png` and `screenshots/before-full-*.png`.
