from exr01_wild_cat_zoo.project.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age, salary)
        