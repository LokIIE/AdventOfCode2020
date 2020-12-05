minRow = 0
maxRow = 127
minCol = 0
maxCol = 7

maxBpId = 0

def getMiddleNumber(a: int, b: int):
    return float.__trunc__((a + b) / 2)

def getBoardingPassRow(bp: str, minRow: int, maxRow: int):
    rowStr = bp[0:6]
    lastChar = bp[6:7]
    for rowDir in rowStr:
        if rowDir == "B":
            minRow = getMiddleNumber(minRow, maxRow) + 1
        elif rowDir == "F":
            maxRow = getMiddleNumber(minRow, maxRow)

    if lastChar == "B":
        return maxRow
    else: 
        return minRow

def getBoardingPassCol(bp: str, minCol: int, maxCol: int):
    colStr = bp[7:9]
    lastChar = bp[9:10]
    for colDir in colStr:
        if colDir == "R":
            minCol = getMiddleNumber(minCol, maxCol) + 1
        elif colDir == "L":
            maxCol = getMiddleNumber(minCol, maxCol)

    if lastChar == "L":
        return minCol
    else:
        return maxCol

def getBoardingPassId(bpRow: int, bpCol: int):
    return bpRow * 8 + bpCol

with open("input.txt", "r") as boardingPassList:
    for boardingPass in boardingPassList:
        row = getBoardingPassRow(boardingPass, minRow, maxRow)
        col = getBoardingPassCol(boardingPass, minCol, maxCol)

        bpId = getBoardingPassId(row, col)

        if bpId > maxBpId:
            maxBpId = bpId

print(maxBpId)
