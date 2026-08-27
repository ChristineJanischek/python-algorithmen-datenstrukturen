"""Tests für das Hilfestufen-System (hint_levels.py)."""

import pytest

from learning_agent.learning.hint_levels import (
    STUFEN_BESCHREIBUNGEN,
    beschreibe_hilfestufe,
    ist_hoehere_stufe_sinnvoll,
)
from learning_agent.models import HintLevel, LearningContext


@pytest.fixture
def kontext() -> LearningContext:
    return LearningContext(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente hinzufügen",
        eingabe="Ich weiß nicht weiter.",
        hilfestufe=HintLevel.ORIENTIERUNG,
    )


def test_beschreibe_hilfestufe_alle_stufen() -> None:
    for stufe in HintLevel:
        beschreibung = beschreibe_hilfestufe(stufe)
        assert isinstance(beschreibung, str)
        assert len(beschreibung) > 0


def test_alle_stufen_haben_beschreibung() -> None:
    for stufe in HintLevel:
        assert stufe in STUFEN_BESCHREIBUNGEN


def test_ist_hoehere_stufe_sinnvoll_nach_zwei_versuchen(kontext: LearningContext) -> None:
    assert ist_hoehere_stufe_sinnvoll(kontext, anzahl_versuche=2) is True


def test_ist_hoehere_stufe_nicht_sinnvoll_bei_wenig_versuchen(kontext: LearningContext) -> None:
    assert ist_hoehere_stufe_sinnvoll(kontext, anzahl_versuche=1) is False


def test_ist_hoehere_stufe_nicht_sinnvoll_auf_hoechster_stufe() -> None:
    kontext_max = LearningContext(
        fachgebiet="Informatik",
        thema="Test",
        niveau="Einstieg",
        lernziel="Test",
        eingabe="Test",
        hilfestufe=HintLevel.ERKLAERUNG,
    )
    assert ist_hoehere_stufe_sinnvoll(kontext_max, anzahl_versuche=5) is False
