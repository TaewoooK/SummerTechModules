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

def winHor(board):
    for i in range(0, 6):
        for j in range (0, 4):
            if board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn:
                return True
    return False

def winVert(board):
    for i in range(0, 7):
        for j in range(0, 4):
            if board[j][i] == turn and board[j+1][i] == turn and board[j+2][i] == turn and board[j+3][i] == turn:
                return True
    return False

turn = "X"
turnNum = 0
win = False
print("Welcome to Connect Four!")
showBoard(board)

while win == False:
    print("Player", turn, "goes first")

    goodCol = False
    goodRow = False
    while goodCol == False:
        colSpace = playerMoveCol()
        goodCol = checkCol(colSpace)
        if goodCol == True:
            goodRow = checkRow(colSpace, turn)
        if goodRow == False:
            goodCol = False
        
    board = placeMove(board, colSpace, turn)
    showBoard(board)

    winHor = winHor(board)
    winVert = winVert(board)

    if winHor or winVert:
        print("WIN!")
        win = True

    turnNum += 1
    turn = switchTurn(turnNum)


