import sys, os
sys.path.insert(0, os.getcwd())
from exr04_need_for_speed.project.car import Car
from exr04_need_for_speed.project.vehicle import Vehicle


class FamilyCar(Car):
    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel, horse_power)


if __name__ == '__main__':
    vehicle = Vehicle(50, 150)

    print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
    print(vehicle.fuel)
    print(vehicle.horse_power)
    print(vehicle.fuel_consumption)
    vehicle.drive(100)
    print(vehicle.fuel)

    family_car = FamilyCar(150, 150)

    print(family_car.DEFAULT_FUEL_CONSUMPTION)
    print(family_car.fuel_consumption)
    family_car.drive(50)
    print(family_car.fuel)
    family_car.drive(50)
    print(family_car.fuel)
    print(family_car.__class__.__bases__[0].__name__)
