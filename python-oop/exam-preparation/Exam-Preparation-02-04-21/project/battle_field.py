from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')
        
        if attacker.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker_bonus_points = 0
        for card in attacker.card_repository.cards:
            attacker_bonus_points += card.health_points
        attacker.health += attacker_bonus_points
        
        enemy_bonus_points = 0
        for card in enemy.card_repository.cards:
            enemy_bonus_points += card.health_points
        enemy.health += enemy_bonus_points
        
        for card in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return

            enemy.take_damage(card.damage_points)
        
        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            
            attacker.take_damage(card.damage_points)
