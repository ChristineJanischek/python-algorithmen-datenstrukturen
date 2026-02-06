"""
Bmirechner Klasse - Version 3
BMI-Rechner mit Assoziation zu Messungen (1:N)
"""


class Bmirechner:
    """
    BMI-Rechner zur Berechnung, Klassifizierung und Verwaltung von BMI-Messungen.
    Ein Bmirechner kann mehrere Messungen durchführen (1:N Assoziation).
    """
    
    def __init__(self, name):
        """
        Initialisiert den BMI-Rechner.
        
        Args:
            name (str): Name des BMI-Rechners
        """
        self.name = name
        self.messungen = []  # Liste der Messungen (N-Seite der Assoziation)
    
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
    
    def fuege_messung_hinzu(self, messung):
        """
        Fügt eine Messung zum BMI-Rechner hinzu.
        
        Args:
            messung: Messung-Objekt
        """
        if messung not in self.messungen:
            self.messungen.append(messung)
    
    def entferne_messung(self, messung):
        """
        Entfernt eine Messung vom BMI-Rechner.
        
        Args:
            messung: Messung-Objekt
        """
        if messung in self.messungen:
            self.messungen.remove(messung)
    
    def zeige_messungen(self):
        """
        Gibt alle Messungen des BMI-Rechners zurück.
        
        Returns:
            list: Liste der Messung-Objekte
        """
        return self.messungen
    
    def zeige_statistik(self):
        """
        Zeigt Statistiken über alle durchgeführten Messungen.
        """
        print(f"\nStatistik für {self.name}:")
        print("-" * 60)
        
        if not self.messungen:
            print("Keine Messungen vorhanden.")
        else:
            print(f"Anzahl Messungen: {len(self.messungen)}")
            
            bmis = [m.berechne_bmi() for m in self.messungen]
            durchschnitt_bmi = sum(bmis) / len(bmis)
            min_bmi = min(bmis)
            max_bmi = max(bmis)
            
            print(f"Durchschnittlicher BMI: {durchschnitt_bmi:.2f}")
            print(f"Minimaler BMI: {min_bmi:.2f}")
            print(f"Maximaler BMI: {max_bmi:.2f}")
            
            # Verteilung der Kategorien
            kategorien = {}
            for m in self.messungen:
                bmi = m.berechne_bmi()
                kategorie = self.klassifiziere_bmi(bmi)
                kategorien[kategorie] = kategorien.get(kategorie, 0) + 1
            
            print("\nVerteilung nach Kategorien:")
            for kategorie, anzahl in kategorien.items():
                print(f"  {kategorie}: {anzahl}")
        
        print("-" * 60)
    
    def __str__(self):
        """Gibt eine String-Repräsentation des BMI-Rechners zurück."""
        anzahl_messungen = len(self.messungen)
        return f"BMI-Rechner: {self.name} ({anzahl_messungen} Messungen)"
