from OOP.exam_preparation_second.bakedfood.test.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.petshop = PetShop('Moo-moo')
        self.petshop.food = {'Granules': 100}
        self.petshop.pets = ['Kitten']

    def test_correct_init(self):
        self.assertEqual('Moo-moo', self.petshop.name)
        self.assertEqual({'Granules': 100}, self.petshop.food)
        self.assertEqual(['Kitten'], self.petshop.pets)

    def test_add_food_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.petshop.add_food('pouch', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_correct(self):
        result = self.petshop.add_food('Granules', 10.5)
        self.assertEqual({'Granules': 110.5}, self.petshop.food)
        self.assertEqual("Successfully added 10.50 grams of Granules.", result)

    def test_add_food_correct_new_food(self):
        result = self.petshop.add_food('Pouch', 10)
        self.assertEqual({'Granules': 100, 'Pouch': 10}, self.petshop.food)
        self.assertEqual("Successfully added 10.00 grams of Pouch.", result)

    def test_add_pet_exception(self):
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet('Kitten')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_correct(self):
        result = self.petshop.add_pet('Doggy')
        self.assertEqual(['Kitten', 'Doggy'], self.petshop.pets)
        self.assertEqual("Successfully added Doggy.", result)

    def test_feed_pet_exception(self):
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet('Granules', 'Doggy')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_missing(self):
        result = self.petshop.feed_pet('Pouch', 'Kitten')
        self.assertEqual('You do not have Pouch', result)

    def test_feed_pet_food_under_100(self):
        self.petshop.food['Granules'] = 90
        result = self.petshop.feed_pet('Granules', 'Kitten')
        self.assertEqual(1090.00, self.petshop.food['Granules'])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_correct(self):
        result = self.petshop.feed_pet('Granules', 'Kitten')
        self.assertEqual(0.00, self.petshop.food['Granules'])
        self.assertEqual("Kitten was successfully fed", result)

    def test_repr(self):
        self.assertEqual('Shop Moo-moo:\nPets: Kitten', str(self.petshop))


if __name__ == '__main__':
    main()
