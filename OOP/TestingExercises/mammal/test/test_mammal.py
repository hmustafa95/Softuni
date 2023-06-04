from unittest import TestCase, main
from OOP.TestingExercises.mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Monke', 'Gorilla', 'Meow')

    def test_correct_init(self):
        self.assertEqual('Monke', self.mammal.name)
        self.assertEqual('Gorilla', self.mammal.type)
        self.assertEqual('Meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual('Monke makes Meow', result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual('Monke is of type Gorilla', result)


if __name__ == '__main__':
    main()
