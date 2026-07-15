import type {
  GateDescriptor,
  LocalizedString,
  ManifestFragment,
  WorkbenchPlugin,
} from "./contract";

/* The shell's actual singleton majors — the refuse-and-surface baseline (HK-11).
   Kept in lockstep with package.json/the import map by review; a drift check is the
   natural first workbench guard. */
export const SHELL_SINGLETONS: Record<string, number> = {
  react: 18,
  "react-dom": 18,
  "react-router-dom": 6,
  "locveil-ui-kit": 0, // 0.x line: minor is breaking — see majorOf/compatible
};
const UI_KIT_MINOR = 1; // locveil-ui-kit 0.1.x

export type LoadedPlugin =
  | {
      kind: "active";
      fragment: ManifestFragment;
      plugin: WorkbenchPlugin;
      baseUrl: string;
      backends: Record<string, string>;
    }
  | { kind: "dormant"; id: string; title: LocalizedString; gate: GateDescriptor }
  | { kind: "failed"; id: string; reason: string };

function parseRange(range: string): { major: number; minor: number } {
  const m = /(\d+)(?:\.(\d+))?/.exec(range);
  return { major: m ? parseInt(m[1], 10) : -1, minor: m && m[2] ? parseInt(m[2], 10) : 0 };
}

/** Strict-major (0.x: strict-minor too). Returns a human reason on mismatch. */
export function peerMismatch(peers: Record<string, string>): string | null {
  for (const [name, range] of Object.entries(peers)) {
    if (!(name in SHELL_SINGLETONS)) continue; // non-singleton peers are the plugin's business
    const want = parseRange(range);
    const have = SHELL_SINGLETONS[name];
    if (want.major !== have) return `${name}: plugin wants ${range}, shell has ${have}.x`;
    if (have === 0 && want.minor !== UI_KIT_MINOR)
      return `${name}: plugin wants ${range}, shell has 0.${UI_KIT_MINOR}.x`;
  }
  return null;
}

function injectStyles(base: URL, styles: string[] | undefined): void {
  for (const href of styles ?? []) {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = new URL(href, base).toString();
    link.dataset.workbenchPlugin = base.toString();
    document.head.appendChild(link);
  }
}

async function loadOne(baseUrl: string, backends: Record<string, string>): Promise<LoadedPlugin> {
  /* Config URLs are root-relative ("/plugins/0/") — a URL BASE must be absolute
     (browser-only failure class; anchor to the shell origin first). */
  const base = new URL(baseUrl, window.location.href);
  const manifestUrl = new URL("manifest.json", base).toString();
  let fragment: ManifestFragment;
  try {
    const res = await fetch(manifestUrl);
    if (!res.ok) return { kind: "failed", id: baseUrl, reason: `manifest.json → HTTP ${res.status}` };
    fragment = (await res.json()) as ManifestFragment;
  } catch (e) {
    return { kind: "failed", id: baseUrl, reason: `manifest fetch failed: ${String(e)}` };
  }

  const mismatch = peerMismatch(fragment.peers ?? {});
  if (mismatch) return { kind: "failed", id: fragment.id, reason: `peer mismatch — ${mismatch}` };

  injectStyles(base, fragment.styles);

  try {
    const entryUrl = new URL(fragment.entry, base).toString();
    const mod = (await import(/* @vite-ignore */ entryUrl)) as { default?: WorkbenchPlugin };
    if (!mod.default?.id || typeof mod.default.pages !== "function")
      return { kind: "failed", id: fragment.id, reason: "entry has no WorkbenchPlugin default export" };
    return { kind: "active", fragment, plugin: mod.default, baseUrl, backends };
  } catch (e) {
    return { kind: "failed", id: fragment.id, reason: `entry import failed: ${String(e)}` };
  }
}

interface RuntimeEntry {
  url?: string;
  id?: string;
  title?: LocalizedString;
  gate?: GateDescriptor;
  backends?: Record<string, string>;
}

/** Reads the serve-script-generated runtime config; dormant entries load NOTHING. */
export async function loadPlugins(): Promise<LoadedPlugin[]> {
  let entries: RuntimeEntry[];
  try {
    const res = await fetch("/runtime-config.json");
    if (!res.ok) return [];
    entries = ((await res.json()) as { plugins: RuntimeEntry[] }).plugins;
  } catch {
    return [];
  }

  return Promise.all(
    entries.map(async (e): Promise<LoadedPlugin> => {
      if (e.gate && !e.url)
        return { kind: "dormant", id: e.id ?? "?", title: e.title ?? e.id ?? "?", gate: e.gate };
      if (!e.url) return { kind: "failed", id: e.id ?? "?", reason: "config entry has neither url nor gate" };
      return loadOne(e.url.endsWith("/") ? e.url : e.url + "/", e.backends ?? {});
    })
  );
}
