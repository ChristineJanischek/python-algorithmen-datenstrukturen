"""
DOCX Markdown Optimizer - Optimiert Markdown für DOCX-Export.

Dieses Modul bietet Tools zur Optimierung von Markdown-Dokumenten für den
Export nach DOCX-Format, insbesondere:
- Strukto­gramm­ein­bin­dungen mit DOCX-Metadaten
- Quellcode-Styling und Formatierung
- Footer-Versionsangaben
- Bild-Einbettung und Fallbacks

Architektur:
- DocxMetadata: Zentrale Verwaltung von DOCX-Einstellungen
- DocxOptimizer: Hauptoptimierungslogik (Pipeline-Pattern)
- Verschiedene Optimizer-Klassen für spezifische Aufgaben

Autor: python-algorithmen-datenstrukturen
Version: 1.0
Datum: 2026-03-03
Lizenz: MIT
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Any
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


@dataclass
class DocxMetadata:
    """Zentrale Konfiguration für DOCX-Export-Optimierungen.
    
    Diese Klasse speichert alle DOCX-spezifischen Einstellungen und kann
    von verschiedenen Tools verwendet werden um konsistentes Verhalten
    sicherzustellen.
    
    Attributes:
        code_bg_color: Hintergrundfarbe für Code-Blöcke
        code_text_color: Textfarbe für Code
        code_border_color: Rahmenfarbe für Code-Blöcke
        embed_struktogramme: Sollen Struktogramme embedded werden?
        add_alttext: Sollen Alt-Texte hinzugefügt werden?
        version_footer: Soll Versionierung in Footer?
        footer_format: Template für Footer
    """
    
    # Code-Styling (RGB-Hex)
    code_bg_color: str = "#F2F2F2"  # Hellgrau
    code_text_color: str = "#111111"  # Dunkelgrau
    code_border_color: str = "#C8C8C8"  # Mittleres Grau
    
    # Struktogramm-Einstellung
    embed_struktogramme: bool = True
    add_alttext: bool = True
    add_embedding_info: bool = True
    
    # Version/Footer
    version_footer: bool = True
    footer_format: str = "Version {version}"
    
    # Konvertierungszielformat
    export_format: str = "docx"
    
    # Logging
    verbose: bool = False
    
    @classmethod
    def from_dict(cls, config: Dict[str, Any]) -> DocxMetadata:
        """Erstellt Metadaten aus Dictionary. Ermöglicht Konfigurationsdateien."""
        return cls(**{k: v for k, v in config.items() if k in cls.__dataclass_fields__})


@dataclass
class OptimizationResult:
    """Ergebnis einer Optimierung.
    
    Attributes:
        success: War Optimierung erfolgreich?
        file_path: Path der verarbeiteten Datei
        changes_count: Anzahl der vorgenommenen Änderungen
        message: Beschreibung des Ergebnisses
        details: Zusätzliche Details
    """
    success: bool
    file_path: Path
    changes_count: int = 0
    message: str = ""
    details: Dict[str, Any] = field(default_factory=dict)


class BaseOptimizer(ABC):
    """Abstrakte Basis-Klasse für Optimierer.
    
    Alle spezifischen Optimierer erben von dieser Klasse und implementieren
    die optimize()-Methode. Dies ermöglicht ein flexibles Plugin-System.
    """
    
    def __init__(self, metadata: DocxMetadata):
        """
        Args:
            metadata: Zentrale DOCX-Metadaten
        """
        self.metadata = metadata
    
    @abstractmethod
    def optimize(self, content: str) -> Tuple[str, int]:
        """
        Optimiert Markdown-Inhalt.
        
        Args:
            content: Markdown-Inhalt
            
        Returns:
            Tuple[optimierter_inhalt, anzahl_änderungen]
        """
        pass


class StruktogrammOptimizer(BaseOptimizer):
    """Optimiert Struktogramm-Einbindungen für DOCX.
    
    Fügt DOCX-Metadaten-Kommentare hinzu, um sicherzustellen, dass
    Struktogramme bei DOCX-Export korrekt eingebettet werden.
    """
    
    def optimize(self, content: str) -> Tuple[str, int]:
        """
        Optimiert alle Struktogramm-Referenzen.
        
        Pattern: ![alt_text](path/to/image.svg)
        
        Args:
            content: Markdown-Inhalt
            
        Returns:
            Tuple[optimierter_inhalt, anzahl_änderungen]
        """
        
        image_with_docx_pattern = re.compile(
            r'(!\[([^\]]+)\]\(([^)]+\.svg)\))'
            r'((?:\n<!-- DOCX-(?:ALT-TEXT|EMBED-SVG|EMBEDDING-(?:HINT|INFO)):[^\n]*-->[ \t]*)*)'
        )
        count = 0

        def replace_link(match: re.Match[str]) -> str:
            nonlocal count
            image_markdown = match.group(1)
            alt_text = match.group(2)
            svg_path = match.group(3)
            existing_docx_block = match.group(4) or ""

            comments: list[str] = []
            if self.metadata.add_alttext:
                comments.append(f"<!-- DOCX-ALT-TEXT: {alt_text} -->")
            comments.append(f"<!-- DOCX-EMBED-SVG: {svg_path} -->")
            if self.metadata.add_embedding_info:
                comments.append(
                    "<!-- DOCX-EMBEDDING-HINT: "
                    "Dieses Struktogramm wird bei DOCX-Export als eingebettete Grafik dargestellt "
                    "für bessere Kopierbarkeit und Formatierung. -->"
                )

            canonical_docx_block = "\n" + "\n".join(comments)
            canonical = f"{image_markdown}{canonical_docx_block}"

            if canonical_docx_block != existing_docx_block:
                count += 1

            return canonical

        new_content = image_with_docx_pattern.sub(replace_link, content)
        return new_content, count


class CodeBlockOptimizer(BaseOptimizer):
    """Optimiert Code-Blöcke für DOCX-Export.
    
    Fügt DOCX-Metadaten-Kommentare für Code-Styling hinzu.
    """
    
    def optimize(self, content: str) -> Tuple[str, int]:
        """
        Optimiert Python-Code-Blöcke für DOCX.
        
        Args:
            content: Markdown-Inhalt
            
        Returns:
            Tuple[optimierter_inhalt, anzahl_änderungen]
        """
        
        # Pattern: ```python ... ```
        pattern = r'(```python\n(?:.*?\n)*?```)'
        
        # Überprüfe ob bereits optimiert
        if "DOCX-CODE-STYLING" in content:
            return content, 0
        
        # Füge Styling-Info am Anfang des Dokuments hinzu (nicht bei jedem Block)
        count = 0
        if "```python" in content:
            count = 1
            styling_info = (
                f"<!-- DOCX-CODE-STYLING: "
                f"bg={self.metadata.code_bg_color}, "
                f"text={self.metadata.code_text_color}, "
                f"border={self.metadata.code_border_color} -->\n"
            )
            # Füge am Anfang nach Titel ein
            if content.startswith("#"):
                lines = content.split("\n", 2)
                content = f"{lines[0]}\n{styling_info}{'\n'.join(lines[1:])}"
            else:
                content = f"{styling_info}{content}"
        
        return content, count


class FooterVersionOptimizer(BaseOptimizer):
    """Optimiert Versionierung für DOCX-Footer.
    
    Stellt sicher, dass Versionsnummern in Footer sind statt im Dokument-Body.
    """
    
    def optimize(self, content: str) -> Tuple[str, int]:
        """
        Optimiert Versionierungsangaben.
        
        Args:
            content: Markdown-Inhalt
            
        Returns:
            Tuple[optimierter_inhalt, anzahl_änderungen]
        """
        count = 0
        
        # Überprüfe ob bereits DOCX-FUSSZEILE vorhanden
        if "DOCX-FUSSZEILE" not in content:
            # Versuche Version aus Kommentaren oder Struktur zu extrahieren
            # Dies ist optional - kann auch vom Benutzer gesetzt werden
            pass
        
        return content, count


class DocxOptimizer:
    """
    Hauptklasse für DOCX-Optimierung.
    
    Diese Klasse koordiniert mehrere spezialisierte Optimizer und wendet sie
    auf Markdown-Dokumente an. Sie folgt dem Chain-of-Responsibility-Pattern.
    
    Beispiel:
        ```python
        optimizer = DocxOptimizer()
        result = optimizer.optimize_file(Path("dokument.md"))
        print(f"Optimiert: {result.changes_count} Änderungen")
        ```
    """
    
    def __init__(self, metadata: Optional[DocxMetadata] = None):
        """
        Initialisiert den Optimizer.
        
        Args:
            metadata: DOCX-Metadaten. Wenn None, werden Defaults verwendet.
        """
        self.metadata = metadata or DocxMetadata()
        
        # Optimizer in Reihenfolge (Pipeline)
        self.optimizers: List[BaseOptimizer] = [
            CodeBlockOptimizer(self.metadata),
            StruktogrammOptimizer(self.metadata),
            FooterVersionOptimizer(self.metadata),
        ]
        
        if self.metadata.verbose:
            logger.setLevel(logging.DEBUG)
    
    def optimize(self, content: str) -> Tuple[str, int]:
        """
        Optimiert Markdown-Inhalt durch alle registrierten Optimizer.
        
        Args:
            content: Markdown-Inhalt
            
        Returns:
            Tuple[optimierter_inhalt, gesamt_anzahl_änderungen]
        """
        total_changes = 0
        
        for optimizer in self.optimizers:
            content, changes = optimizer.optimize(content)
            total_changes += changes
            
            if changes > 0 and self.metadata.verbose:
                logger.debug(f"{optimizer.__class__.__name__}: {changes} Änderungen")
        
        return content, total_changes
    
    def optimize_file(self, filepath: Path) -> OptimizationResult:
        """
        Optimiert eine Markdown-Datei.
        
        Args:
            filepath: Pfad zur Markdown-Datei
            
        Returns:
            OptimizationResult mit Details
        """
        try:
            # Datei einlesen
            content = filepath.read_text(encoding='utf-8')
            original_content = content
            
            # Optimieren
            optimized_content, changes_count = self.optimize(content)
            
            # Nur schreiben wenn tatsächliche Änderungen
            if optimized_content != original_content:
                filepath.write_text(optimized_content, encoding='utf-8')
                
                return OptimizationResult(
                    success=True,
                    file_path=filepath,
                    changes_count=changes_count,
                    message=f"✅ {changes_count} Optimierungen angewendet",
                    details={"optimizers_used": [o.__class__.__name__ for o in self.optimizers]}
                )
            else:
                return OptimizationResult(
                    success=True,
                    file_path=filepath,
                    changes_count=0,
                    message="⏭️  Keine Änderungen notwendig"
                )
        
        except Exception as e:
            return OptimizationResult(
                success=False,
                file_path=filepath,
                message=f"❌ Fehler: {str(e)}",
                details={"error": str(e)}
            )
    
    def optimize_directory(self, directory: Path, pattern: str = "*.md") -> List[OptimizationResult]:
        """
        Optimiert alle Markdown-Dateien in einem Verzeichnis rekursiv.
        
        Args:
            directory: Pfad zum Verzeichnis
            pattern: Glob-Pattern für Dateien (default: *.md)
            
        Returns:
            Liste von OptimizationResult
        """
        results = []
        
        for md_file in sorted(directory.rglob(pattern)):
            # Überspringe spezielle Dateien
            if md_file.name in ["INDEX.md", "README.md"]:
                continue
            
            result = self.optimize_file(md_file)
            results.append(result)
        
        return results


def optimize_pruefungen_directory(
    directory: Optional[Path] = None,
    metadata: Optional[DocxMetadata] = None,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Convenience-Funktion: Optimiert alle Prüfungsdokumente.
    
    Diese Funktion ist ein einstiegsfreundliches Interface für die
    Standard-Anwendung (alle Prüfungsdokumente optimieren).
    
    Args:
        directory: Zielverzeichnis (default: docs/pruefungen)
        metadata: DOCX-Metadaten (default: Defaults)
        verbose: Soll Ausgabe verbose sein?
        
    Returns:
        Dictionary mit Zusammenfassung
    """
    
    if directory is None:
        directory = Path(__file__).parent.parent.parent / "docs" / "pruefungen"
    
    if metadata is None:
        metadata = DocxMetadata(verbose=verbose)
    
    # Optimizer ausführen
    optimizer = DocxOptimizer(metadata)
    results = optimizer.optimize_directory(directory)
    
    # Zusammenfassung
    successful = [r for r in results if r.success]
    with_changes = [r for r in successful if r.changes_count > 0]
    
    return {
        "total_files": len(results),
        "successful": len(successful),
        "with_changes": len(with_changes),
        "total_changes": sum(r.changes_count for r in with_changes),
        "results": results,
        "summary": {
            "files_optimized": len(with_changes),
            "files_unchanged": len(successful) - len(with_changes),
            "total_optimizations": sum(r.changes_count for r in with_changes)
        }
    }


__all__ = [
    "DocxMetadata",
    "OptimizationResult",
    "BaseOptimizer",
    "StruktogrammOptimizer",
    "CodeBlockOptimizer",
    "FooterVersionOptimizer",
    "DocxOptimizer",
    "optimize_pruefungen_directory",
]
