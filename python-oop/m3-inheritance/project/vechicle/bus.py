from project.vechicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats: int, ticket_price: float, ticket_sold=0) -> None:
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.ticket_sold = ticket_sold

    def get_ticket(self, ticket_count):
        try:
            self.get_capacity(self.available_seats, self.ticket_sold + ticket_count)
            self.available_seats -= ticket_count
            self.ticket_sold += ticket_count
        except Exception as exep:
            return str(exep)

    def get_total_profit(self):
        return self.ticket_sold * self.ticket_price
