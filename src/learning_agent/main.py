"""Konsolenanwendung des Lernagenten (MVP).

Starte mit:
    python -m learning_agent.main
oder:
    python src/learning_agent/main.py

DATENSCHUTZ-HINWEIS:
    Es werden keine personenbezogenen Daten gespeichert.
    Die Sitzung wird nach Beendigung nicht aufbewahrt.
    Du arbeitest mit einem KI-System – Antworten können fehlerhaft sein.
"""

import sys

from learning_agent.agent import LearningAgent
from learning_agent.learning.feedback import formatiere_antwort
from learning_agent.learning.hint_levels import (
    beschreibe_hilfestufe,
    ist_hoehere_stufe_sinnvoll,
)
from learning_agent.models import HintLevel
from learning_agent.providers.mock_provider import MockProvider


def _eingabe(aufforderung: str) -> str:
    """Liest eine Eingabe von der Konsole und bricht bei EOF oder leerem Input ab.

    Args:
        aufforderung: Der angezeigte Eingabetext.

    Returns:
        Der eingegebene Text (getrimmt).
    """
    try:
        wert = input(aufforderung).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nSitzung beendet.")
        sys.exit(0)
    return wert


def starte_sitzung() -> None:
    """Startet eine interaktive Lernsitzung in der Konsole."""
    print("=" * 60)
    print("  Lernagent – Didaktischer KI-Assistent (MVP)")
    print("=" * 60)
    print(
        "\nHINWEIS: Du arbeitest mit einem KI-System (MockProvider).\n"
        "Antworten des Agenten können fehlerhaft sein.\n"
        "Überprüfe Ergebnisse immer selbst.\n"
    )

    fachgebiet = _eingabe("Lerngebiet (z.B. Informatik): ")
    thema = _eingabe("Thema (z.B. Python-Listen): ")
    niveau = _eingabe("Lernniveau (z.B. Einstieg): ")
    lernziel = _eingabe("Lernziel (z.B. Elemente zu einer Liste hinzufügen): ")

    if not all([fachgebiet, thema, niveau, lernziel]):
        print("Alle Felder müssen ausgefüllt werden. Sitzung beendet.")
        sys.exit(1)

    agent = LearningAgent(provider=MockProvider())
    hilfestufe = HintLevel.ORIENTIERUNG
    versuche_auf_stufe = 0

    print("\n" + "-" * 60)
    print("Eingabe: Stelle eine Frage oder beschreibe deinen Lösungsversuch.")
    print("Eingabe: 'mehr' für eine höhere Hilfestufe, 'ende' zum Beenden.\n")

    while True:
        eingabe = _eingabe("Deine Frage oder dein Lösungsversuch: ")

        if eingabe.lower() == "ende":
            print("\nSitzung beendet. Viel Erfolg weiterhin!")
            break

        if eingabe.lower() == "mehr":
            if hilfestufe == HintLevel.ERKLAERUNG:
                print("Du befindest dich bereits auf der höchsten Hilfestufe.")
                continue
            hilfestufe = HintLevel(hilfestufe.value + 1)
            versuche_auf_stufe = 0
            print(f"Hilfestufe erhöht auf: {beschreibe_hilfestufe(hilfestufe)}")
            continue

        if not eingabe:
            print("Bitte gib etwas ein.")
            continue

        antwort = agent.verarbeite(
            fachgebiet=fachgebiet,
            thema=thema,
            niveau=niveau,
            lernziel=lernziel,
            eingabe=eingabe,
            hilfestufe=hilfestufe,
        )

        print(formatiere_antwort(antwort))
        versuche_auf_stufe += 1

        if versuche_auf_stufe >= 2 and hilfestufe != HintLevel.ERKLAERUNG:
            print(
                "\nTipp: Wenn du mehr Hilfe möchtest, tippe 'mehr'."
            )

        print()


if __name__ == "__main__":
    starte_sitzung()
