'''
Walt Disney sagte einst, “Alle Träume können wahr werden, wenn wir den Mut haben, ihnen zu folgen.”
'''

def say_quote(quote, author):
    print(f'{author} sagte einst, "{quote}"')

zitat = input('Bitte das Zitat eingeben: ')
person = input('Von welcher Person stammt das Zitat? ')

say_quote(zitat, person)