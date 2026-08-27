"""Lerninhalte laden: Lernmodule aus JSON-Dateien einlesen.

Lernmodule sind in JSON gespeichert und können wiederverwendet werden.
Das Format ist in courses/schemas/learning-module.schema.json definiert.

SCHÜLERAUFGABE (student_tasks/04-learning-content.md):
    Implementiere eine Validierungsfunktion, die prüft, ob ein geladenes
    Modul alle Pflichtfelder enthält und dem JSON-Schema entspricht.
    Eingabe: Modul-Dictionary aus JSON
    Ausgabe: LearningModule oder ValidationError
    Akzeptanzkriterien: Ungültige Module werden abgelehnt, gültige akzeptiert.
"""

import json
from pathlib import Path

from learning_agent.models import LearningModule


def lade_modul(pfad: Path) -> LearningModule:
    """Lädt ein Lernmodul aus einer JSON-Datei.

    Args:
        pfad: Pfad zur JSON-Datei des Lernmoduls.

    Returns:
        Das geladene ``LearningModule``.

    Raises:
        FileNotFoundError: Wenn die Datei nicht gefunden wird.
        ValueError: Wenn die Datei kein gültiges Lernmodul enthält.
    """
    if not pfad.exists():
        raise FileNotFoundError(f"Lernmodul nicht gefunden: {pfad}")

    with pfad.open(encoding="utf-8") as datei:
        daten = json.load(datei)

    return _parse_modul(daten)


def _parse_modul(daten: dict) -> LearningModule:
    """Wandelt ein Dictionary in ein LearningModule um.

    Args:
        daten: Rohdaten aus der JSON-Datei.

    Returns:
        Ein ``LearningModule``.

    Raises:
        ValueError: Wenn Pflichtfelder fehlen.
    """
    pflichtfelder = [
        "id", "titel", "fachgebiet", "thema", "niveau",
        "lernziele", "vorkenntnisse", "aufgabenstellung",
        "fehlvorstellungen", "hinweise", "reflexionsfrage", "transferaufgabe",
    ]

    fehlende = [f for f in pflichtfelder if f not in daten]
    if fehlende:
        raise ValueError(f"Pflichtfelder fehlen im Lernmodul: {fehlende}")

    # Hinweise: JSON-Schlüssel sind Strings, LearningModule erwartet int-Schlüssel
    hinweise_raw = daten["hinweise"]
    hinweise = {int(k): v for k, v in hinweise_raw.items()}

    return LearningModule(
        id=daten["id"],
        titel=daten["titel"],
        fachgebiet=daten["fachgebiet"],
        thema=daten["thema"],
        niveau=daten["niveau"],
        lernziele=daten["lernziele"],
        vorkenntnisse=daten["vorkenntnisse"],
        aufgabenstellung=daten["aufgabenstellung"],
        fehlvorstellungen=daten["fehlvorstellungen"],
        hinweise=hinweise,
        reflexionsfrage=daten["reflexionsfrage"],
        transferaufgabe=daten["transferaufgabe"],
        metadaten=daten.get("metadaten", {}),
    )
