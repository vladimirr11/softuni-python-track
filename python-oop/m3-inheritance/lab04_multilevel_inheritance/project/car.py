import sys, os
sys.path.insert(0, os.getcwd())
from lab04_multilevel_inheritance.project.vehicle import Vehicle


class Car(Vehicle):
    def drive(self):
        return 'driving...'
