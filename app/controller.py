from flask import render_template
from app import app
from app.models.player import Player
from app.models.game import *

#route showing player choices and printing choice?
@app.route("/")
def base():
    return render_template("base.html", title="Home")

@app.route("/<choice1>/<choice2>")
def play(choice1, choice2):
    #print choices and result of game?
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Player 2", choice2)

    game = Game(player_1, player_2)
    winner = game.play_rock_paper_scissors()
    return render_template("result.html", title="Results", player_1 = player_1.name, player_2 = player_2.name, choice1 = choice1, choice2 = choice2, winner= winner)

    