numbers = []

while True:
    number = input("Entrez un nombre (tapez 'q' pour quitter) : ")
    if number == 'q':
        break
    numbers.append(float(number))

average = sum(numbers) / len(numbers)
print("La moyenne est : ", average)
