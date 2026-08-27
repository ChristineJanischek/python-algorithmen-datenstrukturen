# Aufgabe 05: Testabdeckung erweitern

**Typ:** Basisaufgabe  
**Schwierigkeit:** ⭐  
**Empfohlener Branch:** `feature/aufgabe-05-testing`

---

## Ausgangssituation

Der Lernagent hat grundlegende Tests für alle Module.
Die Testabdeckung ist aber noch nicht vollständig.
Einige Randfälle und Fehlerfälle werden noch nicht getestet.

## Lernziel

Du verstehst, warum automatische Tests wichtig sind,
und kannst eigene sinnvolle Testfälle schreiben.

## Fachlicher Hintergrund

**Unit-Tests** prüfen einzelne Funktionen in Isolation.
**pytest** ist das Standard-Testframework für Python.

Wichtige Konzepte:
- **Arrange:** Testdaten vorbereiten
- **Act:** Die Funktion aufrufen
- **Assert:** Das Ergebnis prüfen
- **Edge Cases:** Randfälle und Fehlersituationen testen

## Aufgabe

Ergänze fehlende Tests in den vorhandenen Testdateien.

### Pflichtaufgabe: Sicherheitstests

**Datei:** `tests/learning_agent/test_safety.py` (neu anlegen)

```python
"""Tests für die Sicherheitsüberprüfungen."""

from learning_agent.safety.input_check import EingabeFehler, pruefe_eingabe
from learning_agent.safety.output_check import pruefe_ausgabe

def test_leere_eingabe_wird_abgelehnt():
    # TODO: Implementiere den Test
    pass

def test_zu_lange_eingabe_wird_abgelehnt():
    # TODO: Implementiere den Test
    pass

def test_sensible_schluesselwoerter_werden_abgelehnt():
    # TODO: Teste mit "api_key", "password" usw.
    pass

def test_normale_eingabe_wird_akzeptiert():
    # TODO: Implementiere den Test
    pass

def test_ausgabe_wird_geprüft():
    # TODO: Teste pruefe_ausgabe mit leerem Text
    pass
```

### Standardaufgabe: Modell-Tests

**Datei:** `tests/learning_agent/test_models.py` (neu anlegen)

Schreibe Tests für die Datenmodelle in `models.py`:
- `LearningContext` mit verschiedenen Werten
- `AgentResponse` mit und ohne `naechste_aktion`
- `HintLevel`-Enum: alle drei Stufen vorhanden?
- `Message` mit allen `MessageRole`-Werten

## Betroffene Dateien

- `tests/learning_agent/test_safety.py` (neu anlegen)
- `tests/learning_agent/test_models.py` (neu anlegen)
- Optional: Ergänzungen in bestehenden Testdateien

## Akzeptanzkriterien

- [ ] `test_safety.py` mit mindestens 5 vollständigen Tests.
- [ ] `test_models.py` mit mindestens 5 vollständigen Tests.
- [ ] Alle Tests laufen durch: `pytest tests/` ohne Fehler.
- [ ] Kein Test verwendet `pass` ohne Implementierung.

## Tipps

```python
import pytest

# Test, der einen Fehler erwartet:
def test_fehler_wird_ausgeloest():
    with pytest.raises(EingabeFehler):
        pruefe_eingabe("")

# Parametrisierter Test:
@pytest.mark.parametrize("text", ["api_key=123", "password: secret"])
def test_sensible_eingaben(text):
    with pytest.raises(EingabeFehler):
        pruefe_eingabe(text)
```

## Reflexionsfragen

1. Was ist der Unterschied zwischen Unit-Tests und Integrationstests?
2. Was passiert, wenn Tests fehlen und jemand den Code ändert?
3. Wie könntest du testen, ob der Agent wirklich *didaktisch sinnvoll* antwortet?

## Optionale Erweiterung

Richte eine Testabdeckungsmessung ein:
```bash
pip install pytest-cov
pytest --cov=learning_agent tests/
```
Dokumentiere die gemessene Abdeckung in einem Kommentar oben in `test_safety.py`.

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
