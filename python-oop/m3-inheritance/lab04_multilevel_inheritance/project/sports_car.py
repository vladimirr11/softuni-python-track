import sys, os
sys.path.insert(0, os.getcwd())
from lab04_multilevel_inheritance.project.car import Car


class SportsCar(Car):
    def race(self):
        return 'racing...'
