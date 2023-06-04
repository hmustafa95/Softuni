from unittest import TestCase, main
from OOP.Testing.tasks.worker import Worker


class WorkerTest(TestCase):
    def setUp(self):
        self.worker = Worker('Jorj', 1000, 10)

    def test_correct_init(self):
        self.assertEqual('Jorj', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_correct_money_and_energy(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)
        self.assertEqual(9, self.worker.energy)

    def test_rest_energy_gain(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_get_info(self):
        self.assertEqual('Jorj has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()