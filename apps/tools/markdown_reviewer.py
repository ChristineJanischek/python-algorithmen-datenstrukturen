#!/usr/bin/env python3
"""
Markdown Reviewer - Automatische Überprüfung aller .md Dateien auf Konsistenz und Aktualität

Diese Routine überprüft:
1. Ungültige oder veraltete Datei-Referenzen
2. Tote Links (Verweise auf nicht existente Dateien)
3. Verwaiste Dateien (keine Verweise darauf)
4. Struktur-Konsistenz (z.B. fehlende INDEX.md Einträge)
5. Aktualität von Dokumentation vs. Codeänderungen
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
import json


class MarkdownReviewer:
    """Überprüft konsistenz und Validität aller Markdown-Dateien im Repository."""
    
    def __init__(self, repo_root: str):
        """
        Initialisiere den Markdown Reviewer.
        
        Args:
            repo_root: Root-Verzeichnis des Repositories
        """
        self.repo_root = Path(repo_root)
        self.docs_dir = self.repo_root / "docs"
        self.src_dir = self.repo_root / "src"
        self.apps_dir = self.repo_root / "apps"
        
        self.errors: List[Dict] = []
        self.warnings: List[Dict] = []
        self.info: List[Dict] = []
        
    def review_all(self) -> Dict:
        """
        Führe alle Überprüfungen durch.
        
        Returns:
            Dictionary mit Ergebnissen: {'errors': [...], 'warnings': [...], 'info': [...]}
        """
        self.errors = []
        self.warnings = []
        self.info = []
        
        # Überprüfe verschiedene Aspekte
        self._check_file_references()
        self._check_dead_links()
        self._check_orphaned_files()
        self._check_index_consistency()
        self._check_documentation_structure()
        self._check_code_documentation_sync()
        
        return {
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info,
            'summary': {
                'error_count': len(self.errors),
                'warning_count': len(self.warnings),
                'info_count': len(self.info),
            }
        }
    
    def _get_all_markdown_files(self, directories: List[Path] = None) -> List[Path]:
        """Hole alle .md Dateien aus den angegebenen Verzeichnissen."""
        if directories is None:
            directories = [self.docs_dir]
        
        files = []
        for directory in directories:
            if directory.exists():
                for md_file in directory.rglob("*.md"):
                    if not any(part.startswith('.') for part in md_file.parts):
                        files.append(md_file)
        return files
    
    def _extract_references(self, file_path: Path) -> Set[str]:
        """Extrahiere alle Datei-Referenzen aus einer Markdown-Datei."""
        references = set()
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Markdown Links: [text](path)
            for match in re.finditer(r'\]\(([^)]+)\)', content):
                ref = match.group(1)
                # Entferne Anchor-Links
                ref = ref.split('#')[0]
                if ref and not ref.startswith('http'):
                    references.add(ref)
            
            # Inline Code-Referenzen: `path/to/file.md`
            for match in re.finditer(r'`([^\`]+\.md)`', content):
                ref = match.group(1)
                references.add(ref)
            
            # Explizite Pfad-Referenzen in Text
            for match in re.finditer(r'(?:Datei|File|Pfad|Path):\s*[`\']?([^\s`\']+\.md)[`\']?', content):
                ref = match.group(1)
                references.add(ref)
                
        except Exception as e:
            self.errors.append({
                'type': 'read_error',
                'file': str(file_path),
                'message': f'Fehler beim Lesen der Datei: {e}'
            })
        
        return references
    
    def _check_file_references(self):
        """Überprüfe, dass alle Datei-Referenzen gültig sind."""
        md_files = self._get_all_markdown_files()
        
        for md_file in md_files:
            references = self._extract_references(md_file)
            
            for ref in references:
                # Relative Pfad auflösen
                if ref.startswith('/'):
                    target = self.repo_root / ref.lstrip('/')
                else:
                    target = (md_file.parent / ref).resolve()
                
                # Überprüfe ob Datei existiert
                if not target.exists():
                    # Aber nur melden, wenn es im docs/ oder src/ Bereich ist
                    if 'docs' in str(target) or 'src' in str(target) or 'apps' in str(target):
                        self.errors.append({
                            'type': 'invalid_reference',
                            'file': str(md_file.relative_to(self.repo_root)),
                            'reference': ref,
                            'target': str(target.relative_to(self.repo_root)),
                            'message': f'Ungültige Referenz: {ref} → nicht gefunden'
                        })
    
    def _check_dead_links(self):
        """Überprüfe auf tote externe Links (optional - wir machen das nur für relative Links)."""
        pass  # Externe Links sind schwer zu prüfen, deshalb überspringen wir das
    
    def _check_orphaned_files(self):
        """Überprüfe auf Dateien, die nirgendwo verlinkt sind."""
        md_files = self._get_all_markdown_files()
        all_references = set()
        
        # Sammle alle Referenzen
        for md_file in md_files:
            references = self._extract_references(md_file)
            all_references.update(references)
        
        # Überprüfe jede Datei, ob sie verlinkt ist
        for md_file in md_files:
            file_name = md_file.name
            relative_path = str(md_file.relative_to(self.repo_root))
            
            # INDEX.md und TEMPLATE Dateien ignorieren
            if file_name in ['INDEX.md', 'TEMPLATE.md'] or 'TEMPLATE' in file_name:
                continue
            
            # Überprüfe ob die Datei verlinkt ist
            is_referenced = False
            for ref in all_references:
                if file_name in ref or relative_path in ref or relative_path.replace('\\', '/') in ref:
                    is_referenced = True
                    break
            
            if not is_referenced:
                self.warnings.append({
                    'type': 'orphaned_file',
                    'file': relative_path,
                    'message': f'Datei wird nirgendwo verlinkt: {relative_path}'
                })
    
    def _check_index_consistency(self):
        """Überprüfe, dass INDEX.md Dateien aktuell sind."""
        index_files = list(self.docs_dir.rglob("INDEX.md"))
        
        for index_file in index_files:
            directory = index_file.parent
            md_files_in_dir = [f for f in directory.glob("*.md") 
                             if f.name != "INDEX.md" and "TEMPLATE" not in f.name]
            
            index_content = index_file.read_text(encoding='utf-8')
            
            missing_in_index = []
            for md_file in md_files_in_dir:
                if md_file.name not in index_content:
                    missing_in_index.append(md_file.name)
            
            if missing_in_index:
                self.warnings.append({
                    'type': 'incomplete_index',
                    'file': str(index_file.relative_to(self.repo_root)),
                    'missing_entries': missing_in_index,
                    'message': f'INDEX.md - Fehlende Einträge: {", ".join(missing_in_index)}'
                })
    
    def _check_documentation_structure(self):
        """Überprüfe die Standard-Verzeichnisstruktur."""
        required_dirs = [
            'docs/aufgaben',
            'docs/information',
            'docs/loesungen',
            'docs/handbuch',
        ]
        
        for dir_path in required_dirs:
            full_path = self.repo_root / dir_path
            if not full_path.exists():
                self.warnings.append({
                    'type': 'missing_directory',
                    'path': dir_path,
                    'message': f'Standard-Verzeichnis fehlt: {dir_path}'
                })
    
    def _check_code_documentation_sync(self):
        """Überprüfe, dass Code-Änderungen auch mit Dokumentation aktualisiert sind."""
        # Suche nach Python-Funktionen und -Klassen mit Änderungen
        python_files = list(self.src_dir.rglob("*.py")) if self.src_dir.exists() else []
        
        # Einfache Heuristik: Wenn neue Python-Dateien, sollte es auch Dokumentation geben
        new_modules = []
        for py_file in python_files:
            relative_path = py_file.relative_to(self.repo_root)
            # Ignoriere __pycache__ und __init__.py
            if '__pycache__' in str(py_file) or py_file.name == '__init__.py':
                continue
            
            # Prüfe ob entsprechende Dokumentation existiert
            module_name = py_file.stem
            
            # Suche nach entsprechenden .md Dateien
            found_doc = False
            for doc_file in self._get_all_markdown_files():
                if module_name in doc_file.read_text(encoding='utf-8'):
                    found_doc = True
                    break
            
            if not found_doc and py_file.stat().st_size > 100:  # Nur für nennenswerte Dateien
                self.info.append({
                    'type': 'undocumented_module',
                    'module': str(relative_path),
                    'message': f'Modul {relative_path} hat möglicherweise keine Dokumentation'
                })
    
    def format_report(self) -> str:
        """Formatiere den Report als lesbaren Text."""
        report = []
        report.append("\n" + "="*70)
        report.append("📋 MARKDOWN-DATEIEN REVIEW REPORT")
        report.append("="*70 + "\n")
        
        # Fehler
        if self.errors:
            report.append(f"❌ FEHLER ({len(self.errors)}):")
            report.append("-" * 70)
            for error in self.errors:
                report.append(f"  • [{error['type']}] {error['file']}")
                report.append(f"    → {error['message']}")
            report.append("")
        
        # Warnungen
        if self.warnings:
            report.append(f"⚠️  WARNUNGEN ({len(self.warnings)}):")
            report.append("-" * 70)
            for warning in self.warnings:
                report.append(f"  • [{warning['type']}] {warning['file']}")
                report.append(f"    → {warning['message']}")
            report.append("")
        
        # Info
        if self.info:
            report.append(f"ℹ️  INFORMATIONEN ({len(self.info)}):")
            report.append("-" * 70)
            for info_item in self.info:
                report.append(f"  • [{info_item['type']}] {info_item.get('module', info_item.get('file', ''))}")
                report.append(f"    → {info_item['message']}")
            report.append("")
        
        # Zusammenfassung
        if not self.errors and not self.warnings and not self.info:
            report.append("✅ ALLES BEREIT!")
            report.append("   Keine Probleme gefunden. Markdown-Dateien sind konsistent.")
        else:
            total = len(self.errors) + len(self.warnings) + len(self.info)
            report.append(f"📊 ZUSAMMENFASSUNG: {total} Probleme gefunden")
            report.append(f"   - Fehler: {len(self.errors)}")
            report.append(f"   - Warnungen: {len(self.warnings)}")
            report.append(f"   - Informationen: {len(self.info)}")
        
        report.append("="*70 + "\n")
        return "\n".join(report)


def main():
    """Hauptfunktion - Wird vom Git Hook aufgerufen."""
    import sys
    
    try:
        repo_root = Path(__file__).parent.parent.parent  # apps/tools -> apps -> root
        reviewer = MarkdownReviewer(str(repo_root))
        
        print("\n🔍 Überprüfe Markdown-Dateien auf Konsistenz und Aktualität...\n")
        
        results = reviewer.review_all()
        
        # Gebe Report aus
        print(reviewer.format_report())
        
        # Speichere Report als JSON (optional)
        report_file = repo_root / ".github" / "markdown_review_report.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Gebe Exit-Code zurück (0 = OK, 1 = Fehler)
        if results['summary']['error_count'] > 0:
            return 1
        return 0
        
    except Exception as e:
        print(f"❌ Fehler beim Review: {e}")
        import traceback
        traceback.print_exc()
        return 2


if __name__ == "__main__":
    import sys
    sys.exit(main())
