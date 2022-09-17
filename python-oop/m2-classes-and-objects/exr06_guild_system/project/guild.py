import sys, os
sys.path.insert(0, os.getcwd())
from exr06_guild_system.project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == 'Unaffiliated':
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'

        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        player = [player for player in self.players if player.name == player_name]
        if player:
            self.players.remove(player[0])
            player.guild = 'Unaffiliated'
            return f'Player {player_name} has been removed from the guild.'

        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        message = f'Guild: {self.name}\n'
        for player in self.players:
            message += f'{player.player_info()}'

        return message


if __name__ == '__main__':
    player = Player('George', 50, 100)

    print(player.add_skill('Shield Break', 20))
    print(player.player_info())

    guild = Guild('UGT')

    print(guild.assign_player(player))
    print(guild.guild_info())
