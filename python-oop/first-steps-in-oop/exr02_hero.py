class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    
    def defend(self, demage: int):
        self.health -= demage

        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'
        
    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)

print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
