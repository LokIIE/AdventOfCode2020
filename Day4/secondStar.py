import re

document = {}
nbValidPassports = 0
skipDocument = False

def isValidPassport(document):
    hasRequiredFields = True
    hasRequiredFields &= 'byr' in document and isValidByr(document['byr'])
    hasRequiredFields &= 'iyr' in document and isValidIyr(document['iyr'])
    hasRequiredFields &= 'eyr' in document and isValidEyr(document['eyr'])
    hasRequiredFields &= 'hgt' in document and isValidHgt(document['hgt'])
    hasRequiredFields &= 'hcl' in document and isValidHcl(document['hcl'])
    hasRequiredFields &= 'ecl' in document and isValidEcl(document['ecl'])
    hasRequiredFields &= 'pid' in document and isValidPid(document['pid'])

    return hasRequiredFields

def isValidByr(value: str):
    return value.isdigit() and 1920 <= int(value) and int(value) <= 2002

def isValidIyr(value: str):
    return value.isdigit() and 2010 <= int(value) and int(value) <= 2020

def isValidEyr(value: str):
    return value.isdigit() and 2020 <= int(value) and int(value) <= 2030

def isValidHgt(value: str):
    if len(value) < 4:
        return False

    height = int(value[:-2])
    if value.endswith('cm'):
        return len(value) == 5 and 150 <= height and height <= 193
    elif value.endswith('in'):
        return len(value) == 4 and 59 <= height and height <= 76

    return False

def isValidHcl(value: str):
    return re.match('#[0-9a-f]', value) != None

def isValidEcl(value: str):
    return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def isValidPid(value: str): 
    return value.isdigit() and len(value) == 9

with open("input.txt", "r") as inputFile:
    for line in inputFile:
        if line == '\n':
            if not skipDocument and isValidPassport(document):
                nbValidPassports += 1
            document = {}
            skipDocument = False
        
        fields = line.split()
        for field in fields:
            if skipDocument:
                pass
            key, value = field.split(':')
            if key in document:
                skipDocument = True
                pass
            document[key] = value
    
    if not skipDocument and isValidPassport(document):
        nbValidPassports += 1

print(nbValidPassports)