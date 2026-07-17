import * as React from "react";

/* Stylebook §10: the Locveil logo. Canonical assets live in packages/brand/ — this
   component is their token-wired rendition (accent = --primary, structure =
   --muted-foreground), so it follows the theme with no wiring on the consumer side.
   Path data must stay byte-equal to the brand SVGs; re-sync in the same change. */

const ACCENT = "hsl(var(--primary))";
const STRUCTURE = "hsl(var(--muted-foreground))";

const strokeProps = (stroke: string, strokeWidth: number) =>
  ({
    stroke,
    strokeWidth,
    fill: "none",
    strokeLinecap: "round",
    strokeLinejoin: "round",
  }) as const;

/* The mark on its native 24px grid (stroke-2). */
const MarkPaths = ({ simplified = false }: { simplified?: boolean }) => (
  <>
    <path {...strokeProps(STRUCTURE, 2)} d="M3 21V12L12 3L21 12V21Z" />
    {simplified ? (
      <>
        <path {...strokeProps(ACCENT, 2)} d="M7.5 15L12 10.5L16.5 15" />
        <circle fill={ACCENT} cx="12" cy="18" r="1.2" />
      </>
    ) : (
      <>
        <path {...strokeProps(ACCENT, 2)} d="M6.5 13.5L12 8L17.5 13.5" />
        <path {...strokeProps(ACCENT, 2)} d="M9 16L12 13L15 16" />
        <circle fill={ACCENT} cx="12" cy="18.5" r="1" />
      </>
    )}
  </>
);

/* The wordmark on its native grid (stroke-5, baseline at y=0). */
const WordmarkPaths = () => (
  <>
    <path {...strokeProps(STRUCTURE, 5)} d="M2.5 -58V0" />
    <path {...strokeProps(ACCENT, 5)} d="M41.2 -39.3A20 20 0 0 1 41.2 -0.7" />
    <path {...strokeProps(ACCENT, 5)} d="M30.8 -0.7A20 20 0 0 1 30.8 -39.3" />
    <circle fill={ACCENT} cx="36" cy="-20" r="4" />
    <path {...strokeProps(STRUCTURE, 5)} d="M100.5 -33A20 20 0 1 0 100.5 -7" />
    <path {...strokeProps(STRUCTURE, 5)} d="M116 -40L134 0L152 -40" />
    <path {...strokeProps(STRUCTURE, 5)} d="M162 -20H202" />
    <path {...strokeProps(STRUCTURE, 5)} d="M202 -20A20 20 0 1 0 196.1 -5.9" />
    <path {...strokeProps(STRUCTURE, 5)} d="M214.5 -40V0" />
    <circle fill={STRUCTURE} cx="214.5" cy="-52" r="3.5" />
    <path {...strokeProps(STRUCTURE, 5)} d="M230.5 -58V0" />
  </>
);

const VARIANTS = {
  mark: {
    viewBox: "0 0 24 24",
    width: 24,
    height: 24,
    body: <MarkPaths />,
  },
  "mark-16": {
    viewBox: "0 0 24 24",
    width: 16,
    height: 16,
    body: <MarkPaths simplified />,
  },
  wordmark: {
    viewBox: "0 0 238 63",
    width: 238,
    height: 63,
    body: (
      <g transform="translate(2.5 60.5)">
        <WordmarkPaths />
      </g>
    ),
  },
  horizontal: {
    viewBox: "0 0 209 54",
    width: 209,
    height: 54,
    body: (
      <g transform="translate(2.7 2.7)">
        <g transform="translate(-8 -8) scale(2.6667)">
          <MarkPaths />
        </g>
        <g transform="translate(60 48) scale(0.6207)">
          <WordmarkPaths />
        </g>
      </g>
    ),
  },
  stacked: {
    viewBox: "0 0 150 106",
    width: 150,
    height: 106,
    body: (
      <g transform="translate(2.7 2.7)">
        <g transform="translate(40.3 -8) scale(2.6667)">
          <MarkPaths />
        </g>
        <g transform="translate(0 100) scale(0.6207)">
          <WordmarkPaths />
        </g>
      </g>
    ),
  },
} as const;

export type LogoVariant = keyof typeof VARIANTS;

export interface LogoProps extends React.SVGAttributes<SVGSVGElement> {
  variant?: LogoVariant;
  /** Rendered height in px; width follows the variant's aspect. Natural size if omitted. */
  height?: number;
}

const Logo = React.forwardRef<SVGSVGElement, LogoProps>(
  ({ variant = "horizontal", height, ...props }, ref) => {
    const v = VARIANTS[variant];
    const h = height ?? v.height;
    const w = Math.round((h * v.width) / v.height);
    return (
      <svg
        ref={ref}
        xmlns="http://www.w3.org/2000/svg"
        viewBox={v.viewBox}
        width={w}
        height={h}
        role="img"
        aria-label={props["aria-label"] ?? "Locveil"}
        {...props}
      >
        <title>Locveil</title>
        {v.body}
      </svg>
    );
  }
);
Logo.displayName = "Logo";

export { Logo };
