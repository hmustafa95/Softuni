from unittest import TestCase, main
from OOP.Testing.tasks.car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'Prius', 5, 50)

    def test_correct_init(self):
        self.assertEqual('Toyota', self.car.make)
        self.assertEqual('Prius', self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_cons_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_cap_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_correct(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_overload(self):
        self.car.refuel(100)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_correct(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(45, self.car.fuel_amount)


if __name__ == '__main__':
    main()
