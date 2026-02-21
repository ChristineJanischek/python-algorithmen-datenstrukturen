# API

## Endpunkte
- GET /api/health
- GET /api/themes
- GET /api/milestones
- GET /api/milestones/{id}
- GET /api/tasks?milestone=ms1
- GET /api/operatorenliste

## API v1 (M0 – Prüfungsmodul)
- POST /api/v1/pruefungen
- GET /api/v1/pruefungen/{pruefung_id}
- PATCH /api/v1/pruefungen/{pruefung_id}
- POST /api/v1/pruefungen/{pruefung_id}/aufgaben:swap
- POST /api/v1/pruefungen/{pruefung_id}/loesungen:generate
- POST /api/v1/pruefungen/{pruefung_id}/export

## API v1 (Plugin-Registry)
- GET /api/v1/plugins
	- Optionaler Filter: `?enabled=true|false`
- GET /api/v1/plugins/{plugin_id}
- PATCH /api/v1/plugins/{plugin_id}/activation

### Hinweise
- Persistenz erfolgt aktuell dateibasiert in `data/elearning/pruefungen_v1.json`.
- Export- und Lösungsendpunkte sind in M0 als Queue-Stub implementiert (`status=queued`).
- RBAC aktiv für `api/v1/pruefungen` und `api/v1/plugins` über Header:
	- `X-Role`: `autor`, `review`, `freigabe`, `admin`
	- `X-User-Id`: frei wählbare Benutzerkennung
- Aktivierung/Deaktivierung von Plugins ist auf Rolle `admin` beschränkt.
- Audit-Events werden in `data/elearning/audit_log_v1.jsonl` protokolliert.

## Starten & Testen
- API lokal starten:
	- `uvicorn app.main:app --reload`
- Backend-Tests ausführen:
	- `python -m unittest discover -s tests -p "test_*.py"`
