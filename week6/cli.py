# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':
    mode = input("Please choose your game mode, 1 for playing against players, 2 for playing against bot: ")
    if mode == '1':
        game = Game(Human('X'), Human('O'))
        game.run()
    else:
        game = Game(Human('X'), Bot('O'))
        game.run()
