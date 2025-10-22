import shutil
columns = shutil.get_terminal_size().columns

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
        print(line.center(columns))


def menu(title, prompt, options):
    print(title.center(columns))
    print()
    for x in options:
        print(f"{x}) {options[x]}".center(columns))
    while True:
        choice=input(prompt.center(columns))
        if choice in options:
            print()
            print(f"You selected: {options[choice]}".center(columns))
            print()
            return choice



def Game_menu():
    while True:
        print("splash()")
        print()
        menu("MAIN MENU", "Choose an option: ", options1)
        if choice == "s":
            #Function for game
        elif choice == "m":
            MatchHistory()
        elif choice == "q":
            return(f"Goodbye!")
        
        
def After_game():
    while True:
        choice=menu("GAME OVER", "Choose an option: ", options2)
        if choice == "r":
            #Function for game
        elif choice == "q":
            return Game_menu()
        
        
################### Match history

#Function for creating a match history
def GameData:
    if result == "O":
        playerO.append("Win")
        playerX.append("Loss")
    elif result == "X":
        playerX.append("Win")
        playerO.append("Loss")
    elif result == "DRAW":
        playerO.append("Draw")
        playerX.append("Draw")
    print(f"Game result: {result}".center(columns))
    return result

playerO =[]
playerX=[]


def chooseplayer():
    n=input("Choose player X or O: ".center(columns)).upper()
    if not playerO and not playerX:
        print("No matches played yet!".center(columns))
    elif n == "O":
        print(f"Player {n}: {playerO}".center(columns))
    elif n == "X":
        print(f"Player {n}: {playerX}".center(columns))
    else:
        print("Player does not exist".center(columns))
    

def MatchHistory():
    chooseplayer()
    choice=menu("", "Choose an option: ", options3)
    if choice == "m":
        Game_menu()
    elif choice == "r":
        MatchHistory()
            
Game_menu()