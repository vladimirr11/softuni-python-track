from exr04_restaurant.project.food.food import Food


class Starter(Food):
    def __init__(self, name, price, grams) -> None:
        super().__init__(name, price, grams)
