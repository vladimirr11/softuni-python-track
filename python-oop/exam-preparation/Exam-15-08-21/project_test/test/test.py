import sys, os
sys.path.insert(0, os.getcwd())


from project.pet_shop import PetShop

import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.pet_shop = PetShop('PetShop')

    def test_petshop_init_method(self):
        self.assertEqual(self.pet_shop.name, 'PetShop')
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])
    
    def test_petshop_add_food_method_when_quantity_zero_should_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('food', 0)
        
        self.assertTrue(str(ex.exception))

    def test_petshop_add_food_method_when_quantity_below_zero_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_food('food', -7)
        
        self.assertIsNotNone(str(ex.exception))

    def test_petshop_add_food_method(self):
        self.pet_shop.add_food('food', 10)
        
        self.assertEqual(self.pet_shop.food, {'food': 10})

    def test_pethshop_add_food_method_when_food_in_list(self):
        self.pet_shop.add_food('food', 10)
        self.pet_shop.add_food('food', 110)

        self.assertEqual(self.pet_shop.food, {'food': 120})

    def test_petshop_add_food_method_return_massage(self):
        result = self.pet_shop.add_food('food', 10)
        expected_result = f'Successfully added 10.00 grams of food.'
        
        self.assertEqual(result, expected_result)
    
    def test_pethsop_add_pet_method_when_pet_already_in_list_should_raises(self):
        self.pet_shop.add_pet('Rusty')
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('Rusty')
        
        # self.assertIsNotNone(str(ex.exception))
        self.assertEqual(str(ex.exception), 'Cannot add a pet with the same name')
    
    def test_pethsop_add_pet_method(self):
        self.pet_shop.add_pet('Rusty')
        
        self.assertEqual(self.pet_shop.pets[0], 'Rusty')
    
    def test_pethsop_add_pet_method_return_massage(self):
        result = self.pet_shop.add_pet('Rusty')
        expected_result = f'Successfully added Rusty.'

        self.assertEqual(self.pet_shop.pets[0], 'Rusty')
        self.assertEqual(result, expected_result)
    
    def test_petshop_feed_pet_method_when_pet_not_in_list_should_raises(self):
        self.pet_shop.add_pet('Jupyter')
        self.pet_shop.add_food('pulneny chushki', 100)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('pulneny chushki', 'Rusty')
        
        # self.assertIsNotNone(str(ex.exception))
        self.assertEqual(str(ex.exception), 'Please insert a valid pet name')

    def test_petshop_feed_pet_method_when_food_non_in_list(self):
        self.pet_shop.add_pet('Rusty')
        self.pet_shop.add_food('pulneny chushki', 100)

        result = self.pet_shop.feed_pet('chushki', 'Rusty')
        expected_result = f'You do not have chushki'

        self.assertEqual(result, expected_result)
    
    def test_petshop_feed_pet_method_when_food_below_100(self):
        self.pet_shop.add_pet('Rusty')
        self.pet_shop.add_food('pulneny chushki', 10)

        result = self.pet_shop.feed_pet('pulneny chushki', 'Rusty')
        expected_result = f'Adding food...'

        self.assertEqual(self.pet_shop.food['pulneny chushki'], 1010)
        self.assertEqual(result, expected_result)

    def test_petshop_feed_pet_method_when_food_above_100(self):
        self.pet_shop.add_pet('Rusty')
        self.pet_shop.add_food('pulneny chushki', 200)

        result = self.pet_shop.feed_pet('pulneny chushki', 'Rusty')
        expected_result = f'Rusty was successfully fed'

        self.assertEqual(self.pet_shop.food['pulneny chushki'], 100)
        self.assertEqual(result, expected_result)
    
    def test_petshop_repr_method(self):
        self.pet_shop.add_pet('Rusty')
        result = self.pet_shop.__repr__()
        expected_result = f'Shop PetShop:\nPets: Rusty'

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
