"""
Utilities für die Namenskonvention von Prüfungsdateien.

Zielschema:
    Klausur_<Thema>_<Musteraufgaben|Musterloesungen>_VersionX.md

Thema:
    GdP | AuD | RDB | GA
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


KONFORM_REGEX = re.compile(
    r"^Klausur_(GdP|AuD|RDB|GA)_(Musteraufgaben|Musterloesungen)_Version([1-9][0-9]*)\.md$"
)

ERLAUBTE_THEMEN = ("GdP", "AuD", "RDB", "GA")
ERLAUBTE_TYPEN = ("Musteraufgaben", "Musterloesungen")


@dataclass(frozen=True)
class PruefungsDateiBefund:
    """Analyse-Ergebnis für eine einzelne Prüfungsdatei."""

    datei: Path
    ist_konform: bool
    vorgeschlagener_name: str
    grund: str


@dataclass(frozen=True)
class Umbenennung:
    """Repräsentiert eine konkrete Umbenennung."""

    quelle: Path
    ziel: Path


@dataclass(frozen=True)
class NormalisierungsErgebnis:
    """Gesamtergebnis einer Namens-Normalisierung."""

    geprueft: int
    konform: int
    umbenennungen: tuple[Umbenennung, ...]
    befunde: tuple[PruefungsDateiBefund, ...]


def ist_konformer_dateiname(dateiname: str) -> bool:
    """Prüft, ob der Dateiname exakt dem Zielschema entspricht."""

    return bool(KONFORM_REGEX.fullmatch(dateiname))


def analysiere_pruefungsdatei(datei: Path) -> PruefungsDateiBefund:
    """
    Analysiert eine Prüfungsdatei und liefert den Soll-Dateinamen.

    Args:
        datei: Absoluter oder relativer Dateipfad.

    Returns:
        Analyse-Befund mit Konformität und Namensvorschlag.
    """

    aktueller_name = datei.name
    if ist_konformer_dateiname(aktueller_name):
        return PruefungsDateiBefund(
            datei=datei,
            ist_konform=True,
            vorgeschlagener_name=aktueller_name,
            grund="bereits konform",
        )

    dateiname_ohne_ext = datei.stem
    typ = _ermittle_typ(dateiname_ohne_ext)
    thema = _ermittle_thema(dateiname_ohne_ext)
    version = _ermittle_version(dateiname_ohne_ext)

    vorgeschlagener_name = f"Klausur_{thema}_{typ}_Version{version}.md"
    return PruefungsDateiBefund(
        datei=datei,
        ist_konform=False,
        vorgeschlagener_name=vorgeschlagener_name,
        grund="nicht im Zielschema",
    )


def normalisiere_pruefungsdateien(
    basis_verzeichnis: Path,
    dry_run: bool = True,
) -> NormalisierungsErgebnis:
    """
    Normalisiert alle Klausur-Dateinamen unterhalb eines Verzeichnisses.

    Die Routine ist konfliktfrei und vergibt bei Namenskollisionen
    automatisch die nächste freie Versionsnummer.

    Args:
        basis_verzeichnis: Startpfad für die rekursive Suche.
        dry_run: Wenn True, nur Analyse; wenn False, echte Umbenennung.

    Returns:
        Aggregiertes Ergebnis inkl. Umbenennungen.
    """

    dateien = _finde_klausur_markdown_dateien(basis_verzeichnis)
    befunde: list[PruefungsDateiBefund] = []
    umbenennungen: list[Umbenennung] = []

    gruppiert = _gruppiere_nach_ordner(dateien)
    for ordner, ordner_dateien in gruppiert.items():
        belegte_namen = {pfad.name for pfad in ordner_dateien}

        for datei in sorted(ordner_dateien, key=lambda p: p.name):
            befund = analysiere_pruefungsdatei(datei)

            if befund.ist_konform:
                befunde.append(befund)
                continue

            ziel_name = _finde_kollisionsfreien_zielnamen(
                vorgeschlagener_name=befund.vorgeschlagener_name,
                belegte_namen=belegte_namen,
            )
            ziel_pfad = ordner / ziel_name

            belegte_namen.discard(datei.name)
            belegte_namen.add(ziel_name)

            finaler_befund = PruefungsDateiBefund(
                datei=datei,
                ist_konform=False,
                vorgeschlagener_name=ziel_name,
                grund=befund.grund,
            )
            befunde.append(finaler_befund)
            umbenennungen.append(Umbenennung(quelle=datei, ziel=ziel_pfad))

    if not dry_run:
        for umbenennung in umbenennungen:
            if umbenennung.quelle != umbenennung.ziel:
                umbenennung.quelle.rename(umbenennung.ziel)

    konforme = sum(1 for befund in befunde if befund.ist_konform)
    return NormalisierungsErgebnis(
        geprueft=len(dateien),
        konform=konforme,
        umbenennungen=tuple(umbenennungen),
        befunde=tuple(befunde),
    )


def _finde_klausur_markdown_dateien(basis_verzeichnis: Path) -> list[Path]:
    """Sucht rekursiv nach potenziellen Klausur-Markdown-Dateien."""

    return [
        pfad
        for pfad in basis_verzeichnis.rglob("*.md")
        if "klausur" in pfad.name.lower()
    ]


def _gruppiere_nach_ordner(dateien: Iterable[Path]) -> dict[Path, list[Path]]:
    """Gruppiert Dateien nach Parent-Verzeichnis."""

    gruppiert: dict[Path, list[Path]] = {}
    for datei in dateien:
        gruppiert.setdefault(datei.parent, []).append(datei)
    return gruppiert


def _ermittle_typ(dateiname_ohne_ext: str) -> str:
    """Leitet den Typ (Musteraufgaben/Musterloesungen) aus dem Namen ab."""

    name_klein = dateiname_ohne_ext.lower()
    if "musterloesung" in name_klein or "musterlösung" in name_klein:
        return "Musterloesungen"
    if "musteraufgabe" in name_klein:
        return "Musteraufgaben"
    return "Musteraufgaben"


def _ermittle_thema(dateiname_ohne_ext: str) -> str:
    """Leitet den Themen-Code aus dem Dateinamen ab (heuristisch, erweiterbar)."""

    name = dateiname_ohne_ext
    name_klein = name.lower()

    for thema in ERLAUBTE_THEMEN:
        if f"_{thema.lower()}_" in f"_{name_klein}_":
            return thema

    regeln = (
        (r"(rdb|datenbank|sql|relation)", "RDB"),
        (r"((^|_)ga(_|$)|gesellschaft|ethik|datenschutz|recht)", "GA"),
        (r"(aud|algorithm|sort|suche|array|liste|bubble|selection|l2_2|l2_3)", "AuD"),
        (r"(gdp|grundlagen|programmierung|l1_|l2_1)", "GdP"),
    )

    for muster, thema in regeln:
        if re.search(muster, name_klein):
            return thema

    return "GdP"


def _ermittle_version(dateiname_ohne_ext: str) -> int:
    """Leitet die Version aus vorhandenem Namen ab."""

    match_version = re.search(r"Version([1-9][0-9]*)", dateiname_ohne_ext, flags=re.IGNORECASE)
    if match_version:
        return int(match_version.group(1))

    match_variante = re.search(r"Variante[_\s-]*([A-Z])", dateiname_ohne_ext, flags=re.IGNORECASE)
    if match_variante:
        buchstabe = match_variante.group(1).upper()
        if "A" <= buchstabe <= "Z":
            return 2 + (ord(buchstabe) - ord("A"))

    return 1


def _finde_kollisionsfreien_zielnamen(
    vorgeschlagener_name: str,
    belegte_namen: set[str],
) -> str:
    """Erhöht Version automatisch, bis ein freier Name gefunden wurde."""

    if vorgeschlagener_name not in belegte_namen:
        return vorgeschlagener_name

    match = re.match(
        r"^(Klausur_(?:GdP|AuD|RDB|GA)_(?:Musteraufgaben|Musterloesungen)_Version)([1-9][0-9]*)(\.md)$",
        vorgeschlagener_name,
    )
    if not match:
        raise ValueError(f"Ungültiger vorgeschlagener Name: {vorgeschlagener_name}")

    praefix, version_text, suffix = match.groups()
    version = int(version_text)

    while True:
        version += 1
        kandidat = f"{praefix}{version}{suffix}"
        if kandidat not in belegte_namen:
            return kandidat
