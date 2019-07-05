import os

os.system('cls' if os.name == 'nt' else 'clear')

p1TopBoard=[["-" for i in range(10)] for i in range(10)]
p1BottomBoard=[["-" for i in range(10)] for i in range(10)]
p2TopBoard=[["-" for i in range(10)] for i in range(10)]
p2BottomBoard=[["-" for i in range(10)] for i in range(10)]

def showP1Board():
    for i in range(len(p1TopBoard)):
        for j in range(len(p1TopBoard[i])):
            print(p1TopBoard[i][j], end="  ")
        print()
    print()
    for i in range(len(p1BottomBoard)):
        for j in range(len(p1BottomBoard[i])):
            print(p1BottomBoard[i][j], end="  ")
        print()

def showP2Board(p1TopBoard, p1BottomBoard):
    for i in range(len(p1TopBoard)):
        for j in range(len(p1TopBoard[i])):
            print(p1TopBoard[i][j], end="  ")
        print()
    print()
    for i in range(len(p1BottomBoard)):
        for j in range(len(p1BottomBoard[i])):
            print(p1BottomBoard[i][j], end="  ")
        print()

def checkRow(rowNum, spaces, direction):
    if direction == "up":
        if rowNum < (spaces-1):
            print("Invalid Move")
            return False
        return True
    elif direction == "down":
        if rowNum > (10-spaces):
            print("Invalid Move")
            return False
        return True
    
def checkCol(colNum, spaces, direction):
    if direction == "left":
        if colNum < (spaces-1):
            print("Invalid Move")
            return False
        return True
    if direction == "right":
        if colNum > (10-spaces):
            print("Invalid Move")
            return False
        return True

def placeShip(board, rowNum, colNum, spaces, direction):
    for i in range(spaces):
        if direction == "up":
            board[rowNum-i][colNum] = "#"
        elif direction == "down":
            board[rowNum+i][colNum] = "#"
        elif direction == "left":
            board[rowNum][colNum-i] = "#"
        elif direction == "right":
            board[rowNum][colNum+1] = "#"
    return board

def checkOverlap(board, rowNum, colNum, spaces, direction):
    for i in range(spaces):
        if direction == "up":
            if board[rowNum-i][colNum] == "#":
                return True
        elif direction == "down":
            if board[rowNum+i][colNum] == "#":
               return True 
        elif direction == "left":
            if board[rowNum][colNum-i] == "#":
                return True
        elif direction == "right":
            if board[rowNum][colNum+1] == "#":
                return True
    return False

print("Welcome to Battleship!")
print("============================")

showP1Board()
print("============================")
print("Player 1 place down Destroyer (2 Spaces)")

yesRow = False
yesCol = False
overlap = True

while yesRow == False or yesCol == False or overlap == True:
    rowNum = int(input("Row: "))
    colNum = int(input("Column: "))
    direction = input("up, down, left, right: ")

    yesRow = checkRow(rowNum, 2, direction)
    yesCol = checkCol(colNum, 2, direction)
    overlap = checkOverlap(p1BottomBoard, rowNum, colNum, 2, direction)

p1BottomBoard = placeShip(p1BottomBoard, rowNum, colNum, 2, direction)

showP1Board()






