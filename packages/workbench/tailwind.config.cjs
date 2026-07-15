module.exports = {
  presets: [require("locveil-ui-kit/preset")],
  content: [
    "./index.html",
    "./src/**/*.{ts,tsx}",
    "./node_modules/locveil-ui-kit/dist/**/*.js",
  ],
};
