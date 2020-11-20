import unittest

from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Ashley", "Rock")
        self.player_2 = Player("Liam", "Scissors")

        self.game_1 = Game(self.player_1, self.player_2)
    
    def test_game_has_player1(self):
        self.assertEqual(self.game_1.first_player, self.player_1)

    def test_game_has_player2(self):
        self.assertEqual(self.game_1.second_player, self.player_2)