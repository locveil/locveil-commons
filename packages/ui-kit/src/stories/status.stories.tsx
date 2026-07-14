import type { Meta, StoryObj } from "@storybook/react";
import { StatusChip, StatusDot } from "../components/ui/status-chip";
import { Button } from "../components/ui/button";

const meta: Meta<typeof StatusChip> = {
  title: "Primitives/Status",
  component: StatusChip,
};
export default meta;
type Story = StoryObj<typeof StatusChip>;

/* The council's D8 ruling rendered: tested stays blue NEXT TO the blue accent —
   the pill shape carries the distinction. */
export const WorkflowChips: Story = {
  render: () => (
    <div className="flex flex-wrap items-center gap-2">
      <Button>Применить</Button>
      <StatusChip variant="pristine">исходно</StatusChip>
      <StatusChip variant="edited">изменено</StatusChip>
      <StatusChip variant="tested">проверено</StatusChip>
      <StatusChip variant="persisted">сохранено</StatusChip>
      <StatusChip variant="conflict">конфликт</StatusChip>
      <span className="ml-2 flex items-center gap-1.5 text-sm">
        <StatusDot on /> вкл
      </span>
      <span className="flex items-center gap-1.5 text-sm">
        <StatusDot on={false} /> выкл
      </span>
    </div>
  ),
};
