from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class Controller:
    def __init__(self) -> None:
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()
    
    def add_player(self, type, username):
        if type == 'Beginner':
            p = Beginner(username)
            self.player_repository.add(p)

            return f'Successfully added player of type {type} with username: {username}'
        
        p = Advanced(username)
        self.player_repository.add(p)

        return f'Successfully added player of type {type} with username: {username}'

    def add_card(self, type, name):
        if type == 'Magic':
            magic_c = MagicCard(name)
            self.card_repository.add(magic_c)

            return f'Successfully added card of type {type}Card with name: {name}'
        
        trap_c = TrapCard(name)
        self.card_repository.add(trap_c)

        return f'Successfully added card of type {type}Card with name: {name}'

    def add_player_card(self, username, card_name):
        card = [c for c in self.card_repository.cards if c.name == card_name][0]
        for pl in self.player_repository.players:
            if pl.username == username:
                pl.card_repository.add(card)

                return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attack_name, enemy_name):
        enemy = self.player_repository.find(attack_name)
        attacker = self.player_repository.find(enemy_name)

        battle_field = BattleField()
        battle_field.fight(attacker, enemy)

        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def report(self):
        message = f''

        for pl in self.player_repository.players:
            message += f'Username: {pl.username} - Health: {pl.health} - Cards {pl.card_repository.count}\n'
            
            for card in pl.card_repository.cards:
                message += f'### Card: {card.name} - Damage: {card.damage_points}\n'
        
        return message
    