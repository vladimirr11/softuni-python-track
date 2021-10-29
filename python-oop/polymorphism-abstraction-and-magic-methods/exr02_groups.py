class Person:
    def __init__(self, name, surname) -> None:
        self.name = str(name)
        self.surname = str(surname)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'unsopported operand type(s) for +: {self.__class__.__name__} and {self.__class__.__name__}')
        return __class__(name=self.name, surname=other.surname)


class Group:
    def __init__(self, name, people: list) -> None:
        self.name = name
        self.people = people
    
    def __len__(self):
        return len(self.people)
    
    def __add__(self, other):
        new_group_name = self.name + ' ' + other.name

        return __class__(name=new_group_name, people=self.people + other.people)

    def __str__(self):
        return f'Group {self.name} with members {", ".join([person.__str__() for person in self.people])}'
    
    def __getitem__(self, index):
        return f'Person {index}: {self.people[index]}'


if __name__ == '__main__':
    p0 = Person('Aliko', 'Dangote')
    p1 = Person('Bill', 'Gates')
    p2 = Person('Warren', 'Buffet')
    p3 = Person('Elon', 'Musk')

    p4 = p2 + p3

    print(p4)

    first_group = Group('__VIP__', [p0, p1, p2])
    second_group = Group('Special', [p3, p4])

    third_group = first_group + second_group

    print(len(first_group))
    print(second_group)
    print(third_group)
    print(third_group[0])

    for person in third_group:
        print(person)
