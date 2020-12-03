inputFile = open("input.txt", "r")

grid = []
currColumn = 0

countTrees = 0

for line in inputFile:
    if line[currColumn] == "#":
        countTrees += 1
    
    currColumn += 3
    if currColumn >= (len(line) - 1):
        currColumn = currColumn % (len(line) - 1)

print(countTrees)