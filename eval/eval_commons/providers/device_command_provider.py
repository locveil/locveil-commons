"""promptfoo Python provider: utterance → the canonical command Irene actually emitted.

The producer half of the Irene↔bridge contract tests (locveil-voice TEST-18 Slice B,
`mqtt_integration.md` §14.3). Drives a RUNNING Irene over REST (`/execute/command`,
text-input first — isolates NLU → resolver → handler, no audio) while the SUT's
`[outputs.bridge]` points at the mock bridge (`eval_commons.mock_bridge`), then reads what
the mock captured. The output is a JSON envelope promptfoo assertions inspect:

    {"captured": [<fixture-expect-shaped command>, ...],
     "reply": {"text": ..., "success": ..., "intent_name": ..., "metadata": {...}}}

promptfoo entrypoint: call_api(prompt, options, context) -> {"output": str}

`prompt` : the utterance (RU/EN).
`config` : {
             execute_url: "http://localhost:6000/execute/command",
             capture_url: "http://localhost:8010/_captured",
             timeout_s:   30,
           }
`vars`   : room — the fixture's `context.room`, sent as the request's `room_alias`
           (empty/absent = no room context).
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Dict


def _get_json(url: str, timeout: float) -> Dict[str, Any]:
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _post_json(url: str, payload: Dict[str, Any], timeout: float) -> Dict[str, Any]:
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def call_api(prompt: str, options: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    config = (options or {}).get("config", {}) or {}
    execute_url = config.get("execute_url", "http://localhost:6000/execute/command")
    capture_url = config.get("capture_url", "http://localhost:8010/_captured")
    timeout = float(config.get("timeout_s", 30))
    room = ((context or {}).get("vars") or {}).get("room") or None

    try:
        before = _get_json(f"{capture_url}?since=0", timeout).get("total", 0)
        payload: Dict[str, Any] = {"command": prompt}
        if room:
            payload["room_alias"] = room
        reply = _post_json(execute_url, payload, timeout)
        after = _get_json(f"{capture_url}?since={before}", timeout)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:500]
        return {"error": f"HTTP {e.code} from {e.url}: {detail}"}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}

    envelope = {
        "captured": after.get("captured", []),
        "reply": {
            "text": reply.get("text"),
            "success": reply.get("success"),
            "intent_name": reply.get("intent_name"),
            "metadata": reply.get("metadata") or {},
        },
    }
    return {"output": json.dumps(envelope, ensure_ascii=False)}
