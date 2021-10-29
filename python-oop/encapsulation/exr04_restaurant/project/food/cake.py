import sys, os
sys.path.insert(0, os.getcwd())

from exr04_restaurant.project.food.dessert import Dessert
from exr04_restaurant.project.food.food import Food
from exr04_restaurant.project.food.main_dish import MainDish
from exr04_restaurant.project.food.salmon import Salmon
from exr04_restaurant.project.food.soup import Soup
from exr04_restaurant.project.food.starter import Starter
from exr04_restaurant.project.beverage.beverage import Beverage
from exr04_restaurant.project.beverage.coffee import Coffee
from exr04_restaurant.project.beverage.cold_beverage import ColdBeverage
from exr04_restaurant.project.beverage.hot_beverage import HotBeverage
from exr04_restaurant.project.beverage.tea import Tea
from exr04_restaurant.project.product import Product


class Cake(Dessert):

    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name, price, grams, calories) -> None:
        super().__init__(name, price, grams, calories)


if __name__ == '__main__':
    product = Product('coffee', 2.5)

    print(product.__class__.__name__)
    print(product.name)
    print(product.price)

    beverage = Beverage('coffee', 2.5, 50)

    print(beverage.__class__.__name__)
    print(beverage.__class__.__bases__[0].__name__)
    print(beverage.name)
    print(beverage.price)
    print(beverage.milliliters)

    soup = Soup('fish soup', 9.90, 230)

    print(soup.__class__.__name__)
    print(soup.__class__.__bases__[0].__name__)
    print(soup.name)
    print(soup.price)
    print(soup.grams)

    coffee = Coffee('Illy', 2.46, 30, 45)

    print(coffee.MILLILITERS)
    print(coffee.milliliters)
    print(coffee.name)
    print(coffee.price)
    print(coffee.PRICE)
    print(coffee.caffeine)
