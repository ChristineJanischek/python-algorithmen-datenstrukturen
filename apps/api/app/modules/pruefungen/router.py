from __future__ import annotations

from fastapi import APIRouter

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


@router.post("", response_model=PruefungResponse)
def create_pruefung(payload: PruefungCreateRequest) -> PruefungResponse:
    return service.create_pruefung(payload)


@router.get("/{pruefung_id}", response_model=PruefungResponse)
def get_pruefung(pruefung_id: str) -> PruefungResponse:
    return service.get_pruefung(pruefung_id)


@router.patch("/{pruefung_id}", response_model=PruefungResponse)
def update_pruefung(pruefung_id: str, payload: PruefungUpdateRequest) -> PruefungResponse:
    return service.update_pruefung(pruefung_id, payload)


@router.post("/{pruefung_id}/aufgaben:swap", response_model=PruefungResponse)
def swap_aufgaben(pruefung_id: str, payload: SwapAufgabenRequest) -> PruefungResponse:
    return service.swap_aufgaben(pruefung_id, payload.index_a, payload.index_b)


@router.post("/{pruefung_id}/loesungen:generate", response_model=LoesungGenerateResponse)
def generate_loesung(pruefung_id: str, payload: GenerateLoesungRequest) -> LoesungGenerateResponse:
    return service.generate_loesung(pruefung_id, payload)


@router.post("/{pruefung_id}/export", response_model=ExportResponse)
def export_pruefung(pruefung_id: str, payload: ExportRequest) -> ExportResponse:
    return service.export_pruefung(pruefung_id, payload)