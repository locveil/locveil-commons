import * as React from "react";
import {
  ActionBar,
  Alert,
  AlertDescription,
  Button,
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  Input,
  Label,
  StatusChip,
  toast,
} from "locveil-ui-kit";
import type { PageProps, WorkbenchPlugin } from "../../src/contract";

/* The demo plugin: proves runtime loading, singleton sharing (hooks work ⇒ one react),
   ui-kit via the import map, style injection, status slot, and the report hook. */

function DemoPage({ locale }: PageProps) {
  const [value, setValue] = React.useState("0.52");
  const ru = locale === "ru";
  return (
    <div className="demo-accent-frame max-w-md space-y-3 rounded-lg p-4">
      <Card>
        <CardHeader>
          <CardTitle>{ru ? "Демо-плагин" : "Demo plugin"}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="space-y-1">
            <Label htmlFor="demo-vad">{ru ? "Порог VAD" : "VAD threshold"}</Label>
            <Input
              id="demo-vad"
              value={value}
              onChange={(e) => setValue(e.target.value)}
              className="tabular-nums"
            />
          </div>
          <div className="flex items-center gap-2">
            <Button>{ru ? "Сохранить" : "Save"}</Button>
            <StatusChip variant="edited">{ru ? "изменено" : "edited"}</StatusChip>
          </div>
          <Alert variant="accent">
            <AlertDescription>
              {ru
                ? "Загружено динамически через import map — сборка оболочки не требовалась."
                : "Loaded at runtime through the import map — no shell rebuild involved."}
            </AlertDescription>
          </Alert>
        </CardContent>
      </Card>
      {/* IMPL-5 cross-bundle proof: this ActionBar renders in the SHELL's bottom slot
          through the kit's singleton bus; the toast crosses the same boundary. */}
      <ActionBar>
        <Button
          size="sm"
          onClick={() =>
            toast({
              title: ru ? "Применено" : "Applied",
              description: ru ? "Порог VAD обновлён." : "VAD threshold updated.",
            })
          }
        >
          {ru ? "Применить всё" : "Apply all"}
        </Button>
        <span className="text-xs text-muted-foreground">
          {ru ? "панель из плагина — слот оболочки" : "plugin bar — shell slot"}
        </span>
      </ActionBar>
    </div>
  );
}

function AboutPage({ locale }: PageProps) {
  return (
    <p className="max-w-md text-sm text-muted-foreground">
      {locale === "ru"
        ? "Вторая страница — проверяет боковую навигацию плагина."
        : "Second page — exercises the plugin sidebar navigation."}
    </p>
  );
}

const plugin: WorkbenchPlugin = {
  id: "demo",
  title: { ru: "Демо", en: "Demo" },
  pages: () => [
    { route: "main", title: { ru: "Главная", en: "Main" }, render: DemoPage },
    { route: "about", title: { ru: "О плагине", en: "About" }, render: AboutPage },
  ],
  status: () => ({ level: "ok", text: { ru: "работает", en: "running" } }),
  reportHook: (ctx) => {
    // a real plugin posts to its backend writer; the demo proves the delegation path
    window.alert(`report from plugin=${ctx.pluginId} route=${ctx.route} locale=${ctx.locale}`);
  },
};

export default plugin;
