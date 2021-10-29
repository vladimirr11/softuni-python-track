import sys, os
sys.path.insert(0, os.getcwd())

from project.battle_field import BattleField
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.player.player import Player
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard

import unittest


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.enemy = Advanced('Chicho Mitko')
        self.beginner = Beginner('Mitko')

        self.battle_filed = BattleField()

    def test_battle_field_fight_method_when_player_is_death(self):
        with self.assertRaises(ValueError) as ex:
            self.enemy.health = 0
            self.battle_filed.fight(self.beginner, self.enemy)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_battle_field_fight_method_when_attacker_is_beginner_health_should_increase(self):
        self.battle_filed.fight(self.beginner, self.enemy)
        self.assertEqual(self.beginner.health, 90)
        self.assertEqual(self.enemy.health, 250)
    
    def test_battle_field_fight_method_when_attacker_is_beginner_cards_damage_points_should_increase(self):
        magic_card = MagicCard('Magic card')
        trap_card = TrapCard('Trap Card')

        self.beginner.card_repository.add(magic_card)
        self.enemy.card_repository.add(trap_card)

        self.battle_filed.fight(self.beginner, self.enemy)
        
        self.assertEqual(self.beginner.health, 50)
        self.assertEqual(self.enemy.health, 220)

    def test_battle_field_fight_method_when_player_dies(self):
        magic_card = MagicCard('Magic card')
        trap_card = TrapCard('Trap Card')
        trap_card2 = TrapCard('Trap Card2')

        self.beginner.card_repository.add(magic_card)
        self.enemy.card_repository.add(trap_card)
        self.enemy.card_repository.add(trap_card2)
        
        with self.assertRaises(Exception) as ex:
            self.battle_filed.fight(self.beginner, self.enemy)

        self.assertIsNotNone(str(ex.exception))


if __name__ == '__main__':
    unittest.main()
