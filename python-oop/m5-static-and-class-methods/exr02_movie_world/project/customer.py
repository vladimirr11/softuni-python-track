class Customer:
    def __init__(self, name, age, id) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = list()

    def __repr__(self) -> str:
        rented_dvds = ', '.join([dvd.name for dvd in self.rented_dvds])
        return f'{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD\'s ({rented_dvds})'
    