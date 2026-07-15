import * as React from "react";
import { cn } from "../../lib/utils";

/* The bottom action-bar slot (IMPL-5) — the IMPL-4 pattern again: a module-scope bus
   in the kit (one shared instance through the HK-11 import-map singleton) + a host the
   SHELL renders in its bottom slot. Plugins render <ActionBar>…</ActionBar> anywhere in
   their page tree (no prop drilling); standalone apps render <ActionBarHost/> at their
   own layout bottom. `fixed bottom-0` in plugins is banned (stylebook §8) — this is
   the replacement. SINGLE-OCCUPANCY: the latest-mounted bar wins (dev warn on clash);
   unmount clears the slot. */

interface Entry {
  owner: number;
  node: React.ReactNode;
}

let current: Entry | null = null;
let ownerSeq = 0;
const listeners = new Set<(e: Entry | null) => void>();

function emit() {
  for (const l of listeners) l(current);
}

export function ActionBar({ children }: { children: React.ReactNode }) {
  const ownerRef = React.useRef(0);
  if (ownerRef.current === 0) ownerRef.current = ++ownerSeq;

  React.useEffect(() => {
    const owner = ownerRef.current;
    if (current && current.owner !== owner) {
      console.warn(
        "locveil-ui-kit <ActionBar>: replacing an existing action bar — the slot is single-occupancy (stylebook §8)."
      );
    }
    current = { owner, node: children };
    emit();
    return () => {
      if (current?.owner === owner) {
        current = null;
        emit();
      }
    };
  }, [children]);

  return null;
}

export function ActionBarHost({ className }: { className?: string }) {
  const [entry, setEntry] = React.useState<Entry | null>(current);
  React.useEffect(() => {
    listeners.add(setEntry);
    setEntry(current);
    return () => {
      listeners.delete(setEntry);
    };
  }, []);
  if (!entry) return null;
  return (
    <div
      id="wb-bottom-slot"
      className={cn(
        "flex shrink-0 items-center gap-2 border-t border-border bg-card px-4 py-2",
        className
      )}
    >
      {entry.node}
    </div>
  );
}
