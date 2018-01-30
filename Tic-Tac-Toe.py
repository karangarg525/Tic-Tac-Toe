import os
def disp_board(board): # for dispalying the board
    #board = [0,'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']helloo
    #os.system("cls")
    print("   |   |")
    print(" " + board[7] + " |" + " " + board[8] + " |" + " " + board[9] + " ")
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[4] + " |" + " " + board[5] + " |" + " " + board[6] + " ")
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[1] + " |" + " " + board[2] + " |" + " " + board[3] + " ")
    print("   |   |")

def player_input(): # for taking the player input
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('player1 you want to be X or O?').upper()
    if marker == 'X':
        return (('X', 'O'))
    else:
        return (('O', 'X'))

def place_marker(board, marker, position): #This function will place the marker on the board
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

import random
def choose_first():
    if random.randint(0,1) == 0:
        return ("Player1")
    else:
        return ("Player2")

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9')
    return int(position)

def replay():
    return input('Do you want to play again? Enter yes or No').lower().startswith('y')

print("Welcome to Tic Tac Toe!")

# Game Starts Here

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn, " will go first!")

    game_on = True

    while game_on:
        if turn == 'Player1':
            disp_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                disp_board(theBoard)
                print("Player1 has won the game!!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    disp_board(theBoard)
                    print("The Game is a draw")
                else:
                    turn = "Player2"
        else:
            disp_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                disp_board(theBoard)
                print("Player2 has won the game!!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The Game is a draw")
                else:
                    turn = "Player1"

    if not replay():
        break
