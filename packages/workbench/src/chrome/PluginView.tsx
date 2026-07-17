import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import { cn } from "locveil-ui-kit";
import type { Locale, PageDescriptor, WorkbenchPlugin } from "../contract";
import { ls, t } from "../i18n";

/* Sidebar of the active plugin's pages + the content outlet — the wireframe's
   second nav level. Pages are read per render pass: RUNTIME-registrable (UI-16). */
export function PluginView({
  plugin,
  locale,
  backends,
}: {
  plugin: WorkbenchPlugin;
  locale: Locale;
  backends: Record<string, string>;
}) {
  const pages: PageDescriptor[] = plugin.pages();

  if (pages.length === 0)
    return (
      <main className="flex flex-1 items-center justify-center p-6 text-sm text-muted-foreground">
        {t(locale, "noPages")}
      </main>
    );

  return (
    <>
      <aside className="w-[var(--wb-rail-w)] shrink-0 overflow-y-auto border-r border-border bg-card p-2">
        <nav className="flex flex-col gap-0.5">
          {pages.map((p) => (
            <NavLink
              key={p.route}
              to={p.route}
              className={({ isActive }) =>
                cn(
                  "rounded-md px-2.5 py-1.5 text-sm transition-colors duration-200",
                  isActive
                    ? "bg-primary/15 font-semibold text-foreground"
                    : "text-muted-foreground hover:bg-muted hover:text-foreground"
                )
              }
            >
              {ls(locale, p.title)}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="min-w-0 flex-1 overflow-y-auto p-4">
        <Routes>
          <Route index element={<Navigate to={pages[0].route} replace />} />
          {pages.map((p) => (
            <Route
              key={p.route}
              path={p.route}
              element={<p.render locale={locale} backends={backends} />}
            />
          ))}
        </Routes>
      </main>
    </>
  );
}
