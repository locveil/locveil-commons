# Locveil token inventory — extraction draft (PROD-10 stage ①)

**Status:** draft evidence, 2026-07-14. Mined read-only from `locveil-bridge/ui` and
`locveil-voice/config-ui` at their current HEADs, plus the owner's remote scan
(`locveil-bridge/docs/design/ui/remote.png`). Anchored by PROD-10 (board). Consumed by
stage ② (style council) and ③ (stylebook/tokens file). Nothing here is final — tier-1
entries are owner-approved-by-use; everything else is inventory.

**Evidence tiers (owner ruling at extraction start):**
- **T1** — the remote control pages (device remotes + scenarios) + the remote scan: the
  only deliberately styled, owner-approved surfaces.
- **T2** — shared bridge chrome (Navbar, Icon wrapper); the bug-button treatment is
  already ratified (PROD-24).
- **T3** — appliance pages + all of config-ui: "worked, never styled" — inventory, not
  taste.

---

## 1. Headline finding: the token carrier already exists (and is empty)

Bridge `ui/` is a **stock shadcn/ui install in all but name**: the full shadcn
CSS-variable semantic theme (`background/foreground/primary/…/muted/accent` +
`--radius`) in `tailwind.config.js:21-60`, `darkMode: ["class"]`, canonical
`cn()`/`cva` (`src/lib/utils.ts:4-6`), a `components/ui/` dir with a verbatim shadcn
Button. **But the variable values are the untouched shadcn defaults** (zinc neutrals,
blue-600-ish primary, 0.5rem radius — `index.html:11-56`) — i.e. the theme system was
adopted, its values were never chosen. Voice config-ui has **no theme layer at all**
(stock tailwind config, `theme.extend: {}`, every decision inline).

**Consequence:** the Locveil tokens file (stage ③) is not an invention — it is *filling
in the shadcn CSS variables* (plus a small extension set below), which both UIs can
consume natively. Two delivery defects to fix at codification: bridge's variables live
in an inline `<style>` in `index.html` (move to a real CSS file), and the theme's dead
freight (radix accordion keyframes with no radix installed) gets dropped.

## 2. Second headline: MUI is a ghost

`@mui/material` + emotion have **zero imports** in bridge src. The only MUI usage is
`@mui/icons-material` (one wildcard import, `src/components/icons/index.tsx:8`). There
is no MUI-vs-Tailwind divergence to reconcile — both UIs express appearance in Tailwind.
"Replace MUI" = replace the icon set + delete three dead dependencies. Caveat: **the
icon vocabulary is a backend contract** — bridge layout manifests emit Material icon
names (`action.icon.iconName`, resolved by string lookup into the full
`@mui/icons-material` namespace) — so an icon-family change needs a mapping layer, not
just a dependency swap. → divergence D1.

## 3. Tier-1 tokens (approved by use — the remote island)

The remote deliberately ignores the theme system: a self-contained **dark "physical
remote" island** styled by a runtime-injected stylesheet
(`RemoteControlLayout.tsx:1243-1573`), identical in light and dark mode. Its decisions:

| token (proposed name) | value | evidence |
|---|---|---|
| `island.shell` | metal gradient `135deg #2a2a2a → #1a1a1a` (5 stops) | RemoteControlLayout.tsx:1253-1259 |
| `island.shell.border` | `2px solid #404040` + shadow `0 8px 32px rgba(0,0,0,.3)` + inset white/10 top highlight | :1262-1267 |
| `island.surface.1/2/3` | white-alpha ladder `rgba(255,255,255,.03/.05/.08)` | zones :1315-1342, groups :1352-1360, pointer :1513 |
| `island.border` | `1px solid rgba(255,255,255,.10)` (dimmer `.08` on central zones) | :1318, :1436 |
| `island.inset` | `rgba(0,0,0,.2)` control strip · `.3` header chip · form fields `bg-black/30 border-white/20` | :1295-1312, :1279-1285, :273 |
| `island.text` | white · `white/70` secondary · `white/50–40` dimmed · `rgba(255,255,255,.4)` empty | :1100, :606, :63, :1527 |
| `state.on` / `state.off` | `green-600` / `red-600` | :60, :81-86 |
| `state.attention` | **amber family**: `ring-amber-400 animate-pulse` armed · `border-amber-400/60 bg-amber-500/15 text-amber-200` banner · `text-amber-300/400` notes/errors | :94-97, :1109, :1215, :260 |
| `state.info/fill` | `blue-400` slider fill/ticks, `blue-500` indicator | :628-689 |
| `button.remote` | rounded-square ghost: `bg-transparent border-white/30 text-white hover:bg-white/10 hover:border-white/50 transition-all duration-200` — repeated verbatim ~15× | :108 et al., NavCluster.tsx:76 et al. |
| `radius.island` | px ladder **24 shell / 16 strip / 12 zone / 8 group**; buttons `rounded-md` | :1262, :1302, :1318, :1355 |
| `type.legend` | 10px · 600 · uppercase · tracking .5px · `white/70` | :1379-1383 |
| `type.scale` (de-facto) | 8px ticks · 10px legends · xs(12) · sm(14) · lg(18) bold header · 2xl(24) errors; weights 500/600/700 | :677, :1100, button.tsx:7 |
| `motion.standard` | `transition-all duration-200`; pending = `Refresh` icon + `animate-spin`; armed = `animate-pulse` | throughout |
| `size.button` | `h-8` (power/mute) · `h-10` (media/screen/volume) · `h-14` (nav grid) | :108-748, NavCluster.tsx:70-76 |
| `density.island` | container p-16px · zone gap 8-12px · grid gap 8px | :1272-1291 |

**T2 (ratified/near-ratified chrome):** Navbar `h-16 bg-card border-b border-border`;
ghost icon buttons `text-muted-foreground hover:text-amber-400` (the PROD-24-ratified
bug button, Navbar.tsx:260); dialog primary `bg-amber-600 hover:bg-amber-500`
(ReportProblemDialog.tsx:104) — **amber is the de-facto shell accent** (→ D2).
Focus: cva `focus-visible:ring-2 ring-ring` (button.tsx:7). Disabled: `opacity-50`.

## 4. Tier-3 inventory (exists — not taste)

- **config-ui de-facto look:** `bg-gray-50` page / `bg-white` cards / `border-gray-200/300`
  / gray-500..900 text ramp / **blue-600 accent** — the stock Tailwind admin. Type:
  `text-sm` dominant (263×), `font-medium` (156×). Radii **incoherent by evidence**
  (`md/lg/xl/2xl/full` coexist) — proof of no system.
- **The one near-deliberate T3 pattern, worth preserving as tokens:** the semantic tint
  recipe `bg-{c}-50 border-{c}-200 text-{c}-700/800` (error red, warning yellow, success
  green, info blue, edited orange) + the workflow-state mapping pristine=gray /
  edited=orange / tested=blue / persisted=green / conflict=red
  (WorkflowStatusIndicator.tsx:40-91). → D8.
- **Bridge T3:** HvacPanel/KitchenHoodPage are clean shadcn-token consumers
  (`rounded-lg border-border`, responsive enum grids, `tabular-nums` readings) — newer
  code already converging on the system; light-mode-only washes (`bg-blue-50/50` etc.,
  DeviceStatePanel.tsx:323-377) break in dark mode.
- **Density (T3):** config-ui compact admin — inputs `px-3 py-2 text-sm`, sm buttons
  `px-2 py-1 text-xs`; three parallel hand-rolled Button size props.

## 5. Typography & fonts

**No webfont exists anywhere** — both UIs render Tailwind's default system sans stack;
the only explicit font-family in either repo is the custom Number SVG icon
(`Number.tsx:26`). RU text renders through the system stack today (no Cyrillic-specific
handling). `font-mono` for code/values (both repos), `tabular-nums` for readings
(HvacPanel). → D6 (confirm system stack vs pick a webfont with Cyrillic coverage).

## 6. Icons

- Bridge: **Material** (@mui/icons-material) via a wrapper with fallback chain
  (material → custom → fallback map → `Help` at 50% opacity, icons/index.tsx:85-109) +
  a hand-made custom SVG set for device-remote glyphs (play-pause, tray, fan, swing,
  aspect ratios, numbers — icons/custom/). Names arrive from the backend layout
  manifest (contract!).
- Voice: **lucide-react**, ~48 icons, sized `w-3/4/5` (12/16/20px).
- Bridge's wrapper size system (sm/md/lg = 12/16/20px) is **bypassed on tier 1** with
  `!w-8 !h-8`-style overrides — the size scale needs a redesign in ui-kit regardless of
  family. → D1.

## 7. Dark/light reality

- The remote island is **dark-by-design** and theme-independent (approved look: a dark
  slab even on a light page).
- Bridge chrome: full shadcn dual-theme plumbing exists (`.dark` class, system-pref
  watcher, both variable blocks populated) but **no toggle UI**, zero `dark:` classes in
  src, and some light-only chrome washes.
- Voice: no dark mode at all (zero `dark:` classes; one component-local Monaco toggle).
- → D4 (workbench theme policy; the shadcn-var token carrier makes dual-theme cheap).

## 8. Requirements carried forward (not tokens)

1. **Fluid remote (the stiffness, mechanism documented):** fixed
   `width: 320px; min-height: 850px; aspect-ratio: 4/10.5` with exactly two hand-tuned
   breakpoints (280px@≤640, 360px@iPad-portrait; nothing landscape/desktop/4K —
   RemoteControlLayout.tsx:1245-1250, 1533-1571); fixed 192px NavCluster shrunk via
   `scale-75 transform` with padding compensation (:967, NavCluster.tsx:70, :1450);
   absolute-px slider (:621, :675); seven literal "FIX:" patch comments; the whole
   island as a per-mount `dangerouslySetInnerHTML` stylesheet. **The zoning (remote.png:
   POWER row → INPUTS/PLAYBACK/TRACKS → SCREEN·MENU·VOLUME → APPS → POINTER) is
   approved and survives; the fixed geometry does not.** ui-kit remote components must
   be container-relative and orientation-aware.
2. **Theme delivery**: CSS variables move from `index.html` inline style to a real
   stylesheet; tokens file becomes their single source.
3. **Icon size system**: wrapper scale redesign (current one bypassed with `!important`).
4. **Global pending-dims-all**: every remote button disables while ANY action is
   pending (`isActionPending`) — retain or scope-per-zone is a ux question for the
   council backlog, noted, not urgent.
5. **Shell slot arbitration** (PROD-24 input): config-ui has two independent
   `fixed bottom-0 z-50` bars (ApplyChangesBar, LocalizationsPage:363) — the Workbench
   needs one owned bottom-slot; Header's connection-polling status pill (30s /
   exponential backoff, Header.tsx:39-47) is exactly what the plugin `status` slot must
   absorb.
6. **Dead deps cleanup** (bridge): @mui/material, @emotion/react, @emotion/styled,
   i18next/react-i18next (installed, never imported — bridge UI is not i18n-wired yet;
   `name.en` hardcoded in Navbar) — cleanup rides ui-kit adoption, and the plugin
   contract's i18n bundles fix the gap properly.

## 9. shadcn/ui feasibility verdict (owner asked: "if it works out")

**It works out — strongly.** Evidence: bridge is already a minimal shadcn install
(§1-§2) missing only radix primitives, `components.json`, and real
dropdown/dialog/tooltip components (its hand-rolled ones are the exact gaps shadcn
fills); voice's hand-built primitives map cleanly (Badge→Badge, Input/TextArea→Input/
Textarea+Label, Toggle→Checkbox, Section→Card+Collapsible, BlockingConflictsDialog→
Dialog — no portal/focus-trap/Esc today, LanguageTabs→Tabs, LanguageSwitcher→
ToggleGroup, ConfigWidgets selects→Select (all native `<select>` today), RangeSlider→
Slider, ValidationErrorDisplay→Alert) and shadcn *adds* what's missing everywhere
(Toast — feedback is `window.confirm()` today, Tooltip — `title=` only, Skeleton,
AlertDialog). Genuinely custom and staying custom: the remote-island component family,
the donation pattern-card editor family, Monaco/syntax-highlighter panes, ArrayWidget-
style repeating-row editors. Recommended shape: **ui-kit = a Locveil-themed shadcn set
(radix under it) + the tokens file + the custom families** — voice replaces primitives
at adoption, bridge completes its install. Icon default question rides D1 (shadcn's
own default is lucide).
