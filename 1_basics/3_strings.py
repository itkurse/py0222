'''
Strings sind Zeichenketten (miteinander verkettete einzelne Zeichen)
Strings sind in Python Objekte - alle Strings werden in einfachen oder doppelten Anführungszeichen geschrieben.
Alle Strings haben Methoden - z. B. für die Formatierung oder Texttransformation. 
'''

name = 'Susi'   # str
age = 37        # int 

# concatenate (Zusammenfügen)
# nur Strings können zusammengefügt werden - Lösung: cast to string
print('Hallo mein Name ist ' + name + ' und ich bin ' + str(age) + ' Jahre alt.')

# Argumente nach Position
print('Hallo mein Name ist {name} und ich bin {age} Jahre alt.'.format(name=name, age=age))

# f-Strings seit Python 3.6+
print(f'Hallo mein Name ist {name} und ich bin {age} Jahre alt.')


'''
Strings kennen zwei Operatoren: + und *
+ fügt zwei Strings zusammen
* wiederholt den String
'''
x = 'Hansi' + ' ' + 'Huber'
print('+', x)

x = 'Hansi' * 2 + 'Huber' * 3
print('*', x)


'''
String Methoden - String Transformation
'''
s = 'hello world'

# capitalize() --> auf die runden Klammern achten - weil Methode!
print('capitalize', s.capitalize())
print('title', s.title())
print('upper', s.upper()) # alles in Großbuchstaben
print('lower', s.lower()) # alles in Kleinbuchstaben
print('swapcase', s.title().swapcase())

# Wie viele Zeichen hat der String?
print('Len: ', len(s))

# replace - ersetzt 'world' mit 'everyone'

print(s.replace('world', 'everyone'))
#s = s.replace('world', 'everyone')

# starts with: gibt einen boolean zurück
# Groß- und Kleinschreibung muss übereinstimmen
print('starts with:', s.startswith('hello'))

# ends with: gibt ebenso einen boolean zurück
print('ends with:', s.endswith('world'))

# count - wie oft kommt etwas im String vor?
print('count o:', s.count('o'))

# String aufteilen (Leerzeichen)
print('split (Leerzeichen):', s.split())

# String aufteilen (z. B. l)
print('split (l):', s.split('l'))

# find position (Index beginnt mit 0!)
print('find e:', s.find('e'))

# nur alphanumerisch?
print('alphanumerisch:', s.isalnum())

# nur Buchstaben?
print('nur Buchstaben:', s.isalpha())

# nur numerisch?
print('nur numerisch:', s.isnumeric())