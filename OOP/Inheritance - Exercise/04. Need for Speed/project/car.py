from vehicle import Vehicle

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        driving = kilometers * self.fuel_consumption
        if driving <= self.fuel:
            self.fuel -= driving
