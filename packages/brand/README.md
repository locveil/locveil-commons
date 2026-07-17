# Locveil brand assets

Mark **2b** (nested chevrons, outermost is the roof) + wordmark **B** (parted-veil `o`).
Drawn in the chrome's own language per stylebook §5: 24px grid, stroke-2 equivalent,
round caps and joins, no fills except the emitter dot. Owner-picked 2026-07-17,
integrated as **IMPL-7**; normative rules: `docs/design/ui/stylebook.md` §10.

**This directory is the canonical home.** The ui-kit `<Logo>` component is the
token-wired rendition of these files for React surfaces; the landing page (`site/`),
presentation templates, favicons and READMEs consume the SVGs directly. If a path or
color changes here, the component must be re-synced in the same change.

## Files

| File | Use |
|---|---|
| `locveil-mark.svg` | Primary mark. **≥24px only.** |
| `locveil-mark-16.svg` | Simplified mark (one inner chevron). Favicon and any 16px slot. |
| `locveil-wordmark.svg` | Wordmark alone. **≥18px ascender only.** |
| `locveil-lockup-horizontal.svg` | Top bar, README headers. Default lockup. |
| `locveil-lockup-stacked.svg` | Splash, empty states, square crops. |

## Color hooks

Each file exposes two custom properties and carries a hardcoded fallback so it also
works standalone (with a `prefers-color-scheme` dark stop):

```css
--locveil-logo-accent      /* the signal: chevrons + dot + the o */
--locveil-logo-structure   /* the shelter: house outline + remaining letters */
```

In a React app, prefer the ui-kit `<Logo>` component — it is pre-wired and cannot be
mis-wired. When inlining an SVG directly instead, wire the hooks once at the app root
(§9: product repos consume, they do not fork values):

```css
:root {
  --locveil-logo-accent: hsl(var(--primary));
  --locveil-logo-structure: hsl(var(--muted-foreground));
}
```

Do NOT wire structure to a `--lv-status-*` token — those hold bare hue numbers, not
color triplets; `hsl(var(--lv-status-pristine))` is invalid CSS and renders the
structure strokes invisible.

**Custom properties only resolve when the SVG is inlined** (SVGR / a React component /
`dangerouslySetInnerHTML`), not via `<img src>` or `background-image`. For `<img>` and
favicon use, the built-in fallbacks apply and the dark stop is handled by the file's
own media query — no wiring needed.

## Fallback hexes = exact token renditions

The hardcoded fallbacks are the tokens of `packages/ui-kit/tokens/locveil.css`
rendered to hex — standalone and in-app rendering agree by construction. If the tokens
move, re-snap these in the same ledger task:

| Fallback | Token |
|---|---|
| `#2073B6` | light `--primary: 207 70% 42%` |
| `#51A6EC` | dark `--primary: 207 80% 62%` |
| `#607080` | light `--muted-foreground: 211 14% 44%` |
| `#8794A1` | dark `--muted-foreground: 209 12% 58%` |

## Rules

- Two colors, always. Never introduce a third.
- **No amber** (§2: the island's attention color stays inside the island). If the logo
  ever needs a listening state, animate the accent dot / arcs, do not recolor.
- Lockup spacing is derived, not absolute. With mark box `H` and stroke unit `u = H/12`:
  horizontal gap `3u`, stacked gap `4u`, wordmark ascender `0.75H`. At `H=24` this gives
  a 2px stroke, a 6px gap and an 18px ascender — on-grid, and 18px matches the §3 heading size.
- Clear space around any lockup: `2u`.
- Motion, if any: 200ms, `prefers-reduced-motion` respected (§6).
- **The Latin wordmark is universal** (owner ruling 2026-07-17): it is used on RU
  surfaces as-is; no Cyrillic lockup exists or is planned.
