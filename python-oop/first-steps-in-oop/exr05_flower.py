class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
    
    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True
    
    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'


flower = Flower("Flowy", 10)

print(flower.name)
print(flower.water_requirements)
print(flower.is_happy)

flower.water(15)
print(flower.status())
flower.water(5)
print(flower.status())
flower.water(5)
print(flower.status())
flower.water(15)
print(flower.status())
