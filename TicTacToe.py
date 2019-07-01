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

board = []
good = False
turn = "X"
print("Welcome to TicTacToe")
setBoardDefault(board)
drawBoard(board)

while good == False:
    numSpace = playerMove()
    good = checkMove(numSpace, board)

board = placeMove(board, numSpace, turn)
drawBoard(board)





