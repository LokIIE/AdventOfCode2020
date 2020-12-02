import re

policyRegex = r"(\d+)-(\d+)\s(\w):\s(\w+)"
inputFile = open("input.txt", "r")

countValidPasswords = 0

def isValidPassword(password, character, minCount, maxCount):
    charCount = 0
    for letter in password:
        if letter == character:
            charCount += 1
    
    if charCount < minCount or charCount > maxCount:
        return False
    
    return True

for line in inputFile:
    policy = re.search(policyRegex, line)
    minCount, maxCount, character, password = policy.groups()
    if isValidPassword(password, character, int(minCount), int(maxCount)):
        countValidPasswords += 1
    
print(countValidPasswords)
