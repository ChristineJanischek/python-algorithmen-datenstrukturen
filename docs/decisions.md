# Architektur-Entscheidungen

Dieses Dokument hält wichtige Entscheidungen während der Entwicklung fest.
Es erklärt, warum bestimmte Ansätze gewählt wurden.

---

## ADR-001: MockProvider als einziger Provider im MVP

**Datum:** 2024-01  
**Status:** Beschlossen

**Kontext:** Das MVP soll ohne API-Schlüssel und Internetverbindung funktionieren.
Ein echter LLM-Aufruf würde Kosten verursachen und Datenschutzfragen aufwerfen.

**Entscheidung:** Nur `MockProvider` wird implementiert.
Die `LLMProvider`-Protocol-Schnittstelle erlaubt spätere Erweiterungen.

**Konsequenz:** Antworten sind vorhersagbar und testbar, aber nicht generativ.

---

## ADR-002: Keine Datenbank im MVP

**Datum:** 2024-01  
**Status:** Beschlossen

**Kontext:** Eine Datenbank erhöht die Komplexität und erfordert Datenschutzmaßnahmen.
Im MVP werden keine Daten dauerhaft gespeichert.

**Entscheidung:** Kein ORM, keine SQL-Datenbank, kein Datenbankschema.

**Konsequenz:** Kein dauerhafter Lernstand. Spätere Erweiterung möglich.

---

## ADR-003: Kein Webframework im MVP

**Datum:** 2024-01  
**Status:** Beschlossen

**Kontext:** Ein Webframework (Flask, FastAPI) erhöht Abhängigkeiten und Komplexität.
Das MVP soll als Konsolenanwendung funktionieren.

**Entscheidung:** Nur `input()`/`print()` für die Interaktion.
FastAPI wird als dokumentierte Erweiterungsstelle vorgesehen.

---

## ADR-004: Deutsche Variablennamen erlaubt

**Datum:** 2024-01  
**Status:** Beschlossen

**Kontext:** Die Zielgruppe sind deutschsprachige Schüler.
Deutsche Bezeichner erhöhen die Lesbarkeit für sie.

**Entscheidung:** Deutsche Bezeichner in domänenspezifischen Modulen erlaubt.
Englisch bleibt Standard für generische Infrastruktur.

---

## ADR-005: dataclasses statt Pydantic

**Datum:** 2024-01  
**Status:** Beschlossen

**Kontext:** Pydantic bietet Validierung, ist aber eine externe Abhängigkeit.
Dataclasses sind in der Standardbibliothek enthalten.

**Entscheidung:** `dataclasses` für alle Modelle.
Validierung erfolgt manuell in `content/loader.py`.

---

## ADR-006: pytest als Testframework

**Datum:** 2024-01  
**Status:** Beschlossen

**Kontext:** pytest ist der Python-Standard, einfach zu lernen und gut dokumentiert.

**Entscheidung:** `pytest` für alle Tests. Kein unittest.

---

*Neue Entscheidungen werden an dieser Datei angehängt.*

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
