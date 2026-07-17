/* Dev-phase workstation server (HK-11): serves the shell dist at /, mounts each
   configured plugin LOCATION (a local path, typically a sibling repo's dist) under
   /plugins/<n>/, and generates /runtime-config.json from workbench.config.json.
   Dormant entries (gate, no location) pass through untouched — zero activity. */
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { extname, join, normalize, resolve } from "node:path";

const PORT = Number(process.env.PORT || 6107);
const ROOT = resolve("dist");
const config = JSON.parse(await readFile("workbench.config.json", "utf8"));

const mounts = [];
const runtime = { plugins: [] };
for (const entry of config.plugins ?? []) {
  if (entry.location) {
    const dir = resolve(entry.location);
    const n = mounts.length;
    mounts.push(dir);
    runtime.plugins.push({ url: `/plugins/${n}/`, backends: entry.backends ?? {} });
    if (!existsSync(dir)) console.warn(`WARN: plugin location missing on disk: ${dir}`);
  } else {
    runtime.plugins.push(entry); // dormant slot — metadata only
  }
}

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".map": "application/json",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".png": "image/png",
  ".woff2": "font/woff2",
};

async function sendFile(res, base, rel) {
  const path = normalize(join(base, rel));
  if (!path.startsWith(base)) {
    res.writeHead(403).end();
    return;
  }
  try {
    const data = await readFile(path);
    res.writeHead(200, { "content-type": MIME[extname(path)] ?? "application/octet-stream" });
    res.end(data);
  } catch {
    res.writeHead(404).end("not found");
  }
}

createServer(async (req, res) => {
  const url = new URL(req.url ?? "/", "http://localhost");
  const p = decodeURIComponent(url.pathname);

  if (p === "/runtime-config.json") {
    res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
    res.end(JSON.stringify(runtime));
    return;
  }
  const m = /^\/plugins\/(\d+)\/(.*)$/.exec(p);
  if (m) {
    const base = mounts[Number(m[1])];
    if (!base) {
      res.writeHead(404).end();
      return;
    }
    await sendFile(res, base, m[2] || "index.html");
    return;
  }
  if (p === "/" || !existsSync(join(ROOT, normalize(p)))) {
    await sendFile(res, ROOT, "index.html"); // SPA fallback (hash router barely needs it)
    return;
  }
  await sendFile(res, ROOT, p);
}).listen(PORT, () => {
  console.log(`Locveil Workbench @ http://localhost:${PORT}`);
  runtime.plugins.forEach((e, i) =>
    console.log(e.url ? `  plugin ${i}: ${mounts[i] ?? "?"} → ${e.url}` : `  dormant: ${e.id} (${e.gate?.all?.join(" + ")})`)
  );
});
