from exr04_restaurant.project.food.starter import Starter


class Soup(Starter):
    def __init__(self, name, price, grams) -> None:
        super().__init__(name, price, grams)
