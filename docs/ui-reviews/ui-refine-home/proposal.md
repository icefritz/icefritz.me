# Proposal

## Why

The home screen has three AI-looking patterns and one legibility problem:

- The crystal menu items are rounded glass boxes with blur. The boosts and checklist pages were moved to flat rules in f129bf6, so home now uses a different navigation language.
- The word "ice" in the heading and the rune ring both glow, which competes with the crystal, the one element that should be lit.
- The only instruction on the page, "(no, really. click the crystal)", is about 10px on phones. Visitors arriving from Discord may not read it.

## What Changes

- Crystal menu: flat list separated by thin rules, no box, blur or radius. Reference: Teenage Engineering (https://teenage.engineering/), whose top navigation is plain text with no boxes. The open menu of that site was not checked.
- Heading: remove the glow from "ice"; the crystal stays the only glowing element.
- Hint: 12px, weight 400, kept on one line.
- Navigation stays behind the crystal (decided: keep).
- Data and behaviour (menu links, the crystal's animation, copy) do not change.

## Impact

- Files: `assets/crystal.css` (`.site-nav a`), `index.html` (`h1 b`, `.hint`, `.tagline`).
- Affected other screens: boosts and checklist. Both use the same corner menu (`.crystal-nav.corner`), so the menu change also applies there. Check both.
- Tests: none in this project.
- Verify: `/ui-review --verify ui-refine-home` (Before/After screenshots and checking on a real phone).
- Before screenshots: `screenshots/before-*.png`.
