from Python_OOP.exam_prep_first.unit_test.project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(10)

    def test_books_limit_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_len_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 3, 'b': 2}
        self.assertEqual(5, len(self.bookstore))

    def test_receive_book_books_limit_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('a', 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 1}
        result = self.bookstore.receive_book('a', 4)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles['a'])
        self.assertEqual("5 copies of a are available in the bookstore.", result)

    def test_sell_book_not_in_titles_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('a', 1)
        self.assertEqual("Book a doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_copies_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 1}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('a', 3)
        self.assertEqual("a has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 5}
        result = self.bookstore.sell_book('a', 1)
        self.assertEqual(4, self.bookstore.availability_in_store_by_book_titles['a'])
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual("Sold 1 copies of a", result)

    def test_str_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 5}
        self.bookstore._Bookstore__total_sold_books = 3
        result = str(self.bookstore)
        self.assertEqual('Total sold books: 3\nCurrent availability: 5\n - a: 5 copies', result)


if __name__ == '__main__':
    main()
