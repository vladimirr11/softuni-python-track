import sys, os
sys.path.insert(0, os.getcwd())

from exr02_pizza_maker.project.topping import Topping
from exr02_pizza_maker.project.dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, topping_capacity: int, toppings={}) -> None:
        self.name = name
        self.dough = dough
        self.topping_capacity = topping_capacity
        self.toppings = toppings

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('The name cannot be an empty string')
        
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError('You should add dough to the pizza')

        self.__dough = value

    @property
    def topping_capacity(self):
        return self.__topping_capacity

    @topping_capacity.setter
    def topping_capacity(self, value):
        if value <= 0:
            raise ValueError('The topping\'s capacity cannot be less or equal to zero')
        
        self.__topping_capacity = value
    
    def add_topping(self, topping: Topping):
        if topping.topping_type not in self.toppings and self.topping_capacity > len(self.toppings):
            self.toppings[topping.topping_type] = topping.weight
        elif topping.topping_type not in self.toppings and self.topping_capacity <= len(self.toppings):
            raise ValueError('Not enough space for another topping')
        elif topping.topping_type in self.toppings and self.topping_capacity <= len(self.toppings):
            raise ValueError('Not enough space for another topping')
        elif topping.topping_type in self.toppings and self.topping_capacity > len(self.toppings):
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum([v for (_, v) in self.toppings.items()])
        return self.dough.weight + toppings_weight


if __name__ == '__main__':
    tomato_topping = Topping('tomato', 60)

    print(tomato_topping.topping_type)
    print(tomato_topping.weight)

    mushrooms_topping = Topping('Mushroom', 75)

    print(mushrooms_topping.topping_type)
    print(mushrooms_topping.weight)

    mozzarella_topping = Topping('Mozzarella', 80)

    print(mozzarella_topping.topping_type)
    print(mozzarella_topping.weight)

    cheddar_topping = Topping('Cheddar', 150)

    pepperoni_topping = Topping('Pepperoni', 120)

    white_flour_dough = Dough('White Flour', 'Mixing', 200)

    print(white_flour_dough.flour_type)
    print(white_flour_dough.weight)
    print(white_flour_dough.baking_technique)

    whole_wheat_dough = Dough('Whole Wheat Flour', 'Mixing', 200)

    print(whole_wheat_dough.weight)
    print(whole_wheat_dough.flour_type)
    print(whole_wheat_dough.baking_technique)

    p = Pizza('Margherita', whole_wheat_dough, 2)

    p.add_topping(tomato_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
