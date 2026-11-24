# Tasks

## 1. Filters match the checklist chips

- [x] 1.1 In `boosts/index.html`, change `.filters button` to 4px corners, 12.5px text, padding 6px 10px, background rgba(13,21,32,.45) and the edge border (as `.ftag` on the checklist). Keep the selected style. Check at 390 and 1440.

## 2. Rows: kind only, and only under All

- [x] 2.1 In the row rendering, remove the date from the second line. Show "Server boost" or "Resource boost" there only when the All filter is selected. Check that the date stays only in the left block.

## 3. Empty state names the filter and offers All

- [x] 3.1 In the empty-state text (around line 228), say which kind is empty ("No server boosts scheduled.", "No resource boosts scheduled.") and add a "Show all" button in the same place that sets the filter to All. Check with Server selected when no server boost is upcoming, if the data allows, or by reading the code path.

## 4. Copy: time zone and home link

- [x] 4.1 Change the sub-line to "Server time (ET) …" and "Schedule updated … ET" (around lines 244-245).
- [x] 4.2 Change "Go back" to "Home" (around line 102).

## 5. Weekday labels readable

- [x] 5.1 Set `.date .dow` to 12px, a brighter tone than the muted grey, and letter spacing .06em.

## 6. Week headings use dates

- [x] 6.1 In `weekLabel`, use "Week of 23 Nov" style for every week, and "This week" only for the current week (around lines 198-205).

## 7. Check

- [ ] 7.1 Check boosts at 360×740, 390×844 and 1440×900 with All and Server, and check that there is no horizontal overflow.
- [ ] 7.2 (User runs) `/ui-review --verify ui-refine-boosts-2` for Before/After. The implementer does not check this task.

## Implementation notes

- Checked at 390: filters 4px; the Server filter leaves the row's second line empty; week headings are dates with This week for the current week; the header shows ET; the back link says Home; no overflow.
- 3.1 (empty state) is implemented from the code path; the live data always has upcoming boosts, so the empty text was not seen on screen.
- 7.1 for 360 and 1440 and 7.2 (your verify) remain.

## Verify result

- 6 of 7 checks passed as specified at 360, 390 and 1440px: filter chips, row lines, copy, weekday labels, week headings, no overflow.
- Fixed after verify: the Show all button had no styles (browser-default grey). It now matches the filter chips, with hover and focus.
- Not checked on screen: the empty state with live data (the data always has upcoming boosts); the Server filter at 360px; the Resource filter with real data.
