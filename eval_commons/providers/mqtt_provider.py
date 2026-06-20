"""promptfoo Python provider: generic MQTT publish/subscribe assertion.

The reusable MQTT piece. Primary consumer is wb-mqtt-bridge (which talks MQTT directly);
wb-mqtt-voice only touches the retained `bridge/catalog/version` topic.

Flow: connect → (optionally) publish one message → wait for a message on the expected
topic → return the received payload. Either leg is optional, so this covers:
  - pub-only      : assert the publish succeeds.
  - sub-only      : assert a retained/expected message arrives (e.g. catalog version).
  - pub-then-sub  : actuate, then assert the resulting state/event is published.

promptfoo entrypoint:  call_api(prompt, options, context) -> {"output": str}

`config` : {
             host: "localhost", port: 1883,
             username: null, password: null,
             publish_topic: "...", publish_payload: "...",   # optional pub leg
             subscribe_topic: "...",                          # optional sub leg
             qos: 0, timeout_s: 5,
             return_mode: "payload" | "full",
           }
"""

from __future__ import annotations

import json
import threading
from typing import Any, Dict, Optional


def call_api(prompt: str, options: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    config = (options or {}).get("config", {}) or {}
    try:
        received = _run(prompt, config)
    except Exception as exc:
        return {"error": f"mqtt_provider failed: {type(exc).__name__}: {exc}"}

    if config.get("return_mode", "payload") == "full":
        return {"output": json.dumps(received, ensure_ascii=False)}
    return {"output": received.get("payload", "")}


def _run(prompt: str, config: Dict[str, Any]) -> Dict[str, Any]:
    import paho.mqtt.client as mqtt  # lazy import

    host = config.get("host", "localhost")
    port = int(config.get("port", 1883))
    qos = int(config.get("qos", 0))
    timeout = float(config.get("timeout_s", 5))
    subscribe_topic: Optional[str] = config.get("subscribe_topic")
    publish_topic: Optional[str] = config.get("publish_topic")
    # `prompt` may carry the payload when the YAML wires the test input as the message body.
    publish_payload = config.get("publish_payload", prompt if publish_topic else None)

    got = threading.Event()
    received: Dict[str, Any] = {"topic": None, "payload": None}

    client = mqtt.Client()
    if config.get("username"):
        client.username_pw_set(config["username"], config.get("password"))

    def on_message(_c, _u, message):
        received["topic"] = message.topic
        received["payload"] = message.payload.decode("utf-8", errors="replace")
        got.set()

    client.on_message = on_message
    client.connect(host, port, keepalive=int(timeout) + 5)
    client.loop_start()
    try:
        if subscribe_topic:
            client.subscribe(subscribe_topic, qos=qos)
        if publish_topic and publish_payload is not None:
            client.publish(publish_topic, publish_payload, qos=qos).wait_for_publish()
        if subscribe_topic:
            if not got.wait(timeout=timeout):
                raise TimeoutError(f"no message on '{subscribe_topic}' within {timeout}s")
    finally:
        client.loop_stop()
        client.disconnect()

    return received
