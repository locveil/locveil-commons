import type { Meta, StoryObj } from "@storybook/react";
import { Logo } from "../components/ui/logo";

const meta: Meta<typeof Logo> = {
  title: "Identity/Logo",
  component: Logo,
};
export default meta;
type Story = StoryObj<typeof Logo>;

export const Variants: Story = {
  render: () => (
    <div className="flex flex-col gap-8">
      <div className="flex items-center gap-10">
        <Logo />
        <Logo variant="stacked" />
      </div>
      <div className="flex items-end gap-10">
        <Logo variant="wordmark" height={40} />
        <Logo variant="mark" height={48} />
        <Logo variant="mark" />
        <Logo variant="mark-16" />
      </div>
    </div>
  ),
};

/* Mirrors the Workbench top bar (stylebook §10): horizontal lockup at the width of
   the function cluster on the right. */
export const InChrome: Story = {
  render: () => (
    <div className="flex h-14 items-center gap-3 rounded-xl border border-border bg-card px-4">
      <Logo variant="horizontal" height={32} />
      <div className="flex-1" />
      <span className="text-sm font-semibold uppercase text-muted-foreground">ru</span>
    </div>
  ),
};
