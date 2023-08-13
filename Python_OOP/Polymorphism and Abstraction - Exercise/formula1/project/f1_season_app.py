from formula_teams.mercedes_team import MercedesTeam
from formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self, red_bull_team: RedBullTeam = None, mercedes_team: MercedesTeam = None):
        self.red_bull_team = red_bull_team
        self.mercedes_team = mercedes_team

    def register_team_for_season(self, team_name: str, budget: int):
        valid_names = ["Red Bull", "Mercedes"]
        if team_name not in valid_names:
            raise ValueError("Invalid team name!")
        if team_name == valid_names[0]:
            self.red_bull_team = RedBullTeam(budget)
            return "Red Bull has joined the new F1 season."
        if team_name == valid_names[1]:
            self.mercedes_team = MercedesTeam(budget)
            return "Mercedes has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        if red_bull_pos < mercedes_pos:
            return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. " + \
                   f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. " + \
                   f"Red Bull is ahead at the {race_name} race."

        if red_bull_pos > mercedes_pos:
            return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. " + \
                   f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. " + \
                   f"Mercedes is ahead at the {race_name} race."
