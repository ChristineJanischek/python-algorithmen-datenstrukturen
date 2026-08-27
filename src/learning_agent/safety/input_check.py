"""Eingabeprüfung: Sicherheitsprüfungen für Benutzereingaben.

Prüft Eingaben auf offensichtlich problematische Inhalte,
bevor sie an den Provider weitergegeben werden.

DATENSCHUTZ-HINWEIS:
    Keine Eingaben werden dauerhaft gespeichert.
    Es werden keine personenbezogenen Daten verarbeitet.

SCHÜLERAUFGABE (student_tasks/03-error-analysis.md):
    Erweitere die Eingabeprüfung um eine Klassifikation:
    - Ist die Eingabe eine Frage?
    - Ist es ein Lösungsversuch (enthält Code)?
    - Enthält sie einen erkennbaren Denkfehler?
    Eingabe: text (str)
    Ausgabe: InputClassification (eigenes Modell)
    Akzeptanzkriterien: Alle drei Typen müssen erkannt werden.
"""

_MAX_LAENGE = 2000  # Zeichen
_VERBOTENE_MUSTER = [
    "api_key",
    "password",
    "passwort",
    "geheimnis",
    "token",
]


class EingabeFehler(ValueError):
    """Wird ausgelöst, wenn eine Eingabe die Sicherheitsprüfung nicht besteht."""


def pruefe_eingabe(text: str) -> str:
    """Prüft eine Benutzereingabe auf Sicherheitsprobleme.

    Args:
        text: Die Eingabe der lernenden Person.

    Returns:
        Die bereinigte Eingabe (getrimmt).

    Raises:
        EingabeFehler: Wenn die Eingabe nicht akzeptiert wird.
    """
    bereinigt = text.strip()

    if not bereinigt:
        raise EingabeFehler("Die Eingabe darf nicht leer sein.")

    if len(bereinigt) > _MAX_LAENGE:
        raise EingabeFehler(
            f"Die Eingabe ist zu lang (max. {_MAX_LAENGE} Zeichen)."
        )

    text_lower = bereinigt.lower()
    for muster in _VERBOTENE_MUSTER:
        if muster in text_lower:
            raise EingabeFehler(
                "Die Eingabe enthält sensible Inhalte. "
                "Bitte gib keine Zugangsdaten oder Schlüssel ein."
            )

    return bereinigt
