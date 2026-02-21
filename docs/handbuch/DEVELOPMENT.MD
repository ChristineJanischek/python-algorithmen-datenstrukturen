# Entwicklung (Best Practices)

## Prinzipien
- Trennung von Backend, Frontend und Daten.
- Fachinhalte als Markdown/Struktogramm im Repository.
- Erweiterbarkeit über JSON-Kataloge.
- Operatorenliste ist stets verfügbar.

## Nächste Ausbaustufen
- Authentifizierung (Schüler/Lehrkräfte)
- Bewertungssystem mit Testfällen
- Persistente Speicherung von Lösungen
- Markdown-Rendering im Frontend

## Lauffähigkeit und erste Tests (Backend + Frontend)

### Backend
- Abhängigkeiten installieren: `cd apps/api && pip3 install -r requirements.txt`
- API starten: `uvicorn app.main:app --reload`
- Tests ausführen: `python -m unittest discover -s tests -p "test_*.py"`

### Frontend
- Abhängigkeiten installieren: `cd apps/web && npm install`
- Frontend starten: `npm run dev`
- Tests ausführen: `npm run test`
- Optionale Rollensteuerung (Plugin-Admin-Toggle):
	- `VITE_USER_ROLE=admin`
	- `VITE_USER_ID=dein-name`

## CI-Qualitätsprüfung (Backend + Frontend)

- Workflow: `.github/workflows/app-quality.yml`
- Läuft auf PR/Push bei Änderungen in `apps/api/**` oder `apps/web/**`
- Prüft automatisch:
	- Backend-Tests (`python -m unittest discover -s tests -p "test_*.py"`)
	- Frontend-Tests (`npm run test`)
	- Frontend-Build (`npm run build`)

## Docker-Profile für reproduzierbare Tests

- Datei: `docker-compose.yml`
- Profile:
	- `live` → API + Frontend-Liveserver
	- `test` → DoD-Check, Backend-Tests, Security-Scan, Frontend-Tests/Build

### Live starten

- `docker compose --profile live up --build`

### Testläufe in Containern

- `docker compose --profile test run --rm docs-dod`
- `docker compose --profile test run --rm api-tests`
- `docker compose --profile test run --rm api-security`
- `docker compose --profile test run --rm web-tests`

## Einheitliches API-Fehlerformat

Alle API-Fehler liefern das gleiche Schema:

- `code`
- `message`
- `details`
- `traceId`

Für `api/v1/pruefungen` ist dieses Schema zusätzlich in OpenAPI als Response-Modell dokumentiert.

## Aktueller Sicherungsstand (2026-02-21)

- Backup-Branch: `chore/docker-testumgebung-backup-2026-02-21`
- Backup-Tag: `v2026.02.21-docker-setup-backup`
- PR erstellen: `https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen/pull/new/chore/docker-testumgebung-backup-2026-02-21`
