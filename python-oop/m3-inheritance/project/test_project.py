import sys, os
sys.path.insert(0, os.getcwd())

from project.technology.laptop import Laptop
from project.technology.smart_phone import SmartPhone
from project.vechicle.plane import Plane
from project.vechicle.car import Car
from project.vechicle.bus import Bus
from project.vechicle.plane import Plane


if __name__ == '__main__':
    print('------------Car-------------')
    car = Car(4, 50, 7, 10)
    print(car.refuel(10))

    print('\n------------Bus-------------')
    bus = Bus(50, 4)
    bus.get_ticket(31)
    print(bus.get_total_profit())

    print('\n------------Plane-------------')
    plane = Plane(50, 5, 10)
    print(plane.seats_available)
    print(plane.buy_tickets(4, 3))
    print(plane.buy_tickets(4, 8))

    print('\n-----------Laptop--------------')
    laptop = Laptop(1000, 350)
    print(laptop.install_software('opencv', 350))
    print(laptop.install_software('tensorflow', 150))

    print('\n------------SmartPhone----------')
    smart_phone = SmartPhone(300, 100)
    print(smart_phone.install_app('instagram', 100))
    print(smart_phone.install_app('biochem', 101))
