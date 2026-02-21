from __future__ import annotations

from ...core.errors import ValidationError
from .schemas import ABVerteilung


def validate_ab_verteilung(verteilung: ABVerteilung) -> None:
    gesamt = verteilung.ab1 + verteilung.ab2 + verteilung.ab3
    if gesamt != 100:
        raise ValidationError("Die Verteilung der Anforderungsbereiche muss 100 ergeben.")