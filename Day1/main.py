inputFile = open("input.txt", "r")
complements = {}

for line in inputFile:
    number = int(line)
    if complements.get(number) != None:
        print(number * complements.get(number))
        exit()
    complements[2020 - number] = number