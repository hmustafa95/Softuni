from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError

    @abstractmethod
    def calculate_perimeter(self):
        raise NotImplementedError

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return
