from project.parking_mall.parking_mall import ParkingMall


class Level3(ParkingMall):
    def __init__(self) -> None:
        ParkingMall.__init__(self, parking_lots=80)
