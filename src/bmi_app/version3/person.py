"""
Person Klasse - Version 3
Person-Klasse mit Assoziation zu Messungen (1:N)
"""


class Person:
    """
    Repräsentiert eine Person mit Namen, Geburtsdatum und zugehörigen Messungen.
    Eine Person kann mehrere Messungen haben (1:N Assoziation).
    """
    
    def __init__(self, name, geburtsdatum):
        """
        Initialisiert eine Person.
        
        Args:
            name (str): Name der Person
            geburtsdatum (str): Geburtsdatum im Format YYYY-MM-DD
        """
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.messungen = []  # Liste der Messungen (N-Seite der Assoziation)
    
    def fuege_messung_hinzu(self, messung):
        """
        Fügt eine Messung zur Person hinzu.
        
        Args:
            messung: Messung-Objekt
        """
        if messung not in self.messungen:
            self.messungen.append(messung)
    
    def entferne_messung(self, messung):
        """
        Entfernt eine Messung von der Person.
        
        Args:
            messung: Messung-Objekt
        """
        if messung in self.messungen:
            self.messungen.remove(messung)
    
    def zeige_messungen(self):
        """
        Gibt alle Messungen der Person zurück.
        
        Returns:
            list: Liste der Messung-Objekte
        """
        return self.messungen
    
    def zeige_messungshistorie(self):
        """
        Gibt eine formatierte Messungshistorie aus.
        """
        print(f"\nMessungshistorie für {self.name}:")
        print("-" * 60)
        if not self.messungen:
            print("Keine Messungen vorhanden.")
        else:
            for i, messung in enumerate(self.messungen, 1):
                print(f"{i}. {messung}")
        print("-" * 60)
    
    def __str__(self):
        """Gibt eine String-Repräsentation der Person zurück."""
        anzahl_messungen = len(self.messungen)
        return f"Person: {self.name}, geboren am {self.geburtsdatum} ({anzahl_messungen} Messungen)"
