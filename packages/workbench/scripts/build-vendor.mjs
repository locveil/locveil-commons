/* Builds the import-map singleton bundles into dist/vendor/ (HK-11).
   Each vendor bundle externalizes the OTHER singletons so the graph shares one
   instance of everything.

   CJS→ESM interop (two owner-found live failures, first browser runs):
   1. react's packages are CJS behind a NODE_ENV conditional — esbuild can't statically
      detect their named exports, so a plain entry bundle exports only `default`.
      → we ENUMERATE exports in node and generate a static re-export entry.
   2. esbuild externalizes a package INCLUDING its subpaths, and a CJS `require()` of an
      external under ESM output becomes a throwing `__require` shim.
      → the entry requires the RESOLVED FILE (never the bare name), and a banner
        defines an ambient `require` mapping external bare names to real ESM imports —
        esbuild's __require defers to an ambient `require` when present.
   Verified by scripts/smoke-vendor.mjs, which EXECUTES the whole vendor graph. */
import { build } from "esbuild";
import { mkdir } from "node:fs/promises";
import { createRequire } from "node:module";

process.env.NODE_ENV = "production";
const require = createRequire(import.meta.url);

const SINGLETONS = ["react", "react-dom", "react-dom/client", "react/jsx-runtime", "react-router-dom", "locveil-ui-kit"];

function cjsEntryContents(specifier) {
  const resolved = require.resolve(specifier);
  const names = Object.keys(require(specifier)).filter(
    (n) => n !== "default" && n !== "__esModule" && /^[A-Za-z_$][\w$]*$/.test(n)
  );
  return [
    `const m = require(${JSON.stringify(resolved)});`,
    ...names.map((n) => `export const ${n} = m[${JSON.stringify(n)}];`),
    `export default m;`,
  ].join("\n");
}

function requireShimBanner(externals) {
  if (externals.length === 0) return "";
  const imports = externals
    .map((e, i) => `import * as __shim${i} from ${JSON.stringify(e)};`)
    .join("\n");
  const map = externals.map((e, i) => `${JSON.stringify(e)}: __shim${i}`).join(", ");
  return [
    imports,
    `const __shimmed = { ${map} };`,
    // esbuild's __require uses the ambient `require` when one is defined
    `var require = (n) => { const s = __shimmed[n]; if (!s) throw new Error("unshimmed require: " + n); return s.default ?? s; };`,
  ].join("\n");
}

const bundles = [
  { entry: "react", out: "react.js", external: [], cjs: true },
  { entry: "react/jsx-runtime", out: "react-jsx-runtime.js", external: ["react"], cjs: true },
  { entry: "react-dom", out: "react-dom.js", external: ["react"], cjs: true },
  { entry: "react-dom/client", out: "react-dom-client.js", external: ["react", "react-dom"], cjs: true },
  { entry: "react-router-dom", out: "react-router-dom.js", external: ["react", "react-dom", "react/jsx-runtime"] },
  { entry: "locveil-ui-kit", out: "locveil-ui-kit.js", external: SINGLETONS.filter((s) => s !== "locveil-ui-kit") },
];

await mkdir("dist/vendor", { recursive: true });
for (const b of bundles) {
  const common = {
    bundle: true,
    format: "esm",
    platform: "browser",
    define: { "process.env.NODE_ENV": '"production"' },
    external: b.external,
    outfile: `dist/vendor/${b.out}`,
    logLevel: "warning",
  };
  if (b.cjs) {
    await build({
      ...common,
      banner: { js: requireShimBanner(b.external) },
      stdin: {
        contents: cjsEntryContents(b.entry),
        resolveDir: process.cwd(),
        sourcefile: `vendor-${b.out}`,
        loader: "js",
      },
    });
  } else {
    await build({ ...common, entryPoints: [b.entry] });
  }
  console.log(`vendor: ${b.entry} → dist/vendor/${b.out}${b.cjs ? " (cjs re-export + require shim)" : ""}`);
}
