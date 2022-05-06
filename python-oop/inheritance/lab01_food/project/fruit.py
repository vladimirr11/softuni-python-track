import sys
import os
sys.path.insert(0, os.getcwd())

from lab01_food.project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date: str) -> None:
        super().__init__(expiration_date)
        self.name = name