class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person: Person):
        self.people.append(person)

    def names_of_attendees(self):
        return ', '.join([person.name for person in self.people])

    def number_of_guests(self):
        return len(self.people)


if __name__ == '__main__':
    party = Party()

    while True:
        person_name = input()
        if person_name == 'End':
            break

        person = Person(person_name)
        party.invite(person)

    print(f'Going: {party.names_of_attendees()}')
    print(f'Total: {party.number_of_guests()}')
