# locveil-ui-kit

The Locveil design system as code: **blued-steel tokens** + shadcn-style primitives on
radix. Decided by the PROD-10 style council (2026-07-14); normative prose:
`../../docs/design/ui/stylebook.md` (token values in `tokens/locveil.css` win).
Versioned with `ui-kit-vX` tags. Deployment-class-agnostic: the Workbench shell
(IMPL-1), voice config-ui, and bridge's operations `ui` all consume the same package.

## Consumption (dev-phase: sibling `file:` deps — the eval-framework pattern)

```jsonc
// package.json
"dependencies": { "locveil-ui-kit": "file:../../locveil-commons/packages/ui-kit" }
```

```js
// tailwind.config.js — the preset + scan the kit for utility classes
module.exports = {
  presets: [require("locveil-ui-kit/preset")],
  content: [
    "./src/**/*.{ts,tsx}",
    "./node_modules/locveil-ui-kit/dist/**/*.js",
  ],
};
```

```ts
// app entry — tokens once, both themes included (`.dark` class strategy)
import "locveil-ui-kit/tokens.css";
import { Button, StatusChip, Dialog } from "locveil-ui-kit";
```

Build the kit before consuming: `npm install && npm run build` (emits version-agnostic
ESM + types to `dist/` — vite majors are per-consumer by council ruling).

## Rules (the short version — full: stylebook + the `ui-style` skill)

- One interactive color: the steel-blue accent. Status = `StatusChip`/`StatusDot`,
  never raw palette classes; pills are the status-vs-interaction contract.
- Icons: lucide in workbench/chrome via `<Icon>` (16px inline / 20px button — sizing is
  owned here, `!w-*` overrides banned). Material filled stays inside the remote island.
- Both themes always; compact density; system type stack; 200ms motion;
  `prefers-reduced-motion` respected.
- Island tokens (`--lv-island-*`) ship in tokens.css for the bridge's island components;
  the island family itself stays bridge-owned.

## Workbench

`npm run storybook` — the living workbench (theme toolbar renders every story on both
grounds). Stories double as the stylebook's rendered examples.
