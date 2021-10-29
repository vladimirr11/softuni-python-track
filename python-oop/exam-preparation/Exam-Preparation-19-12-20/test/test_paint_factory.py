import sys, os
sys.path.insert(0, os.getcwd())

from project.factory.paint_factory import PaintFactory

import unittest


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory('PF', 1000)
    
    def test_paint_factory_init_method(self):
        ingredients = ["white", "yellow", "blue", "green", "red"]
        self.assertEqual(self.paint_factory.name, 'PF')
        self.assertEqual(self.paint_factory.capacity, 1000)
        self.assertEqual(self.paint_factory.valid_ingredients, ingredients)
        self.assertEqual(self.paint_factory.products, {})

    def test_paint_factory_add_ingredient_method_when_igredient_in_list(self):
        collor = 'white'
        self.paint_factory.add_ingredient(collor, 10)
        self.assertEqual(self.paint_factory.ingredients, {'white': 10})
    
    def test_paint_factory_add_igredient_method_when_not_enough_space_should_raises(self):
        collor = 'white'

        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient(collor, 1001)

        self.assertIsNotNone(str(ex.exception))

    def test_paint_factory_add_igredient_method_when_product_not_allowed_should_raises(self):
        collor = 'purple'

        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient(collor, 10)

        self.assertIsNotNone(str(ex.exception))

    def test_paint_factory_remove_ingredient_method_when_product_in_list(self):
        collor = 'white'
        self.paint_factory.add_ingredient(collor, 10)
        self.paint_factory.remove_ingredient(collor, 5)
        self.assertEqual(self.paint_factory.ingredients, {'white': 5})

    def test_paint_factory_remove_ingredient_method_when_product_less_than_zero_should_raises(self):
        collor = 'white'
        self.paint_factory.add_ingredient(collor, 10)
        
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient(collor, 15)
        
        self.assertIsNotNone(str(ex.exception))

    def test_paint_factory_remove_ingredient_method_when_product_not_allowed_should_raises(self):
        collor2 = 'purple'
        collor = 'green'
        self.paint_factory.add_ingredient(collor, 10)
        
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient(collor2, 5)
        
        self.assertIsNotNone(str(ex.exception))


if __name__ == '__main__':
    unittest.main()
        