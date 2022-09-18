import sys, os
sys.path.insert(0, os.getcwd())
from exr03_players_and_monsters.project.hero import Hero


class Elf(Hero):
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)


if __name__ == '__main__':
    hero = Hero('Hero', 4)

    print(hero.username)
    print(hero.level)
    print(str(hero))

    elf = Elf('Elf', 4)

    print(str(elf))
    print(elf.__class__.__bases__[0].__name__)
    print(elf.username)
    print(elf.level)
