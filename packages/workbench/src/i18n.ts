import type { Locale, LocalizedString } from "./contract";

/* Shell chrome strings — deliberately tiny; plugins own their own i18n (HK-11). */
const dict = {
  ru: {
    dormant: "ожидает",
    failed: "не загружен",
    noPlugins: "Плагины не настроены — проверьте workbench.config.json и запустите npm run serve.",
    noPages: "У плагина нет страниц.",
    report: "Сообщить о проблеме",
    reportNone: "Активный плагин не поддерживает отчёты",
    theme: "Тема",
  },
  en: {
    dormant: "pending",
    failed: "failed to load",
    noPlugins: "No plugins configured — check workbench.config.json and run npm run serve.",
    noPages: "This plugin has no pages.",
    report: "Report a problem",
    reportNone: "The active plugin does not support reports",
    theme: "Theme",
  },
} as const;

export type ShellKey = keyof (typeof dict)["ru"];

export function t(locale: Locale, key: ShellKey): string {
  return dict[locale][key];
}

export function ls(locale: Locale, s: LocalizedString): string {
  return typeof s === "string" ? s : s[locale];
}

const LS_KEY = "locveil.workbench.locale";

export function initialLocale(): Locale {
  try {
    const v = localStorage.getItem(LS_KEY);
    if (v === "ru" || v === "en") return v;
  } catch {
    /* private mode */
  }
  return "ru"; // Russian-first product
}

export function persistLocale(l: Locale): void {
  try {
    localStorage.setItem(LS_KEY, l);
  } catch {
    /* private mode */
  }
  document.documentElement.lang = l;
}
