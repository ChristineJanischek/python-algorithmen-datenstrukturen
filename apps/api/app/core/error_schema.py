from __future__ import annotations

from typing import Any


def error_response_payload(
    *,
    code: str,
    message: str,
    trace_id: str,
    details: Any | None = None,
) -> dict[str, Any]:
    return {
        "code": code,
        "message": message,
        "details": details,
        "traceId": trace_id,
    }