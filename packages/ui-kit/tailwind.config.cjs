/* Internal config — Storybook/dev only; consumers use tailwind-preset.cjs. */
module.exports = {
  presets: [require("./tailwind-preset.cjs")],
  content: ["./src/**/*.{ts,tsx}", "./.storybook/**/*.{ts,tsx}"],
};
