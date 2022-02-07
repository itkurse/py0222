import random 

def guess_number(high):
    random_number = random.randint(1, high)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Rate eine Zahl zwischen 1 und {high}: '))
        if random_number > guess:
            print('Geratene Zahl zu klein!')
        elif random_number < guess:
            print('Geratene Zahl zu groß!')

    print(f'Gratulation! Du hast die Zahl {random_number} richtig erraten!')

def guess_computer(high):
    print(f'Bitte eine Zufallszahl zwischen 1 und {high} überlegen.')

    # < (gesuchte Zahl ist kleiner als Computer-Versuch)
    # > (gesuchte Zahl ist größer als Computer-Versuch)
    # = (gesuchte Zahl wurde vom Computer gefunden!)

    low = 1
    high = high 
    user_feedback = ''
    while user_feedback != '=':
        guess = random.randint(low, high)
        user_feedback = input(f'Ist {guess} die gesuchte Zahl? (< , >, oder = eingeben)')

        if user_feedback == '<':
            high = guess - 1
        elif user_feedback == '>':
            low = guess + 1 
    
    print(f'Gratulation, {guess} ist die gesuchte Zahl!')

#guess_number(100)
guess_computer(100)