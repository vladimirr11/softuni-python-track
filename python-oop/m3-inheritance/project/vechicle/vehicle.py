from project.capacity_mixin import CapacityMixin


class Vehicle(CapacityMixin):
    def __init__(self, available_seats: int) -> None:
        self.available_seats = available_seats
