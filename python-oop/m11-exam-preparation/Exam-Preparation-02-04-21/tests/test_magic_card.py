import sys, os
import unittest
sys.path.insert(0, os.getcwd())

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self) -> None:
        self.magic_card = MagicCard('Mitko')
    
    def test_init_method(self):
        self.assertEqual(self.magic_card.name, 'Mitko')
        self.assertEqual(self.magic_card.damage_points, 5)
        self.assertEqual(self.magic_card.health_points, 80)
    

if __name__ == '__main__':
    unittest.main()
