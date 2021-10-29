class ImageArea:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def __gt__(sefl, other):
        return sefl.get_area() > other.get_area()
    
    def __ge__(sefl, other):
        return sefl.get_area() >= other.get_area()
    
    def __eq__(sefl, other):
        return sefl.get_area() == other.get_area()


if __name__ == '__main__':
    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)

    print(a1 == a2)
    print(a1 != a3)

    print(dir(ImageArea))
    