"""
Config Loader für stroktogramm.yml
Lädt Config auch ohne PyYAML (fallback auf einfaches Parsing)
"""

from pathlib import Path
from typing import Dict, Optional, Any
import json


class SimpleConfigLoader:
    """Einfacher Config-Loader ohne externe Dependencies"""
    
    DEFAULT_CONFIG = {
        'profiles': {
            'loesung': {
                'severity': 'ERROR',
                'auto_fix': True,
                'required_sections': ['📐 Struktogramm', '💻 Python-Implementierung']
            },
            'aufgabe': {
                'severity': 'WARNING',
                'auto_fix': False,
            },
            'pruefung': {
                'severity': 'ERROR',
                'auto_fix': True,
            }
        },
        'rules': {
            'python_needs_struktogramm': {'enabled': True},
            'section_order': {'enabled': True},
            'graphic_elements_required': {'enabled': True},
        },
        'auto_fix': {
            'enabled': True,
            'add_missing_struktogramm': {'enabled': True},
            'reorder_sections': {'enabled': True},
            'fix_code_blocks': {'enabled': True},
        },
        'exclusions': {
            'ignore_patterns': [
                '**/TEMPLATE_*.md',
                '**/INDEX.md',
                'docs/lehrplan/**',
                'docs/handbuch/**',
            ]
        }
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialisiert Config Loader"""
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "struktogramm.yml"
        
        self.config_path = Path(config_path)
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Lädt YAML ohne PyYAML (einfaches Parsing)"""
        if not self.config_path.exists():
            # print(f"⚠️  Config-Datei nicht gefunden: {self.config_path}, verwende Defaults")
            return self.DEFAULT_CONFIG
        
        try:
            # Versuche PyYAML
            import yaml
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or self.DEFAULT_CONFIG
        except ImportError:
            # Fallback: Einfaches Parsing
            return self._parse_yaml_simple(self.config_path)
        except Exception as e:
            # print(f"⚠️  Fehler beim Laden der Config: {e}")
            return self.DEFAULT_CONFIG
    
    def _parse_yaml_simple(self, file_path: Path) -> Dict[str, Any]:
        """Sehr einfaches YAML-Parsing für Basic-Struktur"""
        config = {}
        current_section = None
        current_subsection = None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.rstrip()
                    
                    # Skip comments und leere Zeilen
                    if line.startswith('#') or not line.strip():
                        continue
                    
                    # Top-level Sektion (z.B. "profiles:")
                    if line and not line.startswith(' ') and line.endswith(':'):
                        current_section = line[:-1]
                        current_subsection = None
                        config[current_section] = {}
                    
                    # Unter-Sektion (z.B. "  loesung:")
                    elif line.startswith('  ') and line.endswith(':') and current_section:
                        current_subsection = line.strip()[:-1]
                        config[current_section][current_subsection] = {}
        
        except Exception:
            pass
        
        return config or self.DEFAULT_CONFIG
    
    def get_profile(self, profile_name: str) -> Dict[str, Any]:
        """Holt ein Profile"""
        profiles = self.config.get('profiles', {})
        return profiles.get(profile_name, {})
    
    def get_profile_severity(self, profile_name: str) -> str:
        """Holt Severity-Level für ein Profil"""
        profile = self.get_profile(profile_name)
        return profile.get('severity', 'WARNING')
    
    def is_auto_fix_allowed(self, profile_name: str) -> bool:
        """Prüft ob Auto-Fix für Profil erlaubt"""
        profile = self.get_profile(profile_name)
        return profile.get('auto_fix', False)
    
    def should_exclude_file(self, file_path: Path) -> bool:
        """Prüft ob Datei ausgeschlossen werden soll"""
        exclusions = self.config.get('exclusions', {}).get('ignore_patterns', [])
        file_str = str(file_path)
        
        for pattern in exclusions:
            # Einfaches Pattern-Matching
            if pattern.startswith('**/'):
                # Wildcard-Pattern: "**/TEMPLATE_*.md"
                pattern_end = pattern[3:]
                if pattern_end.endswith('**'):
                    # Komplexeres Pattern, skip
                    continue
                if pattern_end.endswith('/*.md'):
                    # Verzeichnis-Pattern
                    pattern_end = pattern_end[:-5]
                    if pattern_end in file_str:
                        return True
                elif pattern_end.startswith('*.'):
                    # Datei-Pattern
                    ext = pattern_end[2:]  # z.B. "md"
                    if file_str.endswith(f'.{ext}'):
                        prefix = pattern_end[:pattern_end.find('*')]
                        if prefix in file_str or not prefix:
                            return True
            elif '/' in pattern:
                # Pfad-Pattern
                if pattern in file_str:
                    return True
        
        return False
    
    def get_rule(self, rule_name: str) -> Dict[str, Any]:
        """Holt eine Validierungs-Regel"""
        rules = self.config.get('rules', {})
        return rules.get(rule_name, {})
    
    def is_rule_enabled(self, rule_name: str) -> bool:
        """Prüft ob Regel aktiviert"""
        rule = self.get_rule(rule_name)
        return rule.get('enabled', True)
    
    def get_auto_fix_setting(self, strategy_name: str) -> bool:
        """Prüft ob Auto-Fix Strategie aktiviert"""
        auto_fix = self.config.get('auto_fix', {})
        strategy = auto_fix.get(strategy_name, {})
        return strategy.get('enabled', False)


# Globale Instanz
_config_loader = None


def get_config_loader(config_path: Optional[str] = None) -> SimpleConfigLoader:
    """Holt oder erstellt globale Config-Loader Instanz"""
    global _config_loader
    if _config_loader is None:
        _config_loader = SimpleConfigLoader(config_path)
    return _config_loader


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Convenience-Funktion zum Config Laden"""
    loader = SimpleConfigLoader(config_path)
    return loader.config
