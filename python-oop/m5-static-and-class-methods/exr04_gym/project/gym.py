import sys, os
sys.path.insert(0, os.getcwd())

from exr04_gym.project.customer import Customer
from exr04_gym.project.equipment import Equipment
from exr04_gym.project.exercise_plan import ExercisePlan
from exr04_gym.project.trainer import Trainer
from exr04_gym.project.subscription import Subscription


class Gym:
    def __init__(self) -> None:
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription: Subscription = list(filter(lambda s: s.id == subscription_id, self.subscriptions))[0]
        
        customer_id = subscription.customer_id
        trainer_id = subscription.trainer_id
        plan_id = subscription.exercise_id
        
        customer: Customer = list(filter(lambda c: c.id == customer_id, self.customers))[0]
        trainer: Trainer = list(filter(lambda t: t.id == trainer_id, self.trainers))[0]
        plan: ExercisePlan = list(filter(lambda p: p.id == plan_id, self.plans))[0]
        
        equipment_id = plan.equipment_id

        equipment: Equipment = list(filter(lambda e: e.id == equipment_id, self.equipment))[0]

        message = subscription.__repr__()
        message += '\n' + customer.__repr__()
        message += '\n' + trainer.__repr__()
        message += '\n' + equipment.__repr__()
        message += '\n' + plan.__repr__()

        return message


if __name__ == '__main__':
    customer = Customer('John', 'Maple Street', 'john.smith@gmail.com')

    equipment = Equipment('Treadmill')

    trainer = Trainer('Peter')

    subscription = Subscription('14.05.2020', 1, 1, 1)

    plan = ExercisePlan(1, 1, 20)

    gym = Gym()

    gym.add_customer(customer)
    gym.add_equipment(equipment)
    gym.add_trainer(trainer)
    gym.add_plan(plan)
    gym.add_subscription(subscription)

    print(Customer.get_next_id())
    print(gym.subscription_info(1))
