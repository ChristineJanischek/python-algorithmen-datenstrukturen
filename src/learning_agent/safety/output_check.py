"""Ausgabeprüfung: Sicherheitsprüfungen für Agentenantworten.

Prüft generierte Antworten, bevor sie an die lernende Person ausgegeben werden.

HINWEIS:
    KI-generierte Antworten können fehlerhaft sein.
    Lernende sollen stets darauf hingewiesen werden, Ergebnisse zu prüfen.
"""

_MAX_ANTWORT_LAENGE = 5000  # Zeichen


class AusgabeFehler(ValueError):
    """Wird ausgelöst, wenn eine Ausgabe die Sicherheitsprüfung nicht besteht."""


def pruefe_ausgabe(text: str) -> str:
    """Prüft eine Agentenantwort auf Sicherheitsprobleme.

    Args:
        text: Die generierte Antwort des Agenten.

    Returns:
        Die bereinigte Antwort.

    Raises:
        AusgabeFehler: Wenn die Antwort nicht ausgegeben werden kann.
    """
    if not text or not text.strip():
        raise AusgabeFehler("Der Agent hat keine Antwort erzeugt.")

    if len(text) > _MAX_ANTWORT_LAENGE:
        # Antwort kürzen statt ablehnen
        return text[:_MAX_ANTWORT_LAENGE] + "\n\n[Antwort gekürzt]"

    return text.strip()
