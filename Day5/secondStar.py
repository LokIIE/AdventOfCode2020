# From first part, I know the maximum seat ID
maxSeatID = 822

minRow = 0
maxRow = 127
minCol = 0
maxCol = 7

def getBoardingPassId(bpRow: int, bpCol: int):
    return bpRow * 8 + bpCol

# Theoric seats IDs available
freeSeats = list(range(getBoardingPassId(minRow + 1, minCol), maxSeatID + 1))

def getMiddleNumber(a: int, b: int):
    return float.__trunc__((a + b) / 2)

def getBoardingPassRow(bp: str, leftCursor: int, rightCursor: int):
    rowStr = bp[0:7]
    for rowDir in rowStr:
        if rowDir == "B":
            leftCursor = getMiddleNumber(leftCursor, rightCursor) + 1
        elif rowDir == "F":
            rightCursor = getMiddleNumber(leftCursor, rightCursor)

    return leftCursor

def getBoardingPassCol(bp: str, leftCursor: int, rightCursor: int):
    colStr = bp[7:10]
    lastChar = bp[9:10]
    for colDir in colStr:
        if colDir == "R":
            leftCursor = getMiddleNumber(leftCursor, rightCursor) + 1
        elif colDir == "L":
            rightCursor = getMiddleNumber(leftCursor, rightCursor)

    return leftCursor

with open("input.txt", "r") as boardingPassList:
    for boardingPass in boardingPassList:
        row = getBoardingPassRow(boardingPass, minRow, maxRow)
        col = getBoardingPassCol(boardingPass, minCol, maxCol)
        bpId = getBoardingPassId(row, col)
        
        if bpId in freeSeats:
            freeSeats.remove(bpId)

for seatId in freeSeats:
    if seatId - 1 not in freeSeats and seatId + 1 not in freeSeats:
        print(seatId)
        break