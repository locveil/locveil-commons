/* Builds the demo plugin exactly the way a product repo would (HK-11):
   ESM bundle with the singletons EXTERNAL + a build-emitted manifest fragment. */
import { build } from "esbuild";
import { mkdir, writeFile } from "node:fs/promises";

const SINGLETONS = ["react", "react-dom", "react-dom/client", "react/jsx-runtime", "react-router-dom", "locveil-ui-kit"];

await mkdir("demo-plugin/dist", { recursive: true });
await build({
  entryPoints: ["demo-plugin/src/index.tsx"],
  bundle: true,
  format: "esm",
  platform: "browser",
  define: { "process.env.NODE_ENV": '"production"' },
  external: SINGLETONS,
  outfile: "demo-plugin/dist/index.js",
  logLevel: "warning",
});

const manifest = {
  id: "demo",
  version: "0.1.0",
  entry: "./index.js",
  styles: ["./style.css"],
  peers: { react: "^18", "react-dom": "^18", "react-router-dom": "^6", "locveil-ui-kit": "^0.1" },
};
await writeFile("demo-plugin/dist/manifest.json", JSON.stringify(manifest, null, 2));
await writeFile(
  "demo-plugin/dist/style.css",
  ".demo-accent-frame { outline: 1px dashed hsl(var(--primary)); outline-offset: 4px; }\n"
);
console.log("demo plugin → demo-plugin/dist/");
