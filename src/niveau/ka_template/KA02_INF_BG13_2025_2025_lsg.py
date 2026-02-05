#1.2 Algorithmus:
#Welches Ergebnis liefert der Algorithmus bei der Eingabe von n = 7 oder 6:
def ermittleErgebnis():
        n = int(input("Eingabe eines Wertes für n:"))
        ergebnis = 0
        for i in range(1,n,1):
            ergebnis = ergebnis + n
            
        print("Lösung Aufgabe 1.2:",ergebnis )

#2.1 Algorithmus:["der", "Hund","bellt"] oder ["die", "Katze","miaut"]
def ermittleSatzAusArray():
        woerter = ["die", "Katze","miaut"]
        ergebnis = ""
        for i in range(0,len(woerter),1):
            ergebnis = ergebnis + " "+  woerter[i] 
        
        print("Lösung Aufgabe 2.1:",ergebnis,"!")

#2.2 Algorithmus: ["der", "Hund","bellt"] oder ["die", "Katze","miaut"]
def ermittleFrageAusArray():
        woerter = ["die", "Katze","miaut"]
        #Tausche
        parke = woerter[0]
        woerter[0] = woerter[2]
        woerter[2] = woerter[1]
        woerter[1] = parke
        
        ergebnis = ""
        #Ausgabe
        for i in range(0,len(woerter),1):
            ergebnis = ergebnis + " "+  woerter[i] 
            
        print("Lösung Aufgabe 2.2:",ergebnis,"?")

#3.1 Algorithmus: Avocados, Kürbis, Gurken oder USB-Sticks,Tastaturen,Monitore
def ermittleRechnungsbetrag():
    #Eingabe: Deklaration und Einlesen
    a = int(input("Anzahl für USB-Sticks:"))
    b = int(input("Anzahl für Tastaturen:"))
    c = int(input("Anzahl für Monitoren:"))
    
    #Verarbeitung: Zuweisung
    rechnungsbetrag = a * 12.50 + b * 29.90 + c * 199.00
    
    #Ausgabe: rechnungsbetrag
    print("Rechnungsbetrag: ",rechnungsbetrag)
    
def ermittleRabattUndRechnungsbetrag():
    #Eingabe: Deklaration und Einlesen
    rechnungsbetrag = int(input("Rechnungsbetrag:"))
    
    #Deklaration und Initialisierung
    rabattbetrag = 0
    
    #Verarbeitung
    #Für rechnungsbetrag>=20
    if(rechnungsbetrag>=20):
        #Zuweisung:
        rabattbetrag = rechnungsbetrag * 0.1
    
    #Deklaration und Initialisierung rabatt = rechnungsbetrag - rabattbetrag
    rabatt = rechnungsbetrag - rabattbetrag

    #Ausgabe
    print("Rabatt:", rabatt)
    print("Rechnungsbetrag:", rabatt)
   
def ermittleBonus():
    #Eingabe: Deklaration und Einlesen
    umsatz = int(input("Gesamtumsatz:"))

    #Verarbeitung
    #Für umsatz>=500
    if(umsatz>=500):
        #Zuweisung:
        bonusbetrag = umsatz * 0.05
        
        #Ausgabe
        print("Bonusbetrag:",bonusbetrag)
    else:
        #Ausgabe
        print("Sie erhalten keinen Bonus!")
        
def sortiereMitBubbleSort():
    #D & I: Array mit Ganzzahlen 
    zahlen = [4, 1, 8, 2, 5, 7]

    #D & I: laenge als Ganzzahl =
    # Anzahl der Elemente des Arrays Zahlen
    laenge = len(zahlen)
    
    #Für i=1 solange 1< länge, Schrittweite 1
    for i in range(1,laenge,1):
        #Für i=1 solange 1< länge, Schrittweite 1
        for j in range(0,laenge -i,1):
            #Ja-Fall
            if(zahlen[j] > zahlen[j+1]):
                #D&I: zwischenspeicher als Ganzahl = zahlen[j]
                zwischenspeicher = zahlen[j]
                #Zuweisungen: rechter Wert an linke Stelle schreiben
                zahlen[j] = zahlen[j+1]
                #Zuweisung: Wert aus dem zwischenspeicher an rechte Stelle schreiben
                zahlen[j+1] = zwischenspeicher
                                            
    #Testausgabe
    print(zahlen)
    
sortiereMitBubbleSort()