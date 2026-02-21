# Technische Umsetzungsvorlage – Prüfungsmodul

Stand: 2026-02-21
Status: Vorlage für M0 (verbindliche Zielstruktur)

## Ziel

Diese Vorlage definiert die **verbindliche Ordnungsstruktur** für Backend, Frontend, Daten, Prozesse und Dokumentation des Prüfungsmoduls.

Leitlinien:

- klare Verantwortlichkeiten
- keine Redundanzen
- maximale Automatisierung administrativer Abläufe
- Security und Nachvollziehbarkeit ab Start

---

## 1) Zielbild der Code-Organisation

## 1.1 Backend (`apps/api/app`)

```text
app/
├── main.py
├── core/
│   ├── config.py
│   ├── security.py
│   ├── logging.py
│   ├── errors.py
│   └── permissions.py
├── modules/
│   ├── pruefungen/
│   │   ├── router.py
│   │   ├── service.py
│   │   ├── repository.py
│   │   ├── schemas.py
│   │   └── validators.py
│   ├── aufgaben/
│   ├── bewertung/
│   ├── loesungen/
│   ├── export/
│   └── lms/
├── jobs/
│   ├── queue.py
│   ├── export_jobs.py
│   └── ai_jobs.py
└── tests/
```

Regel:

- `router.py` enthält nur HTTP-Anbindung.
- Fachlogik liegt ausschließlich in `service.py`.
- Persistenzzugriff nur in `repository.py`.

## 1.2 Frontend (`apps/web/src`)

```text
src/
├── app/
├── pages/
├── widgets/
├── features/
│   ├── pruefung-erstellen/
│   ├── aufgabe-bearbeiten/
│   ├── aufgabe-tauschen/
│   ├── niveau-konfigurieren/
│   ├── loesung-generieren/
│   └── exportieren/
├── entities/
│   ├── pruefung/
│   ├── aufgabe/
│   └── erwartungshorizont/
├── shared/
│   ├── api/
│   ├── ui/
│   ├── config/
│   └── utils/
└── tests/
```

Regel:

- Keine API-Aufrufe in `pages/` oder UI-Komponenten.
- Alle API-Zugriffe über `shared/api`.
- Domänenlogik nicht in UI-Hilfsfunktionen verstecken.

---

## 2) Single-Source-of-Truth (Redundanzvermeidung)

## 2.1 Kanonische Quellen

- Prüfungsmetadaten: zentrale strukturierte Prüfungsspeicher (JSON/DB)
- Aufgabeninhalte: Aufgabenmodul + versionierte Snapshots
- Lösungsinhalte: Lösungsmodul (generiert + reviewed)
- Exportdateien (`.docx`, `.pdf`, `.html`, `.xml`): **abgeleitete Artefakte**, niemals Primärquelle

## 2.2 Verbotene Muster

- Gleiche Regel in mehreren Validatoren ohne gemeinsamen Shared-Validator
- Direktes Kopieren von Logik zwischen Frontend und Backend
- Manuelles Nachpflegen von Exportdateien als „Wahrheit"

## 2.3 Pflichtmuster

- Gemeinsame Schemas pro Domäne
- Versionierte Änderungen über definierte Status (`draft`, `review`, `freigegeben`, `archiviert`)
- Reproduzierbare Generierung (gleicher Input -> gleicher Output)

---

## 3) API- und Vertragsstandards

- Prefix: `/api/v1/...`
- Contract-first mit OpenAPI
- Einheitliches Fehlerformat (`code`, `message`, `details`, `traceId`)
- Pagination-/Filterkonzept für Listenendpunkte
- Idempotenz-Key für Generierungs- und Exportendpunkte

Pflichtendpunkte (MVP):

- `POST /api/v1/pruefungen`
- `GET /api/v1/pruefungen/{id}`
- `PATCH /api/v1/pruefungen/{id}`
- `POST /api/v1/pruefungen/{id}/aufgaben:swap`
- `POST /api/v1/pruefungen/{id}/loesungen:generate`
- `POST /api/v1/pruefungen/{id}/export`

---

## 4) Sicherheits- und Compliance-Basis

- OIDC/OAuth2 oder JWT mit kurzer Lebensdauer
- RBAC (Autor, Review, Freigabe, Admin)
- Audit-Log für alle inhaltlichen Änderungen
- Pflichtvalidierung vor Freigabe:
  - BW-Operatorenliste
  - Erwartungshorizont vollständig
  - Verteilungsschlüssel konsistent
- Secrets niemals im Repository
- Dependency-Scans in CI verpflichtend

---

## 5) Automatisierung bürokratischer und administrativer Prozesse

## 5.1 Pflicht-Automationen in CI/CD

1. Lint + Type Checks
2. Unit- + Integrations-Tests
3. Security-Scan (Python/Node)
4. OpenAPI-Diff-Check (Breaking Changes blockieren)
5. Dokumentations-Check (Pflichtdokumente vorhanden)
6. Export-Regressionstest auf Referenzprüfung

## 5.2 Prozessautomationen

- Automatische Erstellung von Prüfungs-Snapshots bei Statuswechsel `freigegeben`
- Automatische Aktualisierung von Indizes/Übersichten
- Auto-Generierung von Änderungszusammenfassung für PRs
- Vorlagengetriebene Anlage neuer Aufgaben/Prüfungen (Scaffolding)
- Geplante Backups + Restore-Protokoll

## 5.3 Administrative Standard-Workflows

- Freigabeworkflow: `draft -> review -> freigegeben`
- 4-Augen-Prinzip für KI-generierte Inhalte
- Release-Checkliste als blockierender Gate

---

## 6) Dokumentations-Definition of Done

Ein Feature ist nur abgeschlossen, wenn alle Punkte erfüllt sind:

1. Fachspezifikation aktualisiert
2. API-Vertrag dokumentiert
3. Architekturentscheidung (ADR) hinterlegt
4. Testfälle + Abnahme dokumentiert
5. Betriebs-/Security-Auswirkung dokumentiert

Pfadkonvention:

- Architektur: `docs/handbuch/ARCHITECTURE.MD`
- Betrieb/Security/Backup: `docs/handbuch/BACKUP_STRATEGY.md`
- Meilensteine: `docs/milestones/`

---

## 7) Startpaket für M0 (konkret)

## Woche 1 – verbindlich

1. Ordnerstruktur gemäß Abschnitt 1 anlegen
2. API-`v1` Routing einführen
3. Rollenmodell + Audit-Log-Grundlage implementieren
4. OpenAPI- und Fehlerformat standardisieren
5. CI-Pipeline um Pflicht-Automationen erweitern

Abnahme:

- Ein kompletter End-to-End-Flow „Prüfung erstellen -> Aufgabe tauschen -> Lösung generieren -> Export auslösen“ läuft in Testumgebung.

---

## 8) Entscheidungsvorlage

Ja, die Richtung ist **sehr gut**.

Der größte Hebel für Ordnung, Wartbarkeit und Automatisierung ist:

1. strikte Modulgrenzen,
2. ein einziger Daten-Wahrheitskern,
3. automatisierte Qualitäts- und Freigabegates.

Wenn diese drei Punkte früh umgesetzt werden, vermeidest du spätere Architektur-Schulden fast vollständig.
