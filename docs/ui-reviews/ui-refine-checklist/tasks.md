# Tasks

## 1. Phones: first item on the first screen

- [x] 1.1 Below 560px, put the "Filter by tag" chips behind one button, closed by default, showing the number of active filters. In `checklist/index.html`, change the filter section (around lines 175-179) and its CSS.
- [x] 1.2 Collapse My goals when there are no goals (`isCollapsed("goals", false)` around line 441). Open it when goals exist. Check that the first item starts within the first 844px at 390px wide.

## 2. Desktop: the filter stays in view

- [x] 2.1 In `assets/ice.css`, at `min-width:1100px`, make `.side` sticky: `position:sticky; top:24px; max-height:calc(100vh - 48px); overflow:auto`. This is shared with boosts, so check boosts at 1440px too.

## 3. Tags: colour only the paywall tags

- [x] 3.1 Keep the colour on Legend, SDKA, AC, IoDA and Legion. Make the other tag kinds neutral, keeping their text labels (tag colour tokens around lines 17-23, tag styles around lines 61-71).

## 4. Items: one column on desktop

- [x] 4.1 At `min-width:1100px`, change the item grid (line 98, `repeat(auto-fill,minmax(290px,1fr))`) to one column. Put the name in a fixed-width left column and let the tags flow to the right, wrapping only when needed.

## 5. Progress bars: solid fill

- [x] 5.1 Replace the gradient on `.bar i` (line 29) and `.amt .mbar i` (line 152) with a single colour, `var(--ice)`.

## 6. Corners

- [x] 6.1 Buttons, inputs, textarea and amount controls: 6px. Item tags and filter chips: 4px. Remove the 999px pills (lines 28, 81).

## 7. Check

- [x] 7.1 Check the checklist at 360×740, 390×844 and 1440×900, closed and with items ticked and a filter on. Check boosts at 1440px for the sticky sidebar.
- [ ] 7.2 (User runs) `/ui-review --verify ui-refine-checklist` for Before/After. The implementer does not check this task.

## Implementation notes

- 3.1: the paywall tags share one warm hue (`--c-ac`), as chosen in the review; their labels still tell them apart.
- 1.2: My goals is collapsed by default only when there are no goals; once the visitor toggles it, their choice is kept.

## Verify result (2026-11-24)

- Passed: phone filter button (closed by default, count shown), goals collapsed when empty, sticky sidebar, one-column items with tags on the right, paywall-only tag colour, solid bars, 6px/4px corners on the checked elements, no overflow at 360/390/1440, boosts and home unaffected.
- Fixed after verify: checkbox corners 7px to 6px; unused tokens --c-legend and --c-ioda and their rules removed.
- Decided: goal progress bar keeps 4px corners (a bar, not a control); sticky sidebar left as is.
- Not checked at runtime: goal form and goal amount row (no goals in the data, not added).

## Verify result (latest, checklist)

- All seven checks passed at 360, 390, 1099 and 1440px: collapsed filter, goals collapsed, sticky sidebar with Your progress, narrow order, colours, solid bars, corners, no overflow.
- Paywall gold colour: seven kinds (Legion, Legend, AC, IoDA, SDKA, Heromart, Kickstarter). Heromart and Kickstarter are paywall-linked, so the change text is updated to match the code.
- Not checked: the goal form and amounts (no goals in the data).

## Verify result (OR filters)

- All seven checks passed at 360, 390, 1099 and 1440px: collapsed filter, goals collapsed, sticky sidebar, narrow order, colours and order, solid bars, corners, no overflow.
- Filter logic: F2P alone shows 22 of 38; F2P plus Legion shows 30 of 38; an excluded tag hides its items.
- Not checked: the goal form and amounts (no goals in the data).
