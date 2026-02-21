# Entwicklungsschritte (CHANGELOG)

## [Unreleased]
### Hinzugefügt:
- `Meilenstein-Plan` erstellt.
- Erster Entwurf der `README.md` Links zu Plan und Logs.
- Grundlage für automatisierte Protokollierung entwickelt.
- BW-konforme SVG-Struktogramme für Aufgabe 4c ergänzt:
	- `L2_4c1_Aufgabe4_Array_Verdoppeln_Neue_Liste` (XML + SVG)
	- `L2_4c2_Aufgabe4_Array_Verdoppeln_Original` (XML + SVG)
- `docs/pruefungen/Klausur_L2_2_1_Musterloesungen.md` vollständig von Monospace/ASCII-Struktogrammen auf SVG-Einbindungen umgestellt.
- `docs/pruefungen/archiv/Klausur_L2_2_1_Musterloesungen_2026-02-20_MILESTONE_KOPIE.md` auf denselben Stand vereinheitlicht.
- Lokale Notenfelder/Bewertungsmaßstab-Abschnitte in den betroffenen Lösungs-/Prüfungsdateien entfernt (Verweis auf allgemein gültigen BW-Maßstab).
- API-v1-Grundgerüst mit modularem Aufbau (`core`, `modules`, `api/v1`) eingeführt.
- Einheitliches API-Fehlerformat (`code`, `message`, `details`, `traceId`) + TraceId-Middleware umgesetzt.
- RBAC-Basis (`X-Role`, `X-User-Id`) und Audit-Logging (`audit_log_v1.jsonl`) produktiv ergänzt.
- Plugin-Registry eingeführt (`plugins_v1.json`) mit Endpunkten:
	- `GET /api/v1/plugins`
	- `GET /api/v1/plugins/{plugin_id}`
	- `PATCH /api/v1/plugins/{plugin_id}/activation` (admin)
	- Filterung über `?enabled=true|false`
- Frontend um Plugin-Statusansicht und Admin-Aktivierungstoggle erweitert.
- Qualitätsworkflow für Apps ergänzt: `.github/workflows/app-quality.yml`
	- Backend-Tests
	- Frontend-Tests
	- Frontend-Build
- M0-Statusdashboard ergänzt: `docs/milestones/M0_STATUS_DASHBOARD_2026-02-21.MD`.
- Docker-Testumgebung ergänzt:
	- `apps/api/Dockerfile`
	- `apps/web/Dockerfile`
	- `docker-compose.yml` mit Profilen `live` und `test`
	- `docs/handbuch/DOCKER_TESTUMGEBUNG.MD`

### Nächste Schritte:
- Planung der direkten Aufgabenintegration.