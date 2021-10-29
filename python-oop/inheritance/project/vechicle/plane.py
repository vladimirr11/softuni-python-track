from project.vechicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, available_seats: int, rows: int, seats_per_row: int) -> None:
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {row: self.seats_per_row for row in range(1, rows + 1)}

    def buy_tickets(self, row_number, tickets_count):
        if row_number > self.rows:
            return f'There is no row {row_number} in the plane!'

        try:
            seats_desired_row = [v for k, v in self.seats_available.items() if k == row_number][0]
            self.get_capacity(seats_desired_row, tickets_count)
            self.seats_available[row_number] -= tickets_count
            return tickets_count
        except Exception:
            return f'Not enough tickets on row {row_number}!'