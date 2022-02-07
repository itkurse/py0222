
age = int(input('Alter eingeben: '))

# Personen jünger als 16 Jahre sind nie berechtigt Alkohol zu trinken
if age < 16:
    print('No')
elif age >= 16 and age <= 20:
    land = input('Aus welchem Land kommst du?')
    if land != 'USA':
        print('Yes')
    else:
        print('No')
else:
    print('Yes, welcome')



# if age < 16:
#     print('No')

# if age >= 16 and age <= 20:
#     land = input('Aus welchem Land kommst du?')
#     if land != 'USA':
#         print('Yes')
#     else:
#         print('No')

# if age > 20:
#     print('Yes, welcome')