from project_func.supply.supply import Supply


class WaterSupply(Supply):
    def __init__(self) -> None:
        super().__init__(needs_increase=40)
