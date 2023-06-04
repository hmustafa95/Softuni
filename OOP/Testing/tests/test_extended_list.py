from unittest import TestCase, main
from OOP.Testing.tasks.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList('a', True, 1, 2, 3, 'T')

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('e')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_correct(self):
        result = self.integer_list.add(4)
        self.assertEqual([1, 2, 3, 4], result)
        self.assertEqual([1, 2, 3, 4], self.integer_list._IntegerList__data)

    def test_remove_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index(self):
        result = self.integer_list.remove_index(1)
        self.assertEqual([1, 3], self.integer_list._IntegerList__data)
        self.assertNotIn(result, self.integer_list._IntegerList__data)

    def test_get_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct(self):
        self.assertEqual(2, self.integer_list.get(1))

    def test_insert_incorrect_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(5, 5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_incorrect_value(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 'e')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct(self):
        self.integer_list.insert(1, 4)
        self.assertEqual([1, 4, 2, 3], self.integer_list._IntegerList__data)

    def test_get_biggest(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.integer_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
