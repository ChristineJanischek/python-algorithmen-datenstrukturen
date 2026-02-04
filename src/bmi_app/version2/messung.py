"""
Messung Klasse - Version 2
Grundlegende Messung-Klasse ohne Assoziationen
"""


class Messung:
    """
    Repräsentiert eine BMI-Messung mit Gewicht und Größe.
    """
    
    def __init__(self, gewicht, groesse, datum):
        """
        Initialisiert eine Messung.
        
        Args:
            gewicht (float): Gewicht in kg
            groesse (float): Größe in Metern
            datum (str): Datum der Messung im Format YYYY-MM-DD
        """
        self.gewicht = gewicht
        self.groesse = groesse
        self.datum = datum
    
    def berechne_bmi(self):
        """
        Berechnet den BMI-Wert.
        
        Returns:
            float: BMI-Wert
        """
        return self.gewicht / (self.groesse ** 2)
    
    def __str__(self):
        """Gibt eine String-Repräsentation der Messung zurück."""
        bmi = self.berechne_bmi()
        return f"Messung vom {self.datum}: {self.gewicht}kg, {self.groesse}m, BMI: {bmi:.2f}"
