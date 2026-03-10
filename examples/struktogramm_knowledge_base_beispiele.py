#!/usr/bin/env python3
"""
Beispiel-Verwendung der Struktogramm Knowledge Base

Dieses Script demonstriert die wichtigsten Funktionen der zentralen
Wissensdatenbank für Struktogramm-Standards (BW v2.2).

Autor: python-algorithmen-datenstrukturen
Datum: 10.03.2026
"""

from src.utils.struktogramm_knowledge_base import (
    get_knowledge_base,
    get_operator_syntax,
    get_pattern,
    validate_bw_notation,
    OperatorKategorie
)


def beispiel_1_operatoren_abrufen():
    """Beispiel: Operatoren-Definitionen abrufen"""
    print("=" * 60)
    print("BEISPIEL 1: Operatoren abrufen")
    print("=" * 60)
    
    kb = get_knowledge_base()
    
    # Einzelner Operator
    deklaration = kb.get_operator("deklaration")
    print(f"\nOperator: {deklaration.name}")
    print(f"Syntax: {deklaration.syntax}")
    print(f"Beispiel: {deklaration.beispiel}")
    print(f"Kategorie: {deklaration.kategorie.value}")
    print("\nHinweise:")
    for hinweis in deklaration.hinweise:
        print(f"  - {hinweis}")
    
    # Schnellzugriff nur Syntax
    print(f"\nSchnellzugriff Syntax: {get_operator_syntax('zuweisung')}")


def beispiel_2_pattern_templates():
    """Beispiel: Pattern-Templates verwenden"""
    print("\n" + "=" * 60)
    print("BEISPIEL 2: Pattern-Templates")
    print("=" * 60)
    
    kb = get_knowledge_base()
    
    # Alle verfügbaren Patterns
    patterns = kb.get_all_pattern_templates()
    print(f"\nVerfügbare Patterns: {', '.join(patterns.keys())}")
    
    # Konkretes Pattern abrufen
    print("\n--- Pattern: Summe berechnen ---")
    pattern = get_pattern("summe_berechnen")
    print(pattern)
    
    print("\n--- Pattern: Array durchlaufen ---")
    pattern = get_pattern("array_durchlaufen")
    print(pattern)


def beispiel_3_notation_regeln():
    """Beispiel: BW-Notation-Regeln"""
    print("\n" + "=" * 60)
    print("BEISPIEL 3: BW-Notation-Regeln")
    print("=" * 60)
    
    kb = get_knowledge_base()
    
    # Briefumschlag-Alternative (VERBINDLICH!)
    regel = kb.get_notation_regel("briefumschlag_alternative")
    print(f"\nRegel: {regel['name']}")
    print(f"\nBeschreibung: {regel['beschreibung']}")
    
    print("\nTemplate:")
    print(regel['template'])
    
    print("\nQualitätschecks:")
    for check in regel['qualitaetscheck']:
        print(f"  ✓ {check}")


def beispiel_4_operatoren_nach_kategorie():
    """Beispiel: Operatoren nach Kategorie filtern"""
    print("\n" + "=" * 60)
    print("BEISPIEL 4: Operatoren nach Kategorie")
    print("=" * 60)
    
    kb = get_knowledge_base()
    
    # Alle Array-Operatoren
    print("\n--- Array-Operatoren ---")
    array_ops = kb.get_operators_by_kategorie(OperatorKategorie.ARRAYS)
    for op in array_ops:
        print(f"  • {op.name}: {op.syntax}")
    
    # Alle Kontrollstrukturen
    print("\n--- Kontrollstrukturen ---")
    kontroll_ops = kb.get_operators_by_kategorie(OperatorKategorie.KONTROLLSTRUKTUREN)
    for op in kontroll_ops:
        print(f"  • {op.name}: {op.syntax}")


def beispiel_5_validierung():
    """Beispiel: Syntax-Validierung"""
    print("\n" + "=" * 60)
    print("BEISPIEL 5: Syntax-Validierung")
    print("=" * 60)
    
    kb = get_knowledge_base()
    
    # Gültige Syntax
    test1 = "Deklaration: alter als Ganzzahl"
    is_valid, error = kb.validate_operator_syntax("deklaration", test1)
    print(f"\nTest: '{test1}'")
    print(f"Gültig: {is_valid}")
    
    # Ungültige Syntax
    test2 = "Variable: x"
    is_valid, error = kb.validate_operator_syntax("deklaration", test2)
    print(f"\nTest: '{test2}'")
    print(f"Gültig: {is_valid}")
    if error:
        print(f"Fehler: {error}")
    
    # Mit Convenience-Function
    print(f"\nSchnell-Validierung: {validate_bw_notation('Zuweisung: x = 5', 'zuweisung')}")


def beispiel_6_zusammenfassung_exportieren():
    """Beispiel: Wissens-Zusammenfassung exportieren"""
    print("\n" + "=" * 60)
    print("BEISPIEL 6: Zusammenfassung exportieren")
    print("=" * 60)
    
    kb = get_knowledge_base()
    
    # Statistik
    print(f"\nStatistik:")
    print(f"  • Operatoren: {len(kb.get_all_operators())}")
    print(f"  • Pattern-Templates: {len(kb.get_all_pattern_templates())}")
    print(f"  • Notation-Regeln: {len(kb.get_all_notation_regeln())}")
    print(f"  • Grafik-Formen: {len(kb.get_all_grafik_formen())}")
    
    # Vollständige Zusammenfassung
    # summary = kb.export_knowledge_summary()
    # print("\nVollständige Zusammenfassung:")
    # print(summary[:500] + "...")  # Gekürzt für Beispiel


def main():
    """Hauptfunktion: Alle Beispiele ausführen"""
    print("\n" + "=" * 60)
    print("STRUKTOGRAMM KNOWLEDGE BASE - BEISPIELE")
    print("=" * 60)
    print("\nDieses Script demonstriert die Verwendung der zentralen")
    print("Wissensdatenbank für Struktogramm-Standards (BW v2.2)")
    print()
    
    try:
        beispiel_1_operatoren_abrufen()
        beispiel_2_pattern_templates()
        beispiel_3_notation_regeln()
        beispiel_4_operatoren_nach_kategorie()
        beispiel_5_validierung()
        beispiel_6_zusammenfassung_exportieren()
        
        print("\n" + "=" * 60)
        print("✓ Alle Beispiele erfolgreich ausgeführt!")
        print("=" * 60)
        print()
        
    except Exception as e:
        print(f"\n❌ Fehler: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
