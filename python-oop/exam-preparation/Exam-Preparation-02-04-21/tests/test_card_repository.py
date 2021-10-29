import sys, os
sys.path.insert(0, os.getcwd())

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard

import unittest


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = CardRepository()
    
    def test_init_method(self):
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.cards, [])
    
    def test_add_method_when_player_already_in_list_should_raises(self):
        mc = MagicCard('Mitko')
        self.repo.add(mc)

        with self.assertRaises(Exception) as ex:
            self.repo.add(mc)

        self.assertIsNotNone(str(ex.exception))
    
    def test_add_method_when_player_not_in_list(self):
        mc = MagicCard('Mitko')
        self.repo.add(mc)

        self.assertIsNotNone(self.repo.cards[0], 'Mitko')

    def test_remove_method_when_empty_string_provided_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.repo.remove('')
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_remove_method_when_username_provided(self):
        mc = MagicCard('Mitko')
        self.repo.add(mc)
        self.repo.remove('Mitko')
        
        self.assertEqual(self.repo.cards, [])
    
    def test_find_method(self):
        mc = MagicCard('Mitko')
        self.repo.add(mc)

        resuslt = self.repo.find('Mitko')
        expected_result = 'Mitko'

        self.assertEqual(resuslt.name, expected_result)
    

if __name__ == '__main__':
    unittest.main()
    