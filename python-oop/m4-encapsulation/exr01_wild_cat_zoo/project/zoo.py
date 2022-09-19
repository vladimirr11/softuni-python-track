import sys, os
sys.path.insert(0, os.getcwd())

from exr01_wild_cat_zoo.project.animal import Animal
from exr01_wild_cat_zoo.project.worker import Worker
from exr01_wild_cat_zoo.project.caretaker import Caretaker
from exr01_wild_cat_zoo.project.cheetah import Cheetah
from exr01_wild_cat_zoo.project.keeper import Keeper
from exr01_wild_cat_zoo.project.lion import Lion
from exr01_wild_cat_zoo.project.tiger import Tiger
from exr01_wild_cat_zoo.project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return f'Not enough budget'
        else:
            return 'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        workers_lst = [w for w in self.workers if w.name == worker_name]
        if workers_lst:
            fired_worker = workers_lst[0]
            self.workers.remove(fired_worker)
            return f'{worker_name} fired successfully'
        
        return f'There is no {worker_name} in the zoo'
    
    def pay_workers(self):
        total_workers_salary = sum([worker.salary for worker in self.workers])
        if total_workers_salary < self.__budget:
            self.__budget -= total_workers_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        money_for_animal_care = sum([animal.money_for_care for animal in self.animals])
        if money_for_animal_care < self.__budget:
            self.__budget -= money_for_animal_care
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = f'You have {len(self.animals)} animals\n'

        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)
        
        message += f'----- {len(lions)} Lions:\n'
        for lion in lions:
            message += lion.__repr__() + '\n'
        
        message += f'----- {len(tigers)} Tigers:\n'
        for tiger in tigers:
            message += tiger.__repr__() + '\n'
        
        message += f'----- {len(cheetahs)} Cheetahs:'
        for cheetah in cheetahs:
            message += '\n' + cheetah.__repr__()

        return message

    def workers_status(self):
        message = f'You have {len(self.workers)} workers\n'

        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)
        
        message += f'----- {len(keepers)} Keepers:\n'
        for keeper in keepers:
            message += keeper.__repr__() + '\n'
        
        message += f'----- {len(caretakers)} Caretakers:\n'
        for caretaker in caretakers:
            message += caretaker.__repr__() + '\n'

        message += f'----- {len(vets)} Vets:'
        for vet in vets:
            message += '\n' + vet.__repr__()
        
        return message


if __name__ == '__main__':
    zoo = Zoo("Zootopia", 3000, 5, 8)

    # Animals creation
    animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

    # Animal prices
    prices = [200, 190, 204, 156, 211, 140]

    # Workers creation
    workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

    # Adding all animals
    for i in range(len(animals)):
        animal = animals[i]
        price = prices[i]
        print(zoo.add_animal(animal, price))

    # Adding all workers
    for worker in workers:
        print(zoo.hire_worker(worker))

    # Tending animals
    print(zoo.tend_animals())

    # Paying keepers
    print(zoo.pay_workers())

    # Fireing worker
    print(zoo.fire_worker("Adam"))

    # Printing statuses
    print(zoo.animals_status())
    print(zoo.workers_status())
