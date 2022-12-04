# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':
    mode = input("Please choose your game mode, 1 for playing against players, 2 for playing against bot: ")
    player1 = input("Please input player1's name: ")
    player2 = input("Please input player2's name: ")
    games_filename = "games.csv"
    if mode == '1':
        game = Game(Human('X', player1), Human('O', player2), games_filename)
        game.run()
    else:
        game = Game(Human('X', player1), Bot('O', player2), games_filename)
        game.run()
