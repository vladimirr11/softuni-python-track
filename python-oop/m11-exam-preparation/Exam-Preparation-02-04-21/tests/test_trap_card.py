import sys, os
import unittest
sys.path.insert(0, os.getcwd())

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self) -> None:
        self.trap_card = TrapCard('Mitko')
    
    def test_init_method(self):
        self.assertEqual(self.trap_card.name, 'Mitko')
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)
    

if __name__ == '__main__':
    unittest.main()
