from OOP.exam_preparation_second.seaworld.testing.project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('Choo-choo', 20)
        self.train.passengers = ['Mike']

    def test_init_correct(self):
        self.assertEqual('Choo-choo', self.train.name)
        self.assertEqual(20, self.train.capacity)
        self.assertEqual(['Mike'], self.train.passengers)

    def test_add_error_full(self):
        self.train.capacity = 1
        with self.assertRaises(ValueError) as ve:
            self.train.add('George')
        self.assertEqual('Train is full', str(ve.exception))

    def test_add_error_passenger_already_in(self):
        with self.assertRaises(ValueError) as ve:
            self.train.add('Mike')
        self.assertEqual('Passenger Mike Exists', str(ve.exception))

    def test_add_correct(self):
        result = self.train.add('George')
        self.assertEqual(['Mike', 'George'], self.train.passengers)
        self.assertEqual('Added passenger George', result)

    def test_remove_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove('George')
        self.assertEqual('Passenger Not Found', str(ve.exception))

    def test_remove_correct(self):
        result = self.train.remove('Mike')
        self.assertEqual([], self.train.passengers)
        self.assertEqual('Removed Mike', result)


if __name__ == '__main__':
    main()
