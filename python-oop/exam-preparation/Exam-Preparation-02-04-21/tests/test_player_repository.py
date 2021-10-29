import sys, os
from unittest.case import expectedFailure
sys.path.insert(0, os.getcwd())

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository

import unittest


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = PlayerRepository()
    
    def test_init_method(self):
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.players, [])
    
    def test_add_method_when_player_already_in_list_should_raises(self):
        pl = Advanced('Mitko')
        self.repo.add(pl)

        with self.assertRaises(Exception) as ex:
            self.repo.add(pl)

        self.assertIsNotNone(str(ex.exception))
    
    def test_add_method_when_player_not_in_list(self):
        pl = Advanced('Mitko')
        self.repo.add(pl)

        self.assertIsNotNone(self.repo.players[0], 'Mitko')

    def test_remove_method_when_empty_string_provided_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.repo.remove('')
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_remove_method_when_username_provided(self):
        pl = Advanced('Mitko')
        self.repo.add(pl)
        self.repo.remove('Mitko')
        
        self.assertEqual(self.repo.players, [])
    
    def test_find_method(self):
        pl = Advanced('Mitko')
        self.repo.add(pl)

        resuslt = self.repo.find('Mitko')
        expected_result = 'Mitko'

        self.assertEqual(resuslt.username, expected_result)
    

if __name__ == '__main__':
    unittest.main()
