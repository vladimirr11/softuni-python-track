from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2 * pi

    def calculate_perimeter(self):
        return self.__radius * 2 * pi


class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


if __name__ == '__main__':
    circle = Circle(5)

    print(circle.calculate_area())
    print(circle.calculate_perimeter())
