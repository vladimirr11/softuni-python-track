import sys, os
sys.path.insert(0, os.getcwd())

from exr03_players_and_monsters.project.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
        