from project.parking_mall.parking_mall import ParkingMall


class Level2(ParkingMall):
    def __init__(self) -> None:
        ParkingMall.__init__(self, parking_lots=100)
