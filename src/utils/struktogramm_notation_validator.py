"""
Struktogramm Notation Validator und Konverter

Dieses Modul stellt sicher, dass Programmlogik in Form von Struktogrammen
ausschließlich in grafischer Box-Notation (mit ┌─│└ Zeichen) verwendet wird.

Baden-Württemberg Abitur-Standard: Grafische Notation ist Pflicht!
"""

import re
from pathlib import Path
from typing import List, Tuple, Dict
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Ergebnis einer Validierung"""
    is_valid: bool
    file_path: str
    errors: List[str]
    warnings: List[str]
    text_based_struktogramme: List[Tuple[int, str]]  # (line_number, content)


class StruktogrammNotationValidator:
    """Validiert und konvertiert Struktogramm-Notationen"""
    
    # Patterns für textbasierte Operatoren (ohne Box-Zeichen)
    TEXT_PATTERNS = [
        r'^Deklaration:',
        r'^Deklaration und Initialisierung:',
        r'^Initialisierung:',
        r'^Zuweisung:',
        r'^Einlesen:',
        r'^Ausgabe:',
        r'^Rückgabe:',
        r'^Aufruf:',
        r'^Wenn .+, dann$',
        r'^Wiederhole solange',
        r'^Zähle .+ von .+ bis',
    ]
    
    # Box-Zeichen für grafische Notation
    BOX_CHARS = ['┌', '─', '│', '└', '├', '┤', '┬', '┴', '┼', '┐', '┘']
    
    def __init__(self):
        self.compiled_patterns = [re.compile(p, re.MULTILINE) for p in self.TEXT_PATTERNS]
    
    def validate_file(self, file_path: Path) -> ValidationResult:
        """
        Validiert eine Datei auf korrekte Struktogramm-Notation.
        
        Args:
            file_path: Pfad zur zu validierenden Datei
            
        Returns:
            ValidationResult mit Ergebnissen
        """
        errors = []
        warnings = []
        text_based_struktogramme = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            errors.append(f"Fehler beim Lesen der Datei: {e}")
            return ValidationResult(
                is_valid=False,
                file_path=str(file_path),
                errors=errors,
                warnings=warnings,
                text_based_struktogramme=text_based_struktogramme
            )
        
        # Finde alle Code-Blöcke
        code_blocks = self._extract_code_blocks(content)
        
        for block_info in code_blocks:
            start_line, end_line, block_content = block_info
            
            # Prüfe, ob der Block textbasierte Operatoren enthält
            has_text_operators = self._has_text_based_operators(block_content)
            has_box_chars = self._has_box_characters(block_content)
            
            if has_text_operators and not has_box_chars:
                # Textbasiertes Struktogramm gefunden (FEHLER!)
                errors.append(
                    f"Zeile {start_line}-{end_line}: Struktogramm in textbasierter "
                    f"Notation gefunden. Bitte verwende grafische Box-Notation!"
                )
                text_based_struktogramme.append((start_line, block_content[:100]))
            
            elif has_text_operators and has_box_chars:
                # Gemischte Notation (sollte überprüft werden)
                warnings.append(
                    f"Zeile {start_line}-{end_line}: Gemischte Notation erkannt. "
                    f"Bitte stelle sicher, dass die grafische Notation korrekt ist."
                )
        
        is_valid = len(errors) == 0
        
        return ValidationResult(
            is_valid=is_valid,
            file_path=str(file_path),
            errors=errors,
            warnings=warnings,
            text_based_struktogramme=text_based_struktogramme
        )
    
    def validate_directory(self, directory: Path, pattern: str = "**/*.md") -> List[ValidationResult]:
        """
        Validiert alle Dateien in einem Verzeichnis.
        
        Args:
            directory: Verzeichnis zum Durchsuchen
            pattern: Glob-Pattern für Dateien (Standard: **/*.md)
            
        Returns:
            Liste von ValidationResults
        """
        results = []
        
        for file_path in directory.glob(pattern):
            if file_path.is_file():
                result = self.validate_file(file_path)
                results.append(result)
        
        return results
    
    def convert_text_to_graphic(self, text_struktogramm: str) -> str:
        """
        Konvertiert ein textbasiertes Struktogramm in grafische Box-Notation.
        
        Args:
            text_struktogramm: Textbasiertes Struktogramm
            
        Returns:
            Struktogramm in grafischer Box-Notation
        """
        lines = text_struktogramm.strip().split('\n')
        graphic_lines = []
        indent_level = 0
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                continue
            
            # Indent-Level erkennen
            current_indent = len(line) - len(line.lstrip())
            indent_level = current_indent // 4
            
            # Erstelle Box-Zeile
            if self._is_loop_start(stripped):
                graphic_line = self._create_loop_box(stripped, indent_level)
            elif self._is_condition_start(stripped):
                graphic_line = self._create_condition_box(stripped, indent_level)
            else:
                graphic_line = self._create_simple_box(stripped, indent_level)
            
            graphic_lines.extend(graphic_line)
        
        return '\n'.join(graphic_lines)
    
    def _extract_code_blocks(self, content: str) -> List[Tuple[int, int, str]]:
        """Extrahiert alle Code-Blöcke aus dem Inhalt mit Zeilennummern"""
        code_blocks = []
        lines = content.split('\n')
        in_code_block = False
        block_start = 0
        block_lines = []
        
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                if not in_code_block:
                    # Start eines Code-Blocks
                    in_code_block = True
                    block_start = i + 1
                    block_lines = []
                else:
                    # Ende eines Code-Blocks
                    in_code_block = False
                    if block_lines:
                        code_blocks.append((block_start, i - 1, '\n'.join(block_lines)))
            elif in_code_block:
                block_lines.append(line)
        
        return code_blocks
    
    def _has_text_based_operators(self, text: str) -> bool:
        """Prüft, ob Text textbasierte Struktogramm-Operatoren enthält"""
        for pattern in self.compiled_patterns:
            if pattern.search(text):
                return True
        return False
    
    def _has_box_characters(self, text: str) -> bool:
        """Prüft, ob Text Box-Zeichen für grafische Notation enthält"""
        return any(char in text for char in self.BOX_CHARS)
    
    def _is_loop_start(self, line: str) -> bool:
        """Prüft, ob Zeile ein Schleifen-Start ist"""
        return (line.startswith('Wiederhole solange') or 
                line.startswith('Zähle ') or
                line.startswith('Wiederhole von'))
    
    def _is_condition_start(self, line: str) -> bool:
        """Prüft, ob Zeile ein Bedingung-Start ist"""
        return line.startswith('Wenn ') and ', dann' in line
    
    def _create_simple_box(self, content: str, indent: int = 0) -> List[str]:
        """Erstellt eine einfache Box für eine Anweisung"""
        width = 57
        indent_str = '│ ' * indent
        
        # Prüfe ob mehrzeilig
        if len(content) > width - len(indent_str) - 4:
            lines = self._wrap_text(content, width - len(indent_str) - 4)
            result = []
            if indent == 0:
                result.append('┌' + '─' * (width - 2) + '┐')
            for i, line in enumerate(lines):
                result.append('│ ' + indent_str + line.ljust(width - len(indent_str) - 4) + ' │')
            if indent == 0:
                result.append('└' + '─' * (width - 2) + '┘')
            return result
        else:
            result = []
            if indent == 0:
                result.append('┌' + '─' * (width - 2) + '┐')
            result.append('│ ' + indent_str + content.ljust(width - len(indent_str) - 4) + ' │')
            if indent == 0:
                result.append('└' + '─' * (width - 2) + '┘')
            return result
    
    def _create_loop_box(self, content: str, indent: int = 0) -> List[str]:
        """Erstellt eine Box für eine Schleife"""
        width = 57
        indent_str = '│ ' * indent
        
        result = []
        if indent == 0:
            result.append('┌' + '─' * (width - 2) + '┐')
        result.append('│ ' + indent_str + '┌─ ' + content.ljust(width - len(indent_str) - 8) + ' │')
        result.append('│ ' + indent_str + '│' + ' ' * (width - len(indent_str) - 4) + ' │')
        
        return result
    
    def _create_condition_box(self, content: str, indent: int = 0) -> List[str]:
        """Erstellt eine Box für eine Bedingung"""
        width = 57
        
        # Extrahiere Bedingung
        match = re.match(r'Wenn (.+), dann', content)
        if match:
            condition = match.group(1).strip()
        else:
            condition = content
        
        result = []
        result.append('┌' + '─' * (width - 2) + '┐')
        result.append('│' + condition.center(width - 2) + '│')
        result.append('├' + '─' * (width - 2) + '┤')
        result.append('│ J' + ' ' * (width // 2 - 4) + '│ N' + ' ' * (width // 2 - 4) + '│')
        
        return result
    
    def _wrap_text(self, text: str, max_width: int) -> List[str]:
        """Bricht langen Text in mehrere Zeilen um"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines


def create_validation_report(results: List[ValidationResult]) -> Dict[str, any]:
    """
    Erstellt einen Validierungsbericht.
    
    Args:
        results: Liste von ValidationResults
        
    Returns:
        Dictionary mit Zusammenfassung
    """
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    invalid = total - valid
    total_errors = sum(len(r.errors) for r in results)
    total_warnings = sum(len(r.warnings) for r in results)
    
    files_with_issues = [r for r in results if not r.is_valid]
    
    return {
        'total_files': total,
        'valid_files': valid,
        'invalid_files': invalid,
        'total_errors': total_errors,
        'total_warnings': total_warnings,
        'files_with_issues': files_with_issues
    }


def print_validation_report(report: Dict[str, any]):
    """Gibt einen Validierungsbericht auf der Konsole aus"""
    print("\n" + "=" * 60)
    print("📊 STRUKTOGRAMM-NOTATIONS-VALIDIERUNG")
    print("=" * 60)
    print(f"Gesamt:    {report['total_files']} Dateien")
    print(f"✅ Gültig:  {report['valid_files']} Dateien")
    print(f"❌ Ungültig: {report['invalid_files']} Dateien")
    print(f"Fehler:    {report['total_errors']}")
    print(f"Warnungen: {report['total_warnings']}")
    print("=" * 60)
    
    if report['files_with_issues']:
        print("\n❌ Dateien mit Problemen:\n")
        for result in report['files_with_issues']:
            print(f"📄 {result.file_path}")
            for error in result.errors:
                print(f"   ❌ {error}")
            for warning in result.warnings:
                print(f"   ⚠️  {warning}")
            print()


# CLI-Funktion
def main():
    """Hauptfunktion für CLI-Nutzung"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validiert Struktogramm-Notationen in Markdown-Dateien'
    )
    parser.add_argument(
        'directory',
        type=Path,
        help='Verzeichnis zum Durchsuchen'
    )
    parser.add_argument(
        '--pattern',
        type=str,
        default='**/*.md',
        help='Glob-Pattern für Dateien (Standard: **/*.md)'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Versuche automatisch zu korrigieren'
    )
    
    args = parser.parse_args()
    
    validator = StruktogrammNotationValidator()
    results = validator.validate_directory(args.directory, args.pattern)
    report = create_validation_report(results)
    print_validation_report(report)
    
    if args.fix and report['files_with_issues']:
        print("\n🔧 Automatische Korrektur wird in einer zukünftigen Version implementiert.")


if __name__ == '__main__':
    main()
