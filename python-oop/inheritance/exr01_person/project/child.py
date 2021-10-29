import sys, os
sys.path.insert(0, os.getcwd())

from exr01_person.project.person import Person


class Child(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)


if __name__ == '__main__':
    person = Person('Peter', 25)

    child = Child('Peter Junior', 5)

    print(person.name)
    print(person.age)
    print(child.__class__.__bases__[0].__name__)
