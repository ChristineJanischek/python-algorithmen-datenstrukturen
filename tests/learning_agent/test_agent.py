"""Tests für den Lernagenten (agent.py)."""

import pytest

from learning_agent.agent import LearningAgent, _bestimme_antworttyp
from learning_agent.models import HintLevel, ResponseType
from learning_agent.providers.mock_provider import MockProvider


@pytest.fixture
def agent() -> LearningAgent:
    return LearningAgent(provider=MockProvider())


def test_verarbeite_gibt_antwort_zurueck(agent: LearningAgent) -> None:
    antwort = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente hinzufügen",
        eingabe="Ich weiß nicht, wie ich ein Element ergänzen kann.",
    )
    assert antwort.text
    assert isinstance(antwort.text, str)


def test_verarbeite_orientierungsstufe_ist_standard(agent: LearningAgent) -> None:
    antwort = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Schleifen",
        niveau="Einstieg",
        lernziel="For-Schleife verstehen",
        eingabe="Was ist eine Schleife?",
    )
    assert antwort.hilfestufe == HintLevel.ORIENTIERUNG
    assert antwort.antworttyp == ResponseType.FRAGE


def test_verarbeite_leere_eingabe_liefert_fehlermeldung(agent: LearningAgent) -> None:
    antwort = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Arrays",
        niveau="Fortgeschritten",
        lernziel="Sortierung verstehen",
        eingabe="",
    )
    assert antwort.antworttyp == ResponseType.FEHLERANALYSE
    assert antwort.text


def test_verarbeite_hilfestufe_hinweis(agent: LearningAgent) -> None:
    antwort = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente hinzufügen",
        eingabe="Ich weiß nicht, wie append funktioniert.",
        hilfestufe=HintLevel.HINWEIS,
    )
    assert antwort.hilfestufe == HintLevel.HINWEIS
    assert antwort.antworttyp == ResponseType.HINWEIS


def test_bestimme_antworttyp_mapping() -> None:
    assert _bestimme_antworttyp(HintLevel.ORIENTIERUNG) == ResponseType.FRAGE
    assert _bestimme_antworttyp(HintLevel.HINWEIS) == ResponseType.HINWEIS
    assert _bestimme_antworttyp(HintLevel.ERKLAERUNG) == ResponseType.ERKLAERUNG
