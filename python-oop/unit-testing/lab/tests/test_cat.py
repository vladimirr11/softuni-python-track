import sys, os
sys.path.insert(0, os.getcwd())

from lab.cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('kuche')
    
    def test_cat_size_increase_when_eat(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)
    
    def test_cat_is_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
    
    def test_cat_cannot_eat_after_fed_should_raises(self):
        cat = Cat('chocho')
        cat.fed = True
        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertIsNotNone(ex.exception)

    def test_cat_cannot_fall_asleep_when_fungry_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        
        self.assertIsNotNone(ex.exception)

    def test_cat_not_sleepy_after_sleep(self):
        cat = Cat('chocho')

        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
