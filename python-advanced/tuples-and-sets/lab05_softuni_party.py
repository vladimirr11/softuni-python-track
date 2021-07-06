def register_softuni_guests():
    """
    """
    registered_guests = set()
    others = set()

    num_guests = int(input())

    counter = 0
    while True:
        reg_number = input()
        counter += 1
        if reg_number == 'END':
            break

        if counter <= num_guests:
            registered_guests.add(reg_number)
        else:
            others.add(reg_number)

    arrived_guest = [guest for guest in registered_guests.symmetric_difference(others)]
    sorted_arrived_guests = list(sorted(arrived_guest))

    return sorted_arrived_guests


def print_arrived_guests(arrived_guest):
    """
    """
    print(len(arrived_guest))

    return [print(guest) for guest in arrived_guest]


print_arrived_guests(register_softuni_guests())
