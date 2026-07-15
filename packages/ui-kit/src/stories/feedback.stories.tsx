import * as React from "react";
import type { Meta, StoryObj } from "@storybook/react";
import { ActionBar, ActionBarHost } from "../components/ui/action-bar";
import { Button } from "../components/ui/button";
import { Toaster } from "../components/ui/toaster";
import { toast } from "../components/ui/use-toast";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "../components/ui/alert-dialog";

const meta: Meta = { title: "Primitives/Feedback (IMPL-4)" };
export default meta;

/* Toast replaces window.confirm/inline banners (stylebook §7); the module-scope bus
   is a singleton through the import map — the shell owns the one <Toaster>. */
export const Toasts: StoryObj = {
  render: () => (
    <div className="flex gap-2">
      <Button
        onClick={() =>
          toast({ title: "Сохранено", description: "Конфигурация применена." })
        }
      >
        Сохранить
      </Button>
      <Button
        variant="destructive"
        onClick={() =>
          toast({
            variant: "destructive",
            title: "Ошибка валидации",
            description: "Порог VAD должен быть в диапазоне 0–1.",
          })
        }
      >
        Ошибка
      </Button>
      <Toaster />
    </div>
  ),
};

/* IMPL-5: plugins render <ActionBar> anywhere in their tree; the shell renders the
   single <ActionBarHost/>. Toggle to see single-occupancy + unmount-clears. */
export const BottomActionBar: StoryObj = {
  render: function Story() {
    const [on, setOn] = React.useState(true);
    return (
      <div className="flex min-h-48 flex-col justify-between gap-4">
        <Button variant="outline" onClick={() => setOn((v) => !v)}>
          {on ? "Убрать панель" : "Показать панель"}
        </Button>
        {on && (
          <ActionBar>
            <Button>Сохранить</Button>
            <Button variant="outline">Проверить</Button>
            <span className="text-xs text-muted-foreground">3 изменения не применены</span>
          </ActionBar>
        )}
        <ActionBarHost />
      </div>
    );
  },
};

export const ConfirmDialog: StoryObj = {
  render: () => (
    <AlertDialog>
      <AlertDialogTrigger asChild>
        <Button variant="destructive">Удалить язык</Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Удалить язык «en»?</AlertDialogTitle>
          <AlertDialogDescription>
            Все шаблоны и локализации этого языка будут удалены. Действие необратимо.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Отмена</AlertDialogCancel>
          <AlertDialogAction>Удалить</AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  ),
};
