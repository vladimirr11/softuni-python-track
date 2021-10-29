import sys, os
sys.path.insert(0, os.getcwd())

from lab.intiger_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.intiger_list = IntegerList(5, 6, 7)
    
    def test_integer_list_initialize_correctly(self):
        self.assertEqual(self.intiger_list.get_data(), [5, 6, 7])
    
    def test_integer_list_method_add_when_int_supplied_should_add_element_and_returns_list(self):
        self.intiger_list.add(8)
        self.assertEqual(self.intiger_list.get_data(), [5, 6, 7, 8])
    
    def test_integer_list_method_add_when_non_int_supplied_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.intiger_list.add('8')
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_integer_list_method_remove_index_when_correct_index_suplied_should_return_element(self):
        self.intiger_list.remove_index(0)
        self.assertEqual(self.intiger_list.get_data(), [6, 7])
    
    def test_integer_list_method_remove_index_when_incorrect_index_suplied_should_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.intiger_list.remove_index(4)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_integer_list_method_get_when_correct_index_supplied_should_return_element(self):
        self.assertEqual(self.intiger_list.get(1), 6)
    
    def test_integer_list_method_get_when_incorrect_index_supplied_should_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.intiger_list.get(4)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_integer_list_method_insert_when_supplied_index_out_of_range_should_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.intiger_list.insert(4, 4)
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_integer_list_method_insert_when_supplied_element_not_int_should_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.intiger_list.insert(0, '4')
        
        self.assertIsNotNone(str(ex.exception))

    def test_intiger_list_method_get_biggest_returns_correct_element(self):
        self.assertEqual(self.intiger_list.get_biggest(), 7)

    def test_integer_list_method_get_index_when_element_supplied_should_return_the_index(self):
        self.assertEqual(self.intiger_list.get_index(5), 0)


if __name__ == '__main__':
    unittest.main()
