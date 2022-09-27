import sys, os
sys.path.insert(0, os.getcwd())

from project.rooms.room import Room

from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child


class Everland:
    def __init__(self) -> None:
        self.rooms = []
    
    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = 0
        for room in self.rooms:
            expenses += room.expenses + room.room_cost
        
        return f'Monthly consumptions: {expenses:.2f}$.'
    
    def pay(self):
        message = ''
        for room in self.rooms:
            if room.budget >= (room.expenses + room.room_cost):
                room.budget -= (room.expenses + room.room_cost)
                message += f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left.\n" 
            else:
                self.rooms.remove(room)
                message += f'{room.family_name} does not have enough budget and must leave the hotel.\n'

        message = message.rstrip('\n')
        return message

    def status(self):
        message = ''

        message += f'Total population: {sum([r.members_count for r in self.rooms])}\n'
        for room in self.rooms:
            message += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'

            if room.children:
                counter = 0
                for child in room.children:
                    counter += 1
                    message += f'--- Child {counter} monthly cost: {(30 * child.cost):.2f}$\n'

            if hasattr(room, 'appliances'):
                message += f'--- Appliances monthly cost: {sum([appl.get_monthly_expense() for appl in room.appliances]):.2f}$\n'
        
        return message


everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
