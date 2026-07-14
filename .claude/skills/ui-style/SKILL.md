---
name: ui-style
description: Load the Locveil design system before ANY UI work in any Locveil repo — building or restyling components, pages, Workbench plugins, Storybook stories, or reviewing UI diffs. Applies the decided tokens (blued-steel palette, steel-blue accent, split icon ruling, 0.75rem chrome radius, compact density) instead of improvising values.
---

# ui-style — the Locveil design system, executable half

Normative sources (read in this order when detail is needed; this digest is enough for
most component work):
1. **Tokens:** `../locveil-commons/packages/ui-kit/tokens/locveil.css` (values win)
2. **Rules:** `../locveil-commons/docs/design/ui/stylebook.md`
3. Evidence/why: `docs/design/ui/token-inventory-draft.md` + `divergence-list.md`

Decided by the PROD-10 style council 2026-07-14. Changes go through a council round +
ledger task — never a one-off value in a component.

## The digest

- **Identity: воронёная сталь.** Neutrals hue 207–213, restrained chroma. Light bg
  `hsl(210 25% 97.5%)` / white cards; dark bg `hsl(213 26% 8.5%)` / cards
  `hsl(212 22% 12.5%)`. Dual theme always (`.dark` class); test both.
- **Accent (the only interactive color):** steel-blue — light `hsl(207 70% 42%)` on
  white text; dark "polished" `hsl(207 80% 62%)` on near-black text. Buttons, active
  tab/nav, links, focus ring. Never introduce a second interactive color.
- **Status ≠ interaction:** pill-shaped bordered chips with per-theme recipes
  (see tokens `--lv-status-*`): pristine 211 · edited 28 · tested 210 (blue — owner
  ruling; the pill shape keeps it from reading as a button) · persisted 145 ·
  conflict 0. Device on/off green/red dots. NEVER `*-50` washes on dark.
- **Radius:** chrome `--radius: 0.75rem` (controls 10px, inner 8px). The remote island
  keeps its own 24/16/12/8px ladder — never mix systems in one component.
- **Type:** system sans stack (no webfonts — offline-first WB7). 11px/600/uppercase
  labels · 12.5 secondary · 14 body · 18/700 headings. `tabular-nums` readings, `mono`
  code. Always check layouts with RU strings (~20% longer).
- **Density:** compact (`px-3 py-2 text-sm` inputs). One density everywhere.
- **Icons — split ruling:** lucide (stroke-2) in workbench/chrome; Material filled
  ONLY inside the remote island (backend manifest names are a contract). 16px inline /
  20px buttons via the icon component — `!w-* !h-*` overrides are banned.
- **Motion:** 200ms standard; spin = pending; pulse = island attention (amber, island
  only); respect `prefers-reduced-motion`. No `active:` press styles.
- **Components:** Locveil-themed shadcn/ui on radix. Toast (not `window.confirm`),
  Tooltip (not `title=`), AlertDialog, Skeleton are standard. Custom stays custom:
  island family, donation card editors, Monaco panes.
- **Layout:** fluid only — no fixed-px canvases, no scale-transform hacks,
  orientation-aware (the shipped remote is grandfathered until its bridge rework).
  Plugins never own `fixed bottom-0` — the Workbench shell provides the slot.

## Checklist before finishing any UI change

Both themes rendered · RU strings fit · states (hover/focus-visible/disabled) present ·
status colors via tokens not raw classes · icons from the right family for the surface ·
radius from the right system · no new hex/hsl literals outside the tokens file.
