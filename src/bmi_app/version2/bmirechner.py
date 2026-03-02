"""
Bmirechner Klasse - Version 2
Grundlegender BMI-Rechner ohne Assoziationen
"""


class Bmirechner:
    """
    BMI-Rechner zur Berechnung und Klassifizierung von BMI-Werten.
    """
    
    def __init__(self, name):
        """
        Initialisiert den BMI-Rechner.
        
        Args:
            name (str): Name des BMI-Rechners
        """
        self.name = name
    
    def berechne_bmi(self, gewicht, groesse):
        """
        Berechnet den BMI-Wert.
        
        Args:
            gewicht (float): Gewicht in kg
            groesse (float): Größe in Metern
            
        Returns:
            float: BMI-Wert
        """
        return gewicht / (groesse ** 2)
    
    def klassifiziere_bmi(self, bmi):
        """
        Klassifiziert einen BMI-Wert.
        
        Args:
            bmi (float): BMI-Wert
            
        Returns:
            str: BMI-Kategorie
        """
        if bmi < 18.5:
            return "Untergewicht"
        elif bmi < 25:
            return "Normalgewicht"
        elif bmi < 30:
            return "Übergewicht"
        else:
            return "Adipositas"
    
    def __str__(self):
        """Gibt eine String-Repräsentation des BMI-Rechners zurück."""
        return f"BMI-Rechner: {self.name}"
