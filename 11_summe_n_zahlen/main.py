'''
Schreiben Sie ein Script das die Summe der ersten n natürlichen Zahlen berechnet. Eingabe von n über input. 
Beispiel: n = 5 → 1 + 2 + 3 + 4 + 5 = 15


1 + 2 + 3 + 4 + 5

'''


n = int(input('Bitte eine Zahl eingeben: '))
ergebnis = 0
for zahl in range(1, n + 1):
    ergebnis = ergebnis + zahl 

print(ergebnis)