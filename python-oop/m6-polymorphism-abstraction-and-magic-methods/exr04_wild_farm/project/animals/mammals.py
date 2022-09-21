import sys, os
sys.path.insert(0, os.getcwd())

from exr04_wild_farm.project.animals.animal import Mammal, Bird, Animal
from exr04_wild_farm.project.animals.birds import Owl, Hen
from exr04_wild_farm.project.food import Food, Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):

    _WEIGHT_GAINED_PER_FOOD = 0.1
    _ALLOWED_FOODS = (Vegetable, Fruit)

    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):

    _WEIGHT_GAINED_PER_FOOD = 0.4
    _ALLOWED_FOODS = (Meat, )

    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):

    _WEIGHT_GAINED_PER_FOOD = 0.3
    _ALLOWED_FOODS = (Vegetable, Meat)

    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):

    _WEIGHT_GAINED_PER_FOOD = 1.00
    _ALLOWED_FOODS = ()

    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return 'ROAR!!!'


if __name__ == '__main__':
    owl = Owl('Pip', 10, 10)
    print(owl)

    meat = Meat(4)
    print(owl.make_sound())
    owl.feed(meat)

    veg = Vegetable(1)
    print(owl.feed(veg))
    print(owl)
