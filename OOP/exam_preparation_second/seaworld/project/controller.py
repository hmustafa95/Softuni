from aquarium.freshwater_aquarium import FreshwaterAquarium
from aquarium.saltwater_aquarium import SaltwaterAquarium
from decoration.decoration_repository import DecorationRepository
from decoration.plant import Plant
from decoration.ornament import Ornament
from fish.freshwater_fish import FreshwaterFish
from fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."
        if aquarium_type == valid_aquariums[0]:
            new_aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."
        new_aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_decorations = ['Ornament', 'Plant']
        if decoration_type not in valid_decorations:
            return "Invalid decoration type."
        if decoration_type == valid_decorations[0]:
            new_decoration = Ornament()
            self.decorations_repository.add(new_decoration)
            return f"Successfully added {decoration_type}."
        new_decoration = Plant()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ['FreshwaterFish', 'SaltwaterFish']
        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                if fish_type == valid_fish_types[0] and aquarium.__class__.__name__ == 'FreshwaterAquarium':
                    new_fish = FreshwaterFish(fish_name, fish_species, price)
                    aquarium.add_fish(new_fish)
                elif fish_type == valid_fish_types[1] and aquarium.__class__.__name__ == 'SaltwaterAquarium':
                    new_fish = SaltwaterFish(fish_name, fish_species, price)
                    aquarium.add_fish(new_fish)
                else:
                    return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        fed_fishes = 0
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for fish in aquarium.fish:
                    fed_fishes += 1
                    fish.eat()
        return f"Fish fed: {fed_fishes}"

    def calculate_value(self, aquarium_name: str):
        decorations = 0
        fishes = 0
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for fish in aquarium.fish:
                    fishes += fish.price
                for decoration in aquarium.decorations:
                    decorations += decoration.price
        result = decorations + fishes
        return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return '\n'.join(result)
