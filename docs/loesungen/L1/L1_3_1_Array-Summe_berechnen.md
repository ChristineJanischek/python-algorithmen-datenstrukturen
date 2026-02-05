---
titel: "Array-Summe berechnen"
level: L1
kategorie: 3
nummer: 1
autor: "Demo-Autor"
datum: 05.02.2026
version: 1.0
---

# Lösung: Array-Summe berechnen

## 📋 Übersicht

- **Level:** L1
- **Kategorie:** 3
- **Komplexität:** O(n) - Lineare Zeitkomplexität, da wir jedes Element einmal besuchen

## 💡 Lösungsansatz

Wir durchlaufen das Array mit einer Schleife und addieren jeden Wert zur Summe.

## 💻 Python-Implementierung

```python
def berechne_summe(zahlen: list[int]) -> int:
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe

# Test
zahlen = [5, 10, 15, 20]
ergebnis = berechne_summe(zahlen)
print(f"Summe: {ergebnis}")
```

## 📝 Erklärung

Die Lösung verwendet eine einfache for-Schleife:
1. Initialisiere `summe` mit 0
2. Für jedes Element im Array: addiere es zur Summe
3. Gib die finale Summe zurück

## ⏱️ Komplexitätsanalyse

O(n) - Lineare Zeitkomplexität, da wir jedes Element einmal besuchen

---

*Erstellt am 05.02.2026 von Demo-Autor*
