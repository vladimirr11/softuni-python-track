from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.appliances.appliance import Appliance
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children) -> None:
        count = len(children) + 2
        super().__init__(name=family_name, budget=(salary_one + salary_two), members_count=count)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * count
        
        self.calculate_expenses(self.appliances, self.children)
