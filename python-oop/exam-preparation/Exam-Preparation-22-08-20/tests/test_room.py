import sys, os
sys.path.insert(0, os.getcwd())

from project.rooms.room import Room

import unittest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(name='Patersson', budget=1000, members_count=2)
    
    def test_room_init_method(self):
        self.assertEqual(self.room.family_name, 'Patersson')
        self.assertEqual(self.room.budget, 1000)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_room_expenses_setter_when_value_below_zero_should_raises(self):
        with self.assertRaises(Exception) as ex:
            self.room.expenses = -4
        
        self.assertIsNotNone(str(ex.exception))
    
    def test_room_expenses_setter_when_valid_value_passed(self):
        self.room.expenses = 30

        self.assertEqual(self.room.expenses, 30)
    

if __name__ == '__main__':
    unittest.main()
