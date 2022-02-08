'''

a   b   ergebnis
1 x 1 = 1
2 x 1 = 2
…
1 x 2 = 2
2 x 2 = 4
…
10 x 10 = 100

'''

# Lösung: 2 geschachtelte for-Schleifen
for a in range(1, 11):
    for b in range(1, 11):
        ergebnis = a * b
        print(f'{a} x {b} = {ergebnis}')