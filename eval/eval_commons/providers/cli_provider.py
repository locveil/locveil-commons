"""promptfoo Python provider: drive a single-shot subprocess CLI and assert on its output.

Both locveil-voice and locveil-bridge ship their main test surface as `argparse` console
scripts (irene-config-validate, irene-build-analyze, wb-openapi, broadlink-cli --convert,
device-test <id> <command>, ...). They take argv in and emit stdout/stderr, a JSON blob
(with --json), and a meaningful exit code (0/1/2). None of promptfoo's built-in providers
spawn a local process, so this shared provider does it once for every project.

Scope: deterministic, single-shot invocations (argv → output → exit). Interactive REPLs
(irene-cli, device-test interactive mode) and long-running services (servers, mqtt-sniffer)
are NOT this provider's job — the former is a later scripted-stdin extension, the latter is
already covered by the WS/MQTT/HTTP transport providers and smoke tests.

promptfoo entrypoint:  call_api(prompt, options, context) -> {"output": str}

`prompt`  : used as the command line (shlex-split) when `config.argv` is not given;
            ignored when `config.argv` is present.
`config`  : {
              argv:        ["irene-config-validate", "--config-file", "{{cfg}}", "--json"],
                           # list form — preferred, no shell, each arg passed verbatim.
              cwd:         "../locveil-voice",   # run console scripts / `python -m` from here
              env:         {KEY: "val"},          # merged onto the inherited environment
              stdin:       "y\n",                 # optional fixed stdin (still single-shot)
              timeout_s:   30,
              return_mode: "full" | "stdout" | "stderr" | "json" | "exit_code",
            }

`return_mode` mirrors the §4 pattern so one provider serves both deterministic checks and
the UX judge (e.g. llm-rubric over a tool's human-facing --help text):

  full (default) : JSON {stdout, stderr, exit_code, duration_ms}  — multi-field assertions
  stdout         : stdout only                                    — contains / regex / rubric
  stderr         : stderr only                                    — error-message assertions
  json           : stdout parsed & re-emitted (fails if not JSON) — is-json / JSON-path
  exit_code      : the exit code as a string                      — equals "0" / "2"
"""

from __future__ import annotations

import json
import shlex
import subprocess
import time
from typing import Any, Dict, List


def call_api(prompt: str, options: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    config = (options or {}).get("config", {}) or {}
    try:
        result = _run(prompt, config)
    except Exception as exc:  # surface spawn/timeout failures as a provider error, not a crash
        return {"error": f"cli_provider failed: {type(exc).__name__}: {exc}"}

    return_mode = config.get("return_mode", "full")
    if return_mode == "stdout":
        return {"output": result["stdout"]}
    if return_mode == "stderr":
        return {"output": result["stderr"]}
    if return_mode == "exit_code":
        return {"output": str(result["exit_code"])}
    if return_mode == "json":
        try:
            parsed = json.loads(result["stdout"])
        except json.JSONDecodeError as exc:
            return {"error": f"cli_provider: stdout is not valid JSON: {exc}; got {result['stdout']!r:.200}"}
        return {"output": json.dumps(parsed, ensure_ascii=False)}
    return {"output": json.dumps(result, ensure_ascii=False)}


def _run(prompt: str, config: Dict[str, Any]) -> Dict[str, Any]:
    argv: List[str] = config.get("argv") or shlex.split(prompt or "")
    if not argv:
        raise ValueError("no command: set config.argv (list) or pass the command as the prompt")

    env = None
    if config.get("env"):
        import os

        env = {**os.environ, **{k: str(v) for k, v in config["env"].items()}}

    timeout = float(config.get("timeout_s", 30))
    started = time.monotonic()
    # No shell=True: argv is passed verbatim, so test inputs can't inject shell metacharacters.
    completed = subprocess.run(
        argv,
        cwd=config.get("cwd"),
        env=env,
        input=config.get("stdin"),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return {
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "exit_code": completed.returncode,
        "duration_ms": round((time.monotonic() - started) * 1000, 1),
    }
