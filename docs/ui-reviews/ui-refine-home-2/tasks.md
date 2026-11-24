# Tasks

## 1. Rune dims while the menu is open

- [x] 1.1 In `index.html` styles, give `.rune` an opacity transition (`.3s ease`) and add `.menu-open main .rune{opacity:.12}`. Keep the reduced-motion rule. Check at 390 and 1440 that the menu labels are readable with the menu open.

## 2. Name plates look like links

- [x] 2.1 In `assets/ice.css`, give `a.plate` a thin underline in `var(--edge)` with `text-underline-offset:4px`.
- [x] 2.2 In `index.html`, add a visually hidden "(opens in new tab)" inside both name links (ICEFRITZ and CRUEL). Check that the visible text is unchanged.

## 3. Menu titles match the headings

- [x] 3.1 In `assets/crystal.js` (PAGES), set the titles to "Server boosts" (boosts) and "Item checklist" (checklist). Check the menu at 360px wide on home, boosts and checklist.

## 4. The name is the page heading

- [x] 4.1 In `index.html`, wrap the name link in the `<h1>` and change the slogan to a `<p>`. Move the heading styles so the look is unchanged: name and slogan keep their sizes, weights and colours. Check at 360, 390 and 1440.

## 5. Larger crystal on home

- [x] 5.1 In `index.html` styles, enlarge the crystal on home only, to about 64px at min-width 700px (`main .crystal`). Check that the touch target grows and nothing overlaps at 1440×900 and 390×844.

## 6. Background without the bottom gradient

- [x] 6.1 In `assets/ice.css`, remove the bottom `radial-gradient(120% 90% at 50% 120%, ...)` layer from `body` and keep the centre light. Check boosts and checklist still look right.

## 7. Check

- [ ] 7.1 Check home, boosts and checklist at 360×740, 390×844 and 1440×900, closed and with the menu open.
- [ ] 7.2 (User runs) `/ui-review --verify ui-refine-home-2` for Before/After. The implementer does not check this task.

## Implementation notes

- Checked at 1440 and 360 on home: name is the page heading with the slogan as a paragraph; name underlined; crystal 64px on wide screens; rune dims to 12% with the menu open; menu titles match the headings; no overflow.
- The menu is only on home now, so the title check for 3.1 was done on home. Boosts and checklist have no crystal menu.
- 7.1 is partly done: the background change on boosts and checklist was not screenshot-checked yet.
- Changed on request: the underline on the name links (task 2.1) is removed; the hidden new-tab text stays.
- Changed on request: the menu titles are back to "Boosts" and "Checklist" (the longer titles wrapped onto two lines); task 3.1 is superseded.
