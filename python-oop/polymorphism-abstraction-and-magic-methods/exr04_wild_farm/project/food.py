from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity) -> None:
        self.quantity = int(quantity)


class Vegetable(Food):
    def __init__(self, quantity) -> None:
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity) -> None:
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity) -> None:
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity) -> None:
        super().__init__(quantity)
        