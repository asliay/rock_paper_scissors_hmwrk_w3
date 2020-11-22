from flask import render_template
from app import app
from app.models.player import Player
from app.models.game import *


@app.route("/")
def base():
    return render_template("base.html", title="Home")

# Take routes as Rock, Paper, Scissors choices and returns game result 
@app.route("/<choice1>/<choice2>")
def play(choice1, choice2):
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Player 2", choice2)

    game = Game(player_1, player_2)
    winner = game.play_rock_paper_scissors()
    return render_template("result.html", title="Results", player_1 = player_1.name, player_2 = player_2.name, choice1 = choice1, choice2 = choice2, winner= winner)

# -------- EXTENSIONS:  ----------
# Rules page 
@app.route("/rules")
def about():
    return render_template("rules.html")

# front page image:
# <a href="https://www.vecteezy.com/free-vector/rock-paper-scissors">Rock Paper Scissors Vectors by Vecteezy</a>