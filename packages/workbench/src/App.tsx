import * as React from "react";
import {
  HashRouter,
  Navigate,
  Route,
  Routes,
  useNavigate,
  useParams,
} from "react-router-dom";
import { ActionBarHost, Toaster, cn } from "locveil-ui-kit";
import type { Locale, PageDescriptor, ReportContext } from "./contract";
import type { LoadedPlugin } from "./loader";
import { initialLocale, ls, persistLocale, t } from "./i18n";
import { applyTheme, initialTheme, type Theme } from "./theme";
import { TopBar } from "./chrome/TopBar";
import { PluginView } from "./chrome/PluginView";

export interface AppProps {
  plugins: LoadedPlugin[];
}

export function App({ plugins }: AppProps) {
  const [locale, setLocale] = React.useState<Locale>(initialLocale);
  const [theme, setTheme] = React.useState<Theme>(initialTheme);

  React.useEffect(() => applyTheme(theme), [theme]);
  React.useEffect(() => persistLocale(locale), [locale]);

  const firstActive = plugins.find((p) => p.kind === "active");

  return (
    <HashRouter>
      <div className="flex h-screen flex-col bg-background text-foreground">
        <TopBar
          plugins={plugins}
          locale={locale}
          onLocale={setLocale}
          theme={theme}
          onTheme={setTheme}
        />
        <div className="flex min-h-0 flex-1">
          <Routes>
            <Route
              path="/"
              element={
                firstActive && firstActive.kind === "active" ? (
                  <Navigate to={`/p/${firstActive.plugin.id}`} replace />
                ) : (
                  <EmptyState locale={locale} />
                )
              }
            />
            <Route
              path="/p/:pluginId/*"
              element={<PluginRoute plugins={plugins} locale={locale} />}
            />
          </Routes>
        </div>
        {/* IMPL-5: the ONE bottom action-bar slot — plugins render <ActionBar>
            (locveil-ui-kit) anywhere in their tree; the kit's singleton bus delivers
            it here. Plugin-owned fixed bottom-0 is banned (stylebook §8). */}
        <ActionBarHost />
        {/* IMPL-4: the ONE toast viewport — plugins call toast() through the
            import-map singleton bus; they never render their own Toaster */}
        <Toaster />
      </div>
    </HashRouter>
  );
}

function PluginRoute({ plugins, locale }: { plugins: LoadedPlugin[]; locale: Locale }) {
  const { pluginId } = useParams();
  const entry = plugins.find((p) => p.kind === "active" && p.plugin.id === pluginId);
  if (!entry || entry.kind !== "active") return <EmptyState locale={locale} />;
  return (
    <PluginView
      key={pluginId}
      plugin={entry.plugin}
      locale={locale}
      backends={entry.backends}
    />
  );
}

function EmptyState({ locale }: { locale: Locale }) {
  return (
    <main className="flex flex-1 items-center justify-center p-6">
      <p className="max-w-md text-center text-sm text-muted-foreground">
        {t(locale, "noPlugins")}
      </p>
    </main>
  );
}

/* Shared helpers for chrome components */
export function useReportHook(
  plugins: LoadedPlugin[],
  locale: Locale
): { enabled: boolean; fire: () => void } {
  const navigate = useNavigate();
  void navigate;
  const active = currentActive(plugins);
  const enabled = !!active?.plugin.reportHook;
  const fire = React.useCallback(() => {
    if (!active?.plugin.reportHook) return;
    const route = window.location.hash.split("/").slice(3).join("/") || "";
    const ctx: ReportContext = { pluginId: active.plugin.id, route, locale };
    active.plugin.reportHook(ctx);
  }, [active, locale]);
  return { enabled, fire };
}

export function currentActive(plugins: LoadedPlugin[]) {
  const m = /#\/p\/([^/]+)/.exec(window.location.hash);
  const id = m?.[1];
  const found = plugins.find((p) => p.kind === "active" && p.plugin.id === id);
  return found && found.kind === "active" ? found : undefined;
}

export function pageTitle(locale: Locale, p: PageDescriptor): string {
  return ls(locale, p.title);
}

export function cnx(...args: Parameters<typeof cn>): string {
  return cn(...args);
}
