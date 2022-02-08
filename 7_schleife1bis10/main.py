
# schreibt die Zahlen von 1 bis 10, Zeile für Zeile, auf die Konsole
for i in range(1, 11):
    print(i)

# schreibt die Zahlen von 1 bis 10 in einer Zeile auf die Konsole
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for i in range(1, 11):
    if i < 10:
        print(i, end=', ')
    else:
        print(i)