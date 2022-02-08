'''
Ein Tuple ist eine Collection deren Elemente eine fixe Reihenfolge 
haben, und der Inhalt (Elemente) eines Tuples ist unveränderbar.

Gemeinsamkeiten Listen und Tuple:
- Listen als auch Tuple speichern eine Collection von Einträgen
- Werte beliebiger Datentypen können in Tuple und Listen gespeichert werden
- Auf Einträge kann über den Index zugegriffen werden

Tuple sind jedoch ...
- Tuple sind nicht veränderbar
- Tuple sind jedoch schneller als Listen

--> Mit Tuple definiert man eine konstante Collection an Einträgen

'''

# Tuple erstellen
fruits = ('Apples', 'Oranges', 'Grapes', 'Oranges')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Tuple mit nur einem Wert: benötigt einen Beistrich am Ende!
f = ('Apples',)

print(fruits, fruits2, f)

# type ausgeben
print('f: ', f, type(f))

# TypeError: 'tuple' object does not support item assignment
#fruits[0] = 'Bananas'

# Wie viele Einträge hat mein Tuple?
print('Len:', len(fruits))

# Auf einen bestimmten Wert zugreifen
print('Erstes Element: ', fruits[0])
print('Letztes Element: ', fruits[ len(fruits) - 1 ])


# lösche die Variable
del fruits



'''
Sets:
Ein Set ist eine unsortierte und nicht-indizierte Collection. 
Ein Set erlaubt KEINE doppelten Inhalte!
'''

# Set erstellen
fruits = {'Apples', 'Oranges', 'Grapes'}

# Element zum Set hinzufügen
fruits.add('Mangos')
fruits.add('Oranges')

print('Inhalt des Set fruits:', fruits)

# Ist ein bestimmtes Element im Set enthalten?
# Sind Mangos im Set enthalten?
if 'Mangos' in fruits:
    print('Mangos sind im Set!')

# Lösche ein Element
fruits.remove('Mangos')

# Alle Elemente im Set ausgeben lassen
for x in fruits:
    print(x)

# clear - lösche den Inhalt des Sets
fruits.clear()

# Wie viele Elemente sind noch im Set?
print('Length: ', len(fruits))