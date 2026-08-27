# Aufgabe 02: Verbesserte Prompt-Strategien

**Typ:** Standardaufgabe  
**Schwierigkeit:** ⭐⭐  
**Empfohlener Branch:** `feature/aufgabe-02-prompt-strategies`

---

## Ausgangssituation

Der Systemprompt in `system_prompt.py` gibt dem Sprachmodell grundlegende Anweisungen.
Er ist funktional, aber noch nicht sehr präzise und differenziert.

Ein guter Prompt führt zu besseren, gezielteren Antworten – besonders bei didaktischen Systemen.

## Lernziel

Du verstehst, wie Systemprompts die Qualität von KI-Antworten beeinflussen,
und kannst einen Prompt gezielt für verschiedene Lernziele anpassen.

## Fachlicher Hintergrund

**Prompt Engineering** bezeichnet die gezielte Formulierung von Anweisungen
an ein Sprachmodell. Wichtige Prinzipien:
- Konkrete Verhaltensregeln statt allgemeiner Aufforderungen
- Rollenspezifikation: „Du bist ein..."-Formulierungen
- Beispiele einbetten (Few-Shot-Prompting)
- Negative Beispiele: Was soll der Agent *nicht* tun?

## Aufgabe

**Datei:** `src/learning_agent/prompts/system_prompt.py`

Erweitere den Systemprompt um mindestens zwei der folgenden Punkte:

### Option A: Metakognitive Fragen
Füge Anweisungen hinzu, die den Agenten dazu bringen,
metakognitive Fragen zu stellen:
- „Wie bist du auf diesen Lösungsweg gekommen?"
- „Welche Annahme hast du dabei gemacht?"
- „Wie könntest du deine Lösung testen?"

### Option B: Niveauanpassung
Passe den Prompt abhängig vom Niveau an:
- **Einstieg:** Einfache Sprache, kurze Sätze, Alltagsbeispiele
- **Fortgeschritten:** Fachbegriffe erlaubt, komplexere Erklärungen

### Option C: Fehleranalyse-Anweisung
Füge eine Anweisung hinzu, die den Agenten instruiert:
„Wenn die Eingabe einen Fehler enthält, benenne zuerst die Art des Fehlers
(Syntaxfehler, Verständnisfehler, Strategiefehler), bevor du einen Hinweis gibst."

## Betroffene Dateien

- `src/learning_agent/prompts/system_prompt.py` (erweitern)
- `tests/learning_agent/test_prompt.py` (Tests anpassen/hinzufügen)

## Technische Anforderungen

- Die Funktion `erzeuge_systemprompt(kontext)` muss weiterhin funktionieren.
- Bestehende Tests dürfen nicht brechen.
- Neue Inhalte müssen für verschiedene Kontexte generiert werden.

## Akzeptanzkriterien

- [ ] Mindestens zwei Erweiterungen aus den Optionen A–C implementiert.
- [ ] Neue Tests für die neuen Prompt-Inhalte.
- [ ] Alle bestehenden Tests laufen weiterhin durch.
- [ ] Der Prompt ist verständlich und kommentiert.

## Reflexionsfragen

1. Wie kann man überprüfen, ob ein Prompt „gut" ist?
2. Was sind Risiken, wenn der Prompt zu viele Anweisungen enthält?
3. Warum sollte ein didaktischer Agent anders instruiert werden als ein allgemeiner Assistent?

## Optionale Erweiterung

Implementiere PHP-Python-Vergleiche: Wenn das Fachgebiet „Informatik" ist
und das Thema Schleifenstrukturen enthält, füge einen Hinweis ein,
der einen Vergleich mit PHP anbietet.
