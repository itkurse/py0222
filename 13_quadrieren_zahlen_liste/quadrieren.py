

numbers = [1, 2, 3, 4, 5, 6]

for i in range(0, len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)


# Lösung 2
numbers = [1, 2, 3, 4, 5, 6]
for i, number in enumerate(numbers):
    numbers[i] = number ** 2 
print(numbers)
