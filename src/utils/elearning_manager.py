"""
E-Learning Content Manager für Baden-Württemberg Abitur Materialien

Automatisches Erstellen, Validieren und Verwalten von E-Learning-Inhalten
in strukturierten Markdown-Dateien.

Autor: Erstellt für python-algorithmen-datenstrukturen
Version: 1.0
Datum: 05.02.2026
"""

import os
import re
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path


class ContentType(Enum):
    """Typ des E-Learning-Inhalts"""
    AUFGABE = "aufgaben"
    INFORMATION = "information"
    LOESUNG = "loesungen"


class Level(Enum):
    """Schwierigkeitsgrad nach Repository-Standard"""
    L1 = "L1"  # Grundlagen
    L2 = "L2"  # Fortgeschritten
    L3 = "L3"  # Expert


@dataclass
class ELearningMetadata:
    """Metadaten für E-Learning-Inhalte"""
    titel: str
    level: Level
    kategorie: int  # 1=Grundlagen, 2=Sortieren, 3=Suchen, 4=Vertiefung, etc.
    nummer: int
    autor: str = "Unbekannt"
    datum: str = field(default_factory=lambda: datetime.now().strftime("%d.%m.%Y"))
    version: str = "1.0"
    themen: List[str] = field(default_factory=list)
    lernziele: List[str] = field(default_factory=list)
    voraussetzungen: List[str] = field(default_factory=list)
    zeitaufwand: Optional[str] = None
    schwierigkeitsgrad: Optional[str] = None
    
    def to_filename(self, content_type: ContentType) -> str:
        """
        Generiert den Dateinamen nach Namenskonvention.
        
        Format: LX_Y_Z_Thema.md
        X = Level (1-3)
        Y = Kategorie
        Z = Nummer
        
        Returns:
            Dateiname als String
        """
        # Titel für Dateinamen bereinigen
        clean_title = re.sub(r'[^a-zA-ZäöüÄÖÜß0-9_-]', '_', self.titel)
        clean_title = re.sub(r'_+', '_', clean_title).strip('_')
        
        return f"{self.level.value}_{self.kategorie}_{self.nummer}_{clean_title}.md"
    
    def to_frontmatter(self) -> str:
        """
        Generiert YAML-Frontmatter für Markdown-Dateien.
        
        Returns:
            Frontmatter als String
        """
        lines = [
            "---",
            f"titel: \"{self.titel}\"",
            f"level: {self.level.value}",
            f"kategorie: {self.kategorie}",
            f"nummer: {self.nummer}",
            f"autor: \"{self.autor}\"",
            f"datum: {self.datum}",
            f"version: {self.version}"
        ]
        
        if self.themen:
            lines.append("themen:")
            for thema in self.themen:
                lines.append(f"  - {thema}")
        
        if self.lernziele:
            lines.append("lernziele:")
            for ziel in self.lernziele:
                lines.append(f"  - {ziel}")
        
        if self.voraussetzungen:
            lines.append("voraussetzungen:")
            for voraus in self.voraussetzungen:
                lines.append(f"  - {voraus}")
        
        if self.zeitaufwand:
            lines.append(f"zeitaufwand: \"{self.zeitaufwand}\"")
        
        if self.schwierigkeitsgrad:
            lines.append(f"schwierigkeitsgrad: \"{self.schwierigkeitsgrad}\"")
        
        lines.append("---")
        lines.append("")
        
        return "\n".join(lines)


@dataclass
class ELearningAufgabe:
    """Struktur einer E-Learning-Aufgabe"""
    metadata: ELearningMetadata
    problemstellung: str
    struktogramm: Optional[str] = None
    hinweise: Optional[str] = None
    beispiel_eingabe: Optional[str] = None
    beispiel_ausgabe: Optional[str] = None
    testfaelle: List[Tuple[str, str]] = field(default_factory=list)
    zusatzaufgaben: List[str] = field(default_factory=list)
    
    def to_markdown(self) -> str:
        """
        Generiert vollständiges Markdown für die Aufgabe.
        
        Returns:
            Markdown-String
        """
        md = []
        md.append(self.metadata.to_frontmatter())
        md.append(f"# Aufgabe: {self.metadata.titel}")
        md.append("")
        
        # Metadaten-Box
        md.append("## 📋 Übersicht")
        md.append("")
        md.append(f"- **Level:** {self.metadata.level.value}")
        md.append(f"- **Kategorie:** {self.metadata.kategorie}")
        if self.metadata.zeitaufwand:
            md.append(f"- **Zeitaufwand:** {self.metadata.zeitaufwand}")
        if self.metadata.schwierigkeitsgrad:
            md.append(f"- **Schwierigkeitsgrad:** {self.metadata.schwierigkeitsgrad}")
        md.append("")
        
        if self.metadata.themen:
            md.append("**Themen:**")
            for thema in self.metadata.themen:
                md.append(f"- {thema}")
            md.append("")
        
        if self.metadata.lernziele:
            md.append("**Lernziele:**")
            for ziel in self.metadata.lernziele:
                md.append(f"- {ziel}")
            md.append("")
        
        if self.metadata.voraussetzungen:
            md.append("**Voraussetzungen:**")
            for voraus in self.metadata.voraussetzungen:
                md.append(f"- {voraus}")
            md.append("")
        
        # Problemstellung
        md.append("## 📝 Problemstellung")
        md.append("")
        md.append(self.problemstellung)
        md.append("")
        
        # Struktogramm
        if self.struktogramm:
            md.append("## 📊 Struktogramm")
            md.append("")
            md.append("```")
            md.append(self.struktogramm)
            md.append("```")
            md.append("")
        
        # Hinweise
        if self.hinweise:
            md.append("## 💡 Hinweise")
            md.append("")
            md.append(self.hinweise)
            md.append("")
        
        # Beispiele
        if self.beispiel_eingabe or self.beispiel_ausgabe:
            md.append("## 🧪 Beispiel")
            md.append("")
            if self.beispiel_eingabe:
                md.append("**Eingabe:**")
                md.append("```")
                md.append(self.beispiel_eingabe)
                md.append("```")
                md.append("")
            if self.beispiel_ausgabe:
                md.append("**Erwartete Ausgabe:**")
                md.append("```")
                md.append(self.beispiel_ausgabe)
                md.append("```")
                md.append("")
        
        # Testfälle
        if self.testfaelle:
            md.append("## ✅ Testfälle")
            md.append("")
            for i, (eingabe, ausgabe) in enumerate(self.testfaelle, 1):
                md.append(f"### Test {i}")
                md.append("")
                md.append("**Eingabe:**")
                md.append("```")
                md.append(eingabe)
                md.append("```")
                md.append("")
                md.append("**Ausgabe:**")
                md.append("```")
                md.append(ausgabe)
                md.append("```")
                md.append("")
        
        # Zusatzaufgaben
        if self.zusatzaufgaben:
            md.append("## 🔥 Zusatzaufgaben")
            md.append("")
            for i, zusatz in enumerate(self.zusatzaufgaben, 1):
                md.append(f"{i}. {zusatz}")
            md.append("")
        
        # Footer
        md.append("---")
        md.append("")
        md.append(f"*Erstellt am {self.metadata.datum} von {self.metadata.autor}*")
        md.append("")
        
        return "\n".join(md)


@dataclass
class ELearningInformation:
    """Struktur einer E-Learning-Information"""
    metadata: ELearningMetadata
    einfuehrung: str
    inhalt: str
    beispiele: Optional[str] = None
    zusammenfassung: Optional[str] = None
    weiterführende_themen: List[str] = field(default_factory=list)
    ressourcen: List[Tuple[str, str]] = field(default_factory=list)  # (Titel, Link/Pfad)
    
    def to_markdown(self) -> str:
        """
        Generiert vollständiges Markdown für die Information.
        
        Returns:
            Markdown-String
        """
        md = []
        md.append(self.metadata.to_frontmatter())
        md.append(f"# Information: {self.metadata.titel}")
        md.append("")
        
        # Metadaten-Box
        md.append("## 📚 Übersicht")
        md.append("")
        md.append(f"- **Level:** {self.metadata.level.value}")
        md.append(f"- **Kategorie:** {self.metadata.kategorie}")
        if self.metadata.zeitaufwand:
            md.append(f"- **Lesezeit:** {self.metadata.zeitaufwand}")
        md.append("")
        
        if self.metadata.themen:
            md.append("**Themen:**")
            for thema in self.metadata.themen:
                md.append(f"- {thema}")
            md.append("")
        
        if self.metadata.voraussetzungen:
            md.append("**Voraussetzungen:**")
            for voraus in self.metadata.voraussetzungen:
                md.append(f"- {voraus}")
            md.append("")
        
        # Einführung
        md.append("## 🎯 Einführung")
        md.append("")
        md.append(self.einfuehrung)
        md.append("")
        
        # Hauptinhalt
        md.append("## 📖 Inhalt")
        md.append("")
        md.append(self.inhalt)
        md.append("")
        
        # Beispiele
        if self.beispiele:
            md.append("## 💡 Beispiele")
            md.append("")
            md.append(self.beispiele)
            md.append("")
        
        # Zusammenfassung
        if self.zusammenfassung:
            md.append("## 📝 Zusammenfassung")
            md.append("")
            md.append(self.zusammenfassung)
            md.append("")
        
        # Weiterführende Themen
        if self.weiterführende_themen:
            md.append("## 🔗 Weiterführende Themen")
            md.append("")
            for thema in self.weiterführende_themen:
                md.append(f"- {thema}")
            md.append("")
        
        # Ressourcen
        if self.ressourcen:
            md.append("## 📚 Ressourcen")
            md.append("")
            for titel, link in self.ressourcen:
                md.append(f"- [{titel}]({link})")
            md.append("")
        
        # Footer
        md.append("---")
        md.append("")
        md.append(f"*Erstellt am {self.metadata.datum} von {self.metadata.autor}*")
        md.append("")
        
        return "\n".join(md)


@dataclass
class ELearningLoesung:
    """Struktur einer E-Learning-Lösung"""
    metadata: ELearningMetadata
    loesungsansatz: str
    struktogramm: Optional[str] = None
    python_code: Optional[str] = None
    erklaerung: Optional[str] = None
    komplexitaet: Optional[str] = None
    alternative_loesungen: List[Tuple[str, str]] = field(default_factory=list)  # (Titel, Code)
    hinweise: Optional[str] = None
    
    def to_markdown(self) -> str:
        """
        Generiert vollständiges Markdown für die Lösung.
        
        Returns:
            Markdown-String
        """
        md = []
        md.append(self.metadata.to_frontmatter())
        md.append(f"# Lösung: {self.metadata.titel}")
        md.append("")
        
        # Metadaten-Box
        md.append("## 📋 Übersicht")
        md.append("")
        md.append(f"- **Level:** {self.metadata.level.value}")
        md.append(f"- **Kategorie:** {self.metadata.kategorie}")
        if self.komplexitaet:
            md.append(f"- **Komplexität:** {self.komplexitaet}")
        md.append("")
        
        # Lösungsansatz
        md.append("## 💡 Lösungsansatz")
        md.append("")
        md.append(self.loesungsansatz)
        md.append("")
        
        # Struktogramm
        if self.struktogramm:
            md.append("## 📊 Struktogramm")
            md.append("")
            md.append("```")
            md.append(self.struktogramm)
            md.append("```")
            md.append("")
        
        # Python-Code
        if self.python_code:
            md.append("## 💻 Python-Implementierung")
            md.append("")
            md.append("```python")
            md.append(self.python_code)
            md.append("```")
            md.append("")
        
        # Erklärung
        if self.erklaerung:
            md.append("## 📝 Erklärung")
            md.append("")
            md.append(self.erklaerung)
            md.append("")
        
        # Komplexität
        if self.komplexitaet:
            md.append("## ⏱️ Komplexitätsanalyse")
            md.append("")
            md.append(self.komplexitaet)
            md.append("")
        
        # Alternative Lösungen
        if self.alternative_loesungen:
            md.append("## 🔄 Alternative Lösungen")
            md.append("")
            for i, (titel, code) in enumerate(self.alternative_loesungen, 1):
                md.append(f"### Alternative {i}: {titel}")
                md.append("")
                md.append("```python")
                md.append(code)
                md.append("```")
                md.append("")
        
        # Hinweise
        if self.hinweise:
            md.append("## 💡 Zusätzliche Hinweise")
            md.append("")
            md.append(self.hinweise)
            md.append("")
        
        # Footer
        md.append("---")
        md.append("")
        md.append(f"*Erstellt am {self.metadata.datum} von {self.metadata.autor}*")
        md.append("")
        
        return "\n".join(md)


class ELearningManager:
    """Manager für E-Learning-Content"""
    
    def __init__(self, base_path: str = "/workspaces/python-algorithmen-datenstrukturen"):
        """
        Initialisiert den ELearning-Manager.
        
        Args:
            base_path: Basis-Pfad des Repositories
        """
        self.base_path = Path(base_path)
        self.docs_path = self.base_path / "docs"
        
        # Sicherstellen, dass Verzeichnisse existieren
        for content_type in ContentType:
            path = self.docs_path / content_type.value
            path.mkdir(parents=True, exist_ok=True)
    
    def _get_target_path(self, metadata: ELearningMetadata, content_type: ContentType) -> Path:
        """
        Ermittelt den Ziel-Pfad für eine Datei.
        
        Args:
            metadata: Metadaten des Inhalts
            content_type: Typ des Inhalts
            
        Returns:
            Pfad zur Zieldatei
        """
        # Level-Unterordner erstellen
        level_dir = self.docs_path / content_type.value / metadata.level.value
        level_dir.mkdir(parents=True, exist_ok=True)
        
        # Dateiname generieren
        filename = metadata.to_filename(content_type)
        
        return level_dir / filename
    
    def save_aufgabe(self, aufgabe: ELearningAufgabe) -> Path:
        """
        Speichert eine Aufgabe als Markdown-Datei.
        
        Args:
            aufgabe: Die zu speichernde Aufgabe
            
        Returns:
            Pfad zur gespeicherten Datei
        """
        target_path = self._get_target_path(aufgabe.metadata, ContentType.AUFGABE)
        markdown = aufgabe.to_markdown()
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"✅ Aufgabe gespeichert: {target_path}")
        return target_path
    
    def save_information(self, info: ELearningInformation) -> Path:
        """
        Speichert eine Information als Markdown-Datei.
        
        Args:
            info: Die zu speichernde Information
            
        Returns:
            Pfad zur gespeicherten Datei
        """
        target_path = self._get_target_path(info.metadata, ContentType.INFORMATION)
        markdown = info.to_markdown()
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"✅ Information gespeichert: {target_path}")
        return target_path
    
    def save_loesung(self, loesung: ELearningLoesung) -> Path:
        """
        Speichert eine Lösung als Markdown-Datei.
        
        Args:
            loesung: Die zu speichernde Lösung
            
        Returns:
            Pfad zur gespeicherten Datei
        """
        target_path = self._get_target_path(loesung.metadata, ContentType.LOESUNG)
        markdown = loesung.to_markdown()
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"✅ Lösung gespeichert: {target_path}")
        return target_path
    
    def generate_index(self, content_type: ContentType, level: Optional[Level] = None) -> Path:
        """
        Generiert eine INDEX.md-Datei für einen Content-Typ.
        
        Args:
            content_type: Typ des Inhalts
            level: Optional spezifisches Level
            
        Returns:
            Pfad zur INDEX-Datei
        """
        base_dir = self.docs_path / content_type.value
        
        if level:
            target_dir = base_dir / level.value
            index_path = target_dir / "INDEX.md"
            md_files = list(target_dir.glob("*.md"))
            title = f"{content_type.value.capitalize()} - {level.value}"
        else:
            index_path = base_dir / "INDEX.md"
            md_files = []
            for lvl in Level:
                lvl_dir = base_dir / lvl.value
                if lvl_dir.exists():
                    md_files.extend(lvl_dir.glob("*.md"))
            title = f"{content_type.value.capitalize()} - Alle Level"
        
        # INDEX-Dateien selbst ausschließen
        md_files = [f for f in md_files if f.name != "INDEX.md"]
        md_files.sort()
        
        # Markdown generieren
        md = []
        md.append(f"# {title}")
        md.append("")
        md.append(f"*Automatisch generiert am {datetime.now().strftime('%d.%m.%Y %H:%M')}*")
        md.append("")
        md.append(f"**Anzahl Dateien:** {len(md_files)}")
        md.append("")
        
        # Nach Level gruppieren
        by_level = {}
        for file in md_files:
            file_level = file.parent.name if file.parent.name.startswith('L') else "Unbekannt"
            if file_level not in by_level:
                by_level[file_level] = []
            by_level[file_level].append(file)
        
        for lvl in sorted(by_level.keys()):
            md.append(f"## {lvl}")
            md.append("")
            for file in sorted(by_level[lvl]):
                # Relativen Pfad berechnen
                rel_path = file.relative_to(index_path.parent)
                # Titel aus Dateinamen extrahieren
                name = file.stem
                md.append(f"- [{name}]({rel_path})")
            md.append("")
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md))
        
        print(f"✅ Index generiert: {index_path}")
        return index_path
    
    def generate_all_indices(self) -> List[Path]:
        """
        Generiert alle INDEX-Dateien.
        
        Returns:
            Liste der generierten Index-Pfade
        """
        indices = []
        
        for content_type in ContentType:
            # Haupt-Index
            indices.append(self.generate_index(content_type))
            
            # Level-spezifische Indices
            for level in Level:
                level_dir = self.docs_path / content_type.value / level.value
                if level_dir.exists() and any(level_dir.glob("*.md")):
                    indices.append(self.generate_index(content_type, level))
        
        return indices
    
    def validate_content(self, file_path: Path) -> List[str]:
        """
        Validiert eine Content-Datei.
        
        Args:
            file_path: Pfad zur zu validierenden Datei
            
        Returns:
            Liste von Fehlermeldungen (leer wenn OK)
        """
        errors = []
        
        if not file_path.exists():
            errors.append(f"Datei existiert nicht: {file_path}")
            return errors
        
        content = file_path.read_text(encoding='utf-8')
        
        # Prüfe Frontmatter
        if not content.startswith("---"):
            errors.append("Fehlende YAML-Frontmatter")
        
        # Prüfe Dateinamen-Konvention
        pattern = r'^L[123]_\d+_\d+_.+\.md$'
        if not re.match(pattern, file_path.name):
            errors.append(f"Dateiname entspricht nicht der Konvention: {file_path.name}")
        
        # Struktogramm-Validierung
        errors.extend(self.validate_struktogramm_usage(file_path))
        
        return errors
    
    def validate_struktogramm_usage(self, file_path: Path) -> List[str]:
        """
        Validiert, dass Programmlogik mit grafischen Struktogrammen erklärt wird.
        
        Args:
            file_path: Pfah zur zu validierenden Datei
            
        Returns:
            Liste von Warnungen/Fehlern
        """
        warnings = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except:
            return warnings
        
        # Erkenne Content-Typ basierend auf Pfad
        path_str = str(file_path)
        is_solution = "loesungen" in path_str
        is_exam = "pruefungen" in path_str
        
        if is_solution:
            # Für Lösungen: Prüfe auf Python-Code NACH Struktogramm
            python_blocks = re.finditer(r'```python\n(.*?)\n```', content, re.DOTALL)
            
            for match in python_blocks:
                # Finde die Position des Python-Blocks
                pos = match.start()
                content_before = content[:pos]
                
                # Prüfe ob davor ein grafisches Struktogramm ist
                has_graphic = any(char in content_before for char in ['┌', '├', '└', '│', '─'])
                has_struktogramm_heading = "Struktogramm" in content_before.split('\n')[-20:]
                
                if not (has_graphic or has_struktogramm_heading):
                    warnings.append(
                        f"⚠️  Python-Code ohne vorhergehendes grafisches Struktogramm "
                        f"(Zeile ~{content[:pos].count(chr(10))})"
                    )
        
        elif is_exam:
            # Für Prüfungen: Prüfe auf Python-Code mit Struktogramm-Kontext
            textual_struktogramms = re.finditer(r'```struktogramm\n', content)
            graphic_blocks = re.finditer(r'┌', content)
            
            python_blocks = list(re.finditer(r'```python\n', content))
            graphic_positions = [m.start() for m in graphic_blocks]
            
            for python_match in python_blocks:
                pos = python_match.start()
                
                # Prüfe ob davor ein grafisches Struktogramm ist
                has_graphic_before = any(
                    graphic_pos < pos
                    for graphic_pos in graphic_positions
                    if pos - 500 < graphic_pos < pos  # Innerhalb 500 Zeichen davor
                )
                
                if not has_graphic_before:
                    line_num = content[:pos].count('\n') + 1
                    warnings.append(
                        f"⚠️  Python-Code ohne grafisches Struktogramm (Zeile {line_num})"
                    )
        
        return warnings



# Hilfs-Funktionen für schnelle Content-Erstellung

def create_aufgabe_quick(
    titel: str,
    level: Level,
    kategorie: int,
    nummer: int,
    problemstellung: str,
    autor: str = "Unbekannt",
    struktogramm: Optional[str] = None
) -> ELearningAufgabe:
    """
    Schnell-Erstellung einer Aufgabe mit Mindestangaben.
    
    Returns:
        ELearningAufgabe-Objekt
    """
    metadata = ELearningMetadata(
        titel=titel,
        level=level,
        kategorie=kategorie,
        nummer=nummer,
        autor=autor
    )
    
    return ELearningAufgabe(
        metadata=metadata,
        problemstellung=problemstellung,
        struktogramm=struktogramm
    )


def create_information_quick(
    titel: str,
    level: Level,
    kategorie: int,
    nummer: int,
    einfuehrung: str,
    inhalt: str,
    autor: str = "Unbekannt"
) -> ELearningInformation:
    """
    Schnell-Erstellung einer Information mit Mindestangaben.
    
    Returns:
        ELearningInformation-Objekt
    """
    metadata = ELearningMetadata(
        titel=titel,
        level=level,
        kategorie=kategorie,
        nummer=nummer,
        autor=autor
    )
    
    return ELearningInformation(
        metadata=metadata,
        einfuehrung=einfuehrung,
        inhalt=inhalt
    )


def create_loesung_quick(
    titel: str,
    level: Level,
    kategorie: int,
    nummer: int,
    loesungsansatz: str,
    python_code: str,
    autor: str = "Unbekannt",
    struktogramm: Optional[str] = None
) -> ELearningLoesung:
    """
    Schnell-Erstellung einer Lösung mit Mindestangaben.
    
    Returns:
        ELearningLoesung-Objekt
    """
    metadata = ELearningMetadata(
        titel=titel,
        level=level,
        kategorie=kategorie,
        nummer=nummer,
        autor=autor
    )
    
    return ELearningLoesung(
        metadata=metadata,
        loesungsansatz=loesungsansatz,
        struktogramm=struktogramm,
        python_code=python_code
    )


# Beispiel-Verwendung
if __name__ == "__main__":
    print("=== E-Learning Manager Demo ===\n")
    
    # Manager initialisieren
    manager = ELearningManager()
    
    # Beispiel 1: Einfache Aufgabe erstellen
    print("1. Beispiel: Aufgabe erstellen")
    print("-" * 60)
    
    aufgabe = create_aufgabe_quick(
        titel="Array-Summe berechnen",
        level=Level.L1,
        kategorie=3,
        nummer=1,
        problemstellung="Schreibe ein Programm, das die Summe aller Elemente eines Arrays berechnet.",
        autor="Demo-Autor",
        struktogramm="""Deklaration und Initialisierung: zahlen = [5, 10, 15, 20]
Deklaration und Initialisierung: summe = 0
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 1, Schrittweite 1
    Zuweisung: summe = summe + zahlen[i]
Ausgabe: "Summe: " + summe"""
    )
    
    # Zusätzliche Details hinzufügen
    aufgabe.metadata.themen = ["Arrays", "Schleifen", "Summierung"]
    aufgabe.metadata.lernziele = [
        "Array durchlaufen können",
        "Summe akkumulieren können"
    ]
    aufgabe.metadata.zeitaufwand = "15 Minuten"
    aufgabe.beispiel_eingabe = "[5, 10, 15, 20]"
    aufgabe.beispiel_ausgabe = "Summe: 50"
    
    # Speichern
    path = manager.save_aufgabe(aufgabe)
    print()
    
    # Beispiel 2: Information erstellen
    print("2. Beispiel: Information erstellen")
    print("-" * 60)
    
    info = create_information_quick(
        titel="Einführung in Arrays",
        level=Level.L1,
        kategorie=1,
        nummer=1,
        einfuehrung="Arrays sind eine fundamentale Datenstruktur in der Programmierung.",
        inhalt="""Ein Array ist eine geordnete Sammlung von Elementen des gleichen Datentyps.

**Eigenschaften:**
- Feste oder dynamische Größe
- Zugriff über Index (beginnt bei 0)
- Effizient für sequentiellen Zugriff

**Beispiel in Python:**
```python
zahlen = [1, 2, 3, 4, 5]
print(zahlen[0])  # Ausgabe: 1
```""",
        autor="Demo-Autor"
    )
    
    info.metadata.themen = ["Arrays", "Datenstrukturen", "Grundlagen"]
    info.metadata.zeitaufwand = "10 Minuten"
    
    path = manager.save_information(info)
    print()
    
    # Beispiel 3: Lösung erstellen
    print("3. Beispiel: Lösung erstellen")
    print("-" * 60)
    
    loesung = create_loesung_quick(
        titel="Array-Summe berechnen",
        level=Level.L1,
        kategorie=3,
        nummer=1,
        loesungsansatz="Wir durchlaufen das Array mit einer Schleife und addieren jeden Wert zur Summe.",
        python_code="""def berechne_summe(zahlen: list[int]) -> int:
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe

# Test
zahlen = [5, 10, 15, 20]
ergebnis = berechne_summe(zahlen)
print(f"Summe: {ergebnis}")""",
        autor="Demo-Autor"
    )
    
    loesung.komplexitaet = "O(n) - Lineare Zeitkomplexität, da wir jedes Element einmal besuchen"
    loesung.erklaerung = """Die Lösung verwendet eine einfache for-Schleife:
1. Initialisiere `summe` mit 0
2. Für jedes Element im Array: addiere es zur Summe
3. Gib die finale Summe zurück"""
    
    path = manager.save_loesung(loesung)
    print()
    
    # Beispiel 4: Indices generieren
    print("4. Beispiel: Indices generieren")
    print("-" * 60)
    
    indices = manager.generate_all_indices()
    print(f"\n{len(indices)} Index-Dateien generiert")
    print()
    
    print("✅ Demo abgeschlossen!")
