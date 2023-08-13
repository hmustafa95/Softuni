from animal import Mammal


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.living_region = living_region
        self.food_eaten = food_eaten

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ == 'Vegetable' or food.__class__.__name__ == 'Fruit':
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Mouse does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.living_region = living_region
        self.food_eaten = food_eaten

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Dog does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Dog [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.living_region = living_region
        self.food_eaten = food_eaten

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ == 'Vegetable' or food.__class__.__name__ == 'Meat':
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Cat does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Cat [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.living_region = living_region
        self.food_eaten = food_eaten

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Tiger does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Tiger [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
