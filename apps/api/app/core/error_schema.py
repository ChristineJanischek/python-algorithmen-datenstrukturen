from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    code: str
    message: str
    details: Any | None = None
    traceId: str


def error_response_payload(
    *,
    code: str,
    message: str,
    trace_id: str,
    details: Any | None = None,
) -> dict[str, Any]:
    return ErrorResponse(
        code=code,
        message=message,
        details=details,
        traceId=trace_id,
    ).model_dump()