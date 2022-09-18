import sys, os
sys.path.insert(0, os.getcwd())
from lab05_hierarchical_inheritance.project.animal import Animal


class Cat(Animal):
    def meow(self):
        return 'meowing...'
