"""
Unit tests for BMI App Version 3
Tests the bidirectional associations between Person, Messung and Bmirechner
"""

import sys
import os
import unittest

# Füge den Pfad zum src-Verzeichnis hinzu
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from version3.person import Person
from version3.messung import Messung
from version3.bmirechner import Bmirechner


class TestPerson(unittest.TestCase):
    """Tests für die Person-Klasse"""
    
    def setUp(self):
        """Wird vor jedem Test ausgeführt"""
        self.person = Person("Test Person", "1990-01-01")
    
    def test_person_initialization(self):
        """Test: Person wird korrekt initialisiert"""
        self.assertEqual(self.person.name, "Test Person")
        self.assertEqual(self.person.geburtsdatum, "1990-01-01")
        self.assertEqual(len(self.person.messungen), 0)
    
    def test_person_str(self):
        """Test: String-Repräsentation der Person"""
        expected = "Person: Test Person, geboren am 1990-01-01 (0 Messungen)"
        self.assertEqual(str(self.person), expected)
    
    def test_person_fuege_messung_hinzu(self):
        """Test: Messung kann zur Person hinzugefügt werden"""
        rechner = Bmirechner("Test Rechner")
        messung = Messung(70, 1.75, "2024-01-01", self.person, rechner)
        
        self.assertEqual(len(self.person.messungen), 1)
        self.assertIn(messung, self.person.messungen)
    
    def test_person_entferne_messung(self):
        """Test: Messung kann von der Person entfernt werden"""
        rechner = Bmirechner("Test Rechner")
        messung = Messung(70, 1.75, "2024-01-01", self.person, rechner)
        
        self.person.entferne_messung(messung)
        self.assertEqual(len(self.person.messungen), 0)
        self.assertNotIn(messung, self.person.messungen)


class TestMessung(unittest.TestCase):
    """Tests für die Messung-Klasse"""
    
    def setUp(self):
        """Wird vor jedem Test ausgeführt"""
        self.person = Person("Test Person", "1990-01-01")
        self.rechner = Bmirechner("Test Rechner")
        self.messung = Messung(75, 1.80, "2024-01-01", self.person, self.rechner)
    
    def test_messung_initialization(self):
        """Test: Messung wird korrekt initialisiert"""
        self.assertEqual(self.messung.gewicht, 75)
        self.assertEqual(self.messung.groesse, 1.80)
        self.assertEqual(self.messung.datum, "2024-01-01")
        self.assertEqual(self.messung.hole_person(), self.person)
        self.assertEqual(self.messung.hole_bmirechner(), self.rechner)
    
    def test_messung_berechne_bmi(self):
        """Test: BMI wird korrekt berechnet"""
        bmi = self.messung.berechne_bmi()
        expected_bmi = 75 / (1.80 ** 2)
        self.assertAlmostEqual(bmi, expected_bmi, places=2)
    
    def test_messung_assoziation_zu_person(self):
        """Test: Bidirektionale Assoziation zur Person"""
        # Prüfe, dass Messung in Person-Liste ist
        self.assertIn(self.messung, self.person.messungen)
        # Prüfe, dass Messung die Person referenziert
        self.assertEqual(self.messung.hole_person(), self.person)
    
    def test_messung_assoziation_zu_bmirechner(self):
        """Test: Bidirektionale Assoziation zum Bmirechner"""
        # Prüfe, dass Messung in Rechner-Liste ist
        self.assertIn(self.messung, self.rechner.messungen)
        # Prüfe, dass Messung den Rechner referenziert
        self.assertEqual(self.messung.hole_bmirechner(), self.rechner)
    
    def test_messung_person_wechsel(self):
        """Test: Person einer Messung kann geändert werden"""
        person2 = Person("Zweite Person", "1985-01-01")
        
        # Ändere Person
        self.messung.setze_person(person2)
        
        # Prüfe neue Assoziation
        self.assertEqual(self.messung.hole_person(), person2)
        self.assertIn(self.messung, person2.messungen)
        
        # Prüfe alte Assoziation wurde entfernt
        self.assertNotIn(self.messung, self.person.messungen)
    
    def test_messung_bmirechner_wechsel(self):
        """Test: Bmirechner einer Messung kann geändert werden"""
        rechner2 = Bmirechner("Zweiter Rechner")
        
        # Ändere Rechner
        self.messung.setze_bmirechner(rechner2)
        
        # Prüfe neue Assoziation
        self.assertEqual(self.messung.hole_bmirechner(), rechner2)
        self.assertIn(self.messung, rechner2.messungen)
        
        # Prüfe alte Assoziation wurde entfernt
        self.assertNotIn(self.messung, self.rechner.messungen)


class TestBmirechner(unittest.TestCase):
    """Tests für die Bmirechner-Klasse"""
    
    def setUp(self):
        """Wird vor jedem Test ausgeführt"""
        self.rechner = Bmirechner("Test Rechner")
    
    def test_bmirechner_initialization(self):
        """Test: Bmirechner wird korrekt initialisiert"""
        self.assertEqual(self.rechner.name, "Test Rechner")
        self.assertEqual(len(self.rechner.messungen), 0)
    
    def test_bmirechner_berechne_bmi(self):
        """Test: BMI-Berechnung funktioniert"""
        bmi = self.rechner.berechne_bmi(75, 1.80)
        expected_bmi = 75 / (1.80 ** 2)
        self.assertAlmostEqual(bmi, expected_bmi, places=2)
    
    def test_bmirechner_klassifiziere_untergewicht(self):
        """Test: Untergewicht wird korrekt klassifiziert"""
        self.assertEqual(self.rechner.klassifiziere_bmi(17.0), "Untergewicht")
    
    def test_bmirechner_klassifiziere_normalgewicht(self):
        """Test: Normalgewicht wird korrekt klassifiziert"""
        self.assertEqual(self.rechner.klassifiziere_bmi(22.0), "Normalgewicht")
    
    def test_bmirechner_klassifiziere_uebergewicht(self):
        """Test: Übergewicht wird korrekt klassifiziert"""
        self.assertEqual(self.rechner.klassifiziere_bmi(27.0), "Übergewicht")
    
    def test_bmirechner_klassifiziere_adipositas(self):
        """Test: Adipositas wird korrekt klassifiziert"""
        self.assertEqual(self.rechner.klassifiziere_bmi(32.0), "Adipositas")
    
    def test_bmirechner_fuege_messung_hinzu(self):
        """Test: Messung kann zum Rechner hinzugefügt werden"""
        person = Person("Test Person", "1990-01-01")
        messung = Messung(70, 1.75, "2024-01-01", person, self.rechner)
        
        self.assertEqual(len(self.rechner.messungen), 1)
        self.assertIn(messung, self.rechner.messungen)
    
    def test_bmirechner_entferne_messung(self):
        """Test: Messung kann vom Rechner entfernt werden"""
        person = Person("Test Person", "1990-01-01")
        messung = Messung(70, 1.75, "2024-01-01", person, self.rechner)
        
        self.rechner.entferne_messung(messung)
        self.assertEqual(len(self.rechner.messungen), 0)
        self.assertNotIn(messung, self.rechner.messungen)


class TestAssoziationen(unittest.TestCase):
    """Tests für die Assoziationen zwischen den Klassen"""
    
    def test_bidirektionale_assoziation_person_messung(self):
        """Test: Bidirektionale Assoziation Person-Messung"""
        person = Person("Test Person", "1990-01-01")
        rechner = Bmirechner("Test Rechner")
        messung = Messung(70, 1.75, "2024-01-01", person, rechner)
        
        # Von Person zu Messung
        self.assertIn(messung, person.messungen)
        # Von Messung zu Person
        self.assertEqual(messung.hole_person(), person)
    
    def test_bidirektionale_assoziation_bmirechner_messung(self):
        """Test: Bidirektionale Assoziation Bmirechner-Messung"""
        person = Person("Test Person", "1990-01-01")
        rechner = Bmirechner("Test Rechner")
        messung = Messung(70, 1.75, "2024-01-01", person, rechner)
        
        # Von Bmirechner zu Messung
        self.assertIn(messung, rechner.messungen)
        # Von Messung zu Bmirechner
        self.assertEqual(messung.hole_bmirechner(), rechner)
    
    def test_mehrere_messungen_pro_person(self):
        """Test: Eine Person kann mehrere Messungen haben"""
        person = Person("Test Person", "1990-01-01")
        rechner = Bmirechner("Test Rechner")
        
        messung1 = Messung(70, 1.75, "2024-01-01", person, rechner)
        messung2 = Messung(72, 1.75, "2024-02-01", person, rechner)
        messung3 = Messung(69, 1.75, "2024-03-01", person, rechner)
        
        self.assertEqual(len(person.messungen), 3)
        self.assertIn(messung1, person.messungen)
        self.assertIn(messung2, person.messungen)
        self.assertIn(messung3, person.messungen)
    
    def test_mehrere_messungen_pro_bmirechner(self):
        """Test: Ein Bmirechner kann mehrere Messungen haben"""
        person1 = Person("Person 1", "1990-01-01")
        person2 = Person("Person 2", "1985-01-01")
        rechner = Bmirechner("Test Rechner")
        
        messung1 = Messung(70, 1.75, "2024-01-01", person1, rechner)
        messung2 = Messung(60, 1.65, "2024-02-01", person2, rechner)
        
        self.assertEqual(len(rechner.messungen), 2)
        self.assertIn(messung1, rechner.messungen)
        self.assertIn(messung2, rechner.messungen)
    
    def test_assoziation_konsistenz_bei_aenderung(self):
        """Test: Assoziationen bleiben konsistent bei Änderungen"""
        person1 = Person("Person 1", "1990-01-01")
        person2 = Person("Person 2", "1985-01-01")
        rechner1 = Bmirechner("Rechner 1")
        rechner2 = Bmirechner("Rechner 2")
        
        messung = Messung(70, 1.75, "2024-01-01", person1, rechner1)
        
        # Prüfe initiale Assoziationen
        self.assertIn(messung, person1.messungen)
        self.assertIn(messung, rechner1.messungen)
        
        # Ändere Person
        messung.setze_person(person2)
        
        # Prüfe Konsistenz
        self.assertNotIn(messung, person1.messungen)
        self.assertIn(messung, person2.messungen)
        self.assertEqual(messung.hole_person(), person2)
        
        # Ändere Rechner
        messung.setze_bmirechner(rechner2)
        
        # Prüfe Konsistenz
        self.assertNotIn(messung, rechner1.messungen)
        self.assertIn(messung, rechner2.messungen)
        self.assertEqual(messung.hole_bmirechner(), rechner2)


if __name__ == '__main__':
    unittest.main()
