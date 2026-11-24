# Proposal

## Why

The checklist is the page people use to track gear, but the layout works against scanning it:

- On a phone, the filter chips and the goals form take about 1000px, so the first item starts below the first screen.
- On desktop the filter sidebar scrolls out of view while the list continues.
- Each item shows 3 to 8 coloured tags in about ten hues, which dilutes what the colours mean.
- On desktop, items run in three columns, so names wrap and rows vary in height.
- The progress bars use a gradient, and the corner radii are mixed (6, 7, 8, 10px and pills).

## What Changes

- Phones (560px and below): filter chips behind a "Filter by tag" button, closed by default; My goals collapsed when there are no goals.
- Desktop (1100px and up): the sidebar stays in view while the list scrolls.
- Tags: only the paywall tags (Legend, SDKA, AC, IoDA, Legion) keep a colour; the others are neutral with their text labels.
- Desktop items: one column, the name on the left in a fixed-width column, tags flowing to the right.
- Progress bars: a single solid colour.
- Corners: buttons, inputs and amount controls 6px; tags and filter chips 4px; no pills.
- Reference layouts were checked from page text only: Paimon.moe Achievement (a "not achieved first" toggle) and the OSRS Wiki Collection log (one list per section with totals). Their visual layout was not confirmed.
- Data and behaviour (ticking, goals, sync, import and export, filters) do not change.

## Impact

- Files: `checklist/index.html` (filter and goals layout, tag colours, item grid, bar fill, radii); `assets/ice.css` (`.side` sticky, shared with boosts).
- Affected other screens: boosts, through the shared sticky sidebar. Check boosts at 1440px.
- Tests: none in this project.
- Verify: `/ui-review --verify ui-refine-checklist` (Before/After and a check on a real phone).
- Before screenshots: `screenshots/before-*.png` (4 items ticked and the F2P filter on for the ticked states).
