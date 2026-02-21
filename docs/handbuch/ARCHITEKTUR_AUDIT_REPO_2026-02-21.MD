# Architektur-Audit Repository (Stand 2026-02-21)

## Ziel des Audits

Prüfung, ob die aktuelle Repository-Architektur für das Prüfungsmodul langfristig geeignet ist, und Definition eines konkreten Anpassungspfads für:

- Ordnung und klare Verantwortlichkeiten
- Vermeidung von Redundanzen
- hohe Automatisierung administrativer Prozesse
- sichere, nachvollziehbare Betriebsfähigkeit

---

## 1) Kurzfazit

Das Repository hat eine starke fachliche Basis (BW-Standards, Struktogramm-Tooling, Content-Management), aber die technische Produktarchitektur für ein skalierbares Prüfungsmodul ist noch in der Übergangsphase.

**Bewertung:**

- Fachliche Reife: **hoch**
- Technische Modularität (Produkt): **mittel**
- Security-/Governance-Reife: **mittel-niedrig**
- CI/CD-Automatisierung (gesamt): **mittel-niedrig**

**Empfehlung:** Geplanter M0-Kurs ist richtig und sollte vor weiterem Feature-Ausbau konsequent umgesetzt werden.

---

## 2) Ist-Zustand (präzise)

## 2.1 Stärken

1. **Klare fachliche Leitplanken**
   - BW-Standards dokumentiert und durch Helper gestützt (`src/utils/struktogramm_*`, `elearning_manager.py`).

2. **Dokumentationskultur vorhanden**
   - Handbuch- und Milestone-Struktur ist etabliert.

3. **Technischer Einstieg in API-v1 bereits gestartet**
   - Neues Modulgerüst für Prüfungen ist angelegt (`apps/api/app/api/v1`, `modules/pruefungen`).

4. **Gute Basis für Content-Daten**
   - `data/elearning` als zentraler Einstiegspunkt für strukturierte Daten.

## 2.2 Haupt-Gaps

1. **Monorepo-Governance noch unvollständig**
   - Keine durchgängige Build-/Test-Orchestrierung über alle Apps.

2. **Frontend-Architektur noch komponentenzentriert statt featurezentriert**
   - API-Aufrufe liegen aktuell in `App.tsx`; Zielstruktur aus M0 noch nicht umgesetzt.

3. **CI fokussiert aktuell stark auf Struktogramm-Validierung**
   - Fehlende verpflichtende Gates für API-Tests, Security-Scans, OpenAPI-Drift, Doku-DoD.

4. **Security-Querschnitt noch nicht implementiert**
   - Rollenmodell, Audit-Logging, einheitliches Fehler-/Trace-Format fehlen in produktiver Implementierung.

5. **Betriebsautomatisierung unvollständig**
   - Export-/Lösungsjobs und Freigabeworkflow sind konzeptionell vorhanden, aber noch nicht als End-to-End-Prozess automatisiert.

---

## 3) Zielbild-Abgleich (Soll vs. Ist)

## Must (vor Feature-Skalierung)

1. API-v1 als Standard für neue Produktfunktionen
2. Einheitliches Fehlerformat + TraceId in API
3. Rollen-/Rechtebasis + Audit-Log
4. CI-Gates: Lint, Tests, Security, Doku-Vollständigkeit
5. Frontend-Schnittstellen über zentralen API-Client

## Should (kurz danach)

1. Job-Queue für Export/KI/Jobs
2. OpenAPI-Diff-Check als Breaking-Change-Schutz
3. Snapshot-Workflow bei `freigegeben`
4. Referenz-Regression für Exportformate

## Nice-to-have (nach Stabilisierung)

1. Vollständige Plug-in-Schnittstellen für Export/LMS/AI
2. Architektur-Metriken (Cycle Time, Defect Leakage, MTTR)
3. Template-Generatoren für neue Module/Features

---

## 4) Redundanzrisiken und Gegenmaßnahmen

## Risiko A: Doppelte Logik in Frontend und Backend

- **Gegenmaßnahme:** Alle Validierungsregeln serverseitig als Wahrheit; Frontend nur UX-nahe Vorprüfung.

## Risiko B: Exportdateien werden als Primärdaten missverstanden

- **Gegenmaßnahme:** Exportartefakte als abgeleitete Outputs markieren; Primärdaten strikt versionieren.

## Risiko C: Dokumentation driftet von Implementierung weg

- **Gegenmaßnahme:** Doku-DoD als CI-Blocker + PR-Checkliste.

---

## 5) Migrationspfad (geordnet, risikoarm)

## Phase 1 – Governance-Basis (1–2 Wochen)

1. API-v1-Konvention verbindlich durchsetzen
2. Fehlerformat + TraceId-Middleware einführen
3. RBAC-Skeleton + Audit-Events für Kernaktionen
4. CI-Minimum-Gates aufsetzen

## Phase 2 – Strukturhärtung (1–2 Wochen)

1. Frontend in Feature-Slice überführen
2. API-Service-/Repository-Trennung konsolidieren
3. Testpyramide für API-v1 (Unit + Integration)

## Phase 3 – Prozessautomatisierung (2 Wochen)

1. Export-/Lösungsjobs in Queue verschieben
2. Snapshot-Automation bei Statuswechsel `freigegeben`
3. Release-/Restore-Checks in Pipeline integrieren

---

## 6) Konkrete nächste technische Aufgaben (Backlog-ready)

1. `apps/api/app/core/` erweitern um:
   - `error_schema.py`, `trace.py`, `auth.py`, `rbac.py`
2. `apps/api/app/main.py`:
   - globale Exception-Handler auf einheitliches Fehlerobjekt umstellen
3. `apps/web/src`:
   - `shared/api/client.ts` einführen, direkte `fetch`-Aufrufe aus `App.tsx` entfernen
4. `.github/workflows/`:
   - neuer Workflow für API-Test + Security-Scan + Doku-Gates
5. `docs/handbuch/`:
   - ADR-Template ergänzen und verpflichtend referenzieren

---

## 7) Audit-Entscheidung

**Ja: Architektur zuerst anpassen ist die richtige Entscheidung.**

Für dein Ziel „von Anfang an Ordnung und optimale Voraussetzungen“ ist das der effizienteste Weg: erst Governance/Struktur/Automatisierung, danach Feature-Breite.

---

## 8) Referenzen

- `docs/handbuch/ARCHITECTURE.MD`
- `docs/handbuch/TECHNISCHE_UMSETZUNGSVORLAGE_PRUEFUNGEN.MD`
- `docs/handbuch/BACKUP_STRATEGY.md`
- `docs/milestones/MEILENSTEIN-M0-ARCHITEKTUR-GOVERNANCE-AUTOMATISIERUNG.MD`

---

## 9) Architekturergänzung: Funktionsorientierter Prototyp mit Plugin-Modell

Für das Repository wird ein **Core + Plugin**-Ansatz empfohlen, damit das System ab Start lauffähig bleibt und iterativ erweitert werden kann.

### 9.1 Core (stabiler Kern)

Der Core enthält nur die querschnittlichen Grundlagen:

- API-Start, Routing-Basis, Fehlerformat, TraceId
- RBAC + Audit-Basis
- Persistenzschnittstellen, Test- und Build-Basis
- CI-Gates und Dokumentationspflichten

### 9.2 Plugins (fachliche Erweiterungen)

Plugins liefern besondere Fachfunktionen, ohne den Core zu destabilisieren:

1. **Prüfungsmodul-Plugin**
   - Prüfungserstellung, Aufgabenverwaltung, Erwartungshorizont, Export

2. **Draw.io-Extension-Plugin**
   - Struktogramm-spezifische Visualisierung, Konverter/Validator, Editor-Integration

### 9.3 Funktionsorientierte Ausbau-Regel

Jede neue Funktion wird in kleinen Schritten geliefert:

1. Feature-Contract (Input/Output, Rollen, Fehler)
2. Minimal implementierter End-to-End-Flow
3. Tests + Doku + CI-Gates
4. Erst danach nächste Funktion

Dadurch bleibt das System zu jedem Zeitpunkt lauffähig und testfähig.
