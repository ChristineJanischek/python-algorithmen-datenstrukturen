from __future__ import annotations

from fastapi import Request
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .api import v1_router
from .core import (
    ForbiddenError,
    NotFoundError,
    TraceIdMiddleware,
    ValidationError,
    error_response_payload,
)
from .data_loader import load_json, load_text

app = FastAPI(title="Struktogramm E-Learning API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"] ,
)
app.add_middleware(TraceIdMiddleware)

app.include_router(v1_router, prefix="/api/v1")


def _trace_id(request: Request) -> str:
    return getattr(request.state, "trace_id", "unbekannt")


@app.exception_handler(NotFoundError)
async def not_found_handler(request: Request, exc: NotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content=error_response_payload(
            code="NOT_FOUND",
            message=exc.message,
            details=None,
            trace_id=_trace_id(request),
        ),
    )


@app.exception_handler(ValidationError)
async def validation_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content=error_response_payload(
            code="VALIDATION_ERROR",
            message=exc.message,
            details=None,
            trace_id=_trace_id(request),
        ),
    )


@app.exception_handler(ForbiddenError)
async def forbidden_handler(request: Request, exc: ForbiddenError) -> JSONResponse:
    return JSONResponse(
        status_code=403,
        content=error_response_payload(
            code="FORBIDDEN",
            message=exc.message,
            details=None,
            trace_id=_trace_id(request),
        ),
    )


@app.exception_handler(RequestValidationError)
async def request_validation_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content=error_response_payload(
            code="REQUEST_VALIDATION_ERROR",
            message="Ungültige Anfrageparameter.",
            details=exc.errors(),
            trace_id=_trace_id(request),
        ),
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    message = exc.detail if isinstance(exc.detail, str) else "HTTP-Fehler"
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response_payload(
            code=f"HTTP_{exc.status_code}",
            message=message,
            details=None if isinstance(exc.detail, str) else exc.detail,
            trace_id=_trace_id(request),
        ),
    )


@app.exception_handler(Exception)
async def fallback_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content=error_response_payload(
            code="INTERNAL_SERVER_ERROR",
            message="Ein unerwarteter Fehler ist aufgetreten.",
            details=str(exc),
            trace_id=_trace_id(request),
        ),
    )


@app.get("/api/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/api/themes")
def list_themes() -> list[dict]:
    return load_json("themes.json")


@app.get("/api/milestones")
def list_milestones() -> list[dict]:
    milestones = load_json("milestones.json")
    for milestone in milestones:
        content_path = milestone.get("contentPath")
        if content_path:
            milestone["content"] = load_text(content_path)
    return milestones


@app.get("/api/milestones/{milestone_id}")
def get_milestone(milestone_id: str) -> dict:
    milestones = load_json("milestones.json")
    for milestone in milestones:
        if milestone["id"] == milestone_id:
            content_path = milestone.get("contentPath")
            if content_path:
                milestone["content"] = load_text(content_path)
            return milestone
    raise HTTPException(status_code=404, detail="Milestone nicht gefunden")


@app.get("/api/tasks")
def list_tasks(milestone: str | None = None) -> list[dict]:
    tasks = load_json("tasks.json")
    if milestone:
        return [task for task in tasks if task.get("milestoneId") == milestone]
    return tasks


@app.get("/api/operatorenliste")
def get_operatorenliste() -> dict:
    milestones = load_json("milestones.json")
    if not milestones:
        raise HTTPException(status_code=404, detail="Operatorenliste nicht gefunden")
    operator_path = milestones[0].get("operatorListPath")
    if not operator_path:
        raise HTTPException(status_code=404, detail="Operatorenliste nicht gefunden")
    return {
        "path": operator_path,
        "content": load_text(operator_path),
    }
