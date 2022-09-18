import sys, os
sys.path.insert(0, os.getcwd())
from exr05_shop.project.product import Product


class Drink(Product):
    def __init__(self, name: str, quantity=10) -> None:
        super().__init__(name, quantity)
        self.quantity = 10


if __name__ == '__main__':
    prod = Product('coca', 20)

    print(prod.quantity)
    print(prod.name)

    drink = Drink('cola')

    print(drink.quantity)
    print(drink.name)
    drink.decrease(5)
    print(drink.quantity)
