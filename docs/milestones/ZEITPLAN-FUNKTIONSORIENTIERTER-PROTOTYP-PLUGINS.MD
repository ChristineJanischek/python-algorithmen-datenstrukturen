# Zeitplan – Funktionsorientierter Prototyp mit Plugin-Erweiterungen

Stand: 2026-02-21
Status: Umsetzungsplan (lauffähig von Anfang an)

## Ziel

Ein stabiler, gut strukturierter Prototyp, der **funktion für funktion** erweitert wird.
Dabei gelten:

- Core bleibt jederzeit lauffähig
- Erweiterungen erfolgen als Plugins
- Jeder Schritt ist testbar und dokumentiert

## Architekturmodell

- **Core:** API-Basis, Fehlerformat, TraceId, RBAC, Audit, Test-/Build-Pipeline
- **Plugin 1:** `pruefungsmodul`
- **Plugin 2:** `apps/drawio-extension`

---

## Zeitplan (8 Wochen, funktionsorientiert)

## Woche 1 – Stabiler Core-Start

- API-v1-Grundgerüst stabilisieren
- Einheitliches Fehlerobjekt + TraceId fixieren
- RBAC/Audit-Basis produktiv machen
- Backend- und Frontend-Smoke-Tests als Pflicht

**Ergebnis:** Core startet zuverlässig, Tests laufen lokal und in CI.

## Woche 2 – CI- und Qualitäts-Gates

- CI-Workflow für Backend/Frontend-Tests
- Frontend-Build als Gate
- Doku-DoD in den Workflow verankern

**Ergebnis:** Jede Änderung wird automatisch auf Lauffähigkeit geprüft.

## Woche 3 – Plugin-Rahmen definieren

- Plugin-Contract festlegen (Schnittstellen, Zuständigkeiten, Versionierung)
- Basis-Loader/Registry für Plugins dokumentieren
- Startzustand: Plugins optional aktivierbar

**Ergebnis:** Erweiterungen können modular angebunden werden.

## Woche 4 – Prüfungsmodul Plugin: MVP Funktion 1–2

- Funktion 1: Prüfung anlegen
- Funktion 2: Prüfung laden/aktualisieren
- Rollenprüfung + Audit je Aktion

**Ergebnis:** Erste echte Fachfunktion produktiv nutzbar.

## Woche 5 – Prüfungsmodul Plugin: MVP Funktion 3–4

- Funktion 3: Aufgaben tauschen/bearbeiten
- Funktion 4: Lösungsjob auslösen (Queue-Stub)
- API-Verträge und Tests erweitern

**Ergebnis:** Iteratives Arbeiten an Prüfungen möglich.

## Woche 6 – Draw.io Extension Plugin Integration

- Plugin-Schnittstellen zum Core abstimmen
- Export/Import-Pfade definieren (xml/svg)
- Smoke-Tests für Integration

**Ergebnis:** Draw.io-Features als separates Plugin nutzbar.

## Woche 7 – Export- und Betriebsstabilisierung

- Exportkette (`md` -> `html`/`pdf`/`docx`) absichern
- Regressionstests für Referenzdaten
- Snapshot/Versionierung bei Freigabe vorbereiten

**Ergebnis:** reproduzierbare Dokumentausgabe und stabile Betriebsprozesse.

## Woche 8 – Hardening + Pilot-Ready

- Sicherheits- und Restore-Checks nachziehen
- Performance-Basis-Metriken ergänzen
- Pilotdurchlauf mit Referenzprozess

**Ergebnis:** lauffähiger, testbarer Prototyp mit klarer Erweiterungsstrategie.

---

## Definition „lauffähig von Anfang an"

Ein Sprint gilt nur als abgeschlossen, wenn:

1. Starten funktioniert (`api` + `web`)
2. Smoke-Tests grün sind
3. Build erfolgreich ist
4. Dokumentation aktualisiert ist

---

## Reihenfolge für neue Funktionen (verbindlich)

1. Contract definieren
2. Minimalfunktion implementieren
3. Tests ergänzen
4. Doku aktualisieren
5. CI grün
6. Erst dann nächste Funktion

So bleibt das Repository jederzeit sauber, nachvollziehbar und erweiterbar.
