from exr04_need_for_speed.project.vehicle import Vehicle


class Car(Vehicle):

    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
