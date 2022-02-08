'''
Ein Modul ist im Grunde genommen eine Datei die eine Reihe von Funktionen enthält. 
Und diese Datei kann mit einem "import" zu unserer Anwendung hinzugefügt werden. 

Es gibt 
- Core Python Module (sind schon dabei), z. B. random
- Module die über den pip Package Manager installiert werden können - z. B. Django
- Custom Modules (selbst geschriebene Module)
'''

# import core python module
import datetime # importiere das gesamte modul datetime
# ODER nur einen Teil daraus ... 
from datetime import date # importiere date aus dateime 

import time # importiert das gesamte modul time --> time.time()
from time import time # importiere time aus time --> time()


'''
pip modules (package manager)

Ein Modul über den pip package manager installieren
pip install <modulname>
pip install camelcase

Welche Module habe ich schon selbst installiert?
pip freeze

'''
import camelcase 
from camelcase import CamelCase


'''
Eigene Module importieren
'''
import validator 
from validator import validate_password



# direkt über den (großen) datetime import arbeiten
today = datetime.date.today()
print('today: ', today)

# über date (from datetime import date) auf die Funktionen zugreifen
print(date.today())

today = datetime.datetime.today()
print(today)




c = CamelCase()
print(c.hump('hallo welt mir gehts gut'))



# eigenen Validator verwenden
print(validator.validate_email('xy@abc.com'))
print(validate_password('asdfv'))