from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_types = ["MuscleCar", "SportsCar"]
        if car_type in valid_types:
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")
            if car_type == valid_types[0]:
                self.cars.append(MuscleCar(model, speed_limit))
                return f"{car_type} {model} is created."
            else:
                self.cars.append(SportsCar(model, speed_limit))
                return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            car = next(filter(lambda x: x.__class__.__name__ == car_type, self.cars), reversed)
        except StopIteration:
            raise Exception(f"Car {car_type} could not be found!")

        if not car.is_taken and driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."

        if not car.is_taken and not driver.car:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = next(filter(lambda x: x.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = next(filter(lambda x: x.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        result = []
        for current_winner in winners[0:3]:
            current_winner.number_of_wins += 1
            result.append(f"Driver {current_winner.name} wins the {race_name} race with a speed of {current_winner.car.speed_limit}.")
        return '\n'.join(result)
