"""promptfoo Python provider: agent-as-human, multi-turn simulated user.

PHASE 1.5 STUB. Phase 1 uses promptfoo's built-in multi-turn conversation support
directly in YAML. Promote this provider only if persona depth proves insufficient — it
wraps DeepEval's ConversationSimulator (verified: role-plays a goal-driven user across
multi-turn dialogue) behind the same promptfoo Python-provider interface, so adopting it
is a change *here*, with no change to consuming projects.

Intended config:
    config: {
      persona:   "нетерпеливый пользователь, хочет поставить таймер на кухне",
      goal:      "успешно установить таймер на 10 минут",
      max_turns: 6,
      target:    { ws_url: "ws://localhost:6000/ws/audio", ... },  # how to reach the SUT
      judge:     file://../../locveil-commons/eval/shared/deepseek-judge.yaml,          # who scores the run
    }

Returns a transcript of the simulated conversation as `output`, which an `llm-rubric` /
`g-eval` assertion (DeepSeek judge) then scores against the goal.
"""

from __future__ import annotations

from typing import Any, Dict


def call_api(prompt: str, options: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    raise NotImplementedError(
        "sim_user_provider is a Phase 1.5 stub. Use promptfoo built-in multi-turn for now. "
        "To enable: `pip install deepeval`, wire DeepEval ConversationSimulator here, return "
        "the conversation transcript as {'output': <transcript>}. See ARCHITECTURE.md §6."
    )
