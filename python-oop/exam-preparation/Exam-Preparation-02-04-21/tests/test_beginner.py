import sys, os
sys.path.insert(0, os.getcwd())

from project.player.beginner import Beginner

import unittest


class TestBeginner(unittest.TestCase):
    def setUp(self) -> None:
        self.beginner = Beginner('Mitko')
    
    def test_init_method(self):
        self.assertEqual(self.beginner.username, 'Mitko')
        self.assertEqual(self.beginner.health, 50)
        self.assertEqual(self.beginner.card_repository.__class__.__name__, 'CardRepository')
    

if __name__ == '__main__':
    unittest.main()
