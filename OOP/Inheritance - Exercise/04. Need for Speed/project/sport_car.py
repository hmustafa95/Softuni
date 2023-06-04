from car import Car

class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        driving = kilometers * self.fuel_consumption
        if driving <= self.fuel:
            self.fuel -= driving