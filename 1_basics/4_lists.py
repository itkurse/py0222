'''
Eine Liste ist eine durchnummerierte Collection,
sie erlaubt doppelte (gleiche) Einträge
'''

# Erstellen einer Liste
numbers = [1, 2, 3, 5]
numbers2 = list((1, 2, 3, 5))
print(numbers, numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Zugriff auf ein einzelnes Listen-Element: Listen sind Zero-Based!
print(fruits[2]) # Grapes

# Wie viele Elemente sind in der Liste?
print('Length: ', len(fruits))

# Wert hinzufügen: append
fruits.append('Mangos')
print(fruits)

# Wert löschen: remove()
fruits.remove('Grapes')
print(fruits)

# Wert anhand des Index löschen: pop(index)
rem = fruits.pop(2)
print(rem, fruits)

# Wert an einem bestimmten Index einfügen: insert(index, wert)
fruits.insert(2, 'Strawberry')
print(fruits)

# User-Eingabe einfügen (über input-Befehl)
#fruit = input('Welche Frucht möchten Sie hinzufügen? ')
# Eingabe ans Ende der Liste hinzufügen
#fruits.append(fruit)

# sortieren
fruits.sort()

# umgekehrt sortieren
fruits.sort(reverse=True)

# reverse
fruits.reverse()

# replace (einen bestehenden Wert ersetzen)
fruits[0] = 'Bananas'

# Iteration einer Liste
for fruit in fruits:
    print(fruit)

for index, value in enumerate(fruits):
    print(index, value)