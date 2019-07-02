board=[["-" for i in range(7)] for i in range(6)]

def showBoard(board):
    for i in range (len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

def playerMoveCol():
    colSpace = int(input("Enter a space number from 0 - 6: "))
    return colSpace

def checkCol(colSpace):
    if colSpace < 0 or colSpace > 6:
        print("Invalid Move")
        return False
    return True

def checkRow(colSpace, turn):
    if board[0][colSpace] == "X" or board[0][colSpace] == "O":
        print("This Column is FULL")
        return False
    return True

def placeMove(board, colSpace, turn):
    for i in range(5, -1, -1):
        if board[i][colSpace] == "-":
            board[i][colSpace] = turn
            return board

def switchTurn(turnNum):
    if turnNum%2 == 0:
        return "X"
    else:
       return "O"

turn = "X"
turnNum = 0
print("Welcome to Connect Four!")
showBoard(board)

while True:
    print("Player", turn, "goes first")

    goodCol = False
    goodRow = False
    while goodCol == False or goodRow == False:
        colSpace = playerMoveCol()
        goodRow = checkRow(colSpace, turn)
        goodCol = checkCol(colSpace)

    board = placeMove(board, colSpace, turn)
    showBoard(board)

    turnNum += 1
    turn = switchTurn(turnNum)