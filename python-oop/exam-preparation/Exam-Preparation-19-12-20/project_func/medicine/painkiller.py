from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    def __init__(self) -> None:
        super().__init__(health_increase=20)
