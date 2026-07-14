import * as React from "react";
import type { LucideIcon } from "lucide-react";
import { cn } from "../../lib/utils";

/* Stylebook §5: the icon component owns sizing — 16px inline, 20px in buttons.
   No important-width/height overrides anywhere (banned pattern from the extraction).
   Workbench/chrome icons are lucide (split ruling); pass any LucideIcon in. */

export interface IconProps extends React.SVGAttributes<SVGSVGElement> {
  icon: LucideIcon;
  size?: "inline" | "button";
}

const px = { inline: 16, button: 20 } as const;

const Icon = React.forwardRef<SVGSVGElement, IconProps>(
  ({ icon: LucideCmp, size = "inline", className, ...props }, ref) => (
    <LucideCmp
      ref={ref}
      width={px[size]}
      height={px[size]}
      strokeWidth={2}
      className={cn("shrink-0", className)}
      aria-hidden={props["aria-label"] ? undefined : true}
      {...props}
    />
  )
);
Icon.displayName = "Icon";

export { Icon };
