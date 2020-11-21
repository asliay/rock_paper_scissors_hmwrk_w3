import unittest

from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Ashley", "rock")
        self.player_2 = Player("Liam", "scissors")
        self.player_3 = Player("Marisha", "paper")
        self.player_4 = Player("Laura", "rock")
        self.player_5 = Player("Sam", "scissors")
        self.player_6 = Player("Travis", "paper")
        self.player_7 = Player("Matt", "rock")
        self.player_8 = Player("Taliesin", "rock")

        self.game_1 = Game(self.player_1, self.player_2)
        self.game_2 = Game(self.player_3, self.player_4)
        self.game_3 = Game(self.player_5, self.player_6)
        self.game_4 = Game(self.player_7, self.player_8)

        
    
    def test_game_has_player1(self):
        self.assertEqual(self.game_1.first_player, self.player_1)

    def test_game_has_player2(self):
        self.assertEqual(self.game_1.second_player, self.player_2)

    def test_rock_beats_scissors(self):
        result = self.game_1.play_rock_paper_scissors()
        self.assertEqual("Ashley", result)

    def test_paper_beats_rock(self):
        result = self.game_2.play_rock_paper_scissors()
        self.assertEqual("Marisha", result)

    def test_scissors_beats_paper(self):
        result = self.game_3.play_rock_paper_scissors()
        self.assertEqual("Sam", result)

    def test_same_hand_is_draw(self):
        result = self.game_4.play_rock_paper_scissors()
        self.assertEqual(None, result)


