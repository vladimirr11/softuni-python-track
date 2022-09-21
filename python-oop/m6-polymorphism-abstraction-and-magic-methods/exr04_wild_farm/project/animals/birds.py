from exr04_wild_farm.project.food import Fruit, Meat, Seed, Vegetable
from exr04_wild_farm.project.animals.animal import Bird


class Owl(Bird):

    _WEIGHT_GAINED_PER_FOOD = 0.25
    _ALLOWED_FOODS = (Meat, )

    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):

    _WEIGHT_GAINED_PER_FOOD = 0.35
    _ALLOWED_FOODS = (Vegetable, Meat, Fruit, Seed)

    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'
