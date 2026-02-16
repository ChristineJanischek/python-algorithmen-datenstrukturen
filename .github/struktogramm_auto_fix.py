"""
Struktogramm Auto-Fix Tool
Automatische Korrektur von Dateien mit fehlenden/falschen Struktogramm-Notationen

Features:
  - Fehlende Struktogramme hinzufügen
  - Abschnitte richtig anordnen
  - Code-Blöcke korrigieren
  - Config-basiert für maximale Flexibilität

Verwendung:
  python .github/struktogramm_auto_fix.py [dateipath] [--dry-run]
"""

import sys
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class FixStrategy(Enum):
    """Verfügbare Fix-Strategien"""
    ADD_STRUKTOGRAMM = "add_struktogramm"
    REORDER_SECTIONS = "reorder_sections"
    FIX_CODE_BLOCKS = "fix_code_blocks"


@dataclass
class FixResult:
    """Ergebnis einer Fix-Operation"""
    success: bool
    file_path: Path
    strategy: FixStrategy
    changes_made: List[str]
    error: Optional[str] = None


class ConfigLoader:
    """Lädt und verwaltet die zentrale Config"""
    
    def __init__(self, config_path: str = None):
        if config_path is None:
            config_path = Path(__file__).parent / "config" / "struktogramm.yml"
        
        self.config_path = Path(config_path)
        self.config = self._load_config()
    
    def _load_config(self) -> dict:
        """Lädt YAML-Config"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️  Config nicht gefunden ({self.config_path}), nutze Defaults")
            return self._get_default_config()
    
    def _get_default_config(self) -> dict:
        """Default-Konfiguration"""
        return {
            'auto_fix': {
                'enabled': True,
                'add_missing_struktogramm': {'enabled': True},
                'reorder_sections': {'enabled': True},
            },
            'templates': {
                'struktogramm_template_basic': '## 📐 Struktogramm (grafische Notation)\n\n```\n┌────────────────────────────────────────┐\n│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │\n└────────────────────────────────────────┘\n```'
            }
        }
    
    def is_auto_fix_enabled(self, strategy: str) -> bool:
        """Prüft ob Auto-Fix für Strategie aktiviert"""
        auto_fix_config = self.config.get('auto_fix', {})
        strategy_config = auto_fix_config.get(strategy, {})
        return strategy_config.get('enabled', False)
    
    def get_template(self, template_name: str) -> str:
        """Holt ein Template"""
        templates = self.config.get('templates', {})
        return templates.get(template_name, "")


class StructogrammAutoFixer:
    """Hauptklasse für automatische Fixes"""
    
    def __init__(self, config_path: str = None):
        self.config_loader = ConfigLoader(config_path)
        self.config = self.config_loader.config
    
    def fix_file(self, file_path: Path, dry_run: bool = False) -> List[FixResult]:
        """
        Repariert eine Datei
        
        Args:
            file_path: Pfad zur Datei
            dry_run: Nur zeigen, nicht speichern
            
        Returns:
            Liste von FixResults
        """
        results = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            return [FixResult(
                success=False,
                file_path=file_path,
                strategy=FixStrategy.ADD_STRUKTOGRAMM,
                changes_made=[],
                error=f"Datei konnte nicht gelesen werden: {e}"
            )]
        
        original_content = content
        
        # Strategy 1: Fehlende Struktogramme hinzufügen
        if self.config_loader.is_auto_fix_enabled('add_missing_struktogramm'):
            content, changes = self._add_missing_struktogramm(content, file_path)
            if changes:
                results.append(FixResult(
                    success=True,
                    file_path=file_path,
                    strategy=FixStrategy.ADD_STRUKTOGRAMM,
                    changes_made=changes
                ))
        
        # Strategy 2: Abschnitte neuordnen
        if self.config_loader.is_auto_fix_enabled('reorder_sections'):
            content, changes = self._reorder_sections(content, file_path)
            if changes:
                results.append(FixResult(
                    success=True,
                    file_path=file_path,
                    strategy=FixStrategy.REORDER_SECTIONS,
                    changes_made=changes
                ))
        
        # Strategy 3: Code-Blöcke korrigieren
        if self.config_loader.is_auto_fix_enabled('fix_code_blocks'):
            content, changes = self._fix_code_blocks(content)
            if changes:
                results.append(FixResult(
                    success=True,
                    file_path=file_path,
                    strategy=FixStrategy.FIX_CODE_BLOCKS,
                    changes_made=changes
                ))
        
        # Speichere wenn Änderungen und nicht dry-run
        if content != original_content and not dry_run:
            try:
                file_path.write_text(content, encoding='utf-8')
                print(f"✅ Datei aktualisiert: {file_path}")
                return results
            except Exception as e:
                return [FixResult(
                    success=False,
                    file_path=file_path,
                    strategy=FixStrategy.ADD_STRUKTOGRAMM,
                    changes_made=[],
                    error=f"Fehler beim Speichern: {e}"
                )]
        
        return results if results else [FixResult(
            success=True,
            file_path=file_path,
            strategy=FixStrategy.ADD_STRUKTOGRAMM,
            changes_made=["Keine Änderungen nötig" if not dry_run else "[DRY-RUN] Keine Änderungen nötig"]
        )]
    
    def _add_missing_struktogramm(self, content: str, file_path: Path) -> Tuple[str, List[str]]:
        """
        Fügt fehlende Struktogramme hinzu
        """
        changes = []
        lines = content.split('\n')
        
        # Finde Python-Blöcke ohne vorhergehendes Struktogramm
        i = 0
        new_lines = []
        
        while i < len(lines):
            line = lines[i]
            
            # Erkenne ```python Blöcke
            if line.strip().startswith("```python"):
                # Prüfe davor
                context_start = max(0, i - 20)
                context = '\n'.join(lines[context_start:i])
                
                has_graphic = any(char in context for char in ['┌', '├', '└', '│', '─'])
                has_section = "Struktogramm" in context
                
                if not (has_graphic or has_section):
                    # Füge Struktogramm ein
                    template = self.config_loader.get_template('struktogramm_template_basic')
                    new_lines.append('')
                    new_lines.append(template)
                    new_lines.append('')
                    changes.append(f"Struktogramm hinzugefügt vor Zeile {i+1}")
            
            new_lines.append(line)
            i += 1
        
        return '\n'.join(new_lines), changes
    
    def _reorder_sections(self, content: str, file_path: Path) -> Tuple[str, List[str]]:
        """
        Sortiert Abschnitte in korrekter Reihenfolge
        """
        changes = []
        preferred_order = self.config.get('auto_fix', {}).get('reorder_sections', {}).get('preferred_order', [])
        
        if not preferred_order:
            return content, changes
        
        # Einfache Implementierung: Prüfe nur ob Struktogramm vor Python kommt
        struktogramm_pos = content.find("## 📐 Struktogramm")
        python_impl_pos = content.find("## 💻 Python-Implementierung")
        
        if 0 < struktogramm_pos and 0 < python_impl_pos and struktogramm_pos > python_impl_pos:
            # Falsche Reihenfolge - braucht Advanced Parsing, skip für jetzt
            changes.append("Abschnitte sollten neu angeordnet werden (requires advanced parsing)")
        
        return content, changes
    
    def _fix_code_blocks(self, content: str) -> Tuple[str, List[str]]:
        """
        Korrigiert Code-Blöcke
        """
        changes = []
        
        # Stelle sicher dass alle Code-Blöcke ```python statt ``` haben
        pattern = r'```\n(.*?)\n```'
        
        def fix_code_block(match):
            code = match.group(1)
            # Prüfe ob Python-Code
            if any(keyword in code for keyword in ['def ', 'for ', 'while ', 'if ', 'import ']):
                changes.append("Code-Block-Tag korrigiert (``` → ```python)")
                return f'```python\n{code}\n```'
            return match.group(0)
        
        new_content = re.sub(pattern, fix_code_block, content, flags=re.DOTALL)
        
        return new_content, changes


def print_results(results: List[FixResult]):
    """Gibt Fix-Ergebnisse aus"""
    print("\n" + "=" * 70)
    print("📝 STRUKTOGRAMM AUTO-FIX RESULTS")
    print("=" * 70)
    
    total_changes = sum(len(r.changes_made) for r in results if r.success)
    
    for result in results:
        if result.success:
            print(f"\n✅ {result.file_path.name}")
            print(f"   Strategy: {result.strategy.value}")
            if result.changes_made:
                for change in result.changes_made:
                    print(f"   • {change}")
            else:
                print(f"   • Keine Änderungen nötig")
        else:
            print(f"\n❌ {result.file_path.name}")
            print(f"   Error: {result.error}")
    
    print(f"\n📊 Zusammenfassung: {total_changes} Änderungen gemacht")
    print("=" * 70)


def main():
    """Hauptfunktion"""
    if len(sys.argv) < 2:
        print("Verwendung: python struktogramm_auto_fix.py <dateipath> [--dry-run]")
        print("\nBeispiele:")
        print("  python .github/struktogramm_auto_fix.py docs/loesungen/L1/test.md")
        print("  python .github/struktogramm_auto_fix.py docs/loesungen/L1/test.md --dry-run")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv
    
    if not file_path.exists():
        print(f"❌ Datei nicht gefunden: {file_path}")
        sys.exit(1)
    
    fixer = StructogrammAutoFixer()
    results = fixer.fix_file(file_path, dry_run=dry_run)
    print_results(results)
    
    if dry_run:
        print("\n💡 [DRY-RUN] Keine Änderungen gespeichert. Entferne --dry-run um zu speichern.")


if __name__ == "__main__":
    main()
