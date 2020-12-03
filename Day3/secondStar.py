inputFile = open("input.txt", "r")

grid = []
currLine = 0
currColumnIndexes = [0, 0, 0, 0, 0]
rightSteps = [1, 1, 3, 5, 7]

countTrees = [0, 0, 0, 0, 0]

def slideRight(index, slideCount, max):
    index += slideCount
    if index >= max:
        index = index % max
    
    return index

for line in inputFile:
    lineMaxIndex = len(line) - 1

    if currLine % 2 == 0:
        if line[currColumnIndexes[0]] == "#":
            countTrees[0] += 1
        currColumnIndexes[0] = slideRight(currColumnIndexes[0], rightSteps[0], lineMaxIndex)

    for i in range(1, 5):
        if line[currColumnIndexes[i]] == "#":
            countTrees[i] += 1
        currColumnIndexes[i] = slideRight(currColumnIndexes[i], rightSteps[i], lineMaxIndex)
    
    currLine += 1

result = 1
for nbTrees in countTrees:
    result *= nbTrees

print(result)