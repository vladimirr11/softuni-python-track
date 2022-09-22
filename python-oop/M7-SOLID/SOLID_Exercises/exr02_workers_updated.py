from abc import ABCMeta, abstractmethod
import time


class Workable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass


class Eatable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def eat(self):
        pass


class AbstractWorker(Workable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass


class Worker(AbstractWorker, Eatable):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker, Eatable):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if 'AbstractWorker' in [w.__name__ for w in worker.__class__.__mro__]:
            self.worker = worker
        else:
            raise AssertionError(
                '`worker` must be of type {}'.format(AbstractWorker))


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker):
    def work(self):
        print("I'm a robot. I'm working....")


if __name__ == '__main__':
    work_manager = WorkManager()
    break_manager = BreakManager()

    work_manager.set_worker(Worker())
    break_manager.set_worker(Worker())
    work_manager.manage()
    break_manager.lunch_break()
    work_manager.set_worker(SuperWorker())
    break_manager.set_worker(SuperWorker())
    work_manager.manage()
    break_manager.lunch_break()
    work_manager.set_worker(Robot())
    work_manager.manage()

    try:
        break_manager.set_worker(Robot())
        break_manager.lunch_break()
    except:
        pass
