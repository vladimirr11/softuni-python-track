from abc import ABC, abstractmethod
from project.drink.drink import Drink
from project.baked_food.baked_food import BakedFood


class Table(ABC):
    def __init__(self, table_number: int, capacity: int) -> None:
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
    
    @property
    def capacity(self):
        return self.__capacity 

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError('Capacity has to be greater than 0!')
        
        self.__capacity = value
    
    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_bill = 0
        drink_bill = 0
        for food in self.food_orders:
            food_bill += food.price

        for drink in self.drink_orders:
            drink_bill += drink.price
        
        return food_bill + drink_bill 

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0

    def free_table_info(self):
        massage = f''
        if self.is_reserved == False:
            massage += f'Table: {self.table_number}\n'
            massage += f'Type: {self.__class__.__name__}\n'
            massage += f'Capacity: {self.capacity}\n'

        return massage
        