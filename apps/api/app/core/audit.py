from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _audit_file() -> Path:
    return _repo_root() / "data" / "elearning" / "audit_log_v1.jsonl"


def append_audit_event(
    *,
    action: str,
    resource_type: str,
    resource_id: str,
    actor_user_id: str,
    actor_role: str,
    trace_id: str,
    metadata: dict[str, Any] | None = None,
) -> None:
    record = {
        "timestamp": datetime.now(UTC).isoformat(),
        "action": action,
        "resourceType": resource_type,
        "resourceId": resource_id,
        "actor": {
            "userId": actor_user_id,
            "role": actor_role,
        },
        "traceId": trace_id,
        "metadata": metadata or {},
    }
    path = _audit_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")