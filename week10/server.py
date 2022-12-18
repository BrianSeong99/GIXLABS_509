from flask import Flask, request
from logic import *

app = Flask(__name__)

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

games_filename = "games.csv"
game = Game(Human('X', "Alice"), Human('O', "Bob"), games_filename)

# IN: mode, player1 name, player2 name
# OUT: board state
@app.route('/newgame', methods=['PUT'])
def newgame():
    args = request.args
    mode = args.get("mode", default=1, type=int)
    player1 = args.get("player1", default="Alice", type=str)
    player2 = args.get("player2", default="Bob", type=str)
    if mode == '1':
        game = Game(Human('X', player1), Human('O', player2), games_filename)
    else:
        game = Game(Human('X', player1), Bot('O', player2), games_filename)
    return game.board.getboardflask()
    

@app.route('/play', methods=['POST'])
def play():
    args = request.args
    player = args.get("player", default="", type=str)
    x = args.get("x", default="0", type=int)
    y = args.get("y", default="0", type=int)
    if player == "X" or player == "O":
        return game.runflask(player, x, y)
    else:
        return "error"
