from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, 200, price)
        