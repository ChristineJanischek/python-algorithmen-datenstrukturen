"""Hilfestufen: Logik zur Auswahl und Beschreibung der drei Hilfestufen.

Das Hilfestufen-System ist ein zentrales didaktisches Element:

Stufe 1 – ORIENTIERUNG:
    Der Agent stellt eine Frage, die hilft, das Problem zu verstehen.
    Keine Lösung oder Strategie wird genannt.

Stufe 2 – HINWEIS:
    Der Agent gibt einen fachlichen Hinweis oder eine Teilstrategie.
    Noch keine vollständige Erklärung.

Stufe 3 – ERKLAERUNG:
    Der Agent erklärt den Lösungsweg ausführlich.
    Kann auch eine Musterlösung enthalten – immer mit Reflexionsfrage.

SCHÜLERAUFGABE (student_tasks/01-hint-levels.md):
    Die adaptive Auswahl der passenden Hilfestufe anhand des
    Lernstands und der Eingabe ist noch nicht implementiert.
    Entwickle eine Funktion ``waehle_hilfestufe(kontext, verlauf)``,
    die automatisch entscheidet, welche Stufe angemessen ist.
"""

from learning_agent.models import HintLevel, LearningContext

# Beschreibungen der Hilfestufen für die Ausgabe
STUFEN_BESCHREIBUNGEN: dict[HintLevel, str] = {
    HintLevel.ORIENTIERUNG: "Orientierungsfrage",
    HintLevel.HINWEIS: "Fachlicher Hinweis",
    HintLevel.ERKLAERUNG: "Ausführliche Erklärung",
}


def beschreibe_hilfestufe(stufe: HintLevel) -> str:
    """Gibt eine lesbare Beschreibung der Hilfestufe zurück.

    Args:
        stufe: Die Hilfestufe.

    Returns:
        Beschreibungstext der Hilfestufe.
    """
    return STUFEN_BESCHREIBUNGEN.get(stufe, "Unbekannte Stufe")


def ist_hoehere_stufe_sinnvoll(kontext: LearningContext, anzahl_versuche: int) -> bool:
    """Prüft einfach, ob eine höhere Hilfestufe angeboten werden sollte.

    Diese einfache Regel: Nach zwei Versuchen auf gleicher Stufe wird
    eine höhere Stufe angeboten.

    TODO (Schüleraufgabe):
        Implementiere eine intelligentere Regel, die den Inhalt der
        Eingabe analysiert. Erkenne z.B., ob:
        - der Lernende ratlos wirkt („ich verstehe das nicht"),
        - ein konkreter Denkfehler vorliegt,
        - ein Syntax-, Verständnis- oder Strategiefehler erkennbar ist.
        Eingabe: kontext (LearningContext), verlauf (list[Message])
        Ausgabe: bool oder HintLevel
        Akzeptanzkriterien: Tests in tests/learning_agent/test_hint_levels.py

    Args:
        kontext: Der aktuelle Lernkontext.
        anzahl_versuche: Wie oft die aktuelle Stufe schon genutzt wurde.

    Returns:
        True, wenn eine höhere Stufe angeboten werden sollte.
    """
    return anzahl_versuche >= 2 and kontext.hilfestufe != HintLevel.ERKLAERUNG
