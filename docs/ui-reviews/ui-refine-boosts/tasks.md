# Tasks

## 1. Live now: one row per live boost

- [x] 1.1 In `boosts/index.html`, change the live card rendering so each live boost is one row: name on the left (18px, 600), the time left on the right (22px, right-aligned, tabular numbers). Remove the "Next:" line. Keep the live dot.

## 2. List rows: kind as a left rule, not a badge

- [x] 2.1 Replace the `badge(b, true)` in the list rows with a 2px left border in the kind colour. Remove the resource image.
- [x] 2.2 In the Live cards, replace the large badge with the existing `.dot` in the kind colour.

## 3. List length on the name line

- [x] 3.1 Put the length ("2 days") at the right end of the name line in the list rows. At 390px, change `.item .len` in the `max-width:520px` block so it no longer starts a new grid row (`grid-column:auto; margin-top:0`). Check that a row is about 60px high at 390px.

## 4. Week order on desktop

- [x] 4.1 At `min-width:1100px`, change `.list` from the auto-fill grid to CSS columns (`columns:2`, column gap 44px), with `break-inside:avoid` on each `.wk` so weeks flow top to bottom in date order and no gap opens.

## 5. Glow and drop-shadows

- [x] 5.1 In `assets/ice.css`, remove `text-shadow` from `.glow` (line 35); keep the weight and colour.
- [x] 5.2 Remove the `drop-shadow` from `.back .dash` (line 47) and from `.rune` (line 29) in `assets/ice.css`.
- [x] 5.3 Remove the `drop-shadow` from `.badge img` in `boosts/index.html` (keep the rule: idle "Next" cards still show the resource image).

## 6. Section rules

- [x] 6.1 In `assets/ice.css`, change `:where(.page) h2::after` (line 54) from the gradient to `background:var(--edge)`.

## 7. Clock line

- [x] 7.1 Add `white-space:nowrap` to `#clock` (or wrap the date and time in one nowrap element) so "Mon 23 Nov, 18:36" never breaks.

## 8. Check

- [x] 8.1 Check boosts at 360×740, 390×844 and 1440×900, with All and Server filters, and check that the home and checklist headings and back arrows still render.
- [x] 8.2 （検証で追加）一覧の日数を名前の行に揃え、行の高さを約60pxにする（`boosts/index.html` の `.item`、`.item .len`、`.item .what b`）
- [x] 8.3 （検証で追加）`a.plate` の hover の drop-shadow を外す（`assets/ice.css`）。ホーム・ブースト・チェックリストに効く
- [x] 8.4 （検証で追加）ヘッダーの「All times are AQW server time (ET)」を削除する
- [ ] 8.5 (User runs) `/ui-review --verify ui-refine-boosts` for Before/After. The implementer does not check this task.
