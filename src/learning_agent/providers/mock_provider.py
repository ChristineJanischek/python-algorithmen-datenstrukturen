"""MockProvider: Zuverlässig testbarer Ersatz für ein echtes Sprachmodell.

Der MockProvider gibt vordefinierte, didaktisch sinnvolle Antworten zurück.
Er benötigt weder API-Schlüssel noch Internetverbindung.
Er ist der Standardprovider im MVP und in allen Tests.

HINWEIS FÜR SCHÜLER:
    Ein echter externer Provider (z.B. OpenAI-kompatible API) kann später
    als Erweiterung implementiert werden. Dazu muss nur die ``generate``-
    Methode mit einem echten API-Aufruf versehen werden.
    Niemals API-Schlüssel im Quellcode speichern!
    Verwende dafür ausschließlich Umgebungsvariablen (.env).
"""

import re

from learning_agent.models import HintLevel, Message, MessageRole
from learning_agent.providers.base import BaseProvider

# Antworten nach Hilfestufe und Schlüsselwörtern im Kontext
_MOCK_ANSWERS: dict[str, list[str]] = {
    "liste": [
        "Welche Operation möchtest du durchführen: "
        "ein Element lesen, verändern oder am Ende ergänzen?",
        "Python-Listen haben eine Methode, die speziell dafür gedacht ist, "
        "Elemente anzuhängen. Kennst du Methoden, die auf Listen aufgerufen werden?",
        "Mit ``meine_liste.append(element)`` fügst du ein Element am Ende der "
        "Liste hinzu. ``append`` kommt vom englischen Wort fuer 'anhaengen'.",
    ],
    "schleife": [
        "Was soll mit jedem Element der Liste passieren?",
        "Eine ``for``-Schleife eignet sich, um alle Elemente nacheinander "
        "zu verarbeiten. Wie würdest du die Schleife aufbauen?",
        "``for element in meine_liste:`` durchläuft alle Elemente. "
        "Im Schleifenrumpf kannst du mit ``element`` arbeiten.",
    ],
    "fehler": [
        "Was genau passiert, wenn du den Code ausführst? Welche Fehlermeldung siehst du?",
        "Schau dir die Fehlermeldung genau an: "
        "Welche Zeile wird genannt? Was bedeutet der Fehlertyp?",
        "Syntax-Fehler entstehen oft durch fehlende Doppelpunkte, "
        "falsche Einrückung oder vergessene Klammern.",
    ],
    "default": [
        "Was weißt du bereits über dieses Thema? "
        "Formuliere zunächst in eigenen Worten, was gefragt ist.",
        "Denk an ähnliche Aufgaben, die du schon gelöst hast. "
        "Welcher Schritt könnte hier als Erstes sinnvoll sein?",
        "Hier ist ein strukturierter Hinweis: Teile die Aufgabe in kleinere "
        "Teilschritte auf und löse jeden Schritt nacheinander.",
    ],
}


def _waehle_antwortliste(user_text: str) -> list[str]:
    """Wählt die passende Antwortliste anhand von Schlüsselwörtern aus.

    Args:
        user_text: Eingabetext der lernenden Person.

    Returns:
        Liste mit drei Antworten für die drei Hilfestufen.
    """
    text = user_text.lower()
    for schluessel, antworten in _MOCK_ANSWERS.items():
        if schluessel != "default" and re.search(schluessel, text):
            return antworten
    return _MOCK_ANSWERS["default"]


def _bestimme_hilfestufe(messages: list[Message]) -> HintLevel:
    """Leitet die Hilfestufe aus dem Systemkontext ab.

    Sucht im Systemkontext nach der codierten Hilfestufe.

    Args:
        messages: Gesprächshistorie.

    Returns:
        Die Hilfestufe als ``HintLevel``.
    """
    for msg in messages:
        if msg.role == MessageRole.SYSTEM:
            if "HILFESTUFE:3" in msg.content:
                return HintLevel.ERKLAERUNG
            if "HILFESTUFE:2" in msg.content:
                return HintLevel.HINWEIS
    return HintLevel.ORIENTIERUNG


class MockProvider(BaseProvider):
    """Zuverlässig testbarer Provider ohne externe Abhängigkeiten.

    Gibt vordefinierte, didaktisch strukturierte Antworten zurück.
    Die Antwort wird anhand von Schlüsselwörtern in der Nutzereingabe
    und der aktuellen Hilfestufe ausgewählt.
    """

    def generate(self, messages: list[Message]) -> str:
        """Gibt eine vordefinierte didaktische Antwort zurück.

        Args:
            messages: Gesprächshistorie mit Systemkontext und Nutzereingabe.

        Returns:
            Passende Antwort als Text.
        """
        user_text = ""
        for msg in messages:
            if msg.role == MessageRole.USER:
                user_text = msg.content
                break

        hilfestufe = _bestimme_hilfestufe(messages)
        antwortliste = _waehle_antwortliste(user_text)

        # Index 0 = Hilfestufe 1 (ORIENTIERUNG), Index 2 = Hilfestufe 3 (ERKLAERUNG)
        index = hilfestufe.value - 1
        return antwortliste[index]
