import shutil
import os


width=shutil.get_terminal_size().columns


c, r=(7,6)

PLAYER_1="[O]"
PLAYER_2="[X]"
GAME_OVER = False

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
            
            coordinates = (y, int(x))
            
            GAME_OVER = is_win(grid, coordinates)
            
            if(GAME_OVER):
                
                return GAME_OVER
            
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

def is_win(board, coordinates): #requires the grid/board and the current coordinates of the token
    
    row = coordinates[0] #row index
    col = coordinates[1] #column index
    token = board[row][col][1] #saves the second element in that column which will be the token
    
    match = 1
    
    #HANDLES HORIZONTAL WINS
    if(col-1 >= 0):
        #if there is a column before the column user placed their token on
        
        current_col = col-1 #index of column before the on user placed their token on
        
        while(current_col >= 0 and token in board[row][current_col] and match != 4):
            #while there still is a column before the one checked, check if it matches the players token
            #if yes;
            
            match += 1 #add 1 to match
            current_col -= 1 #the column before that one
        
    if(col+1 < 7):
        #if there is a column before the column user placed their token on
        
        current_col = col+1 #index of column after the on user placed their token on
        
        while(current_col < 7 and token in board[row][current_col] and match != 4):
            #while there still is a column after the one checked, check if it matches the players token
            #if yes;
                       
            match += 1 #add 1 to match
            current_col += 1 #the column after that one

    if(match == 4):
        
        return True

    match = 1
    
    #HANDLES VERTICAL WINS
    if(row-1 >= 1):
        #if there is a row before the row user placed their token on
        
        current_row = row-1 #index of row before the on user placed their token on
        
        while(current_row >= 1 and token in board[current_row][col] and match != 4):
            #while there still is a row before the one checked, check if it matches the players token
            #if yes;
            
            match += 1 #add 1 to match
            current_row -= 1 #the row before that one
        
    
    if(row+1 <= 6):
        #if there is a row before the row user placed their token on
        
        current_row = row+1 #index of row before the on user placed their token on
        
        while(current_row <= 6 and token in board[current_row][col] and match != 4):
            #while there still is a row after the one checked, check if it matches the players token
            #if yes;
                       
            match += 1 #add 1 to match
            current_row += 1 #the ro w after that one            
            
                
    if(match == 4):
        
        return True
    
    else: 
        
        return False

def runGame():
    showGrid(board)
    while True:
        GAME_OVER = writeInGrid(board)
        
        if(GAME_OVER):
            
            return
        
        

runGame()

showGrid(board)

Winner = ""

if GAME_PHASE == PLAYER_1:
    Winner = "PLAYER 1"
else:
    Winner = "PLAYER 2"
    
print(f"{Winner} WINS!!!".center(width))