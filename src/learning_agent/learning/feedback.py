"""Feedback-Erzeugung: Strukturierte Rückmeldungen für Lernende.

Rückmeldungen müssen respektvoll, konkret, verständlich und ermutigend sein.
Pauschale Aussagen wie „falsch" ohne Erklärung sind zu vermeiden.
"""

from learning_agent.models import AgentResponse, HintLevel, ResponseType


def erzeuge_antwort(
    text: str,
    hilfestufe: HintLevel,
    antworttyp: ResponseType = ResponseType.FRAGE,
    naechste_aktion: str | None = None,
) -> AgentResponse:
    """Erstellt eine strukturierte Agentenantwort.

    Args:
        text: Der Antworttext für die lernende Person.
        hilfestufe: Die verwendete Hilfestufe.
        antworttyp: Art der Rückmeldung.
        naechste_aktion: Optionaler Vorschlag für den nächsten Schritt.

    Returns:
        Eine strukturierte ``AgentResponse``.
    """
    return AgentResponse(
        text=text,
        antworttyp=antworttyp,
        hilfestufe=hilfestufe,
        naechste_aktion=naechste_aktion,
    )


def formatiere_antwort(antwort: AgentResponse) -> str:
    """Formatiert eine Agentenantwort für die Konsolenausgabe.

    Args:
        antwort: Die Agentenantwort.

    Returns:
        Formatierter Text für die Ausgabe.
    """
    ausgabe = f"\nLernagent ({antwort.antworttyp.value}):\n{antwort.text}"
    if antwort.naechste_aktion:
        ausgabe += f"\n\n→ {antwort.naechste_aktion}"
    return ausgabe
