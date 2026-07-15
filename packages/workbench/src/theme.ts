export type Theme = "light" | "dark";

const LS_KEY = "locveil.workbench.theme";

export function initialTheme(): Theme {
  try {
    const v = localStorage.getItem(LS_KEY);
    if (v === "light" || v === "dark") return v;
  } catch {
    /* private mode */
  }
  return window.matchMedia?.("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

export function applyTheme(t: Theme): void {
  document.documentElement.classList.toggle("dark", t === "dark");
  try {
    localStorage.setItem(LS_KEY, t);
  } catch {
    /* private mode */
  }
}
