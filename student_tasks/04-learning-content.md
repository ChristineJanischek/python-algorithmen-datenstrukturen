# Aufgabe 04: Lernmodul-Validierung

**Typ:** Basisaufgabe  
**Schwierigkeit:** ⭐⭐  
**Empfohlener Branch:** `feature/aufgabe-04-learning-content`

---

## Ausgangssituation

Der Content Loader lädt Lernmodule aus JSON-Dateien.
Er prüft nur, ob Pflichtfelder vorhanden sind, nicht ob die Inhalte sinnvoll sind.

Außerdem fehlt noch ein zweites Beispiel-Lernmodul.

## Lernziel

Du kannst JSON-Daten gegen ein Schema validieren und eigene Lernmodule erstellen.

## Fachlicher Hintergrund

**JSON-Schema** ist ein Standard zur Beschreibung und Validierung von JSON-Daten.
Es definiert:
- Welche Felder vorhanden sein müssen (required)
- Welche Datentypen erwartet werden
- Welche Werte erlaubt sind (enum)

Das Schema liegt unter `courses/schemas/learning-module.schema.json`.

## Aufgabe A: Validierungsfunktion

**Datei:** `src/learning_agent/content/loader.py`

Erweitere `_parse_modul` um eine inhaltliche Validierung:

```python
def _validiere_modul_inhalte(daten: dict) -> None:
    """Prüft, ob die Inhalte eines Lernmoduls sinnvoll sind.
    
    TODO: Implementiere Prüfungen:
    - id darf nicht leer sein und muss Klein-Buchstaben und Bindestriche enthalten
    - lernziele muss mindestens ein nicht-leeres Element enthalten
    - hinweise muss die Schlüssel "1", "2", "3" enthalten, alle nicht leer
    - niveau muss einer der erlaubten Werte sein: Einstieg, Grundkurs, Leistungskurs, Fortgeschritten
    
    Eingabe: daten (dict) – Rohdaten aus JSON
    Ausgabe: None (bei Fehler: ValueError mit verständlicher Meldung)
    """
    raise NotImplementedError("TODO: Aufgabe 04")
```

## Aufgabe B: Eigenes Lernmodul

Erstelle ein zweites Beispiel-Lernmodul unter:
`courses/examples/python-schleifen/module.json`

Das Modul soll das Thema **Python-Schleifen (for-Schleife)** behandeln.
Orientiere dich am vorhandenen Beispiel `courses/examples/python-lists/module.json`.

Erstelle auch passende `introduction.md` und `exercise.md`.

## Betroffene Dateien

- `src/learning_agent/content/loader.py` (erweitern)
- `tests/learning_agent/test_content_loader.py` (Tests hinzufügen)
- `courses/examples/python-schleifen/` (neues Verzeichnis mit drei Dateien)

## Akzeptanzkriterien

- [ ] `_validiere_modul_inhalte` ist vollständig implementiert.
- [ ] Ungültige Module werden mit verständlicher Fehlermeldung abgelehnt.
- [ ] Das neue Schleifenmodul entspricht dem JSON-Schema.
- [ ] Neue Tests bestehen.

## Reflexionsfragen

1. Warum ist eine Schema-Validierung wichtig, wenn Inhalte von Schülern erstellt werden?
2. Welche weiteren Felder würdest du dem Schema hinzufügen?
3. Wie könntest du das Modul-Format so gestalten, dass es auch für andere Fächer nutzbar ist?

## Optionale Erweiterung

Nutze die Python-Bibliothek `jsonschema`, um das Modul automatisch gegen das
offizielle JSON-Schema zu validieren. Dokumentiere die Installation in `docs/student-setup.md`.
