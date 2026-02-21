# Docker-Testumgebung (kurz-, mittel- und langfristig)

## Ziel

Die Docker-Testumgebung ergänzt die lokalen Schnelltests um reproduzierbare Läufe in einer konsistenten Umgebung.

## Verfügbare Profile

- `live`: Komfortable Entwicklungsumgebung mit API + Frontend-Liveserver
- `test`: Reproduzierbare Qualitätsläufe (DoD, Backend, Security, Frontend)

Datei: `docker-compose.yml`

## Kurzfristig (sofort nutzbar)

### Live-Entwicklung starten

```bash
docker compose --profile live up --build
```

Ergebnis:
- API unter `http://localhost:8000`
- Frontend unter `http://localhost:5173`

### Testprofil komplett ausführen

```bash
docker compose --profile test up --build --abort-on-container-exit --exit-code-from web-tests
```

Hinweis:
- Für DoD/Backend-Tests kann alternativ `--exit-code-from api-tests` genutzt werden.

## Mittelfristig

- `test`-Profil in PR-Checks integrieren (gleiches Verhalten lokal + CI)
- Optionale Erweiterung um E2E-Service (z. B. Playwright)
- Parallele Teil-Läufe je Service (`api-tests`, `web-tests`, `api-security`, `docs-dod`)

## Langfristig

- Nightly-Läufe mit erweitertem Security-Scope
- Versionsfixierte Base-Images und regelmäßige Image-Refresh-Routine
- Trennung in `docker-compose.dev.yml` und `docker-compose.ci.yml` bei wachsender Komplexität

## Einzelservices gezielt ausführen

```bash
docker compose --profile test run --rm docs-dod
docker compose --profile test run --rm api-tests
docker compose --profile test run --rm api-security
docker compose --profile test run --rm web-tests
```

## Stoppen und Aufräumen

```bash
docker compose --profile live down
docker compose --profile test down
```
