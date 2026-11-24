# Proposal

## Why

Reviewing the boosts page as a whole (after the first refinement) found six problems:

- The filter buttons are full pills, which the design rules and the checklist filters do not use.
- Each row repeats the date, and the kind is repeated under a server filter.
- The empty state does not match the filter and gives no next step.
- The sub-line mixes time formats, and "Go back" leads to the home page.
- The weekday labels are 11px, muted grey and hard to read.
- The week headings mix "This week", "Next week" and "Week of 7 Dec".

## What Changes

- Filters: 4px corners, 12.5px text, and the same padding and background as the checklist filter chips.
- Rows: the second line shows the kind only, and only when All is selected; the date stays in the left block.
- Empty state: names the filter ("No server boosts scheduled.") with a "Show all" button in the same place.
- Copy: "Server time (ET)" and "Schedule updated … ET"; "Go back" becomes "Home".
- Weekday labels: 12px, a brighter tone, slightly tighter letter spacing.
- Week headings: "Week of 23 Nov" style for every week; "This week" only for the current week.
- Data and behaviour (which boosts appear, the countdowns, the filters, the refresh) do not change.

## Impact

- Files: `boosts/index.html` (filter and row styles, row rendering, empty state, sub-line, back link, weekday and week heading styles).
- Affected other screens: none expected; the filter style matches the checklist, which already uses it.
- Tests: none in this project.
- Verify: `/ui-review --verify ui-refine-boosts-2` (Before/After and a check on a real phone).
- Before screenshots: `screenshots/before-*.png`.
