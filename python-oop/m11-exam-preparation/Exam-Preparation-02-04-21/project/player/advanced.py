from project.player.player import Player


class Advanced(Player):
    def __init__(self, username: str) -> None:
        super().__init__(username, health=250)
        