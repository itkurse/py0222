
monate = ['Jänner', 'Februar', 'März', 'April', 'Mai', 
'Juni', 'Juli', 'August', 'September', 'Oktober', 
'November', 'Dezember']

# task 1: Monate Zeile für Zeile ausgeben
for monat in monate:
    print(monat)

# task 2: Monate mit Beistrich getrennt in einer Zeile ausgeben
for monat in monate:
    if monat != 'Dezember':
        print(monat, end=', ')
    else:
        print(monat)

# task 2: nach dem letzten Element kein Beistrich!
for index, monat in enumerate(monate):
    # index des letzten Listen-Elements: len(monate) - 1
    if len(monate) - 1 == index:
        print(monat)
    else:
        print(monat, end=', ')
    