import sys, os
sys.path.insert(0, os.getcwd())

from lab.car_manager import Car

import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car('Unknown', '101', 5, 50)
    
    def test_car_init_method_initialize_correct(self):
        self.assertEqual(self.car.make, 'Unknown')
        self.assertEqual(self.car.model, '101')
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)
    
    def test_car_method_make_setter_when_value_supplied(self):
        self.car.make = 'New Make'
        self.assertEqual(self.car.make, 'New Make')
    
    def test_car_method_make_setter_when_value_not_supplied_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_car_method_model_setter_when_value_supplied(self):
        self.car.model = 'New Model'
        self.assertEqual(self.car.model, 'New Model')
    
    def test_car_method_model_setter_when_value_not_supplied_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_car_method_fuel_consumption_setter_when_value_supplied(self):
        self.car.fuel_consumption = 6
        self.assertEqual(self.car.fuel_consumption, 6)
    
    def test_car_method_fuel_consumption_setter_when_value_less_than_zero_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        
        self.assertIsNotNone(str(ex.exception))

    def test_car_method_fuel_capacity_setter_when_value_supplied(self):
        self.car.fuel_capacity = 60
        self.assertEqual(self.car.fuel_capacity, 60)
    
    def test_car_method_fuel_capacity_setter_when_value_less_than_zero_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_car_method_fuel_amount_setter_when_value_supplied(self):
        self.car.fuel_amount = 1
        self.assertEqual(self.car.fuel_amount, 1)
    
    def test_car_method_fuel_amount_setter_when_value_less_than_zero_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_car_method_refuel_when_negative_value_supplied_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-7)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_car_method_refuel_when_value_plus_current_amount_below_fuel_capacity(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)
    
    def test_car_method_refuel_when_value_plus_current_amount_above_fuel_capacity(self):
        self.car.refuel(60)
        self.assertEqual(self.car.fuel_amount, 50)
    
    def test_car_method_drive_when_fuel_not_enough_for_supplied_distance_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_car_method_drive_when_fuel_enough_for_supplied_distance_should_decrease_fuel_amount(self):
        self.car.fuel_amount = 20
        self.car.drive(3)

        self.assertEqual(self.car.fuel_amount, 19.85)


if __name__ == '__main__':
    unittest.main()
