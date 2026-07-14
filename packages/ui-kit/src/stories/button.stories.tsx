import type { Meta, StoryObj } from "@storybook/react";
import { Plus } from "lucide-react";
import { Button } from "../components/ui/button";
import { Icon } from "../components/ui/icon";

const meta: Meta<typeof Button> = {
  title: "Primitives/Button",
  component: Button,
};
export default meta;
type Story = StoryObj<typeof Button>;

export const Variants: Story = {
  render: () => (
    <div className="flex flex-wrap items-center gap-3">
      <Button>Сохранить</Button>
      <Button variant="secondary">Проверить</Button>
      <Button variant="outline">Отмена</Button>
      <Button variant="ghost">Журнал</Button>
      <Button variant="destructive">Удалить</Button>
      <Button variant="link">Подробнее</Button>
      <Button size="icon" aria-label="Добавить">
        <Icon icon={Plus} size="button" />
      </Button>
      <Button disabled>Недоступно</Button>
    </div>
  ),
};
