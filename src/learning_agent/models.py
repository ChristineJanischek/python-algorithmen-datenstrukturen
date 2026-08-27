"""Datenmodelle für den Lernagenten.

Diese Modelle beschreiben die zentralen Datenstrukturen:
- LearningContext: Was und wie wird gelernt?
- Message: Eine Nachricht im Gespräch mit dem Agenten.
- AgentResponse: Eine strukturierte Antwort des Agenten.
- HintLevel: Die drei Hilfestufen des Agenten.
- LearningModule: Ein wiederverwendbares Lernmodul.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class HintLevel(Enum):
    """Die drei Hilfestufen des Lernagenten.

    ORIENTIERUNG: Orientierungs- oder Verständnisfrage
    HINWEIS:       Fachlicher Hinweis oder Teilstrategie
    ERKLAERUNG:    Ausführlichere Erklärung des Lösungsweges
    """

    ORIENTIERUNG = 1
    HINWEIS = 2
    ERKLAERUNG = 3


class ResponseType(Enum):
    """Art der Rückmeldung des Agenten."""

    FRAGE = "frage"
    HINWEIS = "hinweis"
    ERKLAERUNG = "erklaerung"
    LOESUNG = "loesung"
    FEHLERANALYSE = "fehleranalyse"
    REFLEXION = "reflexion"


class MessageRole(Enum):
    """Rolle einer Gesprächsnachricht."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


@dataclass
class Message:
    """Eine Nachricht im Gespräch mit dem Lernagenten.

    Attributes:
        role: Wer sendet die Nachricht (System, Lernender oder Agent)?
        content: Der Inhalt der Nachricht.
    """

    role: MessageRole
    content: str


@dataclass
class LearningContext:
    """Der Lernkontext einer Sitzung.

    Beschreibt, was und wie gelernt wird.
    Enthält keine personenbezogenen Daten.

    Attributes:
        fachgebiet: Das Lehrfach, z.B. „Informatik".
        thema: Das konkrete Thema, z.B. „Python-Listen".
        niveau: Das Lernniveau, z.B. „Einstieg", „Fortgeschritten".
        lernziel: Das aktuelle Lernziel, z.B. „Elemente hinzufügen".
        eingabe: Die Frage oder der Lösungsversuch der lernenden Person.
        hilfestufe: Die aktuell gewählte Hilfestufe.
    """

    fachgebiet: str
    thema: str
    niveau: str
    lernziel: str
    eingabe: str
    hilfestufe: HintLevel = HintLevel.ORIENTIERUNG


@dataclass
class AgentResponse:
    """Die strukturierte Antwort des Lernagenten.

    Attributes:
        text: Der Antworttext für die lernende Person.
        antworttyp: Art der Rückmeldung.
        hilfestufe: Die verwendete Hilfestufe.
        naechste_aktion: Optionaler Vorschlag für den nächsten Schritt.
    """

    text: str
    antworttyp: ResponseType
    hilfestufe: HintLevel
    naechste_aktion: str | None = None


@dataclass
class LearningModule:
    """Ein wiederverwendbares Lernmodul.

    Attributes:
        id: Eindeutige Kennung des Moduls.
        titel: Titel des Moduls.
        fachgebiet: Das Lehrfach.
        thema: Das Thema.
        niveau: Zielgruppe bzw. Niveau.
        lernziele: Liste der Lernziele.
        vorkenntnisse: Benötigte Vorkenntnisse.
        aufgabenstellung: Die Aufgabenstellung.
        fehlvorstellungen: Häufige Fehlvorstellungen.
        hinweise: Hinweise nach Hilfestufen (1–3).
        reflexionsfrage: Reflexionsfrage nach der Aufgabe.
        transferaufgabe: Eine ähnliche Aufgabe zum Übertragen.
    """

    id: str
    titel: str
    fachgebiet: str
    thema: str
    niveau: str
    lernziele: list[str]
    vorkenntnisse: list[str]
    aufgabenstellung: str
    fehlvorstellungen: list[str]
    hinweise: dict[int, str]
    reflexionsfrage: str
    transferaufgabe: str
    metadaten: dict = field(default_factory=dict)
