from exr05_animals.project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Woof!'

    def __repr__(self) -> str:
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}'
