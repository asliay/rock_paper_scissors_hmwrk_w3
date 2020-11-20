import unittest

from app.models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Ashley", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Ashley", self.player_1.name)

    def test_player_has_hand(self):
        self.assertEqual("Rock", self.player_1.hand)