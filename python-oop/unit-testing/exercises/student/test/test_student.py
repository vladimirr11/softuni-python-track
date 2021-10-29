# import sys, os
# from unittest import result
# sys.path.insert(0, os.getcwd())

# from exercises.student.project.student import Student
from project.student import Student

import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('Vladi', courses={'Python': ['Note']})

    def test_student_init_method_when_no_courses(self):
        student = Student('Vladi')

        self.assertEqual(student.courses, {})
        self.assertEqual(student.name, 'Vladi')
    
    def test_student_init_method_when_courses_specified(self):
        courses = {'Python': ['Note']}

        self.assertEqual(self.student.courses, courses)
        self.assertEqual(self.student.name, 'Vladi')

    def test_student_enroll_method_when_course_already_enrolled(self):
        course_name = 'Python'
        notes = ['Note1', 'Note2']

        student = Student('Vladi', courses={'Python': []})
        result = student.enroll(course_name, notes=notes)
        expected_result = 'Course already added. Notes have been updated.'

        self.assertEqual(result, expected_result)
    
    def test_student_enroll_method_when_course_add_course_notes(self):
        student = Student('Vladi', courses={'Python': []})

        course_name = 'C++'
        notes = ['Note']
        add_course_notes = 'Y'

        result = student.enroll(course_name, notes=notes, add_course_notes=add_course_notes)

        expected_result = 'Course and course notes have been added.'

        self.assertEqual(result, expected_result)
    
    def test_student_enroll_method_when_course_not_enrolled_and_not_add_courses_argument(self):
        course_name = 'C++'

        student = Student('Vladi')
        notes = ['Note']

        result = student.enroll(course_name, notes=notes, add_course_notes='N')
        expected_result = 'Course has been added.'

        self.assertEqual(result, expected_result)

    def test_student_add_notes_methods_when_course_in_list(self):
        result = self.student.add_notes('Python', 'Note2')
        expected_result = 'Notes have been updated'

        self.assertEqual(result, expected_result)
    
    def test_student_add_notes_method_when_course_not_in_list(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('C++', 'Note')
        
        self.assertIsNotNone(ex.exception)

    def test_student_leave_course_method_when_course_enrolled(self):
        result = self.student.leave_course('Python')
        expected_result = 'Course has been removed'

        self.assertEqual(result, expected_result)

    def test_student_leave_course_method_when_course_not_enrolled(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('C++')
        
        self.assertIsNotNone(ex.exception)


if __name__== '__main__':
    unittest.main()
