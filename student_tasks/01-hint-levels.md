# Aufgabe 01: Intelligente Hilfestufen-Auswahl

**Typ:** Standardaufgabe  
**Schwierigkeit:** ⭐⭐  
**Empfohlener Branch:** `feature/aufgabe-01-hint-levels`

---

## Ausgangssituation

Der Lernagent kennt drei Hilfestufen (Orientierung, Hinweis, Erklärung).
Im aktuellen MVP wird immer die Stufe verwendet, die die lernende Person manuell auswählt.

Eine wirklich hilfreiche Unterstützung erkennt aber selbst, wann welche Stufe sinnvoll ist.

## Lernziel

Du verstehst, wie adaptive Systeme Benutzereingaben auswerten, und kannst
eine einfache Regel implementieren und testen.

## Fachlicher Hintergrund

Adaptive Lernsysteme analysieren die Eingaben von Lernenden, um den Grad der
Unterstützung anzupassen. Mögliche Signale sind:
- Direkte Ratlosigkeit: „Ich verstehe das nicht", „Keine Ahnung"
- Fehlerhafte Antwortversuche
- Anzahl der bisherigen Versuche
- Verständnis-Signale: „Ich glaube, ich habe es"

## Aufgabe

**Datei:** `src/learning_agent/learning/hint_levels.py`

Implementiere eine Funktion `waehle_hilfestufe`:

```python
def waehle_hilfestufe(
    eingabe: str,
    bisherige_stufe: HintLevel,
    anzahl_versuche: int,
) -> HintLevel:
    """Wählt die passende Hilfestufe anhand der Eingabe aus.
    
    Regeln (mindestens):
    - Bei Ratlosigkeit ("weiß nicht", "keine ahnung"): eine Stufe höher
    - Bei mehr als 2 Versuchen auf der gleichen Stufe: eine Stufe höher
    - Bei Verständnis-Signalen ("verstehe", "hab's"): aktuelle Stufe beibehalten
    - Nie über HintLevel.ERKLAERUNG hinausgehen
    
    Args:
        eingabe: Die Eingabe der lernenden Person.
        bisherige_stufe: Die aktuell verwendete Hilfestufe.
        anzahl_versuche: Anzahl der Versuche auf der aktuellen Stufe.
    
    Returns:
        Die empfohlene HintLevel.
    """
    raise NotImplementedError("TODO: Implementiere die Hilfestufen-Auswahl")
```

## Betroffene Dateien

- `src/learning_agent/learning/hint_levels.py` (erweitern)
- `tests/learning_agent/test_hint_levels.py` (Tests hinzufügen)

## Technische Anforderungen

- Die Funktion muss mindestens drei Regeln implementieren.
- Die Funktion darf nicht über `HintLevel.ERKLAERUNG` hinausgehen.
- Schlüsselwörter wie „weiß nicht" oder „keine ahnung" müssen erkannt werden.
- Groß-/Kleinschreibung darf keine Rolle spielen.

## Didaktische Anforderungen

- Die Regeln müssen im Docstring klar dokumentiert sein.
- Die Logik muss für Schüler verständlich und nachvollziehbar sein.

## Akzeptanzkriterien

- [ ] Funktion existiert und ist vollständig implementiert (kein `NotImplementedError`).
- [ ] Mindestens 5 Testfälle mit verschiedenen Eingaben.
- [ ] Alle Tests laufen durch (`pytest tests/`).
- [ ] Die vorhandene Funktion `ist_hoehere_stufe_sinnvoll` wird nicht entfernt.

## Benötigte Tests

```python
def test_ratlosigkeit_erhoeht_stufe():
    stufe = waehle_hilfestufe("Ich weiß nicht weiter", HintLevel.ORIENTIERUNG, 1)
    assert stufe == HintLevel.HINWEIS

def test_viele_versuche_erhoeht_stufe():
    stufe = waehle_hilfestufe("Versuch", HintLevel.ORIENTIERUNG, 3)
    assert stufe == HintLevel.HINWEIS

def test_hoechste_stufe_nicht_ueberschreiten():
    stufe = waehle_hilfestufe("Keine Ahnung", HintLevel.ERKLAERUNG, 5)
    assert stufe == HintLevel.ERKLAERUNG
```

## Pull Request

Beschreibe im PR:
- Welche Regeln du implementiert hast
- Welche Testfälle du hinzugefügt hast
- Was du dabei gelernt hast

## Reflexionsfragen

1. Wie könnte man die Erkennung von Ratlosigkeit verbessern?
2. Welche Probleme könnten entstehen, wenn die KI immer automatisch eine höhere Stufe wählt?
3. Was wäre ein fairer Algorithmus, der die Lernenden nicht zu schnell "abhängig" macht?

## Optionale Erweiterung (für schnellere Schüler)

Implementiere eine Erweiterung, die auch erkennt, ob die Eingabe
einen **Syntaxfehler** enthält (z.B. fehlendes `:` am Schleifenende).
Gib dann gezielt einen Syntaxhinweis zurück.

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
