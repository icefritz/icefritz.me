# Proposal

## Why

Reviewing the home screen as a whole (after the first refinement) found six problems:

- With the menu open, the rune ring and star lines run through the menu labels, which are the only navigation.
- The name plates ICEFRITZ and CRUEL look like titles; nothing shows they are links that open a new tab.
- The menu's titles (Boosts, Checklist) do not match the pages' headings (Server boosts, Item checklist).
- The only top-level heading is the slogan; the name is a link.
- The crystal, the only control, is the smallest item on desktop, and its hint sits below the heading.
- A second radial gradient at the bottom of the body reads as a dark smudge on phones.

## What Changes

- Rune: fades to about 12% opacity while the menu is open, using the same open-state rule as the tagline.
- Name plates: a thin underline, and a visually hidden "(opens in new tab)" for screen readers.
- Menu titles: "Server boosts" and "Item checklist", matching the page headings.
- Heading: the name is the page heading, and the slogan is a paragraph with the same size and weight. No visual change.
- Crystal: larger on home only, about 64px on wide screens, with the touch target growing with it.
- Background: the bottom radial gradient is removed; the centre light behind the crystal stays.
- Reference rules: GOV.UK guidance on "opens in new tab" was used for the link text. Other candidates were not confirmed.
- Data and behaviour (links, the menu open and close, the crystal's animation) do not change.

## Impact

- Files: `index.html` (rune open state, name plates, heading, crystal size), `assets/crystal.js` (menu titles), `assets/ice.css` (plate underline, body background).
- Affected other screens: the menu titles change on boosts and checklist too; the background change applies to boosts and checklist.
- Tests: none in this project.
- Verify: `/ui-review --verify ui-refine-home-2` (Before/After and a check on a real phone).
- Before screenshots: `screenshots/before-*.png`.
