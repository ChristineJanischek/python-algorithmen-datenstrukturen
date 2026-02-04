"""
BMI App - Demonstrationsskript für Version 3
Zeigt die Verwendung der Assoziationen zwischen Person, Messung und Bmirechner.
"""

import sys
import os

# Füge den Pfad zum src-Verzeichnis hinzu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from version3.person import Person
from version3.messung import Messung
from version3.bmirechner import Bmirechner


def main():
    """Hauptfunktion zur Demonstration der BMI App Version 3."""
    
    print("=" * 70)
    print("BMI App Version 3 - Demonstration der Assoziationen")
    print("=" * 70)
    
    # 1. Erstelle Personen
    print("\n1. Erstelle Personen")
    print("-" * 70)
    person1 = Person("Max Mustermann", "1990-05-15")
    person2 = Person("Anna Schmidt", "1985-08-22")
    person3 = Person("Tom Weber", "1995-03-10")
    print(f"Erstellt: {person1}")
    print(f"Erstellt: {person2}")
    print(f"Erstellt: {person3}")
    
    # 2. Erstelle BMI-Rechner
    print("\n2. Erstelle BMI-Rechner")
    print("-" * 70)
    rechner1 = Bmirechner("Standard BMI Rechner")
    rechner2 = Bmirechner("Präzisions BMI Rechner")
    print(f"Erstellt: {rechner1}")
    print(f"Erstellt: {rechner2}")
    
    # 3. Erstelle Messungen (die Assoziationen werden automatisch gesetzt)
    print("\n3. Erstelle Messungen mit automatischen Assoziationen")
    print("-" * 70)
    
    # Messungen für Person 1
    messung1 = Messung(75.5, 1.80, "2024-01-15", person1, rechner1)
    print(f"✓ {messung1}")
    
    messung2 = Messung(74.8, 1.80, "2024-02-01", person1, rechner1)
    print(f"✓ {messung2}")
    
    messung3 = Messung(73.5, 1.80, "2024-02-15", person1, rechner1)
    print(f"✓ {messung3}")
    
    # Messungen für Person 2
    messung4 = Messung(62.0, 1.68, "2024-01-20", person2, rechner2)
    print(f"✓ {messung4}")
    
    messung5 = Messung(63.5, 1.68, "2024-02-10", person2, rechner2)
    print(f"✓ {messung5}")
    
    # Messungen für Person 3
    messung6 = Messung(85.0, 1.75, "2024-01-25", person3, rechner1)
    print(f"✓ {messung6}")
    
    # 4. Zeige Assoziation: Person -> Messungen (1:N)
    print("\n4. Assoziation Person -> Messungen (1:N)")
    print("=" * 70)
    person1.zeige_messungshistorie()
    person2.zeige_messungshistorie()
    person3.zeige_messungshistorie()
    
    # 5. Zeige Assoziation: Bmirechner -> Messungen (1:N)
    print("\n5. Assoziation Bmirechner -> Messungen (1:N)")
    print("=" * 70)
    rechner1.zeige_statistik()
    rechner2.zeige_statistik()
    
    # 6. Zeige Assoziation: Messung -> Person (N:1)
    print("\n6. Assoziation Messung -> Person (N:1)")
    print("-" * 70)
    print(f"Messung 1 gehört zu: {messung1.hole_person()}")
    print(f"Messung 4 gehört zu: {messung4.hole_person()}")
    print(f"Messung 6 gehört zu: {messung6.hole_person()}")
    
    # 7. Zeige Assoziation: Messung -> Bmirechner (N:1)
    print("\n7. Assoziation Messung -> Bmirechner (N:1)")
    print("-" * 70)
    print(f"Messung 1 verwendet: {messung1.hole_bmirechner()}")
    print(f"Messung 4 verwendet: {messung4.hole_bmirechner()}")
    print(f"Messung 6 verwendet: {messung6.hole_bmirechner()}")
    
    # 8. Demonstriere dynamische Änderung der Assoziationen
    print("\n8. Dynamische Änderung der Assoziationen")
    print("-" * 70)
    print(f"Vorher: {person1} hat {len(person1.zeige_messungen())} Messungen")
    print(f"Vorher: {rechner2} hat {len(rechner2.zeige_messungen())} Messungen")
    
    # Ändere die Person einer Messung
    print(f"\nÄndere Person von Messung 3 von {messung3.hole_person().name} zu {person2.name}...")
    messung3.setze_person(person2)
    
    # Ändere den BMI-Rechner einer Messung
    print(f"Ändere BMI-Rechner von Messung 3 von {messung3.hole_bmirechner().name} zu {rechner2.name}...")
    messung3.setze_bmirechner(rechner2)
    
    print(f"\nNachher: {person1} hat {len(person1.zeige_messungen())} Messungen")
    print(f"Nachher: {person2} hat {len(person2.zeige_messungen())} Messungen")
    print(f"Nachher: {rechner1} hat {len(rechner1.zeige_messungen())} Messungen")
    print(f"Nachher: {rechner2} hat {len(rechner2.zeige_messungen())} Messungen")
    
    # 9. Finale Übersicht
    print("\n9. Finale Übersicht aller Assoziationen")
    print("=" * 70)
    person1.zeige_messungshistorie()
    person2.zeige_messungshistorie()
    person3.zeige_messungshistorie()
    
    print("\n" + "=" * 70)
    print("Demonstration abgeschlossen!")
    print("=" * 70)


if __name__ == "__main__":
    main()
