"""Beispiel: Eine einfache Lernsitzung mit dem Lernagenten.

Dieses Skript zeigt, wie der Lernagent programmatisch verwendet wird.
Es benötigt keine Eingabe und kann direkt ausgeführt werden.

Starte mit:
    python examples/basic_session.py
"""

import sys
from pathlib import Path

# Damit das Skript auch ohne Installation aus dem Projektverzeichnis läuft
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from learning_agent.agent import LearningAgent
from learning_agent.learning.feedback import formatiere_antwort
from learning_agent.models import HintLevel
from learning_agent.providers.mock_provider import MockProvider


def main() -> None:
    agent = LearningAgent(provider=MockProvider())

    print("=" * 60)
    print("  Beispiel-Lernsitzung (programmatisch)")
    print("=" * 60)

    # Sitzung: Stufe 1 – Orientierungsfrage
    print("\n--- Hilfestufe 1: Orientierungsfrage ---")
    antwort1 = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente zu einer Liste hinzufügen",
        eingabe="Ich weiß nicht, wie ich ein neues Element ergänzen kann.",
        hilfestufe=HintLevel.ORIENTIERUNG,
    )
    print(f"Eingabe: Ich weiß nicht, wie ich ein neues Element ergänzen kann.")
    print(formatiere_antwort(antwort1))

    # Sitzung: Stufe 2 – Fachlicher Hinweis
    print("\n--- Hilfestufe 2: Fachlicher Hinweis ---")
    antwort2 = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente zu einer Liste hinzufügen",
        eingabe="Ich habe eine leere Liste, aber weiß nicht welche Methode.",
        hilfestufe=HintLevel.HINWEIS,
    )
    print(f"Eingabe: Ich habe eine leere Liste, aber weiß nicht welche Methode.")
    print(formatiere_antwort(antwort2))

    # Sitzung: Stufe 3 – Ausführliche Erklärung
    print("\n--- Hilfestufe 3: Ausführliche Erklärung ---")
    antwort3 = agent.verarbeite(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente zu einer Liste hinzufügen",
        eingabe="Ich brauche eine ausführliche Erklärung.",
        hilfestufe=HintLevel.ERKLAERUNG,
    )
    print(f"Eingabe: Ich brauche eine ausführliche Erklärung.")
    print(formatiere_antwort(antwort3))

    print("\n" + "=" * 60)
    print("  Ende der Beispiel-Sitzung")
    print("=" * 60)


if __name__ == "__main__":
    main()
