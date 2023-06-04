from unittest import TestCase, main
from OOP.TestingExercises.student.project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Jorj')

    def test_correct_init(self):
        self.assertEqual('Jorj', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_course_already_added(self):
        self.student.courses = {'one': []}
        result = self.student.enroll('one', [1, 2], '')
        self.assertEqual([1, 2], self.student.courses['one'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_notes_y(self):
        result = self.student.enroll('one', [1, 2], 'Y')
        self.assertEqual([1, 2], self.student.courses['one'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_notes_whitespace(self):
        result = self.student.enroll('one', [1, 2], '')
        self.assertEqual([1, 2], self.student.courses['one'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_only_course(self):
        result = self.student.enroll('one', [1, 2], 'a')
        self.assertEqual([], self.student.courses['one'])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('one', [1, 2])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_correct(self):
        self.student.courses = {'one': [1, 2]}
        result = self.student.add_notes('one', 3)
        self.assertEqual([1, 2, 3], self.student.courses['one'])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('one')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_correct(self):
        self.student.courses = {'one': [1, 2]}
        result = self.student.leave_course('one')
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == '__main__':
    main()
