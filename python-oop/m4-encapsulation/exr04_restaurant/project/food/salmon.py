from exr04_restaurant.project.food.main_dish import MainDish


class Salmon(MainDish):

    GRAMS = 22

    def __init__(self, name, price, grams) -> None:
        super().__init__(name, price, grams)
