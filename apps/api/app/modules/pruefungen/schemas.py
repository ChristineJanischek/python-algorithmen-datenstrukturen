from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

PruefungsStatus = Literal["draft", "review", "freigegeben", "archiviert"]
ExportFormat = Literal["md", "docx", "pdf", "xml", "html"]


class AufgabeRef(BaseModel):
    aufgabe_id: str = Field(..., min_length=1)
    titel: str = Field(..., min_length=1)
    punkte: int = Field(..., ge=0)


class ABVerteilung(BaseModel):
    ab1: int = Field(..., ge=0, le=100)
    ab2: int = Field(..., ge=0, le=100)
    ab3: int = Field(..., ge=0, le=100)


class PruefungCreateRequest(BaseModel):
    titel: str = Field(..., min_length=3)
    jahrgangsstufe: str = Field(..., min_length=1)
    fach: str = Field(..., min_length=1)
    zeit_minuten: int = Field(..., gt=0)
    status: PruefungsStatus = "draft"
    anforderungsbereiche: ABVerteilung
    themen: list[str] = Field(default_factory=list)
    aufgaben: list[AufgabeRef] = Field(default_factory=list)


class PruefungUpdateRequest(BaseModel):
    titel: str | None = Field(default=None, min_length=3)
    jahrgangsstufe: str | None = Field(default=None, min_length=1)
    fach: str | None = Field(default=None, min_length=1)
    zeit_minuten: int | None = Field(default=None, gt=0)
    status: PruefungsStatus | None = None
    anforderungsbereiche: ABVerteilung | None = None
    themen: list[str] | None = None
    aufgaben: list[AufgabeRef] | None = None


class SwapAufgabenRequest(BaseModel):
    index_a: int = Field(..., ge=0)
    index_b: int = Field(..., ge=0)


class GenerateLoesungRequest(BaseModel):
    modus: Literal["bw-konform", "entwurf"] = "bw-konform"


class ExportRequest(BaseModel):
    format: ExportFormat


class LoesungGenerateResponse(BaseModel):
    pruefung_id: str
    status: Literal["queued", "done"]
    hinweis: str


class ExportResponse(BaseModel):
    pruefung_id: str
    format: ExportFormat
    status: Literal["queued", "done"]
    hinweis: str


class PruefungResponse(BaseModel):
    id: str
    titel: str
    jahrgangsstufe: str
    fach: str
    zeit_minuten: int
    status: PruefungsStatus
    anforderungsbereiche: ABVerteilung
    themen: list[str]
    aufgaben: list[AufgabeRef]
    version: int
    created_at: datetime
    updated_at: datetime