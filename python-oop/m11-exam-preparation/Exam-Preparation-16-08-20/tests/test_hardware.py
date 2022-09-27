import sys, os
import unittest
sys.path.insert(0, os.getcwd())

from project.software.software import Software
from project.hardware.hardware import Hardware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hw = Hardware('NVIDIA', 'video card', 4, 4)
    
    def test_hardware_init_method(self):
        self.assertEqual(self.hw.name, 'NVIDIA')
        self.assertEqual(self.hw.type, 'video card')
        self.assertEqual(self.hw.capacity, 4)
        self.assertEqual(self.hw.memory, 4)
    
    def test_install_method_when_capacity_and_memory_not_enough_for_software_should_raises(self):
        sw = Software('Linux', 'os', 5, 4)
        with self.assertRaises(Exception) as ex:
            self.hw.install(sw)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_install_method_when_capacity_and_memory_enough(self):
        sw = Software('Linux', 'os', 4, 4)
        self.hw.install(sw)
        result = self.hw.software_components[0]
        expected = 'Linux'

        self.assertEqual(result.name, expected)
    
    def test_uninstall_method(self):
        sw = Software('Linux', 'os', 4, 4)
        self.hw.install(sw)
        self.hw.uninstall(sw)

        self.assertEqual(self.hw.software_components, [])


if __name__ == '__main__':
    unittest.main()
