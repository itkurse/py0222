'''
Eine Function ist ein Block mit Code der nur ausgeführt wird, wenn er aufgerufen wird. 
In Python werden keine geschwungenen Klammern verwendet, stattdessen Einrückungen. 
'''

# Function erstellen
# function name: say_hello
# 2 Parameter: name, last_name 
def say_hello(name, last_name='Mustermann'):
    print(f'Hello {name} {last_name}!')

# Function aufrufen (call function)
say_hello('Marc', 'Fenz')
say_hello('Max')

# Function mit Rückgabewert
def addition(a, b):
    total = a + b
    return total        # beende die Funktion (und gebe den angegebenen Wert zurück)

result = addition(3, 4)
print(result)


'''
Eine Lambda-Funktion ist eine kleine anonyme Funktion
Eine Lambda-Funktion kann beliebig viele Argumente, jedoch nur eine Expression haben
'''
get_sum = lambda a, b: a + b 
print(get_sum(3, 4))
