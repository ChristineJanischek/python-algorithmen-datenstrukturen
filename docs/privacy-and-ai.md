# Datenschutz und KI

## Grundsätze

Dieses Projekt richtet sich auch an minderjährige Lernende.
Folgende Datenschutzgrundsätze sind verbindlich:

### Was gespeichert wird (MVP)

**Nichts.**

Im MVP werden keine Daten dauerhaft gespeichert:
- keine Schülerantworten,
- keine Gesprächsverläufe,
- keine Lernstände,
- keine Nutzungsstatistiken.

### Was niemals gespeichert werden darf

- Echte Namen von Schülerinnen und Schülern
- Noten oder Bewertungen
- Gesundheitsdaten
- Private Informationen aus Gesprächen
- Vollständige Gesprächsprotokolle
- API-Schlüssel oder Zugangsdaten

### Datenminimierung

Das System fragt nur nach:
- Fachgebiet (z.B. „Informatik")
- Thema (z.B. „Python-Listen")
- Lernniveau
- Lernziel
- Frage oder Lösungsversuch

Diese Angaben sind themenbezogen und nicht personenbezogen.

## Transparenz gegenüber Lernenden

Lernende müssen immer wissen:

1. **Sie arbeiten mit einem KI-System.**
2. **KI-Antworten können fehlerhaft sein.** Ergebnisse müssen selbst geprüft werden.
3. **Der Agent gibt keine Noten.** Bewertungen liegen immer beim Lehrenden.
4. **Sie können stärkere Hilfe anfordern** – die Entscheidung liegt bei ihnen.

Der Lernagent zeigt beim Start einen entsprechenden Hinweis.

## API-Schlüssel

- Keine echten API-Schlüssel im Repository.
- Kein echter Schlüssel in Tests, Beispielen oder Dokumentation.
- `.env.example` enthält nur Platzhalter.
- Eine echte `.env`-Datei wird in `.gitignore` ausgeschlossen.

## DSGVO-Hinweis

Das Projekt befindet sich im Schulkontext.
Bevor echte Schülerdaten verarbeitet werden, muss:
- die Schulleitung informiert werden,
- eine datenschutzrechtliche Prüfung stattfinden,
- eine Einwilligung der Erziehungsberechtigten vorliegen (bei Minderjährigen),
- ein Verarbeitungsverzeichnis angelegt werden.

Der MVP vermeidet diese Anforderungen durch Verzicht auf jegliche Datenspeicherung.

## Grenzen der KI

Lernende sollen verstehen:

- KI-Systeme generieren Texte – sie „wissen" nichts im menschlichen Sinne.
- KI-Antworten können plausibel klingen, aber falsch sein.
- Der Lernagent ist ein **Lernwerkzeug**, kein Tutor mit menschlichem Urteil.
- Eigenes Nachdenken und kritisches Prüfen bleiben unersetzbar.

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
