import sys, os
sys.path.insert(0, os.getcwd())
from exr05_animals.project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age, gender='Male') -> None:
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Hiss'
    
    def __repr__(self) -> str:
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}'
