from formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value >= 1000000:
            self.__budget = value
        else:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_reward = 0
        if race_pos == 1:
            sponsor_reward += 1100000
        elif race_pos == 2 or race_pos == 3:
            sponsor_reward += 600000
        elif 4 <= race_pos <= 5:
            sponsor_reward += 100000
        elif 6 <= race_pos <= 7:
            sponsor_reward += 50000

        sponsor_reward -= 200000
        self.__budget += sponsor_reward
        return f"The revenue after the race is {sponsor_reward}$. Current budget {self.__budget}$"
