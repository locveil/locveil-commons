"""promptfoo Python provider: goal-driven UI interaction simulation.

PHASE 2 STUB. The UI-simulation surface. An LLM observes a rendered UI (DOM/screenshot)
and acts toward a goal via Playwright, then the *same* UX-judge machinery (llm-rubric +
DeepSeek) scores whether the goal was achieved. "Talks" (sim_user_provider) becomes
"clicks" — scoring is unchanged.

This slots into the existing shared-provider boundary, so adding UI tests touches no
existing project: a consuming project just adds YAML cases pointing here.

Intended config:
    config: {
      base_url:   "http://localhost:5173",
      goal:       "включить свет в детской через UI",
      persona:    "обычный пользователь",
      max_steps:  20,
      headless:   true,
      planner:    file://../../locveil-commons/eval/shared/deepseek-judge.yaml,   # model driving the agent
    }

Returns a step/action trace + final DOM state as `output` for the judge to score.
"""

from __future__ import annotations

from typing import Any, Dict


def call_api(prompt: str, options: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    raise NotImplementedError(
        "ui_provider is a Phase 2 stub. To enable: `pip install playwright` (+ `playwright "
        "install`), implement a goal-driven observe→act loop, and return the action trace "
        "as {'output': <trace>}. See ARCHITECTURE.md §6 (Phase 2)."
    )
