# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':
    board = make_empty_board()
    winner = '.'
    player = other_player('O')
    while winner == '.':
        print_board(board)
        print("Current Player: ", player)
        while True:
            x = input("Please put down your move, in row: ")
            y = input("Please put down your move, in col: ")
            if x.isnumeric() == False or y.isnumeric() == False:
                print("Please input in numbers")
                continue
            x = int(x)
            y = int(y)
            if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0:
                print("Please input the number within the board size")
                continue
            if board[int(x)][int(y)] != '.':
                print("Cannot Place on already used position!")
            else:
                board[int(x)][int(y)] = player
                break
        player = other_player(player)
        winner = get_winner(board)
        print()
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        # winner = 'X'  # FIXME
    print("winner: ", winner)
