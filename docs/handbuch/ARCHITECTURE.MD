# Architekturleitbild (Backend + Frontend)

Stand: 2026-02-21

## Ziel

Das System soll für das Prüfungsmodul **langfristig erweiterbar, sicher und wartbar** sein.
Kernprinzip: schnelle MVP-Entwicklung ohne spätere Architektur-Sackgassen.

---

## 1) Architekturprinzipien

1. **Modularer Monolith zuerst, Services später bei Bedarf**
	- Fachlich getrennte Module, aber zunächst in einem Deployable.
	- Geringe Komplexität in Betrieb und Entwicklung.

2. **Domain-first statt UI-first**
	- Fachobjekte (Prüfung, Aufgabe, Erwartungshorizont, Bewertung) bestimmen API und UI.

3. **Erweiterung über stabile Schnittstellen**
	- Versionierte APIs (`/api/v1/...`), definierte Events, klare Export-Verträge.

4. **Security und Qualität als Default**
	- Validierung, Rechte, Audit und Tests sind fester Teil jedes Features.

5. **Dokumentation ist Teil des Produkts**
	- Kein Feature gilt als „fertig“ ohne aktualisierte technische und fachliche Doku.

---

## 2) Zielstruktur Backend (FastAPI)

Empfohlene Paketstruktur in `apps/api/app`:

```text
app/
├── main.py
├── core/                # Konfiguration, Security, Logging, Fehlerbehandlung
├── modules/
│   ├── pruefungen/      # Prüfungs-CRUD, Builder, Versionierung
│   ├── aufgaben/        # Pool, Varianten, KI-Workflows
│   ├── bewertung/       # Erwartungshorizont, Schlüssel, Rubrics
│   ├── loesungen/       # Generierung + BW-Validierung
│   ├── export/          # md/html/docx/pdf/xml Pipeline
│   └── lms/             # Einbettung/Connectoren
├── schemas/             # Pydantic Request/Response Modelle
├── repositories/        # Datenzugriff (Datei/DB)
├── services/            # Domänenlogik (Use Cases)
└── tests/
```

### Backend-Best-Practices

- **Hexagonale Trennung**: Router -> Service -> Repository.
- **Keine Fachlogik im Router**.
- **Transaktionsgrenzen** pro Use Case.
- **Idempotente Endpunkte** für Generierung/Export-Jobs.
- **Async-Job-Queue** für schwere Prozesse (PDF, KI, Batch-Exports).
- **OpenAPI als Vertragsquelle** für Frontend und Integrationen.

---

## 3) Zielstruktur Frontend (React/Vite)

Empfohlen: **Feature-Sliced Architecture** statt rein technischem Zuschnitt.

```text
apps/web/src/
├── app/                 # Routing, Provider, globale Guards
├── pages/               # Seitenkomposition
├── widgets/             # Zusammengesetzte UI-Bausteine
├── features/
│   ├── pruefung-erstellen/
│   ├── aufgabe-tauschen/
│   ├── niveau-konfigurieren/
│   ├── loesung-pruefen/
│   └── exportieren/
├── entities/            # Prüfung, Aufgabe, Erwartungshorizont
├── shared/              # UI-Kit, API-Client, Utilities
└── tests/
```

### Frontend-Best-Practices

- **API-Client zentral** (kein Direktzugriff in Komponenten).
- **Form-Schemas mit Validierung** (z. B. Zod/Yup).
- **Optimistic Updates nur bei sicheren Fällen**.
- **Feature Flags** für inkrementellen Rollout.
- **A11y und i18n** von Beginn an berücksichtigen.

---

## 4) Erweiterbarkeit (Plug-in-fähig)

Damit Backend und Frontend flexibel bleiben:

- Neue Aufgabentypen über **registrierte Typdefinitionen** (Renderer + Validator + Exporter).
- Exportformate über **Exporter-Interface** (`prepare`, `render`, `validate`).
- LMS-Integrationen über **Connector-Interface** (Push, Sync, Rückmeldung).
- KI-Provider abstrahieren (Provider-Schnittstelle statt Vendor-Lock-in).

---

## 5) Daten- und Versionsstrategie

- **Single Source of Truth:** strukturierte Prüfungsdaten + Markdown-Artefakte.
- **Versionierte Prüfungen:** Status `draft`, `review`, `freigegeben`, `archiviert`.
- **Immutable Snapshots** für jede freigegebene Version.
- **Diff-fähige Speicherung** für Aufgabenänderungen und Erwartungshorizont.

---

## 6) Sicherheit (Security-by-Design)

Siehe auch `BACKUP_STRATEGY.md` für Betriebssicherheit.

### Technische Mindestanforderungen

- Authentifizierung: OIDC/OAuth2 (mindestens JWT mit kurzer TTL)
- Autorisierung: Rollen + Rechte (RBAC), optional ABAC für feinere Regeln
- Input Validation: strikt serverseitig (Pydantic + Domänenvalidatoren)
- Output Encoding: XSS-Schutz für Rich-Text/Markdown
- Secrets Management: keine Secrets im Repository
- Audit Logging: wer hat was wann an Prüfung/ Lösung geändert
- Rate Limiting: Schutz gegen Missbrauch bei KI-/Export-Endpunkten
- Dependency Scans: automatisiert (Python + Node)

### Fachliche Sicherheit

- Pflicht-Review für KI-generierte Aufgaben/Lösungen vor Freigabe
- BW-Konformitätsprüfung vor Veröffentlichung
- Sperre von Veröffentlichungen bei fehlendem Erwartungshorizont

---

## 7) Qualität, Observability, Betrieb

- **Testpyramide**:
  - Unit-Tests für Services/Validatoren
  - Integrations-Tests für API + Exportpipeline
  - E2E-Tests für Kernflows (Prüfung bauen, exportieren, freigeben)
- **Observability**:
  - Strukturierte Logs (korrelierbar pro Request/Job)
  - Metriken (Latenz, Fehlerquote, Jobdauer)
  - Alerting auf Exportfehler, Validierungsfehler, Auth-Anomalien
- **CI/CD-Gates**:
  - Linting, Tests, Security-Checks, Build-Artefakt-Validierung

---

## 8) Dokumentationsstandard (vollständig)

Pflichtdokumente pro größerem Feature:

1. Fachspezifikation (Ziel, Regeln, Beispiele)
2. API-Vertrag (Request/Response, Fehlerfälle)
3. Architekturentscheidung (ADR: warum so, warum nicht anders)
4. Testkonzept und Abnahmekriterien
5. Betriebsaspekte (Monitoring, Backup-Auswirkung, Rollback)

Ohne diese 5 Punkte gilt ein Feature nicht als abgeschlossen.

---

## 9) Konkrete nächste Schritte

1. API auf `v1`-Namespace umstellen
2. Modulstruktur (`modules/*`) im Backend einführen
3. Frontend auf Feature-Slice umstellen
4. RBAC + Audit Log als Querschnittsfunktion implementieren
5. Export- und KI-Prozesse in Job-Queue auslagern
6. ADR-Template und Security-Checkliste verpflichtend machen
