from project.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        super().__init__(cost=1.2)
    