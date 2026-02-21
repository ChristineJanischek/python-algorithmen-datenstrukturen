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

### Hinweise
- Persistenz erfolgt aktuell dateibasiert in `data/elearning/pruefungen_v1.json`.
- Export- und Lösungsendpunkte sind in M0 als Queue-Stub implementiert (`status=queued`).

## Starten & Testen
- API lokal starten:
	- `uvicorn app.main:app --reload`
- Backend-Tests ausführen:
	- `python -m unittest discover -s tests -p "test_*.py"`
