"""Mock locveil-bridge — the SUT-facing half of the device-command contract tests (TEST-18 B).

A tiny stdlib HTTP server that stands in for the real bridge during producer contract runs:

- ``GET /system/catalog``            → serves the PINNED golden catalog (the shared world both
                                       sides resolve against — `contracts/pins/catalog/catalog.golden.json`);
- ``POST /devices/{id}/canonical``   → records the command, answers the §5b success echo;
- ``POST /rooms/{id}/canonical``     → records the room-group command (VWB-23), answers a
                                       plausible per-member aggregate built from the catalog's
                                       `group_defaults`/group members;
- ``GET /devices/{id}/state``        → records a read, answers a static state (the PR-5 read
                                       flow's stand-in);
- ``GET /_captured?since=N``         → introspection for the test provider: everything captured
                                       after index N, already in the crossover-fixture `expect`
                                       vocabulary (kind: actuate | room-group | read);
- ``POST /_reset``                   → clears the capture log.

Run:  python -m eval_commons.mock_bridge --catalog contracts/pins/catalog/catalog.golden.json --port 8010
"""

from __future__ import annotations

import argparse
import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional

_DEVICE_RE = re.compile(r"^/devices/([^/]+)/canonical$")
_ROOM_RE = re.compile(r"^/rooms/([^/]+)/canonical$")
_STATE_RE = re.compile(r"^/devices/([^/]+)/state$")
_OPTIONS_RE = re.compile(r"^/devices/([^/]+)/options/([^/]+)$")

# Deterministic stand-ins for the parametric (driver-queried) option sets — the by_value
# sets come from the catalog itself (VWB-19 §11.2: options fall back to the table keys).
_PARAMETRIC_OPTIONS = {
    "inputs": ["hdmi1", "hdmi2", "av", "component"],
    "apps": ["YouTube", "Netflix", "Кинопоиск"],
}


class MockBridgeState:
    def __init__(self, catalog: Dict[str, Any]):
        self.catalog = catalog
        self.captured: List[Dict[str, Any]] = []
        self.lock = threading.Lock()
        self._devices = {d["id"]: d for d in catalog.get("devices", [])}
        self._rooms = {r["id"]: r for r in catalog.get("rooms", [])}

    def record(self, entry: Dict[str, Any]) -> None:
        with self.lock:
            self.captured.append(entry)

    def device_options(self, device_id: str, kind: str) -> Optional[List[str]]:
        """VWB-19: by_value selects answer their static value keys; parametric sets get
        the deterministic stand-in list; unknown device/kind -> None (404)."""
        device = self._devices.get(device_id)
        if device is None:
            return None
        for cap in device.get("capabilities") or []:
            for action in cap.get("actions") or []:
                for param in action.get("params") or []:
                    if param.get("options_from") == kind:
                        return list(_PARAMETRIC_OPTIONS.get(kind, []))
                    if kind == "inputs" and cap.get("name") == "input" and param.get("values"):
                        return [v["wire"] for v in param["values"]]
        return None

    def group_targets(self, room_id: str, group: str, scope: str) -> List[str]:
        """Which member(s) a room-group command lands on — mirrors the bridge's policy."""
        room = self._rooms.get(room_id, {})
        default = (room.get("group_defaults") or {}).get(group)
        members = [d["id"] for d in self._devices.values()
                   if d.get("room") == room_id
                   and any((c.get("group") == group) for c in d.get("capabilities") or [])]
        if scope != "all" and default:
            return [default]
        return members or ([default] if default else [])


class _Handler(BaseHTTPRequestHandler):
    state: MockBridgeState  # set by serve()

    def log_message(self, fmt, *args):  # quiet
        pass

    def _json(self, code: int, payload: Dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self) -> Dict[str, Any]:
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            return json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return {}

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/system/catalog":
            self._json(200, self.state.catalog)
            return
        match = _STATE_RE.match(path)
        if match:
            device_id = match.group(1)
            self.state.record({"kind": "read", "device_id": device_id})
            self._json(200, {"device_id": device_id,
                             "state": {"temperature": 23.5, "humidity": 41.0,
                                       "room_temperature": 23.5, "setpoint": 22.0,
                                       "level": 60}})  # level: brightness %, read by the
                             # relative-adjustment flow (F100/F101 expect 60±10)
            return
        match = _OPTIONS_RE.match(path)
        if match:
            options = self.state.device_options(match.group(1), match.group(2))
            if options is None:
                self._json(404, {"success": False, "detail": "no such option set"})
            else:
                self._json(200, {"success": True, "data": options})
            return
        if path == "/_captured":
            since = 0
            if "?" in self.path:
                query = self.path.split("?", 1)[1]
                for part in query.split("&"):
                    if part.startswith("since="):
                        since = int(part[6:] or 0)
            with self.state.lock:
                self._json(200, {"captured": self.state.captured[since:],
                                 "total": len(self.state.captured)})
            return
        self._json(404, {"detail": "not found"})

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        if path == "/_reset":
            with self.state.lock:
                self.state.captured.clear()
            self._json(200, {"ok": True})
            return

        body = self._read_body()
        match = _DEVICE_RE.match(path)
        if match:
            device_id = match.group(1)
            self.state.record({"kind": "actuate", "device_id": device_id,
                               "capability": body.get("capability"),
                               "action": body.get("action"),
                               "params": body.get("params")})
            self._json(200, {"success": True, "device_id": device_id,
                             "capability": body.get("capability"),
                             "action": body.get("action"),
                             "state": {body.get("capability", "power"): body.get("action")},
                             "error": None})
            return
        match = _ROOM_RE.match(path)
        if match:
            room_id = match.group(1)
            scope = body.get("scope", "auto")
            self.state.record({"kind": "room-group", "room_id": room_id,
                               "group": body.get("group"),
                               "action": body.get("action"),
                               "scope": scope})
            targets = self.state.group_targets(room_id, body.get("group", ""), scope)
            self._json(200, {"success": True, "room_id": room_id,
                             "group": body.get("group"), "action": body.get("action"),
                             "scope_applied": "default" if scope != "all" and len(targets) == 1
                             else "fan_out",
                             "results": [{"device_id": t, "status": "executed"}
                                         for t in targets],
                             "error": None})
            return
        self._json(404, {"detail": "not found"})


def serve(catalog_path: Path, port: int, host: str = "127.0.0.1") -> ThreadingHTTPServer:
    """Start the mock bridge (blocking via .serve_forever(); tests use a thread)."""
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    _Handler.state = MockBridgeState(catalog)
    server = ThreadingHTTPServer((host, port), _Handler)
    return server


def main() -> None:
    parser = argparse.ArgumentParser(description="Mock locveil-bridge for contract tests")
    parser.add_argument("--catalog", required=True, type=Path,
                        help="Path to the pinned catalog.golden.json")
    parser.add_argument("--port", type=int, default=8010)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    server = serve(args.catalog, args.port, args.host)
    print(f"mock bridge on http://{args.host}:{args.port} "
          f"(catalog {args.catalog}, version {_Handler.state.catalog.get('version')})")
    server.serve_forever()


if __name__ == "__main__":
    main()
