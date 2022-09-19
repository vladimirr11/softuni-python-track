from exr04_restaurant.project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters) -> None:
        super().__init__(name, price, milliliters)
