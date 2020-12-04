document = {}
nbValidPassports = 0

def isValidPassport(document):
    hasRequiredFields = True
    hasRequiredFields &= 'byr' in document
    hasRequiredFields &= 'iyr' in document
    hasRequiredFields &= 'eyr' in document
    hasRequiredFields &= 'hgt' in document
    hasRequiredFields &= 'hcl' in document
    hasRequiredFields &= 'ecl' in document
    hasRequiredFields &= 'pid' in document

    return hasRequiredFields


with open("input.txt", "r") as inputFile:
    for line in inputFile:
        if line == '\n':
            if isValidPassport(document):
                nbValidPassports += 1
            document = {}
        
        fields = line.split()
        for field in fields:
            key, value = field.split(':')
            document[key] = value
    
    if isValidPassport(document):
        nbValidPassports += 1

print(nbValidPassports)