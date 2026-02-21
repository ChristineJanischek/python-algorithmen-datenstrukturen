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
