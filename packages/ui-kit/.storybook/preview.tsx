import React from "react";
import type { Preview } from "@storybook/react";
import "../tokens/locveil.css";
import "./storybook.css";

/* Theme toolbar: renders every story on both grounds the stylebook requires. */
const preview: Preview = {
  globalTypes: {
    theme: {
      description: "Locveil theme",
      toolbar: {
        title: "Theme",
        items: [
          { value: "light", title: "Светлая" },
          { value: "dark", title: "Тёмная" },
        ],
        dynamicTitle: true,
      },
    },
  },
  initialGlobals: { theme: "dark" },
  decorators: [
    (Story, ctx) => {
      const dark = ctx.globals.theme === "dark";
      return (
        <div
          className={dark ? "dark" : ""}
          style={{ margin: "-1rem", padding: "1.5rem", minHeight: "100vh" }}
        >
          <div className="bg-background text-foreground min-h-full p-6 font-sans">
            <Story />
          </div>
        </div>
      );
    },
  ],
};
export default preview;
