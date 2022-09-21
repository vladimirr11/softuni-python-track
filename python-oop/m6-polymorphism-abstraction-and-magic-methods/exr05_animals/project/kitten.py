from exr05_animals.project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender='Female') -> None:
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow'

    def __repr__(self) -> str:
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}'
