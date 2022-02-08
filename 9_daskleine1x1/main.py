'''
Ausgabe des kleinen 1x1 auf der Konsole
'''

'''
a   b   ergebnis
1 x 2 = 2
'''

b = int(input('1x1 für welche Zahl? '))
for a in range(1, 11):
    ergebnis = a * b
    print(f'{a} x {b} = {ergebnis}')
