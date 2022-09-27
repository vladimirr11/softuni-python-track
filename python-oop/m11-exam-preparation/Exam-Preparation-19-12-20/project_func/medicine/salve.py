from project_func.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self) -> None:
        super().__init__(health_increase=50)
        