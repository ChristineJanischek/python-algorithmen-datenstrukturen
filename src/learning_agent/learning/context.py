"""Lernkontext: Verwaltung des aktuellen Lernzustands."""

from learning_agent.models import HintLevel, LearningContext


def erstelle_kontext(
    fachgebiet: str,
    thema: str,
    niveau: str,
    lernziel: str,
    eingabe: str,
    hilfestufe: HintLevel = HintLevel.ORIENTIERUNG,
) -> LearningContext:
    """Erstellt einen neuen Lernkontext.

    Args:
        fachgebiet: Das Lehrfach.
        thema: Das konkrete Thema.
        niveau: Das Lernniveau.
        lernziel: Das Lernziel der Sitzung.
        eingabe: Die Frage oder der Lösungsversuch.
        hilfestufe: Die Hilfestufe (Standard: ORIENTIERUNG).

    Returns:
        Ein neuer ``LearningContext``.
    """
    return LearningContext(
        fachgebiet=fachgebiet.strip(),
        thema=thema.strip(),
        niveau=niveau.strip(),
        lernziel=lernziel.strip(),
        eingabe=eingabe.strip(),
        hilfestufe=hilfestufe,
    )


def erhoehe_hilfestufe(kontext: LearningContext) -> LearningContext:
    """Erhöht die Hilfestufe um eine Stufe.

    Ist die maximale Stufe erreicht, bleibt sie unverändert.

    Args:
        kontext: Der aktuelle Lernkontext.

    Returns:
        Neuer Lernkontext mit erhöhter Hilfestufe.
    """
    naechste_stufe_wert = min(kontext.hilfestufe.value + 1, HintLevel.ERKLAERUNG.value)
    naechste_stufe = HintLevel(naechste_stufe_wert)
    return LearningContext(
        fachgebiet=kontext.fachgebiet,
        thema=kontext.thema,
        niveau=kontext.niveau,
        lernziel=kontext.lernziel,
        eingabe=kontext.eingabe,
        hilfestufe=naechste_stufe,
    )
