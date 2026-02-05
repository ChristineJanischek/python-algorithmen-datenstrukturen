# Architektur (Kurzüberblick)

## Ziel
Moderne, erweiterbare E-Learning-Plattform mit Aufgaben, Themen und Code-Boxen.

## Struktur
- Backend: FastAPI in apps/api
- Frontend: React (Vite) in apps/web
- Daten: JSON unter data/elearning
- Fachliche Inhalte: Struktogramme und Aufgaben im Repository

## Erweiterbarkeit
- Neue Themen: data/elearning/themes.json
- Neue Meilensteine: data/elearning/milestones.json + Markdown im Aufgabenverzeichnis
- Neue Aufgaben: data/elearning/tasks.json

## Inhalte
- Meilenstein 1 (Listen, Sortieren, Suchen) ist eingebettet und wird über die API ausgeliefert.
