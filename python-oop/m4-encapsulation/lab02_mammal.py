class Mammal:

    __kingdom = 'animals'

    def __init__(self, name, type, sound) -> None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'


if __name__ == '__main__':
    mammal = Mammal('Dog', 'Domestic', 'Bark')
    print(mammal.make_sound())
    print(mammal.get_kingdom())
    print(mammal.info())
