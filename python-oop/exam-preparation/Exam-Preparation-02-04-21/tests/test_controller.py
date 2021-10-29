import sys, os
sys.path.insert(0, os.getcwd())

from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller

import unittest


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
    
    def test_controller_init_methof(self):
        self.assertEqual(self.controller.player_repository.__class__.__name__, 'PlayerRepository')
        self.assertEqual(self.controller.card_repository.__class__.__name__, 'CardRepository')
    
    def test_controller_add_method_when_beginner_passed(self):
        self.controller.add_player('Beginner', 'Mitko')
        self.assertEqual(self.controller.player_repository.players[0].username, 'Mitko')
        self.assertEqual(self.controller.player_repository.count, 1)

    def test_controller_add_method_when_beginner_passed_should_return(self):
        result = self.controller.add_player('Beginner', 'Mitko')
        expected_result = 'Successfully added player of type Beginner with username: Mitko'
        self.assertEqual(result, expected_result)

    def test_controller_add_method_when_advanced_passed_should_return(self):
        result = self.controller.add_player('Advanced', 'Mitko')
        expected_result = 'Successfully added player of type Advanced with username: Mitko'
        self.assertEqual(result, expected_result)

    def test_controller_add_card_method_when_magic_card_added(self):
        self.controller.add_card('Magic', 'Magic Card')
        self.assertEqual(self.controller.card_repository.cards[0].name, 'Magic Card')
        self.assertEqual(self.controller.card_repository.count, 1)

    def test_controller_add_card_method_when_magic_card_added_should_return(self):
        result = self.controller.add_card('Magic', 'Magic Card')
        expected_result = 'Successfully added card of type MagicCard with name: Magic Card'
        self.assertEqual(result, expected_result)

    def test_controller_add_card_method_when_trap_card_added_should_return(self):
        result = self.controller.add_card('Trap', 'Trap Card')
        expected_result = 'Successfully added card of type TrapCard with name: Trap Card'
        self.assertEqual(result, expected_result)

    def test_controller_add_player_card_method(self):
        mc = MagicCard('Magic')
        pl = Advanced('Mitko')
        self.controller.player_repository.add(pl)
        self.controller.card_repository.add(mc)

        result = self.controller.add_player_card('Mitko', 'Magic')
        expected_result = 'Successfully added card: Magic to user: Mitko'

        self.assertEqual(result, expected_result)

    def test_controller_fight_method(self):
        pl = Advanced('Mitko')
        en = Beginner('Mitko Enemy')

        self.controller.player_repository.add(pl)
        self.controller.player_repository.add(en)

        result = self.controller.fight('Mitko', 'Mitko Enemy')
        expected_result = f'Attack user health 90 - Enemy user health 250'

        self.assertEqual(result, expected_result)
    
    def test_controller_report_method(self):
        result = self.controller.report()
        expected_result = ''

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
