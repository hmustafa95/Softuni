from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team('Best')

    def test_correct_init(self):
        self.team.members = {'Player': 10}
        self.assertEqual('Best', self.team.name)
        self.assertEqual({'Player': 10}, self.team.members)

    def test_name_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = '1'
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_name_setter_correct(self):
        self.team.name = 'Horse'
        self.assertEqual('Horse', self.team.name)

    def test_add_member(self):
        result = self.team.add_member(john=10, mark=20)
        self.assertEqual('Successfully added: john, mark', result)
        self.assertEqual({'john': 10, 'mark': 20}, self.team.members)

    def test_remove_member_success(self):
        self.team.members = {'Player': 10}
        result = self.team.remove_member('Player')
        self.assertEqual('Member Player removed', result)
        self.assertEqual({}, self.team.members)

    def test_remove_member_fail(self):
        result = self.team.remove_member('Player')
        self.assertEqual("Member with name Player does not exist", result)

    def test_correct_gt(self):
        self.team.members = {'Player': 10, 'OPlayer': 20}
        other = Team('Yes')
        other.members = {'Clayer': 11}
        result = self.team.__gt__(other)
        self.assertEqual(True, result)

    def test_incorrect_gt(self):
        self.team.members = {'Clayer': 11}
        other = Team('Yes')
        other.members = {'Player': 10, 'OPlayer': 20}
        result = self.team.__gt__(other)
        self.assertEqual(False, result)

    def test_len(self):
        result = len(self.team.members)
        self.assertEqual(0, result)

    def test_add(self):
        other = Team('Yes')
        self.team.members = {'Player': 10, 'OPlayer': 20}
        other.members = {'Clayer': 11}
        result = self.team.__add__(other)
        smth = result
        self.assertEqual(smth, result)
        self.assertEqual({'Player': 10, 'OPlayer': 20, 'Clayer': 11}, result.members)
        self.assertEqual('BestYes', result.name)

    def test_str(self):
        self.team.members = {'Player': 10, 'OPlayer': 20}
        result = str(self.team)
        self.assertEqual('Team name: Best\nMember: OPlayer - 20-years old\nMember: Player - 10-years old', result)


if __name__ == '__main__':
    main()
