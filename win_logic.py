def is_win(board, coordinates):
    
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

    #HANDLES VERTICAL WINS
    match = 1
    
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
            current_row += 1 #the row after that one            
            
                
    if(match == 4):
        
        return True
    
    else: 
        
        return False