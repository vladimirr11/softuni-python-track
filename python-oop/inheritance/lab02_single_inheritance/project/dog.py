import sys
import os
sys.path.insert(0, os.getcwd())

from lab02_single_inheritance.project.animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking...'
