# Style divergence list — the stage-② council agenda (PROD-10 ①)

**Status:** extraction output, 2026-07-14. Anchored by PROD-10. Each entry below becomes
a rendered A/B card on the style-council pages (stage ② — preference by rendered
variants, never by terms). Owner weighting applied: where config-ui or appliance pages
"disagree" with the remote, that is usually **no-decision-exists**, not a conflict —
those entries ask a fresh question instead of arbitrating two accidents.
Evidence citations: `docs/design/ui/token-inventory-draft.md`.

| # | question | evidence / options | council render |
|---|---|---|---|
| **D1** | **Icon family** | Bridge: Material (backend layout-manifest contract emits Material names + custom SVG remote glyphs). Voice: lucide (~48 icons). shadcn default: lucide. Options: (a) Material everywhere; (b) lucide everywhere + name-mapping layer for the backend contract (+ future contract evolution note); (c) split — Material inside the remote island, lucide for workbench/chrome | same panel rendered with both families |
| **D2** | **Shell accent** | Amber is the de-facto bridge shell accent (ratified bug-button hover, dialog primaries, attention states). Voice/T3 + stock shadcn: blue-600. Also: amber currently doubles as the ATTENTION color on tier 1 — if amber becomes the accent, attention may need its own hue (or stays amber-on-dark-island only) | chrome + buttons rendered amber vs blue vs a third candidate |
| **D3** | **Base neutrals + primary (the shadcn variable values)** | Never chosen: bridge runs stock zinc/blue defaults; voice runs raw gray-x00. The remote island's warm dark greys (#2a2a2a/#1a1a1a/#404040) are the only APPROVED neutrals — candidate: derive the app neutral ramp from them | 2–3 full palette candidates rendered on the same page (light+dark) |
| **D4** | **Dark-mode policy for the Workbench** | Island: dark-by-design (unchanged either way). Bridge chrome: dual-theme plumbing exists, no toggle, some light-only washes. Voice: none. shadcn vars make dual-theme cheap. Options: (a) dual-theme from day one + chrome toggle; (b) light-first, dark later | same page light vs dark |
| **D5** | **Radius scale** | Island ladder 24/16/12/8px (approved, stays) vs chrome `--radius: 0.5rem` (stock default, never chosen). Question is the CHROME radius: sharper (0.375), stock (0.5), rounder (0.75)? config-ui's md/lg/xl/2xl chaos is evidence-of-nothing | identical form/card/button set at 3 radius values |
| **D6** | **Type: stack + scale** | No webfont anywhere; system sans is the incumbent (and RU-safe by construction). Scale de-facto: 10 legend /12/14/18/24 (+8px ticks — kill?). Options: (a) ratify system stack; (b) webfont with full Cyrillic (e.g. Inter/IBM Plex) — cost: bundle + offline-first hosting (no CDN on WB7!) | same content system-stack vs webfont, RU + EN sample text |
| **D7** | **Density** | config-ui compact admin (px-3 py-2 text-sm inputs) vs bridge looser T3 pages. Workbench is an operator tool — compact is the incumbent bias | same form at 2 densities |
| **D8** | **Semantic status tokens** | The one near-deliberate T3 system: tint recipe `{c}-50/200/700` + workflow mapping gray/orange/blue/green/red (pristine/edited/tested/persisted/conflict) + island's green-600/red-600 on/off. Proposal: ratify as tokens (adjusted for dark mode — the -50 washes break there) | status chips/banners rendered light+dark |
| **D9** | **ui-kit base = themed shadcn/radix** | Feasibility verdict: strong yes (inventory §9 — bridge is 80% installed, voice maps cleanly, gaps are exactly shadcn's additions). Owner already leaning ("standard components if it works out"). Council card = confirmation with the migration sketch, not A/B | decision card (no render) |
| **D10** | **Fluid remote requirement** | Not a preference — a requirement carried into ui-kit: container-relative sizing, no fixed 320/850px, no scale-75 hacks, orientation-aware; zoning per remote.png preserved (POWER / INPUTS / PLAYBACK / TRACKS / SCREEN·MENU·VOLUME / APPS / POINTER). Owner note: even the wireframe may evolve pre-release — the ui-kit components must not bake the current zoning as the only composition | requirement card (no render); a responsive mock MAY be shown for confirmation |

**Backlog notes (not council cards):** global pending-dims-all UX on the remote;
bottom-slot arbitration + status-slot absorption (owned by PROD-24/IMPL-1 contract);
bridge dead deps (@mui/material, emotion, unwired i18next) ride ui-kit adoption; icon
size-prop redesign rides D1's outcome; bridge theme variables move out of index.html at
codification.
