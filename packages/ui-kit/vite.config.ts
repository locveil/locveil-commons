import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";

// Library build: version-agnostic ESM + externalized deps (style council ruling —
// vite majors are per-consumer; the kit ships plain ESM both vite 6 and 8 consume).
export default defineConfig({
  plugins: [react()],
  build: {
    lib: {
      entry: path.resolve(__dirname, "src/index.ts"),
      formats: ["es"],
      fileName: () => "index.js",
    },
    rollupOptions: {
      external: (id) => !id.startsWith(".") && !path.isAbsolute(id),
    },
    sourcemap: true,
  },
});
