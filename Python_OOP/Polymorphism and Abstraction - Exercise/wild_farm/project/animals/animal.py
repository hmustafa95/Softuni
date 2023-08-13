from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten


class Bird(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.wing_size = wing_size
        self.food_eaten = food_eaten


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.living_region = living_region
        self.food_eaten = food_eaten
