import sys, os
sys.path.insert(0, os.getcwd())
from exr05_shop.project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        prod = [prod for prod in self.products if prod.name == product_name]
        if prod:
            return prod[0]

    def remove(self, product_name: str):
        prod = [prod for prod in self.products if prod.name == product_name]
        if prod:
            self.products.remove(prod[0])

    def __repr__(self) -> str:
        message = f''
        last_prod = self.products[-1]
        for prod in self.products:
            if prod == last_prod:
                message += f'{prod.name}: {prod.quantity}'
                break

            message += f'{prod.name}: {prod.quantity}\n'

        return message
