/* Builds the import-map singleton bundles into dist/vendor/ (HK-11).
   Each vendor bundle externalizes the OTHER singletons so the graph shares one
   instance of everything.

   CJS→ESM interop (owner-found live, first browser run): react's packages are CJS
   behind a NODE_ENV conditional re-export — esbuild cannot statically detect their
   named exports, so a plain entry bundle exports only `default` and true-ESM importers
   (`import { Fragment } from "react/jsx-runtime"`) throw at evaluation. Fix: for CJS
   entries we ENUMERATE the exports in node at build time and generate a static
   re-export entry (the vite-prebundle strategy). ESM entries (react-router-dom,
   locveil-ui-kit) keep the direct path — their named exports survive statically. */
import { build } from "esbuild";
import { mkdir } from "node:fs/promises";
import { createRequire } from "node:module";

process.env.NODE_ENV = "production";
const require = createRequire(import.meta.url);

const SINGLETONS = ["react", "react-dom", "react-dom/client", "react/jsx-runtime", "react-router-dom", "locveil-ui-kit"];

function cjsEntryContents(specifier) {
  const names = Object.keys(require(specifier)).filter(
    (n) => n !== "default" && n !== "__esModule" && /^[A-Za-z_$][\w$]*$/.test(n)
  );
  return [
    `const m = require(${JSON.stringify(specifier)});`,
    ...names.map((n) => `export const ${n} = m[${JSON.stringify(n)}];`),
    `export default m;`,
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
  console.log(`vendor: ${b.entry} → dist/vendor/${b.out}${b.cjs ? " (cjs re-export)" : ""}`);
}
