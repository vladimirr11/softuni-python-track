class Player:
    def __init__(self, name, sprint, dribble, passing, shooting) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        message = f'Player: {self.name}\n'
        message += f'Sprint: {self.__sprint}\n'
        message += f'Dribble: {self.__dribble}\n'
        message += f'Passing: {self.__passing}\n'
        message += f'Shooting: {self.__shooting}'

        return message
