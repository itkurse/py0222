# Eine Variable ist ein Container für einen Wert
# dieser Wert hat einen bestimmten Typ (Datentyp)

# Das ist ein Kommentar über eine Zeile

'''
Das ist ein Kommentar über mehrere Zeilen
'''

"""
Regeln für Variablen:
- Variablennamen sind Case-Sensitive
- Müssen mit einem Buchstaben oder Underscore starten
  -- Underscore am Anfang hat eine eigene Bedeutung (vorerst nicht machen)
- Dürfen Zahlen enthalten, dürfen jedoch nicht mit einer Zahl beginnen
- Besteht der Name aus mehreren Namen (last name), dann wird es mit der Underscore zusammengefügt --> last_name 
- Variablennamen sollten keine Umlaute oder sonstige Sonderzeichen enthalten
"""

# Im Gegensatz zu anderen Sprachen: Kein Datentyp, kein Strichpunkt, kein var, kein $, ... 

x = 1           # int 
y = 2.5         # float 
name = 'Hansi'  # str - in einfachen oder doppelten Anführungszeichen
is_cool = True  # boolean - großen Anfangsbuchstaben beachten! 

print(x, y, name, is_cool)


'''
Variablen können aktualisiert (d. h. überschrieben werden). 
Dabei kann auch Bezug auf den alten Wert der selben Variable genommen werden.
'''
x = x + 5
# ist gleich wie
x += 5

x -= y 
# gleich wie 
x = x - y 


# Welchen Datentyp hat der Wert in der Variable?
print(x, type(x))