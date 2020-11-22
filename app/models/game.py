import random

class Game():
   
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        
# Compares the possible results and returns winner
    def play_rock_paper_scissors(self):
        if self.first_player.hand == "rock" and self.second_player.hand == "scissors":
            return self.first_player.name
        elif self.second_player.hand == "rock" and self.first_player.hand == "scissors":
            return self.second_player.name

        elif self.first_player.hand == "paper" and self.second_player.hand == "rock":
            return self.first_player.name
        elif self.second_player.hand == "paper" and self.first_player.hand == "rock":
            return self.second_player.name
        
        elif self.first_player.hand == "scissors" and self.second_player.hand == "paper":
            return self.first_player.name
        elif self.second_player.hand == "scissors" and self.first_player == "paper":
            return self.first_player.name

        elif self.first_player.hand == self.second_player.hand:
            return None



        
