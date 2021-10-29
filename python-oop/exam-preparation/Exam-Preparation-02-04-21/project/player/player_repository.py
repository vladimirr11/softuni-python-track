from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []
    
    def add(self, player: Player):
        for p in self.players:
            if p.username == player.username:
                raise ValueError(f'Player {player.username} already exists!')
        
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError('Player cannot be an empty string!')
        
        p = [p for p in self.players if p.username == player]
        if p:
            player_to_remove = p[0]
            self.players.remove(player_to_remove)
            self.count -= 1

    def find(self, username):
        player = [p for p in self.players if p.username == username]
        if player:
            found_player = player[0]

            return found_player
