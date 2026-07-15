import * as React from "react";

/* Module-scope toast bus. Because locveil-ui-kit is an HK-11 import-map SINGLETON,
   this store is one shared instance across the Workbench shell and every runtime-
   loaded plugin — plugins call toast(), the shell's single <Toaster> renders it.
   Standalone apps render their own <Toaster> and get the same behavior. */

export interface ToastOptions {
  title?: string;
  description?: string;
  variant?: "default" | "destructive";
  /** ms until auto-dismiss; default 5000 */
  duration?: number;
  action?: React.ReactNode;
}

export interface ToastItem extends ToastOptions {
  id: string;
  open: boolean;
}

const TOAST_LIMIT = 3;

let counter = 0;
let toasts: ToastItem[] = [];
const listeners = new Set<(items: ToastItem[]) => void>();

function emit() {
  for (const l of listeners) l(toasts);
}

export function toast(opts: ToastOptions): { id: string; dismiss: () => void } {
  const id = String(++counter);
  toasts = [{ ...opts, id, open: true }, ...toasts].slice(0, TOAST_LIMIT);
  emit();
  return { id, dismiss: () => dismissToast(id) };
}

export function dismissToast(id: string): void {
  toasts = toasts.map((t) => (t.id === id ? { ...t, open: false } : t));
  emit();
  // drop after the close animation settles
  setTimeout(() => {
    toasts = toasts.filter((t) => t.id !== id);
    emit();
  }, 300);
}

export function useToast(): { toasts: ToastItem[]; toast: typeof toast; dismiss: typeof dismissToast } {
  const [items, setItems] = React.useState<ToastItem[]>(toasts);
  React.useEffect(() => {
    listeners.add(setItems);
    return () => {
      listeners.delete(setItems);
    };
  }, []);
  return { toasts: items, toast, dismiss: dismissToast };
}
