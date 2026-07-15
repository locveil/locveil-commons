import * as React from "react";
import { cn } from "../../lib/utils";

/* Locveil status tokens (stylebook §2, council D8).
   Pill shape is the status-vs-interaction contract: tested is BLUE next to the blue
   accent BY OWNER RULING — the bordered pill keeps it from reading as a button.
   Recipes (tokens/locveil.json): light bg h/70%/96% · border h/45%/80% · text h/55%/32%;
   dark bg h/45%/22%/45% · border h/45%/45%/60% · text h/70%/72%.
   Hue numbers live in tokens/locveil.css as --lv-status-*. */

export type StatusVariant =
  | "pristine"
  | "edited"
  | "tested"
  | "persisted"
  | "conflict";

export interface StatusChipProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant: StatusVariant;
}

/* One fully-literal class string per variant: Tailwind's extractor only generates
   arbitrary-value utilities it can read WHOLE from the source/dist — a template
   literal here means no chip styles in any consumer (and the `${...}` pseudo-class
   it does extract breaks lightningcss minification downstream). */
const recipe: Record<StatusVariant, string> = {
  pristine:
    "bg-[hsl(var(--lv-status-pristine)_70%_96%)] border-[hsl(var(--lv-status-pristine)_45%_80%)] text-[hsl(var(--lv-status-pristine)_55%_32%)] dark:bg-[hsl(var(--lv-status-pristine)_45%_22%_/_0.45)] dark:border-[hsl(var(--lv-status-pristine)_45%_45%_/_0.6)] dark:text-[hsl(var(--lv-status-pristine)_70%_72%)]",
  edited:
    "bg-[hsl(var(--lv-status-edited)_70%_96%)] border-[hsl(var(--lv-status-edited)_45%_80%)] text-[hsl(var(--lv-status-edited)_55%_32%)] dark:bg-[hsl(var(--lv-status-edited)_45%_22%_/_0.45)] dark:border-[hsl(var(--lv-status-edited)_45%_45%_/_0.6)] dark:text-[hsl(var(--lv-status-edited)_70%_72%)]",
  tested:
    "bg-[hsl(var(--lv-status-tested)_70%_96%)] border-[hsl(var(--lv-status-tested)_45%_80%)] text-[hsl(var(--lv-status-tested)_55%_32%)] dark:bg-[hsl(var(--lv-status-tested)_45%_22%_/_0.45)] dark:border-[hsl(var(--lv-status-tested)_45%_45%_/_0.6)] dark:text-[hsl(var(--lv-status-tested)_70%_72%)]",
  persisted:
    "bg-[hsl(var(--lv-status-persisted)_70%_96%)] border-[hsl(var(--lv-status-persisted)_45%_80%)] text-[hsl(var(--lv-status-persisted)_55%_32%)] dark:bg-[hsl(var(--lv-status-persisted)_45%_22%_/_0.45)] dark:border-[hsl(var(--lv-status-persisted)_45%_45%_/_0.6)] dark:text-[hsl(var(--lv-status-persisted)_70%_72%)]",
  conflict:
    "bg-[hsl(var(--lv-status-conflict)_70%_96%)] border-[hsl(var(--lv-status-conflict)_45%_80%)] text-[hsl(var(--lv-status-conflict)_55%_32%)] dark:bg-[hsl(var(--lv-status-conflict)_45%_22%_/_0.45)] dark:border-[hsl(var(--lv-status-conflict)_45%_45%_/_0.6)] dark:text-[hsl(var(--lv-status-conflict)_70%_72%)]",
};

const StatusChip = React.forwardRef<HTMLSpanElement, StatusChipProps>(
  ({ className, variant, ...props }, ref) => (
    <span
      ref={ref}
      className={cn(
        "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold",
        recipe[variant],
        className
      )}
      {...props}
    />
  )
);
StatusChip.displayName = "StatusChip";

/* Device on/off dot (stylebook §2). */
export interface StatusDotProps extends React.HTMLAttributes<HTMLSpanElement> {
  on: boolean;
}

const StatusDot = React.forwardRef<HTMLSpanElement, StatusDotProps>(
  ({ className, on, ...props }, ref) => (
    <span
      ref={ref}
      aria-label={on ? "on" : "off"}
      className={cn(
        "inline-block h-2 w-2 rounded-full",
        on ? "bg-[hsl(var(--lv-on))]" : "bg-[hsl(var(--lv-off))]",
        className
      )}
      {...props}
    />
  )
);
StatusDot.displayName = "StatusDot";

export { StatusChip, StatusDot };
