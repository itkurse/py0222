'''
if/else Bedingungen werden verwendet um etwas (nicht) zu tun, abhängig davon ob 
eine Bedingung True oder False ist
'''

x = 10
y = 5

'''
Vergleichsoperatoren:
== (Gleichheitsoperator)
!= (Ist nicht, ungleich)
< (kleiner als)
> (größer als)
<= (kleiner oder gleich)
>= (größer oder gleich)
'''

if x > y:
    print(f'{x} > {y}')

if x < y:
    print(f'{x} < {y}')
else:
    print(f'{x} > {y}')

if x < y:
    print(f'{x} < {y}')
elif x == y:
    print(f'{x} == {y}')
else:
    print('in allen anderen Fällen')
    print(f'{x} > {y}')


# geschachtelte if
if x > 2:
    if x <= 10:
        print('x ist eine Zahl zwischen 3 und 10')

# Logische Operatoren (and, or, not) - verbinden Bedingungen
if x > 2 and x <= 10:
    print('x ist eine Zahl zwischen 3 und 10')

if x < 0 or x >= 10:
    print('Zahl ist kleiner als 0 oder >= 10')

# not: dreht den Wahrtswert um
if not (x < 0) and x <= 10:
    print('Zahlen von 0 bis 10 sind OK!')

if not (x == y):
    print('x ist nicht y')


'''
Membership Operatoren: in, not, not in
'''
numbers = [1, 2, 3, 4, 5]
y = 3

# ist y in numbers?
if y in numbers:
    print(f'{y} ist in {numbers}')

y = 7
if y not in numbers:
    print(f'{y} nicht in {numbers}')


'''
Identity
Gibt True zurück wenn es die gleichen Objekte sind
--> Es wird nicht der Inhalt der Variable verglichen, sondern die Speicheradresse!
'''
if x is y:
    print('x ist das gleiche Objekt wie y')
