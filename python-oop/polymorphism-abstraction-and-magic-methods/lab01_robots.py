class Robot:

    NUM_SENSORS = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return __class__.NUM_SENSORS


class MedicalRobot(Robot):

    NUM_SENSORS = 6

    @staticmethod
    def sensors_amount():
        return __class__.NUM_SENSORS


class ChefRobot(Robot):

    NUM_SENSORS = 4

    @staticmethod
    def sensors_amount():
        return __class__.NUM_SENSORS


class WarRobot(Robot):

    NUM_SENSORS = 12

    @staticmethod
    def sensors_amount():
        return __class__.NUM_SENSORS


def number_of_robot_sensors(robot):
    """
    """
    print(robot.sensors_amount())
    

if __name__ == '__main__':
    basic_robot = Robot('Robo')
    da_vinci = MedicalRobot('Da Vinci')
    moley = ChefRobot('Moley')
    griffin = WarRobot('Griffin')

    number_of_robot_sensors(basic_robot)
    number_of_robot_sensors(da_vinci)
    number_of_robot_sensors(moley)
    number_of_robot_sensors(griffin)
