import * as React from "react";
import { NavLink } from "react-router-dom";
import { Moon, Sun } from "lucide-react";
import { Button, Icon, Logo, Tooltip, TooltipContent, TooltipProvider, TooltipTrigger, cn } from "locveil-ui-kit";
import type { Locale, PluginStatus } from "../contract";
import type { LoadedPlugin } from "../loader";
import { ls, t } from "../i18n";
import type { Theme } from "../theme";
import { useReportHook } from "../App";

/* The ratified BugReport glyph — Material filled, shipped as raw SVG (no MUI dep);
   quiet-grey with amber hover per the PROD-24 ruling. */
function BugGlyph() {
  return (
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden>
      <path d="M20 8h-2.81c-.45-.78-1.07-1.45-1.82-1.96L17 4.41 15.59 3l-2.17 2.17C12.96 5.06 12.49 5 12 5s-.96.06-1.41.17L8.41 3 7 4.41l1.62 1.63C7.88 6.55 7.26 7.22 6.81 8H4v2h2.09c-.05.33-.09.66-.09 1v1H4v2h2v1c0 .34.04.67.09 1H4v2h2.81c1.04 1.79 2.97 3 5.19 3s4.15-1.21 5.19-3H20v-2h-2.09c.05-.33.09-.66.09-1v-1h2v-2h-2v-1c0-.34-.04-.67-.09-1H20V8zm-6 8h-4v-2h4v2zm0-4h-4v-2h4v2z" />
    </svg>
  );
}

const statusColor: Record<PluginStatus["level"], string> = {
  ok: "bg-[hsl(var(--lv-on))]",
  warn: "bg-[hsl(38_92%_50%)]",
  error: "bg-[hsl(var(--lv-off))]",
};

function useStatus(entry: LoadedPlugin): PluginStatus | null {
  const [status, setStatus] = React.useState<PluginStatus | null>(null);
  React.useEffect(() => {
    if (entry.kind !== "active" || !entry.plugin.status) return;
    let alive = true;
    const poll = async () => {
      try {
        const s = await entry.plugin.status!();
        if (alive) setStatus(s);
      } catch {
        if (alive) setStatus({ level: "error" });
      }
    };
    poll();
    const iv = setInterval(poll, 30_000);
    return () => {
      alive = false;
      clearInterval(iv);
    };
  }, [entry]);
  return status;
}

function PluginTab({ entry, locale }: { entry: LoadedPlugin; locale: Locale }) {
  const status = useStatus(entry);
  if (entry.kind === "active") {
    return (
      <NavLink
        to={`/p/${entry.plugin.id}`}
        className={({ isActive }) =>
          cn(
            "inline-flex items-center gap-1.5 rounded-md px-3 py-1 text-sm font-semibold transition-colors duration-200",
            isActive
              ? "bg-primary text-primary-foreground"
              : "text-muted-foreground hover:bg-muted hover:text-foreground"
          )
        }
      >
        {ls(locale, entry.plugin.title)}
        {status && (
          <span
            className={cn("inline-block h-2 w-2 rounded-full", statusColor[status.level])}
            title={status.text ? ls(locale, status.text) : status.level}
          />
        )}
      </NavLink>
    );
  }
  if (entry.kind === "dormant") {
    return (
      <span
        className="inline-flex cursor-default items-center rounded-md px-3 py-1 text-sm font-semibold text-muted-foreground opacity-50"
        title={`${t(locale, "dormant")}: ${entry.gate.all.join(" + ")}`}
      >
        {ls(locale, entry.title)}
      </span>
    );
  }
  return (
    <span
      className="inline-flex cursor-default items-center gap-1.5 rounded-md px-3 py-1 text-sm font-semibold text-[hsl(var(--lv-off))] opacity-70"
      title={entry.reason}
    >
      {entry.id}
      <span className="text-xs font-normal">({t(locale, "failed")})</span>
    </span>
  );
}

export interface TopBarProps {
  plugins: LoadedPlugin[];
  locale: Locale;
  onLocale: (l: Locale) => void;
  theme: Theme;
  onTheme: (t: Theme) => void;
}

export function TopBar({ plugins, locale, onLocale, theme, onTheme }: TopBarProps) {
  const report = useReportHook(plugins, locale);
  return (
    <TooltipProvider delayDuration={300}>
      <header className="flex h-14 shrink-0 items-center gap-3 border-b border-border bg-card px-4">
        {/* Horizontal lockup at the width of the function cluster on the right
           (owner ruling 2026-07-17, IMPL-7; stylebook §10). */}
        <Logo variant="horizontal" height={32} />
        <nav className="flex items-center gap-1">
          {plugins.map((p, i) => (
            <PluginTab key={p.kind === "active" ? p.plugin.id : `${p.kind}-${i}`} entry={p} locale={locale} />
          ))}
        </nav>
        <div className="flex-1" />
        <div className="flex items-center gap-1">
          <Button
            variant="ghost"
            size="sm"
            aria-label="RU/EN"
            onClick={() => onLocale(locale === "ru" ? "en" : "ru")}
            className="font-semibold uppercase"
          >
            {locale}
          </Button>
          <Button
            variant="ghost"
            size="icon"
            aria-label={t(locale, "theme")}
            onClick={() => onTheme(theme === "dark" ? "light" : "dark")}
          >
            <Icon icon={theme === "dark" ? Sun : Moon} size="button" />
          </Button>
          {/* reserved auth-guard slot (workbench.md §7) */}
          <span id="wb-auth-slot" />
          <Tooltip>
            <TooltipTrigger asChild>
              <button
                aria-label={t(locale, "report")}
                onClick={report.fire}
                disabled={!report.enabled}
                className={cn(
                  "inline-flex h-9 w-9 items-center justify-center rounded-md text-muted-foreground transition-colors duration-200",
                  report.enabled
                    ? "hover:text-[hsl(38_92%_50%)]"
                    : "cursor-default opacity-40"
                )}
              >
                <BugGlyph />
              </button>
            </TooltipTrigger>
            <TooltipContent>
              {report.enabled ? t(locale, "report") : t(locale, "reportNone")}
            </TooltipContent>
          </Tooltip>
        </div>
      </header>
    </TooltipProvider>
  );
}
