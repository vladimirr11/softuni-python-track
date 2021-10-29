class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    person = Person('George', 32)
    print(person.get_name())
    print(person.get_age())
    print(person._Person__age)
    