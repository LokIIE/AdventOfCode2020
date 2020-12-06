total = 0
answeredYes = dict()

with open("input.txt", "r") as inputFile:
    for answers in inputFile:
        if answers == '\n':
            total += len(answeredYes.keys())
            answeredYes.clear()
            continue

        for question in answers:
            if question != '\n' and question not in answeredYes.keys():
                answeredYes[question] = True

total += len(answeredYes.keys())
print(total)