import sys, os
import unittest
sys.path.insert(0, os.getcwd())

from exercises.mammal.project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('kuche', 'cat', 'mooou')
    
    def test_mammal_init_method_initialize_correct(self):
        self.assertEqual(self.mammal.name, 'kuche')
        self.assertEqual(self.mammal.type, 'cat')
        self.assertEqual(self.mammal.sound, 'mooou')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')
    
    def test_mammal_method_make_sound_should_return_correct_string(self):
        self.assertEqual(self.mammal.make_sound(), 'kuche makes mooou')

    def test_mammal_get_kingdom_method(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_mammal_info(self):
        self.assertEqual(self.mammal.info(), 'kuche is of type cat')


if __name__ == '__main__':
    unittest.main()
