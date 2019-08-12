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
        
def top_change(board, col,row):
    if board[row][col-1] == 1:
        board[row][col-1] = 0
    else:
        board[row][col-1] = 1
        
def bot_change(board, col, row):
    if board[row][col+1] == 1:
        board[row][col+1] = 0
    else:
        board[row][col+1] = 1
        
def west_change(board,col, row):
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
    if row == 0:
        center_change(board, col, row)
        #check if romving top or bot then move forward
        if col == 0:
            #remove bot and west
            bot_change(board, col, row)
            east_change(board,col, row)
        elif col == 4:
            #remove top and west
            top_change(board, col, row)
            west_change(board, col, row)
        else:
            #just remove west
            top_change(board, col, row)
            bot_change(board, col, row)
            east_change(board, col, row)
            
    elif row == 4:
        center_change(board, col, row)
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
    win_failure_count = 0
    for c in range(COL_COUNT):
        for r in range(COL_COUNT):
            while x != COL_COUNT:
                while y != ROW_COUNT:
                    win_failure_count = win_failure_count + int(board[x][y])
                    y += 1
                x += 1
    print("Count finished" + str(win_failure_count))
    
#Create Randomly on board
def boardGen(board):
    pass







#Create board
board = create_board()
#Game Over (false)
game_over = False
#Counter for turn
turn = 1


while not game_over:
    print(np.flip(board,0))

    #get player inputs
    col = int(input("Please enter the colum you would like to select: "))
    row = int(input("Please enter the row you would like to select: "))

    lights_change(board, col, row)
