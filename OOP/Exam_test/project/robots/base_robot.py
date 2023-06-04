from abc import ABC, abstractmethod


class BaseRobot(ABC):
    @abstractmethod
    def __init__(self, name: str, kind: str, price: float):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise "Robot name cannot be empty!"
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if value == '':
            raise "Robot kind cannot be empty!"
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise "Robot price cannot be less than or equal to 0.0!"
        self.__price = value

    @abstractmethod
    def eating(self):
        pass
