from abc import ABC, abstractmethod


class Horse(ABC):
    MAXIMUM_SPEED = 0

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError("Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if value == __class__.MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def take_horse(self):
        if not self.is_taken:
            self.is_taken = True

    @abstractmethod
    def train(self):
        pass
