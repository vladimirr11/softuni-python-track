from exr04_restaurant.project.food.food import Food


class MainDish(Food):
    def __init__(self, name, price, grams) -> None:
        super().__init__(name, price, grams)
        