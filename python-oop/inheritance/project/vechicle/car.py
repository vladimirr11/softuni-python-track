from project.vechicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats: int, fuel_tank: int, fuel_consumption: float, fuel: float) -> None:
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel
    
    @fuel.setter
    def set_fuel(self, amount):
        if self.__fuel + amount < self.fuel_tank:
            self.__fuel = amount
            return
        self.__fuel = 50
    
    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if  fuel_needed <= self.__fuel:
            self.__fuel -= fuel_needed
            return 'We\'ve enjoyed the travel!'
    
    def refuel(self, liters):
        try:
            self.get_capacity(self.fuel_tank, self.__fuel + liters)
            self.__fuel += liters
            return self.__fuel
        except Exception as exep:
            return str(exep)