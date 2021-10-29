from exr04_need_for_speed.project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel, horse_power)
