"""Tests für den Content Loader (content/loader.py)."""

import json
from pathlib import Path

import pytest

from learning_agent.content.loader import _parse_modul, lade_modul
from learning_agent.models import LearningModule


@pytest.fixture
def beispiel_modul_daten() -> dict:
    return {
        "id": "test-modul-001",
        "titel": "Test-Modul",
        "fachgebiet": "Informatik",
        "thema": "Python-Listen",
        "niveau": "Einstieg",
        "lernziele": ["Ziel 1"],
        "vorkenntnisse": ["Grundlagen Python"],
        "aufgabenstellung": "Ergänze die Liste.",
        "fehlvorstellungen": ["Listen sind unveränderbar"],
        "hinweise": {
            "1": "Was möchtest du tun?",
            "2": "Nutze append.",
            "3": "meine_liste.append(element)",
        },
        "reflexionsfrage": "Wann würdest du append verwenden?",
        "transferaufgabe": "Füge drei Zahlen zur Liste hinzu.",
    }


def test_parse_modul_gibt_learning_module_zurueck(beispiel_modul_daten: dict) -> None:
    modul = _parse_modul(beispiel_modul_daten)
    assert isinstance(modul, LearningModule)
    assert modul.id == "test-modul-001"
    assert modul.thema == "Python-Listen"


def test_parse_modul_hinweise_als_int_schluessel(beispiel_modul_daten: dict) -> None:
    modul = _parse_modul(beispiel_modul_daten)
    assert 1 in modul.hinweise
    assert 2 in modul.hinweise
    assert 3 in modul.hinweise


def test_parse_modul_fehlende_pflichtfelder_wirft_fehler() -> None:
    unvollstaendig = {"id": "test", "titel": "Test"}
    with pytest.raises(ValueError, match="Pflichtfelder fehlen"):
        _parse_modul(unvollstaendig)


def test_lade_modul_nicht_gefunden(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        lade_modul(tmp_path / "existiert_nicht.json")


def test_lade_modul_aus_datei(tmp_path: Path, beispiel_modul_daten: dict) -> None:
    datei = tmp_path / "modul.json"
    datei.write_text(json.dumps(beispiel_modul_daten), encoding="utf-8")
    modul = lade_modul(datei)
    assert modul.id == "test-modul-001"
