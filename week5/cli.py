# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

if __name__ == '__main__':
    board = make_empty_board()
    winner = '.'
    player = other_player('O')
    while winner == '.':
        print("TODO: take a turn!")
        print_board(board)
        print("Current Player: ", player)
        while True:
            x = input("Please put down your move, in row: ")
            y = input("Please put down your move, in col: ")
            if board[int(x)][int(y)] != '.':
                print("Cannot Place on already used position!")
            else:
                board[int(x)][int(y)] = player
                break
        player = other_player(player)
        winner = get_winner(board)
        print("winner: ", winner)
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        # winner = 'X'  # FIXME
