total = 0

answeredYes = dict()
groupCount = 0

with open("input.txt", "r") as inputFile:
    for answers in inputFile:
        if answers == '\n':
            for question in answeredYes:
                if answeredYes[question] == groupCount:
                    total += 1
            answeredYes.clear()
            groupCount = 0
            continue

        groupCount += 1
        for question in answers:
            if question != '\n':
                answeredYes[question] = answeredYes.get(question, 0) + 1

for question in answeredYes:
    if answeredYes[question] == groupCount:
        total += 1
        
print(total)