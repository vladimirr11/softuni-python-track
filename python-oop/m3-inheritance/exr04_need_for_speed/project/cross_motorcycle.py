from exr04_need_for_speed.project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel, horse_power)
