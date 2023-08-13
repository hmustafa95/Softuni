from formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
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
            sponsor_reward += 1520000
        elif race_pos == 2:
            sponsor_reward += 820000
        elif 3 <= race_pos <= 8:
            sponsor_reward += 20000
        elif 9 <= race_pos <= 10:
            sponsor_reward += 10000

        sponsor_reward -= 250000
        self.__budget += sponsor_reward
        return f"The revenue after the race is {sponsor_reward}$. Current budget {self.__budget}$"
