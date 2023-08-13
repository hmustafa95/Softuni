from abc import ABC, abstractmethod


class Car(ABC):
    MINIMUM_SPEED_LIMIT = 0
    MAX_SPEED_LIMIT = 1

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError("Model {model} is less than 4 symbols!")
        self.__model = value
    
    @property
    def speed_limit(self):
        return self.__speed_limit
    
    @speed_limit.setter
    def speed_limit(self, value):
        if not self.__class__.MAX_SPEED_LIMIT >= value >= self.__class__.MINIMUM_SPEED_LIMIT:
            raise ValueError("Invalid speed limit! Must be between {min_speed_limit} and {max_speed_limit}!")
        self.__speed_limit = value
