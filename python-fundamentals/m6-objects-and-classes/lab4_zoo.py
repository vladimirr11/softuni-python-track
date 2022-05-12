class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name

        if species == 'mammal':
            species_names = self.mammals
        elif species == 'fish':
            species_names = self.fishes
        elif species == 'bird':
            species_names = self.birds

        names = ', '.join(species_names)

        return f'{species} in {zoo_name}: {names}'

    def get_total(self):
        return f'Total animals: {self.__animals}'


if __name__ == '__main__':
    # read input name
    zoo_name = input()

    # instantiate class Zoo
    zoo = Zoo(zoo_name)

    # recieve number of animals
    num_animals = int(input())

    # read the animals
    for animal in range(num_animals):
        species, animal_name = input().split(' ')
        zoo.add_animal(species, animal_name)

    # get the kind of the output species
    output_species = input()

    print(zoo.get_info(output_species))
    print(zoo.get_total())
