"""
Messung Klasse - Version 3
Messung-Klasse mit bidirektionalen Assoziationen zu Person (N:1) und Bmirechner (N:1)
"""


class Messung:
    """
    Repräsentiert eine BMI-Messung mit Gewicht, Größe und Assoziationen.
    Eine Messung gehört zu genau einer Person (N:1) und einem Bmirechner (N:1).
    """
    
    def __init__(self, gewicht, groesse, datum, person, bmirechner):
        """
        Initialisiert eine Messung mit bidirektionalen Assoziationen.
        
        Args:
            gewicht (float): Gewicht in kg
            groesse (float): Größe in Metern
            datum (str): Datum der Messung im Format YYYY-MM-DD
            person: Person-Objekt (1-Seite der Assoziation)
            bmirechner: Bmirechner-Objekt (1-Seite der Assoziation)
        """
        self.gewicht = gewicht
        self.groesse = groesse
        self.datum = datum
        self._person = None
        self._bmirechner = None
        
        # Setze die Assoziationen (bidirektional)
        self.setze_person(person)
        self.setze_bmirechner(bmirechner)
    
    def berechne_bmi(self):
        """
        Berechnet den BMI-Wert.
        
        Returns:
            float: BMI-Wert
        """
        return self.gewicht / (self.groesse ** 2)
    
    def setze_person(self, person):
        """
        Setzt die Assoziation zur Person (bidirektional).
        
        Args:
            person: Person-Objekt
        """
        # Entferne alte Assoziation
        if self._person is not None:
            self._person.entferne_messung(self)
        
        # Setze neue Assoziation
        self._person = person
        if person is not None:
            person.fuege_messung_hinzu(self)
    
    def hole_person(self):
        """
        Gibt die zugehörige Person zurück.
        
        Returns:
            Person: Zugehörige Person
        """
        return self._person
    
    def setze_bmirechner(self, bmirechner):
        """
        Setzt die Assoziation zum BMI-Rechner (bidirektional).
        
        Args:
            bmirechner: Bmirechner-Objekt
        """
        # Entferne alte Assoziation
        if self._bmirechner is not None:
            self._bmirechner.entferne_messung(self)
        
        # Setze neue Assoziation
        self._bmirechner = bmirechner
        if bmirechner is not None:
            bmirechner.fuege_messung_hinzu(self)
    
    def hole_bmirechner(self):
        """
        Gibt den zugehörigen BMI-Rechner zurück.
        
        Returns:
            Bmirechner: Zugehöriger BMI-Rechner
        """
        return self._bmirechner
    
    def __str__(self):
        """Gibt eine String-Repräsentation der Messung zurück."""
        bmi = self.berechne_bmi()
        person_name = self._person.name if self._person else "Unbekannt"
        rechner_name = self._bmirechner.name if self._bmirechner else "Unbekannt"
        kategorie = self._bmirechner.klassifiziere_bmi(bmi) if self._bmirechner else "N/A"
        return (f"Messung vom {self.datum}: {self.gewicht}kg, {self.groesse}m, "
                f"BMI: {bmi:.2f} ({kategorie}) - Person: {person_name}, "
                f"Rechner: {rechner_name}")
