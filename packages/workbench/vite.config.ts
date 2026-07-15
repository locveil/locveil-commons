import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

/* The shell externalizes the HK-11 singleton set — its own code resolves react &
   friends through the SAME import map plugins use, so there is exactly one instance
   of each singleton at runtime by construction. */
const SINGLETONS = [
  "react",
  "react-dom",
  "react-dom/client",
  "react/jsx-runtime",
  "react-router-dom",
  "locveil-ui-kit",
];

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      external: SINGLETONS,
      output: { format: "es" },
    },
    sourcemap: true,
    // vendor bundles are emitted separately by scripts/build-vendor.mjs into dist/vendor
    emptyOutDir: false,
  },
});
