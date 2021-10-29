from exr04_restaurant.project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters) -> None:
        super().__init__(name, price, milliliters)
