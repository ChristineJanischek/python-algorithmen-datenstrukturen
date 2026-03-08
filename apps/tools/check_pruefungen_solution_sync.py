#!/usr/bin/env python3
"""Prueft die Konsistenz zwischen Klausur-Aufgaben und Musterloesungen.

Routine-Ziel:
- Bei Aenderungen in `Klausur_AuD_Musteraufgaben_VersionX.md` sicherstellen,
  dass die zugehoerige `Klausur_AuD_Musterloesungen_VersionX.md` konsistent ist.
- Als CI-Gate ausfuehren, um vergessene Loesungsupdates frueh zu blockieren.
 - Optional mit `--apply` relevante Loesungsabschnitte automatisch nachziehen.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
import hashlib


ROOT = Path(__file__).resolve().parents[2]
PRUEFUNGEN_DIR = ROOT / "docs" / "pruefungen"

# Erweiterbar: explizite Algorithmusbezeichnungen, die in Aufgabe-5-Analyseprompts
# ("Algorithmen pruefen") nicht genannt werden duerfen.
ALGORITHM_NAME_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bbina(?:e|ä)re\s+suche\b", re.IGNORECASE),
    re.compile(r"\blineare\s+suche\b", re.IGNORECASE),
    re.compile(r"\bbubble\s*sort\b", re.IGNORECASE),
    re.compile(r"\bselection\s*sort\b", re.IGNORECASE),
    re.compile(r"\binsertion\s*sort\b", re.IGNORECASE),
    re.compile(r"\bmerge\s*sort\b", re.IGNORECASE),
    re.compile(r"\bquick\s*sort\b", re.IGNORECASE),
    re.compile(r"\bheap\s*sort\b", re.IGNORECASE),
    re.compile(r"\bcounting\s*sort\b", re.IGNORECASE),
    re.compile(r"\bradix\s*sort\b", re.IGNORECASE),
)


@dataclass
class Section:
    nummer: int
    start: int
    end: int
    heading_line: str
    text: str


def _extract_sections(content: str) -> dict[int, Section]:
    header_pattern = re.compile(r"^###\s+(?:\*\*)?Aufgabe\s+(\d+)\b.*$", re.MULTILINE)
    matches = list(header_pattern.finditer(content))
    sections: dict[int, Section] = {}

    for idx, match in enumerate(matches):
        nummer = int(match.group(1))
        if nummer in sections:
            # Nur die erste (primäre) Aufgaben-Sektion verwenden.
            continue
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
        sections[nummer] = Section(
            nummer=nummer,
            start=start,
            end=end,
            heading_line=match.group(0).strip(),
            text=content[start:end],
        )

    return sections


def _extract_embed_svgs(section_text: str) -> list[str]:
    return re.findall(r"DOCX-EMBED-SVG:\s*([^\s]+)", section_text)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _normalize_heading(text: str) -> str:
    compact = text.replace("**", "")
    compact = re.sub(r"\s+", " ", compact).strip().lower()
    return compact


def _heading_from_aufgabe(heading_line: str) -> str:
    clean = re.sub(r"^###\s+", "", heading_line).strip().replace("**", "")
    return f"### {clean}"


def _extract_aufgabenstellung_lines(section_text: str) -> list[str]:
    lines = section_text.splitlines()
    if len(lines) <= 1:
        return []

    collected: list[str] = []
    for line in lines[1:]:
        stripped = line.strip()
        if re.match(r"^\*\*[a-z]\)", stripped, re.IGNORECASE):
            break
        if stripped.startswith("```"):
            break
        if stripped == "---":
            break
        collected.append(line.rstrip())

    while collected and not collected[0].strip():
        collected.pop(0)
    while collected and not collected[-1].strip():
        collected.pop()

    return [line.strip() for line in collected]


def _quote_lines(lines: list[str]) -> list[str]:
    return [">" if not line else f"> {line}" for line in lines]


def _normalize_quoted_lines(lines: list[str]) -> list[str]:
    normalized: list[str] = []
    for line in lines:
        content = re.sub(r"^>\s?", "", line.strip())
        if not content:
            continue
        normalized.append(re.sub(r"\s+", " ", content).strip())
    return normalized


def _find_solution_statement_block(lines: list[str]) -> tuple[int | None, int | None, int | None]:
    marker = "**Aufgabenstellung (aus Prüfungsblatt):**"
    marker_idx: int | None = None

    for idx, line in enumerate(lines):
        if line.strip() == marker:
            marker_idx = idx
            break

    if marker_idx is None:
        return None, None, None

    start = marker_idx + 1
    while start < len(lines) and not lines[start].lstrip().startswith(">") and not lines[start].strip():
        start += 1

    end = start
    while end < len(lines) and lines[end].lstrip().startswith(">"):
        end += 1

    return marker_idx, start, end


def _extract_task_prompt_lines(section_text: str) -> list[str]:
    """Extrahiert den Aufgabentext bis vor die erste Teilaufgabe (a/b/c)."""
    lines = section_text.splitlines()
    if len(lines) <= 1:
        return []

    collected: list[str] = []
    for line in lines[1:]:
        stripped = line.strip()
        if re.match(r"^\*\*[a-z]\)", stripped, re.IGNORECASE):
            break
        # Technische Referenzen sollen die didaktische Leak-Pruefung nicht beeinflussen.
        if stripped.startswith("![") or stripped.startswith("<!--"):
            continue
        collected.append(line.rstrip())

    return [line for line in collected if line.strip()]


def _is_algorithm_check_task(section: Section) -> bool:
    heading = section.heading_line.lower()
    text = section.text.lower()
    return "algorithmen prüfen" in heading or "algorithmen pruefen" in heading or "vermuteter zweck" in text


def _find_algorithm_name_leaks(section: Section) -> list[str]:
    """Findet explizite Algorithmusnamen im Aufgabentext von Analyseaufgaben."""
    if not _is_algorithm_check_task(section):
        return []

    prompt_text = "\n".join(_extract_task_prompt_lines(section.text))
    if not prompt_text:
        return []

    hits: list[str] = []
    for pattern in ALGORITHM_NAME_PATTERNS:
        match = pattern.search(prompt_text)
        if match:
            hits.append(match.group(0))
    return hits


def _normalized_task_text_for_dedup(section_text: str) -> str:
    """Normalisiert Aufgaben-Text fuer robuste Dublettenpruefung."""
    lines: list[str] = []
    for raw in section_text.splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        # Technische Referenzen nicht als inhaltlichen Unterschied zaehlen.
        if stripped.startswith("![") or stripped.startswith("<!--"):
            continue
        lines.append(re.sub(r"\s+", " ", stripped))
    return "\n".join(lines)


def check_no_duplicate_tasks(aufgaben_paths: list[Path]) -> list[str]:
    """Prueft, dass keine identische Aufgabe in mehreren Klausurdokumenten vorkommt."""
    errors: list[str] = []
    by_hash: dict[str, list[tuple[Path, int]]] = {}

    for aufgaben_path in aufgaben_paths:
        content = _read(aufgaben_path)
        sections = _extract_sections(content)
        for nummer, section in sections.items():
            normalized = _normalized_task_text_for_dedup(section.text)
            if not normalized:
                continue
            digest = hashlib.sha1(normalized.encode("utf-8")).hexdigest()
            by_hash.setdefault(digest, []).append((aufgaben_path, nummer))

    for occurences in by_hash.values():
        if len(occurences) <= 1:
            continue
        locations = ", ".join(f"{_display_path(path)}#Aufgabe{nummer}" for path, nummer in occurences)
        errors.append(
            "Doppelte Aufgabe erkannt (inhaltlich identisch in mehreren Musteraufgaben-Dateien): "
            f"{locations}"
        )

    return errors


def _sync_solution_section(aufgabe: Section, loesung: Section, errors: list[str], apply: bool) -> str:
    section_lines = loesung.text.splitlines()
    if not section_lines:
        errors.append(f"Aufgabe {aufgabe.nummer}: Leerer Abschnitt in Musterloesung.")
        return loesung.text

    changed = False
    expected_heading = _heading_from_aufgabe(aufgabe.heading_line)
    if _normalize_heading(section_lines[0]) != _normalize_heading(expected_heading):
        if apply:
            section_lines[0] = expected_heading
            changed = True
        else:
            errors.append(
                f"Aufgabe {aufgabe.nummer}: Ueberschrift weicht ab. Erwartet: '{expected_heading}'."
            )

    aufgabenstellung_lines = _extract_aufgabenstellung_lines(aufgabe.text)
    if not aufgabenstellung_lines:
        errors.append(
            f"Aufgabe {aufgabe.nummer}: Keine Aufgabenstellung im Aufgabenblatt extrahierbar."
        )
        return "\n".join(section_lines)

    expected_quote = _quote_lines(aufgabenstellung_lines)
    marker_idx, quote_start, quote_end = _find_solution_statement_block(section_lines)
    if marker_idx is None or quote_start is None or quote_end is None:
        errors.append(
            f"Aufgabe {aufgabe.nummer}: Marker '**Aufgabenstellung (aus Prüfungsblatt):**' fehlt in Musterloesung."
        )
        return "\n".join(section_lines)

    current_quote = section_lines[quote_start:quote_end]
    if _normalize_quoted_lines(current_quote) != _normalize_quoted_lines(expected_quote):
        if apply:
            section_lines[quote_start:quote_end] = expected_quote
            changed = True
        else:
            errors.append(
                f"Aufgabe {aufgabe.nummer}: Aufgabenstellung im Loesungsdokument ist nicht mehr synchron."
            )

    updated = "\n".join(section_lines)
    if loesung.text.endswith("\n"):
        updated += "\n"
    return updated if changed else loesung.text


def check_pair(
    aufgaben_path: Path,
    loesung_path: Path,
    apply: bool = False,
    enforce_text_sync: bool = False,
) -> list[str]:
    errors: list[str] = []

    aufgaben_content = _read(aufgaben_path)
    loesung_content = _read(loesung_path)

    aufgaben_sections = _extract_sections(aufgaben_content)
    loesung_sections = _extract_sections(loesung_content)

    # Legacy-Dateien ohne strukturierte Abschnittsueberschriften werden nicht hart geblockt.
    if not aufgaben_sections or not loesung_sections:
        return errors

    # Legacy-Loesungsdateien ohne Aufgabenstellungs-Marker werden im Standardmodus
    # weiterhin tolerant behandelt, damit bestehende Altversionen CI nicht blockieren.
    if not (apply or enforce_text_sync):
        if "**Aufgabenstellung (aus Prüfungsblatt):**" not in loesung_content:
            return errors

    updated_sections: dict[int, str] = {}

    for nummer, aufgabe in aufgaben_sections.items():
        leaked_names = _find_algorithm_name_leaks(aufgabe)
        if leaked_names:
            joined = ", ".join(sorted(set(leaked_names), key=str.lower))
            errors.append(
                f"{_display_path(aufgaben_path)}: Aufgabe {nummer} verraet den Algorithmus in der Aufgabenstellung ({joined})."
            )

        if nummer not in loesung_sections:
            errors.append(
                f"{_display_path(loesung_path)}: Aufgabe {nummer} fehlt (existiert in {aufgaben_path.name})."
            )
            continue

        loesung = loesung_sections[nummer]

        if apply or enforce_text_sync:
            section_errors: list[str] = []
            updated_sections[nummer] = _sync_solution_section(aufgabe, loesung, section_errors, apply)
            for err in section_errors:
                errors.append(f"{_display_path(loesung_path)}: {err}")

        # 1) Diagramm-Referenzen muessen in der Loesung ebenfalls auftauchen.
        for svg_ref in _extract_embed_svgs(aufgabe.text):
            if svg_ref not in loesung.text:
                errors.append(
                    f"{_display_path(loesung_path)}: Aufgabe {nummer} referenziert Diagramm nicht: {svg_ref}"
                )

    if apply and not errors:
        new_content = loesung_content
        changed = False
        for nummer, section in sorted(loesung_sections.items(), key=lambda item: item[1].start, reverse=True):
            replacement = updated_sections.get(nummer, section.text)
            if replacement != section.text:
                changed = True
                new_content = new_content[: section.start] + replacement + new_content[section.end :]

        if changed:
            _write(loesung_path, new_content)
            print(f"🔧 Aktualisiert: {_display_path(loesung_path)}")

    return errors


def find_pairs(version: str | None = None) -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    pattern = (
        f"Klausur_AuD_Musteraufgaben_Version{version}.md"
        if version is not None
        else "Klausur_AuD_Musteraufgaben_Version*.md"
    )
    for aufgaben_path in sorted(PRUEFUNGEN_DIR.glob(pattern)):
        version = aufgaben_path.stem.replace("Klausur_AuD_Musteraufgaben_", "")
        loesung_path = PRUEFUNGEN_DIR / f"Klausur_AuD_Musterloesungen_{version}.md"
        if loesung_path.exists():
            pairs.append((aufgaben_path, loesung_path))
    return pairs


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prueft die Konsistenz zwischen Klausur-Aufgaben und Musterloesungen "
            "und kann mit --apply Loesungsabschnitte automatisch synchronisieren."
        )
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Synchronisiert Ueberschriften und Aufgabenstellung im Loesungsdokument automatisch.",
    )
    parser.add_argument(
        "--strict-task-sync",
        action="store_true",
        help=(
            "Prueft zusaetzlich, ob Ueberschriften und Aufgabenstellung in der Musterloesung "
            "mit dem Aufgabenblatt synchron sind."
        ),
    )
    parser.add_argument(
        "--version",
        type=str,
        default=None,
        help="Optional nur ein Versionspaar pruefen (z. B. 3).",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    all_errors: list[str] = []
    pairs = find_pairs(version=args.version)

    if not pairs:
        print("⚠️ Keine Aufgaben/Loesungs-Paare gefunden.")
        return 0

    aufgaben_paths = [aufgaben_path for aufgaben_path, _ in pairs]
    all_errors.extend(check_no_duplicate_tasks(aufgaben_paths))

    for aufgaben_path, loesung_path in pairs:
        all_errors.extend(
            check_pair(
                aufgaben_path,
                loesung_path,
                apply=args.apply,
                enforce_text_sync=args.strict_task_sync,
            )
        )

    if all_errors:
        print("❌ Aufgaben/Loesungs-Sync fehlgeschlagen:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    if args.apply:
        print("✅ Aufgaben/Loesungs-Sync ist konsistent (Auto-Sync aktiviert).")
    else:
        print("✅ Aufgaben/Loesungs-Sync ist konsistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
