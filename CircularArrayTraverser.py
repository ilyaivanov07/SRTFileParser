
twoDimensionalArray = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

colIndex = 0
rowIndex = 0
matrixSize = 4
rowIncrement = 0
colIncrement = 1
result = []

for inner in twoDimensionalArray:
    for val in inner:
        result.append(twoDimensionalArray[rowIndex][colIndex])
        # go down
        if ((rowIndex + colIndex) == (matrixSize - 1)) and (rowIndex < colIndex):
            colIncrement = 0
            rowIncrement = 1
            rowIndex += 1
        # go left
        elif rowIndex == colIndex and rowIndex >= matrixSize/2:
            colIndex -= 1
            colIncrement = -1
            rowIncrement = 0
        # go up
        elif (rowIndex + colIndex) == (matrixSize - 1) and rowIndex > colIndex:
            colIncrement = 0
            rowIncrement = -1
            rowIndex -= 1
        # go right
        elif (rowIndex - colIndex) == 1 and rowIndex < matrixSize/2:
            colIndex += 1
            colIncrement = 1
            rowIncrement = 0
        else:
            colIndex += colIncrement
            rowIndex += rowIncrement
print result
