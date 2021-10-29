from exr04_need_for_speed.project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel, horse_power)
        self.fuel_consumption = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
        