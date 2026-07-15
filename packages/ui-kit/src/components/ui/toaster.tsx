import {
  Toast,
  ToastClose,
  ToastDescription,
  ToastProvider,
  ToastTitle,
  ToastViewport,
} from "./toast";
import { dismissToast, useToast } from "./use-toast";

/* The ONE toast viewport. In the Workbench the SHELL renders it (plugins only call
   toast() — the import-map singleton makes the bus shared); standalone apps render
   their own. */
export function Toaster() {
  const { toasts } = useToast();
  return (
    <ToastProvider>
      {toasts.map((t) => (
        <Toast
          key={t.id}
          variant={t.variant}
          open={t.open}
          duration={t.duration ?? 5000}
          onOpenChange={(open) => {
            if (!open) dismissToast(t.id);
          }}
        >
          <div className="grid gap-0.5">
            {t.title && <ToastTitle>{t.title}</ToastTitle>}
            {t.description && <ToastDescription>{t.description}</ToastDescription>}
          </div>
          {t.action}
          <ToastClose />
        </Toast>
      ))}
      <ToastViewport />
    </ToastProvider>
  );
}
