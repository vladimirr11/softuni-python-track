animals_sounds_dict = {'cat': 'meow',
                       'dog': 'woof-woof',
                       'chicken': 'kwaa-kwaa'}


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species in animals_sounds_dict:
            print(animals_sounds_dict[animal.species])


if __name__ == '__main__':
    animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
    animal_sound(animals)
