from unittest import TestCase, main
from OOP.TestingExercises.vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100.5, 150.1)

    def test_correct_init(self):
        self.assertEqual(100.5, self.vehicle.fuel)
        self.assertEqual(100.5, self.vehicle.capacity)
        self.assertEqual(150.1, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correct(self):
        self.vehicle.drive(1)
        self.assertEqual(99.25, self.vehicle.fuel)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correct(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(10)
        self.assertEqual(20, self.vehicle.fuel)

    def test_str_call(self):
        self.assertEqual("The vehicle has 150.1 " + \
                         "horse power with 100.5 fuel left and 1.25 " + \
                         "fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    main()
