/* Builds the import-map singleton bundles into dist/vendor/ (HK-11).
   Each vendor bundle externalizes the OTHER singletons so the graph shares one
   instance of everything — react-dom/client re-exports from the external react-dom,
   router leans on the external react, ui-kit on all of them. */
import { build } from "esbuild";
import { mkdir } from "node:fs/promises";

const SINGLETONS = ["react", "react-dom", "react-dom/client", "react/jsx-runtime", "react-router-dom", "locveil-ui-kit"];

const bundles = [
  { entry: "react", out: "react.js", external: [] },
  { entry: "react/jsx-runtime", out: "react-jsx-runtime.js", external: ["react"] },
  { entry: "react-dom", out: "react-dom.js", external: ["react"] },
  { entry: "react-dom/client", out: "react-dom-client.js", external: ["react", "react-dom"] },
  { entry: "react-router-dom", out: "react-router-dom.js", external: ["react", "react-dom", "react/jsx-runtime"] },
  { entry: "locveil-ui-kit", out: "locveil-ui-kit.js", external: SINGLETONS.filter((s) => s !== "locveil-ui-kit") },
];

await mkdir("dist/vendor", { recursive: true });
for (const b of bundles) {
  await build({
    entryPoints: [b.entry],
    bundle: true,
    format: "esm",
    platform: "browser",
    define: { "process.env.NODE_ENV": '"production"' },
    external: b.external,
    outfile: `dist/vendor/${b.out}`,
    logLevel: "warning",
  });
  console.log(`vendor: ${b.entry} → dist/vendor/${b.out}`);
}
