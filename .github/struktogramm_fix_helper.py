#!/usr/bin/env python
"""
Struktogramm Korrektur-Helper
Hilft Autoren, Dateien mit fehlenden grafischen Struktogrammen zu identifizieren
und zu korrigieren.

Verwendung:
    python .github/struktogramm_fix_helper.py [dateipath]
"""

import sys
from pathlib import Path
import re


def find_python_blocks_without_struktogramm(file_path: Path):
    """
    Findet Python-Blöcke ohne vorhergehendes grafisches Struktogramm
    """
    print(f"\n📄 Analysiere: {file_path}")
    print("=" * 70)
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"❌ Fehler beim Lesen: {e}")
        return
    
    lines = content.split('\n')
    
    # Finde alle Python-Code-Blöcke
    python_blocks = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("```python"):
            # Finde Ende
            end = i + 1
            while end < len(lines) and not lines[end].strip().startswith("```"):
                end += 1
            
            python_blocks.append((i, end))
            i = end
        else:
            i += 1
    
    print(f"\n✓ Gefunden: {len(python_blocks)} Python-Code-Block(e)")
    
    issues = []
    for block_start, block_end in python_blocks:
        # Prüfe davor
        context_start = max(0, block_start - 20)
        context = '\n'.join(lines[context_start:block_start])
        
        has_graphic = any(char in context for char in ['┌', '├', '└', '│', '─', '┼'])
        has_section = "Struktogramm" in context or "Grafische Notation" in context
        
        if not (has_graphic or has_section):
            code_snippet = lines[block_start+1:min(block_start+3, block_end)]
            issues.append({
                'line': block_start + 1,
                'type': 'missing_graphic_struktogramm',
                'code': '\n'.join(code_snippet[:2]),
            })
    
    # Zeige Issues
    if issues:
        print(f"\n🚨 Probleme gefunden: {len(issues)}\n")
        for i, issue in enumerate(issues, 1):
            print(f"  Problem {i} (Zeile {issue['line']}):")
            print(f"  Typ: {issue['type']}")
            print(f"  Code: {issue['code'][:60]}...")
            print("  → Bitte ein grafisches Struktogramm VORHER hinzufügen!")
            print()
    else:
        print("\n✅ Keine Probleme gefunden!")


def suggest_template(file_type):
    """
    Zeigt ein Template für die richtige Struktur
    """
    templates = {
        'loesung': """
## 📐 Struktogramm (grafische Notation)

```
┌──────────────────────────────────────────┐
│ Deklaration und Initialisierung:         │
│ summe = 0                                │
├──────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 1              │
│ │                                       │
│ │    Zuweisung: summe = summe + i       │
│ │                                       │
└─┘──────────────────────────────────────────┘
└──────────────────────────────────────────┘
```

## 💻 Python-Implementierung

```python
summe = 0
for i in range(n):
    summe += i
```
        """,
        'pruefung': """
**Erwartetes Struktogramm (BW-Standard - Grafische Notation):**

```
┌──────────────────────────────────────────┐
│ [Ihre grafische Notation hier]           │
│ mit ┌ │ ├ └ und ─                        │
└──────────────────────────────────────────┘
```

**Python-Code (Musterlösung):**
```python
# Code hier
```
        """,
        'aufgabe': """
## 💡 Hinweis zur Lösung

Die Lösung sollte folgende Schritte umfassen:

1. Variablen initialisieren
2. Schleife implementieren
3. Ergebnis ausgeben

**Struktogramm-Notation erwünscht** (grafische Notation mit ┌ │ ├ └)
        """,
    }
    
    return templates.get(file_type, templates['loesung'])


def main():
    if len(sys.argv) < 2:
        print("Verwendung: python struktogramm_fix_helper.py [dateipfad]")
        print("\nBeispiele:")
        print("  python .github/struktogramm_fix_helper.py docs/loesungen/L1/test.md")
        print("  python .github/struktogramm_fix_helper.py docs/pruefungen/pruefung.md")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ Datei nicht gefunden: {file_path}")
        sys.exit(1)
    
    find_python_blocks_without_struktogramm(file_path)
    
    # Zeige Template basierend auf Dateityp
    print("\n" + "=" * 70)
    print("📝 TEMPLATE FÜR KORREKTE STRUKTUR:")
    print("=" * 70)
    
    path_str = str(file_path)
    if 'loesungen' in path_str:
        file_type = 'loesung'
    elif 'pruefungen' in path_str:
        file_type = 'pruefung'
    elif 'aufgaben' in path_str:
        file_type = 'aufgabe'
    else:
        file_type = 'loesung'
    
    print(suggest_template(file_type))
    
    print("\n💡 TIPPS:")
    print("  • Verwende nur die grafischen Box-Zeichen: ┌ ├ ┤ └ │ ─")
    print("  • Python-Code sollte NACH dem Struktogramm stehen")
    print("  • Siehe: docs/handbuch/STRUKTOGRAMM_INTEGRATION_GUIDE.md")
    print("  • Siehe: struktogramme/Operatorenliste-Struktogramme.md")


if __name__ == "__main__":
    main()
