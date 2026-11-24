# Proposal

## Why

Reviewing the checklist as a whole (after the first refinement) found six problems:

- On wide screens the sticky sidebar holds the whole sync and save block, so the save card is cut off and needs a scroll inside the sidebar.
- The subtitle still says "get started" after items are ticked.
- The paywall tags use 10px pixel type, and the two-letter codes are hard to read.
- On phones the open filter pushes the first item below the fold.
- The sync step buttons are taller boxes that overlap the lines around them.
- With a filter on and nothing matching, the empty group offers no way to clear the filter.

## What Changes

- Sidebar: "Save, move or restore" and the code import move into a collapsed section at the end of the list. The sidebar keeps the title, progress, filter and the sync card.
- Subtitle: shows the get-started line when nothing is ticked, and a count line (for example "6 of 38 owned") after that.
- Paywall tags: Outfit 600, uppercase, 11.5px, letter-spacing .04em. The gold colour and tag shape stay.
- Phone filter: each group becomes one horizontally scrolling row with a small label above it.
- Sync steps: the two step buttons are inline and keep the line height.
- Empty groups: a "Clear filters" link sits after "No items match your filters."
- Reference layouts were not confirmed with WebFetch; the candidates named in the review are unverified and were not used.
- Data and behaviour (ticking, goals, sync, import and export, filter logic) do not change.

## Impact

- Files: `checklist/index.html` (sidebar markup, subtitle in render, tag and filter CSS, step links, empty state).
- Affected other screens: none expected. Check that `.tag` and `.btn` are not used by other pages through this file.
- Tests: none in this project.
- Verify: `/ui-review --verify ui-refine-checklist-2` (Before/After and a check on a real phone).
- Before screenshots: `screenshots/before-*.png`.
