import sys, os
sys.path.insert(0, os.getcwd())
from lab03_multiple_inheritance.project.employee import Employee
from lab03_multiple_inheritance.project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
