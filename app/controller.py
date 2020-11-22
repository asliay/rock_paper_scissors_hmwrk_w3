import random
from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import Game



# Take routes as Rock, Paper, Scissors choices and returns game result 
@app.route("/<choice1>/<choice2>")
def play_route(choice1, choice2):
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Player 2", choice2)

    game = Game(player_1, player_2)
    winner = game.play_rock_paper_scissors()
    return render_template("result.html", title="Results", player_1 = player_1.name, player_2 = player_2.name, choice1 = choice1, choice2 = choice2, winner= winner)

# -------- EXTENSIONS:  ----------

# Rules/ Welcome page 
@app.route("/")
def about():
    return render_template("rules.html", title="Rules")

# Form for playing against the computer
@app.route("/play")
def play():
    return render_template("play.html", title="Play")

#Results page once name and move are submitted vs. computer  
@app.route("/play_the_computer", methods = ["POST"])
def play_the_computer():
    player = Player(request.form["name"], request.form["move"])
    move_list = ["rock", "paper", "scissors"]
    computer = Player("SUPER COMPUTER", random.choice(move_list))
    game = Game(player, computer)
    winner = game.play_rock_paper_scissors()
    return render_template("play_the_computer.html", title = "Game vs. Computer Results", player_1 = player.name, player_2 = computer.name, move1 = player.hand, move2 = computer.hand, winner = winner)