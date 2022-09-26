import sys
import os
import unittest
sys.path.insert(0, os.getcwd())

from exercises.hero.project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Hero', 10, 20, 30)

    def test_hero_init_method(self):
        self.assertEqual(self.hero.username, 'Hero')
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 20)
        self.assertEqual(self.hero.damage, 30)

    def test_hero_battle_method_enemy_username_same_as_hero_username_should_raises(self):
        enemy = Hero('Hero', 10, 20, 30)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy.username)

        self.assertIsNotNone(ex.exception)

    def test_hero_battle_method_when_healt_zero_should_raises(self):
        hero = Hero('Hero', 10, 0, 30)
        enemy = Hero('Enemy', 10, 20, 30)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex.exception)

    def test_hero_battle_method_when_healt_negative_should_raises(self):
        hero = Hero('Hero', 10, -6, 30)
        enemy = Hero('Enemy', 20, 3, 30)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex.exception)

    def test_hero_battle_method_when_enemy_healt_zero_should_raises(self):
        hero = Hero('Hero', 10, 4, 30)
        enemy = Hero('Enemy', 20, 0, 30)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex.exception)

    def test_hero_battle_method_when_enemy_healt_negative_should_raises(self):
        hero = Hero('Hero', 10, 4, 30)
        enemy = Hero('Enemy', 20, 0, 30)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex.exception)

    def test_hero_battle_method_damage_correct(self):
        hero = Hero('Hero', 10, 4, 30)
        enemy = Hero('Enemy', 20, 30, 30)

        hero.battle(enemy)

        self.assertEqual(hero.damage, 30)

    def test_hero_battle_method_enemy_health(self):
        hero = Hero('Hero', 10, 4, 30)
        enemy = Hero('Enemy', 20, 30, 30)

        hero.battle(enemy)

        self.assertEqual(enemy.health, -270)

    def test_hero_battle_method_hero_and_enemy_health_bellow_zero(self):
        hero = Hero('Hero', 10, 4, 30)
        enemy = Hero('Enemy', 20, 30, 30)

        result = hero.battle(enemy)

        self.assertEqual('Draw', result)

    def test_hero_battle_method_when_hero_win(self):
        hero = Hero('Hero', 11, 11, 2)
        enemy = Hero('Enemy', 2, 5, 2)

        result = hero.battle(enemy)

        self.assertEqual('You win', result)
        self.assertEqual(hero.level, 12)
        self.assertEqual(hero.health, 12)
        self.assertEqual(hero.damage, 7)

    def test_hero_battle_method_when_hero_lose(self):
        hero = Hero('Hero',  2, 5, 2)
        enemy = Hero('Enemy', 11, 11, 2)

        result = hero.battle(enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(enemy.level, 12)
        self.assertEqual(enemy.health, 12)
        self.assertEqual(enemy.damage, 7)

    def test_hero_str_method(self):
        message = f"Hero Hero: 10 lvl\n" \
                  f"Health: 20\n" \
                  f"Damage: 30\n"

        result = self.hero.__str__()

        self.assertEqual(message, result)


if __name__ == '__main__':
    unittest.main()
