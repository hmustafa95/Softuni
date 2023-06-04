from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        result = 0
        for decoration in self.decorations:
            result += decoration.comfort
        return result

    def add_fish(self, fish):
        if fish.__class__.__name__ in ['FreshwaterFish', 'SaltwaterFish']:
            if len(self.fish) + 1 < self.capacity:
                self.fish.append(fish)
                return f"Successfully added {fish.__class__.__name__} to {self.name}."
            return "Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f'{self.name}:']
        fishes_list = ['Fish:']
        if self.fish:
            for fish in self.fish:
                fishes_list.append(fish.name)
        else:
            fishes_list.append('none')
        result.append(' '.join(fishes_list))
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")
        return '\n'.join(result)
