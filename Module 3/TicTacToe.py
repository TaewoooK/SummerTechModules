def setBoardDefault(board):
    for  i in range(0, 10):
        board.append("-")

def drawBoard(board):
    for i in range(1, 10):
        print(board[i], end=" ")
        if i%3 == 0:
            print()

def playerMove():
    numSpace = int(input("Enter a space number from 1 - 9: "))
    return numSpace

def checkMove(numSpace, board):
    if numSpace < 1 or numSpace > 9:
        print("Invalid Space")
        return False
    if board[numSpace] != "-":
        print("Invalid Space")
        return False

def placeMove(board, numSpace, turn):
    board[numSpace] = turn
    return board

def switchTurn(turnNum):
    if turnNum%2==0:
        return "X"
    else:
        return "O"

def checkCol(board, turn):
    if board[1] == turn and board[4] == turn and board[7] == turn:
        return True
    elif board[2] == turn and board[5] == turn and board[8] == turn:
        return True
    elif board[3] == turn and board[6] == turn and board[9] == turn:
        return True
    else:
        return False

def checkRow(board, turn):
    if board[1] == turn and board[2] == turn and board[3] == turn:
        return True
    elif board[4] == turn and board[5] == turn and board[6] == turn:
        return True
    elif board[7] == turn and board[8] == turn and board[9] == turn:
        return True
    else:
        return False

board = []
turnNum = 0
win = False
turn = "X"

print("Welcome to TicTacToe")

setBoardDefault(board)
drawBoard(board)

while win == False:
    print("Player", turn, end="")
    print("'s turn")

    goodMove = False

    while goodMove == False:
        numSpace = playerMove()
        goodMove = checkMove(numSpace, board)

    board = placeMove(board, numSpace, turn)
    drawBoard(board)

    win = checkCol(board, turn)
    if win == False:
        win = checkRow(board, turn)

    turnNum+=1
    turn = switchTurn(turnNum)

turn = switchTurn(turnNum-1)
print("PLAYER", turn, "WINS!")
