from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self) -> str:
        ...

    def make_sound(self):
        ...
