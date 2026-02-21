from __future__ import annotations

from fastapi import APIRouter, Depends, Request

from ...core import ActorContext, append_audit_event, require_roles
from .repository import PruefungenRepository
from .schemas import (
    ExportRequest,
    ExportResponse,
    GenerateLoesungRequest,
    LoesungGenerateResponse,
    PruefungCreateRequest,
    PruefungResponse,
    PruefungUpdateRequest,
    SwapAufgabenRequest,
)
from .service import PruefungenService

router = APIRouter()
service = PruefungenService(PruefungenRepository())


def _trace_id(request: Request) -> str:
    return getattr(request.state, "trace_id", "unbekannt")


@router.post("", response_model=PruefungResponse)
def create_pruefung(
    payload: PruefungCreateRequest,
    request: Request,
    actor: ActorContext = Depends(require_roles("autor", "admin")),
) -> PruefungResponse:
    result = service.create_pruefung(payload)
    append_audit_event(
        action="pruefung.create",
        resource_type="pruefung",
        resource_id=result.id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"status": result.status},
    )
    return result


@router.get("/{pruefung_id}", response_model=PruefungResponse)
def get_pruefung(
    pruefung_id: str,
    request: Request,
    actor: ActorContext = Depends(require_roles("autor", "review", "freigabe", "admin")),
) -> PruefungResponse:
    result = service.get_pruefung(pruefung_id)
    append_audit_event(
        action="pruefung.read",
        resource_type="pruefung",
        resource_id=pruefung_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={},
    )
    return result


@router.patch("/{pruefung_id}", response_model=PruefungResponse)
def update_pruefung(
    pruefung_id: str,
    payload: PruefungUpdateRequest,
    request: Request,
    actor: ActorContext = Depends(require_roles("autor", "review", "admin")),
) -> PruefungResponse:
    result = service.update_pruefung(pruefung_id, payload)
    append_audit_event(
        action="pruefung.update",
        resource_type="pruefung",
        resource_id=pruefung_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"version": result.version},
    )
    return result


@router.post("/{pruefung_id}/aufgaben:swap", response_model=PruefungResponse)
def swap_aufgaben(
    pruefung_id: str,
    payload: SwapAufgabenRequest,
    request: Request,
    actor: ActorContext = Depends(require_roles("autor", "review", "admin")),
) -> PruefungResponse:
    result = service.swap_aufgaben(pruefung_id, payload.index_a, payload.index_b)
    append_audit_event(
        action="pruefung.aufgaben.swap",
        resource_type="pruefung",
        resource_id=pruefung_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"index_a": payload.index_a, "index_b": payload.index_b},
    )
    return result


@router.post("/{pruefung_id}/loesungen:generate", response_model=LoesungGenerateResponse)
def generate_loesung(
    pruefung_id: str,
    payload: GenerateLoesungRequest,
    request: Request,
    actor: ActorContext = Depends(require_roles("review", "freigabe", "admin")),
) -> LoesungGenerateResponse:
    result = service.generate_loesung(pruefung_id, payload)
    append_audit_event(
        action="pruefung.loesung.generate",
        resource_type="pruefung",
        resource_id=pruefung_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"modus": payload.modus},
    )
    return result


@router.post("/{pruefung_id}/export", response_model=ExportResponse)
def export_pruefung(
    pruefung_id: str,
    payload: ExportRequest,
    request: Request,
    actor: ActorContext = Depends(require_roles("freigabe", "admin")),
) -> ExportResponse:
    result = service.export_pruefung(pruefung_id, payload)
    append_audit_event(
        action="pruefung.export",
        resource_type="pruefung",
        resource_id=pruefung_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"format": payload.format},
    )
    return result