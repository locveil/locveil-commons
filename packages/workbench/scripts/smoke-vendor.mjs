/* EXECUTES the vendor graph (the check static greps can't give): re-bundles a probe
   with the bare singleton names aliased to the built vendor files — an esbuild `alias`
   stand-in for the browser import map — then runs the result in node. Fails loudly on
   any interop regression (missing named exports, throwing require shims). */
import { build } from "esbuild";
import { writeFile, rm } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import { resolve } from "node:path";

const probe = `
import * as React from "react";
import { Fragment, jsx, jsxs } from "react/jsx-runtime";
import { createRoot } from "react-dom/client";
import * as ReactDOM from "react-dom";
import { HashRouter } from "react-router-dom";
import { Button, StatusChip, toast, ActionBar } from "locveil-ui-kit";
const checks = {
  useState: typeof React.useState,
  Fragment: typeof Fragment, jsx: typeof jsx, jsxs: typeof jsxs,
  createRoot: typeof createRoot, createPortal: typeof ReactDOM.createPortal,
  HashRouter: typeof HashRouter,
  Button: typeof Button, StatusChip: typeof StatusChip,
  toast: typeof toast, ActionBar: typeof ActionBar,
};
const bad = Object.entries(checks).filter(([, t]) => t === "undefined");
if (bad.length) { console.error("SMOKE FAIL:", bad); process.exit(1); }
console.log("SMOKE OK:", checks);
`;

const v = (f) => resolve(`dist/vendor/${f}`);
await writeFile("dist/.smoke-entry.mjs", probe);
await build({
  entryPoints: ["dist/.smoke-entry.mjs"],
  bundle: true,
  format: "esm",
  platform: "node",
  outfile: "dist/.smoke-bundle.mjs",
  alias: {
    react: v("react.js"),
    "react/jsx-runtime": v("react-jsx-runtime.js"),
    "react-dom": v("react-dom.js"),
    "react-dom/client": v("react-dom-client.js"),
    "react-router-dom": v("react-router-dom.js"),
    "locveil-ui-kit": v("locveil-ui-kit.js"),
  },
  logLevel: "warning",
});
const res = spawnSync(process.execPath, ["dist/.smoke-bundle.mjs"], { encoding: "utf8" });
process.stdout.write(res.stdout);
process.stderr.write(res.stderr);
await rm("dist/.smoke-entry.mjs", { force: true });
await rm("dist/.smoke-bundle.mjs", { force: true });
process.exit(res.status ?? 1);
