from animal import Bird


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.wing_size = wing_size
        self.food_eaten = food_eaten

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Owl does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Owl [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.wing_size = wing_size
        self.food_eaten = food_eaten

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Hen [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
