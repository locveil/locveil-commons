# The Locveil stylebook

**Status:** normative for all Locveil UI work. Decided by the PROD-10 style council
(two rounds of rendered choices, 2026-07-14) on the extraction evidence
(`token-inventory-draft.md`, `divergence-list.md`). Token values:
**`packages/ui-kit/tokens/locveil.css`** (+ `.json` mirror) — on disagreement the
tokens file wins over this prose. Executable half: the **`ui-style` skill** — UI
sessions load it instead of re-reading this file. Docs-manifest node: `stylebook`.

## 1. The identity — воронёная сталь

Locveil's UI is **gun-blued steel**: cool blue-grey neutrals (hue 207–213, restrained
chroma), a **polished steel-blue accent** from the same metallurgy, and — sitting on
that steel — the untouched **black-ish remote island** with its amber attention states.
The palette is monochrome-metallic on purpose: color is reserved for meaning (status,
attention), not decoration.

- Light theme: cool paper (`210 25% 97.5%`) with white cards.
- Dark theme: near-black oxide (`213 26% 8.5%`) — the primary operator environment.
- **Dual theme from day one**; `.dark` class strategy; the chrome carries a toggle.
- The **remote island is theme-independent** — a dark slab on either theme, exactly as
  shipped today. Its rework (layout AND any restyle) belongs to a dedicated
  bridge-project wireframe session, not to token work.

## 2. Color rules

- Interactive = **accent** (steel-blue `--primary`): primary buttons, active tab,
  active nav, links, focus ring. One accent; no second interactive color.
- Meaning = **status tokens**, never raw palette classes:
  pristine (steel-grey 211) · edited (orange 28) · tested (blue 210) · persisted
  (green 145) · conflict (red 0); device on/off = green/red dots. Recipes per theme are
  in the tokens file — never use Tailwind `*-50` washes on dark.
  *Owner ruling:* tested stays blue next to the blue accent — chips are pill-shaped and
  bordered precisely so they never read as buttons; keep that shape contract.
- The island's attention color stays **amber** and stays inside the island.
- Destructive actions use `--destructive`, not the conflict status hue directly.

## 3. Type

- **System sans stack, ratified** (`system-ui, -apple-system, "Segoe UI", sans-serif`)
  — Cyrillic-safe, zero bundle, offline-first (no CDN fonts on the WB7, ever).
- Scale: 11px/600/uppercase labels · 12.5px secondary · 14px body · 18px/700 headings ·
  24px/700 error/empty titles. The 8px micro-size is dropped. Island legends
  (10px/600/uppercase/tracked) are island-scoped.
- `tabular-nums` for readings and counters; `mono` for code, IDs, and log excerpts.
- RU is the first language of the product — test every layout with Russian strings
  (they run ~20% longer; labels must not truncate).

## 4. Geometry & density

- Chrome radius: **`--radius: 0.75rem`** (cards, panels, bars), derived steps for
  controls (10px) and inner elements (8px). The island keeps its own px ladder
  (24/16/12/8) — never mix the two systems in one component.
- Density: **compact** — inputs `px-3 py-2 text-sm`-equivalent, operator-tool bias.
  One density; no per-page density switches.
- Borders: 1px `--border`; shadows are rare (overlays and the island shell only).

## 5. Icons — the split ruling

- **Workbench/chrome: lucide** (stroke-2, round caps) — shadcn's native set.
- **Remote island: Material filled stays**, because backend layout manifests emit
  Material icon names (a contract) and the island's custom device glyphs
  (play-pause, tray, fan, swing, aspect ratios…) are hand-made SVG regardless.
- The boundary is the island border: no stroke icons inside it, no filled Material in
  the chrome. When the island is rebuilt (bridge session), an icon name-mapping layer
  is the prerequisite for any family change there.
- Sizes: 16px inline, 20px in buttons; the ui-kit icon component owns sizing — no
  `!w-* !h-*` overrides (the extraction found the old size system bypassed; that
  pattern is banned).

## 6. Motion & states

- Standard transition: **200ms** (`transition-colors`/`transition-all`), the extracted
  incumbent. Pending = spinner swap (`animate-spin`); armed/attention = pulse (island,
  amber). Respect `prefers-reduced-motion`.
- States on every interactive element: hover (surface tint), focus-visible (2px accent
  ring), disabled (50% opacity, no pointer events). No `active:` press styles — matches
  the shipped remotes.

## 7. Components — shadcn base (D9)

- ui-kit = **Locveil-themed shadcn/ui on radix**, tokens above as the theme. Voice's
  hand-built primitives are replaced at adoption (Dialog, Tabs, Badge, Select, Slider,
  Alert, Checkbox…); bridge completes its partial install (radix, `components.json`,
  real dropdown/dialog/tooltip instead of hand-rolled ones).
- shadcn additions adopted as standard: **Toast** (no more `window.confirm`),
  **Tooltip** (no more bare `title=`), **AlertDialog**, **Skeleton**.
- Stays custom: the island component family, the donation pattern-card editors,
  Monaco/syntax panes, repeating-row editors.

## 8. Layout requirements

- **Everything fluid** (D10): container-relative sizing, no fixed px canvases, no
  transform-scale compensation hacks, orientation-aware. The shipped remote's fixed
  320×850 layout is grandfathered until its bridge-session rework — new components
  never copy it.
- The Workbench shell (PROD-24/IMPL-1) owns: top bar, tabs, locale switch, theme
  toggle, the problem-report button, per-plugin status slot, and the single bottom
  action-bar slot (plugins must not `fixed bottom-0` themselves).

## 9. Change control

Tokens and this stylebook are commons-owned (PROD-10 lineage): changes land here via a
ledger task and version with the package (`ui-kit-vX`). Product repos consume — they do
not fork values. A visual decision not covered here goes back through a style-council
round, not into a one-off hex in a component.

## 10. The logo

- **Mark 2b + wordmark B** (owner-picked in a browser design session, integrated
  2026-07-17 as IMPL-7). Canonical assets + usage rules: `packages/brand/`. The kit's
  `<Logo>` component is the token-wired rendition — accent = `--primary`, structure =
  `--muted-foreground` — and is the way React surfaces render it; raw SVGs are for
  favicons, `<img>`, `site/` and documents, where their built-in fallbacks apply.
- Drawn in the chrome's icon language (§5): 24px grid, stroke-2, round caps/joins.
  Primary mark ≥24px; the simplified `mark-16` owns 16px slots and favicons. Lockup
  spacing derives from the mark box, `u = H/12`: gap `3u` horizontal / `4u` stacked,
  clear space `2u`.
- Two colors, never a third; **no amber** (§2) — a listening state animates the accent
  dot/arcs, never recolors.
- The brand SVGs' standalone fallback hexes are **exact renditions of the tokens**
  (`#2073B6`/`#51A6EC` accent, `#607080`/`#8794A1` structure) — the one sanctioned
  place hex literals mirror the tokens file; re-snap them whenever the tokens move.
- **The Latin wordmark is universal** (owner ruling 2026-07-17): RU surfaces use it
  as-is; no Cyrillic lockup exists or is planned.
