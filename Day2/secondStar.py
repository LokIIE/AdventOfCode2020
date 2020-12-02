import re

policyRegex = r"(\d+)-(\d+)\s(\w):\s(\w+)"
inputFile = open("input.txt", "r")

countValidPasswords = 0

def isValidPassword(password, character, firstIndex, secondIndex):
    if password[firstIndex] == character:
        return password[secondIndex] != character

    if password[secondIndex] == character:
        return password[firstIndex] != character
    
    return False
    

for line in inputFile:
    policy = re.search(policyRegex, line)
    firstPosition, secondPosition, character, password = policy.groups()
    if isValidPassword(password, character, int(firstPosition) - 1, int(secondPosition) - 1):
        countValidPasswords += 1
    
print(countValidPasswords)