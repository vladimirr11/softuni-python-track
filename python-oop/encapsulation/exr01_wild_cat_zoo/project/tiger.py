from exr01_wild_cat_zoo.project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, age, money_for_care=45) -> None:
        super().__init__(name, gender, age, money_for_care)
        