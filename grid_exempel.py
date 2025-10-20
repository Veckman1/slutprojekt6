import shutil
import os


width=shutil.get_terminal_size().columns


c, r=(7,6)

PLAYER_1="[O]"
PLAYER_2="[X]"

GAME_PHASE=PLAYER_1
def makeGrid(rows,cols):
    grid=[["[ ]" for i in range(cols)] for j in range(rows)]
    nr=[]
    nr = [f" {i+1} " for i in range(cols)]
    grid.insert(0, nr)
    for square in grid:
        square.insert(0,"   ")        
    return grid

board=makeGrid(r,c)

def showGrid(grid):
    os.system("cls")
    for row in grid:
        print("".join(row).center(width))
    print()

def writeInGrid(grid):
    global GAME_PHASE
    if GAME_PHASE == PLAYER_1:
        prompt="Player 1 choose column: "
    else:
        prompt="Player 2 choose column: "
    x = input(prompt)
    if x.isdigit():
        if 1 <= int(x) <=len(grid[0])-1:
            y = len(grid) - 1
            while grid[y][int(x)] != "[ ]":
                y -= 1
                if y == 0:
                    print("Invalid input!")
                    print()
                    return
            grid[y][int(x)] = GAME_PHASE
            if GAME_PHASE == PLAYER_1:
                GAME_PHASE=PLAYER_2
                prompt="Player 2 choose column: "
            else:
                GAME_PHASE=PLAYER_1
                prompt="Player 2 choose column: "

        else:
            print("Invalid input!\n")
            return
    else:
        print("Invalid input!\n")
        return
    showGrid(grid)


def runGame():
    showGrid(board)
    while True:
        writeInGrid(board)

runGame()
  

        
