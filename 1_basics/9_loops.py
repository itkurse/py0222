'''
Schleifen werden oft verwendet um über Sequenzen (Listen, Tuple, Dictionaries, Strings, Sets) zu iterieren. 
'''

people = ['Thomas', 'Philip', 'Fabian', 'Marc']

# simple
for person in people:
    print(f'Aktuelle Person ist {person}')

# break: höre mit der Schleife auf (und fahre nach der Schleife fort) --> beende die Schleife
for person in people:
    if person == 'Fabian':
        break 
    print(f'Die Person ist {person}')

# continue: bricht nur den aktuellen Schleifendurchgang ab, macht mit dem nächsten Schleifendurchgang weiter
for person in people:
    if person == 'Fabian':
        continue
    print(f'Die Person ist {person}')

# range: 0 - 3
for i in range(len(people)):
    print(f'i: {i}, Person: {people[i]}')

# range: 0 - 10
for i in range(0, 11):
    print(i)

# Auf jedes Zeichen im String zugreifen
for zeichen in "Guten Morgen!":
    print(zeichen)


'''
While Schleifen führen bestimmte Statements aus solange eine bestimmte Bedingung erfüllt (True) ist 
'''
count = 0
while count <= 5:
    count += 1
    print(count)
