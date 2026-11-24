# Tasks

## 1. Crystal menu: flat list with rules

- [x] 1.1 In `assets/crystal.css`, remove `background`, `border`, `border-radius` and `backdrop-filter` from `.site-nav a` (line 17). Separate items with a 1px `var(--edge)` rule. On hover and focus, change only the rule colour to `var(--ice)`; remove the `box-shadow` glow on line 21. (The corner menu was removed from boosts and checklist, so this no longer applies there.) Check at 390×844 and 1440×900.

## 2. Heading: glow only on the crystal

- [x] 2.1 In `index.html` line 36, remove `text-shadow` from `h1 b`. Keep the weight and colour. The crystal's glow in `assets/crystal.css` stays.

## 3. Hint: 12px, one line

- [x] 3.1 In `index.html` line 38, set `.hint` to `font-size:12px; font-weight:400`, and keep `white-space:nowrap`.
- [x] 3.2 At 360px wide the hint is currently forced to the heading's width (about 139px), so 12px text on one line would clip. Widen `.tagline` (line 33), for example to `width:min(78vw, 300px)`, so the hint fits. Check that the heading does not wrap or overflow at 360px.

## 4. Check

- [x] 4.1 Check the home page at 360×740, 390×844 and 1440×900, closed and with the menu open.
- [x] 4.2 （検証で追加）メニューの接続線（`.site-nav::before`）の box-shadow を外す（`assets/crystal.css`）
- [x] 4.3 （検証で追加）ブースト・チェックリスト用のコーナーメニューの未使用 CSS を削除する（`assets/crystal.css`）
- [x] 4.4 （検証で追加）メニュー項目の hover で文字色も明るくする。タスク 1.1 の「罫線の色だけ変える」を、この方針に合わせて読み替える
- [ ] 4.5 (User runs) `/ui-review --verify ui-refine-home` for Before/After. The implementer does not check this task.

## Verify result (2026-11-24, home)

- All five checks passed in the code and in the browser at 360, 390 and 1440px.
- Fixed after verify: the menu label colour now fades on hover (`.site-nav a b` transition, assets/crystal.css).
- Note: the rune ring is wider than the viewport on phones; body overflow is hidden, so nothing scrolls. Left as is.
- Fixed after the second verify: the connector line above the menu is a solid 1px line (no gradient).
