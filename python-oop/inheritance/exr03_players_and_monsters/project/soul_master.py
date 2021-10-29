import sys, os
sys.path.insert(0, os.getcwd())

from exr03_players_and_monsters.project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
        