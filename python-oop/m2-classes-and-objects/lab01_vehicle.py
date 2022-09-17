class Vehicle:
    def __init__(self, mileage, max_speed=150) -> None:
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


if __name__ == '__main__':
    car = Vehicle(20)

    print(car.max_speed)
    print(car.mileage)
    print(car.gadgets)
    car.gadgets.append('Hudly Wireless')
    print(car.gadgets)
