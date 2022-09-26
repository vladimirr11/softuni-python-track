import sys, os
import unittest
sys.path.insert(0, os.getcwd())
from exercises.vehicle.project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    default_fc = 1.25

    def setUp(self):
        self.vehicle = Vehicle(50, 163)

    def test_vehicle_init_method_initialize_correctly(self):
        fuel = 50
        hp = 163

        self.assertEqual(self.vehicle.fuel, fuel)
        self.assertEqual(self.vehicle.capacity, fuel)
        self.assertEqual(self.vehicle.horse_power, hp)
        self.assertEqual(self.vehicle.fuel_consumption, TestVehicle.default_fc)
    
    def test_vehicle_drive_method_when_fuel_enough(self):
        needed_fuel = self.vehicle.fuel - (self.vehicle.fuel_consumption * 10)
        self.vehicle.drive(10)

        self.assertEqual(self.vehicle.fuel, needed_fuel)
    
    def test_vehicle_method_drive_when_fuel_not_enough_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_vehicle_refuel_method_when_fuel_amount_not_exceed_fuel_capacity(self):
        self.vehicle.fuel -= 20
        self.vehicle.refuel(10)

        self.assertEqual(self.vehicle.fuel, 40)

    def test_vehicle_refuel_method_when_fuel_amount_exceed_fuel_capacity_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_vehicle_str_method(self):
        target = f"The vehicle has 163 " \
               f"horse power with 50 fuel left and 1.25 fuel consumption"
        
        self.assertEqual(str(self.vehicle), target)


if __name__ == '__main__':
    unittest.main()
