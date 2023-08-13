from horse_specification.appaloosa import Appaloosa
from horse_specification.thoroughbred import Thoroughbred
from horse_race import HorseRace
from jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horses = ["Appaloosa", "Thoroughbred"]
        if horse_type in valid_horses:
            if self.horses:
                for horse in self.horses:
                    if horse.name == horse_name:
                        raise Exception(f"Horse {horse_name} has been already added!")

            if horse_type == valid_horses[0]:
                horse = Appaloosa(horse_name, horse_speed)
                self.horses.append(horse)
                return f"{horse_type} horse {horse_name} is added."

            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = Jockey(jockey_name, age)
        if self.jockeys:
            for jock in self.jockeys:
                if jock.name == jockey_name:
                    raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        horse_race = HorseRace(race_type)
        if self.horse_races:
            for race in self.horse_races:
                if race.race_type == race_type:
                    raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = next(filter(lambda x: x.__class__.__name__ == horse_type, reversed(self.horses)))
        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if not horse.is_taken and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.take_horse(horse)
        horse.take_horse()
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            race = next(filter(lambda x: x.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if not jockey.race_assignment:
            jockey.race_assignment = race.race_type
            return f"Jockey {jockey_name} added to the {race_type} race."

        return f"Jockey {jockey_name} has been already added to the {jockey.race_assignment} race."

    def start_horse_race(self, race_type: str):
        try:
            race = next(filter(lambda x: x.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        jockeys_in_race = []
        for jockey in self.jockeys:
            if jockey.race_assignment == race_type:
                jockeys_in_race.append(jockey)

        if len(jockeys_in_race) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey = ''
        speed = 0
        for jock in jockeys_in_race:
            if jock.horse.speed > speed:
                speed = jock.horse.speed
                winner_jockey = jock

        return f"The winner of the {race_type} race, with a speed of {speed}km/h is {winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}."
