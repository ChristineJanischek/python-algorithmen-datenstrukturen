from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from ...core.errors import NotFoundError, ValidationError
from .repository import PruefungenRepository
from .schemas import (
    ABVerteilung,
    ExportRequest,
    ExportResponse,
    GenerateLoesungRequest,
    LoesungGenerateResponse,
    PruefungCreateRequest,
    PruefungResponse,
    PruefungUpdateRequest,
)
from .validators import validate_ab_verteilung


class PruefungenService:
    def __init__(self, repository: PruefungenRepository) -> None:
        self.repository = repository

    def create_pruefung(self, payload: PruefungCreateRequest) -> PruefungResponse:
        validate_ab_verteilung(payload.anforderungsbereiche)
        now = datetime.now(UTC)
        pruefung = PruefungResponse(
            id=str(uuid4()),
            titel=payload.titel,
            jahrgangsstufe=payload.jahrgangsstufe,
            fach=payload.fach,
            zeit_minuten=payload.zeit_minuten,
            status=payload.status,
            anforderungsbereiche=payload.anforderungsbereiche,
            themen=payload.themen,
            aufgaben=payload.aufgaben,
            version=1,
            created_at=now,
            updated_at=now,
        )
        pruefungen = self.repository.load_all()
        pruefungen.append(pruefung.model_dump(mode="json"))
        self.repository.save_all(pruefungen)
        return pruefung

    def get_pruefung(self, pruefung_id: str) -> PruefungResponse:
        for item in self.repository.load_all():
            if item.get("id") == pruefung_id:
                return PruefungResponse.model_validate(item)
        raise NotFoundError("Prüfung nicht gefunden")

    def update_pruefung(self, pruefung_id: str, payload: PruefungUpdateRequest) -> PruefungResponse:
        pruefungen = self.repository.load_all()
        for index, item in enumerate(pruefungen):
            if item.get("id") != pruefung_id:
                continue

            existing = PruefungResponse.model_validate(item)
            update_data = payload.model_dump(exclude_none=True)

            if "anforderungsbereiche" in update_data:
                verteilung = ABVerteilung.model_validate(update_data["anforderungsbereiche"])
                validate_ab_verteilung(verteilung)

            updated_payload = existing.model_dump()
            updated_payload.update(update_data)
            updated_payload["version"] = existing.version + 1
            updated_payload["updated_at"] = datetime.now(UTC)

            updated = PruefungResponse.model_validate(updated_payload)
            pruefungen[index] = updated.model_dump(mode="json")
            self.repository.save_all(pruefungen)
            return updated

        raise NotFoundError("Prüfung nicht gefunden")

    def swap_aufgaben(self, pruefung_id: str, index_a: int, index_b: int) -> PruefungResponse:
        pruefung = self.get_pruefung(pruefung_id)
        aufgaben = list(pruefung.aufgaben)
        max_index = len(aufgaben) - 1
        if index_a > max_index or index_b > max_index:
            raise ValidationError("Aufgaben-Indizes außerhalb des gültigen Bereichs")

        aufgaben[index_a], aufgaben[index_b] = aufgaben[index_b], aufgaben[index_a]
        return self.update_pruefung(pruefung_id, PruefungUpdateRequest(aufgaben=aufgaben))

    def generate_loesung(
        self,
        pruefung_id: str,
        payload: GenerateLoesungRequest,
    ) -> LoesungGenerateResponse:
        _ = self.get_pruefung(pruefung_id)
        return LoesungGenerateResponse(
            pruefung_id=pruefung_id,
            status="queued",
            hinweis=f"Lösungsjob ({payload.modus}) wurde in die Queue eingestellt.",
        )

    def export_pruefung(self, pruefung_id: str, payload: ExportRequest) -> ExportResponse:
        _ = self.get_pruefung(pruefung_id)
        return ExportResponse(
            pruefung_id=pruefung_id,
            format=payload.format,
            status="queued",
            hinweis=f"Export im Format {payload.format} wurde in die Queue eingestellt.",
        )