from project_func.supply.supply import Supply


class FoodSupply(Supply):
    def __init__(self) -> None:
        super().__init__(needs_increase=20)
        