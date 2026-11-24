# Tasks

## 1. Sidebar: the save card moves to a collapsed section

- [x] 1.1 On wide screens, move "Save, move or restore" and the code import into a collapsed `<details>` at the end of the list, after the Completed sections. Keep the title, progress, filter and the sync card in the sidebar. Check at 1440×900 that nothing in the sidebar is cut off.

## 2. Subtitle follows progress

- [x] 2.1 In `render()`, set the subtitle from state: with nothing ticked, "Sync your inventory or tick manually to get started."; otherwise "N of 38 owned." (or the count of all items). Check at 390 and 1440 with 0 and 6 ticked.

## 3. Paywall tags in sans caps

- [x] 3.1 Set `.tag.legend`, `.tag.ac`, `.tag.ioda`, `.tag.sdka`, `.tag.legion`, `.tag.heromart`, `.tag.kickstarter` and their `.ftag` versions to Outfit 600, uppercase, 11.5px, letter-spacing .04em (checklist/index.html around lines 63, 68, 86). Keep the gold colour. Check that the tag row still fits on a 360px phone.

## 4. Phone filter: one-line scrolling rows

- [x] 4.1 At 560px and below, make each `.frow` one horizontally scrolling line (`flex-wrap: nowrap`, `overflow-x: auto`) with the group label above it. Check at 390 with the filter open that the first item starts within the first 844px.

## 5. Sync step links stay in the line

- [x] 5.1 Give the two step links (AQW sync and account.aq.com, around line 216-217) an inline class: `display:inline-block; padding:1px 7px; line-height:1.4; font-size:13px`. Keep the dashed border on the bookmarklet. Do not change `.btn` itself, since the save card uses it.

## 6. Empty groups offer Clear filters

- [x] 6.1 In `render()`, after "No items match your filters.", add a "Clear filters" link (the `.fclear` style) that clears the filters. Check with the Legion filter on that the link appears and works.

## 7. Check

- [ ] 7.1 Check the checklist at 360×740, 390×844 and 1440×900, closed and with items ticked and a filter on.
- [ ] 7.2 (User runs) `/ui-review --verify ui-refine-checklist-2` for Before/After. The implementer does not check this task.

## Implementation notes

- 1.1: the save card is a collapsed section below the list, inside the main column; the sync card stays in the sidebar.
- Checked at 1440 (sidebar fits, no scroll) and 390 (first item at 631px with the filter open; rows scroll on one line; Clear filters restores all 38).
- 7.1 is done; 7.2 stays with you.
