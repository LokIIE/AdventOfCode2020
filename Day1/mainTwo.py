inputFile = open("input.txt", "r")
numbers = []

for line in inputFile:
    number = int(line)
    numbers.append(number)

for num in numbers:
    complements = {}
    for num2 in numbers:
        if complements.get(num2) != None:
            print(num * num2 * complements.get(num2))
            exit()
        complements[2020 - num - num2] = num2