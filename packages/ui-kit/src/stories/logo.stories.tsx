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

/* Mirrors the Workbench top bar: a logo region exactly as wide as the plugin-pages
   sidebar (shell: --wb-rail-w = 13rem), tabs flush with the content area. */
export const InChrome: Story = {
  render: () => (
    <div className="flex h-14 items-center rounded-xl border border-border bg-card">
      <div className="flex w-52 shrink-0 items-center px-4">
        <Logo variant="horizontal" height={32} />
      </div>
      <span className="ml-4 rounded-md bg-primary px-3 py-1 text-sm font-semibold text-primary-foreground">
        Демо
      </span>
      <div className="flex-1" />
      <span className="pr-4 text-sm font-semibold uppercase text-muted-foreground">ru</span>
    </div>
  ),
};
