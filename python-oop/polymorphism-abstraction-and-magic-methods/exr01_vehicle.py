from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):

    ADD_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel_to_drive = distance * (self.fuel_consumption + __class__.ADD_CONSUMPTION)
        if needed_fuel_to_drive < self.fuel_quantity:
            self.fuel_quantity -= needed_fuel_to_drive

        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel

        return self.fuel_quantity


class Truck(Vehicle):

    ADD_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel_to_drive = distance * (self.fuel_consumption + __class__.ADD_CONSUMPTION)
        if needed_fuel_to_drive < self.fuel_quantity:
            self.fuel_quantity -= needed_fuel_to_drive

        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)

        return self.fuel_quantity
        

if __name__ == '__main__':
    car = Car(20, 5)
    
    car.drive(3)
    print(car.fuel_quantity)
    car.refuel(10)
    print(car.fuel_quantity)

    truck = Truck(100, 15)

    truck.drive(5)
    print(truck.fuel_quantity)
    truck.refuel(50)
    print(truck.fuel_quantity)
