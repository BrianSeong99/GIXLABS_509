from flask import Flask, request, render_template
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
@app.route('/newgame', methods=['POST'])
def newgame():
    mode = request.form.get("Selection", default="Human", type=str)
    player1 = request.form.get("player1", default="Alice", type=str)
    player2 = request.form.get("player2", default="Bob", type=str)
    if mode == 'Human':
        game = Game(Human('X', player1), Human('O', player2), games_filename)
    else:
        game = Game(Human('X', player1), Bot('O', player2), games_filename)
    return render_template("game.html", board=game.board.getboardflask(), message=game.current_player + "'s Turn", current_turn=game.current_player)
    
@app.route('/play', methods=['POST'])
def play():
    player = request.form.get("player", default=".", type=str)
    x = request.form.get("X", default="0", type=int)
    y = request.form.get("Y", default="0", type=int)
    if player == "X" or player == "O":
        message = game.runflask(player, x, y)
        if message == None:
            return render_template("game.html", board=game.board.getboardflask(), message=game.current_player + "'s Turn", current_turn=game.current_player)
        else:
            return render_template("game.html", board=game.board.getboardflask(), message=message, current_turn=game.current_player)
    else:
        return "error: " + player + " " + str(x) + " " + str(y)