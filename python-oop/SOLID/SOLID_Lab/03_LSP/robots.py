from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type
    
    @abstractmethod
    def senzors_count(self):
        ...


class Android(Robot):

    NUM_SENZORS = 4

    def senzors_count(self):
        return __class__.NUM_SENZORS


class Chappie(Robot):

    NUM_SENZORS = 6

    def senzors_count(self):
        return __class__.NUM_SENZORS


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.senzors_count())


if __name__ == '__main__':
    robots = [Android('Robocop'), Chappie('XIX')]
    count_robot_senzors(robots)
