'''
Dictionary: Key-Value Paare
'''

# erstelle dict
person = {
    'first_name': 'Sepp',
    'last_name': 'Peter',
    'age': 40
}

print(person, type(person))

person2 = dict(first_name='Fritz', last_name='Wurst')
print(person2, type(person2))

# auf eine spezielle Eigenschaft der Person zugreifen
# Zugriff über []
print(f"{person['last_name']} {person2['first_name']} ")
# Alternativ: Zugriff über .get()
print(person.get('age'))


# Key/Value zum dict hinzufügen
person['phone'] = 1234
print(person)

person['emails'] = ['sepp@gmail.com', 'seppi@peter.at']
print(person)

person['father'] = person2 
print(person)

# alle Keys
print(person.keys())

# alle Values
print(person.values())

# delete (Löscht ein Key/Value Paar aus dem dict heraus)
del person['father']

# Length (wie viele Keys hat mein dict?)
print('Len: ', len(person), person)

# Key/Value in einer Schleife
for key, val in person.items():
    print(key, val)


# Nur Keys:
for key in person:
    print(key)