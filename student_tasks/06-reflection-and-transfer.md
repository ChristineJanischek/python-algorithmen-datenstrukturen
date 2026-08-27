# Aufgabe 06: Reflexions- und Transferfragen

**Typ:** Erweiterungsaufgabe  
**Schwierigkeit:** ⭐⭐  
**Empfohlener Branch:** `feature/aufgabe-06-reflection`

---

## Ausgangssituation

Der Lernagent gibt didaktische Antworten zurück.
Er stellt aber noch keine automatischen Reflexions- oder Transferfragen,
nachdem er eine Erklärung gegeben hat.

Gutes Lernen endet nicht mit der Antwort – es folgt eine Frage,
die das Gelernte festigt oder überträgt.

## Lernziel

Du verstehst das Konzept des **Transferlernens** und kannst
den Agenten so erweitern, dass er nach einer Erklärung
automatisch eine sinnvolle Folgefrage stellt.

## Fachlicher Hintergrund

**Metakognition** bedeutet, über das eigene Denken nachzudenken.
Typische Reflexionsfragen sind:
- „Wie bist du auf diesen Lösungsweg gekommen?"
- „Was würdest du beim nächsten Mal anders machen?"
- „Woran erkennst du, dass deine Lösung funktioniert?"

**Transfer** bedeutet, das Gelernte auf eine neue Situation anzuwenden:
- „Wie würdest du das bei einer anderen Datenstruktur lösen?"
- „Kannst du das Gleiche mit einer While-Schleife schreiben?"

## Aufgabe

**Datei:** `src/learning_agent/learning/feedback.py`

Implementiere folgende Funktion:

```python
def erzeuge_reflexionsfrage(kontext: LearningContext) -> str:
    """Erzeugt eine Reflexions- oder Transferfrage passend zum Kontext.
    
    TODO: Implementiere mindestens drei verschiedene Fragemuster:
    1. Allgemeine Reflexion: „Wie bist du auf die Lösung gekommen?"
    2. Themenspezifische Reflexion basierend auf kontext.thema
    3. Transfer: „Wie würdest du vorgehen, wenn...?"
    
    Die Frage soll zum Lernziel passen und ermutigen.
    
    Eingabe: kontext (LearningContext)
    Ausgabe: Fragetext (str)
    """
    raise NotImplementedError("TODO: Aufgabe 06")
```

Ändere außerdem `erzeuge_antwort` so, dass bei `HintLevel.ERKLAERUNG`
automatisch eine Reflexionsfrage an den Antworttext angehängt wird.

## Betroffene Dateien

- `src/learning_agent/learning/feedback.py` (erweitern)
- `tests/learning_agent/test_feedback.py` (neu anlegen)

## Akzeptanzkriterien

- [ ] `erzeuge_reflexionsfrage` ist vollständig implementiert.
- [ ] Bei `HintLevel.ERKLAERUNG` enthält die Antwort immer eine Reflexionsfrage.
- [ ] Die Frage ist zum Thema passend (nicht immer dieselbe).
- [ ] Mindestens 4 Tests für die neue Funktion.

## Reflexionsfragen (zu dieser Aufgabe!)

1. Warum ist es wichtig, dass ein Lernagent *nicht* einfach alles erklärt?
2. Wann kann zu viel Scaffolding schädlich sein?
3. Wie würdest du messen, ob die Reflexionsfragen tatsächlich helfen?

## Optionale Erweiterung

Nutze die Reflexionsfrage aus dem Lernmodul (falls vorhanden):
Wenn ein `LearningModule` geladen ist und die Sitzung das gleiche Thema hat,
verwende die Reflexionsfrage aus dem Modul statt einer allgemeinen Frage.

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
