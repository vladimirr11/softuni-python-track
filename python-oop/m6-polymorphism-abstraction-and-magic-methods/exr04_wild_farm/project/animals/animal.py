from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eathen = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def _ALLOWED_FOODS(self):
        pass

    @property
    @abstractmethod
    def _WEIGHT_GAINED_PER_FOOD(self):
        pass

    def feed(self, food):
        if not isinstance(food, self._ALLOWED_FOODS):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += self._WEIGHT_GAINED_PER_FOOD * food.quantity
        self.food_eathen += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight)
        self.wing_size: float = wing_size

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eathen}]'


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight)
        self.living_region: str = living_region

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eathen}]'
