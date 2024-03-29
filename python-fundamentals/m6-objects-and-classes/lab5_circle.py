class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return 2 * self.__pi * (self.diameter / 2)

    def calculate_area(self):
        return self.__pi * (self.diameter / 2) * (self.diameter / 2)

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.__pi * (self.diameter / 2) * (self.diameter / 2)


if __name__ == '__main__':
    # instantiate class Circle
    circle = Circle(10)

    # assigne angle
    angle = 5

    print(f'{circle.calculate_circumference():.2f}')
    print(f'{circle.calculate_area():.2f}')
    print(f'{circle.calculate_area_of_sector(angle):.2f}')
