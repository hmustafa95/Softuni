from unittest import TestCase, main
from OOP.TestingExercises.hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Jekichan', 10, 100.5, 1.5)
        self.enemy = Hero('Donkikong', 10, 100.5, 1.5)

    def test_correct_init(self):
        self.assertEqual('Jekichan', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.5, self.hero.health)
        self.assertEqual(1.5, self.hero.damage)

    def test_battle_self_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_error(self):
        with self.assertRaises(ValueError) as ve:
            self.hero.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_error(self):
        with self.assertRaises(ValueError) as ve:
            self.enemy.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Donkikong. He needs to rest", str(ve.exception))

    def test_battle_correct(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(85.5, self.hero.health)
        self.assertEqual(90.5, self.enemy.health)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(6.5, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_battle_draw(self):
        self.hero.health = 1
        self.enemy.health = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual('Draw', result)

    def test_battle_win(self):
        self.enemy.health = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(90.5, self.hero.health)
        self.assertEqual(6.5, self.hero.damage)
        self.assertEqual('You win', result)

    def test_str(self):
        self.assertEqual("Hero Jekichan: 10 lvl\n" + \
               "Health: 100.5\n" + \
               "Damage: 1.5\n", str(self.hero))


if __name__ == '__main__':
    main()
