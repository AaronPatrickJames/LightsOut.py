import numpy as np
import sys
import os

ROW_COUNT = 5
COL_COUNT = 5

def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

#Check if user selection is selected
def is_valid_location(board, col, row):
    return True


def center_change(board, col, row):
    if board[row][col] == 1:
        board[row][col] = 0
    else:
        board[row][col] = 1
        
def top_change(board, col, row):
    if board[row][col-1] == 1:
        board[row][col-1] = 0
    else:
        board[row][col-1] = 1
        
def bot_change(board, col, row):
    if board[row][col+1] == 1:
        board[row][col+1] = 0
    else:
        board[row][col+1] = 1
        
def west_change(board, col, row):
    if board[row - 1][col] == 1:
        board[row-1][col] = 0
    else:
        board[row-1][col] = 1
        
def east_change(board, col, row):
    if board[row+1][col] == 1:
        board[row+1][col] = 0
    else:
        board[row+1][col] = 1

#turn off clicked light and turn on north, south, east, west lights (do before win check)
def lights_change(board, col, row):
    center_change(board, col, row)
    if row == 0:
        #check if romving top or bot then move forward
        if col == 0:
            #remove bot and west
            top_change(board, col, row)
            east_change(board,col, row)
        elif col == 4:
            #remove top and west
            bot_change(board, col, row)
            east_change(board, col, row)
        else:
            #just remove west
            top_change(board, col, row)
            bot_change(board, col, row)
            east_change(board, col, row)
            
    elif row == 4:
        #check if romving top or bot then move forward
        if col == 0:
            #remove top and east
            bot_change(board, col, row)
            west_change(board,col, row)
        elif col == 4:
            #remove bot and east
            top_change(board, col, row)
            west_change(board, col, row)
        else:
            #just east
            top_change(board, col, row)
            bot_change(board, col, row)
            west_change(board, col, row)
        
    elif row == 1 or row == 2 or row == 3:
        top_change(board, col, row)
        bot_change(board, col, row)
        west_change(board, col, row)
        east_change(board, col, row)
    
#Check for all lights = 0
def win(board, col, row):
    x = 0
    y = 0 
    win_failure_count = 0
    for c in range(COL_COUNT):
        for r in range(COL_COUNT):
            while x != COL_COUNT:
                x += 1
                while y != ROW_COUNT:   
                    win_failure_count = win_failure_count + int(board[x][y])
                    y += 1
                    print(int(y))
                
                
    if win_failure_count >= 1:
        return False
    else:
        return True
    
#Create Randomly on board
def boardGen(board):
    pass







#Create board
board = create_board()
#Game Over (false)
game_over = False
#Counter for turn
turn = 0

#Main Loop
while not game_over:
    turn += 1
    print("Turn: " + str(turn))
    print(np.flip(board,0))

    #get player inputs
    col = int(input("Please enter the colum you would like to select: "))
    row = int(input("Please enter the row you would like to select: "))

    lights_change(board, col, row)
    game_over = win(board, col, row)


    
