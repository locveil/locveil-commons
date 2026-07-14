import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "../../lib/utils";

const alertVariants = cva(
  "relative w-full rounded-md border px-3.5 py-2.5 text-sm [&>svg]:absolute [&>svg]:left-3.5 [&>svg]:top-3 [&>svg]:size-4 [&>svg+div]:pl-6",
  {
    variants: {
      variant: {
        default: "border-border bg-card text-card-foreground",
        accent: "border-primary text-primary bg-transparent",
        destructive:
          "border-[hsl(var(--lv-status-conflict)_45%_60%)] text-[hsl(var(--lv-status-conflict)_55%_38%)] dark:text-[hsl(var(--lv-status-conflict)_70%_72%)] dark:border-[hsl(var(--lv-status-conflict)_45%_45%_/_0.6)]",
      },
    },
    defaultVariants: { variant: "default" },
  }
);

export interface AlertProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof alertVariants> {}

const Alert = React.forwardRef<HTMLDivElement, AlertProps>(
  ({ className, variant, ...props }, ref) => (
    <div
      ref={ref}
      role="alert"
      className={cn(alertVariants({ variant }), className)}
      {...props}
    />
  )
);
Alert.displayName = "Alert";

const AlertTitle = React.forwardRef<HTMLHeadingElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h5 ref={ref} className={cn("mb-1 font-semibold leading-none", className)} {...props} />
  )
);
AlertTitle.displayName = "AlertTitle";

const AlertDescription = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("text-sm [&_p]:leading-relaxed", className)} {...props} />
  )
);
AlertDescription.displayName = "AlertDescription";

export { Alert, AlertTitle, AlertDescription };
