import { createRoot } from "react-dom/client";
import "locveil-ui-kit/tokens.css";
import "./shell.css";
import { App } from "./App";
import { loadPlugins } from "./loader";

async function boot() {
  const plugins = await loadPlugins();
  const root = createRoot(document.getElementById("root")!);
  root.render(<App plugins={plugins} />);
}

void boot();
