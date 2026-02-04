"""
Person Klasse - Version 2
Grundlegende Person-Klasse ohne Assoziationen
"""


class Person:
    """
    Repräsentiert eine Person mit Namen und Geburtsdatum.
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
    
    def __str__(self):
        """Gibt eine String-Repräsentation der Person zurück."""
        return f"Person: {self.name}, geboren am {self.geburtsdatum}"
