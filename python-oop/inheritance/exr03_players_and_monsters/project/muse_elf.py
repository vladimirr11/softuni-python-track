import sys, os
sys.path.insert(0, os.getcwd())

from exr03_players_and_monsters.project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)
        