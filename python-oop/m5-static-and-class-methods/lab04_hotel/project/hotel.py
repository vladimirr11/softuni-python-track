import sys, os
sys.path.insert(0, os.getcwd())

from lab04_hotel.project.room import Room


class Hotel:
    def __init__(self, name) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')
    
    def add_room(self, room: Room):
        self.rooms.append(room)
    
    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number and not room.is_taken]
        if room:
            room_to_take = room[0]
            room_to_take.take_room(people)
            self.guests += room_to_take.guests
    
    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number and room.is_taken]
        if room:
            room_to_free = room[0]
            self.guests -= room_to_free.guests
            room_to_free.free_room()
    
    def status(self):
        message = f'Hotel {self.name} has {self.guests} total guests\n'
        message += f'Free rooms: {", ".join([str(r.number) for r in self.rooms if r.is_taken == False])}\n'
        message += f'Taken rooms: {", ".join([str(r.number) for r in self.rooms if r.is_taken])}'

        return message


if __name__ == '__main__':
    hotel = Hotel.from_stars(5)

    first_room = Room(1, 3)
    second_room = Room(2, 2)
    third_room = Room(3, 1)

    hotel.add_room(first_room)
    hotel.add_room(second_room)
    hotel.add_room(third_room)

    hotel.take_room(1, 4)
    hotel.take_room(1, 2)
    hotel.take_room(3, 1)
    hotel.take_room(3, 1)

    print(hotel.status())
