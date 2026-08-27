"""Agentensteuerung: Zentrale Steuerlogik des Lernagenten.

Der Agent verbindet alle Komponenten:
- Lernkontext (``LearningContext``)
- Prompt-Erzeugung (``system_prompt``)
- Provider (``LLMProvider``)
- Feedback (``AgentResponse``)
- Sicherheitsprüfungen (``safety``)
"""

from learning_agent.learning.context import erstelle_kontext
from learning_agent.learning.feedback import erzeuge_antwort
from learning_agent.models import (
    AgentResponse,
    HintLevel,
    LearningContext,
    ResponseType,
)
from learning_agent.prompts.system_prompt import erzeuge_nachrichten
from learning_agent.providers import LLMProvider
from learning_agent.safety.input_check import EingabeFehler, pruefe_eingabe
from learning_agent.safety.output_check import AusgabeFehler, pruefe_ausgabe


class LearningAgent:
    """Zentraler Lernagent.

    Nimmt die Eingabe der lernenden Person entgegen, erzeugt einen
    strukturierten Prompt und gibt eine didaktisch strukturierte
    Antwort zurück.

    Args:
        provider: Der LLM-Provider (Standard: MockProvider).
    """

    def __init__(self, provider: LLMProvider) -> None:
        self._provider = provider

    def verarbeite(
        self,
        fachgebiet: str,
        thema: str,
        niveau: str,
        lernziel: str,
        eingabe: str,
        hilfestufe: HintLevel = HintLevel.ORIENTIERUNG,
    ) -> AgentResponse:
        """Verarbeitet eine Anfrage und gibt eine strukturierte Antwort zurück.

        Args:
            fachgebiet: Das Lehrfach.
            thema: Das Thema.
            niveau: Das Lernniveau.
            lernziel: Das Lernziel.
            eingabe: Frage oder Lösungsversuch der lernenden Person.
            hilfestufe: Die gewünschte Hilfestufe.

        Returns:
            Eine strukturierte ``AgentResponse``.
        """
        try:
            bereinigte_eingabe = pruefe_eingabe(eingabe)
        except EingabeFehler as fehler:
            return erzeuge_antwort(
                text=str(fehler),
                hilfestufe=hilfestufe,
                antworttyp=ResponseType.FEHLERANALYSE,
            )

        kontext = erstelle_kontext(
            fachgebiet=fachgebiet,
            thema=thema,
            niveau=niveau,
            lernziel=lernziel,
            eingabe=bereinigte_eingabe,
            hilfestufe=hilfestufe,
        )

        nachrichten = erzeuge_nachrichten(kontext)
        rohtext = self._provider.generate(nachrichten)

        try:
            text = pruefe_ausgabe(rohtext)
        except AusgabeFehler as fehler:
            return erzeuge_antwort(
                text=f"Der Agent konnte keine Antwort erzeugen: {fehler}",
                hilfestufe=hilfestufe,
                antworttyp=ResponseType.FEHLERANALYSE,
            )

        antworttyp = _bestimme_antworttyp(hilfestufe)
        return erzeuge_antwort(text=text, hilfestufe=hilfestufe, antworttyp=antworttyp)


def _bestimme_antworttyp(hilfestufe: HintLevel) -> ResponseType:
    """Leitet den Antworttyp aus der Hilfestufe ab.

    Args:
        hilfestufe: Die verwendete Hilfestufe.

    Returns:
        Der passende ``ResponseType``.
    """
    mapping = {
        HintLevel.ORIENTIERUNG: ResponseType.FRAGE,
        HintLevel.HINWEIS: ResponseType.HINWEIS,
        HintLevel.ERKLAERUNG: ResponseType.ERKLAERUNG,
    }
    return mapping.get(hilfestufe, ResponseType.HINWEIS)
