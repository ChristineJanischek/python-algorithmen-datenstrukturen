"""Systemprompt-Erzeugung für den Lernagenten.

Der Systemprompt legt das Verhalten des Agenten fest:
- Didaktische Grundsätze (kein direktes Lösen der Aufgabe),
- Hilfestufe,
- aktueller Lernkontext.

SCHÜLERAUFGABE (student_tasks/02-prompt-strategies.md):
    Verbessere die Prompt-Strategie:
    - Ergänze Anweisungen für metakognitive Fragen.
    - Füge Anweisungen zur Fehleranalyse hinzu.
    - Passe den Prompt für verschiedene Niveaustufen an.
"""

from learning_agent.models import HintLevel, LearningContext, Message, MessageRole
from learning_agent.learning.hint_levels import beschreibe_hilfestufe

_DATENSCHUTZ_HINWEIS = (
    "Du arbeitest mit einem KI-System. KI-Antworten können fehlerhaft sein. "
    "Überprüfe Ergebnisse immer selbst."
)

_GRUNDREGELN = """Du bist ein didaktischer Lernagent für Schülerinnen und Schüler.
Deine Aufgabe ist es NICHT, die Aufgabe direkt zu lösen.
Stattdessen hilfst du den Lernenden, die Lösung selbst zu finden.
Sei respektvoll, konkret, verständlich und ermutigend.
Sage niemals einfach "falsch" ohne Erklärung.
Verwende klare, schülergerechte Sprache."""


def erzeuge_systemprompt(kontext: LearningContext) -> str:
    """Erzeugt den Systemprompt für den aktuellen Lernkontext.

    Args:
        kontext: Der aktuelle Lernkontext.

    Returns:
        Den vollständigen Systemprompt als Text.
    """
    hilfestufe_text = beschreibe_hilfestufe(kontext.hilfestufe)
    stufe_nr = kontext.hilfestufe.value

    prompt_teile = [
        _GRUNDREGELN,
        "",
        f"Aktueller Lernkontext:",
        f"  Fachgebiet: {kontext.fachgebiet}",
        f"  Thema: {kontext.thema}",
        f"  Niveau: {kontext.niveau}",
        f"  Lernziel: {kontext.lernziel}",
        "",
        f"Aktuelle Hilfestufe: {stufe_nr} – {hilfestufe_text}",
        # Codiertes Token, damit der MockProvider die Stufe auslesen kann
        f"HILFESTUFE:{stufe_nr}",
        "",
    ]

    if kontext.hilfestufe == HintLevel.ORIENTIERUNG:
        prompt_teile.append(
            "Stelle eine offene Frage, die hilft, das Problem zu verstehen. "
            "Gib noch keinen fachlichen Hinweis."
        )
    elif kontext.hilfestufe == HintLevel.HINWEIS:
        prompt_teile.append(
            "Gib einen fachlichen Hinweis oder beschreibe eine Teilstrategie. "
            "Erkläre noch nicht die vollständige Lösung."
        )
    elif kontext.hilfestufe == HintLevel.ERKLAERUNG:
        prompt_teile.append(
            "Erkläre den Lösungsweg ausführlich. "
            "Du kannst eine Musterlösung zeigen, "
            "aber stelle danach eine Reflexions- oder Transferfrage."
        )

    prompt_teile.append("")
    prompt_teile.append(_DATENSCHUTZ_HINWEIS)

    return "\n".join(prompt_teile)


def erzeuge_nachrichten(kontext: LearningContext) -> list[Message]:
    """Erzeugt die vollständige Nachrichtenliste für den Provider.

    Args:
        kontext: Der aktuelle Lernkontext.

    Returns:
        Liste mit System- und Nutzernachricht.
    """
    systemprompt = erzeuge_systemprompt(kontext)
    return [
        Message(role=MessageRole.SYSTEM, content=systemprompt),
        Message(role=MessageRole.USER, content=kontext.eingabe),
    ]
