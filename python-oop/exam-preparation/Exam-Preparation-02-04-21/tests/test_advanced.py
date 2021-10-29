import sys, os
sys.path.insert(0, os.getcwd())

from project.player.advanced import Advanced

import unittest


class TestAdvanced(unittest.TestCase):
    def setUp(self) -> None:
        self.advanced_player = Advanced('Mitko')
    
    def test_init_method(self):
        self.assertEqual(self.advanced_player.username, 'Mitko')
        self.assertEqual(self.advanced_player.health, 250)
        self.assertEqual(self.advanced_player.card_repository.__class__.__name__, 'CardRepository')
    

if __name__ == '__main__':
    unittest.main()
