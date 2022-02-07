

# gibt True zurück wenn es ein Schaltjahr ist, ansonsten False
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True 
    if year % 100 == 0 and year % 400 != 0:
        return False 
    if year % 400 == 0:
        return True 
    return False 

'''
Umwandlung:
str --> int: int(str)
int --> str: str(int)
str --> float: float(str)
'''

while True:
    year = int(input('Jahreszahl eingeben: '))

    if is_leap_year(year):
        print(f'{year} ist ein Schaltjahr!')
    else:
        print(f'{year} ist kein Schaltjahr!')