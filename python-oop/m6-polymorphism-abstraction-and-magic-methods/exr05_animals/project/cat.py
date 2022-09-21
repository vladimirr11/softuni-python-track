from exr05_animals.project.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow meow!'

    def __repr__(self) -> str:
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}'
