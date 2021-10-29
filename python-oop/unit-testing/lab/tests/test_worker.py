import sys, os
sys.path.insert(0, os.getcwd())

from lab.worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Ivan', 1000, 40)
    
    def test_worker_init_attributes_properly_initialized(self):
        self.assertEqual(self.worker.name, 'Ivan')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 40)
        self.assertEqual(self.worker.money, 0)
    
    def test_worker_energy_is_incremented_after_rest_method_called(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 41)
    
    def test_worker_tries_work_with_zero_energy_should_raises(self):
        worker = Worker('Ivan', 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual(str(ex.exception), 'Not enough energy.')
    
    def test_worker_tries_work_with_negetive_energy_should_raises(self):
        worker = Worker('Ivan', 1000, -5)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual(str(ex.exception), 'Not enough energy.')
    
    def test_worker_money_increased_when_worked(self):
        self.worker.work()
        self.assertEqual(self.worker.money + self.worker.salary, 2000)

    def test_worker_energy_is_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 39)
    
    def test_worker_get_info_method_returns_correct_string(self):
        expected_result = 'Ivan has saved 0 money.'
        self.assertEqual(self.worker.get_info(), expected_result)


if __name__ == '__main__':
    unittest.main()
