import shutil
import os
width = shutil.get_terminal_size().columns

options1 = {"s":"Start game", "m":"Match history", "q":"Quit"}
options2 = {"r":"Play again", "q":"Return to menu"}
options3 = {"q":"Return to menu", "r":"Choose another player"}

def splash():
    lines = """
O O O O O O O O O O O
O o o o o o o o o o O
O o Four in a row o O
O o o o o o o o o o O
O O O O O O O O O O O
""".strip().split("\n")
    for line in lines:
        print(line.center(width))


def menu(title, prompt, options):
    print(title.center(width))
    print()
    for x in options:
        print(f"{x}) {options[x]}".center(width))
    while True:
        choice=input(prompt.center(width))
        if choice in options:
            print()
            print(f"You selected: {options[choice]}".center(width))
            print()
            return choice
        else:
            print()
            print("Invalid option, please try again")



def Game_menu():
    splash()
    print()
    choice=menu("MAIN MENU", "Choose an option: ", options1)
    if choice == "s":
        Gamerunning()
    elif choice == "m":
        MatchHistory()
    elif choice == "q":
        print(f"Goodbye!".center(width))
        return
        
        
        
def After_game():
    return menu("GAME OVER", "Choose an option: ", options2)
           
################### Match history


player1 =[]
player2=[]


def chooseplayer():
    n=input("Choose player 1 or 2: ".center(width)).upper()
    if not player1 and not player2:
        print("No matches played yet!".center(width))
    elif n == "1":
        print(f"Player {n}: {player1}".center(width))
    elif n == "2":
        print(f"Player {n}: {player2}".center(width))
    else:
        print("Player does not exist".center(width))
    

def MatchHistory():
    os.system("cls" if os.name == "nt" else "clear")
    chooseplayer()
    choice=menu("", "Choose an option: ", options3)
    if choice == "q":
        Game_menu()
    elif choice == "r":
        MatchHistory()
        
        
#Game Logic
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
        
    if(col+1 < c):
        #if there is a column before the column user placed their token on
        
        current_col = col+1 #index of column after the on user placed their token on
        
        while(current_col < c and token in board[row][current_col] and match != 4):
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
        
    
    if(row+1 <= r):
        #if there is a row before the row user placed their token on
        
        current_row = row+1 #index of row before the on user placed their token on
        
        while(current_row <= r and token in board[current_row][col] and match != 4):
            #while there still is a row after the one checked, check if it matches the players token
            #if yes;
                       
            match += 1 #add 1 to match
            current_row += 1 #the ro w after that one            
                        
    if(match == 4):
        
        return True
    
    
    match = 1 #rests the match variable
    
    #HANDLES WINS DIAOGNALLY - (RIGHT UP AND LEFT DOWN)
    if(col-1 >= 0 and row+1 <= r):
        #if there is a row under and a column behind the box the user placed their token in 
        
        current_col = col-1
        current_row = row+1
        
        while((current_col >= 0 and current_row <= r) and token in board[current_row][current_col] and match != 4):
            #while there is a row under and a column behind the box the user placed their tocken in 
            #check if that has the token
            
            match += 1 
            
            current_col -= 1
            current_row += 1
            #go to the next coordinate, the row under and the column before
    
    if(col+1 < c and row-1 >= 1):
        #if there is a row above and a column after the box the user placed their token in 
        
        current_col = col+1
        current_row = row-1
        
        while((current_col < c and current_row >= 1) and token in board[current_row][current_col] and match != 4):
            #while there is a row above and a column after the box the user placed their tocken in 
            #check if that has the token        
            match += 1 
            
            current_col += 1
            current_row -= 1          
            #go to the next coordinate, the row above and the column after
                
    if(match == 4):
        
        return True
    
    match = 1 #rests the match variable
    
    #HANDLES WINS DIAOGNALLY - (LEFT UP AND RIGHT DOWN)
    if(col+1 < c and row+1 <= r):
        #if there is a row under and a column after the box the user placed their token in 
        
        current_col = col+1
        current_row = row+1
        
        while((current_col < c and current_row <= r) and token in board[current_row][current_col] and match != 4):
            #while there is a row under and a column after the box the user placed their tocken in 
            #check if that has the token
            
            match += 1 
            
            current_col += 1
            current_row += 1
            #go to the next coordinate, the row under and the column after
    
    if(col-1 >= 0 and row-1 >= 1):
        #if there is a row above and a column before the box the user placed their token in 
        
        current_col = col-1
        current_row = row-1
        
        while((current_col >= 0 and current_row >= 1) and token in board[current_row][current_col] and match != 4):
            #while there is a row above and a column before the box the user placed their tocken in 
            #check if that has the token        
            match += 1 
            
            current_col -= 1
            current_row -= 1          
            #go to the next coordinate, the row above and the column before
                
    if(match == 4):
        
        return True
    
    return False

def runGame():
    global board
    board = makeGrid(r, c)
    global GAME_PHASE
    GAME_PHASE = PLAYER_1
    turn = 0
    showGrid(board)
    while True:
        turn += 1
        result = writeInGrid(board)
        if result:
            return False
        if turn == r*c:
            return True
    return True
        
        
             
def Gamerunning():
    DRAW = runGame()
    showGrid(board)
    if not DRAW:
        winner = "PLAYER 1" if GAME_PHASE == PLAYER_1 else PLAYER_2
        print(f"{winner} WINS!!!".center(width))
        if winner == "PLAYER 1":
            player1.append("Win")
            player2.append("Loss")
        else:
            player1.append("Loss")
            player2.append("Win")
    else:
        print("IT WAS A DRAW".center(width))
        player1.append("Draw")
        player2.append("Draw")
    choice = After_game()
    if choice == "r":
        Gamerunning()
    elif choice == "q":
        Game_menu()



Game_menu()