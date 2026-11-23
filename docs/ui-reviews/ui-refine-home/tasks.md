# Tasks

## 1. Crystal menu: flat list with rules

- [x] 1.1 In `assets/crystal.css`, remove `background`, `border`, `border-radius` and `backdrop-filter` from `.site-nav a` (line 17). Separate items with a 1px `var(--edge)` rule. On hover and focus, change only the rule colour to `var(--ice)`; remove the `box-shadow` glow on line 21. This also changes the corner menu on boosts and checklist: open the menu there too. Check at 390×844 and 1440×900.

## 2. Heading: glow only on the crystal

- [x] 2.1 In `index.html` line 36, remove `text-shadow` from `h1 b`. Keep the weight and colour. The crystal's glow in `assets/crystal.css` stays.

## 3. Hint: 12px, one line

- [x] 3.1 In `index.html` line 38, set `.hint` to `font-size:12px; font-weight:400`, and keep `white-space:nowrap`.
- [x] 3.2 At 360px wide the hint is currently forced to the heading's width (about 139px), so 12px text on one line would clip. Widen `.tagline` (line 33), for example to `width:min(78vw, 300px)`, so the hint fits. Check that the heading does not wrap or overflow at 360px.

## 4. Check

- [x] 4.1 Check the home page at 360×740, 390×844 and 1440×900, closed and with the menu open.
- [ ] 4.2 (User runs) `/ui-review --verify ui-refine-home` for Before/After. The implementer does not check this task.
